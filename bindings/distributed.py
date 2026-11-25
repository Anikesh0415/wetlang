"""
WetLang Distributed Multi-Organoid Time-Triggered Synchronization (IEEE 1588 PTP / TSN)
Provides ctypes interfaces to wet_distributed.h:
  - 32-byte Time-Sensitive Networking (TSN) spike frame layout
  - Slew-only IEEE 1588 PTP hardware clock disciplining with stimulation safety inhibits
  - O(1) Hierarchical Timing Wheel for heterogeneous axonal delays (eliminating Head-of-Line blocking)
  - Cross-chamber epileptiform rate governor & stimulus artifact echo blanking
"""

from __future__ import annotations

import ctypes
from pathlib import Path
from typing import List, Optional, Tuple
import numpy as np


from bindings.ffi import _find_library_path


def _find_wetvm_dll() -> str:
    """Locates the platform-appropriate wetvm shared library (.dll / .so / .dylib)."""
    return str(_find_library_path())


_DLL_PATH = _find_wetvm_dll()
_LIB = ctypes.CDLL(_DLL_PATH)

WET_DIST_CACHELINE_SIZE = 128
WET_TIMING_WHEEL_SLOTS = 512
WET_WHEEL_BUCKET_CAP = 64
WET_MAX_CHAMBERS = 16


class WetTSNFrame(ctypes.Structure):
    _pack_ = 8
    _fields_ = [
        ("source_epoch_ns", ctypes.c_uint64),
        ("release_epoch_ns", ctypes.c_uint64),
        ("sequence_number", ctypes.c_uint32),
        ("source_chamber", ctypes.c_uint16),
        ("target_chamber", ctypes.c_uint16),
        ("source_channel", ctypes.c_uint16),
        ("target_channel", ctypes.c_uint16),
        ("spike_amplitude_uv", ctypes.c_int16),
        ("flags", ctypes.c_uint16),
    ]


assert ctypes.sizeof(WetTSNFrame) == 32, f"Expected 32 bytes, got {ctypes.sizeof(WetTSNFrame)}"


class WetPTPClockStruct(ctypes.Structure):
    _fields_ = [
        ("local_time_ns", ctypes.c_uint64),
        ("grandmaster_time_ns", ctypes.c_uint64),
        ("accumulated_offset_ns", ctypes.c_int64),
        ("mean_path_delay_ns", ctypes.c_int64),
        ("frequency_slew_ppm", ctypes.c_double),
        ("integral_err_ns", ctypes.c_double),
        ("kp", ctypes.c_double),
        ("ki", ctypes.c_double),
        ("is_synchronized", ctypes.c_uint8),
        ("stim_inhibited", ctypes.c_uint8),
        ("sync_sequence", ctypes.c_uint32),
    ]


class WetTimingWheelBucket(ctypes.Structure):
    _fields_ = [
        ("count", ctypes.c_uint32),
        ("frames", WetTSNFrame * WET_WHEEL_BUCKET_CAP),
    ]


class WetTimingWheelStruct(ctypes.Structure):
    _fields_ = [
        ("buckets", WetTimingWheelBucket * WET_TIMING_WHEEL_SLOTS),
        ("current_wheel_tick", ctypes.c_uint64),
        ("chamber_id", ctypes.c_uint32),
        ("total_scheduled", ctypes.c_uint64),
        ("total_dispatched", ctypes.c_uint64),
        ("late_drops", ctypes.c_uint64),
        ("bucket_overflows", ctypes.c_uint64),
        ("rate_governor_window_spikes", ctypes.c_uint32),
        ("rate_governor_last_tick", ctypes.c_uint64),
        ("is_epileptiform_tripped", ctypes.c_uint8),
        ("tx_blanking_ticks_remaining", ctypes.c_uint32 * WET_MAX_CHAMBERS),
    ]


# FFI Signatures
_LIB.wet_ptp_init.argtypes = [ctypes.POINTER(WetPTPClockStruct), ctypes.c_double, ctypes.c_double]
_LIB.wet_ptp_init.restype = None

_LIB.wet_ptp_update_offset.argtypes = [
    ctypes.POINTER(WetPTPClockStruct),
    ctypes.c_uint64,
    ctypes.c_uint64,
    ctypes.c_uint64,
    ctypes.c_uint64,
]
_LIB.wet_ptp_update_offset.restype = None

_LIB.wet_ptp_get_disciplined_time_ns.argtypes = [ctypes.POINTER(WetPTPClockStruct), ctypes.c_uint64]
_LIB.wet_ptp_get_disciplined_time_ns.restype = ctypes.c_uint64

_LIB.wet_tsn_serialize_frame.argtypes = [
    ctypes.POINTER(WetTSNFrame),
    ctypes.c_uint64,
    ctypes.c_uint64,
    ctypes.c_uint32,
    ctypes.c_uint16,
    ctypes.c_uint16,
    ctypes.c_uint16,
    ctypes.c_uint16,
    ctypes.c_int16,
    ctypes.c_uint16,
]
_LIB.wet_tsn_serialize_frame.restype = ctypes.c_int

_LIB.wet_tsn_validate_frame.argtypes = [ctypes.POINTER(WetTSNFrame), ctypes.c_uint32]
_LIB.wet_tsn_validate_frame.restype = ctypes.c_int

_LIB.wet_timing_wheel_init.argtypes = [ctypes.POINTER(WetTimingWheelStruct), ctypes.c_uint32]
_LIB.wet_timing_wheel_init.restype = ctypes.c_int

_LIB.wet_timing_wheel_schedule.argtypes = [
    ctypes.POINTER(WetTimingWheelStruct),
    ctypes.POINTER(WetTSNFrame),
    ctypes.c_uint64,
]
_LIB.wet_timing_wheel_schedule.restype = ctypes.c_int

_LIB.wet_timing_wheel_drain_tick.argtypes = [
    ctypes.POINTER(WetTimingWheelStruct),
    ctypes.c_uint64,
    ctypes.POINTER(WetTSNFrame),
    ctypes.c_uint32,
]
_LIB.wet_timing_wheel_drain_tick.restype = ctypes.c_uint32

_LIB.wet_timing_wheel_set_tx_blanking.argtypes = [
    ctypes.POINTER(WetTimingWheelStruct),
    ctypes.c_uint16,
    ctypes.c_uint32,
]
_LIB.wet_timing_wheel_set_tx_blanking.restype = None


class WetPTPClock:
    """IEEE 1588 Precision Time Protocol Slew-Only Clock Disciplining Servo."""

    def __init__(self, kp: float = 0.7, ki: float = 0.2):
        self._c_clk = WetPTPClockStruct()
        _LIB.wet_ptp_init(ctypes.byref(self._c_clk), kp, ki)

    def update_offset(self, t1_ns: int, t2_ns: int, t3_ns: int, t4_ns: int):
        _LIB.wet_ptp_update_offset(ctypes.byref(self._c_clk), t1_ns, t2_ns, t3_ns, t4_ns)

    def get_disciplined_time_ns(self, local_raw_ns: int) -> int:
        return _LIB.wet_ptp_get_disciplined_time_ns(ctypes.byref(self._c_clk), local_raw_ns)

    @property
    def is_synchronized(self) -> bool:
        return bool(self._c_clk.is_synchronized)

    @property
    def stim_inhibited(self) -> bool:
        return bool(self._c_clk.stim_inhibited)

    @property
    def accumulated_offset_ns(self) -> int:
        return self._c_clk.accumulated_offset_ns

    @property
    def mean_path_delay_ns(self) -> int:
        return self._c_clk.mean_path_delay_ns


class WetTimingWheel:
    """Hierarchical Timing Wheel for O(1) Heterogeneous Axonal Delay Dispatching."""

    def __init__(self, chamber_id: int = 0):
        self.chamber_id = chamber_id
        self._c_tw = WetTimingWheelStruct()
        res = _LIB.wet_timing_wheel_init(ctypes.byref(self._c_tw), chamber_id)
        if res != 0:
            raise RuntimeError(f"wet_timing_wheel_init failed with code {res}")

    def schedule(self, frame: WetTSNFrame, current_epoch_ns: int) -> int:
        return _LIB.wet_timing_wheel_schedule(ctypes.byref(self._c_tw), ctypes.byref(frame), current_epoch_ns)

    def drain_tick(self, current_epoch_ns: int, max_count: int = 64) -> List[WetTSNFrame]:
        out_buf = (WetTSNFrame * max_count)()
        popped = _LIB.wet_timing_wheel_drain_tick(ctypes.byref(self._c_tw), current_epoch_ns, out_buf, max_count)
        return [out_buf[i] for i in range(popped)]

    def set_tx_blanking(self, target_chamber: int, blanking_ticks: int):
        _LIB.wet_timing_wheel_set_tx_blanking(ctypes.byref(self._c_tw), target_chamber, blanking_ticks)

    @property
    def total_scheduled(self) -> int:
        return self._c_tw.total_scheduled

    @property
    def total_dispatched(self) -> int:
        return self._c_tw.total_dispatched

    @property
    def late_drops(self) -> int:
        return self._c_tw.late_drops

    @property
    def is_epileptiform_tripped(self) -> bool:
        return bool(self._c_tw.is_epileptiform_tripped)


def serialize_tsn_frame(
    src_epoch_ns: int,
    rel_epoch_ns: int,
    seq: int,
    src_chamb: int,
    dst_chamb: int,
    src_ch: int,
    dst_ch: int,
    amp_uv: int,
    flags: int = 0,
) -> WetTSNFrame:
    frame = WetTSNFrame()
    res = _LIB.wet_tsn_serialize_frame(
        ctypes.byref(frame),
        src_epoch_ns,
        rel_epoch_ns,
        seq,
        src_chamb,
        dst_chamb,
        src_ch,
        dst_ch,
        amp_uv,
        flags,
    )
    if res != 0:
        raise RuntimeError("Failed to serialize TSN frame")
    return frame


def validate_tsn_frame(frame: WetTSNFrame, expected_dst_chamber: int = 0xFFFF) -> bool:
    res = _LIB.wet_tsn_validate_frame(ctypes.byref(frame), expected_dst_chamber)
    return res == 0
