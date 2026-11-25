#include "../include/wet_crt.h"
#include "../include/wet_aer.h"

#define WET_AER_FLAG_CRITICAL 0x0004U

static inline int wet_isfinitef(float x) {
    union {
        float f;
        uint32_t u;
    } bits;
    bits.f = x;
    return (bits.u & 0x7F800000U) != 0x7F800000U;
}

int wet_aer_ring_init(wet_aer_ring_t *ring, wet_aer_packet_t *buffer, uint32_t capacity, uint32_t burst_limit_max_hz, uint16_t *ch_counts, uint32_t num_channels) {
    if (!ring || !buffer || capacity < 2) {
        return -1;
    }
    /* Capacity must be a power of 2 */
    if ((capacity & (capacity - 1)) != 0) {
        return -2;
    }
    if (num_channels > WET_AER_MAX_CHANNELS) {
        return -3;
    }

    memset(ring, 0, sizeof(*ring));
    ring->buffer = buffer;
    ring->capacity = capacity;
    ring->mask = capacity - 1;
    /* Allow burst traffic up to 5 MHz during network bursts */
    ring->burst_limit_max_hz = burst_limit_max_hz > 0 ? burst_limit_max_hz : 5000000U;
    ring->channel_spike_counts = ch_counts;
    ring->monitored_channels = num_channels;
    ring->max_channel_hz = 250; /* Quarantine pads oscillating above 250 Hz */
    return 0;
}

static void wet_aer_rollover_window(wet_aer_ring_t *ring, uint64_t tick) {
    if (tick > ring->last_stat_tick + 10000ULL) {
        double elapsed_sec = (double)(tick - ring->last_stat_tick) * 0.0001;
        double rate_hz = (elapsed_sec > 0.0) ? ((double)ring->spikes_in_window / elapsed_sec) : 0.0;
        ring->current_spike_rate_hz = rate_hz;
        /* 16 bytes per packet * 8 bits = 128 bits */
        ring->current_bandwidth_mbps = (rate_hz * 128.0) / 1000000.0;

        if (ring->burst_limit_max_hz > 0) {
            if (rate_hz > (double)ring->burst_limit_max_hz) {
                ring->is_burst_tripped = 1;
            } else if (rate_hz <= 0.8 * (double)ring->burst_limit_max_hz) {
                ring->is_burst_tripped = 0;
            }
        } else {
            ring->is_burst_tripped = 0;
        }
        ring->spikes_in_window = 0;
        ring->last_stat_tick = tick;

        /* Reset per-channel counts so quarantined channels recover on new window */
        if (ring->channel_spike_counts && ring->monitored_channels > 0) {
            memset(ring->channel_spike_counts, 0, ring->monitored_channels * sizeof(uint16_t));
        }
    }
}

int wet_aer_push(wet_aer_ring_t *ring, uint64_t tick, uint32_t channel, int16_t amp_uv, uint16_t flags) {
    if (!ring || !ring->buffer) {
        return -1;
    }

    /* Hard channel bounds check BEFORE touching counters or ring */
    if (channel >= WET_AER_MAX_CHANNELS ||
        (ring->channel_spike_counts && channel >= ring->monitored_channels)) {
        ring->total_dropped++;
        return -4; /* Invalid / out-of-range channel */
    }

    /* Roll over 1-second window BEFORE early quarantine/full returns (prevents quarantine deadlock) */
    wet_aer_rollover_window(ring, tick);

    /* Per-channel rate monitoring to quarantine noisy / oscillating pads (saturating count) */
    if (ring->channel_spike_counts && channel < ring->monitored_channels) {
        if (ring->channel_spike_counts[channel] > ring->max_channel_hz) {
            ring->total_dropped++;
            return -3; /* Quarantined noisy channel */
        }
        if (ring->channel_spike_counts[channel] < UINT16_MAX) {
            ring->channel_spike_counts[channel]++;
        }
    }

    /* Enforced burst shedding when burst limit is tripped (shed non-critical background packets) */
    if (ring->is_burst_tripped && ((flags & WET_AER_FLAG_CRITICAL) == 0U)) {
        if ((ring->spikes_in_window & 0x3U) != 0U) {
            ring->spikes_in_window++;
            ring->total_dropped++;
            return -5; /* Burst shedding active */
        }
    }

    /* Check if ring is full */
    uint32_t head = wet_atomic_load_u32_acquire(&ring->head);
    uint32_t tail = wet_atomic_load_u32_acquire(&ring->tail);
    uint32_t next_head = (head + 1U) & ring->mask;
    if (next_head == tail) {
        ring->total_dropped++;
        return -2; /* Buffer full */
    }

    ring->spikes_in_window++;

    /* Write 16-byte aligned packet */
    uint32_t idx = head & ring->mask;
    ring->buffer[idx].timestamp_tick = tick;
    ring->buffer[idx].channel_id = channel;
    ring->buffer[idx].peak_amplitude_uv = amp_uv;
    ring->buffer[idx].flags = flags;

    /* Publish head with memory barrier */
    wet_atomic_store_u32_release(&ring->head, next_head);
    wet_atomic_store_u64_release(&ring->total_pushed, ring->total_pushed + 1ULL);
    return 0;
}

uint32_t wet_aer_pop_batch(wet_aer_ring_t *ring, wet_aer_packet_t *out_batch, uint32_t max_count) {
    if (!ring || !out_batch || max_count == 0) {
        return 0;
    }

    uint32_t popped = 0;
    uint32_t tail = ring->tail;
    uint32_t head = wet_atomic_load_u32_acquire(&ring->head);
    while (popped < max_count && (tail != head)) {
        uint32_t idx = tail & ring->mask;
        out_batch[popped] = ring->buffer[idx];
        tail = (tail + 1) & ring->mask;
        popped++;
    }
    if (popped > 0) {
        wet_atomic_store_u32_release(&ring->tail, tail);
    }
    return popped;
}

uint32_t wet_aer_available(const wet_aer_ring_t *ring) {
    if (!ring) return 0;
    uint32_t head = wet_atomic_load_u32_acquire(&ring->head);
    uint32_t tail = wet_atomic_load_u32_acquire(&ring->tail);
    if (head >= tail) {
        return head - tail;
    }
    return ring->capacity - (tail - head);
}

void wet_aer_get_stats(wet_aer_ring_t *ring, uint64_t current_tick, uint64_t *out_total, double *out_rate_hz, double *out_mbps) {
    if (!ring) return;
    uint64_t total_pushed = wet_atomic_load_u64_acquire(&ring->total_pushed);
    uint64_t last_tick = ring->last_stat_tick;
    uint32_t win_spikes = ring->spikes_in_window;
    double rate_hz = ring->current_spike_rate_hz;
    double mbps = ring->current_bandwidth_mbps;

    if (current_tick > last_tick) {
        double elapsed_sec = (double)(current_tick - last_tick) * 0.0001;
        if (elapsed_sec > 0.0 && win_spikes > 0) {
            rate_hz = (double)win_spikes / elapsed_sec;
            mbps = (rate_hz * 128.0) / 1000000.0;
        } else if (current_tick > last_tick + 10000ULL && win_spikes == 0) {
            rate_hz = 0.0;
            mbps = 0.0;
            ring->is_burst_tripped = 0;
        }
        ring->current_spike_rate_hz = rate_hz;
        ring->current_bandwidth_mbps = mbps;
    }
    if (out_total) *out_total = total_pushed;
    if (out_rate_hz) *out_rate_hz = rate_hz;
    if (out_mbps) *out_mbps = mbps;
}

/*
 * NEO Detector Implementation with 5-Tap Bartlett Filter & Blanking
 */
int wet_neo_init(wet_neo_detector_t *det, uint32_t num_channels, float threshold_multiplier, uint32_t refractory_ticks) {
    if (!det || num_channels == 0) return -1;
    memset(det, 0, sizeof(*det));

    det->num_channels = num_channels;
    det->threshold_multiplier = threshold_multiplier > 0.0f ? threshold_multiplier : 4.0f;
    det->refractory_ticks = refractory_ticks > 0 ? refractory_ticks : 10; /* 1.0 ms default */

    det->v_baseline = (float*)calloc(num_channels, sizeof(float));
    det->prev_v1 = (float*)calloc(num_channels, sizeof(float));
    det->prev_v2 = (float*)calloc(num_channels, sizeof(float));
    for (int k = 0; k < 4; k++) {
        det->psi_history[k] = (float*)calloc(num_channels, sizeof(float));
    }
    det->refract_left = (uint32_t*)calloc(num_channels, sizeof(uint32_t));
    det->blanking_left = (uint32_t*)calloc(num_channels, sizeof(uint32_t));
    det->running_neo_mean = (float*)calloc(num_channels, sizeof(float));
    det->sample_count = (uint32_t*)calloc(num_channels, sizeof(uint32_t));

    if (!det->v_baseline || !det->prev_v1 || !det->prev_v2 || !det->refract_left ||
        !det->blanking_left || !det->running_neo_mean || !det->sample_count) {
        wet_neo_free(det);
        return -2;
    }

    for (uint32_t i = 0; i < num_channels; i++) {
        det->running_neo_mean[i] = 1.0f;
    }
    return 0;
}

void wet_neo_free(wet_neo_detector_t *det) {
    if (!det) return;
    if (det->v_baseline) { free(det->v_baseline); det->v_baseline = NULL; }
    if (det->prev_v1) { free(det->prev_v1); det->prev_v1 = NULL; }
    if (det->prev_v2) { free(det->prev_v2); det->prev_v2 = NULL; }
    for (int k = 0; k < 4; k++) {
        if (det->psi_history[k]) { free(det->psi_history[k]); det->psi_history[k] = NULL; }
    }
    if (det->refract_left) { free(det->refract_left); det->refract_left = NULL; }
    if (det->blanking_left) { free(det->blanking_left); det->blanking_left = NULL; }
    if (det->running_neo_mean) { free(det->running_neo_mean); det->running_neo_mean = NULL; }
    if (det->sample_count) { free(det->sample_count); det->sample_count = NULL; }
    det->num_channels = 0;
}

void wet_neo_set_blanking(wet_neo_detector_t *det, uint16_t channel, uint32_t blanking_ticks) {
    if (!det || channel >= det->num_channels) return;
    det->blanking_left[channel] = blanking_ticks;
}

int wet_neo_process_sample(wet_neo_detector_t *det, uint16_t channel, float voltage, uint64_t current_tick, wet_aer_ring_t *out_ring) {
    if (!det || channel >= det->num_channels) return 0;
    if (!wet_isfinitef(voltage)) return 0;

    /* Hardware stimulus artifact blanking */
    if (det->blanking_left[channel] > 0) {
        det->blanking_left[channel]--;
        det->v_baseline[channel] = voltage; /* Clamp baseline to avoid transient blinding */
        return 0;
    }

    /* DC baseline estimation */
    if (det->sample_count[channel] == 0) {
        det->v_baseline[channel] = voltage;
    } else {
        det->v_baseline[channel] = 0.95f * det->v_baseline[channel] + 0.05f * voltage;
    }
    float x_ac = voltage - det->v_baseline[channel];

    /* Prime pipeline on first 2 samples */
    if (det->sample_count[channel] < 2) {
        det->prev_v2[channel] = det->prev_v1[channel];
        det->prev_v1[channel] = x_ac;
        det->sample_count[channel]++;
        return 0;
    }
    det->sample_count[channel]++;

    /* Update refractory counter */
    if (det->refract_left[channel] > 0) {
        det->refract_left[channel]--;
    }

    /* Shift voltages: x[n] = x_ac, x[n-1] = prev_v1, x[n-2] = prev_v2 */
    float v_curr = x_ac;
    float v_prev1 = det->prev_v1[channel];
    float v_prev2 = det->prev_v2[channel];

    /* Raw discrete NEO: Psi = v_prev1^2 - v_curr * v_prev2 */
    float raw_psi = (v_prev1 * v_prev1) - (v_curr * v_prev2);
    if (raw_psi < 0.0f) raw_psi = 0.0f;

    /*
     * 5-Tap Bartlett Triangular Smoother:
     * Weights: [1, 2, 3, 2, 1] / 9
     * Suppresses quadratic high-frequency thermal noise amplification
     */
    float p_m2 = det->psi_history[0][channel];
    float p_m1 = det->psi_history[1][channel];
    float p_0  = raw_psi;
    float p_p1 = det->psi_history[2][channel];
    float p_p2 = det->psi_history[3][channel];

    float psi_smooth = (p_m2 + 2.0f * p_m1 + 3.0f * p_0 + 2.0f * p_p1 + p_p2) * (1.0f / 9.0f);

    /* Shift PSI history */
    det->psi_history[0][channel] = det->psi_history[1][channel];
    det->psi_history[1][channel] = p_0;
    det->psi_history[2][channel] = det->psi_history[3][channel];
    det->psi_history[3][channel] = raw_psi;

    /* Running baseline energy tracking */
    det->running_neo_mean[channel] = 0.99f * det->running_neo_mean[channel] + 0.01f * psi_smooth;
    if (det->running_neo_mean[channel] < 0.1f) det->running_neo_mean[channel] = 0.1f;
    float threshold = det->threshold_multiplier * det->running_neo_mean[channel];

    int spike_detected = 0;
    if (psi_smooth > threshold && det->refract_left[channel] == 0) {
        spike_detected = 1;
        det->refract_left[channel] = det->refractory_ticks;
        det->total_detected++;
        if (out_ring) {
            float amp_f = v_curr * 1000.0f; /* Convert mV to uV with saturation */
            if (!wet_isfinitef(amp_f)) amp_f = 0.0f;
            if (amp_f > 32767.0f) amp_f = 32767.0f;
            else if (amp_f < -32768.0f) amp_f = -32768.0f;
            int16_t amp_uv = (int16_t)amp_f;
            wet_aer_push(out_ring, current_tick, channel, amp_uv, 0x0001);
        }
    }

    /* Shift pipeline */
    det->prev_v2[channel] = v_prev1;
    det->prev_v1[channel] = v_curr;

    return spike_detected;
}

/*
 * Event-Driven CSR Synaptic Matrix
 * Complexity: O(spiking_neurons * degree), avoiding O(N_rows) scans
 */
int wet_csr_init(wet_csr_matrix_t *csr, uint32_t rows, uint32_t cols, uint32_t nnz, float scale_ns) {
    if (!csr || rows == 0 || cols == 0 || nnz == 0) return -1;
    if (rows == UINT32_MAX || (uint64_t)nnz > (uint64_t)rows * (uint64_t)cols) return -1;
    if ((size_t)(rows + 1U) > (SIZE_MAX / sizeof(uint32_t)) || (size_t)nnz > (SIZE_MAX / sizeof(uint16_t))) {
        return -1;
    }
    memset(csr, 0, sizeof(*csr));

    csr->num_rows = rows;
    csr->num_cols = cols;
    csr->nnz = nnz;
    csr->weight_scale_ns = scale_ns > 0.0f ? scale_ns : 0.2f;

    csr->row_ptr = (uint32_t*)calloc((size_t)rows + 1U, sizeof(uint32_t));
    csr->col_idx = (uint16_t*)calloc((size_t)nnz, sizeof(uint16_t));
    csr->weights_int8 = (int8_t*)calloc((size_t)nnz, sizeof(int8_t));

    if (!csr->row_ptr || !csr->col_idx || !csr->weights_int8) {
        wet_csr_free(csr);
        return -2;
    }
    return 0;
}

void wet_csr_free(wet_csr_matrix_t *csr) {
    if (!csr) return;
    if (csr->row_ptr) { free(csr->row_ptr); csr->row_ptr = NULL; }
    if (csr->col_idx) { free(csr->col_idx); csr->col_idx = NULL; }
    if (csr->weights_int8) { free(csr->weights_int8); csr->weights_int8 = NULL; }
    csr->num_rows = 0;
    csr->num_cols = 0;
    csr->nnz = 0;
}

void wet_csr_spmv_spikes(const wet_csr_matrix_t *csr, const uint8_t *spike_events, float *out_conductance_ns) {
    if (!csr || !spike_events || !out_conductance_ns || !csr->row_ptr || !csr->col_idx || !csr->weights_int8) return;

    float scale = csr->weight_scale_ns;
    /* Strictly event-driven: only traverse outgoing edges of spiking pre-synaptic neurons */
    for (uint32_t r = 0; r < csr->num_rows; r++) {
        if (!spike_events[r]) continue;

        uint32_t start = csr->row_ptr[r];
        uint32_t end = csr->row_ptr[r + 1];
        if (start > end || end > csr->nnz) continue;
        for (uint32_t idx = start; idx < end; idx++) {
            uint16_t post_id = csr->col_idx[idx];
            if (post_id < csr->num_cols) {
                out_conductance_ns[post_id] += (float)csr->weights_int8[idx] * scale;
            }
        }
    }
}
