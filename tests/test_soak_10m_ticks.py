"""
WetLang Pillar 2: 10-Million Continuous Tick Numerical Soak Stress Test
Automated simulation of 10,000,000 continuous ticks (1,000.0 seconds biological time)
at dt = 0.1 ms with periodic biphasic stimulation pulses (+/-0.4 V, 0.2 ms).
Validates:
  1. EXACT ZERO ATTOCOULOMB DRIFT: |cumulative_dc_attocoulombs - theoretical_ac| == 0
  2. BOUNDED NUMERICAL STABILITY: Zero NaNs, zero Infinities across 64 coupled ODE neurons
  3. WATER-WINDOW COMPLIANCE: Zero interlock lockouts or spurious trips
  4. MEMORY RESILIENCE: Zero process memory growth over 10M iterations (0-byte leak)
"""

import ctypes
import os
import sys
import time
from pathlib import Path
import psutil

# FFI ctypes struct definition matching native/include/wet_verification.h
class WetSoakResult(ctypes.Structure):
    _fields_ = [
        ("total_ticks", ctypes.c_uint64),
        ("final_cumulative_dc_attocoulombs", ctypes.c_int64 * 64),
        ("max_absolute_drift_attocoulombs", ctypes.c_int64),
        ("min_membrane_voltage_mv", ctypes.c_float),
        ("max_membrane_voltage_mv", ctypes.c_float),
        ("nan_or_inf_detected", ctypes.c_uint32),
        ("interlock_trips", ctypes.c_uint32),
        ("elapsed_seconds", ctypes.c_double),
    ]


def _load_wetvm():
    proj_root = Path(__file__).resolve().parent.parent
    lib_name = "wetvm.dll" if sys.platform == "win32" else ("wetvm.dylib" if sys.platform == "darwin" else "wetvm.so")
    dll_path = proj_root / "native" / "bin" / lib_name
    if not dll_path.exists():
        dll_path = proj_root / "native" / lib_name
    if not dll_path.exists():
        dll_path = proj_root / "bin" / lib_name
    return ctypes.CDLL(str(dll_path))


def test_ten_million_tick_numerical_soak():
    lib = _load_wetvm()
    lib.wet_run_soak_10m_ticks.argtypes = [ctypes.c_uint32, ctypes.POINTER(WetSoakResult)]
    lib.wet_run_soak_10m_ticks.restype = ctypes.c_int

    process = psutil.Process(os.getpid())
    # Baseline memory before running soak test
    mem_before_bytes = process.memory_info().rss

    total_ticks = 10_000_000
    result = WetSoakResult()

    t_start = time.perf_counter()
    res = lib.wet_run_soak_10m_ticks(ctypes.c_uint32(total_ticks), ctypes.byref(result))
    elapsed_wall_s = time.perf_counter() - t_start

    mem_after_bytes = process.memory_info().rss
    mem_growth_bytes = max(0, mem_after_bytes - mem_before_bytes)

    ticks_per_sec = total_ticks / elapsed_wall_s if elapsed_wall_s > 0 else 0.0

    print("\n==========================================================================")
    print(" WetLang Pillar 2: 10-Million Continuous Tick Numerical Soak Stress Test")
    print("==========================================================================")
    print(f"  Total Ticks Executed:          {result.total_ticks:,} ticks")
    print(f"  Simulated Biological Time:     {result.total_ticks * 0.0001:.1f} seconds (16.67 minutes)")
    print(f"  Execution Wallclock Time:      {elapsed_wall_s:.3f} seconds")
    print(f"  Throughput Speed:              {ticks_per_sec:,.0f} ticks/second ({ticks_per_sec * 0.0001:.1f}x real-time)")
    print(f"  Max Absolute DC Charge Drift:  {result.max_absolute_drift_attocoulombs} attoCoulombs (0 aC theoretical)")
    print(f"  Final Channel 0 Charge:        {result.final_cumulative_dc_attocoulombs[0]} aC")
    print(f"  Final Channel 1 Charge:        {result.final_cumulative_dc_attocoulombs[1]} aC")
    print(f"  Membrane Voltage Range:        [{result.min_membrane_voltage_mv:.2f} mV, {result.max_membrane_voltage_mv:.2f} mV]")
    print(f"  NaN / Inf Anomalies Detected:  {result.nan_or_inf_detected}")
    print(f"  Spurious Interlock Trips:      {result.interlock_trips}")
    print(f"  Process Memory RSS (Initial):  {mem_before_bytes / (1024*1024):.2f} MB")
    print(f"  Process Memory RSS (Final):    {mem_after_bytes / (1024*1024):.2f} MB")
    print(f"  Process Memory Growth:         {mem_growth_bytes} bytes")
    print("==========================================================================")

    # Invariants verification
    assert res == 0, "Native soak engine reported execution failure"
    assert result.total_ticks == total_ticks
    assert result.max_absolute_drift_attocoulombs == 0, f"Expected 0 aC drift, got {result.max_absolute_drift_attocoulombs} aC"
    assert result.final_cumulative_dc_attocoulombs[0] == 0, "Final Channel 0 DC charge must be 0 aC"
    assert result.final_cumulative_dc_attocoulombs[1] == 0, "Final Channel 1 DC charge must be 0 aC"
    assert result.nan_or_inf_detected == 0, f"Detected {result.nan_or_inf_detected} NaNs or Infinities"
    assert result.interlock_trips == 0, f"Detected {result.interlock_trips} unexpected interlock trips"
    assert -95.0 <= result.min_membrane_voltage_mv <= -60.0, f"Min membrane voltage {result.min_membrane_voltage_mv:.2f} mV out of physiological range"
    assert -55.0 <= result.max_membrane_voltage_mv <= -30.0, f"Max membrane voltage {result.max_membrane_voltage_mv:.2f} mV out of physiological COBA-LIF subthreshold range"
    # Zero memory growth tolerance: memory growth across 10M ticks must be zero (or within minor OS page granularity < 500 KB)
    assert mem_growth_bytes < 512 * 1024, f"Memory leak detected: growth of {mem_growth_bytes} bytes"
