/**
 * WetLang Hard Real-Time Sub-100 µs Execution Scheduler
 * Implementation (native/src/wet_scheduler.c)
 *
 * Deterministic C99 execution scheduler operating at 10 kHz (100 µs period):
 *  - Dedicated real-time thread with core pinning (SetThreadAffinityMask)
 *  - Process & thread priority elevation (REALTIME_PRIORITY_CLASS / THREAD_PRIORITY_TIME_CRITICAL)
 *  - High-resolution hardware monotonic timer (QueryPerformanceCounter / QueryPerformanceFrequency)
 *  - Hybrid precision pacing: bytecode/ODE compute + calibrated spin-wait tail (_mm_pause)
 *  - Cacheline-aligned (64-byte) lockless SPSC ring buffers for telemetry & stimulus injection
 *  - Static memory arena: zero heap allocations during real-time stepping
 */

#if !defined(_WIN32)
#ifndef _POSIX_C_SOURCE
#define _POSIX_C_SOURCE 200809L
#endif
#if defined(__linux__) && !defined(_GNU_SOURCE)
#define _GNU_SOURCE
#endif
#endif

#include "../include/wet_crt.h"
#include "../include/wet_scheduler.h"
#include "../include/wetvm_vm.h"
#include "../include/biophysics.h"

/* 128-byte cache line alignment isolates Intel L2 spatial prefetcher pairs (eliminating cross-core false sharing) */
#define WET_CACHELINE_SIZE 128
#define WET_DEFAULT_SAMPLE_CAPACITY 100000
#define WET_SCHED_MAX_TELEM_CAP 2048U
#define WET_SCHED_MAX_STIM_CAP 1024U
#define WET_MAX_SCHEDULERS 8

#if defined(_MSC_VER) && !defined(__clang__)
long _InterlockedCompareExchange(long volatile*, long, long);
#pragma intrinsic(_InterlockedCompareExchange)
#endif

static inline int wet_atomic_cas_u32(volatile uint32_t* ptr, uint32_t expected, uint32_t desired) {
#if defined(__GNUC__) || defined(__clang__)
    return __atomic_compare_exchange_n(ptr, &expected, desired, 0, __ATOMIC_ACQ_REL, __ATOMIC_ACQUIRE);
#elif defined(_MSC_VER)
    return (_InterlockedCompareExchange((volatile long*)ptr, (long)desired, (long)expected) == (long)expected);
#else
    if (*ptr == expected) { *ptr = desired; return 1; }
    return 0;
#endif
}

#if defined(_WIN32)
typedef union _LARGE_INTEGER {
    struct {
        uint32_t LowPart;
        int32_t  HighPart;
    } s;
    int64_t QuadPart;
} LARGE_INTEGER;

typedef void* HANDLE;
typedef unsigned long DWORD;
typedef uint64_t DWORD_PTR;
typedef int BOOL;
typedef DWORD (__stdcall *LPTHREAD_START_ROUTINE)(void* lpThreadParameter);

#ifdef __cplusplus
extern "C" {
#endif
int __stdcall QueryPerformanceCounter(LARGE_INTEGER* lpPerformanceCount);
int __stdcall QueryPerformanceFrequency(LARGE_INTEGER* lpFrequency);
HANDLE __stdcall GetCurrentThread(void);
HANDLE __stdcall GetCurrentProcess(void);
DWORD_PTR __stdcall SetThreadAffinityMask(HANDLE hThread, DWORD_PTR dwThreadAffinityMask);
BOOL __stdcall SetPriorityClass(HANDLE hProcess, DWORD dwPriorityClass);
BOOL __stdcall SetThreadPriority(HANDLE hThread, int nPriority);
HANDLE __stdcall CreateThread(void* lpThreadAttributes, size_t dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress, void* lpParameter, DWORD dwCreationFlags, DWORD* lpThreadId);
DWORD __stdcall WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds);
BOOL __stdcall CloseHandle(HANDLE hObject);
void __stdcall Sleep(DWORD dwMilliseconds);
BOOL __stdcall VirtualLock(void* lpAddress, size_t dwSize);
BOOL __stdcall VirtualUnlock(void* lpAddress, size_t dwSize);
#ifdef __cplusplus
}
#endif
#else
#include <time.h>
#include <pthread.h>
#include <sched.h>
#endif

/* =========================================================================
 * Lockless Single-Producer Single-Consumer (SPSC) Ring Buffer
 * Cacheline-aligned (128-byte padding) to eliminate false sharing
 * ========================================================================= */

typedef struct {
    /* Producer cache line */
    volatile uint32_t head;
    uint8_t           _pad0[WET_CACHELINE_SIZE - sizeof(uint32_t)];

    /* Consumer cache line */
    volatile uint32_t tail;
    uint8_t           _pad1[WET_CACHELINE_SIZE - sizeof(uint32_t)];

    /* Metadata */
    uint32_t capacity;
    uint32_t mask;
    size_t   elem_size;
    uint8_t* buffer;
} wet_spsc_ring_t;

static int wet_spsc_init(
    wet_spsc_ring_t* ring,
    uint8_t* backing_buf,
    uint32_t max_capacity,
    uint32_t requested_capacity,
    size_t elem_size
) {
    if (!ring || !backing_buf || max_capacity == 0 || elem_size == 0) {
        return 0;
    }
    if (requested_capacity == 0) {
        requested_capacity = 1;
    }
    uint32_t cap = 1;
    while (cap < requested_capacity && cap < max_capacity) {
        cap <<= 1;
    }
    if (cap > max_capacity) {
        cap = max_capacity;
    }
    ring->capacity = cap;
    ring->mask = cap - 1;
    ring->elem_size = elem_size;
    ring->head = 0;
    ring->tail = 0;
    memset(backing_buf, 0, (size_t)cap * elem_size);
    ring->buffer = backing_buf;
    return 1;
}

static void wet_spsc_reset(wet_spsc_ring_t* ring) {
    if (!ring) return;
    ring->buffer = NULL;
    ring->capacity = 0;
    ring->mask = 0;
    ring->elem_size = 0;
    ring->head = 0;
    ring->tail = 0;
}

static inline int wet_spsc_push(wet_spsc_ring_t* ring, const void* item) {
    uint32_t head = ring->head;
    uint32_t tail = wet_atomic_load_u32_acquire(&ring->tail);
    if ((head - tail) >= ring->capacity) {
        return 0; /* Ring buffer full */
    }
    memcpy(ring->buffer + (head & ring->mask) * ring->elem_size, item, ring->elem_size);
    wet_atomic_store_u32_release(&ring->head, head + 1);
    return 1;
}

static inline int wet_spsc_pop(wet_spsc_ring_t* ring, void* out_item) {
    uint32_t tail = ring->tail;
    uint32_t head = wet_atomic_load_u32_acquire(&ring->head);
    if (tail == head) {
        return 0; /* Ring buffer empty */
    }
    memcpy(out_item, ring->buffer + (tail & ring->mask) * ring->elem_size, ring->elem_size);
    wet_atomic_store_u32_release(&ring->tail, tail + 1);
    return 1;
}

/* =========================================================================
 * Scheduler Internal Structure
 * ========================================================================= */

struct wet_scheduler {
    wet_vm_instance_t*     vm;
    wet_scheduler_config_t config;
    wet_scheduler_stats_t  stats;

    /* Ownership Metadata */
    int32_t                pool_index;      /* >= 0 if owned by g_scheduler_pool, -1 if arena */
    uint8_t                arena_allocated; /* 1 if created via wet_scheduler_create_arena */

    /* SPSC Ring Buffers & Inline Backing Storage */
    wet_spsc_ring_t        telem_ring;
    wet_spsc_ring_t        stim_ring;
    uint8_t                telem_storage[WET_SCHED_MAX_TELEM_CAP * sizeof(wet_telemetry_t)];
    uint8_t                stim_storage[WET_SCHED_MAX_STIM_CAP * sizeof(wet_stim_command_t)];
    wet_stim_command_t     pending_stim[WET_SCHED_MAX_STIM_CAP];
    uint32_t               pending_stim_count;

    /* High-Resolution Monotonic Timer State */
    int64_t                qpf_freq;
    double                 qpc_per_us;
    int64_t                period_qpc;
    int64_t                next_deadline_qpc;

    /* Execution State */
    volatile uint32_t      is_running;
    volatile uint32_t      stop_requested;
    uint8_t                thread_initialized;
#if defined(_WIN32)
    HANDLE                 thread_handle;
#else
    pthread_t              thread_handle;
#endif

    /* Benchmark Sample & Sort Scratch Buffers (Inline Static Layout) */
    uint32_t               sample_capacity;
    uint32_t               sample_count;
    double                 sample_jitters_us[WET_DEFAULT_SAMPLE_CAPACITY];
    double                 sample_computes_us[WET_DEFAULT_SAMPLE_CAPACITY];
    double                 sample_periods_us[WET_DEFAULT_SAMPLE_CAPACITY];
    double                 sort_scratch_us[WET_DEFAULT_SAMPLE_CAPACITY];

    /* Running Accumulators for Online Means */
    double                 sum_compute_us;
    double                 sum_period_us;
    double                 sum_jitter_us;
};

/* Static .bss pool of heap-free scheduler instances */
static struct wet_scheduler g_scheduler_pool[WET_MAX_SCHEDULERS];
static volatile uint32_t    g_scheduler_slot_used[WET_MAX_SCHEDULERS];

/* Fast in-place quicksort for doubles (used for exact percentile calculation) */
static void wet_sort_doubles(double* arr, int left, int right) {
    if (left >= right) return;
    double pivot = arr[(left + right) / 2];
    int i = left;
    int j = right;
    while (i <= j) {
        while (arr[i] < pivot) i++;
        while (arr[j] > pivot) j--;
        if (i <= j) {
            double tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    }
    if (left < j)  wet_sort_doubles(arr, left, j);
    if (i < right) wet_sort_doubles(arr, i, right);
}

/* =========================================================================
 * Thread Worker Procedure
 * ========================================================================= */

#if defined(_WIN32)
static DWORD __stdcall wet_scheduler_thread_proc(void* param) {
    wet_scheduler_t* sched = (wet_scheduler_t*)param;
    if (!sched) return 1;

    /* 1. Core Pinning */
    if (sched->config.enable_core_pinning) {
        DWORD_PTR mask = (1ULL << (sched->config.target_core % 64));
        SetThreadAffinityMask(GetCurrentThread(), mask);
    }

    /* 2. Process & Thread Priority Elevation */
    if (sched->config.enable_priority_elevation) {
        if (!SetPriorityClass(GetCurrentProcess(), sched->config.priority_class)) {
            /* Fallback to HIGH_PRIORITY_CLASS if REALTIME permission is restricted */
            SetPriorityClass(GetCurrentProcess(), 0x00000080);
        }
        SetThreadPriority(GetCurrentThread(), sched->config.thread_priority);
    }

    sched->is_running = 1;

    /* Real-Time Stepping Loop */
    while (!wet_atomic_load_u32_acquire(&sched->stop_requested)) {
        if (sched->vm && (sched->vm->is_halted || sched->vm->is_finished)) {
            break;
        }

        wet_status_t st = wet_scheduler_step(sched);
        if (st != WET_OK && st != WET_ERR_HALTED) {
            break;
        }

        if (sched->config.total_ticks > 0 && sched->stats.total_ticks >= sched->config.total_ticks) {
            break;
        }
    }

    sched->is_running = 0;
    return 0;
}
#else
static void* wet_scheduler_thread_proc(void* param) {
    wet_scheduler_t* sched = (wet_scheduler_t*)param;
    if (!sched) return NULL;

#if defined(__linux__)
    if (sched->config.enable_core_pinning) {
        cpu_set_t cpuset;
        CPU_ZERO(&cpuset);
        CPU_SET(sched->config.target_core, &cpuset);
        pthread_setaffinity_np(pthread_self(), sizeof(cpu_set_t), &cpuset);
    }
#endif

    sched->is_running = 1;
    while (!wet_atomic_load_u32_acquire(&sched->stop_requested)) {
        if (sched->vm && (sched->vm->is_halted || sched->vm->is_finished)) {
            break;
        }
        wet_status_t st = wet_scheduler_step(sched);
        if (st != WET_OK && st != WET_ERR_HALTED) break;
        if (sched->config.total_ticks > 0 && sched->stats.total_ticks >= sched->config.total_ticks) break;
    }
    sched->is_running = 0;
    return NULL;
}
#endif

/* =========================================================================
 * Public C-ABI API Implementation
 * ========================================================================= */

static int wet_scheduler_init_instance(
    wet_scheduler_t* sched,
    wet_vm_instance_t* vm,
    const wet_scheduler_config_t* config
) {
    sched->vm = vm;

    /* Apply default configuration */
    if (config) {
        sched->config = *config;
    } else {
        sched->config.target_period_us = 100; /* 100 µs = 10 kHz */
        sched->config.target_core = 1;
        sched->config.priority_class = 0x00000100; /* REALTIME_PRIORITY_CLASS */
        sched->config.thread_priority = 15;        /* THREAD_PRIORITY_TIME_CRITICAL */
        sched->config.enable_core_pinning = 1;
        sched->config.enable_priority_elevation = 1;
        sched->config.telemetry_queue_capacity = 1024;
        sched->config.stimulus_queue_capacity = 256;
        sched->config.total_ticks = 0;
    }

    if (sched->config.target_period_us == 0) sched->config.target_period_us = 100;
    if (sched->config.telemetry_queue_capacity == 0) sched->config.telemetry_queue_capacity = 1024;
    if (sched->config.stimulus_queue_capacity == 0) sched->config.stimulus_queue_capacity = 256;

    if (sched->config.telemetry_queue_capacity > WET_SCHED_MAX_TELEM_CAP) {
        sched->config.telemetry_queue_capacity = WET_SCHED_MAX_TELEM_CAP;
    }
    if (sched->config.stimulus_queue_capacity > WET_SCHED_MAX_STIM_CAP) {
        sched->config.stimulus_queue_capacity = WET_SCHED_MAX_STIM_CAP;
    }

    /* Initialize SPSC Ring Buffers using inline backing storage */
    if (!wet_spsc_init(&sched->telem_ring, sched->telem_storage, WET_SCHED_MAX_TELEM_CAP,
                       sched->config.telemetry_queue_capacity, sizeof(wet_telemetry_t))) {
        return 0;
    }

    if (!wet_spsc_init(&sched->stim_ring, sched->stim_storage, WET_SCHED_MAX_STIM_CAP,
                       sched->config.stimulus_queue_capacity, sizeof(wet_stim_command_t))) {
        wet_spsc_reset(&sched->telem_ring);
        return 0;
    }

    /* Initialize High-Resolution Monotonic Hardware Clock */
#if defined(_WIN32)
    LARGE_INTEGER qpf;
    QueryPerformanceFrequency(&qpf);
    sched->qpf_freq = qpf.QuadPart;
    sched->qpc_per_us = (double)qpf.QuadPart / 1000000.0;
    sched->period_qpc = (int64_t)((double)sched->config.target_period_us * sched->qpc_per_us);
#else
    sched->qpf_freq = 1000000000ULL;
    sched->qpc_per_us = 1000.0;
    sched->period_qpc = (int64_t)(sched->config.target_period_us * 1000ULL);
#endif

    /* Pre-fault and commit inline sample buffers to eliminate demand-paging faults in hot loop */
    sched->sample_capacity = WET_DEFAULT_SAMPLE_CAPACITY;
    memset(sched->sample_jitters_us, 0, sizeof(sched->sample_jitters_us));
    memset(sched->sample_computes_us, 0, sizeof(sched->sample_computes_us));
    memset(sched->sample_periods_us, 0, sizeof(sched->sample_periods_us));
    memset(sched->sort_scratch_us, 0, sizeof(sched->sort_scratch_us));

#if defined(_WIN32)
    /* Pin working set pages in physical RAM to prevent OS page trimming */
    VirtualLock(sched->sample_jitters_us, sizeof(sched->sample_jitters_us));
    VirtualLock(sched->sample_computes_us, sizeof(sched->sample_computes_us));
    VirtualLock(sched->sample_periods_us, sizeof(sched->sample_periods_us));
#endif

    /* Initialize stats */
    sched->stats.min_compute_us = 1e9;
    sched->stats.min_period_us = 1e9;

    return 1;
}

WET_EXPORT wet_scheduler_t* wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config) {
    int32_t acquired = -1;
    for (int32_t i = 0; i < WET_MAX_SCHEDULERS; ++i) {
        if (wet_atomic_cas_u32(&g_scheduler_slot_used[i], 0U, 1U)) {
            acquired = i;
            break;
        }
    }
    if (acquired < 0) {
        return NULL;
    }

    wet_scheduler_t* sched = &g_scheduler_pool[acquired];
    memset(sched, 0, sizeof(struct wet_scheduler));
    sched->pool_index = acquired;
    sched->arena_allocated = 0;

    if (!wet_scheduler_init_instance(sched, vm, config)) {
        sched->pool_index = -1;
        wet_atomic_store_u32_release(&g_scheduler_slot_used[acquired], 0U);
        return NULL;
    }

    return sched;
}

WET_EXPORT size_t wet_scheduler_arena_size(void) {
    return sizeof(struct wet_scheduler) + WET_CACHELINE_SIZE;
}

WET_EXPORT wet_scheduler_t* wet_scheduler_create_arena(
    void* arena_buf,
    size_t arena_bytes,
    wet_vm_instance_t* vm,
    const wet_scheduler_config_t* config
) {
    if (!arena_buf) return NULL;

    uintptr_t u = (uintptr_t)arena_buf;
    uintptr_t aligned_u = (u + (uintptr_t)(WET_CACHELINE_SIZE - 1)) & ~((uintptr_t)(WET_CACHELINE_SIZE - 1));
    size_t align_pad = (size_t)(aligned_u - u);
    if (arena_bytes < align_pad || (arena_bytes - align_pad) < sizeof(struct wet_scheduler)) {
        return NULL;
    }

    wet_scheduler_t* sched = (wet_scheduler_t*)aligned_u;
    memset(sched, 0, sizeof(struct wet_scheduler));
    sched->pool_index = -1;
    sched->arena_allocated = 1;

    if (!wet_scheduler_init_instance(sched, vm, config)) {
        return NULL;
    }

    return sched;
}

WET_EXPORT wet_status_t wet_scheduler_start(wet_scheduler_t* sched) {
    if (!sched) return WET_ERR_NULL_PTR;
    if (sched->is_running) return WET_OK;

    sched->stop_requested = 0;
    sched->next_deadline_qpc = 0;

#if defined(_WIN32)
    DWORD thread_id = 0;
    sched->thread_handle = CreateThread(NULL, 0, wet_scheduler_thread_proc, sched, 0, &thread_id);
    if (!sched->thread_handle) {
        return WET_ERR_ALLOC_FAILED;
    }
#else
    if (pthread_create(&sched->thread_handle, NULL, wet_scheduler_thread_proc, sched) != 0) {
        return WET_ERR_ALLOC_FAILED;
    }
#endif

    sched->thread_initialized = 1;
    return WET_OK;
}

WET_EXPORT wet_status_t wet_scheduler_step(wet_scheduler_t* sched) {
    if (!sched) return WET_ERR_NULL_PTR;
    if (!sched->vm) return WET_ERR_NULL_PTR;

    /* Timestamp at tick start */
#if defined(_WIN32)
    LARGE_INTEGER t_start;
    QueryPerformanceCounter(&t_start);
    int64_t start_qpc = t_start.QuadPart;
#else
    struct timespec ts_start;
#ifdef CLOCK_MONOTONIC_RAW
    clock_gettime(CLOCK_MONOTONIC_RAW, &ts_start);
#else
    clock_gettime(CLOCK_MONOTONIC, &ts_start);
#endif
    int64_t start_qpc = (int64_t)ts_start.tv_sec * 1000000000LL + (int64_t)ts_start.tv_nsec;
#endif

    /* Maintain isochronous deadline.
     * Separate tick-0 initialization (next_deadline_qpc == 0) from genuine OS preemption (> 2 periods).
     * Trade-off: If lag exceeds 2 periods (>200 µs), resynchronize forward to avoid
     * catastrophic catch-up storms at the expense of wallclock phase slip. */
    if (sched->next_deadline_qpc == 0) {
        sched->next_deadline_qpc = start_qpc + sched->period_qpc;
    } else if (start_qpc > (sched->next_deadline_qpc + sched->period_qpc * 2)) {
        sched->next_deadline_qpc = start_qpc + sched->period_qpc;

        /* ATOMIC CHARGE RECOVERY SAFETY INTERLOCK:
         * If an OS preemption occurred mid-pulse, ensure ongoing biphasic pulses
         * immediately complete active discharge to prevent leaving electrodes
         * with uncompensated net DC charge violating the Faradaic water window. */
        if (sched->vm) {
            bio_state_t* bio = &sched->vm->bio;
            for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
                if (bio->stim_pulses[ch].active) {
                    wet_active_discharge(sched->vm, (uint8_t)ch);
                }
            }
        }
    } else {
        sched->next_deadline_qpc += sched->period_qpc;
    }

    /* 1. Process previously buffered future stimuli & drain incoming stimuli from SPSC ring buffer */
    uint64_t cur_tick = sched->vm->current_tick;
    uint32_t kept = 0;
    for (uint32_t i = 0; i < sched->pending_stim_count; ++i) {
        wet_stim_command_t* pcmd = &sched->pending_stim[i];
        if (pcmd->tick_scheduled == 0 || pcmd->tick_scheduled <= cur_tick) {
            if (pcmd->channel < sched->vm->config.channel_count) {
                if (wet_inject_stimulus(sched->vm, pcmd->channel, pcmd->voltage_v, pcmd->phase1_ms, pcmd->phase2_ms) == WET_OK) {
                    sched->stats.stimuli_injected++;
                }
            }
        } else {
            sched->pending_stim[kept++] = *pcmd;
        }
    }
    sched->pending_stim_count = kept;

    wet_stim_command_t stim_cmd;
    while (wet_spsc_pop(&sched->stim_ring, &stim_cmd)) {
        if (stim_cmd.channel < sched->vm->config.channel_count) {
            if (stim_cmd.tick_scheduled == 0 || stim_cmd.tick_scheduled <= cur_tick) {
                if (wet_inject_stimulus(sched->vm, stim_cmd.channel, stim_cmd.voltage_v, stim_cmd.phase1_ms, stim_cmd.phase2_ms) == WET_OK) {
                    sched->stats.stimuli_injected++;
                }
            } else if (sched->pending_stim_count < WET_SCHED_MAX_STIM_CAP) {
                sched->pending_stim[sched->pending_stim_count++] = stim_cmd;
            }
        }
    }

    /* 2. Execute compute step (C99 Bytecode + Biophysical COBA-LIF ODE + Watchdogs) */
    wet_telemetry_t telem;
    wet_status_t status = wet_vm_step_internal(sched->vm, &telem);

    /* 3. Non-blocking stream telemetry to host SPSC queue */
    if (!wet_spsc_push(&sched->telem_ring, &telem)) {
        sched->stats.telemetry_dropped++;
    }

    /* 4. Measure compute latency */
#if defined(_WIN32)
    LARGE_INTEGER t_compute;
    QueryPerformanceCounter(&t_compute);
    double compute_us = (double)(t_compute.QuadPart - start_qpc) / sched->qpc_per_us;
#else
    struct timespec ts_comp;
#ifdef CLOCK_MONOTONIC_RAW
    clock_gettime(CLOCK_MONOTONIC_RAW, &ts_comp);
#else
    clock_gettime(CLOCK_MONOTONIC, &ts_comp);
#endif
    int64_t comp_qpc = (int64_t)ts_comp.tv_sec * 1000000000LL + (int64_t)ts_comp.tv_nsec;
    double compute_us = (double)(comp_qpc - start_qpc) / sched->qpc_per_us;
#endif

    /* 5. Check deadline overrun (compute duration exceeding target period) */
    if (compute_us > (double)sched->config.target_period_us) {
        sched->stats.deadline_overruns++;
    }

#if defined(_WIN32)
    /* 6. Hybrid precision pacing: calibrated spin-wait tail using _mm_pause().
     * STRICTLY ZERO Sleep() in the hot real-time execution loop. */
    if (t_compute.QuadPart < sched->next_deadline_qpc) {
        LARGE_INTEGER t_now;
        do {
            wet_cpu_pause();
            QueryPerformanceCounter(&t_now);
        } while (t_now.QuadPart < sched->next_deadline_qpc);
    }

    /* 7. Measure actual period and jitter */
    LARGE_INTEGER t_end;
    QueryPerformanceCounter(&t_end);
    double actual_period_us = (double)(t_end.QuadPart - start_qpc) / sched->qpc_per_us;
#else
    if (comp_qpc < sched->next_deadline_qpc) {
        struct timespec ts_now;
        do {
            wet_cpu_pause();
#ifdef CLOCK_MONOTONIC_RAW
            clock_gettime(CLOCK_MONOTONIC_RAW, &ts_now);
#else
            clock_gettime(CLOCK_MONOTONIC, &ts_now);
#endif
        } while (((int64_t)ts_now.tv_sec * 1000000000LL + (int64_t)ts_now.tv_nsec) < sched->next_deadline_qpc);
    }
    struct timespec ts_end;
#ifdef CLOCK_MONOTONIC_RAW
    clock_gettime(CLOCK_MONOTONIC_RAW, &ts_end);
#else
    clock_gettime(CLOCK_MONOTONIC, &ts_end);
#endif
    int64_t end_qpc = (int64_t)ts_end.tv_sec * 1000000000LL + (int64_t)ts_end.tv_nsec;
    double actual_period_us = (double)(end_qpc - start_qpc) / sched->qpc_per_us;
#endif

    double jitter_us = wet_fabs(actual_period_us - (double)sched->config.target_period_us);

    /* 8. Record metrics */
    sched->stats.total_ticks++;
    sched->sum_compute_us += compute_us;
    sched->sum_period_us += actual_period_us;
    sched->sum_jitter_us += jitter_us;

    if (compute_us < sched->stats.min_compute_us) sched->stats.min_compute_us = compute_us;
    if (compute_us > sched->stats.max_compute_us) sched->stats.max_compute_us = compute_us;

    if (actual_period_us < sched->stats.min_period_us) sched->stats.min_period_us = actual_period_us;
    if (actual_period_us > sched->stats.max_period_us) sched->stats.max_period_us = actual_period_us;

    if (jitter_us > sched->stats.max_jitter_us) sched->stats.max_jitter_us = jitter_us;

    /* Append to sample buffer */
    if (sched->sample_count < sched->sample_capacity) {
        sched->sample_jitters_us[sched->sample_count] = jitter_us;
        sched->sample_computes_us[sched->sample_count] = compute_us;
        sched->sample_periods_us[sched->sample_count] = actual_period_us;
        sched->sample_count++;
    }

    return status;
}

WET_EXPORT wet_status_t wet_scheduler_stop(wet_scheduler_t* sched) {
    if (!sched) return WET_ERR_NULL_PTR;

    wet_atomic_store_u32_release(&sched->stop_requested, 1);

    if (sched->thread_initialized) {
#if defined(_WIN32)
        if (sched->thread_handle) {
            WaitForSingleObject(sched->thread_handle, 5000);
            CloseHandle(sched->thread_handle);
            sched->thread_handle = NULL;
        }
#else
        pthread_join(sched->thread_handle, NULL);
#endif
        sched->thread_initialized = 0;
    }

    sched->is_running = 0;
    return WET_OK;
}

WET_EXPORT wet_status_t wet_scheduler_get_stats(wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats) {
    if (!sched || !out_stats) return WET_ERR_NULL_PTR;

    *out_stats = sched->stats;

    uint64_t n = sched->stats.total_ticks;
    if (n > 0) {
        out_stats->mean_compute_us = sched->sum_compute_us / (double)n;
        out_stats->mean_period_us = sched->sum_period_us / (double)n;
        out_stats->mean_jitter_us = sched->sum_jitter_us / (double)n;
    }

    /* Compute exact percentiles from sample buffer using in-struct scratch */
    if (sched->sample_count > 0) {
        uint32_t cnt = sched->sample_count;
        if (cnt > WET_DEFAULT_SAMPLE_CAPACITY) {
            cnt = WET_DEFAULT_SAMPLE_CAPACITY;
        }
        double* sorted = sched->sort_scratch_us;
        memcpy(sorted, sched->sample_jitters_us, (size_t)cnt * sizeof(double));
        wet_sort_doubles(sorted, 0, (int)cnt - 1);

        out_stats->p50_jitter_us = sorted[(size_t)(cnt * 0.50)];
        out_stats->p95_jitter_us = sorted[(size_t)(cnt * 0.95)];
        out_stats->p99_jitter_us = sorted[(size_t)(cnt * 0.99)];
        out_stats->p999_jitter_us = sorted[(size_t)(cnt * 0.999)];
        if (sorted[cnt - 1] > out_stats->max_jitter_us) {
            out_stats->max_jitter_us = sorted[cnt - 1];
        }
    }

    return WET_OK;
}

WET_EXPORT wet_status_t wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem) {
    if (!sched || !out_telem) return WET_ERR_NULL_PTR;
    if (wet_spsc_pop(&sched->telem_ring, out_telem)) {
        return WET_OK;
    }
    return WET_ERR_QUEUE_EMPTY; /* No telemetry available */
}

WET_EXPORT wet_status_t wet_scheduler_push_stimulus(wet_scheduler_t* sched, const wet_stim_command_t* cmd) {
    if (!sched || !cmd) return WET_ERR_NULL_PTR;
    if (wet_spsc_push(&sched->stim_ring, cmd)) {
        return WET_OK;
    }
    return WET_ERR_ALLOC_FAILED; /* Stimulus ring buffer full */
}

WET_EXPORT wet_status_t wet_scheduler_benchmark(
    wet_scheduler_t* sched,
    uint32_t total_ticks,
    wet_scheduler_stats_t* out_stats
) {
    if (!sched) return WET_ERR_NULL_PTR;

    /* Apply thread affinity and priority on benchmark caller thread if not backgrounded */
#if defined(_WIN32)
    if (sched->config.enable_core_pinning) {
        DWORD_PTR mask = (1ULL << (sched->config.target_core % 64));
        SetThreadAffinityMask(GetCurrentThread(), mask);
    }
    if (sched->config.enable_priority_elevation) {
        if (!SetPriorityClass(GetCurrentProcess(), sched->config.priority_class)) {
            SetPriorityClass(GetCurrentProcess(), 0x00000080);
        }
        SetThreadPriority(GetCurrentThread(), sched->config.thread_priority);
    }
#endif

    /* Warm-up ticks to ensure hardware instruction/data caches and branch predictors are primed */
    for (int w = 0; w < 10; ++w) {
        wet_scheduler_step(sched);
    }

    /* Reset metrics after warm-up */
    memset(&sched->stats, 0, sizeof(sched->stats));
    sched->stats.min_compute_us = 1e9;
    sched->stats.min_period_us = 1e9;
    sched->sample_count = 0;
    sched->pending_stim_count = 0;
    sched->sum_compute_us = 0.0;
    sched->sum_period_us = 0.0;
    sched->sum_jitter_us = 0.0;
    sched->next_deadline_qpc = 0;
    sched->is_running = 1;

    for (uint32_t i = 0; i < total_ticks; ++i) {
        wet_status_t st = wet_scheduler_step(sched);
        if (st != WET_OK && st != WET_ERR_HALTED) {
            sched->is_running = 0;
            return st;
        }
    }

    sched->is_running = 0;
    return wet_scheduler_get_stats(sched, out_stats);
}

WET_EXPORT void wet_scheduler_destroy(wet_scheduler_t* sched) {
    if (!sched) return;

    wet_scheduler_stop(sched);

#if defined(_WIN32)
    VirtualUnlock(sched->sample_jitters_us, sizeof(sched->sample_jitters_us));
    VirtualUnlock(sched->sample_computes_us, sizeof(sched->sample_computes_us));
    VirtualUnlock(sched->sample_periods_us, sizeof(sched->sample_periods_us));
#endif

    wet_spsc_reset(&sched->telem_ring);
    wet_spsc_reset(&sched->stim_ring);

    int32_t idx = sched->pool_index;
    uint8_t is_arena = sched->arena_allocated;

    volatile uint8_t* scrub_p = (volatile uint8_t*)sched;
    for (size_t k = 0; k < sizeof(struct wet_scheduler); ++k) {
        scrub_p[k] = 0;
    }
    sched->pool_index = -1;

    if (!is_arena && idx >= 0 && idx < WET_MAX_SCHEDULERS) {
        wet_atomic_store_u32_release(&g_scheduler_slot_used[idx], 0U);
    }
}
