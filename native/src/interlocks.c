#include "../include/wet_crt.h"
#include "../include/interlocks.h"

void interlocks_init(interlock_state_t* il) {
    if (!il) return;
    memset(il, 0, sizeof(interlock_state_t));
    il->authorized_capabilities = 0xFFFF; /* Default permissive until bytecode loaded */
    il->authorized_channels = INTERLOCK_NUM_CHANNELS;
    il->electrode_material = (uint8_t)WET_ELEC_PLATINUM;
    il->electrode_area_um2 = 5000.0f; /* Default macro-electrode area (5000 um^2) */
    il->v_water_window_low_v = -0.6f;  /* Platinum safe cathodic limit */
    il->v_water_window_high_v = +0.8f; /* Platinum safe anodic limit */
    il->max_charge_per_phase_nc = INTERLOCK_CHARGE_LIMIT_NC; /* Default 0.5 nC */
    il->max_cumulative_dc_nc = INTERLOCK_DC_DRIFT_LIMIT_NC;  /* Default 1.0 nC */
    il->max_faradaic_current_density_ua_cm2 = 30.0f; /* 30.0 uA/cm^2 safe Faradaic limit */
    il->dynamic_impedance_clamp_events = 0;
    for (int p = 0; p < 8; ++p) {
        il->pump_valve_mapping[p] = (uint8_t)p;
    }
}

void interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2) {
    if (!il) return;
    if (!wet_isfinite_f(area_um2) || area_um2 <= 0.0f) {
        area_um2 = 5000.0f;
    }
    il->electrode_material = material;
    il->electrode_area_um2 = area_um2;

    /* Charge Injection Capacity (CIC) in mC/cm^2:
     * Area in cm^2 = area_um2 * 1e-8 cm^2/um^2
     * Max charge in nC = CIC (mC/cm^2) * Area (cm^2) * 1e6 nC/mC = CIC * area_um2 * 0.01 nC
     */
    float cic_mc_cm2 = 0.10f;
    float v_low = -0.6f;
    float v_high = +0.8f;

    switch ((wet_electrode_material_t)material) {
        case WET_ELEC_PLATINUM:
            cic_mc_cm2 = 0.10f;
            v_low = -0.6f;
            v_high = +0.8f;
            break;
        case WET_ELEC_IROX:
            cic_mc_cm2 = 2.00f;
            v_low = -0.6f;
            v_high = +0.8f;
            break;
        case WET_ELEC_TIN:
            cic_mc_cm2 = 0.90f;
            v_low = -0.9f;
            v_high = +0.9f;
            break;
        case WET_ELEC_PEDOT:
            cic_mc_cm2 = 5.00f;
            v_low = -0.9f;
            v_high = +0.6f;
            break;
        default:
            cic_mc_cm2 = 0.10f;
            v_low = -0.6f;
            v_high = +0.8f;
            break;
    }

    il->v_water_window_low_v = v_low;
    il->v_water_window_high_v = v_high;

    float limit_nc = cic_mc_cm2 * area_um2 * 0.01f;
    if (limit_nc < 0.01f) limit_nc = 0.01f;
    il->max_charge_per_phase_nc = limit_nc;
    il->max_cumulative_dc_nc = limit_nc * 2.0f;
}

wet_status_t interlocks_configure_electrode_area(interlock_state_t* il, uint16_t channel, float area_cm2) {
    if (!il) return WET_ERR_NULL_PTR;
    if (!wet_isfinite_f(area_cm2) || area_cm2 <= 0.0f) {
        snprintf(il->diagnostic, sizeof(il->diagnostic),
                 "ERR_INVALID_ARG: electrode area must be finite and > 0 cm2");
        return WET_ERR_INVALID_ARG;
    }
    if (channel == 0xFFFFU) {
        for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
            il->channel_area_cm2[ch] = area_cm2;
            il->has_channel_area[ch] = 1U;
        }
        il->electrode_area_um2 = area_cm2 * 1e8f;
        return WET_OK;
    }
    if (channel >= INTERLOCK_NUM_CHANNELS) {
        return WET_ERR_OUT_OF_BOUNDS_CH;
    }
    il->channel_area_cm2[channel] = area_cm2;
    il->has_channel_area[channel] = 1U;
    return WET_OK;
}

wet_status_t interlocks_check_shannon_limit(
    interlock_state_t* il,
    uint64_t tick,
    uint8_t channel,
    float current_ua,
    float phase1_ms,
    float phase2_ms
) {
    if (!il) return WET_ERR_NULL_PTR;
    if (channel >= INTERLOCK_NUM_CHANNELS || !il->has_channel_area[channel]) {
        return WET_OK;
    }
    if (!wet_isfinite_f(current_ua) || !wet_isfinite_f(phase1_ms) || !wet_isfinite_f(phase2_ms)) {
        return WET_ERR_INVALID_ARG;
    }
    double area_cm2 = (double)il->channel_area_cm2[channel];
    if (!wet_isfinite_d(area_cm2) || area_cm2 <= 0.0) {
        return WET_ERR_INVALID_ARG;
    }

    double q1_uc = (phase1_ms > 0.0f) ? ((double)wet_fabsf(current_ua) * (double)phase1_ms * 1e-3) : 0.0;
    double q2_uc = (phase2_ms > 0.0f) ? ((double)wet_fabsf(current_ua) * (double)phase2_ms * 1e-3) : 0.0;
    double q_uc = (q1_uc >= q2_uc) ? q1_uc : q2_uc;
    if (q_uc <= 0.0) {
        return WET_OK;
    }

    double d_uc_cm2 = q_uc / area_cm2;
    double prod = d_uc_cm2 * q_uc;
    double k_val = 0.0;
    int tripped = 0;
    if (!wet_isfinite_d(prod)) {
        tripped = 1;
        k_val = 999.0;
    } else if (prod > 0.0) {
        k_val = wet_log10(prod);
        if (!wet_isfinite_d(k_val) || k_val > 1.75) {
            tripped = 1;
        }
    }

    if (tripped) {
        il->locked = 1;
        il->trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
        il->tripped_channel = channel;
        il->trip_tick = tick;
        il->trip_value = (float)k_val;
        snprintf(il->diagnostic, sizeof(il->diagnostic),
                 "ERR_SHANNON_LIMIT_EXCEEDED: ch=%u log10(D*Q)=%.4f > 1.75 (Q=%.6f uC, A=%.6e cm2)",
                 channel, (double)il->trip_value, q_uc, area_cm2);
        return WET_ERR_CHARGE_DENSITY_EXCEEDED;
    }
    return WET_OK;
}

void interlocks_active_discharge(interlock_state_t* il, uint8_t channel) {
    if (!il || channel >= INTERLOCK_NUM_CHANNELS) return;
    il->cumulative_unbounded_dc_nc[channel] = 0.0f;
    il->cumulative_dc_attocoulombs[channel] = 0;
    il->q_dc[channel] = 0.0f;
}

void interlocks_active_discharge_all(interlock_state_t* il) {
    if (!il) return;
    for (int ch = 0; ch < INTERLOCK_NUM_CHANNELS; ++ch) {
        il->cumulative_unbounded_dc_nc[ch] = 0.0f;
        il->cumulative_dc_attocoulombs[ch] = 0;
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
    il->authorized_channels = channel_count > 0 ? channel_count : INTERLOCK_NUM_CHANNELS;
}

void interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask) {
    if (!il) return;
    il->reference_channels_mask = ref_mask;
    il->recording_only_channels_mask = rec_mask;
}

int interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint32_t channel) {
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
        } else if (il->reference_channels_mask != 0ULL || il->recording_only_channels_mask != 0ULL) {
            return 0; /* Fail-safe: bank masks only cover 0..63; deny unverified high channels */
        }
    }

    switch ((wet_opcode_t)opcode) {
        case WET_OP_STIM_BIPHASIC:
        case WET_OP_STIM_CURRENT:
            if (!wet_isfinite_f(voltage_v)) {
                return 0;
            }
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
    if (!wet_isfinite_f(requested_v)) {
        if (il) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_VOLTAGE_OVERRIDE;
            il->clamp_events++;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_VOLTAGE_OVERRIDE: Non-finite (NaN/Inf) stimulation voltage rejected (fail-closed)");
        }
        return 0.0f;
    }
    if (il && il->locked) {
        return 0.0f;
    }

    float v_high = (il && wet_isfinite_f(il->v_water_window_high_v) && il->v_water_window_high_v > 0.0f)
                   ? il->v_water_window_high_v : 0.8f;
    float v_low  = (il && wet_isfinite_f(il->v_water_window_low_v) && il->v_water_window_low_v < 0.0f)
                   ? il->v_water_window_low_v  : -0.6f;

    if (requested_v > v_high) {
        if (il) il->clamp_events++;
        return v_high;
    }
    if (requested_v < v_low) {
        if (il) il->clamp_events++;
        return v_low;
    }
    return requested_v;
}

void interlocks_set_electrode_impedance(
    interlock_state_t* il,
    uint8_t channel,
    float z_magnitude_ohms,
    float z_phase_rad,
    uint64_t tick
) {
    if (!il || channel >= INTERLOCK_NUM_CHANNELS) return;
    il->impedance[channel].z_magnitude_ohms = (wet_isfinite_f(z_magnitude_ohms) && z_magnitude_ohms > 1.0f) ? z_magnitude_ohms : 1.0f;
    il->impedance[channel].z_phase_rad = wet_isfinite_f(z_phase_rad) ? z_phase_rad : 0.0f;
    il->impedance[channel].last_calibration_tick = tick;
}

void interlocks_set_current_density_limit(interlock_state_t* il, float max_ua_cm2) {
    if (!il) return;
    il->max_faradaic_current_density_ua_cm2 = (wet_isfinite_f(max_ua_cm2) && max_ua_cm2 > 0.0f) ? max_ua_cm2 : 30.0f;
}

float interlocks_clamp_voltage_dynamic(interlock_state_t* il, uint8_t channel, float requested_v) {
    if (!wet_isfinite_f(requested_v)) {
        if (il) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_VOLTAGE_OVERRIDE;
            il->tripped_channel = channel;
            il->clamp_events++;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_VOLTAGE_OVERRIDE: ch=%u non-finite (NaN/Inf) voltage rejected (fail-closed)", channel);
        }
        return 0.0f;
    }
    if (!il) return requested_v;
    if (il->locked) return 0.0f;

    /* 1. First clamp to material-dependent water window rails */
    float v_clamped = interlocks_clamp_voltage(il, requested_v);

    /* 2. Enforce dynamic adaptive current limiting: I_peak = V_command / Z_magnitude */
    if (channel >= INTERLOCK_NUM_CHANNELS) {
        il->clamp_events++;
        return 0.0f;
    }
    if (wet_isfinite_f(il->max_faradaic_current_density_ua_cm2) && il->max_faradaic_current_density_ua_cm2 > 0.0f) {
        float z_mag = il->impedance[channel].z_magnitude_ohms;
        if (!wet_isfinite_f(z_mag) || z_mag < 0.0f) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_VOLTAGE_OVERRIDE;
            il->tripped_channel = channel;
            il->clamp_events++;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_VOLTAGE_OVERRIDE: ch=%u invalid impedance in dynamic clamp", channel);
            return 0.0f;
        }
        if (z_mag > 0.0f) {
            float area_um2 = (wet_isfinite_f(il->electrode_area_um2) && il->electrode_area_um2 > 0.0f)
                             ? il->electrode_area_um2 : 5000.0f;
            float area_cm2 = area_um2 * 1e-8f;

            /* Safe Faradaic current limit in Amperes: I_safe = J_limit (A/cm^2) * Area (cm^2) */
            float j_limit_a_cm2 = il->max_faradaic_current_density_ua_cm2 * 1e-6f;
            float i_safe_a = j_limit_a_cm2 * area_cm2;

            /* Maximum allowable dynamic voltage magnitude V_safe = I_safe * Z */
            float v_safe_mag = i_safe_a * z_mag;
            if (!wet_isfinite_f(v_safe_mag) || v_safe_mag < 0.0f) {
                il->locked = 1;
                il->trip_reason = INTERLOCK_TRIP_VOLTAGE_OVERRIDE;
                il->tripped_channel = channel;
                il->clamp_events++;
                return 0.0f;
            }

            if (v_safe_mag > 0.0f && wet_fabsf(v_clamped) > v_safe_mag) {
                float sign = (v_clamped >= 0.0f) ? 1.0f : -1.0f;
                v_clamped = sign * v_safe_mag;
                il->clamp_events++;
                il->dynamic_impedance_clamp_events++;
            }
        }
    }
    return v_clamped;
}

int wet_interlock_check_voltage(
    interlock_state_t* il,
    uint8_t channel,
    float requested_v,
    float* out_clamped_v
) {
    if (!wet_isfinite_f(requested_v)) {
        float clamped = interlocks_clamp_voltage_dynamic(il, channel, requested_v);
        if (out_clamped_v) *out_clamped_v = clamped;
        return 1;
    }
    if (!il) {
        if (out_clamped_v) *out_clamped_v = requested_v;
        return 0;
    }
    float clamped = interlocks_clamp_voltage_dynamic(il, channel, requested_v);
    if (out_clamped_v) *out_clamped_v = clamped;
    return (!wet_isfinite_f(clamped) || wet_fabsf(clamped - requested_v) > 1e-6f) ? 1 : 0;
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
        if (!wet_isfinite_f(new_q)) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_CHARGE_IMBALANCE;
            il->tripped_channel = (uint8_t)ch;
            il->trip_tick = current_tick;
            il->trip_value = 0.0f;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_CHARGE_IMBALANCE: ch=%d non-finite (NaN/Inf) charge value at tick %llu",
                     ch, (unsigned long long)current_tick);
            status = WET_ERR_CHARGE_IMBALANCE;
            break;
        }
        il->q_ring[ch][head] = new_q;

        /* Recompute exact sum periodically or maintain running sum with drift-free precision */
        float accum = il->q_accum[ch] - old_q + new_q;
        if (!wet_isfinite_f(accum)) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_CHARGE_IMBALANCE;
            il->tripped_channel = (uint8_t)ch;
            il->trip_tick = current_tick;
            il->trip_value = 0.0f;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_CHARGE_IMBALANCE: ch=%d non-finite charge accumulator at tick %llu",
                     ch, (unsigned long long)current_tick);
            status = WET_ERR_CHARGE_IMBALANCE;
            break;
        }
        if (wet_fabsf(accum) < 1e-7f) accum = 0.0f;
        il->q_accum[ch] = accum;

        /* Long-horizon leaky DC integrator (tau = 10.0 s = 100,000 ticks) */
        il->q_dc[ch] = il->q_dc[ch] * INTERLOCK_BLEED_DECAY_PER_TICK + new_q;
        if (!wet_isfinite_f(il->q_dc[ch])) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_DC_DRIFT;
            il->tripped_channel = (uint8_t)ch;
            il->trip_tick = current_tick;
            il->trip_value = 0.0f;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_DC_DRIFT: ch=%d non-finite leaky DC accumulator at tick %llu",
                     ch, (unsigned long long)current_tick);
            status = WET_ERR_DC_DRIFT;
            break;
        }
        if (wet_fabsf(il->q_dc[ch]) < 1e-7f) il->q_dc[ch] = 0.0f;

        /* Phase 3 & v2.1: Persistent unbounded cumulative DC charge accumulator
         * (zero decay, exact fixed-point attoCoulombs: 1 nC = 1e9 aC).
         * Eliminates the 0.1 fC (1 pA * 100 us) truncation defect under multi-week soak protocols. */
        double scaled_ac = wet_clampd((double)new_q * 1000000000.0, -4.0e18, 4.0e18);
        int64_t delta_ac = wet_llround(scaled_ac);
        int64_t cur_ac = il->cumulative_dc_attocoulombs[ch];
        if (delta_ac > 0 && cur_ac > INT64_MAX - delta_ac) {
            il->cumulative_dc_attocoulombs[ch] = INT64_MAX;
        } else if (delta_ac < 0 && cur_ac < INT64_MIN - delta_ac) {
            il->cumulative_dc_attocoulombs[ch] = INT64_MIN;
        } else {
            il->cumulative_dc_attocoulombs[ch] = cur_ac + delta_ac;
        }
        il->cumulative_unbounded_dc_nc[ch] = (float)((double)il->cumulative_dc_attocoulombs[ch] * 1e-9);
        if (il->cumulative_dc_attocoulombs[ch] == 0) {
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
        if (!wet_isfinite_f(channel_rates_hz[ch])) {
            il->locked = 1;
            il->trip_reason = INTERLOCK_TRIP_FOCAL_EXCITOTOXICITY;
            il->tripped_channel = (uint8_t)ch;
            il->trip_tick = current_tick;
            il->trip_value = 0.0f;
            snprintf(il->diagnostic, sizeof(il->diagnostic),
                     "ERR_FOCAL_EXCITOTOXICITY: ch=%d non-finite (NaN/Inf) firing rate at tick %llu",
                     ch, (unsigned long long)current_tick);
            return WET_ERR_FOCAL_EXCITOTOXICITY;
        }
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

    if (!wet_isfinite_f(temp_c) || temp_c > INTERLOCK_THERMAL_LIMIT_C) {
        il->locked = 1;
        il->trip_reason = INTERLOCK_TRIP_THERMAL_LIMIT;
        il->tripped_channel = 0xFF;
        il->trip_tick = current_tick;
        il->trip_value = wet_isfinite_f(temp_c) ? temp_c : 0.0f;
        snprintf(il->diagnostic, sizeof(il->diagnostic),
                 "ERR_THERMAL_LIMIT: Temperature %.2f C exceeds incubator threshold (38.00 C) at tick %llu",
                 (double)il->trip_value, (unsigned long long)current_tick);
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

    if (!wet_isfinite_f(v_elec_v) || wet_fabsf(v_elec_v) > INTERLOCK_COMPLIANCE_LIMIT_V) {
        il->locked = 1;
        il->trip_reason = INTERLOCK_TRIP_COMPLIANCE_RAILED;
        il->tripped_channel = channel;
        il->trip_tick = current_tick;
        il->trip_value = wet_isfinite_f(v_elec_v) ? v_elec_v : 0.0f;
        snprintf(il->diagnostic, sizeof(il->diagnostic),
                 "ERR_COMPLIANCE_RAILED: ch=%u electrode potential %.3f V exceeded compliance rail (+/-7.0 V) at tick %llu",
                 channel, (double)il->trip_value, (unsigned long long)current_tick);
        return WET_ERR_COMPLIANCE_RAILED;
    }
    return WET_OK;
}
