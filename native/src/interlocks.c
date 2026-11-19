#include "../include/wet_crt.h"
#include "../include/interlocks.h"

void interlocks_init(interlock_state_t* il) {
    if (!il) return;
    memset(il, 0, sizeof(interlock_state_t));
    il->authorized_capabilities = 0xFFFF; /* Default permissive until bytecode loaded */
    il->authorized_channels = INTERLOCK_NUM_CHANNELS;
    il->electrode_material = (uint8_t)WET_ELEC_PLATINUM;
    il->electrode_area_um2 = 5000.0f; /* Default macro-electrode area (5000 um^2) */
    il->max_charge_per_phase_nc = INTERLOCK_CHARGE_LIMIT_NC; /* Default 0.5 nC */
    il->max_cumulative_dc_nc = INTERLOCK_DC_DRIFT_LIMIT_NC;  /* Default 1.0 nC */
    for (int p = 0; p < 8; ++p) {
        il->pump_valve_mapping[p] = (uint8_t)p;
    }
}

void interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2) {
    if (!il) return;
    il->electrode_material = material;
    il->electrode_area_um2 = area_um2;

    /* Charge Injection Capacity (CIC) in mC/cm^2:
     * Area in cm^2 = area_um2 * 1e-8 cm^2/um^2
     * Max charge in nC = CIC (mC/cm^2) * Area (cm^2) * 1e6 nC/mC = CIC * area_um2 * 0.01 nC
     */
    float cic_mc_cm2 = 0.10f;
    switch ((wet_electrode_material_t)material) {
        case WET_ELEC_PLATINUM: cic_mc_cm2 = 0.10f; break; /* 0.05..0.15 mC/cm^2 water window */
        case WET_ELEC_TIN:      cic_mc_cm2 = 0.90f; break; /* Titanium Nitride */
        case WET_ELEC_IROX:     cic_mc_cm2 = 2.00f; break; /* Iridium Oxide */
        case WET_ELEC_PEDOT:    cic_mc_cm2 = 5.00f; break; /* Conductive polymer */
        default:                cic_mc_cm2 = 0.10f; break;
    }

    float limit_nc = cic_mc_cm2 * area_um2 * 0.01f;
    if (limit_nc < 0.01f) limit_nc = 0.01f;
    il->max_charge_per_phase_nc = limit_nc;
    il->max_cumulative_dc_nc = limit_nc * 2.0f;
}

void interlocks_active_discharge(interlock_state_t* il, uint8_t channel) {
    if (!il || channel >= INTERLOCK_NUM_CHANNELS) return;
    il->cumulative_unbounded_dc_nc[channel] = 0.0f;
    il->q_dc[channel] = 0.0f;
}

void interlocks_active_discharge_all(interlock_state_t* il) {
    if (!il) return;
    for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
        il->cumulative_unbounded_dc_nc[ch] = 0.0f;
        il->q_dc[ch] = 0.0f;
    }
}

void interlocks_enable_dead_head_protection(interlock_state_t* il, uint8_t enable) {
    if (!il) return;
    il->dead_head_protection_enabled = enable;
}

void interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count) {
    if (!il) return;
    il->authorized_capabilities = caps;
    il->authorized_channels = (channel_count > 0 && channel_count <= INTERLOCK_NUM_CHANNELS)
                              ? channel_count : INTERLOCK_NUM_CHANNELS;
}

void interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask) {
    if (!il) return;
    il->reference_channels_mask = ref_mask;
    il->recording_only_channels_mask = rec_mask;
}

int interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel) {
    if (!il) return 0;
    if (il->locked) return 0;

    /* Bounds check for channel-addressed opcodes */
    if (opcode == WET_OP_STIM_BIPHASIC || opcode == WET_OP_STIM_CURRENT ||
        opcode == WET_OP_READ_SPIKES || opcode == WET_OP_READ_VOLTAGE) {
        if ((uint32_t)channel >= il->authorized_channels) {
            return 0;
        }
    }

    /* Typed Channel Banks: Disallow stimulation on reference or recording-only electrodes */
    if (opcode == WET_OP_STIM_BIPHASIC || opcode == WET_OP_STIM_CURRENT) {
        if (channel < 64) {
            uint64_t ch_bit = 1ULL << channel;
            if ((il->reference_channels_mask & ch_bit) != 0ULL ||
                (il->recording_only_channels_mask & ch_bit) != 0ULL) {
                return 0; /* Capability Denied: Channel restricted to reference or recording */
            }
        }
    }

    switch ((wet_opcode_t)opcode) {
        case WET_OP_STIM_BIPHASIC:
        case WET_OP_STIM_CURRENT:
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

        /* Phase 3: Persistent unbounded cumulative DC charge accumulator (zero decay) */
        il->cumulative_unbounded_dc_nc[ch] += new_q;
        if (wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) < 1e-7f) {
            il->cumulative_unbounded_dc_nc[ch] = 0.0f;
        }

        float charge_limit = il->max_charge_per_phase_nc > 0.0f ? il->max_charge_per_phase_nc : INTERLOCK_CHARGE_LIMIT_NC;
        float dc_limit = il->max_cumulative_dc_nc > 0.0f ? il->max_cumulative_dc_nc : INTERLOCK_DC_DRIFT_LIMIT_NC;

        if (wet_fabsf(accum) >= charge_limit) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_CHARGE_IMBALANCE;
            il->tripped_channel = (uint8_t)ch;
            il->trip_tick = current_tick;
            il->trip_value = accum;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_CHARGE_IMBALANCE: ch=%d net_q=%.4f nC >= %.2f nC (CIC limit for material %u, area %.1f um2) at tick %llu",
                     ch, (double)accum, (double)charge_limit, il->electrode_material, (double)il->electrode_area_um2, (unsigned long long)current_tick);
            status = WET_ERR_CHARGE_IMBALANCE;
            break;
        }

        if (wet_fabsf(il->q_dc[ch]) >= dc_limit || wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) >= dc_limit) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_DC_DRIFT;
            il->tripped_channel = (uint8_t)ch;
            il->trip_tick = current_tick;
            il->trip_value = wet_fabsf(il->cumulative_unbounded_dc_nc[ch]) >= dc_limit ? il->cumulative_unbounded_dc_nc[ch] : il->q_dc[ch];
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_DC_DRIFT: ch=%d cumulative DC charge=%.4f nC >= %.2f nC at tick %llu",
                     ch, (double)il->trip_value, (double)dc_limit, (unsigned long long)current_tick);
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

wet_status_t interlocks_check_thermal(interlock_state_t* il, uint64_t current_tick, float temp_c) {
    if (!il) return WET_ERR_NULL_PTR;
    if (il->locked) return WET_ERR_INTERLOCK_LOCKED;

    if (temp_c > INTERLOCK_THERMAL_LIMIT_C) {
        il->locked = 1;
        il->trip_reason = INTERLOCK_TRIP_THERMAL_LIMIT;
        il->tripped_channel = 0xFF;
        il->trip_tick = current_tick;
        il->trip_value = temp_c;
        snprintf(il->diagnostic, sizeof(il->diagnostic),
                 "ERR_THERMAL_LIMIT: Temperature %.2f C exceeds incubator threshold (38.00 C) at tick %llu",
                 (double)temp_c, (unsigned long long)current_tick);
        return WET_ERR_THERMAL_LIMIT;
    }
    return WET_OK;
}

wet_status_t interlocks_check_bubble(interlock_state_t* il, uint64_t current_tick, uint8_t bubble_detected, uint8_t sensor_id) {
    if (!il) return WET_ERR_NULL_PTR;
    if (il->locked) return WET_ERR_INTERLOCK_LOCKED;

    if (bubble_detected) {
        il->locked = 1;
        il->trip_reason = INTERLOCK_TRIP_BUBBLE_DETECTED;
        il->tripped_channel = sensor_id;
        il->trip_tick = current_tick;
        il->trip_value = 1.0f;
        snprintf(il->diagnostic, sizeof(il->diagnostic),
                 "ERR_BUBBLE_DETECTED: Optical bubble sensor %u triggered (fluid line cavitation risk) at tick %llu",
                 sensor_id, (unsigned long long)current_tick);
        return WET_ERR_BUBBLE_DETECTED;
    }
    return WET_OK;
}

wet_status_t interlocks_check_compliance(interlock_state_t* il, uint64_t current_tick, uint8_t channel, float v_elec_v) {
    if (!il) return WET_ERR_NULL_PTR;
    if (il->locked) return WET_ERR_INTERLOCK_LOCKED;

    if (wet_fabsf(v_elec_v) > INTERLOCK_COMPLIANCE_LIMIT_V) {
        il->locked = 1;
        il->trip_reason = INTERLOCK_TRIP_COMPLIANCE_RAILED;
        il->tripped_channel = channel;
        il->trip_tick = current_tick;
        il->trip_value = v_elec_v;
        snprintf(il->diagnostic, sizeof(il->diagnostic),
                 "ERR_COMPLIANCE_RAILED: ch=%u electrode potential %.3f V exceeded compliance rail (+/-7.0 V) at tick %llu",
                 channel, (double)v_elec_v, (unsigned long long)current_tick);
        return WET_ERR_COMPLIANCE_RAILED;
    }
    return WET_OK;
}
