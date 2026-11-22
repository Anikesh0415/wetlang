"""
WetLang Python ctypes FFI Bindings
Exposes C-ABI functions and data structures for wetvm.dll / libwetvm.so.
"""

import os
import sys
import ctypes
from ctypes import c_void_p, c_char_p, c_int, c_int32, c_uint8, c_uint16, c_uint32, c_uint64, c_double, c_float, c_size_t, POINTER
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


class WetHalMode(IntEnum):
    WET_HAL_MODE_SIMULATED    = 0
    WET_HAL_MODE_PHYSICAL     = 1
    WET_HAL_MODE_HIL_LOOPBACK = 2


class WetHalDriverType(IntEnum):
    WET_HAL_DRIVER_EPHYS   = 1
    WET_HAL_DRIVER_PUMP    = 2
    WET_HAL_DRIVER_VALVE   = 3
    WET_HAL_DRIVER_FLOW    = 4
    WET_HAL_DRIVER_CAN_BUS = 5


class WetHalStatus(IntEnum):
    WET_HAL_OK                   = 0
    WET_HAL_ERR_NULL_PTR         = -1
    WET_HAL_ERR_INVALID_MODE     = -2
    WET_HAL_ERR_DRIVER_NOT_FOUND = -3
    WET_HAL_ERR_IO               = -4
    WET_HAL_ERR_TIMEOUT          = -5
    WET_HAL_ERR_CRC_MISMATCH     = -6
    WET_HAL_ERR_COMPLIANCE_RAILED= -7
    WET_HAL_ERR_INTERLOCK        = -8
    WET_HAL_ERR_DEAD_HEAD        = -9
    WET_HAL_ERR_OUT_OF_BOUNDS    = -10
    WET_HAL_ERR_BUS_BUSY         = -11
    WET_HAL_ERR_NOT_SUPPORTED    = -12
    WET_HAL_ERR_BUFFER_FULL      = -13


class WetHalConfig(ctypes.Structure):
    """Mirror of C wet_hal_config_t."""
    _fields_ = [
        ("mode", c_int),
        ("max_ephys_channels", c_uint32),
        ("num_pumps", c_uint32),
        ("num_valves", c_uint32),
        ("num_flow_sensors", c_uint32),
        ("enable_dead_head_protection", c_uint8),
        ("enable_crowbar_fastpath", c_uint8),
        ("valve_for_pump", c_uint8 * 8),
    ]

    def __init__(
        self,
        mode: int = 0,
        max_ephys_channels: int = 64,
        num_pumps: int = 8,
        num_valves: int = 8,
        num_flow_sensors: int = 8,
        enable_dead_head_protection: int = 1,
        enable_crowbar_fastpath: int = 1,
        valve_for_pump = None,
    ):
        v = (c_uint8 * 8)(0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF)
        if valve_for_pump is not None:
            for i, val in enumerate(valve_for_pump):
                v[i] = val
        super().__init__(
            mode=mode,
            max_ephys_channels=max_ephys_channels,
            num_pumps=num_pumps,
            num_valves=num_valves,
            num_flow_sensors=num_flow_sensors,
            enable_dead_head_protection=enable_dead_head_protection,
            enable_crowbar_fastpath=enable_crowbar_fastpath,
            valve_for_pump=v,
        )


class WetHalTelemetry(ctypes.Structure):
    """Mirror of C wet_hal_telemetry_t."""
    _fields_ = [
        ("total_spi_transactions", c_uint64),
        ("total_i2c_transactions", c_uint64),
        ("total_rs232_commands", c_uint64),
        ("total_can_frames", c_uint64),
        ("total_crowbar_events", c_uint64),
        ("last_crowbar_timestamp_us", c_uint64),
        ("last_crowbar_reason", c_uint32),
        ("crowbar_latency_us", c_double),
    ]


class WetHalContext(ctypes.Structure):
    """Mirror of C wet_hal_context_t."""
    _fields_ = [
        ("mode", c_int),
        ("config", WetHalConfig),
        ("vm", c_void_p),
        ("drivers", c_void_p * 16),
        ("driver_count", c_uint32),
        ("ephys_driver", c_void_p),
        ("pump_driver", c_void_p),
        ("valve_driver", c_void_p),
        ("flow_driver", c_void_p),
        ("can_driver", c_void_p),
        ("pump_rates_ul_min", c_float * 8),
        ("valve_states", c_uint8 * 8),
        ("flow_rates_ul_min", c_double * 8),
        ("ephys_voltages", c_float * 64),
        ("ephys_spikes", c_uint8 * 64),
        ("crowbar_tripped", c_uint8),
        ("crowbar_reason", c_uint32),
        ("crowbar_tick", c_uint64),
        ("crowbar_timestamp_us", c_uint64),
        ("telemetry", WetHalTelemetry),
    ]


class WetCanFrame(ctypes.Structure):
    """Mirror of C wet_can_frame_t."""
    _fields_ = [
        ("id", c_uint32),
        ("is_extended", c_uint8),
        ("is_rtr", c_uint8),
        ("dlc", c_uint8),
        ("data", c_uint8 * 8),
        ("timestamp_us", c_uint64),
    ]


# =========================================================================
# C Struct Mirrors
# =========================================================================

class WetVMConfig(ctypes.Structure):
    """Mirror of C wet_vm_config_t (32 bytes)."""
    _fields_ = [
        ("dt_ms", c_double),
        ("max_stack_depth", c_uint32),
        ("max_locals", c_uint32),
        ("channel_count", c_uint32),
        ("max_ops_per_tick", c_uint32),
        ("min_sequence_counter", c_uint32),
    ]

    def __init__(
        self,
        dt_ms: float = 0.1,
        max_stack_depth: int = 1024,
        max_locals: int = 256,
        channel_count: int = 64,
        max_ops_per_tick: int = 100000,
        min_sequence_counter: int = 0
    ):
        super().__init__(
            dt_ms=dt_ms,
            max_stack_depth=max_stack_depth,
            max_locals=max_locals,
            channel_count=channel_count,
            max_ops_per_tick=max_ops_per_tick,
            min_sequence_counter=min_sequence_counter
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

    # Milestone 2: Biophysics Live Synaptic Inspection
    if hasattr(lib, "wet_vm_get_synapse_matrix"):
        lib.wet_vm_get_synapse_matrix.restype = c_int
        lib.wet_vm_get_synapse_matrix.argtypes = [c_void_p, POINTER(c_float), c_size_t]

    if hasattr(lib, "wet_vm_get_synapse_weight"):
        lib.wet_vm_get_synapse_weight.restype = c_float
        lib.wet_vm_get_synapse_weight.argtypes = [c_void_p, c_uint8, c_uint8]

    # Milestone 1: Physical HAL Core APIs
    if hasattr(lib, "wet_hal_create"):
        lib.wet_hal_create.restype = c_void_p
        lib.wet_hal_create.argtypes = [c_int, POINTER(WetHalConfig)]

    if hasattr(lib, "wet_hal_destroy"):
        lib.wet_hal_destroy.restype = None
        lib.wet_hal_destroy.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_init"):
        lib.wet_hal_init.restype = c_int
        lib.wet_hal_init.argtypes = [c_void_p, c_int, POINTER(WetHalConfig)]

    if hasattr(lib, "wet_hal_attach"):
        lib.wet_hal_attach.restype = c_int
        lib.wet_hal_attach.argtypes = [c_void_p, c_void_p]

    if hasattr(lib, "wet_hal_get_context"):
        lib.wet_hal_get_context.restype = c_void_p
        lib.wet_hal_get_context.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_set_mode"):
        lib.wet_hal_set_mode.restype = c_int
        lib.wet_hal_set_mode.argtypes = [c_void_p, c_int]

    if hasattr(lib, "wet_hal_get_mode"):
        lib.wet_hal_get_mode.restype = c_int
        lib.wet_hal_get_mode.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_register_driver"):
        lib.wet_hal_register_driver.restype = c_int
        lib.wet_hal_register_driver.argtypes = [c_void_p, c_void_p]

    if hasattr(lib, "wet_hal_unregister_driver"):
        lib.wet_hal_unregister_driver.restype = c_int
        lib.wet_hal_unregister_driver.argtypes = [c_void_p, c_void_p]

    if hasattr(lib, "wet_hal_find_driver"):
        lib.wet_hal_find_driver.restype = c_void_p
        lib.wet_hal_find_driver.argtypes = [c_void_p, c_int]

    if hasattr(lib, "wet_hal_write_pump"):
        lib.wet_hal_write_pump.restype = c_int
        lib.wet_hal_write_pump.argtypes = [c_void_p, c_uint8, c_double, c_uint8]

    if hasattr(lib, "wet_hal_dispense_pump"):
        lib.wet_hal_dispense_pump.restype = c_int
        lib.wet_hal_dispense_pump.argtypes = [c_void_p, c_uint8, c_double]

    if hasattr(lib, "wet_hal_write_valve"):
        lib.wet_hal_write_valve.restype = c_int
        lib.wet_hal_write_valve.argtypes = [c_void_p, c_uint8, c_uint8]

    if hasattr(lib, "wet_hal_read_flow"):
        lib.wet_hal_read_flow.restype = c_int
        lib.wet_hal_read_flow.argtypes = [c_void_p, c_uint8, POINTER(c_double)]

    if hasattr(lib, "wet_hal_stim_current"):
        lib.wet_hal_stim_current.restype = c_int
        lib.wet_hal_stim_current.argtypes = [c_void_p, c_uint16, ctypes.c_int32, c_uint32]

    if hasattr(lib, "wet_hal_stim_voltage"):
        lib.wet_hal_stim_voltage.restype = c_int
        lib.wet_hal_stim_voltage.argtypes = [c_void_p, c_uint16, c_float, c_float, c_float]

    if hasattr(lib, "wet_hal_read_spikes"):
        lib.wet_hal_read_spikes.restype = c_int
        lib.wet_hal_read_spikes.argtypes = [c_void_p, c_uint16, POINTER(c_uint8)]

    if hasattr(lib, "wet_hal_measure_impedance"):
        lib.wet_hal_measure_impedance.restype = c_int
        lib.wet_hal_measure_impedance.argtypes = [c_void_p, c_uint16, c_float, POINTER(c_float), POINTER(c_float)]

    if hasattr(lib, "wet_hal_active_discharge"):
        lib.wet_hal_active_discharge.restype = c_int
        lib.wet_hal_active_discharge.argtypes = [c_void_p, c_uint16]

    if hasattr(lib, "wet_hal_emergency_crowbar"):
        lib.wet_hal_emergency_crowbar.restype = None
        lib.wet_hal_emergency_crowbar.argtypes = [c_void_p, c_uint32]

    if hasattr(lib, "wet_hal_get_time_us"):
        lib.wet_hal_get_time_us.restype = c_uint64
        lib.wet_hal_get_time_us.argtypes = []

    if hasattr(lib, "wet_hal_get_telemetry"):
        lib.wet_hal_get_telemetry.restype = POINTER(WetHalTelemetry)
        lib.wet_hal_get_telemetry.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_set_valve_for_pump"):
        lib.wet_hal_set_valve_for_pump.restype = None
        lib.wet_hal_set_valve_for_pump.argtypes = [c_void_p, c_uint8, c_uint8]

    # Intan RHS2116 APIs
    if hasattr(lib, "wet_hal_intan_create"):
        lib.wet_hal_intan_create.restype = c_void_p
        lib.wet_hal_intan_create.argtypes = [c_int]

    if hasattr(lib, "wet_hal_intan_destroy"):
        lib.wet_hal_intan_destroy.restype = None
        lib.wet_hal_intan_destroy.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_intan_spi_transfer"):
        lib.wet_hal_intan_spi_transfer.restype = c_uint32
        lib.wet_hal_intan_spi_transfer.argtypes = [c_void_p, c_uint32]

    if hasattr(lib, "wet_hal_intan_set_stim_current"):
        lib.wet_hal_intan_set_stim_current.restype = c_int
        lib.wet_hal_intan_set_stim_current.argtypes = [c_void_p, c_uint8, ctypes.c_int32, c_uint32]

    if hasattr(lib, "wet_hal_intan_get_compliance_status"):
        lib.wet_hal_intan_get_compliance_status.restype = ctypes.c_uint16
        lib.wet_hal_intan_get_compliance_status.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_intan_clear_compliance"):
        lib.wet_hal_intan_clear_compliance.restype = None
        lib.wet_hal_intan_clear_compliance.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_intan_measure_impedance"):
        lib.wet_hal_intan_measure_impedance.restype = c_int
        lib.wet_hal_intan_measure_impedance.argtypes = [c_void_p, c_uint8, c_float, POINTER(c_float), POINTER(c_float)]

    if hasattr(lib, "wet_hal_intan_set_charge_recovery"):
        lib.wet_hal_intan_set_charge_recovery.restype = c_int
        lib.wet_hal_intan_set_charge_recovery.argtypes = [c_void_p, c_uint8, c_uint8]

    if hasattr(lib, "wet_hal_intan_inject_fault"):
        lib.wet_hal_intan_inject_fault.restype = None
        lib.wet_hal_intan_inject_fault.argtypes = [c_void_p, c_uint8, c_uint8, c_uint8]

    # MaxWell MaxOne APIs
    if hasattr(lib, "wet_hal_maxwell_create"):
        lib.wet_hal_maxwell_create.restype = c_void_p
        lib.wet_hal_maxwell_create.argtypes = [c_int]

    if hasattr(lib, "wet_hal_maxwell_destroy"):
        lib.wet_hal_maxwell_destroy.restype = None
        lib.wet_hal_maxwell_destroy.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_maxwell_route_channels"):
        lib.wet_hal_maxwell_route_channels.restype = c_int
        lib.wet_hal_maxwell_route_channels.argtypes = [c_void_p, POINTER(ctypes.c_uint16), c_uint32]

    if hasattr(lib, "wet_hal_maxwell_connect_stim"):
        lib.wet_hal_maxwell_connect_stim.restype = c_int
        lib.wet_hal_maxwell_connect_stim.argtypes = [c_void_p, c_uint8, ctypes.c_uint16]

    if hasattr(lib, "wet_hal_maxwell_sequence_clear"):
        lib.wet_hal_maxwell_sequence_clear.restype = None
        lib.wet_hal_maxwell_sequence_clear.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_maxwell_sequence_append"):
        lib.wet_hal_maxwell_sequence_append.restype = c_int
        lib.wet_hal_maxwell_sequence_append.argtypes = [c_void_p, c_uint32, c_uint8, ctypes.c_uint16, c_float, ctypes.c_uint16]

    if hasattr(lib, "wet_hal_maxwell_sequence_arm"):
        lib.wet_hal_maxwell_sequence_arm.restype = c_int
        lib.wet_hal_maxwell_sequence_arm.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_maxwell_sequence_start"):
        lib.wet_hal_maxwell_sequence_start.restype = c_int
        lib.wet_hal_maxwell_sequence_start.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_maxwell_sequence_get_state"):
        lib.wet_hal_maxwell_sequence_get_state.restype = c_int
        lib.wet_hal_maxwell_sequence_get_state.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_maxwell_stim_voltage"):
        lib.wet_hal_maxwell_stim_voltage.restype = c_int
        lib.wet_hal_maxwell_stim_voltage.argtypes = [c_void_p, c_uint8, ctypes.c_uint16, c_float, c_float, c_float]

    if hasattr(lib, "wet_hal_maxwell_inject_fault"):
        lib.wet_hal_maxwell_inject_fault.restype = None
        lib.wet_hal_maxwell_inject_fault.argtypes = [c_void_p, c_uint8, c_uint8]

    # Microfluidics & CAN APIs
    if hasattr(lib, "wet_hal_microfluidics_create"):
        lib.wet_hal_microfluidics_create.restype = c_void_p
        lib.wet_hal_microfluidics_create.argtypes = [c_int]

    if hasattr(lib, "wet_hal_microfluidics_destroy"):
        lib.wet_hal_microfluidics_destroy.restype = None
        lib.wet_hal_microfluidics_destroy.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_harvard_format_cmd"):
        lib.wet_hal_harvard_format_cmd.restype = c_int
        lib.wet_hal_harvard_format_cmd.argtypes = [c_uint8, c_uint8, c_char_p, c_char_p, c_char_p, c_size_t]

    if hasattr(lib, "wet_hal_harvard_parse_response"):
        lib.wet_hal_harvard_parse_response.restype = c_int
        lib.wet_hal_harvard_parse_response.argtypes = [c_char_p, c_size_t]

    if hasattr(lib, "wet_hal_pump_set_rate"):
        lib.wet_hal_pump_set_rate.restype = c_int
        lib.wet_hal_pump_set_rate.argtypes = [c_void_p, c_uint8, c_double, c_uint8]

    if hasattr(lib, "wet_hal_pump_dispense"):
        lib.wet_hal_pump_dispense.restype = c_int
        lib.wet_hal_pump_dispense.argtypes = [c_void_p, c_uint8, c_double]

    if hasattr(lib, "wet_hal_pump_stop"):
        lib.wet_hal_pump_stop.restype = c_int
        lib.wet_hal_pump_stop.argtypes = [c_void_p, c_uint8]

    if hasattr(lib, "wet_hal_valve_set_state"):
        lib.wet_hal_valve_set_state.restype = c_int
        lib.wet_hal_valve_set_state.argtypes = [c_void_p, c_uint8, c_uint8]

    if hasattr(lib, "wet_hal_pump_bind_downstream_valve"):
        lib.wet_hal_pump_bind_downstream_valve.restype = None
        lib.wet_hal_pump_bind_downstream_valve.argtypes = [c_void_p, c_uint8, c_uint8]

    if hasattr(lib, "wet_hal_can_send"):
        lib.wet_hal_can_send.restype = c_int
        lib.wet_hal_can_send.argtypes = [c_void_p, POINTER(WetCanFrame)]

    if hasattr(lib, "wet_hal_can_recv"):
        lib.wet_hal_can_recv.restype = c_int
        lib.wet_hal_can_recv.argtypes = [c_void_p, POINTER(WetCanFrame)]

    if hasattr(lib, "wet_hal_can_send_emcy"):
        lib.wet_hal_can_send_emcy.restype = c_int
        lib.wet_hal_can_send_emcy.argtypes = [c_void_p, c_uint8, ctypes.c_uint16, c_uint8]

    if hasattr(lib, "wet_hal_microfluidics_inject_fault"):
        lib.wet_hal_microfluidics_inject_fault.restype = None
        lib.wet_hal_microfluidics_inject_fault.argtypes = [c_void_p, c_uint8, c_uint8, c_uint8]

    # Sensirion Flow Meter APIs
    if hasattr(lib, "wet_hal_sensirion_create"):
        lib.wet_hal_sensirion_create.restype = c_void_p
        lib.wet_hal_sensirion_create.argtypes = [c_int]

    if hasattr(lib, "wet_hal_sensirion_destroy"):
        lib.wet_hal_sensirion_destroy.restype = None
        lib.wet_hal_sensirion_destroy.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_sensirion_crc8"):
        lib.wet_hal_sensirion_crc8.restype = c_uint8
        lib.wet_hal_sensirion_crc8.argtypes = [POINTER(c_uint8), c_size_t]

    if hasattr(lib, "wet_hal_sensirion_validate_crc"):
        lib.wet_hal_sensirion_validate_crc.restype = c_int
        lib.wet_hal_sensirion_validate_crc.argtypes = [POINTER(c_uint8)]

    if hasattr(lib, "wet_hal_sensirion_start_measurement"):
        lib.wet_hal_sensirion_start_measurement.restype = c_int
        lib.wet_hal_sensirion_start_measurement.argtypes = [c_void_p, ctypes.c_uint16]

    if hasattr(lib, "wet_hal_sensirion_stop_measurement"):
        lib.wet_hal_sensirion_stop_measurement.restype = c_int
        lib.wet_hal_sensirion_stop_measurement.argtypes = [c_void_p]

    if hasattr(lib, "wet_hal_sensirion_read_flow"):
        lib.wet_hal_sensirion_read_flow.restype = c_int
        lib.wet_hal_sensirion_read_flow.argtypes = [c_void_p, POINTER(c_double)]

    if hasattr(lib, "wet_hal_sensirion_hil_set_flow"):
        lib.wet_hal_sensirion_hil_set_flow.restype = None
        lib.wet_hal_sensirion_hil_set_flow.argtypes = [c_void_p, c_double]

    if hasattr(lib, "wet_hal_shdlc_encode"):
        lib.wet_hal_shdlc_encode.restype = c_size_t
        lib.wet_hal_shdlc_encode.argtypes = [c_uint8, c_uint8, POINTER(c_uint8), c_uint8, POINTER(c_uint8), c_size_t]

    if hasattr(lib, "wet_hal_shdlc_decode"):
        lib.wet_hal_shdlc_decode.restype = c_int
        lib.wet_hal_shdlc_decode.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]

    if hasattr(lib, "wet_hal_sensirion_inject_fault"):
        lib.wet_hal_sensirion_inject_fault.restype = None
        lib.wet_hal_sensirion_inject_fault.argtypes = [c_void_p, c_uint8, c_uint8]

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

    # =========================================================================
    # Milestone 1: Physical Hardware Abstraction Layer (HAL) FFI Methods
    # =========================================================================

    def hal_create(self, mode: int = 2, config: Optional[WetHalConfig] = None):
        cfg_ptr = ctypes.byref(config) if config is not None else None
        ptr = self.lib.wet_hal_create(ctypes.c_int(mode), cfg_ptr)
        return ctypes.cast(ptr, ctypes.POINTER(WetHalContext)) if ptr else None

    def hal_destroy(self, hal: ctypes.c_void_p) -> None:
        self.lib.wet_hal_destroy(hal)

    def hal_get_telemetry(self, hal: ctypes.c_void_p) -> Optional[WetHalTelemetry]:
        if hasattr(self.lib, "wet_hal_get_telemetry"):
            p = self.lib.wet_hal_get_telemetry(hal)
            return p.contents if p else None
        return None

    def hal_set_valve_for_pump(self, hal: ctypes.c_void_p, pump_id: int, valve_id: int) -> None:
        if hasattr(self.lib, "wet_hal_set_valve_for_pump"):
            self.lib.wet_hal_set_valve_for_pump(hal, ctypes.c_uint8(pump_id), ctypes.c_uint8(valve_id))

    def hal_init(self, vm: ctypes.c_void_p, mode: int = 2, config: Optional[WetHalConfig] = None) -> int:
        cfg_ptr = ctypes.byref(config) if config is not None else None
        return self.lib.wet_hal_init(vm, ctypes.c_int(mode), cfg_ptr)

    def hal_attach(self, vm: ctypes.c_void_p, hal: ctypes.c_void_p) -> int:
        return self.lib.wet_hal_attach(vm, hal)

    def hal_get_context(self, vm: ctypes.c_void_p) -> ctypes.c_void_p:
        return self.lib.wet_hal_get_context(vm)

    def hal_set_mode(self, hal: ctypes.c_void_p, mode: int) -> int:
        return self.lib.wet_hal_set_mode(hal, ctypes.c_int(mode))

    def hal_get_mode(self, hal: ctypes.c_void_p) -> int:
        return self.lib.wet_hal_get_mode(hal)

    def hal_register_driver(self, hal: ctypes.c_void_p, driver: ctypes.c_void_p) -> int:
        return self.lib.wet_hal_register_driver(hal, driver)

    def hal_unregister_driver(self, hal: ctypes.c_void_p, driver: ctypes.c_void_p) -> int:
        return self.lib.wet_hal_unregister_driver(hal, driver)

    def hal_find_driver(self, hal: ctypes.c_void_p, driver_type: int) -> ctypes.c_void_p:
        return self.lib.wet_hal_find_driver(hal, ctypes.c_int(driver_type))

    def hal_write_pump(self, hal: ctypes.c_void_p, pump_id: int, rate_ul_min: float, run_flag: int = 1) -> int:
        return self.lib.wet_hal_write_pump(hal, ctypes.c_uint8(pump_id), ctypes.c_double(rate_ul_min), ctypes.c_uint8(run_flag))

    def hal_dispense_pump(self, hal: ctypes.c_void_p, pump_id: int, volume_ul: float) -> int:
        return self.lib.wet_hal_dispense_pump(hal, ctypes.c_uint8(pump_id), ctypes.c_double(volume_ul))

    def hal_write_valve(self, hal: ctypes.c_void_p, valve_id: int, state: int) -> int:
        return self.lib.wet_hal_write_valve(hal, ctypes.c_uint8(valve_id), ctypes.c_uint8(state))

    def hal_read_flow(self, hal: ctypes.c_void_p, sensor_id: int = 0) -> Tuple[int, float]:
        val = ctypes.c_double(0.0)
        st = self.lib.wet_hal_read_flow(hal, ctypes.c_uint8(sensor_id), ctypes.byref(val))
        return st, float(val.value)

    def hal_stim_current(self, hal: ctypes.c_void_p, channel: int, current_pA: int, duration_us: int) -> int:
        return self.lib.wet_hal_stim_current(hal, ctypes.c_uint16(channel), ctypes.c_int32(current_pA), ctypes.c_uint32(duration_us))

    def hal_stim_voltage(self, hal: ctypes.c_void_p, channel: int, voltage_v: float, p1_ms: float = 0.5, p2_ms: float = 0.5) -> int:
        return self.lib.wet_hal_stim_voltage(hal, ctypes.c_uint16(channel), ctypes.c_float(voltage_v), ctypes.c_float(p1_ms), ctypes.c_float(p2_ms))

    def hal_read_spikes(self, hal: ctypes.c_void_p, channel: int) -> Tuple[int, int]:
        spk = ctypes.c_uint8(0)
        st = self.lib.wet_hal_read_spikes(hal, ctypes.c_uint16(channel), ctypes.byref(spk))
        return st, int(spk.value)

    def hal_measure_impedance(self, hal: ctypes.c_void_p, channel: int, freq_hz: float = 1000.0) -> Tuple[int, float, float]:
        mag = ctypes.c_float(0.0)
        phase = ctypes.c_float(0.0)
        st = self.lib.wet_hal_measure_impedance(hal, ctypes.c_uint16(channel), ctypes.c_float(freq_hz), ctypes.byref(mag), ctypes.byref(phase))
        return st, float(mag.value), float(phase.value)

    def hal_active_discharge(self, hal: ctypes.c_void_p, channel: int) -> int:
        return self.lib.wet_hal_active_discharge(hal, ctypes.c_uint16(channel))

    def hal_emergency_crowbar(self, vm: ctypes.c_void_p, trip_reason: int = 1) -> None:
        self.lib.wet_hal_emergency_crowbar(vm, ctypes.c_uint32(trip_reason))

    # Intan RHS2116 Driver
    def intan_create(self, mode: int = 2) -> ctypes.c_void_p:
        return self.lib.wet_hal_intan_create(ctypes.c_int(mode))

    def intan_destroy(self, drv: ctypes.c_void_p) -> None:
        self.lib.wet_hal_intan_destroy(drv)

    def intan_spi_transfer(self, drv: ctypes.c_void_p, mosi_word: int) -> int:
        return int(self.lib.wet_hal_intan_spi_transfer(drv, ctypes.c_uint32(mosi_word)))

    def intan_set_stim_current(self, drv: ctypes.c_void_p, channel: int, current_pA: int, duration_us: int) -> int:
        return self.lib.wet_hal_intan_set_stim_current(drv, ctypes.c_uint8(channel), ctypes.c_int32(current_pA), ctypes.c_uint32(duration_us))

    def intan_get_compliance_status(self, drv: ctypes.c_void_p) -> int:
        return int(self.lib.wet_hal_intan_get_compliance_status(drv))

    def intan_clear_compliance(self, drv: ctypes.c_void_p) -> None:
        self.lib.wet_hal_intan_clear_compliance(drv)

    def intan_measure_impedance(self, drv: ctypes.c_void_p, channel: int, freq_hz: float = 1000.0) -> Tuple[int, float, float]:
        mag = ctypes.c_float(0.0)
        phase = ctypes.c_float(0.0)
        st = self.lib.wet_hal_intan_measure_impedance(drv, ctypes.c_uint8(channel), ctypes.c_float(freq_hz), ctypes.byref(mag), ctypes.byref(phase))
        return st, float(mag.value), float(phase.value)

    def intan_set_charge_recovery(self, drv: ctypes.c_void_p, channel: int, enable: bool) -> int:
        return self.lib.wet_hal_intan_set_charge_recovery(drv, ctypes.c_uint8(channel), ctypes.c_uint8(1 if enable else 0))

    def intan_inject_fault(self, drv: ctypes.c_void_p, force_rail: bool = False, spi_error: bool = False, timeout: bool = False) -> None:
        self.lib.wet_hal_intan_inject_fault(drv, ctypes.c_uint8(1 if force_rail else 0), ctypes.c_uint8(1 if spi_error else 0), ctypes.c_uint8(1 if timeout else 0))

    # MaxWell MaxOne Driver
    def maxwell_create(self, mode: int = 2) -> ctypes.c_void_p:
        return self.lib.wet_hal_maxwell_create(ctypes.c_int(mode))

    def maxwell_destroy(self, drv: ctypes.c_void_p) -> None:
        self.lib.wet_hal_maxwell_destroy(drv)

    def maxwell_route_channels(self, drv: ctypes.c_void_p, electrode_indices: list[int]) -> int:
        c_arr = (ctypes.c_uint16 * len(electrode_indices))(*electrode_indices)
        return self.lib.wet_hal_maxwell_route_channels(drv, c_arr, ctypes.c_uint32(len(electrode_indices)))

    def maxwell_connect_stim(self, drv: ctypes.c_void_p, stim_unit: int, electrode_id: int) -> int:
        return self.lib.wet_hal_maxwell_connect_stim(drv, ctypes.c_uint8(stim_unit), ctypes.c_uint16(electrode_id))

    def maxwell_sequence_clear(self, drv: ctypes.c_void_p) -> None:
        self.lib.wet_hal_maxwell_sequence_clear(drv)

    def maxwell_sequence_append(self, drv: ctypes.c_void_p, timestamp_us: int, stim_unit: int, electrode_id: int, voltage_mv: float, duration_us: int) -> int:
        return self.lib.wet_hal_maxwell_sequence_append(drv, ctypes.c_uint32(timestamp_us), ctypes.c_uint8(stim_unit), ctypes.c_uint16(electrode_id), ctypes.c_float(voltage_mv), ctypes.c_uint16(duration_us))

    def maxwell_sequence_arm(self, drv: ctypes.c_void_p) -> int:
        return self.lib.wet_hal_maxwell_sequence_arm(drv)

    def maxwell_sequence_start(self, drv: ctypes.c_void_p) -> int:
        return self.lib.wet_hal_maxwell_sequence_start(drv)

    def maxwell_sequence_get_state(self, drv: ctypes.c_void_p) -> int:
        return self.lib.wet_hal_maxwell_sequence_get_state(drv)

    def maxwell_stim_voltage(self, drv: ctypes.c_void_p, stim_unit: int, electrode_id: int, voltage_mv: float, p1_ms: float = 0.5, p2_ms: float = 0.5) -> int:
        return self.lib.wet_hal_maxwell_stim_voltage(drv, ctypes.c_uint8(stim_unit), ctypes.c_uint16(electrode_id), ctypes.c_float(voltage_mv), ctypes.c_float(p1_ms), ctypes.c_float(p2_ms))

    def maxwell_inject_fault(self, drv: ctypes.c_void_p, force_charge_violation: bool = False, drop_frames: bool = False) -> None:
        self.lib.wet_hal_maxwell_inject_fault(drv, ctypes.c_uint8(1 if force_charge_violation else 0), ctypes.c_uint8(1 if drop_frames else 0))

    # Microfluidics Driver
    def microfluidics_create(self, mode: int = 2) -> ctypes.c_void_p:
        return self.lib.wet_hal_microfluidics_create(ctypes.c_int(mode))

    def microfluidics_destroy(self, drv: ctypes.c_void_p) -> None:
        self.lib.wet_hal_microfluidics_destroy(drv)

    def harvard_format_cmd(self, address: int, fast_mode: bool, cmd_name: str, args: str = "") -> str:
        buf = ctypes.create_string_buffer(128)
        ret = self.lib.wet_hal_harvard_format_cmd(
            ctypes.c_uint8(address),
            ctypes.c_uint8(1 if fast_mode else 0),
            cmd_name.encode("utf-8"),
            args.encode("utf-8"),
            buf,
            ctypes.c_size_t(len(buf))
        )
        return buf.value.decode("utf-8", errors="replace") if ret >= 0 else ""

    def harvard_parse_response(self, resp: str) -> str:
        c_str = resp.encode("utf-8")
        prompt = self.lib.wet_hal_harvard_parse_response(c_str, ctypes.c_size_t(len(c_str)))
        return chr(prompt) if prompt > 0 else "?"

    def pump_set_rate(self, drv: ctypes.c_void_p, pump_id: int, rate_ul_min: float, run_flag: int = 1) -> int:
        return self.lib.wet_hal_pump_set_rate(drv, ctypes.c_uint8(pump_id), ctypes.c_double(rate_ul_min), ctypes.c_uint8(run_flag))

    def pump_dispense(self, drv: ctypes.c_void_p, pump_id: int, volume_ul: float) -> int:
        return self.lib.wet_hal_pump_dispense(drv, ctypes.c_uint8(pump_id), ctypes.c_double(volume_ul))

    def pump_stop(self, drv: ctypes.c_void_p, pump_id: int) -> int:
        return self.lib.wet_hal_pump_stop(drv, ctypes.c_uint8(pump_id))

    def valve_set_state(self, drv: ctypes.c_void_p, valve_id: int, state: int) -> int:
        return self.lib.wet_hal_valve_set_state(drv, ctypes.c_uint8(valve_id), ctypes.c_uint8(state))

    def pump_bind_downstream_valve(self, drv: ctypes.c_void_p, pump_id: int, valve_id: int) -> None:
        self.lib.wet_hal_pump_bind_downstream_valve(drv, ctypes.c_uint8(pump_id), ctypes.c_uint8(valve_id))

    def can_send(self, drv: ctypes.c_void_p, frame: WetCanFrame) -> int:
        return self.lib.wet_hal_can_send(drv, ctypes.byref(frame))

    def can_recv(self, drv: ctypes.c_void_p) -> Tuple[int, Optional[WetCanFrame]]:
        f = WetCanFrame()
        st = self.lib.wet_hal_can_recv(drv, ctypes.byref(f))
        return st, f if st == 0 else None

    def can_send_emcy(self, drv: ctypes.c_void_p, node_id: int, error_code: int, error_register: int = 0) -> int:
        return self.lib.wet_hal_can_send_emcy(drv, ctypes.c_uint8(node_id), ctypes.c_uint16(error_code), ctypes.c_uint8(error_register))

    def microfluidics_inject_fault(self, drv: ctypes.c_void_p, stall: bool = False, can_drop: bool = False, timeout: bool = False) -> None:
        self.lib.wet_hal_microfluidics_inject_fault(drv, ctypes.c_uint8(1 if stall else 0), ctypes.c_uint8(1 if can_drop else 0), ctypes.c_uint8(1 if timeout else 0))

    # Sensirion Flow Meter Driver
    def sensirion_create(self, mode: int = 2) -> ctypes.c_void_p:
        return self.lib.wet_hal_sensirion_create(ctypes.c_int(mode))

    def sensirion_destroy(self, drv: ctypes.c_void_p) -> None:
        self.lib.wet_hal_sensirion_destroy(drv)

    def sensirion_crc8(self, data: bytes) -> int:
        c_bytes = (ctypes.c_uint8 * len(data)).from_buffer_copy(data)
        return int(self.lib.wet_hal_sensirion_crc8(c_bytes, ctypes.c_size_t(len(data))))

    def sensirion_validate_crc(self, word_and_crc: bytes) -> bool:
        c_bytes = (ctypes.c_uint8 * len(word_and_crc)).from_buffer_copy(word_and_crc)
        return bool(self.lib.wet_hal_sensirion_validate_crc(c_bytes))

    def sensirion_start_measurement(self, drv: ctypes.c_void_p, cmd: int = 0x3608) -> int:
        return self.lib.wet_hal_sensirion_start_measurement(drv, ctypes.c_uint16(cmd))

    def sensirion_stop_measurement(self, drv: ctypes.c_void_p) -> int:
        return self.lib.wet_hal_sensirion_stop_measurement(drv)

    def sensirion_read_flow(self, drv: ctypes.c_void_p) -> Tuple[int, float]:
        val = ctypes.c_double(0.0)
        st = self.lib.wet_hal_sensirion_read_flow(drv, ctypes.byref(val))
        return st, float(val.value)

    def sensirion_hil_set_flow(self, drv: ctypes.c_void_p, flow_ul_min: float) -> None:
        self.lib.wet_hal_sensirion_hil_set_flow(drv, ctypes.c_double(flow_ul_min))

    def shdlc_encode(self, address: int, command: int, payload: bytes) -> bytes:
        p_len = len(payload)
        c_payload = (ctypes.c_uint8 * p_len).from_buffer_copy(payload) if p_len > 0 else None
        out_buf = (ctypes.c_uint8 * 256)()
        enc_len = self.lib.wet_hal_shdlc_encode(
            ctypes.c_uint8(address),
            ctypes.c_uint8(command),
            c_payload,
            ctypes.c_uint8(p_len),
            out_buf,
            ctypes.c_size_t(len(out_buf))
        )
        return bytes(out_buf[:enc_len])

    def shdlc_decode(self, raw_bytes: bytes) -> Tuple[bool, int, int, bytes]:
        c_raw = (ctypes.c_uint8 * len(raw_bytes)).from_buffer_copy(raw_bytes)
        addr = ctypes.c_uint8(0)
        cmd = ctypes.c_uint8(0)
        payload = (ctypes.c_uint8 * 256)()
        plen = ctypes.c_uint8(0)
        ok = self.lib.wet_hal_shdlc_decode(
            c_raw,
            ctypes.c_size_t(len(raw_bytes)),
            ctypes.byref(addr),
            ctypes.byref(cmd),
            payload,
            ctypes.byref(plen)
        )
        if ok:
            return True, int(addr.value), int(cmd.value), bytes(payload[:plen.value])
        return False, 0, 0, b""

    def sensirion_inject_fault(self, drv: ctypes.c_void_p, corrupt_crc: bool = False, nak_addr: bool = False) -> None:
        self.lib.wet_hal_sensirion_inject_fault(drv, ctypes.c_uint8(1 if corrupt_crc else 0), ctypes.c_uint8(1 if nak_addr else 0))
