"""
Wetworld Gymnasium Environment Wrapper (Pre-Done Standard Sandbox from Web)
============================================================================
Conforms strictly to the Farama Gymnasium (gymnasium.Env) API standard.
Enables standard open-source web RL agents (PyTorch, Stable-Baselines3,
Karl Friston Active Inference) to interface with Wetworld organoid wetware.
"""

import gymnasium as gym
from gymnasium import spaces
import numpy as np
from typing import Dict, Any, Tuple, Optional

from bindings.runtime import WetRuntime, WetVMError


class WetworldGymEnv(gym.Env):
    """
    Standard Farama Gymnasium Environment for Biological Organoids.
    
    Observation Space:
        Box(128): First 64 elements = channel voltages (V in [-1.2, 1.2])
                  Next 64 elements  = binary spike rasters [0, 1]
    
    Action Space:
        Box(4): Biphasic stimulation amplitudes (V in [-0.8, 0.8])
                delivered to sensory input electrodes [0, 1, 2, 3].
    """
    metadata = {"render_modes": ["human"], "render_fps": 100}

    def __init__(
        self,
        dt_ms: float = 0.1,
        steps_per_action: int = 10,  # 10 ticks = 1.0 ms biological step
        target_firing_rate_hz: float = 15.0,
    ):
        super().__init__()
        self.dt_ms = dt_ms
        self.steps_per_action = steps_per_action
        self.target_firing_rate_hz = target_firing_rate_hz

        # Observations: 64 voltages + 64 binary spikes = 128 dimensions
        low_obs = np.concatenate([np.full(64, -1.2, dtype=np.float32), np.zeros(64, dtype=np.float32)])
        high_obs = np.concatenate([np.full(64, 1.2, dtype=np.float32), np.ones(64, dtype=np.float32)])
        self.observation_space = spaces.Box(low=low_obs, high=high_obs, dtype=np.float32)

        # Actions: Continuous stimulation amplitudes for sensory channels 0..3
        self.action_space = spaces.Box(low=-0.8, high=0.8, shape=(4,), dtype=np.float32)

        self.runtime: Optional[WetRuntime] = None
        self.current_step = 0
        self.max_episode_steps = 1000

    def _get_obs(self, telem) -> np.ndarray:
        voltages = np.clip(telem.channel_voltages, -1.2, 1.2).astype(np.float32)
        spikes = telem.spike_raster.astype(np.float32)
        return np.concatenate([voltages, spikes])

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Tuple[np.ndarray, Dict[str, Any]]:
        super().reset(seed=seed)
        self.current_step = 0

        if self.runtime is not None:
            self.runtime.close()

        self.runtime = WetRuntime()
        # Default bytecode: single sync_tick
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode, Capability
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE | Capability.CAP_CLOSED_LOOP
        emitter.emit(Opcode.SYNC_TICK)
        self.runtime.load(emitter._build_wbc_binary())

        telem = self.runtime.step(1)
        obs = self._get_obs(telem)
        info = {
            "tick": telem.current_tick,
            "sim_time_ms": telem.sim_time_ms,
            "population_rate_hz": telem.population_rate_hz,
        }
        return obs, info

    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        self.current_step += 1
        action = np.clip(action, -0.8, 0.8)

        # Apply stimulation pulses to sensory channels 0..3
        for ch in range(4):
            volt = float(action[ch])
            if abs(volt) > 0.05:
                try:
                    self.runtime.inject_stimulus(ch, volt, 0.1, 0.1)
                except WetVMError:
                    pass

        # Step biological digital twin
        telem = self.runtime.step(ticks=self.steps_per_action)
        obs = self._get_obs(telem)

        # Reward: Homeostatic penalty (Karl Friston Active Inference)
        # Penalize divergence from target homeostatic population firing rate (e.g. 15 Hz)
        rate_diff = abs(telem.population_rate_hz - self.target_firing_rate_hz)
        reward = float(-rate_diff - 0.1 * np.sum(np.abs(action)))

        terminated = self.runtime.is_halted
        truncated = self.current_step >= self.max_episode_steps

        info = {
            "tick": telem.current_tick,
            "sim_time_ms": telem.sim_time_ms,
            "population_rate_hz": telem.population_rate_hz,
            "is_halted": self.runtime.is_halted,
        }
        return obs, reward, terminated, truncated, info

    def close(self):
        if self.runtime is not None:
            self.runtime.close()
            self.runtime = None
