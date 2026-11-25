"""
WetLang Canonical Gymnasium Standard RL Interface
=================================================
Wraps the C99 native runtime (wetvm) via fixed-size pre-allocated arena structs
(wet_create_vm_arena), ensuring zero heap allocations (malloc) during step()
for deterministic real-time execution.

Provides:
- WetworldGymEnv: Canonical gymnasium.Env wrapper around C99 Wetworld engine.
- make: Factory function matching gymnasium.make("Wetworld-v1", **kwargs).
"""

from typing import Dict, Any, Tuple, Optional, Union
from pathlib import Path
import ctypes
import numpy as np
import gymnasium as gym
from gymnasium import spaces

from bindings.ffi import (
    load_wetvm_lib,
    WetVMConfig,
    WetTelemetry,
    WetStatus,
)
from compiler.emitter import BytecodeEmitter
from compiler.isa import Opcode, Capability


def _build_default_gym_bytecode() -> bytes:
    """Builds minimal bytecode with continuous closed-loop tick synchronization."""
    emitter = BytecodeEmitter()
    emitter.capabilities = (
        Capability.CAP_STIMULATION
        | Capability.CAP_HIGH_VOLTAGE
        | Capability.CAP_CLOSED_LOOP
    )
    emitter.emit(Opcode.SYNC_TICK)
    return emitter._build_wbc_binary()


_DEFAULT_BYTECODE = _build_default_gym_bytecode()


class WetworldGymEnv(gym.Env):
    """
    Canonical Farama Gymnasium Environment for Biological Neural Organoids & Wetware.

    Memory Invariant:
        All internal C99 VM structures (instance, stack, locals, call stack) are
        allocated inside a single contiguous pre-allocated byte buffer (arena).
        Zero heap allocations (malloc/calloc/realloc/free) occur during step().

    Observation Space:
        Box(128):
            Indices [0..63]:  Channel electrode voltages (V in [-1.2, 1.2])
            Indices [64..127]: Binary spike rasters [0.0, 1.0]

    Action Space:
        Box(4):
            Biphasic stimulation amplitudes (V in [-0.8, 0.8]) delivered to
            sensory channels [0, 1, 2, 3].
    """
    metadata = {"render_modes": ["human"], "render_fps": 100}

    def __init__(
        self,
        arena_bytes: int = 1024 * 1024,
        dt_ms: float = 0.1,
        steps_per_action: int = 10,  # 10 ticks = 1.0 ms step
        target_firing_rate_hz: float = 15.0,
        channel_count: int = 64,
        max_episode_steps: int = 1000,
        custom_bytecode: Optional[bytes] = None,
        lib_path: Optional[Union[str, Path]] = None,
    ):
        super().__init__()
        self.arena_bytes = int(arena_bytes)
        self.dt_ms = float(dt_ms)
        self.steps_per_action = int(steps_per_action)
        self.target_firing_rate_hz = float(target_firing_rate_hz)
        self.channel_count = int(channel_count)
        if not (1 <= self.channel_count <= 64):
            raise ValueError(f"channel_count must be in [1, 64], got {self.channel_count}")
        self.max_episode_steps = int(max_episode_steps)
        self.custom_bytecode = custom_bytecode

        # Pre-allocate static ctypes arena buffer (1 MB default)
        self._arena_buf = (ctypes.c_uint8 * self.arena_bytes)()

        # Observation space: 64 voltages [-1.2, 1.2] + 64 binary spikes [0, 1]
        low_obs = np.concatenate([
            np.full(self.channel_count, -1.2, dtype=np.float32),
            np.zeros(self.channel_count, dtype=np.float32)
        ])
        high_obs = np.concatenate([
            np.full(self.channel_count, 1.2, dtype=np.float32),
            np.ones(self.channel_count, dtype=np.float32)
        ])
        self.observation_space = spaces.Box(low=low_obs, high=high_obs, shape=(self.channel_count * 2,), dtype=np.float32)

        # Action space: Continuous stimulation amplitudes for sensory channels 0..3
        self.action_space = spaces.Box(low=-0.8, high=0.8, shape=(4,), dtype=np.float32)

        # Pre-allocated ctypes and NumPy buffers for zero-malloc stepping & multi-tick spike aggregation
        self._lib = load_wetvm_lib(Path(lib_path) if lib_path else None)
        self._handle: Optional[ctypes.c_void_p] = None
        self._telem = WetTelemetry()
        self._executed_ticks = ctypes.c_uint32(0)
        self._spike_counts_c = (ctypes.c_uint32 * self.channel_count)()
        self._spike_counts_np = np.ctypeslib.as_array(self._spike_counts_c)
        self._spike_accum_np = np.zeros(self.channel_count, dtype=np.uint32)
        self._obs_buffer = np.zeros(self.channel_count * 2, dtype=np.float32)

        # VM configuration struct
        self._config = WetVMConfig(
            dt_ms=self.dt_ms,
            max_stack_depth=1024,
            max_locals=256,
            channel_count=self.channel_count,
            max_ops_per_tick=100000,
        )

        self.current_step = 0
        self._is_halted = False
        self._closed = False

    @property
    def is_halted(self) -> bool:
        return self._is_halted

    @property
    def telem(self) -> WetTelemetry:
        return self._telem

    @property
    def window_spike_counts(self) -> np.ndarray:
        """Per-channel spike counts aggregated over the most recent step/reset window."""
        return self._spike_accum_np

    def _init_arena_vm(self) -> None:
        """Initializes or resets the C99 VM instance within the pre-allocated arena buffer."""
        if self._handle is not None:
            self._lib.wet_free_vm(self._handle)
            self._handle = None

        self._handle = self._lib.wet_create_vm_arena(
            ctypes.byref(self._arena_buf),
            ctypes.c_size_t(self.arena_bytes),
            ctypes.byref(self._config),
        )
        if not self._handle:
            raise MemoryError("Failed to allocate native WetVM instance within arena buffer")

        # Load bytecode
        code_data = self.custom_bytecode if self.custom_bytecode is not None else _DEFAULT_BYTECODE
        c_bytes = (ctypes.c_uint8 * len(code_data)).from_buffer_copy(code_data)
        err_buf = ctypes.create_string_buffer(512)
        status = self._lib.wet_load_bytecode(
            self._handle,
            c_bytes,
            ctypes.c_size_t(len(code_data)),
            err_buf,
            ctypes.c_size_t(len(err_buf)),
        )
        if status != WetStatus.WET_OK:
            msg = err_buf.value.decode("utf-8", errors="replace")
            raise RuntimeError(f"Failed to load bytecode into arena VM (status {status}): {msg}")

        self._is_halted = False

    def _populate_obs(self) -> np.ndarray:
        """Fills pre-allocated observation buffer from native telemetry and aggregated window spikes."""
        # Channels voltages
        v_view = np.ctypeslib.as_array(self._telem.voltages)
        np.clip(v_view[:self.channel_count], -1.2, 1.2, out=self._obs_buffer[:self.channel_count])
        # Aggregated binary spike presence across the action window [0.0, 1.0]
        np.minimum(self._spike_accum_np, 1, out=self._spike_counts_np)
        self._obs_buffer[self.channel_count:self.channel_count * 2] = self._spike_counts_np
        return self._obs_buffer.copy()

    def _query_window_spikes(self, lookback_ticks: int, accumulate: bool = False) -> None:
        """Queries C99 static spike history ring buffer without heap allocation."""
        if not accumulate:
            self._spike_accum_np.fill(0)
        if lookback_ticks <= 0:
            return
        if hasattr(self._lib, "wet_get_spikes_window"):
            self._lib.wet_get_spikes_window(
                self._handle,
                ctypes.c_uint32(lookback_ticks),
                self._spike_counts_c,
                ctypes.c_size_t(self.channel_count),
            )
            self._spike_accum_np += self._spike_counts_np
        else:
            s_view = np.ctypeslib.as_array(self._telem.spikes)
            self._spike_accum_np += s_view[:self.channel_count]

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Tuple[np.ndarray, Dict[str, Any]]:
        super().reset(seed=seed)
        self.current_step = 0
        self._spike_accum_np.fill(0)
        self._init_arena_vm()

        # Step 1 tick to synchronize initial biophysics and telemetry
        self._executed_ticks.value = 0
        self._lib.wet_run_ticks(
            self._handle,
            ctypes.c_uint32(1),
            ctypes.byref(self._executed_ticks),
            ctypes.byref(self._telem),
        )
        self._query_window_spikes(int(self._executed_ticks.value), accumulate=False)

        obs = self._populate_obs()
        info = {
            "tick": int(self._telem.current_tick),
            "sim_time_ms": float(self._telem.sim_time_ms),
            "population_rate_hz": float(self._telem.population_rate_hz),
            "is_halted": self._is_halted,
            "arena_bytes": self.arena_bytes,
        }
        return obs, info

    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        """
        Executes one environment step.
        Guarantees zero heap allocations (malloc) in the native C99 execution loop.
        """
        if self._handle is None or self._closed:
            raise RuntimeError("Cannot step closed or uninitialized WetworldGymEnv")

        self.current_step += 1
        action = np.asarray(action, dtype=np.float32)
        action = np.clip(action, -0.8, 0.8)

        # Apply biphasic stimulation pulses to sensory channels [0..3]
        num_act = min(len(action), 4)
        for ch in range(num_act):
            volt = float(action[ch])
            if abs(volt) > 1e-6:
                # 0.1 ms cathodic, 0.1 ms anodic charge-balanced biphasic pulse
                self._lib.wet_inject_stimulus(
                    self._handle,
                    ctypes.c_uint8(ch),
                    ctypes.c_float(volt),
                    ctypes.c_float(0.1),
                    ctypes.c_float(0.1),
                )

        # Step biological digital twin in native C99 arena, aggregating spikes across all ticks
        self._spike_accum_np.fill(0)
        total_executed = 0
        remaining = max(0, self.steps_per_action)
        status_code = WetStatus.WET_OK

        if remaining == 0:
            self._executed_ticks.value = 0
        else:
            while remaining > 0:
                chunk = min(remaining, 500)
                self._executed_ticks.value = 0
                status_code = self._lib.wet_run_ticks(
                    self._handle,
                    ctypes.c_uint32(chunk),
                    ctypes.byref(self._executed_ticks),
                    ctypes.byref(self._telem),
                )
                done_now = int(self._executed_ticks.value)
                total_executed += done_now
                self._query_window_spikes(done_now, accumulate=True)
                remaining -= chunk
                if status_code != WetStatus.WET_OK:
                    break

        if status_code == WetStatus.WET_ERR_HALTED:
            self._is_halted = True

        obs = self._populate_obs()

        # Homeostatic reward (Karl Friston Active Inference):
        # Penalizes divergence from target homeostatic population firing rate
        rate_diff = abs(float(self._telem.population_rate_hz) - self.target_firing_rate_hz)
        action_penalty = float(0.1 * np.sum(np.abs(action)))
        reward = float(-rate_diff - action_penalty)

        terminated = self._is_halted or (status_code != WetStatus.WET_OK and status_code != WetStatus.WET_ERR_HALTED)
        truncated = self.current_step >= self.max_episode_steps

        info = {
            "tick": int(self._telem.current_tick),
            "sim_time_ms": float(self._telem.sim_time_ms),
            "population_rate_hz": float(self._telem.population_rate_hz),
            "is_halted": self._is_halted,
            "status_code": int(status_code),
            "executed_ticks": total_executed,
        }
        return obs, reward, terminated, truncated, info

    def get_telemetry(self) -> WetTelemetry:
        """Returns the current telemetry struct."""
        if self._handle:
            self._lib.wet_get_telemetry(self._handle, ctypes.byref(self._telem))
        return self._telem

    def get_synapse_matrix(self) -> np.ndarray:
        """Extracts the 64x64 synaptic conductance matrix (nS)."""
        if not self._handle:
            raise RuntimeError("WetworldGymEnv not initialized")
        buf = (ctypes.c_float * (64 * 64))()
        st = self._lib.wet_vm_get_synapse_matrix(self._handle, buf, ctypes.c_size_t(64 * 64))
        if st != WetStatus.WET_OK:
            raise RuntimeError(f"Failed to read synapse matrix: status {st}")
        return np.ctypeslib.as_array(buf).reshape((64, 64)).copy()

    def get_synapse_weight(self, pre: int, post: int) -> float:
        """Queries the synaptic conductance weight between pre and post neurons in nS."""
        if not self._handle:
            raise RuntimeError("WetworldGymEnv not initialized")
        return float(self._lib.wet_vm_get_synapse_weight(
            self._handle,
            ctypes.c_uint8(pre),
            ctypes.c_uint8(post)
        ))

    def inject_stimulus(
        self,
        channel: int,
        voltage_v: float,
        phase1_ms: float = 0.1,
        phase2_ms: float = 0.1,
    ) -> int:
        """Injects biphasic stimulus onto designated channel."""
        if not self._handle:
            raise RuntimeError("WetworldGymEnv not initialized")
        return self._lib.wet_inject_stimulus(
            self._handle,
            ctypes.c_uint8(channel),
            ctypes.c_float(voltage_v),
            ctypes.c_float(phase1_ms),
            ctypes.c_float(phase2_ms),
        )

    def close(self) -> None:
        if not getattr(self, "_closed", True) and getattr(self, "_handle", None) is not None:
            self._lib.wet_free_vm(self._handle)
            self._handle = None
            self._closed = True

    def __del__(self) -> None:
        self.close()


def make(env_name: str = "Wetworld-v1", **kwargs) -> WetworldGymEnv:
    """Factory helper matching gymnasium.make('Wetworld-v1')."""
    return WetworldGymEnv(**kwargs)


__all__ = ["WetworldGymEnv", "make"]
