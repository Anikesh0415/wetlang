#ifndef WET_VERIFICATION_H
#define WET_VERIFICATION_H

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(_WIN32) || defined(__CYGWIN__)
  #ifdef WET_BUILDING_DLL
    #define WET_EXPORT __declspec(dllexport)
  #else
    #define WET_EXPORT __declspec(dllimport)
  #endif
#else
  #if defined(__GNUC__) && __GNUC__ >= 4
    #define WET_EXPORT __attribute__((visibility("default")))
  #else
    #define WET_EXPORT
  #endif
#endif

/* Pillar 1: Sanitizer & Invariant Test Results */
typedef struct {
    uint32_t arena_passed;
    uint32_t corrupted_bytecode_passed;
    uint32_t biophysics_passed;
    uint32_t mems_passed;
    uint32_t aer_passed;
    uint32_t attocoulomb_passed;
    uint32_t all_passed;
} wet_sanitizer_result_t;

/* Pillar 2: 10-Million Continuous Tick Numerical Soak Results */
typedef struct {
    uint64_t total_ticks;
    int64_t  final_cumulative_dc_attocoulombs[64];
    int64_t  max_absolute_drift_attocoulombs;
    float    min_membrane_voltage_mv;
    float    max_membrane_voltage_mv;
    uint32_t nan_or_inf_detected;
    uint32_t interlock_trips;
    double   elapsed_seconds;
} wet_soak_result_t;

/* Pillar 3: Multi-Threaded Concurrency & Lock-Free SPSC Results */
typedef struct {
    uint64_t total_packets_produced;
    uint64_t total_packets_consumed;
    uint64_t torn_reads_detected;
    uint64_t sequence_errors;
    uint32_t num_threads;
    double   elapsed_seconds;
    double   throughput_mpps; /* Million packets per second */
} wet_concurrency_result_t;

/* Public Verification API */
WET_EXPORT int wet_run_sanitizer_harness_c(wet_sanitizer_result_t* out_result);
WET_EXPORT int wet_run_soak_10m_ticks(uint32_t total_ticks, wet_soak_result_t* out_result);
WET_EXPORT int wet_run_concurrency_stress(uint32_t total_packets, wet_concurrency_result_t* out_result);

#ifdef __cplusplus
}
#endif

#endif /* WET_VERIFICATION_H */
