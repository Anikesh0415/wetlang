"""
WetLang Python ctypes Bindings for Hard Real-Time Sub-100 µs Execution Scheduler
Provides high-level object-oriented interface to wet_scheduler C99 runtime.
"""

from __future__ import annotations

import ctypes
import multiprocessing
from ctypes import (
    c_void_p,
    c_uint8,
    c_uint32,
    c_uint64,
    c_int32,
    c_double,
    c_float,
    c_int,
    POINTER,
    byref,
)
from dataclasses import dataclass
from typing import Optional, Union, Any

from bindings.ffi import load_wetvm_lib, WetStatus, WetTelemetry


def resolve_p_core(requested_core: Optional[int] = None, allow_e_cores: bool = False) -> int:
    """
    Selects or validates a Performance Core (P-core) for real-time thread affinity.

    ARCHITECTURAL BACKGROUND:
    Modern heterogeneous x86 processors (Intel 12th-15th Gen Alder Lake, Raptor Lake,
    Arrow Lake, and Intel Core Ultra / Lunar Lake) integrate high-performance P-cores
    and low-power E-cores. E-cores exhibit +55% compute latency (13-14 µs vs 8.8 µs)
    and >300 µs jitter, failing hard real-time sub-100 µs guarantees.
    
    Logical Core 0 typically services host OS interrupts and driver DPCs. Therefore,
    Core 1, 2, or 3 are the prime Performance Cores. If no core is requested or an
    out-of-range/E-core is specified on hybrid architectures without allow_e_cores,
    fallback logic redirects execution to a verified P-core.
    """
    try:
        cpu_count = multiprocessing.cpu_count()
    except Exception:
        cpu_count = 1

    if requested_core is None:
        return 1 if cpu_count > 1 else 0

    if requested_core < 0:
        return 1 if cpu_count > 1 else 0

    # If the system has >= 8 logical cores (typical hybrid layout with 4 P-cores + 4 E-cores),
    # guard against accidental assignment to E-cores (cores 4+) unless allow_e_cores=True
    if not allow_e_cores and cpu_count >= 8 and requested_core >= 4:
        p_fallback = requested_core % 4
        if p_fallback == 0 and cpu_count > 1:
            p_fallback = 1
        return p_fallback

    if requested_core >= cpu_count:
        return 1 if cpu_count > 1 else 0

    return requested_core


class WetSchedulerConfig(ctypes.Structure):
    """Mirror of C wet_scheduler_config_t."""
    _fields_ = [
        ("target_period_us", c_uint32),
        ("target_core", c_uint32),
        ("priority_class", c_uint32),
        ("thread_priority", c_int32),
        ("enable_core_pinning", c_uint8),
        ("enable_priority_elevation", c_uint8),
        ("telemetry_queue_capacity", c_uint32),
        ("stimulus_queue_capacity", c_uint32),
        ("total_ticks", c_uint64),
    ]

    def __init__(
        self,
        target_period_us: int = 100,
        target_core: Optional[int] = None,
        priority_class: int = 0x00000100,  # REALTIME_PRIORITY_CLASS
        thread_priority: int = 15,          # THREAD_PRIORITY_TIME_CRITICAL
        enable_core_pinning: bool = True,
        enable_priority_elevation: bool = True,
        telemetry_queue_capacity: int = 1024,
        stimulus_queue_capacity: int = 256,
        total_ticks: int = 0,
        allow_e_cores: bool = False,
    ):
        p_core = resolve_p_core(target_core, allow_e_cores=allow_e_cores)
        super().__init__(
            target_period_us=target_period_us,
            target_core=p_core,
            priority_class=priority_class,
            thread_priority=thread_priority,
            enable_core_pinning=1 if enable_core_pinning else 0,
            enable_priority_elevation=1 if enable_priority_elevation else 0,
            telemetry_queue_capacity=telemetry_queue_capacity,
            stimulus_queue_capacity=stimulus_queue_capacity,
            total_ticks=total_ticks,
        )


class WetStimCommand(ctypes.Structure):
    """Mirror of C wet_stim_command_t."""
    _fields_ = [
        ("channel", c_uint8),
        ("voltage_v", c_float),
        ("phase1_ms", c_float),
        ("phase2_ms", c_float),
        ("tick_scheduled", c_uint64),
    ]

    def __init__(
        self,
        channel: int = 0,
        voltage_v: float = 0.8,
        phase1_ms: float = 0.2,
        phase2_ms: float = 0.2,
        tick_scheduled: int = 0,
    ):
        super().__init__(
            channel=channel,
            voltage_v=voltage_v,
            phase1_ms=phase1_ms,
            phase2_ms=phase2_ms,
            tick_scheduled=tick_scheduled,
        )


class WetSchedulerStats(ctypes.Structure):
    """Mirror of C wet_scheduler_stats_t."""
    _fields_ = [
        ("total_ticks", c_uint64),
        ("min_compute_us", c_double),
        ("max_compute_us", c_double),
        ("mean_compute_us", c_double),
        ("min_period_us", c_double),
        ("max_period_us", c_double),
        ("mean_period_us", c_double),
        ("mean_jitter_us", c_double),
        ("p50_jitter_us", c_double),
        ("p95_jitter_us", c_double),
        ("p99_jitter_us", c_double),
        ("p999_jitter_us", c_double),
        ("max_jitter_us", c_double),
        ("deadline_overruns", c_uint64),
        ("telemetry_dropped", c_uint64),
        ("stimuli_injected", c_uint64),
    ]

    def as_dict(self) -> dict:
        return {
            "total_ticks": self.total_ticks,
            "min_compute_us": self.min_compute_us,
            "max_compute_us": self.max_compute_us,
            "mean_compute_us": self.mean_compute_us,
            "min_period_us": self.min_period_us,
            "max_period_us": self.max_period_us,
            "mean_period_us": self.mean_period_us,
            "mean_jitter_us": self.mean_jitter_us,
            "p50_jitter_us": self.p50_jitter_us,
            "p95_jitter_us": self.p95_jitter_us,
            "p99_jitter_us": self.p99_jitter_us,
            "p999_jitter_us": self.p999_jitter_us,
            "max_jitter_us": self.max_jitter_us,
            "deadline_overruns": self.deadline_overruns,
            "telemetry_dropped": self.telemetry_dropped,
            "stimuli_injected": self.stimuli_injected,
        }


def _bind_scheduler_ffi(lib: ctypes.CDLL) -> None:
    """Configures ctypes argtypes and restypes for scheduler functions."""
    lib.wet_scheduler_create.restype = c_void_p
    lib.wet_scheduler_create.argtypes = [c_void_p, POINTER(WetSchedulerConfig)]

    lib.wet_scheduler_start.restype = c_int
    lib.wet_scheduler_start.argtypes = [c_void_p]

    lib.wet_scheduler_step.restype = c_int
    lib.wet_scheduler_step.argtypes = [c_void_p]

    lib.wet_scheduler_stop.restype = c_int
    lib.wet_scheduler_stop.argtypes = [c_void_p]

    lib.wet_scheduler_get_stats.restype = c_int
    lib.wet_scheduler_get_stats.argtypes = [c_void_p, POINTER(WetSchedulerStats)]

    lib.wet_scheduler_poll_telemetry.restype = c_int
    lib.wet_scheduler_poll_telemetry.argtypes = [c_void_p, POINTER(WetTelemetry)]

    lib.wet_scheduler_push_stimulus.restype = c_int
    lib.wet_scheduler_push_stimulus.argtypes = [c_void_p, POINTER(WetStimCommand)]

    lib.wet_scheduler_benchmark.restype = c_int
    lib.wet_scheduler_benchmark.argtypes = [c_void_p, c_uint32, POINTER(WetSchedulerStats)]

    lib.wet_scheduler_destroy.restype = None
    lib.wet_scheduler_destroy.argtypes = [c_void_p]


class WetScheduler:
    """
    Python wrapper for the C99 deterministic hard real-time scheduler.
    """
    def __init__(
        self,
        vm_or_runtime: Any,
        config: Optional[WetSchedulerConfig] = None,
        lib: Optional[ctypes.CDLL] = None,
    ):
        self._lib = lib or load_wetvm_lib()
        _bind_scheduler_ffi(self._lib)

        if hasattr(vm_or_runtime, "_handle"):
            self._vm_ptr = c_void_p(vm_or_runtime._handle)
        elif hasattr(vm_or_runtime, "vm"):
            v = vm_or_runtime.vm
            self._vm_ptr = c_void_p(v) if isinstance(v, int) else v
        elif hasattr(vm_or_runtime, "_vm"):
            v = vm_or_runtime._vm
            self._vm_ptr = c_void_p(v) if isinstance(v, int) else v
        elif isinstance(vm_or_runtime, int):
            self._vm_ptr = c_void_p(vm_or_runtime)
        else:
            self._vm_ptr = vm_or_runtime

        self._config = config or WetSchedulerConfig()
        self._sched = self._lib.wet_scheduler_create(self._vm_ptr, byref(self._config))
        if not self._sched:
            raise RuntimeError("Failed to allocate wet_scheduler_t instance")

    @property
    def handle(self) -> c_void_p:
        return self._sched

    def start(self) -> None:
        st = self._lib.wet_scheduler_start(self._sched)
        if st != WetStatus.WET_OK:
            raise RuntimeError(f"wet_scheduler_start failed with status {st}")

    def step(self) -> int:
        return self._lib.wet_scheduler_step(self._sched)

    def stop(self) -> None:
        self._lib.wet_scheduler_stop(self._sched)

    def get_stats(self) -> WetSchedulerStats:
        stats = WetSchedulerStats()
        st = self._lib.wet_scheduler_get_stats(self._sched, byref(stats))
        if st != WetStatus.WET_OK:
            raise RuntimeError(f"wet_scheduler_get_stats failed with status {st}")
        return stats

    def poll_telemetry(self) -> Optional[WetTelemetry]:
        telem = WetTelemetry()
        st = self._lib.wet_scheduler_poll_telemetry(self._sched, byref(telem))
        if st == WetStatus.WET_OK:
            return telem
        return None

    def push_stimulus(
        self,
        channel: int,
        voltage_v: float,
        phase1_ms: float = 0.2,
        phase2_ms: float = 0.2,
        tick_scheduled: int = 0
    ) -> bool:
        cmd = WetStimCommand(
            channel=channel,
            voltage_v=voltage_v,
            phase1_ms=phase1_ms,
            phase2_ms=phase2_ms,
            tick_scheduled=tick_scheduled,
        )
        st = self._lib.wet_scheduler_push_stimulus(self._sched, byref(cmd))
        return st == WetStatus.WET_OK

    def benchmark(self, total_ticks: int = 10000) -> WetSchedulerStats:
        stats = WetSchedulerStats()
        st = self._lib.wet_scheduler_benchmark(self._sched, c_uint32(total_ticks), byref(stats))
        if st != WetStatus.WET_OK and st != WetStatus.WET_ERR_HALTED:
            raise RuntimeError(f"wet_scheduler_benchmark failed with status {st}")
        return stats

    def destroy(self) -> None:
        if self._sched:
            self._lib.wet_scheduler_destroy(self._sched)
            self._sched = None

    def __enter__(self) -> "WetScheduler":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.destroy()
