"""
WetLang High-Level Virtual Machine Runtime Wrapper
Provides object-oriented Python interface with zero-copy NumPy array telemetry views.
"""

from pathlib import Path
from typing import Optional, Tuple, Union
import ctypes
import numpy as np

from bindings.ffi import (
    load_wetvm_lib,
    WetStatus,
    WetVMConfig,
    WetTelemetry,
    WetActuatorTelemetry,
)


class WetVMError(RuntimeError):
    """Exception raised for WetVM execution or validation errors."""
    def __init__(self, status: WetStatus, message: str):
        super().__init__(f"[{status.name}] {message}")
        self.status = status
        self.raw_message = message


class WetTelemetryView:
    """Wrapper around WetTelemetry providing convenient properties and array views."""
    def __init__(self, raw: WetTelemetry):
        self._raw = raw

    @property
    def current_tick(self) -> int:
        return int(self._raw.current_tick)

    @property
    def tick_index(self) -> int:
        return int(self._raw.current_tick)

    @property
    def sim_time_ms(self) -> float:
        return float(self._raw.sim_time_ms)

    @property
    def population_rate_hz(self) -> float:
        return float(self._raw.population_rate_hz)

    @property
    def channel_voltages(self) -> np.ndarray:
        arr = np.ctypeslib.as_array(self._raw.voltages)
        arr.flags.writeable = False
        return arr

    @property
    def spike_raster(self) -> np.ndarray:
        arr = np.ctypeslib.as_array(self._raw.spikes)
        return arr

    @property
    def last_charge_nc(self) -> np.ndarray:
        arr = np.ctypeslib.as_array(self._raw.last_charge_nc)
        return arr

    def get(self, key: str, default: object = None) -> object:
        """Dictionary-like get method for telemetry attributes."""
        if hasattr(self, key):
            val = getattr(self, key)
            return val() if callable(val) else val
        return default

    def __getitem__(self, key: str) -> object:
        """Dictionary-like indexer for telemetry attributes."""
        if hasattr(self, key):
            val = getattr(self, key)
            return val() if callable(val) else val
        raise KeyError(key)


class WetVM:
    """
    High-level Python wrapper for the native WetVM execution engine.
    Supports cycle-accurate stepping, batch tick execution, and zero-copy NumPy views.
    """

    def __init__(
        self,
        config: Optional[WetVMConfig] = None,
        lib_path: Optional[Union[str, Path]] = None
    ):
        self._lib = load_wetvm_lib(Path(lib_path) if lib_path else None)
        self._config = config if config is not None else WetVMConfig()
        self._handle = self._lib.wet_create_vm(ctypes.byref(self._config))
        if not self._handle:
            raise MemoryError("Failed to allocate native WetVM instance")

        # Persistent telemetry buffer for reuse and zero-copy NumPy mapping
        self._telem = WetTelemetry()
        self._closed = False
        self._is_halted = False
        self._bytecode_loaded = False

    def close(self) -> None:
        """Frees the native VM resources."""
        if not self._closed and self._handle:
            self._lib.wet_free_vm(self._handle)
            self._handle = None
            self._closed = True

    def __enter__(self) -> "WetVM":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def __del__(self) -> None:
        self.close()

    def _check_alive(self) -> None:
        if self._closed or not self._handle:
            raise RuntimeError("WetVM instance is closed")

    def load_bytecode(self, bytecode: Union[bytes, bytearray, str, Path]) -> None:
        """
        Loads WBC binary bytecode into the VM.
        Accepts raw bytes, or a filesystem path to a .wbc file.
        """
        self._check_alive()
        if isinstance(bytecode, (str, Path)):
            with open(bytecode, "rb") as f:
                code_data = f.read()
        elif isinstance(bytecode, (bytes, bytearray)):
            code_data = bytes(bytecode)
        else:
            raise TypeError(f"Expected bytes or path, got {type(bytecode).__name__}")

        err_buf = ctypes.create_string_buffer(512)
        c_bytes = (ctypes.c_uint8 * len(code_data)).from_buffer_copy(code_data)

        status_code = self._lib.wet_load_bytecode(
            self._handle,
            c_bytes,
            len(code_data),
            err_buf,
            len(err_buf)
        )

        status = WetStatus(status_code)
        if status != WetStatus.WET_OK:
            err_msg = err_buf.value.decode("utf-8", errors="replace")
            if not err_msg:
                err_msg = self.last_error() or self._status_to_string(status)
            raise WetVMError(status, err_msg)

        self._bytecode_loaded = True
        self._is_halted = False
        # Sync initial telemetry
        self.get_telemetry()

    def load(self, bytecode: Union[bytes, bytearray, str, Path]) -> int:
        """Alias for load_bytecode returning 0 on success."""
        self.load_bytecode(bytecode)
        return 0

    def step_tick(self) -> WetTelemetry:
        """
        Executes instructions until the next SYNC_TICK, SLEEP_TICKS, or HALT.
        Advances simulation time by dt_ms.
        """
        self._check_alive()
        if not self._bytecode_loaded:
            raise RuntimeError("No bytecode loaded into VM before stepping")

        status_code = self._lib.wet_step_tick(self._handle, ctypes.byref(self._telem))
        status = WetStatus(status_code)

        if status == WetStatus.WET_ERR_HALTED:
            self._is_halted = True
            raise WetVMError(status, "VM is halted")
        elif status != WetStatus.WET_OK:
            raise WetVMError(status, self.last_error() or self._status_to_string(status))

        return self._telem

    def run_ticks(self, ticks: int) -> Tuple[int, WetTelemetry]:
        """
        Executes up to `ticks` consecutive simulation steps.
        Returns (executed_ticks_count, final_telemetry).
        """
        self._check_alive()
        if not self._bytecode_loaded:
            raise RuntimeError("No bytecode loaded into VM before running")

        if ticks < 0:
            raise ValueError(f"ticks must be non-negative, got {ticks}")

        executed = ctypes.c_uint32(0)
        status_code = self._lib.wet_run_ticks(
            self._handle,
            ctypes.c_uint32(ticks),
            ctypes.byref(executed),
            ctypes.byref(self._telem)
        )

        status = WetStatus(status_code)
        if status == WetStatus.WET_ERR_HALTED:
            self._is_halted = True
        elif status != WetStatus.WET_OK:
            raise WetVMError(status, self.last_error() or self._status_to_string(status))

        return int(executed.value), self._telem

    def step(self, ticks: int = 1) -> WetTelemetryView:
        """Convenience method stepping 1 or more ticks and returning telemetry view."""
        self._check_alive()
        if not self._bytecode_loaded:
            raise RuntimeError("No bytecode loaded into VM before stepping")

        if ticks <= 1:
            try:
                self.step_tick()
            except WetVMError as e:
                if e.status == WetStatus.WET_ERR_HALTED:
                    pass
                else:
                    raise
        else:
            self.run_ticks(ticks)
        return WetTelemetryView(self._telem)

    def inject_stimulus(
        self,
        channel: int,
        voltage_v: float,
        phase1_ms: float = 0.5,
        phase2_ms: float = 0.5
    ) -> None:
        """Injects biphasic stimulus onto designated MEA channel."""
        self._check_alive()
        status_code = self._lib.wet_inject_stimulus(
            self._handle,
            ctypes.c_uint8(channel),
            ctypes.c_float(voltage_v),
            ctypes.c_float(phase1_ms),
            ctypes.c_float(phase2_ms)
        )
        status = WetStatus(status_code)
        if status != WetStatus.WET_OK:
            raise WetVMError(status, self.last_error() or self._status_to_string(status))

    def get_telemetry(self) -> WetTelemetry:
        """Fetches the latest cycle-accurate telemetry snapshot."""
        self._check_alive()
        status_code = self._lib.wet_get_telemetry(self._handle, ctypes.byref(self._telem))
        status = WetStatus(status_code)
        if status != WetStatus.WET_OK:
            raise WetVMError(status, self.last_error() or self._status_to_string(status))
        return self._telem

    def get_actuator_telemetry(self) -> WetActuatorTelemetry:
        """Fetches the latest cyber-physical actuator telemetry."""
        self._check_alive()
        act_telem = WetActuatorTelemetry()
        status_code = self._lib.wet_get_actuator_telemetry(self._handle, ctypes.byref(act_telem))
        status = WetStatus(status_code)
        if status != WetStatus.WET_OK:
            raise WetVMError(status, self.last_error() or self._status_to_string(status))
        return act_telem

    def get_voltages_numpy(self) -> np.ndarray:
        """
        Returns a zero-copy 1D NumPy array view (float32, 64 elements)
        mapped directly onto the telemetry voltage buffer.
        """
        arr = np.ctypeslib.as_array(self._telem.voltages)
        arr.flags.writeable = False
        return arr

    def get_spikes_numpy(self) -> np.ndarray:
        """
        Returns a zero-copy 1D NumPy array view (uint8, 64 elements)
        mapped directly onto the telemetry spike raster buffer.
        """
        return np.ctypeslib.as_array(self._telem.spikes)

    def get_charge_numpy(self) -> np.ndarray:
        """
        Returns a zero-copy 1D NumPy array view (float32, 64 elements)
        mapped directly onto the telemetry cumulative charge buffer.
        """
        return np.ctypeslib.as_array(self._telem.last_charge_nc)

    def last_error(self) -> str:
        """Returns the last recorded native error message."""
        if not self._handle:
            return "VM is closed"
        err = self._lib.wet_get_last_error(self._handle)
        return err.decode("utf-8", errors="replace") if err else ""

    def _status_to_string(self, status: WetStatus) -> str:
        s = self._lib.wet_status_to_string(int(status))
        return s.decode("utf-8", errors="replace") if s else status.name

    @property
    def current_tick(self) -> int:
        return int(self._telem.current_tick)

    @property
    def tick_index(self) -> int:
        return int(self._telem.current_tick)

    @property
    def sim_time_ms(self) -> float:
        return float(self._telem.sim_time_ms)

    @property
    def is_halted(self) -> bool:
        return self._is_halted

    # Phase 3 Hardware Readiness Methods
    def configure_electrode(self, material: int, area_um2: float) -> None:
        """Configures electrode material and physical geometric surface area."""
        self._check_alive()
        self._lib.wet_configure_electrode(self._handle, ctypes.c_uint8(material), ctypes.c_float(area_um2))

    def active_discharge(self, channel: int) -> None:
        """Actuates hardware discharge switch on designated channel to clear accumulated DC charge."""
        self._check_alive()
        self._lib.wet_active_discharge(self._handle, ctypes.c_uint8(channel))

    def active_discharge_all(self) -> None:
        """Actuates hardware discharge switch on all 64 channels."""
        self._check_alive()
        self._lib.wet_active_discharge_all(self._handle)

    def enable_dead_head_protection(self, enable: bool = True) -> None:
        """Enables microfluidic valve-pump dead-head overpressure interlock."""
        self._check_alive()
        self._lib.wet_enable_dead_head_protection(self._handle, ctypes.c_uint8(1 if enable else 0))

    def life_supervisor_shutdown(self) -> None:
        """Terminates Ring-0 Life Support Supervisor autonomous baseline perfusion."""
        self._check_alive()
        self._lib.wet_life_supervisor_shutdown(self._handle)


class WetRuntime(WetVM):
    """Alias / Subclass of WetVM providing E2E test-suite compatibility."""
    pass
