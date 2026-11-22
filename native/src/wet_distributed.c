#include "../include/wet_crt.h"
#include "../include/wet_distributed.h"

/*
 * IEEE 1588 PTP Slew-Only Disciplining & Safety Invariants
 */
void wet_ptp_init(wet_ptp_clock_t *clk, double kp, double ki) {
    if (!clk) return;
    memset(clk, 0, sizeof(*clk));
    clk->kp = (kp > 0.0) ? kp : 0.7;
    clk->ki = (ki > 0.0) ? ki : 0.2;
    clk->stim_inhibited = 1; /* Inhibit inter-chamber stimulation until synchronized */
}

void wet_ptp_update_offset(wet_ptp_clock_t *clk, uint64_t t1_ns, uint64_t t2_ns, uint64_t t3_ns, uint64_t t4_ns) {
    if (!clk) return;

    /*
     * Fundamental PTP 4-Timestamp Formula:
     * offset = ((t2 - t1) - (t4 - t3)) / 2
     * delay  = ((t2 - t1) + (t4 - t3)) / 2
     */
    int64_t ms_diff = (int64_t)t2_ns - (int64_t)t1_ns;
    int64_t sm_diff = (int64_t)t4_ns - (int64_t)t3_ns;

    int64_t raw_offset = (ms_diff - sm_diff) / 2;
    int64_t raw_delay  = (ms_diff + sm_diff) / 2;

    /* Residual timing error after accumulated clock discipline */
    int64_t residual_offset = raw_offset - clk->accumulated_offset_ns;

    /* Slew-only PI Servo filter */
    clk->integral_err_ns += (double)residual_offset * 0.1;
    double adj = (clk->kp * (double)residual_offset) + (clk->ki * clk->integral_err_ns);

    /* Clamp maximum slew rate to +/- 100 ppm (prevents sudden time dilation) */
    if (adj > 10000.0) adj = 10000.0;
    if (adj < -10000.0) adj = -10000.0;

    clk->accumulated_offset_ns += (int64_t)adj;
    clk->mean_path_delay_ns = raw_delay;
    clk->sync_sequence++;

    /* Sub-microsecond synchronization threshold: |residual_offset| <= 1000 ns (1.0 us) */
    int64_t post_residual = raw_offset - clk->accumulated_offset_ns;
    if (post_residual >= -1000 && post_residual <= 1000) {
        clk->is_synchronized = 1;
        clk->stim_inhibited = 0; /* Clear safety inhibit */
    } else {
        clk->is_synchronized = 0;
        clk->stim_inhibited = 1; /* Inhibit inter-chamber stimulation if timing diverges */
    }
}

uint64_t wet_ptp_get_disciplined_time_ns(const wet_ptp_clock_t *clk, uint64_t local_raw_ns) {
    if (!clk) return local_raw_ns;
    return (uint64_t)((int64_t)local_raw_ns - clk->accumulated_offset_ns);
}

/*
 * 32-Byte TSN Frame Serialization & Validation
 */
int wet_tsn_serialize_frame(wet_tsn_frame_t *frame, uint64_t src_epoch_ns, uint64_t rel_epoch_ns, uint32_t seq, uint16_t src_chamb, uint16_t dst_chamb, uint16_t src_ch, uint16_t dst_ch, int16_t amp_uv, uint16_t flags) {
    if (!frame) return -1;
    frame->source_epoch_ns = src_epoch_ns;
    frame->release_epoch_ns = rel_epoch_ns;
    frame->sequence_number = seq;
    frame->source_chamber = src_chamb;
    frame->target_chamber = dst_chamb;
    frame->source_channel = src_ch;
    frame->target_channel = dst_ch;
    frame->spike_amplitude_uv = amp_uv;
    frame->flags = flags;
    return 0;
}

int wet_tsn_validate_frame(const wet_tsn_frame_t *frame, uint32_t expected_dst_chamber) {
    if (!frame) return -1;
    if (frame->target_chamber != expected_dst_chamber && expected_dst_chamber != 0xFFFF) {
        return -2; /* Wrong destination chamber */
    }
    if (frame->release_epoch_ns < frame->source_epoch_ns) {
        return -3; /* Negative axonal delay (causality violation) */
    }
    return 0;
}

/*
 * Timing Wheel: O(1) Heterogeneous Axonal Delay Dispatcher
 * Completely eliminates Head-of-Line blocking inherent to FIFO queues.
 */
int wet_timing_wheel_init(wet_timing_wheel_t *tw, uint32_t chamber_id) {
    if (!tw) return -1;
    memset(tw, 0, sizeof(*tw));
    tw->chamber_id = chamber_id;
    return 0;
}

int wet_timing_wheel_schedule(wet_timing_wheel_t *tw, const wet_tsn_frame_t *frame, uint64_t current_epoch_ns) {
    if (!tw || !frame) return -1;

    /* Outbound stimulus artifact echo blanking check */
    if (frame->target_chamber < WET_MAX_CHAMBERS && tw->tx_blanking_ticks_remaining[frame->target_chamber] > 0) {
        return -5; /* Suppressed by local TX stimulus blanking window */
    }

    /* Cross-chamber epileptiform rate governor (max 50 Hz inter-chamber rate = 50 spikes / second) */
    if (current_epoch_ns > tw->rate_governor_last_tick + 1000000000ULL) {
        tw->rate_governor_window_spikes = 0;
        tw->rate_governor_last_tick = current_epoch_ns;
        tw->is_epileptiform_tripped = 0;
    }
    tw->rate_governor_window_spikes++;
    if (tw->rate_governor_window_spikes > 50) {
        tw->is_epileptiform_tripped = 1;
        return -4; /* Cross-chamber epileptiform runaway tripped */
    }

    /* Check for late arrival (transit delay exceeded axonal delay) */
    if (frame->release_epoch_ns < current_epoch_ns) {
        tw->late_drops++;
        return -2; /* Late drop */
    }

    /* Map absolute release epoch to wheel slot (100 us per slot) */
    uint64_t rel_slots = frame->release_epoch_ns / 100000ULL;
    uint32_t slot_idx = (uint32_t)(rel_slots % WET_TIMING_WHEEL_SLOTS);
    wet_timing_wheel_bucket_t *bucket = &tw->buckets[slot_idx];

    if (bucket->count >= WET_WHEEL_BUCKET_CAP) {
        tw->bucket_overflows++;
        return -3; /* Bucket overflow */
    }

    bucket->frames[bucket->count++] = *frame;
    tw->total_scheduled++;
    return 0;
}

uint32_t wet_timing_wheel_drain_tick(wet_timing_wheel_t *tw, uint64_t current_epoch_ns, wet_tsn_frame_t *out_ready, uint32_t max_count) {
    if (!tw || !out_ready || max_count == 0) return 0;

    /* Advance TX blanking counters */
    for (int c = 0; c < WET_MAX_CHAMBERS; c++) {
        if (tw->tx_blanking_ticks_remaining[c] > 0) {
            tw->tx_blanking_ticks_remaining[c]--;
        }
    }

    /* Map current absolute epoch to wheel slot */
    uint64_t curr_slots = current_epoch_ns / 100000ULL;
    uint32_t slot_idx = (uint32_t)(curr_slots % WET_TIMING_WHEEL_SLOTS);
    wet_timing_wheel_bucket_t *bucket = &tw->buckets[slot_idx];

    uint32_t ready_count = 0;
    while (ready_count < max_count && bucket->count > 0) {
        out_ready[ready_count++] = bucket->frames[--bucket->count];
        tw->total_dispatched++;
    }

    tw->current_wheel_tick = curr_slots;
    return ready_count;
}

void wet_timing_wheel_set_tx_blanking(wet_timing_wheel_t *tw, uint16_t target_chamber, uint32_t blanking_ticks) {
    if (!tw || target_chamber >= WET_MAX_CHAMBERS) return;
    tw->tx_blanking_ticks_remaining[target_chamber] = blanking_ticks;
}
