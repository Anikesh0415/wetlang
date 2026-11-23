"""
WetLang Pillar 3: Multi-Threaded Concurrency & Lock-Free SPSC Queue Audit
Stress tests C99 lock-free ring buffers (wet_aer_ring_t and wet_spsc_ring_t)
under maximum multi-threaded contention across 4 concurrent hardware threads.
Validates:
  1. EXACT ZERO TORN READS: Every 16-byte packet payload matches sequential generation
  2. STRICT ZERO LOST EVENTS: Total produced == total consumed (1,000,000 packets)
  3. SEQUENCE DETERMINISM: Zero sequence inversions or packet corruptions
  4. HIGH-THROUGHPUT SATURATION: Measurement of Million Packets Per Second (MPPS)
  5. PYTHON-C HYBRID CONCURRENCY: Python threading stress test validating cross-boundary SPSC integrity
"""

import ctypes
import os
import sys
import time
import threading
from pathlib import Path

# FFI ctypes struct definition matching native/include/wet_verification.h
class WetConcurrencyResult(ctypes.Structure):
    _fields_ = [
        ("total_packets_produced", ctypes.c_uint64),
        ("total_packets_consumed", ctypes.c_uint64),
        ("torn_reads_detected", ctypes.c_uint64),
        ("sequence_errors", ctypes.c_uint64),
        ("num_threads", ctypes.c_uint32),
        ("elapsed_seconds", ctypes.c_double),
        ("throughput_mpps", ctypes.c_double),
    ]


def _load_wetvm():
    proj_root = Path(__file__).resolve().parent.parent
    dll_path = proj_root / "native" / "bin" / ("wetvm.dll" if sys.platform == "win32" else "wetvm.so")
    if not dll_path.exists():
        dll_path = proj_root / "native" / ("wetvm.dll" if sys.platform == "win32" else "wetvm.so")
    if not dll_path.exists():
        dll_path = proj_root / "bin" / ("wetvm.dll" if sys.platform == "win32" else "wetvm.so")
    return ctypes.CDLL(str(dll_path))


def test_native_c99_multithreaded_concurrency_stress():
    lib = _load_wetvm()
    lib.wet_run_concurrency_stress.argtypes = [ctypes.c_uint32, ctypes.POINTER(WetConcurrencyResult)]
    lib.wet_run_concurrency_stress.restype = ctypes.c_int

    total_packets = 1_000_000
    result = WetConcurrencyResult()

    t_start = time.perf_counter()
    res = lib.wet_run_concurrency_stress(ctypes.c_uint32(total_packets), ctypes.byref(result))
    elapsed_wall_s = time.perf_counter() - t_start

    throughput_mpps = (total_packets / elapsed_wall_s) / 1_000_000.0 if elapsed_wall_s > 0 else 0.0

    print("\n==========================================================================")
    print(" WetLang Pillar 3: Multi-Threaded Concurrency & Lock-Free SPSC Queue Audit")
    print("==========================================================================")
    print(f"  Concurrent Hardware Threads:   {result.num_threads} OS threads (2 Producers, 2 Consumers)")
    print(f"  Total Packets Produced:        {result.total_packets_produced:,}")
    print(f"  Total Packets Consumed:        {result.total_packets_consumed:,}")
    print(f"  Torn Reads Detected:           {result.torn_reads_detected} (Zero-tolerance)")
    print(f"  Sequence Ordering Errors:      {result.sequence_errors} (Zero-tolerance)")
    print(f"  Execution Wallclock Time:      {elapsed_wall_s:.3f} seconds")
    print(f"  Lock-Free Queue Throughput:    {throughput_mpps:.2f} Million Packets / sec (MPPS)")
    print("==========================================================================")

    assert res == 0, "Native concurrency stress engine reported error"
    assert result.total_packets_produced == total_packets
    assert result.total_packets_consumed == total_packets
    assert result.torn_reads_detected == 0, f"Detected {result.torn_reads_detected} torn reads!"
    assert result.sequence_errors == 0, f"Detected {result.sequence_errors} sequence errors!"
    assert throughput_mpps > 0.5, f"Throughput {throughput_mpps:.2f} MPPS below 0.5 MPPS target"


def test_hybrid_python_c_spsc_concurrency():
    """Stress test Python-level multi-threading interfacing with C99 AER functions."""
    from bindings.aer import WetAERRing, WetAERPacket

    ring = WetAERRing(capacity=2048, burst_limit_max_hz=50_000_000, num_channels=0)
    num_events = 20_000
    consumed_events = []
    errors = []

    def producer():
        for i in range(num_events):
            tick = i * 5
            channel = i % 64
            amp = 200 + (i % 300)
            while True:
                if ring.push(tick=tick, channel=channel, amp_uv=amp, flags=1):
                    break
                time.sleep(0)

    def consumer():
        while len(consumed_events) < num_events:
            batch = ring.pop_batch(max_count=128)
            for pkt in batch:
                ts_tick, ch_id, amp_uv, fl = pkt
                idx = len(consumed_events)
                exp_tick = idx * 5
                exp_ch = idx % 64
                exp_amp = 200 + (idx % 300)
                if ts_tick != exp_tick or ch_id != exp_ch or amp_uv != exp_amp:
                    errors.append((idx, ts_tick, exp_tick, ch_id, exp_ch))
                consumed_events.append(pkt)
            if not batch:
                time.sleep(0)

    t_prod = threading.Thread(target=producer)
    t_cons = threading.Thread(target=consumer)

    t_prod.start()
    t_cons.start()

    t_prod.join(timeout=15.0)
    t_cons.join(timeout=15.0)

    assert len(errors) == 0, f"Encountered {len(errors)} torn reads in hybrid Python-C test"
    assert len(consumed_events) == num_events, f"Expected {num_events} consumed, got {len(consumed_events)}"
