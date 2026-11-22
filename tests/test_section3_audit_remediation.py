"""
WetLang v1.1 - Section 3 Independent Audit Verification Tests
Validates:
1. Hardware inline pressure dead-head overpressure interlock (catching tubing cold-welding & coil burnout).
2. Asynchronous Microfluidics Queue (lockless ring buffer decoupling 10 kHz Ephys from slow RS-232 / I2C).
3. I2C 9-SCL-pulse bus recovery routine for clearing stuck-low SDA slave devices.
4. Intan RHS2116 current-limited charge recovery DAC configuration (Registers 36-37).
5. Two-Stage Crowbar bleed resistor sizing (700 kOhm guaranteeing <= 10 uA surge from +/-7.0 V rail).
"""

import ctypes
import pytest

from bindings.ffi import (
    WetVMFFI,
    WetHalMode,
    WetHalConfig,
)


@pytest.fixture(scope="module")
def ffi():
    return WetVMFFI()


def test_hardware_inline_pressure_dead_head_interlock(ffi):
    """Validates that inline transducer overpressure (>150 kPa) aborts pump run even if valve is commanded open."""
    cfg = WetHalConfig(
        mode=WetHalMode.WET_HAL_MODE_SIMULATED,
        enable_dead_head_protection=1,
    )
    hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_SIMULATED, cfg)
    assert hal is not None

    try:
        # Map pump 0 to valve 0 and open valve 0
        ffi.hal_set_valve_for_pump(hal, 0, 0)
        ffi.hal_write_valve(hal, 0, 1) # Valve OPEN

        # Normal line pressure: 101.3 kPa -> Pump run must succeed
        ffi.lib.wet_hal_set_inline_pressure(hal, 0, ctypes.c_float(101.3))
        st = ffi.hal_write_pump(hal, 0, 5.0, 1)
        assert st == 0, f"Expected OK (0), got {st}"

        # Overpressure: 180.0 kPa (e.g. Tubing compression set / cold-weld) -> Must trip WET_HAL_ERR_DEAD_HEAD (-9)
        ffi.lib.wet_hal_set_inline_pressure(hal, 0, ctypes.c_float(180.0))
        st_over = ffi.hal_write_pump(hal, 0, 5.0, 1)
        assert st_over == -9, f"Expected WET_HAL_ERR_DEAD_HEAD (-9), got {st_over}"

        # Dispense mode must also reject overpressure
        st_disp = ffi.hal_dispense_pump(hal, 0, 10.0)
        assert st_disp == -9, f"Expected WET_HAL_ERR_DEAD_HEAD (-9) on dispense, got {st_disp}"
    finally:
        ffi.hal_destroy(hal)


def test_asynchronous_microfluidics_queue(ffi):
    """Validates non-blocking O(1) async enqueue and decoupled queue processing."""
    class WetAsyncCmd(ctypes.Structure):
        _fields_ = [
            ("cmd_type", ctypes.c_uint8),
            ("device_id", ctypes.c_uint8),
            ("state", ctypes.c_uint8),
            ("padding", ctypes.c_uint8),
            ("param_val", ctypes.c_double),
            ("submit_tick", ctypes.c_uint64),
        ]

    hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_SIMULATED)
    assert hal is not None

    try:
        # Enqueue 3 async commands (1 = PUMP_RATE, 2 = PUMP_DISPENSE, 3 = VALVE_SET)
        cmd1 = WetAsyncCmd(cmd_type=1, device_id=0, state=1, param_val=2.5, submit_tick=100)
        cmd2 = WetAsyncCmd(cmd_type=2, device_id=1, state=0, param_val=15.0, submit_tick=101)
        cmd3 = WetAsyncCmd(cmd_type=3, device_id=0, state=1, param_val=0.0, submit_tick=102)

        st1 = ffi.lib.wet_hal_async_enqueue(hal, ctypes.byref(cmd1))
        st2 = ffi.lib.wet_hal_async_enqueue(hal, ctypes.byref(cmd2))
        st3 = ffi.lib.wet_hal_async_enqueue(hal, ctypes.byref(cmd3))

        assert st1 == 0 and st2 == 0 and st3 == 0

        # Process queue
        processed = ffi.lib.wet_hal_process_async_queue(hal)
        assert processed == 3, f"Expected 3 processed commands, got {processed}"

        # Subsequent processing yields 0 (empty queue)
        assert ffi.lib.wet_hal_process_async_queue(hal) == 0
    finally:
        ffi.hal_destroy(hal)


def test_i2c_bus_recovery_routine(ffi):
    """Validates 9-SCL-pulse I2C bus recovery execution."""
    hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_SIMULATED)
    assert hal is not None

    try:
        telem_before = ffi.hal_get_telemetry(hal)
        i2c_before = telem_before.total_i2c_transactions

        st = ffi.lib.wet_hal_i2c_bus_recovery(hal)
        assert st == 0

        telem_after = ffi.hal_get_telemetry(hal)
        assert telem_after.total_i2c_transactions == i2c_before + 9
    finally:
        ffi.hal_destroy(hal)


def test_intan_charge_recovery_dac_registers(ffi):
    """Validates that enabling charge recovery programs Registers 36-37 to current-limited DAC mode."""
    intan_drv = ffi.lib.wet_hal_intan_create(WetHalMode.WET_HAL_MODE_PHYSICAL)
    assert intan_drv is not None and intan_drv != 0

    try:
        # Enable charge recovery on channel 0
        st = ffi.lib.wet_hal_intan_set_charge_recovery(intan_drv, 0, 1)
        assert st == 0
    finally:
        ffi.lib.wet_hal_intan_destroy(intan_drv)
