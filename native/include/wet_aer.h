#ifndef WET_AER_H
#define WET_AER_H

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define WET_AER_CACHELINE_SIZE 128
#define WET_AER_PACKET_SIZE    16
#define WET_AER_MAX_CHANNELS   26400

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

/*
 * Production 16-byte AER Packet Layout
 * Guaranteed 8-byte natural alignment in arrays: eliminates hardware Alignment/UsageFault
 * exceptions on ARM Cortex-M/R and RISC-V cores while preventing split cache-line loads.
 */
#if defined(_MSC_VER)
#pragma pack(push, 8)
typedef struct {
    uint64_t timestamp_tick;    /* 8 bytes: tick count */
    uint32_t channel_id;        /* 4 bytes: 0..4,294,967,295 electrode index */
    int16_t  peak_amplitude_uv; /* 2 bytes: spike peak amplitude in microvolts */
    uint16_t flags;             /* 2 bytes: bit 0: burst, bit 1: multi-unit, bit 2: stim-recovery */
} wet_aer_packet_t;
#pragma pack(pop)
#else
typedef struct __attribute__((aligned(8))) {
    uint64_t timestamp_tick;    /* 8 bytes: tick count */
    uint32_t channel_id;        /* 4 bytes: 0..4,294,967,295 electrode index */
    int16_t  peak_amplitude_uv; /* 2 bytes: spike peak amplitude in microvolts */
    uint16_t flags;             /* 2 bytes: bit 0: burst, bit 1: multi-unit, bit 2: stim-recovery */
} wet_aer_packet_t;
#endif

#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L
_Static_assert(sizeof(wet_aer_packet_t) == 16, "wet_aer_packet_t must be exactly 16 bytes");
#endif

/*
 * High-Throughput Burst-Tolerant Lockless SPSC Circular Ring Buffer
 */
typedef struct {
    /* Producer cacheline */
    uint8_t pad0[WET_AER_CACHELINE_SIZE];
    volatile uint32_t head;
    uint8_t pad1[WET_AER_CACHELINE_SIZE - sizeof(uint32_t)];

    /* Consumer cacheline */
    volatile uint32_t tail;
    uint8_t pad2[WET_AER_CACHELINE_SIZE - sizeof(uint32_t)];

    /* Shared configuration and storage */
    wet_aer_packet_t *buffer;
    uint32_t capacity;
    uint32_t mask; /* capacity - 1 (must be power of 2) */

    /* Statistics and burst rate tracking */
    uint64_t total_pushed;
    uint64_t total_dropped;
    uint64_t last_stat_tick;
    uint32_t spikes_in_window;
    double current_spike_rate_hz;
    double current_bandwidth_mbps;
    uint32_t burst_limit_max_hz; /* Peak burst ceiling (e.g. 5,000,000 Hz) */
    uint8_t is_burst_tripped;

    /* Per-channel rate monitoring to quarantine noisy / oscillating pads */
    uint16_t *channel_spike_counts;
    uint32_t monitored_channels;
    uint16_t max_channel_hz; /* Default 250 Hz per channel */
} wet_aer_ring_t;

/*
 * Nonlinear Energy Operator (NEO) Spike Detector with Bartlett Smoother
 * Pipeline:
 *  1. Baseline subtraction: x_ac = v - v_base
 *  2. Raw discrete NEO: Psi[n] = x_ac[n-1]^2 - x_ac[n] * x_ac[n-2]
 *  3. 5-tap Bartlett smoothing window: Psi_smooth = (1/9)*(Psi[-2] + 2Psi[-1] + 3Psi[0] + 2Psi[1] + Psi[2])
 *  4. Blanking window suppression
 */
typedef struct {
    uint32_t num_channels;
    float threshold_multiplier;
    uint32_t refractory_ticks;
    
    /* Per-channel state */
    float *v_baseline;
    float *prev_v1;       /* x_ac[n-1] */
    float *prev_v2;       /* x_ac[n-2] */
    float *psi_history[4]; /* 4-tap history for 5-tap Bartlett smoother */
    uint32_t *refract_left;
    uint32_t *blanking_left; /* Hardware stimulus artifact blanking window */
    float *running_neo_mean;
    uint32_t *sample_count;
    uint64_t total_detected;
} wet_neo_detector_t;

/*
 * Event-Driven Compressed Sparse Row / Adjacency Synaptic Matrix
 * Total footprint:
 *  - weights_int8: 6.97 MB (int8)
 *  - col_idx:      13.94 MB (uint16_t)
 *  - row_ptr:      0.11 MB (uint32_t)
 *  - Total:        21.02 MB for 26,400 neurons @ 1% density
 *
 * Event-driven dispatch: O(spiking_neurons * avg_degree) complexity.
 */
typedef struct {
    uint32_t num_rows;
    uint32_t num_cols;
    uint32_t nnz;
    uint32_t *row_ptr;      /* Size: num_rows + 1 */
    uint16_t *col_idx;      /* Size: nnz */
    int8_t   *weights_int8;  /* Size: nnz, signed 8-bit quantized weights */
    float    weight_scale_ns; /* Conductance per LSB (default 0.2 nS) */
} wet_csr_matrix_t;

/* AER Ring Buffer Functions */
WET_EXPORT int wet_aer_ring_init(wet_aer_ring_t *ring, wet_aer_packet_t *buffer, uint32_t capacity, uint32_t burst_limit_max_hz, uint16_t *ch_counts, uint32_t num_channels);
WET_EXPORT int wet_aer_push(wet_aer_ring_t *ring, uint64_t tick, uint32_t channel, int16_t amp_uv, uint16_t flags);
WET_EXPORT uint32_t wet_aer_pop_batch(wet_aer_ring_t *ring, wet_aer_packet_t *out_batch, uint32_t max_count);
WET_EXPORT uint32_t wet_aer_available(const wet_aer_ring_t *ring);
WET_EXPORT void wet_aer_get_stats(wet_aer_ring_t *ring, uint64_t current_tick, uint64_t *out_total, double *out_rate_hz, double *out_mbps);

/* NEO Detector Functions */
WET_EXPORT int wet_neo_init(wet_neo_detector_t *det, uint32_t num_channels, float threshold_multiplier, uint32_t refractory_ticks);
WET_EXPORT void wet_neo_free(wet_neo_detector_t *det);
WET_EXPORT void wet_neo_set_blanking(wet_neo_detector_t *det, uint16_t channel, uint32_t blanking_ticks);
WET_EXPORT int wet_neo_process_sample(wet_neo_detector_t *det, uint16_t channel, float voltage, uint64_t current_tick, wet_aer_ring_t *out_ring);

/* CSR int8 Synaptic Matrix Functions */
WET_EXPORT int wet_csr_init(wet_csr_matrix_t *csr, uint32_t rows, uint32_t cols, uint32_t nnz, float scale_ns);
WET_EXPORT void wet_csr_free(wet_csr_matrix_t *csr);
WET_EXPORT void wet_csr_spmv_spikes(const wet_csr_matrix_t *csr, const uint8_t *spike_events, float *out_conductance_ns);

#ifdef __cplusplus
}
#endif

#endif /* WET_AER_H */
