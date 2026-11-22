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

#include "../include/wet_crt.h"
#include "../include/wet_scheduler.h"
#include "../include/wetvm_vm.h"
#include "../include/biophysics.h"

#define WET_CACHELINE_SIZE 64
#define WET_DEFAULT_SAMPLE_CAPACITY 100000

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
HANDLE __stdcall CreateThread(void* lpThreadAttributes, size_t dwStackSize, void* lpStartAddress, void* lpParameter, DWORD dwCreationFlags, DWORD* lpThreadId);
DWORD __stdcall WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds);
BOOL __stdcall CloseHandle(HANDLE hObject);
void __stdcall Sleep(DWORD dwMilliseconds);
#ifdef __cplusplus
}
#endif
#else
#include <time.h>
#include <pthread.h>
#include <sched.h>
#endif

/* Calibrated processor instruction pipeline pause */
static inline void wet_cpu_pause(void) {
#if defined(__clang__) || defined(__GNUC__)
    __builtin_ia32_pause();
#elif defined(_MSC_VER)
    _mm_pause();
#elif defined(__aarch64__)
    __asm__ __volatile__("isb\n");
#else
    /* NOP fallback */
#endif
}

/* Atomic Acquire/Release Memory Barriers */
static inline uint32_t wet_atomic_load_u32_acquire(const volatile uint32_t* ptr) {
#if defined(__GNUC__) || defined(__clang__)
    return __atomic_load_n(ptr, __ATOMIC_ACQUIRE);
#else
    return *ptr;
#endif
}

static inline void wet_atomic_store_u32_release(volatile uint32_t* ptr, uint32_t val) {
#if defined(__GNUC__) || defined(__clang__)
    __atomic_store_n(ptr, val, __ATOMIC_RELEASE);
#else
    *ptr = val;
#endif
}

/* =========================================================================
 * Lockless Single-Producer Single-Consumer (SPSC) Ring Buffer
 * Cacheline-aligned (64-byte padding) to eliminate false sharing
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

static int wet_spsc_init(wet_spsc_ring_t* ring, uint32_t capacity, size_t elem_size) {
    uint32_t cap = 1;
    while (cap < capacity) cap <<= 1;
    ring->capacity = cap;
    ring->mask = cap - 1;
    ring->elem_size = elem_size;
    ring->head = 0;
    ring->tail = 0;
    ring->buffer = (uint8_t*)calloc(cap, elem_size);
    return (ring->buffer != NULL);
}

static void wet_spsc_free(wet_spsc_ring_t* ring) {
    if (ring->buffer) {
        free(ring->buffer);
        ring->buffer = NULL;
    }
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

    /* SPSC Ring Buffers */
    wet_spsc_ring_t        telem_ring;
    wet_spsc_ring_t        stim_ring;

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

    /* Benchmark Sample Buffers */
    uint32_t               sample_capacity;
    uint32_t               sample_count;
    double*                sample_jitters_us;
    double*                sample_computes_us;
    double*                sample_periods_us;

    /* Running Accumulators for Online Means */
    double                 sum_compute_us;
    double                 sum_period_us;
    double                 sum_jitter_us;
};

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

    if (sched->config.enable_core_pinning) {
        cpu_set_t cpuset;
        CPU_ZERO(&cpuset);
        CPU_SET(sched->config.target_core, &cpuset);
        pthread_setaffinity_np(pthread_self(), sizeof(cpu_set_t), &cpuset);
    }

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

WET_EXPORT wet_scheduler_t* wet_scheduler_create(wet_vm_instance_t* vm, const wet_scheduler_config_t* config) {
    wet_scheduler_t* sched = (wet_scheduler_t*)calloc(1, sizeof(wet_scheduler_t));
    if (!sched) return NULL;

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

    /* Initialize SPSC Ring Buffers */
    if (!wet_spsc_init(&sched->telem_ring, sched->config.telemetry_queue_capacity, sizeof(wet_telemetry_t))) {
        free(sched);
        return NULL;
    }

    if (!wet_spsc_init(&sched->stim_ring, sched->config.stimulus_queue_capacity, sizeof(wet_stim_command_t))) {
        wet_spsc_free(&sched->telem_ring);
        free(sched);
        return NULL;
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

    /* Allocate Sample Buffers for Jitter / Latency Statistics */
    sched->sample_capacity = WET_DEFAULT_SAMPLE_CAPACITY;
    sched->sample_jitters_us = (double*)malloc(sched->sample_capacity * sizeof(double));
    sched->sample_computes_us = (double*)malloc(sched->sample_capacity * sizeof(double));
    sched->sample_periods_us = (double*)malloc(sched->sample_capacity * sizeof(double));

    /* Pre-fault and commit all memory pages in advance to eliminate demand-paging faults in hot loop */
    if (sched->sample_jitters_us)  memset(sched->sample_jitters_us, 0, sched->sample_capacity * sizeof(double));
    if (sched->sample_computes_us) memset(sched->sample_computes_us, 0, sched->sample_capacity * sizeof(double));
    if (sched->sample_periods_us)  memset(sched->sample_periods_us, 0, sched->sample_capacity * sizeof(double));

    /* Initialize stats */
    sched->stats.min_compute_us = 1e9;
    sched->stats.min_period_us = 1e9;

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
    clock_gettime(CLOCK_MONOTONIC_RAW, &ts_start);
    int64_t start_qpc = (int64_t)ts_start.tv_sec * 1000000000ULL + ts_start.tv_nsec;
#endif

    /* Maintain isochronous deadline.
     * Trade-off: If lag exceeds 2 periods (>200 µs), resynchronize forward to avoid
     * catastrophic catch-up storms at the expense of wallclock phase slip. */
    if (sched->next_deadline_qpc == 0 || start_qpc > (sched->next_deadline_qpc + sched->period_qpc * 2)) {
        sched->next_deadline_qpc = start_qpc + sched->period_qpc;
    } else {
        sched->next_deadline_qpc += sched->period_qpc;
    }

    /* 1. Drain incoming asynchronous stimuli from SPSC ring buffer */
    wet_stim_command_t stim_cmd;
    while (wet_spsc_pop(&sched->stim_ring, &stim_cmd)) {
        if (stim_cmd.channel < sched->vm->config.channel_count) {
            wet_inject_stimulus(sched->vm, stim_cmd.channel, stim_cmd.voltage_v, stim_cmd.phase1_ms, stim_cmd.phase2_ms);
            sched->stats.stimuli_injected++;
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
    clock_gettime(CLOCK_MONOTONIC_RAW, &ts_comp);
    int64_t comp_qpc = (int64_t)ts_comp.tv_sec * 1000000000ULL + ts_comp.tv_nsec;
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
            clock_gettime(CLOCK_MONOTONIC_RAW, &ts_now);
        } while (((int64_t)ts_now.tv_sec * 1000000000ULL + ts_now.tv_nsec) < sched->next_deadline_qpc);
    }
    struct timespec ts_end;
    clock_gettime(CLOCK_MONOTONIC_RAW, &ts_end);
    int64_t end_qpc = (int64_t)ts_end.tv_sec * 1000000000ULL + ts_end.tv_nsec;
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
        if (sched->thread_handle) {
            pthread_join(sched->thread_handle, NULL);
        }
#endif
        sched->thread_initialized = 0;
    }

    sched->is_running = 0;
    return WET_OK;
}

WET_EXPORT wet_status_t wet_scheduler_get_stats(const wet_scheduler_t* sched, wet_scheduler_stats_t* out_stats) {
    if (!sched || !out_stats) return WET_ERR_NULL_PTR;

    *out_stats = sched->stats;

    uint64_t n = sched->stats.total_ticks;
    if (n > 0) {
        out_stats->mean_compute_us = sched->sum_compute_us / (double)n;
        out_stats->mean_period_us = sched->sum_period_us / (double)n;
        out_stats->mean_jitter_us = sched->sum_jitter_us / (double)n;
    }

    /* Compute exact percentiles from sample buffer */
    if (sched->sample_count > 0) {
        uint32_t cnt = sched->sample_count;
        double* sorted = (double*)malloc(cnt * sizeof(double));
        if (sorted) {
            memcpy(sorted, sched->sample_jitters_us, cnt * sizeof(double));
            wet_sort_doubles(sorted, 0, (int)cnt - 1);

            out_stats->p50_jitter_us = sorted[(size_t)(cnt * 0.50)];
            out_stats->p95_jitter_us = sorted[(size_t)(cnt * 0.95)];
            out_stats->p99_jitter_us = sorted[(size_t)(cnt * 0.99)];
            out_stats->p999_jitter_us = sorted[(size_t)(cnt * 0.999)];
            out_stats->max_jitter_us = sorted[cnt - 1];

            free(sorted);
        }
    }

    return WET_OK;
}

WET_EXPORT wet_status_t wet_scheduler_poll_telemetry(wet_scheduler_t* sched, wet_telemetry_t* out_telem) {
    if (!sched || !out_telem) return WET_ERR_NULL_PTR;
    if (wet_spsc_pop(&sched->telem_ring, out_telem)) {
        return WET_OK;
    }
    return WET_ERR_NULL_PTR; /* No telemetry available */
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

    wet_spsc_free(&sched->telem_ring);
    wet_spsc_free(&sched->stim_ring);

    if (sched->sample_jitters_us)  free(sched->sample_jitters_us);
    if (sched->sample_computes_us) free(sched->sample_computes_us);
    if (sched->sample_periods_us)  free(sched->sample_periods_us);

    free(sched);
}
