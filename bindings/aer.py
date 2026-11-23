"""
WetLang Address-Event Representation (AER) & High-Density MEA Scaling Bindings
Provides ctypes interfaces to wet_aer.h:
  - 16-byte binary AER packets (8-byte aligned, SIMD-friendly, zero unaligned fault hazard)
  - Lockless SPSC circular ring buffer with burst-tolerant rate tracking & per-channel noise quarantine
  - 5-tap Bartlett smoothed Nonlinear Energy Operator (NEO) spike detector with hardware blanking
  - Compressed Sparse Row (CSR) int8 synaptic matrix for 26,400 neural units
"""

from __future__ import annotations

import ctypes
import os
import sys
from pathlib import Path
from typing import List, Optional, Tuple
import numpy as np


def _find_wetvm_dll() -> str:
    """Locates the wetvm shared library."""
    pkg_dir = Path(__file__).resolve().parent
    candidates = [
        pkg_dir.parent / "native" / "bin" / "wetvm.dll",
        pkg_dir.parent / "native" / "wetvm.dll",
        pkg_dir.parent.parent / "native" / "bin" / "wetvm.dll",
        pkg_dir.parent.parent / "native" / "wetvm.dll",
        Path.cwd() / "native" / "bin" / "wetvm.dll",
        Path.cwd() / "native" / "wetvm.dll",
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    raise FileNotFoundError("Could not find wetvm.dll shared library")


_DLL_PATH = _find_wetvm_dll()
_LIB = ctypes.CDLL(_DLL_PATH)

WET_AER_CACHELINE_SIZE = 128


class WetAERPacket(ctypes.Structure):
    _pack_ = 8
    _fields_ = [
        ("timestamp_tick", ctypes.c_uint64),
        ("channel_id", ctypes.c_uint16),
        ("peak_amplitude_uv", ctypes.c_int16),
        ("flags", ctypes.c_uint16),
        ("reserved", ctypes.c_uint16),
    ]


assert ctypes.sizeof(WetAERPacket) == 16, f"Expected 16 bytes, got {ctypes.sizeof(WetAERPacket)}"


class WetAERRingStruct(ctypes.Structure):
    _fields_ = [
        ("pad0", ctypes.c_uint8 * WET_AER_CACHELINE_SIZE),
        ("head", ctypes.c_uint32),
        ("pad1", ctypes.c_uint8 * (WET_AER_CACHELINE_SIZE - 4)),
        ("tail", ctypes.c_uint32),
        ("pad2", ctypes.c_uint8 * (WET_AER_CACHELINE_SIZE - 4)),
        ("buffer", ctypes.POINTER(WetAERPacket)),
        ("capacity", ctypes.c_uint32),
        ("mask", ctypes.c_uint32),
        ("total_pushed", ctypes.c_uint64),
        ("total_dropped", ctypes.c_uint64),
        ("last_stat_tick", ctypes.c_uint64),
        ("spikes_in_window", ctypes.c_uint32),
        ("current_spike_rate_hz", ctypes.c_double),
        ("current_bandwidth_mbps", ctypes.c_double),
        ("burst_limit_max_hz", ctypes.c_uint32),
        ("is_burst_tripped", ctypes.c_uint8),
        ("channel_spike_counts", ctypes.POINTER(ctypes.c_uint16)),
        ("monitored_channels", ctypes.c_uint32),
        ("max_channel_hz", ctypes.c_uint16),
    ]


class WetNEODetectorStruct(ctypes.Structure):
    _fields_ = [
        ("num_channels", ctypes.c_uint32),
        ("threshold_multiplier", ctypes.c_float),
        ("refractory_ticks", ctypes.c_uint32),
        ("v_baseline", ctypes.POINTER(ctypes.c_float)),
        ("prev_v1", ctypes.POINTER(ctypes.c_float)),
        ("prev_v2", ctypes.POINTER(ctypes.c_float)),
        ("psi_history", ctypes.POINTER(ctypes.c_float) * 4),
        ("refract_left", ctypes.POINTER(ctypes.c_uint32)),
        ("blanking_left", ctypes.POINTER(ctypes.c_uint32)),
        ("running_neo_mean", ctypes.POINTER(ctypes.c_float)),
        ("sample_count", ctypes.POINTER(ctypes.c_uint32)),
        ("total_detected", ctypes.c_uint64),
    ]


class WetCSRMatrixStruct(ctypes.Structure):
    _fields_ = [
        ("num_rows", ctypes.c_uint32),
        ("num_cols", ctypes.c_uint32),
        ("nnz", ctypes.c_uint32),
        ("row_ptr", ctypes.POINTER(ctypes.c_uint32)),
        ("col_idx", ctypes.POINTER(ctypes.c_uint16)),
        ("weights_int8", ctypes.POINTER(ctypes.c_int8)),
        ("weight_scale_ns", ctypes.c_float),
    ]


# FFI Signatures
_LIB.wet_aer_ring_init.argtypes = [
    ctypes.POINTER(WetAERRingStruct),
    ctypes.POINTER(WetAERPacket),
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.POINTER(ctypes.c_uint16),
    ctypes.c_uint32,
]
_LIB.wet_aer_ring_init.restype = ctypes.c_int

_LIB.wet_aer_push.argtypes = [
    ctypes.POINTER(WetAERRingStruct),
    ctypes.c_uint64,
    ctypes.c_uint16,
    ctypes.c_int16,
    ctypes.c_uint16,
]
_LIB.wet_aer_push.restype = ctypes.c_int

_LIB.wet_aer_pop_batch.argtypes = [
    ctypes.POINTER(WetAERRingStruct),
    ctypes.POINTER(WetAERPacket),
    ctypes.c_uint32,
]
_LIB.wet_aer_pop_batch.restype = ctypes.c_uint32

_LIB.wet_aer_available.argtypes = [ctypes.POINTER(WetAERRingStruct)]
_LIB.wet_aer_available.restype = ctypes.c_uint32

_LIB.wet_aer_get_stats.argtypes = [
    ctypes.POINTER(WetAERRingStruct),
    ctypes.c_uint64,
    ctypes.POINTER(ctypes.c_uint64),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
]
_LIB.wet_aer_get_stats.restype = None

_LIB.wet_neo_init.argtypes = [
    ctypes.POINTER(WetNEODetectorStruct),
    ctypes.c_uint32,
    ctypes.c_float,
    ctypes.c_uint32,
]
_LIB.wet_neo_init.restype = ctypes.c_int

_LIB.wet_neo_free.argtypes = [ctypes.POINTER(WetNEODetectorStruct)]
_LIB.wet_neo_free.restype = None

_LIB.wet_neo_set_blanking.argtypes = [
    ctypes.POINTER(WetNEODetectorStruct),
    ctypes.c_uint16,
    ctypes.c_uint32,
]
_LIB.wet_neo_set_blanking.restype = None

_LIB.wet_neo_process_sample.argtypes = [
    ctypes.POINTER(WetNEODetectorStruct),
    ctypes.c_uint16,
    ctypes.c_float,
    ctypes.c_uint64,
    ctypes.POINTER(WetAERRingStruct),
]
_LIB.wet_neo_process_sample.restype = ctypes.c_int

_LIB.wet_csr_init.argtypes = [
    ctypes.POINTER(WetCSRMatrixStruct),
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_uint32,
    ctypes.c_float,
]
_LIB.wet_csr_init.restype = ctypes.c_int

_LIB.wet_csr_free.argtypes = [ctypes.POINTER(WetCSRMatrixStruct)]
_LIB.wet_csr_free.restype = None

_LIB.wet_csr_spmv_spikes.argtypes = [
    ctypes.POINTER(WetCSRMatrixStruct),
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_float),
]
_LIB.wet_csr_spmv_spikes.restype = None


class WetAERRing:
    """High-speed lockless SPSC ring buffer for 16-byte AER packets."""

    def __init__(self, capacity: int = 16384, burst_limit_max_hz: int = 5000000, num_channels: int = 64):
        if (capacity & (capacity - 1)) != 0 or capacity < 2:
            raise ValueError(f"Capacity must be a power of 2, got {capacity}")
        self.capacity = capacity
        self._c_ring = WetAERRingStruct()
        self._buf_array = (WetAERPacket * capacity)()
        self._ch_counts = (ctypes.c_uint16 * num_channels)() if num_channels > 0 else None
        res = _LIB.wet_aer_ring_init(
            ctypes.byref(self._c_ring),
            self._buf_array,
            capacity,
            burst_limit_max_hz,
            self._ch_counts,
            num_channels,
        )
        if res != 0:
            raise RuntimeError(f"wet_aer_ring_init failed with code {res}")

    def push(self, tick: int, channel: int, amp_uv: int = 0, flags: int = 0) -> bool:
        res = _LIB.wet_aer_push(ctypes.byref(self._c_ring), tick, channel, amp_uv, flags)
        return res == 0

    def pop_batch(self, max_count: int = 256) -> List[Tuple[int, int, int, int]]:
        out_buf = (WetAERPacket * max_count)()
        popped = _LIB.wet_aer_pop_batch(ctypes.byref(self._c_ring), out_buf, max_count)
        return [
            (
                out_buf[i].timestamp_tick,
                out_buf[i].channel_id,
                out_buf[i].peak_amplitude_uv,
                out_buf[i].flags,
            )
            for i in range(popped)
        ]

    @property
    def available(self) -> int:
        return _LIB.wet_aer_available(ctypes.byref(self._c_ring))

    def get_stats(self, current_tick: int) -> Tuple[int, float, float]:
        tot = ctypes.c_uint64()
        rate = ctypes.c_double()
        mbps = ctypes.c_double()
        _LIB.wet_aer_get_stats(
            ctypes.byref(self._c_ring),
            current_tick,
            ctypes.byref(tot),
            ctypes.byref(rate),
            ctypes.byref(mbps),
        )
        return tot.value, rate.value, mbps.value


class WetNEODetector:
    """Nonlinear Energy Operator Spike Detector with 5-tap Bartlett filter & artifact blanking."""

    def __init__(self, num_channels: int, threshold_mult: float = 4.0, refract_ticks: int = 10):
        self._c_det = WetNEODetectorStruct()
        self.num_channels = num_channels
        res = _LIB.wet_neo_init(ctypes.byref(self._c_det), num_channels, threshold_mult, refract_ticks)
        if res != 0:
            raise RuntimeError(f"wet_neo_init failed with code {res}")

    def close(self):
        _LIB.wet_neo_free(ctypes.byref(self._c_det))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def set_blanking(self, channel: int, blanking_ticks: int):
        _LIB.wet_neo_set_blanking(ctypes.byref(self._c_det), channel, blanking_ticks)

    def process_sample(self, channel: int, voltage: float, current_tick: int, ring: Optional[WetAERRing] = None) -> bool:
        ring_ptr = ctypes.byref(ring._c_ring) if ring else None
        res = _LIB.wet_neo_process_sample(ctypes.byref(self._c_det), channel, voltage, current_tick, ring_ptr)
        return bool(res)


class WetCSRMatrix:
    """Compressed Sparse Row int8 synaptic matrix for high-density neural twins."""

    def __init__(self, rows: int, cols: int, nnz: int, scale_ns: float = 0.2):
        self.rows = rows
        self.cols = cols
        self.nnz = nnz
        self._c_csr = WetCSRMatrixStruct()
        res = _LIB.wet_csr_init(ctypes.byref(self._c_csr), rows, cols, nnz, scale_ns)
        if res != 0:
            raise RuntimeError(f"wet_csr_init failed with code {res}")

    def close(self):
        _LIB.wet_csr_free(ctypes.byref(self._c_csr))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def set_data(self, row_ptr: np.ndarray, col_idx: np.ndarray, weights_int8: np.ndarray):
        row_ptr = np.ascontiguousarray(row_ptr, dtype=np.uint32)
        col_idx = np.ascontiguousarray(col_idx, dtype=np.uint16)
        weights_int8 = np.ascontiguousarray(weights_int8, dtype=np.int8)

        ctypes.memmove(self._c_csr.row_ptr, row_ptr.ctypes.data, row_ptr.nbytes)
        ctypes.memmove(self._c_csr.col_idx, col_idx.ctypes.data, col_idx.nbytes)
        ctypes.memmove(self._c_csr.weights_int8, weights_int8.ctypes.data, weights_int8.nbytes)

    def spmv(self, spike_events: np.ndarray) -> np.ndarray:
        spike_arr = np.ascontiguousarray(spike_events, dtype=np.uint8)
        out_cond = np.zeros(self.cols, dtype=np.float32)

        _LIB.wet_csr_spmv_spikes(
            ctypes.byref(self._c_csr),
            spike_arr.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
            out_cond.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
        )
        return out_cond
