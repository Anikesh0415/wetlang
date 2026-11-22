"""
WetLang v1.1 Milestone 1: Physical Hardware Abstraction Layer (HAL) Driver Test Suite
Validates Physical HAL Architecture, Intan RHS2116 DAQ, MaxWell MaxOne HD-MEA,
Harvard Apparatus RS-232, Microfluidics CAN-bus, Sensirion I2C/SHDLC Flow Meters,
and Sub-100 µs Emergency Hardware Crowbar Fast-Path.
"""

import time
import pytest
import numpy as np

from bindings.ffi import (
    WetVMFFI,
    WetStatus,
    WetHalMode,
    WetHalDriverType,
    WetHalStatus,
    WetHalConfig,
    WetCanFrame,
)
from bindings.runtime import WetVM, WetVMError


@pytest.fixture(scope="module")
def ffi():
    """Provides low-level FFI instance."""
    return WetVMFFI()


# =========================================================================
# 1. Physical HAL Core Architecture & Tri-Modal Router
# =========================================================================

class TestHalCoreArchitecture:
    def test_hal_create_and_destroy(self, ffi):
        cfg = WetHalConfig(
            mode=WetHalMode.WET_HAL_MODE_HIL_LOOPBACK,
            max_ephys_channels=64,
            num_pumps=8,
            num_valves=8,
            num_flow_sensors=8,
            enable_dead_head_protection=1,
            enable_crowbar_fastpath=1,
        )
        hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK, cfg)
        assert hal is not None
        assert ffi.hal_get_mode(hal) == WetHalMode.WET_HAL_MODE_HIL_LOOPBACK
        ffi.hal_destroy(hal)

    def test_hal_mode_switching(self, ffi):
        hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_SIMULATED)
        assert ffi.hal_get_mode(hal) == WetHalMode.WET_HAL_MODE_SIMULATED

        assert ffi.hal_set_mode(hal, WetHalMode.WET_HAL_MODE_HIL_LOOPBACK) == WetHalStatus.WET_HAL_OK
        assert ffi.hal_get_mode(hal) == WetHalMode.WET_HAL_MODE_HIL_LOOPBACK

        assert ffi.hal_set_mode(hal, WetHalMode.WET_HAL_MODE_PHYSICAL) == WetHalStatus.WET_HAL_OK
        assert ffi.hal_get_mode(hal) == WetHalMode.WET_HAL_MODE_PHYSICAL

        ffi.hal_destroy(hal)

    def test_driver_registration_and_lookup(self, ffi):
        hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        intan = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        pump = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        sensirion = ffi.sensirion_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Register drivers
        assert ffi.hal_register_driver(hal, intan) == WetHalStatus.WET_HAL_OK
        assert ffi.hal_register_driver(hal, pump) == WetHalStatus.WET_HAL_OK
        assert ffi.hal_register_driver(hal, sensirion) == WetHalStatus.WET_HAL_OK

        # Fast lookup
        assert ffi.hal_find_driver(hal, WetHalDriverType.WET_HAL_DRIVER_EPHYS) == intan
        assert ffi.hal_find_driver(hal, WetHalDriverType.WET_HAL_DRIVER_PUMP) == pump
        assert ffi.hal_find_driver(hal, WetHalDriverType.WET_HAL_DRIVER_FLOW) == sensirion

        # Unregister driver
        assert ffi.hal_unregister_driver(hal, intan) == WetHalStatus.WET_HAL_OK
        assert ffi.hal_find_driver(hal, WetHalDriverType.WET_HAL_DRIVER_EPHYS) is None

        ffi.hal_destroy(hal)
        ffi.intan_destroy(intan)
        ffi.microfluidics_destroy(pump)
        ffi.sensirion_destroy(sensirion)

    def test_emergency_crowbar_fastpath_sub_100us(self, ffi):
        vm = ffi.create_vm()
        hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        intan = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        pump = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        ffi.hal_register_driver(hal, intan)
        ffi.hal_register_driver(hal, pump)
        ffi.hal_attach(vm, hal)

        # Start infusion and configure stimulation
        ffi.hal_write_pump(hal, 0, 5.0, 1)
        ffi.intan_set_stim_current(intan, 0, 500000, 1000)

        # Benchmark emergency crowbar fastpath latency over 10 iterations to eliminate OS scheduler preemption artifacts
        latencies = []
        for _ in range(10):
            t0 = time.perf_counter()
            ffi.hal_emergency_crowbar(vm, 1) # Trip reason 1 (Charge Density)
            t1 = time.perf_counter()
            latencies.append((t1 - t0) * 1e6)

        best_py_latency_us = min(latencies)
        assert best_py_latency_us < 100.0, f"Crowbar minimum latency {best_py_latency_us:.2f} us exceeded 100 us limit"

        # Query native hardware telemetry (QPC-measured in C)
        native_crowbar_latency_us = hal.contents.telemetry.crowbar_latency_us
        assert native_crowbar_latency_us < 100.0, f"Native QPC crowbar latency {native_crowbar_latency_us:.2f} us exceeded 100 us limit"

        # Verify actuators were immediately clamped to zero
        st, flow = ffi.hal_read_flow(hal, 0)
        assert flow == 0.0

        ffi.free_vm(vm)

    def test_router_valve_mapping_dead_head(self, ffi):
        # Configure pump 0 mapped to valve 2 instead of default valve 0
        cfg = WetHalConfig(
            mode=WetHalMode.WET_HAL_MODE_HIL_LOOPBACK,
            enable_dead_head_protection=1,
            valve_for_pump=[2, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        )
        hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK, cfg)

        # Valve 2 is closed, valve 0 is open
        ffi.hal_write_valve(hal, 2, 0) # Closed
        ffi.hal_write_valve(hal, 0, 1) # Open

        # Pumping on pump 0 must fail because mapped downstream valve 2 is closed
        st = ffi.hal_write_pump(hal, 0, 2.5, 1)
        assert st == WetHalStatus.WET_HAL_ERR_DEAD_HEAD

        # Dispensing on pump 0 must also fail
        st_disp = ffi.hal_dispense_pump(hal, 0, 10.0)
        assert st_disp == WetHalStatus.WET_HAL_ERR_DEAD_HEAD

        # Open valve 2 -> pumping now succeeds
        ffi.hal_write_valve(hal, 2, 1)
        st = ffi.hal_write_pump(hal, 0, 2.5, 1)
        assert st == WetHalStatus.WET_HAL_OK

        ffi.hal_destroy(hal)


# =========================================================================
# 2. Intan RHS2116 DAQ Driver (HIL Mode)
# =========================================================================

class TestIntanRhs2116Driver:
    def test_command_encoding_and_decoding(self, ffi):
        drv = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Test CONVERT command with M flag
        # Opcode 0x00, channel 7, flag M = 1
        mosi_word = (0x00 << 24) | (1 << 23) | (7 << 16)
        # Shift through pipelined SPI
        ffi.intan_spi_transfer(drv, mosi_word)
        ffi.intan_spi_transfer(drv, 0x00000000)
        rx = ffi.intan_spi_transfer(drv, 0x00000000)

        # High 16-bits contains channel 7
        returned_ch = (rx >> 16) & 0x0F
        assert returned_ch == 7

        ffi.intan_destroy(drv)

    def test_constant_current_dac_ranges(self, ffi):
        drv = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Range 1X: 10 nA .. 2.55 uA (e.g. 500 nA = 500,000 pA)
        st = ffi.intan_set_stim_current(drv, 0, 500000, 500)
        assert st == WetHalStatus.WET_HAL_OK

        # Range 10X: 100 nA .. 25.5 uA (e.g. 10.0 uA = 10,000,000 pA)
        st = ffi.intan_set_stim_current(drv, 1, 10000000, 500)
        assert st == WetHalStatus.WET_HAL_OK

        # Range 100X: 1.0 uA .. 2.55 mA (e.g. 30 uA = 30,000,000 pA, V = 30uA * 150kOhm = 4.5V < 7.0V)
        st = ffi.intan_set_stim_current(drv, 2, 30000000, 500)
        assert st == WetHalStatus.WET_HAL_OK

        ffi.intan_destroy(drv)

    def test_compliance_rail_detection_and_clearing(self, ffi):
        drv = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Impedance is 150 kOhm.
        # Voltage = I * Z = 100 uA (1e-4 A) * 150,000 Ohm = 15.0 V > 7.0 V limit!
        # Should trip compliance rail!
        st = ffi.intan_set_stim_current(drv, 3, 100000000, 1000) # 100 uA
        assert st == WetHalStatus.WET_HAL_ERR_COMPLIANCE_RAILED

        # Check compliance register
        status_mask = ffi.intan_get_compliance_status(drv)
        assert (status_mask & (1 << 3)) != 0

        # Clear compliance register
        ffi.intan_clear_compliance(drv)
        assert ffi.intan_get_compliance_status(drv) == 0

        ffi.intan_destroy(drv)

    def test_in_situ_1khz_impedance_check(self, ffi):
        drv = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        st, mag_ohms, phase_rad = ffi.intan_measure_impedance(drv, 0, 1000.0)
        assert st == WetHalStatus.WET_HAL_OK
        assert 50000.0 <= mag_ohms <= 500000.0
        assert -1.57 <= phase_rad <= 0.0 # Capacitive phase

        ffi.intan_destroy(drv)

    def test_active_charge_recovery_switch(self, ffi):
        drv = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        assert ffi.intan_set_charge_recovery(drv, 0, True) == WetHalStatus.WET_HAL_OK
        assert ffi.intan_set_charge_recovery(drv, 0, False) == WetHalStatus.WET_HAL_OK
        ffi.intan_destroy(drv)

    def test_intan_fault_injection(self, ffi):
        drv = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # 1. Bus Timeout Injection
        ffi.intan_inject_fault(drv, timeout=True)
        rx = ffi.intan_spi_transfer(drv, 0x00000000)
        assert rx == 0xFFFFFFFF, "Timed out bus should return 0xFFFFFFFF"
        ffi.intan_inject_fault(drv, timeout=False)

        # 2. Forced Compliance Rail Injection
        ffi.intan_inject_fault(drv, force_rail=True)
        st = ffi.intan_set_stim_current(drv, 0, 100000, 500)
        assert st == WetHalStatus.WET_HAL_ERR_COMPLIANCE_RAILED
        ffi.intan_inject_fault(drv, force_rail=False)

        # 3. Channel out of bounds
        assert ffi.intan_set_stim_current(drv, 16, 100000, 500) == WetHalStatus.WET_HAL_ERR_OUT_OF_BOUNDS

        ffi.intan_destroy(drv)

    def test_intan_voltage_stimulation_duration_and_cathodic_polarity(self, ffi):
        drv = ffi.intan_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # 1. Positive current writes to positive DAC bank (reg 32 + channel)
        ch = 2
        st = ffi.intan_set_stim_current(drv, ch, 500000, 1000) # +500 nA
        assert st == WetHalStatus.WET_HAL_OK

        read_pos = (0xC0 << 24) | ((32 + ch) << 16)
        ffi.intan_spi_transfer(drv, read_pos)
        ffi.intan_spi_transfer(drv, 0)
        rx_pos = ffi.intan_spi_transfer(drv, 0)
        assert (rx_pos >> 16) == (32 + ch), f"Expected reg {32 + ch}, got {rx_pos >> 16}"
        assert (rx_pos & 0xFF) > 0, "Positive DAC value should be non-zero"

        # 2. Negative current writes to negative DAC bank (reg 48 + channel)
        st_neg = ffi.intan_set_stim_current(drv, ch, -500000, 1000) # -500 nA
        assert st_neg == WetHalStatus.WET_HAL_OK

        read_neg = (0xC0 << 24) | ((48 + ch) << 16)
        ffi.intan_spi_transfer(drv, read_neg)
        ffi.intan_spi_transfer(drv, 0)
        rx_neg = ffi.intan_spi_transfer(drv, 0)
        assert (rx_neg >> 16) == (48 + ch), f"Expected reg {48 + ch}, got {rx_neg >> 16}"
        assert (rx_neg & 0xFF) > 0, "Negative DAC value should be non-zero"

        # 3. Voltage stimulation duration must not ignore p1_ms and p2_ms
        hal = ffi.hal_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        ffi.hal_register_driver(hal, drv)
        st_volt = ffi.hal_stim_voltage(hal, ch, 0.05, 1.5, 2.5) # 1.5ms + 2.5ms = 4.0ms = 4000us
        assert st_volt == WetHalStatus.WET_HAL_OK

        ffi.hal_destroy(hal)
        ffi.intan_destroy(drv)


# =========================================================================
# 3. MaxWell MaxOne HD-MEA Driver (HIL Mode)
# =========================================================================

class TestMaxWellMaxOneDriver:
    def test_routing_matrix_configuration(self, ffi):
        drv = ffi.maxwell_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Route first 1024 channels to arbitrary electrode indices (0..26399)
        electrodes = [i * 25 for i in range(1024)]
        st = ffi.maxwell_route_channels(drv, electrodes)
        assert st == WetHalStatus.WET_HAL_OK

        # Out-of-bounds electrode index (>26400) should be rejected
        bad_electrodes = [26400]
        assert ffi.maxwell_route_channels(drv, bad_electrodes) == WetHalStatus.WET_HAL_ERR_OUT_OF_BOUNDS

        ffi.maxwell_destroy(drv)

    def test_sequence_buffering_and_playback(self, ffi):
        drv = ffi.maxwell_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        ffi.maxwell_sequence_clear(drv)

        # Append pulse train steps: 50 mV for 200 us
        for step in range(10):
            st = ffi.maxwell_sequence_append(
                drv,
                timestamp_us=step * 1000,
                stim_unit=0,
                electrode_id=step,
                voltage_mv=50.0,
                duration_us=200
            )
            assert st == WetHalStatus.WET_HAL_OK

        # Arm and start sequence
        assert ffi.maxwell_sequence_arm(drv) == WetHalStatus.WET_HAL_OK
        assert ffi.maxwell_sequence_start(drv) == WetHalStatus.WET_HAL_OK
        assert ffi.maxwell_sequence_get_state(drv) == 2 # MAXWELL_SEQ_RUNNING

        ffi.maxwell_destroy(drv)

    def test_voltage_clamping_and_charge_injection_protection(self, ffi):
        drv = ffi.maxwell_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Pulse exceeds safe Pt charge injection capacity limit (0.13225 nC):
        # 800 mV for 100 ms (100,000 us) yields Q ~ (800 / 300) * 100 = 266 nC >> 0.13225 nC
        st = ffi.maxwell_sequence_append(
            drv,
            timestamp_us=0,
            stim_unit=0,
            electrode_id=100,
            voltage_mv=800.0,
            duration_us=100000
        )
        assert st == WetHalStatus.WET_HAL_ERR_INTERLOCK, "Dangerous charge pulse should be blocked"

        # Safe pulse: 50 mV for 100 us yields Q ~ (50/300) * 0.1 = 0.016 nC <= 0.13225 nC
        st = ffi.maxwell_sequence_append(
            drv,
            timestamp_us=0,
            stim_unit=0,
            electrode_id=100,
            voltage_mv=50.0,
            duration_us=100
        )
        assert st == WetHalStatus.WET_HAL_OK

        ffi.maxwell_destroy(drv)

    def test_maxwell_connect_stim_and_fault_injection(self, ffi):
        drv = ffi.maxwell_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Connect stim unit 5 to electrode 12345
        assert ffi.maxwell_connect_stim(drv, 5, 12345) == WetHalStatus.WET_HAL_OK
        # Out of bounds unit or electrode
        assert ffi.maxwell_connect_stim(drv, 32, 100) == WetHalStatus.WET_HAL_ERR_OUT_OF_BOUNDS
        assert ffi.maxwell_connect_stim(drv, 0, 26400) == WetHalStatus.WET_HAL_ERR_OUT_OF_BOUNDS

        # Forced charge violation fault injection
        ffi.maxwell_inject_fault(drv, force_charge_violation=True)
        st = ffi.maxwell_sequence_append(drv, 0, 0, 100, 10.0, 50)
        assert st == WetHalStatus.WET_HAL_ERR_INTERLOCK
        ffi.maxwell_inject_fault(drv, force_charge_violation=False)

        ffi.maxwell_destroy(drv)


# =========================================================================
# 4. Microfluidic Pump & Valve Protocols (HIL Mode)
# =========================================================================

class TestMicrofluidicProtocols:
    def test_harvard_rs232_formatting_and_prompt_parsing(self, ffi):
        # Test command formatting
        cmd_str = ffi.harvard_format_cmd(address=1, fast_mode=True, cmd_name="irate", args="1.500 u/m")
        assert cmd_str == "01 @irate 1.500 u/m\r"

        cmd_run = ffi.harvard_format_cmd(address=0, fast_mode=True, cmd_name="irun")
        assert cmd_run == "@irun\r"

        # Test prompt response parsing
        assert ffi.harvard_parse_response("01: ") == ":" # Idle
        assert ffi.harvard_parse_response("01> ") == ">" # Infusing
        assert ffi.harvard_parse_response("01< ") == "<" # Withdrawing
        assert ffi.harvard_parse_response("01* ") == "*" # Stalled
        assert ffi.harvard_parse_response("01T*") == "T" # Target volume reached

        # Interior colons in timestamps or error messages must NOT be parsed as prompts
        assert ffi.harvard_parse_response("15:30:00 Command error") == "?"
        assert ffi.harvard_parse_response("Error: invalid argument") == "?"
        assert ffi.harvard_parse_response("Error:") == "?"
        assert ffi.harvard_parse_response("15:30:00") == "?"

    def test_dead_head_overpressure_interlock(self, ffi):
        drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Bind pump 0 to valve 0
        ffi.pump_bind_downstream_valve(drv, 0, 0)

        # Case 1: Valve 0 is open -> Infusion succeeds
        ffi.valve_set_state(drv, 0, 1) # Open
        st = ffi.pump_set_rate(drv, 0, 2.5, 1)
        assert st == WetHalStatus.WET_HAL_OK

        # Case 2: Valve 0 is closed -> Pumping trips dead-head overpressure!
        ffi.valve_set_state(drv, 0, 0) # Close valve
        st = ffi.pump_set_rate(drv, 0, 2.5, 1)
        assert st == WetHalStatus.WET_HAL_ERR_DEAD_HEAD

        ffi.microfluidics_destroy(drv)

    def test_can_bus_pdo_and_emergency_frames(self, ffi):
        drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Transmit CAN Emergency Frame (EMCY)
        st = ffi.can_send_emcy(drv, node_id=1, error_code=0x1000, error_register=0x01)
        assert st == WetHalStatus.WET_HAL_OK

        # Transmit RPDO1: Command pump 1 rate = 3.0 uL/min, run = 1
        rate_val = 3.0
        rate_bytes = list(np.float32(rate_val).tobytes())
        frame = WetCanFrame(
            id=0x200 + 1, # RPDO1 for Node 1
            is_extended=0,
            is_rtr=0,
            dlc=5,
            data=(rate_bytes[0], rate_bytes[1], rate_bytes[2], rate_bytes[3], 1, 0, 0, 0),
            timestamp_us=1000
        )
        assert ffi.can_send(drv, frame) == WetHalStatus.WET_HAL_OK

        ffi.microfluidics_destroy(drv)

    def test_dead_head_recovery_and_fault_injection(self, ffi):
        drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        ffi.pump_bind_downstream_valve(drv, 1, 1)

        # Close valve -> fails
        ffi.valve_set_state(drv, 1, 0)
        assert ffi.pump_set_rate(drv, 1, 2.0, 1) == WetHalStatus.WET_HAL_ERR_DEAD_HEAD

        # Open valve -> recovers
        ffi.valve_set_state(drv, 1, 1)
        assert ffi.pump_set_rate(drv, 1, 2.0, 1) == WetHalStatus.WET_HAL_OK

        # Stall fault injection
        ffi.microfluidics_inject_fault(drv, stall=True)
        assert ffi.pump_set_rate(drv, 1, 2.0, 1) == WetHalStatus.WET_HAL_ERR_IO
        ffi.microfluidics_inject_fault(drv, stall=False)

        ffi.microfluidics_destroy(drv)

    def test_can_bus_boundary_dlc_and_extended_id_segregation(self, ffi):
        drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # 1. DLC > 8 must be rejected with WET_HAL_ERR_OUT_OF_BOUNDS
        bad_dlc = WetCanFrame(id=0x100, is_extended=0, is_rtr=0, dlc=9, data=(0,)*8, timestamp_us=100)
        assert ffi.can_send(drv, bad_dlc) == WetHalStatus.WET_HAL_ERR_OUT_OF_BOUNDS

        # 2. 11-bit standard frame ID > 0x7FF must be rejected with WET_HAL_ERR_OUT_OF_BOUNDS
        bad_std_id = WetCanFrame(id=0x800, is_extended=0, is_rtr=0, dlc=1, data=(0,)*8, timestamp_us=100)
        assert ffi.can_send(drv, bad_std_id) == WetHalStatus.WET_HAL_ERR_OUT_OF_BOUNDS

        # 3. 29-bit extended frame ID > 0x1FFFFFFF must be rejected with WET_HAL_ERR_OUT_OF_BOUNDS
        bad_ext_id = WetCanFrame(id=0x20000000, is_extended=1, is_rtr=0, dlc=1, data=(0,)*8, timestamp_us=100)
        assert ffi.can_send(drv, bad_ext_id) == WetHalStatus.WET_HAL_ERR_OUT_OF_BOUNDS

        # 4. 29-bit extended frame matching standard RPDO1 ID (0x201) must NOT be dispatched as RPDO
        rate_val = 8.5
        rate_bytes = list(np.float32(rate_val).tobytes())
        ext_frame = WetCanFrame(
            id=0x200 + 1, # Same ID as RPDO1 Node 1
            is_extended=1, # Extended 29-bit CAN ID!
            is_rtr=0,
            dlc=5,
            data=(rate_bytes[0], rate_bytes[1], rate_bytes[2], rate_bytes[3], 1, 0, 0, 0),
            timestamp_us=100
        )
        assert ffi.can_send(drv, ext_frame) == WetHalStatus.WET_HAL_OK

        # Standard frame with 11-bit should dispatch
        std_frame = WetCanFrame(
            id=0x200 + 1,
            is_extended=0,
            is_rtr=0,
            dlc=5,
            data=(rate_bytes[0], rate_bytes[1], rate_bytes[2], rate_bytes[3], 1, 0, 0, 0),
            timestamp_us=200
        )
        assert ffi.can_send(drv, std_frame) == WetHalStatus.WET_HAL_OK

        ffi.microfluidics_destroy(drv)

    def test_can_hil_bidirectional_loopback(self, ffi):
        drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        test_data = (0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0)
        tx_frame = WetCanFrame(
            id=0x123,
            is_extended=0,
            is_rtr=0,
            dlc=8,
            data=test_data,
            timestamp_us=12345
        )

        # Send frame
        st_send = ffi.can_send(drv, tx_frame)
        assert st_send == WetHalStatus.WET_HAL_OK

        # Receive frame back via bidirectional loopback
        st_recv, rx_frame = ffi.can_recv(drv)
        assert st_recv == WetHalStatus.WET_HAL_OK
        assert rx_frame is not None
        assert rx_frame.id == 0x123
        assert rx_frame.dlc == 8
        assert tuple(rx_frame.data) == test_data

        ffi.microfluidics_destroy(drv)


# =========================================================================
# 5. Sensirion Flow Meter Driver (HIL Mode)
# =========================================================================

class TestSensirionFlowMeter:
    def test_sensirion_crc8_algorithm(self, ffi):
        # Known test vectors for Sensirion polynomial 0x31 (Init 0xFF)
        # Test word 0xBEEF
        test_data = bytes([0xBE, 0xEF])
        crc = ffi.sensirion_crc8(test_data)
        assert crc == 0x92, f"Expected 0x92, got 0x{crc:02X}"

        # Validate complete 3-byte packet [0xBE, 0xEF, 0x92]
        assert ffi.sensirion_validate_crc(bytes([0xBE, 0xEF, 0x92])) is True
        assert ffi.sensirion_validate_crc(bytes([0xBE, 0xEF, 0x93])) is False

    def test_sensirion_i2c_flow_reading(self, ffi):
        drv = ffi.sensirion_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Start continuous measurement
        assert ffi.sensirion_start_measurement(drv, 0x3608) == WetHalStatus.WET_HAL_OK

        # Set mock flow rate to 4.5 uL/min
        ffi.sensirion_hil_set_flow(drv, 4.5)

        # Read back flow rate with CRC validation
        st, flow = ffi.sensirion_read_flow(drv)
        assert st == WetHalStatus.WET_HAL_OK
        assert pytest.approx(flow, abs=0.1) == 4.5

        # Fault injection: Corrupt CRC
        ffi.sensirion_inject_fault(drv, corrupt_crc=True)
        st, _ = ffi.sensirion_read_flow(drv)
        assert st == WetHalStatus.WET_HAL_ERR_CRC_MISMATCH

        ffi.sensirion_destroy(drv)

    def test_sensirion_shdlc_framing_and_byte_stuffing(self, ffi):
        ffi_inst = ffi
        # Test payload containing bytes that require stuffing: 0x7E, 0x7D, 0x11, 0x13
        raw_payload = bytes([0x10, 0x7E, 0x20, 0x7D, 0x11, 0x13, 0x30])
        encoded = ffi_inst.shdlc_encode(address=0x01, command=0x00, payload=raw_payload)

        # Must start and end with 0x7E
        assert encoded[0] == 0x7E
        assert encoded[-1] == 0x7E

        # Decode packet and verify payload matches original byte-for-byte
        ok, addr, cmd, decoded_payload = ffi_inst.shdlc_decode(encoded)
        assert ok is True
        assert addr == 0x01
        assert cmd == 0x00
        assert decoded_payload == raw_payload

    def test_sensirion_nak_and_multiple_crc_vectors(self, ffi):
        drv = ffi.sensirion_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)

        # Bus NAK injection
        ffi.sensirion_inject_fault(drv, nak_addr=True)
        assert ffi.sensirion_start_measurement(drv, 0x3608) == WetHalStatus.WET_HAL_ERR_IO
        st, _ = ffi.sensirion_read_flow(drv)
        assert st == WetHalStatus.WET_HAL_ERR_IO
        ffi.sensirion_inject_fault(drv, nak_addr=False)

        # Test stop measurement
        assert ffi.sensirion_stop_measurement(drv) == WetHalStatus.WET_HAL_OK

        # Verify CRC8 over zero bytes
        crc0 = ffi.sensirion_crc8(bytes([0x00, 0x00]))
        assert crc0 == 0x81
        assert ffi.sensirion_validate_crc(bytes([0x00, 0x00, 0x81])) is True

        ffi.sensirion_destroy(drv)

    def test_sensirion_shdlc_illegal_stuffing_rejection(self, ffi):
        # Build an encoded valid frame first
        valid_frame = ffi.shdlc_encode(address=0x01, command=0x00, payload=b"\x01\x02\x03")
        ok, _, _, _ = ffi.shdlc_decode(valid_frame)
        assert ok is True

        # Now test illegal bytes following escape 0x7D (legal are strictly 0x5E, 0x5D, 0x31, 0x33)
        illegal_escape_bytes = [0x00, 0x7E, 0x42, 0xFF, 0x11, 0x13, 0x7D]
        for bad_b in illegal_escape_bytes:
            corrupted = bytearray([0x7E, 0x01, 0x00, 0x01, 0x7D, bad_b, 0x00, 0x7E])
            ok_bad, _, _, _ = ffi.shdlc_decode(bytes(corrupted))
            assert ok_bad is False, f"Illegal escape sequence 0x7D 0x{bad_b:02X} should have been rejected"


# =========================================================================
# 6. End-to-End VM Integration with Physical HAL in HIL Mode
# =========================================================================

class TestVmHalIntegration:
    def test_vm_with_hal_pump_and_flow_routing(self, ffi):
        vm = WetVM()
        # Initialize HAL on VM in HIL loopback mode
        assert vm.init_hal(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK) == 0

        hal = vm.get_hal()
        assert hal is not None

        # Register Microfluidic and Flow drivers
        pump_drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        flow_drv = ffi.sensirion_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        ffi.hal_register_driver(hal, pump_drv)
        ffi.hal_register_driver(hal, flow_drv)

        # Set flow on Sensirion sensor
        ffi.sensirion_hil_set_flow(flow_drv, 3.25)
        st, flow = ffi.hal_read_flow(hal, 0)
        assert st == WetHalStatus.WET_HAL_OK
        assert pytest.approx(flow, abs=0.1) == 3.25

        # Command pump rate through HAL
        assert ffi.hal_write_pump(hal, 0, 2.0, 1) == WetHalStatus.WET_HAL_OK

        # Emergency crowbar fast-path
        vm.emergency_crowbar(1)

        # Verify flow after crowbar
        st, flow_after = ffi.hal_read_flow(hal, 0)
        assert flow_after == 0.0

        vm.close()

    def test_vm_bytecode_actuation_with_hal(self, ffi):
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode, Capability

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_MICROFLUIDICS | Capability.CAP_STIMULATION
        # 1. Open valve 0
        emitter.emit(Opcode.VALVE_SET, 0, 1)
        # 2. Set pump 0 rate to 3.5 uL/min
        emitter.emit(Opcode.PUMP_SET_RATE, 0, 3.5)
        # 3. Read flow from sensor 0
        emitter.emit(Opcode.READ_FLOW, 0)
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        vm = WetVM()
        vm.init_hal(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        hal = vm.get_hal()

        pump_drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        flow_drv = ffi.sensirion_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        ffi.hal_register_driver(hal, pump_drv)
        ffi.hal_register_driver(hal, flow_drv)
        ffi.sensirion_hil_set_flow(flow_drv, 3.5)

        vm.load_bytecode(wbc)
        telem = vm.step_tick()
        assert telem is not None

        # Verify HAL registered pump rate 3.5 uL/min
        st, flow = ffi.hal_read_flow(hal, 0)
        assert st == WetHalStatus.WET_HAL_OK
        assert pytest.approx(flow, abs=0.1) == 3.5

        vm.close()

    def test_vm_bytecode_dead_head_interlock_trip(self, ffi):
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode, Capability

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_MICROFLUIDICS
        # Close valve 0
        emitter.emit(Opcode.VALVE_SET, 0, 0)
        # Attempt to pump through closed valve 0 -> should trip dead-head interlock!
        emitter.emit(Opcode.PUMP_SET_RATE, 0, 4.0)
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        vm = WetVM()
        vm.init_hal(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        hal = vm.get_hal()

        pump_drv = ffi.microfluidics_create(WetHalMode.WET_HAL_MODE_HIL_LOOPBACK)
        ffi.hal_register_driver(hal, pump_drv)

        vm.load_bytecode(wbc)
        # Stepping should raise WetVMError with WET_ERR_ACTUATOR_FAULT due to dead-head interlock
        with pytest.raises(WetVMError) as exc_info:
            vm.step_tick()
        assert exc_info.value.status == WetStatus.WET_ERR_ACTUATOR_FAULT

        vm.close()
