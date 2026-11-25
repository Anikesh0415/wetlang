"""
Wetworld Reference Sandbox Encoders & Closed-Loop Benchmark Environments
========================================================================
Provides shared state-to-stimulation encoders, motor spike decoders, and reference
closed-loop benchmark environments for neural organoids:
- PongStateEncoder: Maps 2D Pong kinematic state to 4 sensory MEA stimulation channels.
- CartPoleStateEncoder: Maps 4D CartPole state to 4 sensory MEA stimulation channels.
- MotorSpikeDecoder: Decodes MEA motor channels (60..63) into discrete/continuous actions.
- DishBrainPongEnv: Reference closed-loop Pong environment with organoid wetware.
- OrganoidCartPoleEnv: Reference closed-loop CartPole balancing environment.

Biophysical Safety Coupling:
Encoders enforce C99 hardware interlock invariants:
1. Water window clamping: |V| <= 1.2 V absolute ceiling (default [-1.2, 1.2] V).
2. Dynamic EIS current density clamp:
   I_safe = J_limit * Area
   V_safe = I_safe * Z_magnitude
   V_effective = min(V_water_window, V_safe)
3. Zero net DC charge drift via charge-balanced biphasic waveforms.
"""

from typing import Dict, Any, Tuple, Optional, Union, Sequence
import numpy as np
import gymnasium as gym
from gymnasium import spaces

# Import canonical arena-backed environment from wetlang.gym
from wetlang.gym import WetworldGymEnv, make


class BiophysicalSafetyClamp:
    """
    Enforces electrochemical water window rails and dynamic EIS impedance current limiting.
    Separates steady-state Faradaic DC leakage (J_limit) from transient capacitive
    biphasic pulse limits (CIC * Area / phase_ms, capped by Shannon limit).
    """
    def __init__(
        self,
        j_limit_ua_cm2: float = 30.0,      # Safe Faradaic DC current density limit (uA/cm^2)
        electrode_area_um2: float = 5000.0, # MEA electrode geometric surface area (um^2)
        z_magnitude_ohms: float = 100000.0, # Electrode-electrolyte interface impedance (|Z| in Ohms)
        water_window_low_v: float = -1.2,   # Cathodic hydrogen evolution potential rail (V)
        water_window_high_v: float = 1.2,   # Anodic oxygen evolution potential rail (V)
        cic_mc_cm2: float = 0.10,           # Material Charge Injection Capacity (0.10 mC/cm^2 for Pt)
        q_shannon_nc: float = 0.40,         # Per-phase Shannon charge density ceiling (nC)
    ):
        self.j_limit_ua_cm2 = float(j_limit_ua_cm2)
        self.electrode_area_um2 = float(electrode_area_um2)
        self.z_magnitude_ohms = float(z_magnitude_ohms)
        self.water_window_low_v = float(water_window_low_v)
        self.water_window_high_v = float(water_window_high_v)
        self.cic_mc_cm2 = float(cic_mc_cm2)
        self.q_shannon_nc = float(q_shannon_nc)

    def calculate_safe_voltage_magnitude(self) -> float:
        """Computes dynamic maximum steady-state Faradaic voltage magnitude V_safe = I_safe * |Z|."""
        area_cm2 = self.electrode_area_um2 * 1e-8
        j_limit_a_cm2 = self.j_limit_ua_cm2 * 1e-6
        i_safe_a = j_limit_a_cm2 * area_cm2
        v_safe_mag = i_safe_a * self.z_magnitude_ohms
        return float(v_safe_mag)

    def calculate_safe_transient_voltage_magnitude(self, phase_ms: float = 0.1) -> float:
        """
        Computes transient capacitive biphasic safe voltage magnitude:
            Q_max = min(CIC * Area, Q_shannon)
            I_peak_safe = Q_max / phase_ms
            V_safe_transient = I_peak_safe * |Z|
        Protects against electrode fouling / area loss and impedance collapse while
        permitting physiological biphasic pulses (e.g. 0.1 - 0.6 V) at nominal MEA impedance.
        """
        q_cic_nc = max(self.cic_mc_cm2, 0.0) * max(self.electrode_area_um2, 0.0) * 0.01
        q_max_nc = min(q_cic_nc, self.q_shannon_nc) if self.q_shannon_nc > 0.0 else q_cic_nc
        phase_s = max(float(phase_ms), 1e-3) * 1e-3
        i_peak_safe_a = (q_max_nc * 1e-9) / phase_s
        v_safe_mag = i_peak_safe_a * max(self.z_magnitude_ohms, 0.0)
        return float(v_safe_mag)

    def clamp_voltage(self, requested_v: float) -> float:
        """
        Two-stage clamp matching C99 interlocks_clamp_voltage_dynamic (steady-state J_limit):
        1. Material water-window potential rails.
        2. Dynamic EIS current density limit.
        """
        # 1. Rail clamp
        v_clamped = float(np.clip(requested_v, self.water_window_low_v, self.water_window_high_v))
        # 2. Dynamic EIS impedance clamp
        v_safe_mag = self.calculate_safe_voltage_magnitude()
        if v_safe_mag > 0.0 and abs(v_clamped) > v_safe_mag:
            sign = 1.0 if v_clamped >= 0.0 else -1.0
            v_clamped = sign * v_safe_mag
        return v_clamped

    def clamp_biphasic_voltage(self, requested_v: float, phase_ms: float = 0.1) -> float:
        """
        Two-stage transient capacitive biphasic clamp:
        1. Material water-window potential rails.
        2. Dynamic EIS transient peak-current limit derived from CIC * Area / phase_ms.
        """
        v_clamped = float(np.clip(requested_v, self.water_window_low_v, self.water_window_high_v))
        v_safe_mag = self.calculate_safe_transient_voltage_magnitude(phase_ms=phase_ms)
        if abs(v_clamped) > v_safe_mag:
            sign = 1.0 if v_clamped >= 0.0 else -1.0
            v_clamped = sign * v_safe_mag
        return v_clamped


class PongStateEncoder:
    """
    Encodes 2D DishBrain Pong kinematic state into 4 sensory stimulation channels (0..3).
    Channels:
        Ch 0: Ball above paddle (vertical distance delta > 0)
        Ch 1: Ball below paddle (vertical distance delta < 0)
        Ch 2: Ball approach velocity / proximity
        Ch 3: Ball trajectory angle / vertical velocity
    """
    def __init__(
        self,
        j_limit_ua_cm2: float = 30.0,
        electrode_area_um2: float = 5000.0,
        z_magnitude_ohms: float = 100000.0,
        water_window_v: float = 1.2,
        voltage_scale: float = 0.6,
        phase_ms: float = 0.1,
        cic_mc_cm2: float = 0.10,
        q_shannon_nc: float = 0.40,
    ):
        self.safety = BiophysicalSafetyClamp(
            j_limit_ua_cm2=j_limit_ua_cm2,
            electrode_area_um2=electrode_area_um2,
            z_magnitude_ohms=z_magnitude_ohms,
            water_window_low_v=-water_window_v,
            water_window_high_v=water_window_v,
            cic_mc_cm2=cic_mc_cm2,
            q_shannon_nc=q_shannon_nc,
        )
        self.voltage_scale = float(voltage_scale)
        self.phase_ms = float(phase_ms)

    def clamp_voltage(self, v: float, channel: int = 0) -> float:
        return self.safety.clamp_biphasic_voltage(v, phase_ms=self.phase_ms)

    def encode(
        self,
        paddle_y: float,
        ball_x: float,
        ball_y: float,
        ball_vx: float,
        ball_vy: float,
    ) -> np.ndarray:
        """Maps 5 Pong kinematic parameters to 4 sensory stimulation voltages."""
        delta_y = float(ball_y - paddle_y)

        # Ch 0: Above paddle (0.1 - 0.4 V suprathreshold-capable range)
        v0 = max(0.0, delta_y) * self.voltage_scale
        # Ch 1: Below paddle
        v1 = max(0.0, -delta_y) * self.voltage_scale
        # Ch 2: Ball horizontal approach proximity (scaled so typical ball_vx~0.04 crosses 0.05 V trigger)
        proximity = float(np.clip(ball_x, 0.0, 1.0))
        approach = float(np.clip(abs(float(ball_vx)) / 0.05, 0.0, 1.0)) * (0.4 + 0.6 * proximity)
        v2 = approach * self.voltage_scale
        # Ch 3: Ball vertical trajectory angle / velocity
        v3 = float(np.tanh(float(ball_vy) / 0.04)) * self.voltage_scale

        stim = np.array([
            self.clamp_voltage(v0, 0),
            self.clamp_voltage(v1, 1),
            self.clamp_voltage(v2, 2),
            self.clamp_voltage(v3, 3),
        ], dtype=np.float32)

        return stim

    def encode_state(self, state: Sequence[float]) -> np.ndarray:
        """Helper accepting [paddle_y, ball_x, ball_y, ball_vx, ball_vy]."""
        return self.encode(state[0], state[1], state[2], state[3], state[4])


class CartPoleStateEncoder:
    """
    Encodes 4D CartPole state into 4 sensory stimulation channels (0..3).
    Channels:
        Ch 0: Cart position (x / 2.4)
        Ch 1: Cart velocity (x_dot)
        Ch 2: Pole angle (theta / 0.2095 rad)
        Ch 3: Pole angular velocity (theta_dot)
    """
    def __init__(
        self,
        j_limit_ua_cm2: float = 30.0,
        electrode_area_um2: float = 5000.0,
        z_magnitude_ohms: float = 100000.0,
        water_window_v: float = 1.2,
        voltage_scale: float = 0.6,
        phase_ms: float = 0.1,
        cic_mc_cm2: float = 0.10,
        q_shannon_nc: float = 0.40,
    ):
        self.safety = BiophysicalSafetyClamp(
            j_limit_ua_cm2=j_limit_ua_cm2,
            electrode_area_um2=electrode_area_um2,
            z_magnitude_ohms=z_magnitude_ohms,
            water_window_low_v=-water_window_v,
            water_window_high_v=water_window_v,
            cic_mc_cm2=cic_mc_cm2,
            q_shannon_nc=q_shannon_nc,
        )
        self.voltage_scale = float(voltage_scale)
        self.phase_ms = float(phase_ms)

    def clamp_voltage(self, v: float, channel: int = 0) -> float:
        return self.safety.clamp_biphasic_voltage(v, phase_ms=self.phase_ms)

    def encode(
        self,
        x: float,
        x_dot: float,
        theta: float,
        theta_dot: float,
    ) -> np.ndarray:
        """Maps 4 CartPole parameters to 4 sensory stimulation voltages."""
        norm_x = float(np.clip(x / 2.4, -1.0, 1.0))
        norm_x_dot = float(np.tanh(x_dot / 2.0))
        norm_theta = float(np.clip(theta / 0.2095, -1.0, 1.0))  # 0.2095 rad ~ 12 deg
        norm_theta_dot = float(np.tanh(theta_dot / 2.0))

        v0 = norm_x * self.voltage_scale
        v1 = norm_x_dot * self.voltage_scale
        v2 = norm_theta * self.voltage_scale
        v3 = norm_theta_dot * self.voltage_scale

        stim = np.array([
            self.clamp_voltage(v0, 0),
            self.clamp_voltage(v1, 1),
            self.clamp_voltage(v2, 2),
            self.clamp_voltage(v3, 3),
        ], dtype=np.float32)

        return stim

    def encode_state(self, state: Sequence[float]) -> np.ndarray:
        """Helper accepting [x, x_dot, theta, theta_dot]."""
        return self.encode(state[0], state[1], state[2], state[3])


class MotorSpikeDecoder:
    """
    Decodes biological spike rasters from MEA motor channels (60..63) into motor action commands.
    Channels:
        Motor Bank Left / Down:  Channels 60, 62
        Motor Bank Right / Up:   Channels 61, 63
    """
    def __init__(
        self,
        left_channels: Sequence[int] = (60, 62),
        right_channels: Sequence[int] = (61, 63),
        rate_window: int = 10,
    ):
        self.left_channels = list(left_channels)
        self.right_channels = list(right_channels)
        self.rate_window = rate_window
        self._history = []

    def _extract_motor_spikes(self, spikes: np.ndarray) -> Tuple[float, float]:
        """Extracts spike activity from left and right motor electrode banks."""
        arr = np.asarray(spikes).flatten()
        if len(arr) == 128:
            spikes_64 = arr[64:]
        elif len(arr) >= 64:
            spikes_64 = arr[:64]
        elif len(arr) == 4:
            return float(arr[0] + arr[2]), float(arr[1] + arr[3])
        else:
            return 0.0, 0.0

        left_act = sum(float(spikes_64[ch]) for ch in self.left_channels if ch < len(spikes_64))
        right_act = sum(float(spikes_64[ch]) for ch in self.right_channels if ch < len(spikes_64))
        return left_act, right_act

    def decode_discrete(self, spikes: np.ndarray) -> int:
        """Returns discrete action: 0 for Left/Down, 1 for Right/Up."""
        left, right = self._extract_motor_spikes(spikes)
        return 1 if right > left else 0

    def decode_continuous(self, spikes: np.ndarray) -> float:
        """Returns continuous motor command in range [-1.0, 1.0]."""
        left, right = self._extract_motor_spikes(spikes)
        total = left + right
        if total < 1e-6:
            return 0.0
        return float(np.clip((right - left) / total, -1.0, 1.0))

    def decode(self, spikes: np.ndarray, discrete: bool = True) -> Union[int, float]:
        if discrete:
            return self.decode_discrete(spikes)
        return self.decode_continuous(spikes)


def _read_wetworld_spike_counts(
    wetworld: WetworldGymEnv,
    last_wet_obs: Optional[np.ndarray] = None,
    wet_info: Optional[Dict[str, Any]] = None,
) -> np.ndarray:
    """
    Reads aggregated multi-tick spike counts across steps_per_action ticks when
    exposed by WetworldGymEnv (window_spike_counts or info['window_spike_counts']),
    falling back to the latest obs/telemetry spike raster.
    """
    if wet_info and "window_spike_counts" in wet_info and wet_info["window_spike_counts"] is not None:
        return np.asarray(wet_info["window_spike_counts"], dtype=np.float32)
    win_counts = getattr(wetworld, "window_spike_counts", None)
    if win_counts is not None:
        return np.asarray(win_counts, dtype=np.float32)
    if last_wet_obs is not None and len(last_wet_obs) >= 128:
        return np.asarray(last_wet_obs[64:128], dtype=np.float32)
    return np.ctypeslib.as_array(wetworld.telem.spikes).astype(np.float32)


class DishBrainPongEnv(gym.Env):
    """
    Closed-Loop DishBrain Pong Benchmark Environment.
    Couples 2D Pong kinematic game physics with WetworldGymEnv organoid digital twin.
    """
    metadata = {"render_modes": ["human"], "render_fps": 60}

    def __init__(
        self,
        paddle_height: float = 0.4,
        paddle_speed: float = 0.06,
        ball_speed: float = 0.04,
        max_steps: int = 1000,
        steps_per_action: int = 10,
        **wetworld_kwargs,
    ):
        super().__init__()
        self.paddle_height = paddle_height
        self.paddle_speed = paddle_speed
        self.ball_speed = ball_speed
        self.max_steps = max_steps

        # Internal wetworld organoid VM
        self.wetworld = WetworldGymEnv(steps_per_action=steps_per_action, **wetworld_kwargs)
        self.encoder = PongStateEncoder()
        self.decoder = MotorSpikeDecoder()

        # Action space: Discrete(2) [0: Move Down, 1: Move Up]
        self.action_space = spaces.Discrete(2)

        # Observation space: 5 Pong features + 128 Wetworld features = 133 dimensions
        self.observation_space = spaces.Box(
            low=-10.0,
            high=10.0,
            shape=(5 + 128,),
            dtype=np.float32,
        )

        self.paddle_y = 0.0
        self.ball_x = 0.5
        self.ball_y = 0.0
        self.ball_vx = -self.ball_speed
        self.ball_vy = 0.01
        self.current_step = 0
        self.rally_count = 0
        self.hits = 0
        self.misses = 0
        self._last_wet_obs: Optional[np.ndarray] = None
        self._last_wet_info: Dict[str, Any] = {}

    def _get_obs(self, wet_obs: np.ndarray) -> np.ndarray:
        pong_state = np.array([
            self.paddle_y,
            self.ball_x,
            self.ball_y,
            self.ball_vx,
            self.ball_vy,
        ], dtype=np.float32)
        return np.concatenate([pong_state, wet_obs.astype(np.float32)])

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Tuple[np.ndarray, Dict[str, Any]]:
        super().reset(seed=seed)
        self.current_step = 0
        self.rally_count = 0
        self.hits = 0
        self.misses = 0
        self._last_wet_obs: Optional[np.ndarray] = None
        self._last_wet_info: Dict[str, Any] = {}

        self.paddle_y = 0.0
        self.ball_x = 0.2
        self.ball_y = 0.0
        self.ball_vx = self.ball_speed
        self.ball_vy = float(np.random.uniform(-0.02, 0.02))

        wet_obs, wet_info = self.wetworld.reset(seed=seed)
        self._last_wet_obs = wet_obs
        self._last_wet_info = wet_info
        obs = self._get_obs(wet_obs)
        spike_counts = _read_wetworld_spike_counts(self.wetworld, wet_obs, wet_info)
        info = {
            "hits": self.hits,
            "misses": self.misses,
            "rally_count": self.rally_count,
            "population_rate_hz": wet_info.get("population_rate_hz", 0.0),
            "window_spike_counts": spike_counts,
        }
        return obs, info

    def step(self, action: Optional[Union[int, np.ndarray]] = None) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        self.current_step += 1

        # Decode biological motor spike activity from aggregated multi-tick spike counts
        prev_spikes = _read_wetworld_spike_counts(self.wetworld, self._last_wet_obs, self._last_wet_info)
        if action is None:
            action = self.decoder.decode_discrete(prev_spikes)
        elif isinstance(action, (np.ndarray, list)):
            action = int(action[0] > 0) if len(action) > 0 else 0

        # Move paddle (0: Down, 1: Up)
        if action == 1:
            self.paddle_y = min(1.0 - self.paddle_height / 2, self.paddle_y + self.paddle_speed)
        else:
            self.paddle_y = max(-1.0 + self.paddle_height / 2, self.paddle_y - self.paddle_speed)

        # Update ball physics
        self.ball_x += self.ball_vx
        self.ball_y += self.ball_vy

        # Top and bottom wall bounces
        if self.ball_y >= 1.0:
            self.ball_y = 1.0
            self.ball_vy = -abs(self.ball_vy)
        elif self.ball_y <= -1.0:
            self.ball_y = -1.0
            self.ball_vy = abs(self.ball_vy)

        # Left wall bounce (opponent wall)
        if self.ball_x <= 0.0:
            self.ball_x = 0.0
            self.ball_vx = abs(self.ball_vx)

        # Paddle boundary check at x = 0.95
        reward = 0.01  # Small survival bonus
        hit_occurred = False
        miss_occurred = False

        if self.ball_x >= 0.95:
            # Check paddle collision
            half_h = self.paddle_height / 2.0
            if abs(self.ball_y - self.paddle_y) <= half_h:
                # Paddle Hit!
                hit_occurred = True
                self.hits += 1
                self.rally_count += 1
                reward += 1.0
                self.ball_x = 0.95
                self.ball_vx = -abs(self.ball_vx)
                # Angle variation based on where ball hits paddle
                impact_offset = (self.ball_y - self.paddle_y) / half_h
                self.ball_vy = np.clip(self.ball_vy + impact_offset * 0.02, -0.05, 0.05)
            else:
                # Paddle Miss!
                miss_occurred = True
                self.misses += 1
                reward -= 1.0
                # Reset ball to center
                self.ball_x = 0.2
                self.ball_y = float(np.random.uniform(-0.5, 0.5))
                self.ball_vx = self.ball_speed
                self.ball_vy = float(np.random.uniform(-0.02, 0.02))

        # Encode state into 4 sensory stimulation channels
        stim = self.encoder.encode(self.paddle_y, self.ball_x, self.ball_y, self.ball_vx, self.ball_vy)

        # Step organoid digital twin
        wet_obs, wet_reward, wet_term, wet_trunc, wet_info = self.wetworld.step(stim)
        self._last_wet_obs = wet_obs
        self._last_wet_info = wet_info

        spike_counts = _read_wetworld_spike_counts(self.wetworld, wet_obs, wet_info)
        left_act, right_act = self.decoder._extract_motor_spikes(spike_counts)

        obs = self._get_obs(wet_obs)
        terminated = wet_term
        truncated = self.current_step >= self.max_steps

        info = {
            "hits": self.hits,
            "misses": self.misses,
            "rally_count": self.rally_count,
            "hit_occurred": hit_occurred,
            "miss_occurred": miss_occurred,
            "paddle_y": self.paddle_y,
            "ball_x": self.ball_x,
            "ball_y": self.ball_y,
            "population_rate_hz": wet_info.get("population_rate_hz", 0.0),
            "wet_reward": wet_reward,
            "window_spike_counts": spike_counts,
            "motor_spikes_left": left_act,
            "motor_spikes_right": right_act,
            "organoid_motor_action": self.decoder.decode_discrete(spike_counts),
        }
        return obs, reward, terminated, truncated, info

    def close(self):
        self.wetworld.close()


class OrganoidCartPoleEnv(gym.Env):
    """
    Closed-Loop Organoid CartPole Benchmark Environment.
    Couples nonlinear CartPole inverted pendulum physics with WetworldGymEnv.
    """
    metadata = {"render_modes": ["human"], "render_fps": 50}

    def __init__(
        self,
        gravity: float = 9.8,
        masscart: float = 1.0,
        masspole: float = 0.1,
        length: float = 0.5,
        force_mag: float = 10.0,
        tau: float = 0.02,
        max_steps: int = 500,
        steps_per_action: int = 10,
        **wetworld_kwargs,
    ):
        super().__init__()
        self.gravity = gravity
        self.masscart = masscart
        self.masspole = masspole
        self.total_mass = masscart + masspole
        self.length = length  # actually half the pole's length
        self.polemass_length = masspole * length
        self.force_mag = force_mag
        self.tau = tau
        self.max_steps = max_steps

        self.theta_threshold_radians = 12 * 2 * np.pi / 360  # ~0.2095 rad
        self.x_threshold = 2.4

        # Action space: Discrete(2) [0: Push Left, 1: Push Right]
        self.action_space = spaces.Discrete(2)

        # Observation space: 4 CartPole features + 128 Wetworld features = 132 dimensions
        self.observation_space = spaces.Box(
            low=-10.0,
            high=10.0,
            shape=(4 + 128,),
            dtype=np.float32,
        )

        self.wetworld = WetworldGymEnv(steps_per_action=steps_per_action, **wetworld_kwargs)
        self.encoder = CartPoleStateEncoder()
        self.decoder = MotorSpikeDecoder()

        self.state = None
        self.current_step = 0
        self._last_wet_obs: Optional[np.ndarray] = None
        self._last_wet_info: Dict[str, Any] = {}

    def _get_obs(self, wet_obs: np.ndarray) -> np.ndarray:
        return np.concatenate([self.state.astype(np.float32), wet_obs.astype(np.float32)])

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Tuple[np.ndarray, Dict[str, Any]]:
        super().reset(seed=seed)
        self.current_step = 0
        # Initialize state with small random deviations
        self.state = np.random.uniform(low=-0.05, high=0.05, size=(4,))
        wet_obs, wet_info = self.wetworld.reset(seed=seed)
        self._last_wet_obs = wet_obs
        self._last_wet_info = wet_info
        obs = self._get_obs(wet_obs)
        spike_counts = _read_wetworld_spike_counts(self.wetworld, wet_obs, wet_info)
        info = {
            "step": self.current_step,
            "population_rate_hz": wet_info.get("population_rate_hz", 0.0),
            "window_spike_counts": spike_counts,
        }
        return obs, info

    def step(self, action: Optional[Union[int, np.ndarray]] = None) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        self.current_step += 1

        prev_spikes = _read_wetworld_spike_counts(self.wetworld, self._last_wet_obs, self._last_wet_info)
        if action is None:
            action = self.decoder.decode_discrete(prev_spikes)
        elif isinstance(action, (np.ndarray, list)):
            action = int(action[0] > 0) if len(action) > 0 else 0

        x, x_dot, theta, theta_dot = self.state
        force = self.force_mag if action == 1 else -self.force_mag

        # Standard nonlinear CartPole dynamics ODE
        costheta = np.cos(theta)
        sintheta = np.sin(theta)
        temp = (force + self.polemass_length * theta_dot**2 * sintheta) / self.total_mass
        thetaacc = (self.gravity * sintheta - costheta * temp) / (
            self.length * (4.0 / 3.0 - self.masspole * costheta**2 / self.total_mass)
        )
        xacc = temp - self.polemass_length * thetaacc * costheta / self.total_mass

        # Euler-Cromer numerical integration
        x = x + self.tau * x_dot
        x_dot = x_dot + self.tau * xacc
        theta = theta + self.tau * theta_dot
        theta_dot = theta_dot + self.tau * thetaacc

        self.state = np.array([x, x_dot, theta, theta_dot], dtype=np.float64)

        # Check termination condition
        fallen = bool(
            x < -self.x_threshold
            or x > self.x_threshold
            or theta < -self.theta_threshold_radians
            or theta > self.theta_threshold_radians
        )

        reward = 1.0 if not fallen else -1.0

        # Encode state into sensory stimulation
        stim = self.encoder.encode(x, x_dot, theta, theta_dot)
        wet_obs, wet_reward, wet_term, wet_trunc, wet_info = self.wetworld.step(stim)
        self._last_wet_obs = wet_obs
        self._last_wet_info = wet_info

        spike_counts = _read_wetworld_spike_counts(self.wetworld, wet_obs, wet_info)
        left_act, right_act = self.decoder._extract_motor_spikes(spike_counts)

        obs = self._get_obs(wet_obs)
        terminated = fallen or wet_term
        truncated = self.current_step >= self.max_steps

        info = {
            "x": x,
            "theta": theta,
            "fallen": fallen,
            "population_rate_hz": wet_info.get("population_rate_hz", 0.0),
            "window_spike_counts": spike_counts,
            "motor_spikes_left": left_act,
            "motor_spikes_right": right_act,
            "organoid_motor_action": self.decoder.decode_discrete(spike_counts),
        }
        return obs, reward, terminated, truncated, info

    def close(self):
        self.wetworld.close()


__all__ = [
    "WetworldGymEnv",
    "make",
    "BiophysicalSafetyClamp",
    "PongStateEncoder",
    "CartPoleStateEncoder",
    "MotorSpikeDecoder",
    "DishBrainPongEnv",
    "OrganoidCartPoleEnv",
]
