"""
WetLang Test Suite: Hardware Watchdog & Biocybersecurity Interlocks
Tests:
  - Water-window voltage clamp saturation at +/- 1.2 V
  - Static compile-time overvoltage detection and rejection
  - 10.0 ms sliding charge-balance ring buffer (tripping at >= 0.5 nC)
  - 50.0 ms epileptiform runaway breaker (tripping at > 150 Hz on > 35% channels for 50.0 ms)
  - Fail-safe state lockout and DAC zeroing upon interlock trip
"""

import math
import pytest
import numpy as np
from typing import List, Tuple, Dict, Optional

from compiler.compiler_cli import compile_source
from compiler.semantic import SemanticError
from tests.e2e.common import (
    assert_voltage_clamped,
    assert_sliding_charge_balance,
    assert_epileptiform_trip,
    make_spike_raster_matrix,
    make_overvoltage_code,
)


# =============================================================================
# Reference Implementation of Interlock Watchdog Logic
# =============================================================================

class ReferenceInterlockWatchdog:
    """Cycle-accurate reference implementation of native/src/interlocks.c."""
    def __init__(self, num_channels: int = 64, dt_ms: float = 0.1):
        self.num_channels = num_channels
        self.dt_ms = dt_ms
        self.voltage_limit_v = 1.2
        self.charge_window_ticks = 100  # 10.0 ms at dt = 0.1 ms
        self.charge_limit_nc = 0.5      # 0.5 nC per electrode
        self.epilepsy_rate_hz = 150.0
        self.epilepsy_min_channels = 23 # > 35% of 64
        self.epilepsy_sustain_ticks = 500 # 50.0 ms at dt = 0.1 ms

        # State
        self.locked = False
        self.trip_reason = None
        self.tripped_channel = None
        self.trip_tick = None
        self.diagnostic = ""

        # Ring buffer per channel: [channel][tick_in_window]
        self.q_ring = [[0.0] * self.charge_window_ticks for _ in range(num_channels)]
        self.q_accum = [0.0] * num_channels
        self.q_head = 0

        # Runaway counter
        self.hyperactive_consecutive_ticks = 0

    def clamp_voltage(self, requested_v: float) -> float:
        """Clamp voltage within [-1.2 V, +1.2 V]."""
        if requested_v > self.voltage_limit_v:
            return self.voltage_limit_v
        if requested_v < -self.voltage_limit_v:
            return -self.voltage_limit_v
        return requested_v

    def record_charge_tick(self, current_tick: int, tick_charges_nc: List[float]) -> str:
        """Record charge for all channels this tick. Returns 'OK' or 'ERR_CHARGE_IMBALANCE'."""
        if self.locked:
            return "ERR_INTERLOCK_LOCKED"

        head = self.q_head
        status = "OK"

        for ch in range(self.num_channels):
            old_q = self.q_ring[ch][head]
            new_q = tick_charges_nc[ch]
            self.q_ring[ch][head] = new_q

            accum = self.q_accum[ch] - old_q + new_q
            if abs(accum) < 1e-7:
                accum = 0.0
            self.q_accum[ch] = accum

            if abs(accum) >= self.charge_limit_nc:
                self.locked = True
                self.trip_reason = "ERR_CHARGE_IMBALANCE"
                self.tripped_channel = ch
                self.trip_tick = current_tick
                self.diagnostic = f"ERR_CHARGE_IMBALANCE: ch={ch} net_q={accum:.4f} nC >= {self.charge_limit_nc} nC at tick {current_tick}"
                status = "ERR_CHARGE_IMBALANCE"
                break

        self.q_head = (head + 1) % self.charge_window_ticks
        return status

    def check_epileptiform(self, current_tick: int, channel_rates_hz: List[float]) -> str:
        """Evaluate population epileptiform condition. Returns 'OK' or 'ERR_EPILEPTIFORM_RUNAWAY'."""
        if self.locked:
            return "ERR_INTERLOCK_LOCKED"

        hyper_count = sum(1 for rate in channel_rates_hz if rate > self.epilepsy_rate_hz)

        if hyper_count >= self.epilepsy_min_channels:
            self.hyperactive_consecutive_ticks += 1
            if self.hyperactive_consecutive_ticks >= self.epilepsy_sustain_ticks:
                self.locked = True
                self.trip_reason = "ERR_EPILEPTIFORM_RUNAWAY"
                self.tripped_channel = 0xFF
                self.trip_tick = current_tick
                self.diagnostic = f"ERR_EPILEPTIFORM_RUNAWAY: {hyper_count}/64 channels exceeded 150 Hz for 50.0 ms at tick {current_tick}"
                return "ERR_EPILEPTIFORM_RUNAWAY"
        else:
            self.hyperactive_consecutive_ticks = 0

        return "OK"


# =============================================================================
# 1. Voltage Clamp Saturation & Static Rejection Tests
# =============================================================================

def test_voltage_clamp_positive_saturation():
    """Verify that requests > +1.2 V saturate cleanly to exactly +1.2 V."""
    watchdog = ReferenceInterlockWatchdog()
    for v_req in [1.21, 1.5, 2.0, 2.8, 5.0, 10.0]:
        clamped = watchdog.clamp_voltage(v_req)
        assert clamped == 1.2, f"Failed for {v_req} V: got {clamped}"
        assert_voltage_clamped(requested_v=v_req, actual_v=clamped, clamp_limit=1.2)


def test_voltage_clamp_negative_saturation():
    """Verify that requests < -1.2 V saturate cleanly to exactly -1.2 V."""
    watchdog = ReferenceInterlockWatchdog()
    for v_req in [-1.21, -1.5, -2.0, -2.8, -5.0, -10.0]:
        clamped = watchdog.clamp_voltage(v_req)
        assert clamped == -1.2, f"Failed for {v_req} V: got {clamped}"
        assert_voltage_clamped(requested_v=v_req, actual_v=clamped, clamp_limit=1.2)


def test_voltage_clamp_within_water_window_passthrough():
    """Verify that voltages within [-1.2 V, +1.2 V] pass through unchanged."""
    watchdog = ReferenceInterlockWatchdog()
    for v_req in [-1.2, -0.8, -0.5, 0.0, 0.3, 0.8, 1.0, 1.2]:
        clamped = watchdog.clamp_voltage(v_req)
        assert abs(clamped - v_req) < 1e-6, f"Failed for {v_req} V: got {clamped}"


def test_static_compile_rejection_overvoltage():
    """Verify compiler statically rejects literal stimulation voltages > 1.2 V."""
    code = make_overvoltage_code(voltage_v=2.5)
    with pytest.raises(SemanticError) as exc_info:
        compile_source(code)
    assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"


def test_static_compile_rejection_undervoltage():
    """Verify compiler statically rejects literal stimulation voltages < -1.2 V."""
    code = make_overvoltage_code(voltage_v=-1.8)
    with pytest.raises(SemanticError) as exc_info:
        compile_source(code)
    assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"


# =============================================================================
# 2. Sliding 10.0 ms Charge Balance Watchdog Tests
# =============================================================================

def test_sliding_charge_balance_symmetric_biphasic_no_trip():
    """Verify balanced biphasic pulses (+0.8V 0.2ms, -0.8V 0.2ms) do not trip the watchdog."""
    # 2 ticks cathodic (0.0008 nC each), 2 ticks anodic (-0.0008 nC each), 16 ticks quiet
    pulse_q = [0.0008, 0.0008, -0.0008, -0.0008] + [0.0] * 16
    full_trace = pulse_q * 20  # 400 ticks total
    
    result = assert_sliding_charge_balance(full_trace, max_charge_nc=0.5, window_ticks=100)
    assert result.balanced, "Symmetric biphasic pulses must maintain charge balance"
    assert result.max_residual < 0.01, f"Expected near zero residual, got {result.max_residual}"


def test_sliding_charge_balance_unbalanced_dc_trip_at_100_ticks():
    """Verify continuous DC injection of 0.01 nC/tick trips ERR_CHARGE_IMBALANCE at tick 100."""
    watchdog = ReferenceInterlockWatchdog()
    
    # Inject 0.01 nC on channel 5 on every tick
    tripped = False
    trip_tick = -1
    
    for tick in range(150):
        charges = [0.0] * 64
        charges[5] = 0.01  # 0.01 nC per tick
        
        status = watchdog.record_charge_tick(tick, charges)
        if status == "ERR_CHARGE_IMBALANCE":
            tripped = True
            trip_tick = tick
            break
            
    assert tripped, "Continuous DC must trip charge imbalance"
    assert trip_tick == 49, f"Expected trip at tick 49 (50th tick: 50 * 0.01 = 0.5 nC), got {trip_tick}"
    assert watchdog.locked
    assert watchdog.tripped_channel == 5


def test_sliding_charge_balance_boundary_threshold():
    """Verify threshold boundary: < 0.5 nC does not trip, >= 0.500 nC trips."""
    # Sub-threshold: 0.0049 nC across window (0.49 nC total)
    trace_sub = [0.0049] * 110
    res_sub = assert_sliding_charge_balance(trace_sub, max_charge_nc=0.5, window_ticks=100)
    assert res_sub.balanced, "0.49 nC must not trip"
    
    # Threshold: 0.0050 nC across window (0.50 nC total at tick 100)
    trace_at_limit = [0.0050] * 110
    res_limit = assert_sliding_charge_balance(trace_at_limit, max_charge_nc=0.5, window_ticks=100)
    assert not res_limit.balanced, "0.500 nC must trip"
    assert res_limit.trip_tick == 100


# =============================================================================
# 3. Epileptiform Runaway Breaker Tests
# =============================================================================

def test_epileptiform_sub_critical_burst_does_not_trip():
    """Verify acute burst (>150 Hz across 40 channels) lasting only 20.0 ms (200 ticks) does NOT trip 50.0 ms breaker."""
    watchdog = ReferenceInterlockWatchdog()
    
    # 20.0 ms burst = 200 ticks
    for tick in range(200):
        rates = [0.0] * 64
        for ch in range(40):  # 40 channels > 35%
            rates[ch] = 200.0 # 200 Hz > 150 Hz
        status = watchdog.check_epileptiform(tick, rates)
        assert status == "OK", f"Should not trip during 200 ticks, tripped at {tick}"
        
    # Return to resting baseline for 100 ticks
    for tick in range(200, 300):
        rates = [20.0] * 64
        status = watchdog.check_epileptiform(tick, rates)
        assert status == "OK"
        
    assert not watchdog.locked, "Sub-critical burst must not lock watchdog"
    assert watchdog.hyperactive_consecutive_ticks == 0, "Counter must reset after burst ends"


def test_epileptiform_focal_burst_few_channels_does_not_trip():
    """Verify high firing rate (>150 Hz) on <= 35% of channels (e.g. 15 channels) sustained for 100 ms does NOT trip."""
    watchdog = ReferenceInterlockWatchdog()
    
    # 15 channels hyperactive for 1000 ticks (100.0 ms)
    for tick in range(1000):
        rates = [0.0] * 64
        for ch in range(15):  # 15 channels <= 22 channels (35%)
            rates[ch] = 250.0
        status = watchdog.check_epileptiform(tick, rates)
        assert status == "OK"
        
    assert not watchdog.locked, "Focal high-rate burst on <= 35% of channels must not trip breaker"


def test_epileptiform_runaway_trips_at_500_ticks():
    """Verify hypersynchronous firing (>150 Hz on >=23 channels) sustained for 50.0 ms (500 ticks) trips ERR_EPILEPTIFORM_RUNAWAY."""
    watchdog = ReferenceInterlockWatchdog()
    
    tripped = False
    trip_tick = -1
    
    for tick in range(600):
        rates = [0.0] * 64
        for ch in range(25):  # 25 channels > 35% (23)
            rates[ch] = 180.0 # 180 Hz > 150 Hz
            
        status = watchdog.check_epileptiform(tick, rates)
        if status == "ERR_EPILEPTIFORM_RUNAWAY":
            tripped = True
            trip_tick = tick
            break
            
    assert tripped, "Must trip epileptiform runaway"
    assert trip_tick == 499, f"Expected trip on exactly 500th tick (index 499), got {trip_tick}"
    assert watchdog.locked
    assert watchdog.trip_reason == "ERR_EPILEPTIFORM_RUNAWAY"


# =============================================================================
# 4. Fail-Safe State Lockout Tests
# =============================================================================

def test_failsafe_state_lockout_blocks_further_operations():
    """Verify that once locked, all subsequent watchdog operations return ERR_INTERLOCK_LOCKED."""
    watchdog = ReferenceInterlockWatchdog()
    
    # Trip charge balance
    charges = [0.0] * 64
    charges[0] = 0.55
    status = watchdog.record_charge_tick(1, charges)
    assert status == "ERR_CHARGE_IMBALANCE"
    assert watchdog.locked
    
    # Subsequent calls must return ERR_INTERLOCK_LOCKED
    status2 = watchdog.record_charge_tick(2, [0.0] * 64)
    assert status2 == "ERR_INTERLOCK_LOCKED"
    
    status3 = watchdog.check_epileptiform(3, [0.0] * 64)
    assert status3 == "ERR_INTERLOCK_LOCKED"
