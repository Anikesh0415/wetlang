#include "../include/wet_crt.h"
#include "../include/interlocks.h"

void interlocks_init(interlock_state_t* il) {
    if (!il) return;
    memset(il, 0, sizeof(interlock_state_t));
    il->authorized_capabilities = 0xFFFF; /* Default permissive until bytecode loaded */
    il->authorized_channels = INTERLOCK_NUM_CHANNELS;
}

void interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count) {
    if (!il) return;
    il->authorized_capabilities = caps;
    il->authorized_channels = (channel_count > 0 && channel_count <= INTERLOCK_NUM_CHANNELS)
                              ? channel_count : INTERLOCK_NUM_CHANNELS;
}

int interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel) {
    if (!il) return 0;
    if (il->locked) return 0;

    /* Bounds check for channel-addressed opcodes */
    if (opcode == WET_OP_STIM_BIPHASIC || opcode == WET_OP_READ_SPIKES || opcode == WET_OP_READ_VOLTAGE) {
        if ((uint32_t)channel >= il->authorized_channels) {
            return 0;
        }
    }

    switch ((wet_opcode_t)opcode) {
        case WET_OP_STIM_BIPHASIC:
            if ((il->authorized_capabilities & WET_CAP_STIMULATION) == 0) {
                return 0;
            }
            if (wet_fabsf(voltage_v) > 0.8f && (il->authorized_capabilities & WET_CAP_HIGH_VOLTAGE) == 0) {
                return 0;
            }
            return 1;

        case WET_OP_MODULATE_STDP:
            if ((il->authorized_capabilities & WET_CAP_PLASTICITY) == 0) {
                return 0;
            }
            return 1;

        case WET_OP_PUMP_SET_RATE:
        case WET_OP_PUMP_DISPENSE:
        case WET_OP_VALVE_SET:
            if ((il->authorized_capabilities & WET_CAP_MICROFLUIDICS) == 0) {
                return 0;
            }
            return 1;

        case WET_OP_MOTOR_STEP:
            if ((il->authorized_capabilities & WET_CAP_MOTOR_ACTUATION) == 0) {
                return 0;
            }
            return 1;

        default:
            /* Tier 0 compute and Tier 1 passive readout always permitted */
            return 1;
    }
}

float interlocks_clamp_voltage(interlock_state_t* il, float requested_v) {
    if (requested_v > INTERLOCK_VOLTAGE_LIMIT_V) {
        if (il) il->clamp_events++;
        return INTERLOCK_VOLTAGE_LIMIT_V;
    }
    if (requested_v < -INTERLOCK_VOLTAGE_LIMIT_V) {
        if (il) il->clamp_events++;
        return -INTERLOCK_VOLTAGE_LIMIT_V;
    }
    return requested_v;
}

wet_status_t interlocks_record_charge_tick(
    interlock_state_t* il,
    uint64_t current_tick,
    const float tick_charge_nc[INTERLOCK_NUM_CHANNELS]
) {
    if (!il || !tick_charge_nc) return WET_ERR_NULL_PTR;
    if (il->locked) return WET_ERR_INTERLOCK_LOCKED;

    uint16_t head = il->q_head;
    wet_status_t status = WET_OK;

    for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
        float old_q = il->q_ring[ch][head];
        float new_q = tick_charge_nc[ch];
        il->q_ring[ch][head] = new_q;

        /* Recompute exact sum periodically or maintain running sum with drift-free precision */
        float accum = il->q_accum[ch] - old_q + new_q;
        if (wet_fabsf(accum) < 1e-7f) accum = 0.0f;
        il->q_accum[ch] = accum;

        /* Long-horizon leaky DC integrator (tau = 10.0 s = 100,000 ticks) */
        il->q_dc[ch] = il->q_dc[ch] * INTERLOCK_BLEED_DECAY_PER_TICK + new_q;
        if (wet_fabsf(il->q_dc[ch]) < 1e-7f) il->q_dc[ch] = 0.0f;

        if (wet_fabsf(accum) >= INTERLOCK_CHARGE_LIMIT_NC) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_CHARGE_IMBALANCE;
            il->tripped_channel = (uint8_t)ch;
            il->trip_tick = current_tick;
            il->trip_value = accum;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_CHARGE_IMBALANCE: ch=%d net_q=%.4f nC >= %.2f nC over 10.0 ms at tick %llu",
                     ch, (double)accum, (double)INTERLOCK_CHARGE_LIMIT_NC, (unsigned long long)current_tick);
            status = WET_ERR_CHARGE_IMBALANCE;
            break;
        }

        if (wet_fabsf(il->q_dc[ch]) >= INTERLOCK_DC_DRIFT_LIMIT_NC) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_DC_DRIFT;
            il->tripped_channel = (uint8_t)ch;
            il->trip_tick = current_tick;
            il->trip_value = il->q_dc[ch];
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_DC_DRIFT: ch=%d cumulative leaky DC charge=%.4f nC >= %.2f nC at tick %llu",
                     ch, (double)il->q_dc[ch], (double)INTERLOCK_DC_DRIFT_LIMIT_NC, (unsigned long long)current_tick);
            status = WET_ERR_DC_DRIFT;
            break;
        }
    }

    il->q_head = (uint16_t)((head + 1U) % INTERLOCK_CHARGE_WINDOW_TICKS);
    return status;
}

wet_status_t interlocks_check_epileptiform(
    interlock_state_t* il,
    uint64_t current_tick,
    const float channel_rates_hz[INTERLOCK_NUM_CHANNELS]
) {
    if (!il || !channel_rates_hz) return WET_ERR_NULL_PTR;
    if (il->locked) return WET_ERR_INTERLOCK_LOCKED;

    uint32_t hyper_count = 0U;
    for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
        if (channel_rates_hz[ch] >= INTERLOCK_EPILEPSY_RATE_HZ) {
            hyper_count++;
            il->focal_hyperactive_ticks[ch]++;
            if (il->focal_hyperactive_ticks[ch] >= INTERLOCK_FOCAL_SUSTAIN_TICKS) {
                il->locked = 1;
                il->trip_reason = INTERLOCK_TRIP_FOCAL_EXCITOTOXICITY;
                il->tripped_channel = (uint8_t)ch;
                il->trip_tick = current_tick;
                il->trip_value = channel_rates_hz[ch];
                snprintf(il->diagnostic, sizeof(il->diagnostic),
                         "ERR_FOCAL_EXCITOTOXICITY: ch=%d sustained %.1f Hz >= 150 Hz for 250.0 ms at tick %llu",
                         ch, (double)channel_rates_hz[ch], (unsigned long long)current_tick);
                return WET_ERR_FOCAL_EXCITOTOXICITY;
            }
        } else {
            il->focal_hyperactive_ticks[ch] = 0U;
        }
    }
    for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
        if (channel_rates_hz[ch] >= INTERLOCK_EPILEPSY_RATE_HZ) {
            hyper_count++;
        }
    }

    il->last_hyperactive_channel_count = hyper_count;

    if (hyper_count >= INTERLOCK_EPILEPSY_MIN_CHANNELS) {
        il->hyperactive_consecutive_ticks++;
        if (il->hyperactive_consecutive_ticks >= INTERLOCK_EPILEPSY_SUSTAIN_TICKS) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_EPILEPTIFORM_RUNAWAY;
            il->tripped_channel = 0xFF;
            il->trip_tick = current_tick;
            il->trip_value = (float)hyper_count;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_EPILEPTIFORM_RUNAWAY: %u/64 channels (>35%%) exceeded 150 Hz for 50.0 ms at tick %llu",
                     hyper_count, (unsigned long long)current_tick);
            return WET_ERR_EPILEPTIFORM_RUNAWAY;
        }
    } else {
        il->hyperactive_consecutive_ticks = 0U;
    }

    return WET_OK;
}
