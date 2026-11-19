"""
WetLang Python ctypes FFI Bindings
Exposes C-ABI functions and data structures for wetvm.dll / libwetvm.so.
"""

import os
import sys
import ctypes
from ctypes import c_void_p, c_char_p, c_int, c_uint8, c_uint32, c_uint64, c_double, c_float, c_size_t, POINTER
from enum import IntEnum
from pathlib import Path
from typing import Optional, Tuple
import numpy as np


# =========================================================================
# Status and Error Codes
# =========================================================================

class WetStatus(IntEnum):
    WET_OK                      = 0
    WET_ERR_INVALID_MAGIC       = 1
    WET_ERR_CRC_MISMATCH        = 2
    WET_ERR_UNSUPPORTED_VERSION = 3
    WET_ERR_MALFORMED_SECTION   = 4
    WET_ERR_STACK_OVERFLOW      = 5
    WET_ERR_STACK_UNDERFLOW     = 6
    WET_ERR_INVALID_OPCODE      = 7
    WET_ERR_OUT_OF_BOUNDS_CH    = 8
    WET_ERR_DIVISION_BY_ZERO    = 9
    WET_ERR_NULL_PTR            = 10
    WET_ERR_ALLOC_FAILED        = 11
    WET_ERR_HALTED              = 12
    WET_ERR_CHARGE_IMBALANCE    = 13
    WET_ERR_EPILEPTIFORM_RUNAWAY = 14
    WET_ERR_CAPABILITY_DENIED   = 15
    WET_ERR_INTERLOCK_LOCKED    = 16
    WET_ERR_WATCHDOG_TIMEOUT    = 17
    WET_ERR_DC_DRIFT            = 18
    WET_ERR_CHARGE_DENSITY_EXCEEDED = 19
    WET_ERR_FOCAL_EXCITOTOXICITY = 20
    WET_ERR_SHEAR_STRESS_EXCEEDED = 21
    WET_ERR_SECURITY_UNTRUSTED    = 22
    WET_ERR_ACTUATOR_FAULT        = 23
    WET_ERR_THERMAL_LIMIT         = 24
    WET_ERR_BUBBLE_DETECTED       = 25
    WET_ERR_COMPLIANCE_RAILED     = 26
    WET_ERR_BYTECODE_VERIFICATION = 27


# =========================================================================
# C Struct Mirrors
# =========================================================================

class WetVMConfig(ctypes.Structure):
    """Mirror of C wet_vm_config_t (28 bytes)."""
    _fields_ = [
        ("dt_ms", c_double),
        ("max_stack_depth", c_uint32),
        ("max_locals", c_uint32),
        ("channel_count", c_uint32),
        ("max_ops_per_tick", c_uint32),
    ]

    def __init__(
        self,
        dt_ms: float = 0.1,
        max_stack_depth: int = 1024,
        max_locals: int = 256,
        channel_count: int = 64,
        max_ops_per_tick: int = 100000
    ):
        super().__init__(
            dt_ms=dt_ms,
            max_stack_depth=max_stack_depth,
            max_locals=max_locals,
            channel_count=channel_count,
            max_ops_per_tick=max_ops_per_tick
        )


class WetTelemetry(ctypes.Structure):
    """Mirror of C wet_telemetry_t (600 bytes with 8-byte alignment padding)."""
    _fields_ = [
        ("current_tick", c_uint64),
        ("sim_time_ms", c_double),
        ("voltages", c_float * 64),
        ("spikes", c_uint8 * 64),
        ("population_rate_hz", c_float),
        ("last_charge_nc", c_float * 64),
    ]

    @property
    def tick_index(self) -> int:
        return int(self.current_tick)

    @property
    def channel_voltages(self) -> np.ndarray:
        arr = np.ctypeslib.as_array(self.voltages)
        arr.flags.writeable = False
        return arr

    @property
    def spike_raster(self) -> np.ndarray:
        arr = np.ctypeslib.as_array(self.spikes)
        return arr

    @property
    def net_charge(self) -> np.ndarray:
        arr = np.ctypeslib.as_array(self.last_charge_nc)
        return arr

    @property
    def last_charge(self) -> np.ndarray:
        arr = np.ctypeslib.as_array(self.last_charge_nc)
        return arr


class WetActuatorTelemetry(ctypes.Structure):
    """Mirror of C wet_actuator_telemetry_t."""
    _fields_ = [
        ("pump_rates_ul_min", c_float * 8),
        ("pump_dispensed_ul", c_float * 8),
        ("valve_states", c_uint8 * 8),
        ("motor_positions", c_int * 4),
        ("motor_speeds_rpm", c_float * 4),
        ("ambient_temperature_c", c_float),
        ("fluid_pressure_kpa", c_float * 4),
    ]

    @property
    def pump_rates(self) -> np.ndarray:
        return np.ctypeslib.as_array(self.pump_rates_ul_min)

    @property
    def pump_dispensed(self) -> np.ndarray:
        return np.ctypeslib.as_array(self.pump_dispensed_ul)

    @property
    def valves(self) -> np.ndarray:
        return np.ctypeslib.as_array(self.valve_states)

    @property
    def motors(self) -> np.ndarray:
        return np.ctypeslib.as_array(self.motor_positions)


# =========================================================================
# Shared Library Loader
# =========================================================================

def _find_library_path() -> Path:
    env_path = os.environ.get("WETVM_LIBRARY_PATH")
    if env_path and Path(env_path).is_file():
        return Path(env_path)

    ext = ".dll" if sys.platform == "win32" else (".dylib" if sys.platform == "darwin" else ".so")
    lib_name = f"wetvm{ext}"

    # Search candidates
    curr_dir = Path(__file__).resolve().parent
    candidates = [
        curr_dir.parent / "bin" / lib_name,
        curr_dir.parent / "native" / "bin" / lib_name,
        curr_dir.parent.parent / "bin" / lib_name,
        curr_dir.parent.parent / "native" / "bin" / lib_name,
        curr_dir / lib_name,
        Path.cwd() / "native" / "bin" / lib_name,
        Path.cwd() / "bin" / lib_name,
        Path.cwd() / "native" / lib_name,
    ]

    for cand in candidates:
        if cand.is_file():
            return cand

    # Attempt to build automatically if not found
    build_script = curr_dir.parent / "native" / "build.py"
    if build_script.is_file():
        import subprocess
        res = subprocess.run([sys.executable, str(build_script)], capture_output=True, text=True)
        if res.returncode == 0:
            for cand in candidates:
                if cand.is_file():
                    return cand

    raise FileNotFoundError(
        f"Could not locate {lib_name}. Run 'python native/build.py' first or set WETVM_LIBRARY_PATH."
    )


def load_wetvm_lib(lib_path: Optional[Path] = None) -> ctypes.CDLL:
    path = lib_path if lib_path is not None else _find_library_path()
    lib = ctypes.CDLL(str(path))

    # wet_vm_t* wet_create_vm(const wet_vm_config_t* config)
    lib.wet_create_vm.restype = c_void_p
    lib.wet_create_vm.argtypes = [POINTER(WetVMConfig)]

    # void wet_free_vm(wet_vm_t* vm)
    lib.wet_free_vm.restype = None
    lib.wet_free_vm.argtypes = [c_void_p]

    # wet_status_t wet_load_bytecode(wet_vm_t* vm, const uint8_t* code_bytes, size_t size, char* err_buf, size_t err_buf_len)
    lib.wet_load_bytecode.restype = c_int
    lib.wet_load_bytecode.argtypes = [c_void_p, POINTER(c_uint8), c_size_t, c_char_p, c_size_t]

    # wet_status_t wet_step_tick(wet_vm_t* vm, wet_telemetry_t* out_telem)
    lib.wet_step_tick.restype = c_int
    lib.wet_step_tick.argtypes = [c_void_p, POINTER(WetTelemetry)]

    # wet_status_t wet_run_ticks(wet_vm_t* vm, uint32_t ticks, uint32_t* executed_ticks, wet_telemetry_t* out_telem)
    lib.wet_run_ticks.restype = c_int
    lib.wet_run_ticks.argtypes = [c_void_p, c_uint32, POINTER(c_uint32), POINTER(WetTelemetry)]

    # wet_status_t wet_inject_stimulus(wet_vm_t* vm, uint8_t channel, float voltage_v, float phase1_ms, float phase2_ms)
    lib.wet_inject_stimulus.restype = c_int
    lib.wet_inject_stimulus.argtypes = [c_void_p, c_uint8, c_float, c_float, c_float]

    # wet_status_t wet_get_telemetry(wet_vm_t* vm, wet_telemetry_t* out_telem)
    lib.wet_get_telemetry.restype = c_int
    lib.wet_get_telemetry.argtypes = [c_void_p, POINTER(WetTelemetry)]

    # const char* wet_get_last_error(wet_vm_t* vm)
    lib.wet_get_last_error.restype = c_char_p
    lib.wet_get_last_error.argtypes = [c_void_p]

    # const char* wet_status_to_string(wet_status_t status)
    lib.wet_status_to_string.restype = c_char_p
    lib.wet_status_to_string.argtypes = [c_int]

    # wet_status_t wet_get_actuator_telemetry(wet_vm_t* vm, wet_actuator_telemetry_t* out_act_telem)
    if hasattr(lib, "wet_get_actuator_telemetry"):
        lib.wet_get_actuator_telemetry.restype = c_int
        lib.wet_get_actuator_telemetry.argtypes = [c_void_p, POINTER(WetActuatorTelemetry)]

    # Phase 3 C-ABI Functions
    if hasattr(lib, "wet_create_vm_arena"):
        lib.wet_create_vm_arena.restype = c_void_p
        lib.wet_create_vm_arena.argtypes = [c_void_p, c_size_t, POINTER(WetVMConfig)]

    if hasattr(lib, "wet_configure_electrode"):
        lib.wet_configure_electrode.restype = None
        lib.wet_configure_electrode.argtypes = [c_void_p, c_uint8, c_float]

    if hasattr(lib, "wet_active_discharge"):
        lib.wet_active_discharge.restype = None
        lib.wet_active_discharge.argtypes = [c_void_p, c_uint8]

    if hasattr(lib, "wet_active_discharge_all"):
        lib.wet_active_discharge_all.restype = None
        lib.wet_active_discharge_all.argtypes = [c_void_p]

    if hasattr(lib, "wet_enable_dead_head_protection"):
        lib.wet_enable_dead_head_protection.restype = None
        lib.wet_enable_dead_head_protection.argtypes = [c_void_p, c_uint8]

    if hasattr(lib, "wet_life_supervisor_shutdown"):
        lib.wet_life_supervisor_shutdown.restype = None
        lib.wet_life_supervisor_shutdown.argtypes = [c_void_p]

    if hasattr(lib, "wet_configure_blanking"):
        lib.wet_configure_blanking.restype = None
        lib.wet_configure_blanking.argtypes = [c_void_p, c_float, c_uint8]

    if hasattr(lib, "wet_inject_current_stimulus"):
        lib.wet_inject_current_stimulus.restype = c_int
        lib.wet_inject_current_stimulus.argtypes = [c_void_p, c_uint8, c_float, c_float, c_float]

    if hasattr(lib, "wet_verify_bytecode"):
        lib.wet_verify_bytecode.restype = c_int
        lib.wet_verify_bytecode.argtypes = [POINTER(c_uint8), c_size_t, c_char_p, c_size_t]

    if hasattr(lib, "wet_vm_snapshot"):
        lib.wet_vm_snapshot.restype = c_int
        lib.wet_vm_snapshot.argtypes = [c_void_p, POINTER(c_uint8), POINTER(c_size_t)]

    if hasattr(lib, "wet_vm_restore"):
        lib.wet_vm_restore.restype = c_int
        lib.wet_vm_restore.argtypes = [c_void_p, POINTER(c_uint8), c_size_t]

    if hasattr(lib, "wet_set_environmental_sensors"):
        lib.wet_set_environmental_sensors.restype = None
        lib.wet_set_environmental_sensors.argtypes = [c_void_p, c_float, c_float, c_float, c_uint8, c_uint8, c_float]

    if hasattr(lib, "wet_set_temperature"):
        lib.wet_set_temperature.restype = None
        lib.wet_set_temperature.argtypes = [c_void_p, c_float]

    if hasattr(lib, "wet_set_channel_banks"):
        lib.wet_set_channel_banks.restype = None
        lib.wet_set_channel_banks.argtypes = [c_void_p, c_uint64, c_uint64]

    return lib


def get_wetvm_lib(lib_path: Optional[Path] = None) -> ctypes.CDLL:
    """Alias for load_wetvm_lib."""
    return load_wetvm_lib(lib_path)


class WetVMFFI:
    """Low-level FFI helper wrapper matching E2E test interface."""
    def __init__(self, lib_path: Optional[Path] = None):
        self.lib = get_wetvm_lib(lib_path)

    def get_version(self) -> int:
        return 0x0100

    def create_vm(self, config: Optional[WetVMConfig] = None) -> ctypes.c_void_p:
        cfg_ptr = ctypes.byref(config) if config is not None else None
        return self.lib.wet_create_vm(cfg_ptr)

    def free_vm(self, vm: ctypes.c_void_p) -> None:
        self.lib.wet_free_vm(vm)

    def allocate_telemetry(self) -> WetTelemetry:
        return WetTelemetry()

    def step_tick(self, vm: ctypes.c_void_p, telem: WetTelemetry) -> int:
        telem_ptr = ctypes.byref(telem) if isinstance(telem, WetTelemetry) else telem
        return self.lib.wet_step_tick(vm, telem_ptr)

    def run_ticks(self, vm: ctypes.c_void_p, ticks: int, telem: WetTelemetry) -> Tuple[int, int]:
        executed = ctypes.c_uint32(0)
        telem_ptr = ctypes.byref(telem) if isinstance(telem, WetTelemetry) else telem
        status = self.lib.wet_run_ticks(vm, ctypes.c_uint32(ticks), ctypes.byref(executed), telem_ptr)
        return status, int(executed.value)

    def inject_stimulus(
        self,
        vm: ctypes.c_void_p,
        channel: int,
        voltage_v: float,
        p1_ms: float = 0.5,
        p2_ms: float = 0.5
    ) -> int:
        return self.lib.wet_inject_stimulus(
            vm,
            ctypes.c_uint8(channel),
            ctypes.c_float(voltage_v),
            ctypes.c_float(p1_ms),
            ctypes.c_float(p2_ms)
        )

    def get_last_error(self, vm: Optional[ctypes.c_void_p] = None) -> str:
        if vm:
            err = self.lib.wet_get_last_error(vm)
            return err.decode("utf-8", errors="replace") if err else ""
        return ""

    def status_to_string(self, status: int) -> str:
        s = self.lib.wet_status_to_string(int(status))
        return s.decode("utf-8", errors="replace") if s else str(status)

    def load_bytecode(self, vm: ctypes.c_void_p, bytecode: bytes) -> int:
        c_bytes = (ctypes.c_uint8 * len(bytecode)).from_buffer_copy(bytecode)
        err_buf = ctypes.create_string_buffer(512)
        return self.lib.wet_load_bytecode(vm, c_bytes, len(bytecode), err_buf, len(err_buf))

    def get_telemetry(self, vm: ctypes.c_void_p, telem: WetTelemetry) -> int:
        telem_ptr = ctypes.byref(telem) if isinstance(telem, WetTelemetry) else telem
        return self.lib.wet_get_telemetry(vm, telem_ptr)

    def create_vm_arena(self, arena_bytes: int, config: Optional[WetVMConfig] = None) -> Tuple[ctypes.c_void_p, ctypes.Array]:
        """Creates a VM using a pre-allocated static ctypes byte buffer (zero heap malloc)."""
        buf = (ctypes.c_uint8 * arena_bytes)()
        cfg_ptr = ctypes.byref(config) if config is not None else None
        vm = self.lib.wet_create_vm_arena(ctypes.byref(buf), ctypes.c_size_t(arena_bytes), cfg_ptr)
        return vm, buf

    def configure_electrode(self, vm: ctypes.c_void_p, material: int, area_um2: float) -> None:
        self.lib.wet_configure_electrode(vm, ctypes.c_uint8(material), ctypes.c_float(area_um2))

    def active_discharge(self, vm: ctypes.c_void_p, channel: int) -> None:
        self.lib.wet_active_discharge(vm, ctypes.c_uint8(channel))

    def active_discharge_all(self, vm: ctypes.c_void_p) -> None:
        self.lib.wet_active_discharge_all(vm)

    def enable_dead_head_protection(self, vm: ctypes.c_void_p, enable: bool) -> None:
        self.lib.wet_enable_dead_head_protection(vm, ctypes.c_uint8(1 if enable else 0))

    def life_supervisor_shutdown(self, vm: ctypes.c_void_p) -> None:
        self.lib.wet_life_supervisor_shutdown(vm)

    def configure_blanking(self, vm: ctypes.c_void_p, blanking_ms: float = 2.0, enable_spatial: bool = True) -> None:
        self.lib.wet_configure_blanking(vm, ctypes.c_float(blanking_ms), ctypes.c_uint8(1 if enable_spatial else 0))

    def inject_current_stimulus(
        self,
        vm: ctypes.c_void_p,
        channel: int,
        current_ua: float,
        p1_ms: float = 0.5,
        p2_ms: float = 0.5
    ) -> int:
        return self.lib.wet_inject_current_stimulus(
            vm,
            ctypes.c_uint8(channel),
            ctypes.c_float(current_ua),
            ctypes.c_float(p1_ms),
            ctypes.c_float(p2_ms)
        )

    def verify_bytecode(self, bytecode: bytes) -> Tuple[int, str]:
        c_bytes = (ctypes.c_uint8 * len(bytecode)).from_buffer_copy(bytecode)
        err_buf = ctypes.create_string_buffer(512)
        st = self.lib.wet_verify_bytecode(c_bytes, ctypes.c_size_t(len(bytecode)), err_buf, ctypes.c_size_t(len(err_buf)))
        msg = err_buf.value.decode("utf-8", errors="replace")
        return st, msg

    def snapshot(self, vm: ctypes.c_void_p) -> bytes:
        needed_len = ctypes.c_size_t(0)
        self.lib.wet_vm_snapshot(vm, None, ctypes.byref(needed_len))
        buf = (ctypes.c_uint8 * needed_len.value)()
        st = self.lib.wet_vm_snapshot(vm, buf, ctypes.byref(needed_len))
        if st != 0:
            raise RuntimeError(f"Snapshot failed with status {st}")
        return bytes(buf)

    def restore(self, vm: ctypes.c_void_p, data: bytes) -> int:
        c_bytes = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
        return self.lib.wet_vm_restore(vm, c_bytes, ctypes.c_size_t(len(data)))

    def set_environmental_sensors(
        self,
        vm: ctypes.c_void_p,
        ph: float = 7.4,
        do_pct: float = 95.0,
        co2_pct: float = 5.0,
        bubble_sensor_id: int = 0,
        bubble_state: bool = False,
        flow_rate_ul_min: float = 1.5
    ) -> None:
        self.lib.wet_set_environmental_sensors(
            vm,
            ctypes.c_float(ph),
            ctypes.c_float(do_pct),
            ctypes.c_float(co2_pct),
            ctypes.c_uint8(bubble_sensor_id),
            ctypes.c_uint8(1 if bubble_state else 0),
            ctypes.c_float(flow_rate_ul_min)
        )

    def set_temperature(self, vm: ctypes.c_void_p, temp_c: float) -> None:
        self.lib.wet_set_temperature(vm, ctypes.c_float(temp_c))

    def set_channel_banks(
        self,
        vm: ctypes.c_void_p,
        ref_mask: int = 0,
        rec_mask: int = 0
    ) -> None:
        self.lib.wet_set_channel_banks(vm, ctypes.c_uint64(ref_mask), ctypes.c_uint64(rec_mask))
