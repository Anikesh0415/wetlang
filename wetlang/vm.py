"""
WetLang High-Level Pythonic Virtual Machine Interface (Project Janus - Sprint Task 1)
Wraps C99 wetvm.dll with 1-line compilation, PyTorch / NumPy tensor I/O, and context management.
"""

from __future__ import annotations
import os
from pathlib import Path
from typing import Union, Optional, List
import numpy as np

from bindings.ffi import WetVMConfig, WetStatus
from bindings.runtime import WetRuntime, WetTelemetryView, WetVMError
from compiler.emitter import compile_source
from wetlang.tensors import to_torch_tensor, spikes_tensor_to_aer_packets, TORCH_AVAILABLE


class VirtualMachine:
    """
    High-level, pythonic Virtual Machine interface.
    Allows executing WetLang programs with 1-line Python invocation:
        import wetlang as wl
        vm = wl.VirtualMachine("grid mea[8, 8]; sync_tick();")
        telem = vm.step_tick()
        spikes = vm.spikes_tensor()
    """
    def __init__(
        self,
        source_or_bytecode: Union[str, bytes, Path],
        target: str = "sim",
        channel_count: int = 64,
        dt_ms: float = 0.1,
    ):
        if dt_ms <= 0.0:
            raise ValueError(f"Simulation timestep dt_ms must be strictly positive (got {dt_ms})")
        self.target = target
        self.channel_count = channel_count
        self.dt_ms = dt_ms

        # Resolve bytecode
        if isinstance(source_or_bytecode, (str, Path)) and os.path.isfile(str(source_or_bytecode)):
            path_str = str(source_or_bytecode)
            if path_str.endswith(".wbc"):
                with open(path_str, "rb") as f:
                    self.bytecode = f.read()
            else:
                with open(path_str, "r", encoding="utf-8") as f:
                    src_text = f.read()
                self.bytecode = compile_source(src_text, target=target)
        elif isinstance(source_or_bytecode, str):
            # In-memory source code string
            self.bytecode = compile_source(source_or_bytecode, target=target)
        elif isinstance(source_or_bytecode, bytes):
            self.bytecode = source_or_bytecode
        else:
            raise TypeError(f"Expected source code string, .wet/.wbc filepath, or bytecode bytes, got {type(source_or_bytecode)}")

        if self.channel_count == 64 and len(self.bytecode) >= 32:
            import struct
            try:
                ch_cnt = struct.unpack_from("<I", self.bytecode, 20)[0]
                if ch_cnt > 0:
                    self.channel_count = ch_cnt
            except Exception:
                pass

        self.config = WetVMConfig(dt_ms=self.dt_ms, channel_count=self.channel_count)
        self.runtime = WetRuntime(config=self.config)
        self.runtime.load_bytecode(self.bytecode)

    def step_tick(self) -> WetTelemetryView:
        """Executes 1 biological tick (dt_ms)."""
        return self.runtime.step_tick()

    def step_ticks(self, count: int) -> WetTelemetryView:
        """Executes count continuous biological ticks."""
        return self.runtime.run_ticks(count)

    def __call__(self, input_tensor=None):
        """
        Callable interface for PyTorch / AI loops:
            output_spikes = vm(input_spikes_tensor)
        """
        if input_tensor is not None:
            self.inject_spikes(input_tensor)
        telem = self.step_tick()
        if TORCH_AVAILABLE and input_tensor is not None and hasattr(input_tensor, "__class__") and "Tensor" in input_tensor.__class__.__name__:
            return self.spikes_tensor()
        return self.spikes_numpy()

    def stimulate(
        self,
        channel: int,
        voltage_v: float,
        phase1_ms: float = 0.2,
        phase2_ms: float = 0.2,
        interphase_ms: float = 0.0,
    ) -> None:
        """Injects a biphasic stimulation pulse into an electrode channel."""
        self.runtime.inject_stimulus(
            channel=channel,
            voltage_v=voltage_v,
            phase1_ms=phase1_ms,
            phase2_ms=phase2_ms,
        )

    def inject_spikes(self, spikes_input, peak_amplitude_uv: int = 100) -> None:
        """
        Injects spike events from a PyTorch tensor, NumPy array, or list of channel IDs.
        """
        packets = spikes_tensor_to_aer_packets(
            spikes_input,
            timestamp_tick=self.runtime.current_tick,
            peak_amplitude_uv=peak_amplitude_uv,
        )
        for pkt in packets:
            self.stimulate(pkt.channel_id, voltage_v=0.4, phase1_ms=0.1, phase2_ms=0.1)

    def voltages_numpy(self) -> np.ndarray:
        """Returns zero-copy NumPy array view of 64 electrode voltages."""
        return self.runtime.get_voltages_numpy()

    def spikes_numpy(self) -> np.ndarray:
        """Returns zero-copy NumPy array view of 64 spike flags (0 or 1)."""
        return self.runtime.get_spikes_numpy()

    def voltages_tensor(self):
        """Returns zero-copy PyTorch Tensor of electrode voltages."""
        return to_torch_tensor(self.voltages_numpy())

    def spikes_tensor(self):
        """Returns zero-copy PyTorch Tensor of spike flags."""
        return to_torch_tensor(self.spikes_numpy())

    def set_electrode_impedance(
        self,
        channel: int,
        z_magnitude_ohms: float,
        z_phase_rad: float = 0.0,
        tick: int = 0,
    ) -> None:
        """Dynamically updates measured electrode impedance for adaptive current clamping."""
        self.runtime.set_electrode_impedance(channel, z_magnitude_ohms, z_phase_rad, tick)

    def set_current_density_limit(self, max_ua_cm2: float) -> None:
        """Sets the maximum safe Faradaic current density limit J (default 30.0 uA/cm^2)."""
        self.runtime.set_current_density_limit(max_ua_cm2)

    def clamp_voltage(self, channel: int, requested_v: float) -> float:
        """Returns the clamped voltage against water-window and dynamic impedance limits."""
        return self.runtime.clamp_voltage_dynamic(channel, requested_v)

    @property
    def current_tick(self) -> int:
        return self.runtime.current_tick

    @property
    def sim_time_ms(self) -> float:
        return float(self.runtime.sim_time_ms)

    def close(self) -> None:
        """Frees the native VM instance."""
        if hasattr(self, "runtime") and self.runtime is not None:
            self.runtime.close()

    def __enter__(self) -> VirtualMachine:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
