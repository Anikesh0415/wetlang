/**
 * WetLang Hard Real-Time Sub-100 µs Execution Scheduler
 * Header Interface (native/include/wet_scheduler.h)
 *
 * Deterministic C99 execution scheduler operating at 10 kHz (100 µs period):
 *  - Dedicated real-time thread with core pinning (SetThreadAffinityMask)
 *  - Process & thread priority elevation (REALTIME_PRIORITY_CLASS / THREAD_PRIORITY_TIME_CRITICAL)
 *  - High-resolution hardware monotonic timer (QPC / QPF)
 *  - Hybrid precision pacing: bytecode/ODE compute + calibrated spin-wait tail (_mm_pause)
 *  - Cacheline-aligned (64-byte) lockless SPSC ring buffers for telemetry & stimulus injection
 *  - Static memory arena: zero heap allocations during real-time stepping
 */

#ifndef WET_SCHEDULER_H
#define WET_SCHEDULER_H

#include "wetvm_api.h"
#include "wetvm_types.h"
#include "wetvm_vm.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct wet_vm_instance wet_vm_instance_t;

/* Scheduler Configuration Options */
typedef struct {
    uint32_t target_period_us;         /* Nominal tick period in microseconds (default: 100 µs = 10 kHz) */

    /**
     * target_core: Physical/logical CPU core index for thread affinity mask (default: 1).
     *
     * ARCHITECTURAL GUIDANCE FOR HETEROGENEOUS HYBRID PROCESSORS:
     * On modern heterogeneous x86 architectures (e.g. Intel 12th-15th Gen Alder Lake,
     * Raptor Lake, Arrow Lake, and Intel Core Ultra / Lunar Lake), the processor combines
     * Performance Cores (P-cores, typically logical cores 0-3) and Efficient Cores
     * (E-cores / LP-E cores, typically logical cores 4+).
     *
     * CRITICAL: target_core MUST be pinned to a Performance Core (P-core, typically logical
     * cores 0–3). Benchmarks on heterogeneous hardware show that Efficient Cores (E-cores)
     * exhibit:
     *   - +55% compute latency (13–14 µs vs 8.8 µs on P-cores)
     *   - Highly elevated jitter (>300 µs P99.9) violating the sub-100 µs real-time contract
     *   - Consistent deadline overruns (4–17 overruns per 5k ticks under 10 kHz load).
     * Core 0 typically handles operating system DPCs and hardware interrupts; therefore,
     * logical Cores 1, 2, or 3 are the strongly recommended targets for hard real-time execution.
     */
    uint32_t target_core;
    uint32_t priority_class;           /* Windows priority class (default: 0x00000100 REALTIME_PRIORITY_CLASS) */
    int32_t  thread_priority;          /* Thread priority level (default: 15 THREAD_PRIORITY_TIME_CRITICAL) */
    uint8_t  enable_core_pinning;      /* 1 = pin thread to target_core, 0 = no pinning */
    uint8_t  enable_priority_elevation;/* 1 = elevate to REALTIME/TIME_CRITICAL, 0 = normal */
    uint32_t telemetry_queue_capacity; /* Power-of-2 capacity for telemetry SPSC ring buffer (default: 1024) */
    uint32_t stimulus_queue_capacity;  /* Power-of-2 capacity for stimulus SPSC ring buffer (default: 256) */
    uint64_t total_ticks;              /* Number of ticks to execute in benchmark/run (0 = indefinite) */
} wet_scheduler_config_t;

/* Asynchronous Stimulus Command injected through lockless SPSC queue */
typedef struct {
    uint8_t  channel;         /* MEA electrode channel (0..63) */
    float    voltage_v;       /* Stimulation voltage amplitude (V) */
    float    phase1_ms;       /* Cathodic pulse duration (ms) */
    float    phase2_ms;       /* Anodic counter-charge duration (ms) */
    uint64_t tick_scheduled;  /* Execution tick target (0 = immediate next tick) */
} wet_stim_command_t;

/* Latency & Jitter Performance Statistics */
typedef struct {
    uint64_t total_ticks;
    double   min_compute_us;
    double   max_compute_us;
    double   mean_compute_us;
    double   min_period_us;
    double   max_period_us;
    double   mean_period_us;
    double   mean_jitter_us;
    double   p50_jitter_us;
    double   p95_jitter_us;
    double   p99_jitter_us;
    double   p999_jitter_us;
    double   max_jitter_us;
    uint64_t deadline_overruns; /* Count of ticks where compute duration > target_period */
    uint64_t telemetry_dropped; /* Count of telemetry frames dropped due to full SPSC queue */
    uint64_t stimuli_injected;  /* Count of stimuli popped from SPSC queue and delivered to VM */
} wet_scheduler_stats_t;

/* Opaque Scheduler Instance Pointer */
typedef struct wet_scheduler wet_scheduler_t;

/* Public C-ABI API Functions */
WET_EXPORT wet_scheduler_t* wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config);
WET_EXPORT wet_status_t wet_scheduler_start(wet_scheduler_t* sched);

/**
 * Executes a single isochronous real-time tick step.
 *
 * PHASE SLIP STABILITY TRADE-OFF (Isochronous Pacing vs. Catch-Up Storms):
 * The scheduler deadline calculation evaluates:
 *   if (sched->next_deadline_qpc == 0 ||
 *       start_qpc > (sched->next_deadline_qpc + sched->period_qpc * 2)) {
 *       sched->next_deadline_qpc = start_qpc + sched->period_qpc;
 *   } else {
 *       sched->next_deadline_qpc += sched->period_qpc;
 *   }
 *
 * DESIGN RATIONALE:
 * Under quiescent conditions, accumulating next_deadline_qpc += period_qpc maintains
 * zero cumulative phase drift across thousands of cycles (<0.005% drift).
 * However, on non-RTOS desktop operating systems (e.g. Windows/Linux without PREEMPT_RT),
 * transient kernel DPCs, graphics driver stalls, or System Management Interrupts (SMIs)
 * can intermittently stall user-space threads for >200 µs (more than 2 full periods at 10 kHz).
 *
 * If the scheduler strictly maintained absolute wallclock cumulative phase lock without
 * resynchronization, returning from an OS stall would trigger a catastrophic "catch-up storm":
 * the scheduler would execute dozens of consecutive ticks with zero slack to recover lost time.
 * In wetware electrophysiology and microfluidics, back-to-back stimulation pulses violate
 * biological refractory windows (2.0 ms) and destabilize ODE numerical integration.
 *
 * Therefore, WetLang intentionally resynchronizes the deadline forward when a lag exceeding
 * two periods (>200 µs) occurs. This trades absolute cumulative wallclock phase lock during
 * severe OS stalls for period stability and biophysical execution safety.
 */
WET_EXPORT wet_status_t wet_scheduler_step(wet_scheduler_t* sched);
WET_EXPORT wet_status_t wet_scheduler_stop(wet_scheduler_t* sched);
WET_EXPORT wet_status_t wet_scheduler_get_stats(const wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats);
WET_EXPORT wet_status_t wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem);
WET_EXPORT wet_status_t wet_scheduler_push_stimulus(wet_scheduler_t* sched, const wet_stim_command_t* cmd);
WET_EXPORT wet_status_t wet_scheduler_benchmark(wet_scheduler_t* sched, uint32_t total_ticks, wet_scheduler_stats_t* out_stats);
WET_EXPORT void wet_scheduler_destroy(wet_scheduler_t* sched);

#ifdef __cplusplus
}
#endif

#endif /* WET_SCHEDULER_H */
