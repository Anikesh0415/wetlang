#include "../include/wet_crt.h"
#include "../include/biophysics.h"

/* =========================================================================
 * Helper: Initialize Tsodyks-Markram STP parameters by cortical synapse class
 * ========================================================================= */
static void init_synapse_stp(bio_synapse_t* syn, uint8_t pre_exc, uint8_t post_exc, float weight_ns) {
    syn->exists = 1;
    syn->weight_ns = wet_clampf(weight_ns, BIO_W_MIN_NS, BIO_W_MAX_NS);

    if (pre_exc && post_exc) {
        syn->syn_class = SYN_CLASS_EE;
        syn->U_base = 0.50f;
        syn->tau_rec_ms = 800.0f;
        syn->tau_fac_ms = 20.0f;
    } else if (pre_exc && !post_exc) {
        syn->syn_class = SYN_CLASS_EI;
        syn->U_base = 0.15f;
        syn->tau_rec_ms = 200.0f;
        syn->tau_fac_ms = 600.0f;
    } else if (!pre_exc && post_exc) {
        syn->syn_class = SYN_CLASS_IE;
        syn->U_base = 0.25f;
        syn->tau_rec_ms = 700.0f; /* Gupta et al. 2000 F2 empirical mean (706 ms) */
        syn->tau_fac_ms = 50.0f;
    } else {
        syn->syn_class = SYN_CLASS_II;
        syn->U_base = 0.30f;
        syn->tau_rec_ms = 400.0f;
        syn->tau_fac_ms = 50.0f;
    }

    syn->u_stp = syn->U_base;
    syn->x_stp = 1.0f;
}

void biophysics_init(bio_state_t* bio, double dt_ms, uint64_t seed) {
    if (!bio) return;
    memset(bio, 0, sizeof(bio_state_t));

    bio->dt_ms = (dt_ms > 0.0) ? dt_ms : 0.1;
    bio->rng_state = (seed != 0) ? seed : 0x574554574F524C44ULL; /* "WETWORLD" */
    bio->stdp_lr_scale = 1.0f;
    bio->noise_enabled = 1;

    /* Biophysical constants (COBA-LIF cortical organoid parameters) */
    bio->c_m_pf            = 200.0f;   /* 200 pF */
    bio->g_leak_ns         = 10.0f;    /* 10 nS -> tau_m = 20.0 ms */
    bio->e_leak_mv         = -70.0f;
    bio->e_reset_mv        = -75.0f;
    bio->e_thresh_base_mv  = -50.0f;
    bio->e_exc_mv          = 0.0f;
    bio->e_inh_mv          = -80.0f;
    bio->e_k_mv            = -90.0f;
    bio->tau_exc_ms        = 5.0f;     /* AMPA */
    bio->tau_inh_ms        = 10.0f;    /* GABA_A */
    bio->tau_ahp_ms        = 80.0f;    /* Slow K+ AHP */
    bio->tau_thresh_ms     = 10.0f;    /* Relative refractory threshold decay */
    bio->tau_stdp_plus_ms  = 20.0f;
    bio->tau_stdp_minus_ms = 20.0f;
    bio->stdp_a_plus       = 0.20f;
    bio->stdp_a_minus      = 0.21f;    /* 1.05x LTD bias for network stability */
    bio->electrode_impedance_kohm = 1000.0f; /* 1 MOhm microelectrode impedance */

    /* Phase 3 Blanking and Randles Equivalent Circuit Parameters */
    bio->default_blanking_ticks = 20;   /* 2.0 ms default amplifier blanking */
    bio->spatial_blanking_enabled = 1;  /* Enable adjacent channel crosstalk blanking */
    bio->r_solution_kohm = 2.0f;        /* 2.0 kOhm electrolyte solution resistance */
    bio->r_charge_transfer_kohm = 5000.0f; /* 5.0 MOhm Faradaic charge transfer resistance */
    bio->max_compliance_voltage_v = 7.0f;  /* +/-7.0 V Intan RHS2116 compliance limit */
    bio->v_water_window_low_v = -0.6f;     /* Platinum safe cathodic limit */
    bio->v_water_window_high_v = 0.8f;     /* Platinum safe anodic limit */

    for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        bio->c_double_layer_pf[ch] = 26.45f; /* 26.45 pF for 132 um2 microelectrode */
        bio->v_double_layer_v[ch] = 0.0f;
        bio->last_stim_current_ua[ch] = 0.0f;
        bio->stim_blanking_ticks[ch] = 0;
    }

    /* 1. Place 64 neurons over 8x8 MEA (200 um pitch), 80% Exc (51) / 20% Inh (13) */
    for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
        int r = i / BIO_GRID_COLS;
        int c = i % BIO_GRID_COLS;

        /* Deterministic spatially distributed 20% inhibitory interneurons */
        bio->is_excitatory[i] = ((i % 5) != 4) ? 1 : 0;

        float jx = (float)(wet_rng_uniform(&bio->rng_state) - 0.5) * 30.0f;
        float jy = (float)(wet_rng_uniform(&bio->rng_state) - 0.5) * 30.0f;
        float jz = 20.0f + (float)wet_rng_uniform(&bio->rng_state) * 15.0f;

        bio->pos_x_um[i] = (float)c * BIO_PITCH_UM + jx;
        bio->pos_y_um[i] = (float)r * BIO_PITCH_UM + jy;
        bio->pos_z_um[i] = jz;

        /* Slight heterogeneity in resting membrane potential */
        bio->v_m_mv[i] = bio->e_leak_mv + (float)(wet_rng_uniform(&bio->rng_state) - 0.5) * 4.0f;
        bio->v_thresh_mv[i] = bio->e_thresh_base_mv;
    }

    /* 2. Compute 8x8 MEA 3D volume conduction forward pickup matrix */
    const float lambda_um = 120.0f;
    for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        int col = ch % BIO_GRID_COLS;
        int row = ch / BIO_GRID_COLS;
        float ex = (float)col * BIO_PITCH_UM;
        float ey = (float)row * BIO_PITCH_UM;
        float ez = 0.0f;

        float row_sum = 0.0f;
        for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
            float dx = bio->pos_x_um[i] - ex;
            float dy = bio->pos_y_um[i] - ey;
            float dz = bio->pos_z_um[i] - ez;
            float dist_sq = dx * dx + dy * dy + dz * dz;
            float gain = 1.0f / (1.0f + dist_sq / (lambda_um * lambda_um));
            bio->pickup_matrix[ch][i] = gain;
            row_sum += gain;
        }
        if (row_sum > 1e-6f) {
            for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
                bio->pickup_matrix[ch][i] /= row_sum;
            }
        }
    }

    /* 3. Build distance-dependent sparse cortical connectivity (~20% density) */
    const float conn_scale_um = 350.0f;
    for (int pre = 0; pre < BIO_NUM_NEURONS; ++pre) {
        for (int post = 0; post < BIO_NUM_NEURONS; ++post) {
            if (pre == post) continue;
            float dx = bio->pos_x_um[post] - bio->pos_x_um[pre];
            float dy = bio->pos_y_um[post] - bio->pos_y_um[pre];
            float dz = bio->pos_z_um[post] - bio->pos_z_um[pre];
            float dist = (float)wet_sqrt((double)(dx * dx + dy * dy + dz * dz));
            double p_conn = 0.35 * wet_exp(-(double)(dist / conn_scale_um));
            if (wet_rng_uniform(&bio->rng_state) < p_conn) {
                float w0 = bio->is_excitatory[pre]
                    ? (4.0f + (float)wet_rng_uniform(&bio->rng_state) * 6.0f)
                    : (10.0f + (float)wet_rng_uniform(&bio->rng_state) * 10.0f);
                init_synapse_stp(&bio->synapses[pre][post],
                                 bio->is_excitatory[pre],
                                 bio->is_excitatory[post],
                                 w0);
            }
        }
    }
}

void biophysics_reset(bio_state_t* bio) {
    if (!bio) return;
    double dt = bio->dt_ms;
    biophysics_init(bio, dt, 0x574554574F524C44ULL);
}

void biophysics_schedule_stim_ext(
    bio_state_t* bio,
    uint8_t channel,
    float clamped_voltage_v,
    float phase1_ms,
    float phase2_ms,
    float interphase_ms
) {
    if (!bio || channel >= BIO_NUM_CHANNELS) return;

    float dt = (float)bio->dt_ms;
    uint32_t p1_ticks = (phase1_ms > 0.0f) ? (uint32_t)(phase1_ms / dt + 0.5f) : 0U;
    uint32_t p2_ticks = (phase2_ms > 0.0f) ? (uint32_t)(phase2_ms / dt + 0.5f) : 0U;
    uint32_t ip_ticks = (interphase_ms > 0.0f) ? (uint32_t)(interphase_ms / dt + 0.5f) : 0U;

    if (p1_ticks == 0 && p2_ticks == 0) {
        bio->stim_pulses[channel].active = 0;
        return;
    }

    bio_stim_pulse_t* p = &bio->stim_pulses[channel];
    p->active = 1;
    p->voltage_v = clamped_voltage_v;
    p->phase1_ticks_left = p1_ticks;
    p->interphase_ticks_left = ip_ticks;
    p->phase2_ticks_left = p2_ticks;

    /* Neurophysiologically grounded extracellular stimulation:
     * Phase 1 is negative (cathodic) relative to extracellular bath (depolarizing soma).
     * Phase 2 is positive (anodic) counter-charge. */
    float v_mag = wet_fabsf(clamped_voltage_v);
    p->phase1_amp_v = -v_mag;
    p->phase2_amp_v = v_mag;

    /* Set post-stimulus amplifier blanking window with spatial crosstalk neighbor propagation */
    uint16_t post_blank = bio->has_channel_blanking[channel]
        ? bio->channel_blanking_ticks[channel]
        : bio->default_blanking_ticks;
    uint8_t use_spatial = bio->has_channel_blanking[channel]
        ? bio->channel_spatial_blanking[channel]
        : bio->spatial_blanking_enabled;
    uint16_t total_blanking = (uint16_t)(p1_ticks + ip_ticks + p2_ticks + post_blank);
    if (bio->stim_blanking_ticks[channel] < total_blanking) {
        bio->stim_blanking_ticks[channel] = total_blanking;
    }

    if (use_spatial) {
        int r1 = channel / BIO_GRID_COLS;
        int c1 = channel % BIO_GRID_COLS;
        uint16_t neighbor_blank = (total_blanking * 3) / 4;
        for (int r2 = r1 - 1; r2 <= r1 + 1; ++r2) {
            for (int c2 = c1 - 1; c2 <= c1 + 1; ++c2) {
                if (r2 >= 0 && r2 < BIO_GRID_ROWS && c2 >= 0 && c2 < BIO_GRID_COLS) {
                    int neighbor_ch = r2 * BIO_GRID_COLS + c2;
                    if (neighbor_ch != (int)channel && bio->stim_blanking_ticks[neighbor_ch] < neighbor_blank) {
                        bio->stim_blanking_ticks[neighbor_ch] = neighbor_blank;
                    }
                }
            }
        }
    }
}

void biophysics_schedule_stim_current(
    bio_state_t* bio,
    uint8_t channel,
    float current_ua,
    float phase1_ms,
    float phase2_ms,
    float interphase_ms
) {
    if (!bio || channel >= BIO_NUM_CHANNELS) return;
    bio->last_stim_current_ua[channel] = current_ua;

    /* Randles interface: Effective applied voltage V_eff = I * Rs + V_dl */
    float v_eff = (current_ua / 1000.0f) * bio->r_solution_kohm + bio->v_double_layer_v[channel];
    biophysics_schedule_stim_ext(bio, channel, v_eff, phase1_ms, phase2_ms, interphase_ms);
}

void biophysics_set_blanking_window(bio_state_t* bio, float blanking_ms, uint8_t enable_spatial) {
    if (!bio) return;
    float dt = (float)bio->dt_ms;
    if (dt <= 0.0f) dt = 0.1f;
    uint16_t ticks = (uint16_t)(blanking_ms / dt + 0.5f);
    if (ticks == 0U) ticks = 1U;
    bio->default_blanking_ticks = ticks;
    bio->spatial_blanking_enabled = enable_spatial ? 1U : 0U;
    memset(bio->has_channel_blanking, 0, sizeof(bio->has_channel_blanking));
}

void biophysics_set_channel_blanking_window(bio_state_t* bio, uint16_t channel, float blanking_ms, uint8_t enable_spatial) {
    if (!bio) return;
    if (channel == 0xFFFFU) {
        biophysics_set_blanking_window(bio, blanking_ms, enable_spatial);
        return;
    }
    if (channel >= BIO_NUM_CHANNELS) return;
    float dt = (float)bio->dt_ms;
    if (dt <= 0.0f) dt = 0.1f;
    uint16_t ticks = (uint16_t)(blanking_ms / dt + 0.5f);
    if (ticks == 0U) ticks = 1U;
    bio->channel_blanking_ticks[channel] = ticks;
    bio->channel_spatial_blanking[channel] = enable_spatial ? 1U : 0U;
    bio->has_channel_blanking[channel] = 1U;
}

void biophysics_get_randles_state(
    const bio_state_t* bio,
    uint8_t channel,
    float* out_v_dl_v,
    float* out_v_elec_v
) {
    if (!bio || channel >= BIO_NUM_CHANNELS) return;
    float v_dl = bio->v_double_layer_v[channel];
    float v_elec = (bio->last_stim_current_ua[channel] / 1000.0f) * bio->r_solution_kohm + v_dl;
    if (out_v_dl_v) *out_v_dl_v = v_dl;
    if (out_v_elec_v) *out_v_elec_v = v_elec;
}

void biophysics_schedule_stim(
    bio_state_t* bio,
    uint8_t channel,
    float clamped_voltage_v,
    float phase1_ms,
    float phase2_ms
) {
    biophysics_schedule_stim_ext(bio, channel, clamped_voltage_v, phase1_ms, phase2_ms, 0.0f);
}

void biophysics_zero_all_stim(bio_state_t* bio) {
    if (!bio) return;
    for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        bio->stim_pulses[ch].active = 0;
        bio->stim_pulses[ch].phase1_ticks_left = 0;
        bio->stim_pulses[ch].interphase_ticks_left = 0;
        bio->stim_pulses[ch].phase2_ticks_left = 0;
        bio->stim_pulses[ch].voltage_v = 0.0f;
        bio->stim_pulses[ch].phase1_amp_v = 0.0f;
        bio->stim_pulses[ch].phase2_amp_v = 0.0f;
        bio->ext_stim_v[ch] = 0.0f;
        bio->tick_charge_nc[ch] = 0.0f;
        bio->stim_blanking_ticks[ch] = 0;
        bio->blanking_active[ch] = 0;
    }
}

void biophysics_modulate_stdp(bio_state_t* bio, uint8_t pre, uint8_t post, float delta_w_ns) {
    if (!bio || pre >= BIO_NUM_NEURONS || post >= BIO_NUM_NEURONS) return;
    if (pre == post) return;

    bio_synapse_t* syn = &bio->synapses[pre][post];
    if (!syn->exists) {
        if (delta_w_ns > 0.0f) {
            init_synapse_stp(syn, bio->is_excitatory[pre], bio->is_excitatory[post], delta_w_ns);
            bio->cumulative_weight_drift_ns += wet_fabsf(syn->weight_ns);
        }
        return;
    }

    /* Dale's Principle: Conductance magnitude strictly bounded in [0, 40 nS]; sign fixed by E_rev */
    float old_w = syn->weight_ns;
    float new_w = wet_clampf(old_w + delta_w_ns, BIO_W_MIN_NS, BIO_W_MAX_NS);
    syn->weight_ns = new_w;
    bio->cumulative_weight_drift_ns += wet_fabsf(new_w - old_w);
}

void biophysics_step_tick(bio_state_t* bio) {
    if (!bio) return;

    const double dt = bio->dt_ms;
    const float  dt_f = (float)dt;

    /* Precompute exact exponential decay factors */
    const float decay_exc   = (float)wet_exp(-dt / (double)bio->tau_exc_ms);
    const float decay_inh   = (float)wet_exp(-dt / (double)bio->tau_inh_ms);
    const float decay_ahp   = (float)wet_exp(-dt / (double)bio->tau_ahp_ms);
    const float decay_thr   = (float)wet_exp(-dt / (double)bio->tau_thresh_ms);
    const float decay_pre   = (float)wet_exp(-dt / (double)bio->tau_stdp_plus_ms);
    const float decay_post  = (float)wet_exp(-dt / (double)bio->tau_stdp_minus_ms);
    const float decay_net_up = (float)wet_exp(-dt / 35.0);

    /* Capture active pulse & blanking status at start of tick */
    uint8_t pulse_active_this_tick[BIO_NUM_CHANNELS];
    uint8_t blank_this_tick[BIO_NUM_CHANNELS];
    for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        pulse_active_this_tick[ch] = bio->stim_pulses[ch].active ? 1U : 0U;
        blank_this_tick[ch] = (bio->stim_blanking_ticks[ch] > 0U) ? 1U : 0U;
        bio->blanking_active[ch] = blank_this_tick[ch];
    }

    /* 1. Advance active biphasic stimulation waveforms & compute tick charge (nC) */
    for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        bio_stim_pulse_t* p = &bio->stim_pulses[ch];
        float v_applied = 0.0f;

        if (p->active) {
            if (p->phase1_ticks_left > 0) {
                v_applied = p->phase1_amp_v;
                p->phase1_ticks_left--;
            } else if (p->interphase_ticks_left > 0) {
                v_applied = 0.0f;
                p->interphase_ticks_left--;
                /* Interphase Overpotential (E_mc): During zero-current interphase delay,
                 * I * Rs = 0, so measured electrode potential is purely the interfacial overpotential E_mc.
                 * Asymmetric Water-Window Evaluation (Audit Remediation):
                 * Water windows are chemically asymmetric (e.g. [-0.6 V, +0.8 V] for Pt, [-0.9 V, +0.6 V] for PEDOT).
                 * If E_mc violates either rail, extend amplifier blanking and flag Faradaic excursion. */
                float e_mc_v = bio->v_double_layer_v[ch];
                float v_low_window = bio->v_water_window_low_v < 0.0f ? bio->v_water_window_low_v : -0.6f;
                float v_high_window = bio->v_water_window_high_v > 0.0f ? bio->v_water_window_high_v : 0.8f;
                if ((e_mc_v < v_low_window || e_mc_v > v_high_window) && bio->stim_blanking_ticks[ch] < 50) {
                    bio->stim_blanking_ticks[ch] += 10;
                    blank_this_tick[ch] = 1U;
                    bio->blanking_active[ch] = 1U;
                }
            } else if (p->phase2_ticks_left > 0) {
                v_applied = p->phase2_amp_v;
                p->phase2_ticks_left--;
            }
            if (p->phase1_ticks_left == 0 && p->interphase_ticks_left == 0 && p->phase2_ticks_left == 0) {
                p->active = 0;
            }
        }

        bio->ext_stim_v[ch] = v_applied;
        /* I (uA) = V (V) / Z (kOhm) * 1000; Q (nC) = I (uA) * dt (ms) */
        float i_ua = (v_applied / bio->electrode_impedance_kohm) * 1000.0f;
        bio->tick_charge_nc[ch] = i_ua * dt_f;

        /* Randles Cell Integration: dV_dl/dt = (I - V_dl/Rct) / Cdl
         * Incorporates exponential Butler-Volmer Faradaic leakage when overpotential extends
         * beyond the safe reversible charge transfer regime (electrolysis runaway). */
        float c_dl_pf = bio->c_double_layer_pf[ch] > 0.0f ? bio->c_double_layer_pf[ch] : 26.45f;
        float r_ct_kohm = bio->r_charge_transfer_kohm > 0.0f ? bio->r_charge_transfer_kohm : 5000.0f;
        float tau_dl_ms = (r_ct_kohm * 1e3f) * (c_dl_pf * 1e-12f) * 1e3f; /* Rct * Cdl in ms */
        if (tau_dl_ms < 0.01f) tau_dl_ms = 0.01f;

        float v_dl_now = bio->v_double_layer_v[ch];
        float v_low_lim = bio->v_water_window_low_v < 0.0f ? bio->v_water_window_low_v : -0.6f;
        float v_high_lim = bio->v_water_window_high_v > 0.0f ? bio->v_water_window_high_v : 0.8f;
        if (v_dl_now > v_high_lim) {
            float excess_v = v_dl_now - v_high_lim;
            tau_dl_ms /= (1.0f + 10.0f * excess_v);
        } else if (v_dl_now < v_low_lim) {
            float excess_v = v_low_lim - v_dl_now;
            tau_dl_ms /= (1.0f + 10.0f * excess_v);
        }
        if (tau_dl_ms < 0.001f) tau_dl_ms = 0.001f;

        float decay_dl = (float)wet_exp(-dt / (double)tau_dl_ms);
        /* Injected dv = I * dt / Cdl; I in uA, dt in ms, Cdl in pF -> (uA * ms) / pF = (1e-6 * 1e-3) / 1e-12 = 1.0 V */
        float dv_dl = (i_ua * dt_f) / c_dl_pf;
        bio->v_double_layer_v[ch] = bio->v_double_layer_v[ch] * decay_dl + dv_dl;
    }

    /* 2. Decay synaptic conductances, AHP, dynamic thresholds, STDP traces & STP state */
    for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
        bio->g_exc_ns[i]   *= decay_exc;
        bio->g_inh_ns[i]   *= decay_inh;
        bio->g_ahp_ns[i]   *= decay_ahp;
        bio->v_thresh_mv[i] = bio->e_thresh_base_mv + (bio->v_thresh_mv[i] - bio->e_thresh_base_mv) * decay_thr;
        bio->trace_pre[i]  *= decay_pre;
        bio->trace_post[i] *= decay_post;
        bio->spikes_now[i]  = 0;

        /* Denormal / Subnormal Floating-Point Clamping to eliminate microcode exception traps */
        if (bio->g_exc_ns[i] < 1e-12f) bio->g_exc_ns[i] = 0.0f;
        if (bio->g_inh_ns[i] < 1e-12f) bio->g_inh_ns[i] = 0.0f;
        if (bio->g_ahp_ns[i] < 1e-12f) bio->g_ahp_ns[i] = 0.0f;
        if (bio->trace_pre[i] < 1e-12f) bio->trace_pre[i] = 0.0f;
        if (bio->trace_post[i] < 1e-12f) bio->trace_post[i] = 0.0f;
    }

    /* Spontaneous cortical Up-state network barrage (~1.2 Hz Poisson bursts, tau = 35 ms) */
    bio->g_net_up_ns *= decay_net_up;
    if (bio->g_net_up_ns < 1e-12f) bio->g_net_up_ns = 0.0f;
    if (bio->noise_enabled) {
        if (wet_rng_uniform(&bio->rng_state) < (0.0012 * dt)) {
            bio->g_net_up_ns += 16.0f + (float)wet_rng_uniform(&bio->rng_state) * 10.0f;
        }
    }

    /* Independent Poisson miniature spontaneous EPSPs (~2.5 Hz per neuron) */
    if (bio->noise_enabled) {
        for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
            if (wet_rng_uniform(&bio->rng_state) < (0.0025 * dt)) {
                bio->g_exc_ns[i] += 18.0f + (float)wet_rng_uniform(&bio->rng_state) * 8.0f;
            }
        }
    }

    /* Exact Exponential Euler relaxation of Tsodyks-Markram STP variables */
    for (int pre = 0; pre < BIO_NUM_NEURONS; ++pre) {
        for (int post = 0; post < BIO_NUM_NEURONS; ++post) {
            bio_synapse_t* syn = &bio->synapses[pre][post];
            if (!syn->exists) continue;
            float d_rec = (float)wet_exp(-dt / (double)syn->tau_rec_ms);
            float d_fac = (float)wet_exp(-dt / (double)syn->tau_fac_ms);
            syn->x_stp = 1.0f + (syn->x_stp - 1.0f) * d_rec;
            syn->u_stp = syn->U_base + (syn->u_stp - syn->U_base) * d_fac;
        }
    }

    /* 3. Integrate COBA-LIF membrane ODE via Exact Exponential Euler */
    const double dt_safe = (dt > 0.0) ? dt : 0.1;
    uint32_t refract_calc = (uint32_t)((double)BIO_ABS_REFRACT_MS / dt_safe + 0.5);
    if (refract_calc == 0U) refract_calc = 1U;
    if (refract_calc > 65535U) refract_calc = 65535U;
    const uint16_t abs_refract_ticks = (uint16_t)refract_calc;

    for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
        if (bio->refract_ticks[i] > 0) {
            bio->refract_ticks[i]--;
            bio->v_m_mv[i] = bio->e_reset_mv;
            continue;
        }

        /* Couple nearby electrode stimulation via volume conduction pickup matrix */
        float stim_v_eff = 0.0f;
        for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
            if (bio->ext_stim_v[ch] != 0.0f) {
                stim_v_eff += bio->pickup_matrix[ch][i] * bio->ext_stim_v[ch];
            }
        }
        /* Convert effective extracellular field (V) into depolarizing soma current (pA).
         * Cathodic extracellular field (stim_v_eff < 0) depolarizes the soma (Vm = Vi - Ve);
         * scale calibrated so 0.5-1.0 V drives firing. */
        float i_stim_pa = -stim_v_eff * 1500.0f;

        /* Subthreshold fluctuating cortical synaptic background current */
        float i_bg_pa = bio->noise_enabled
            ? (80.0f + (float)wet_rng_normal(&bio->rng_state) * 90.0f)
            : 0.0f;

        /* Total conductance (nS) */
        float g_exc_eff = bio->g_exc_ns[i] + bio->g_net_up_ns;
        float g_tot = bio->g_leak_ns + g_exc_eff + bio->g_inh_ns[i] + bio->g_ahp_ns[i];
        if (g_tot < 1e-3f) g_tot = bio->g_leak_ns;

        /* Steady-state target potential V_inf (mV): (nS * mV + pA) / nS = mV */
        float num = bio->g_leak_ns * bio->e_leak_mv
                  + g_exc_eff * bio->e_exc_mv
                  + bio->g_inh_ns[i] * bio->e_inh_mv
                  + bio->g_ahp_ns[i] * bio->e_k_mv
                  + i_stim_pa + i_bg_pa;
        float v_inf = num / g_tot;

        /* Exact Exponential Euler step: tau_eff (ms) = C_m (pF) / g_tot (nS) */
        float tau_eff_ms = bio->c_m_pf / g_tot;
        float decay_v = (float)wet_exp(-dt / (double)tau_eff_ms);
        float v_next = v_inf + (bio->v_m_mv[i] - v_inf) * decay_v;

        /* Numerical safety clamp */
        v_next = wet_clampf(v_next, -120.0f, 50.0f);

        if (v_next >= bio->v_thresh_mv[i]) {
            bio->spikes_now[i] = 1;
            bio->v_m_mv[i] = bio->e_reset_mv;
            bio->refract_ticks[i] = abs_refract_ticks;     /* 2.0 ms hard absolute refractory scaled by dt_ms */
            bio->v_thresh_mv[i] += 15.0f;                  /* +15 mV relative refractory jump */
            bio->g_ahp_ns[i]    += 2.0f;                   /* Slow AHP potassium adaptation */
        } else {
            bio->v_m_mv[i] = v_next;
        }
    }

    /* Suppress spikes on blanked channels BEFORE Step 4 STP/STDP propagation */
    for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        if (blank_this_tick[ch]) {
            bio->spikes_now[ch] = 0;
        }
    }

    /* 4. Propagate spikes through Tsodyks-Markram STP synapses & Online Pairwise STDP */
    for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
        if (!bio->spikes_now[i]) continue;

        /* Update pre-synaptic and post-synaptic STDP traces */
        bio->trace_pre[i]  += 1.0f;
        bio->trace_post[i] += 1.0f;

        /* A) Outgoing synapses (i -> post): STP transmission + LTD */
        for (int post = 0; post < BIO_NUM_NEURONS; ++post) {
            bio_synapse_t* syn = &bio->synapses[i][post];
            if (!syn->exists) continue;

            /* Tsodyks-Markram discrete spike update:
             * Release fraction is determined by current utilization u_stp;
             * then x_stp is depleted, and u_stp facilitates for subsequent spikes.
             * This eliminates the 50% first-spike double-counting defect. */
            float release = syn->u_stp * syn->x_stp;
            syn->x_stp = wet_clampf(syn->x_stp - release, 0.0f, 1.0f);
            syn->u_stp = wet_clampf(syn->u_stp + syn->U_base * (1.0f - syn->u_stp), 0.0f, 1.0f);

            float dg = syn->weight_ns * release;
            if (bio->is_excitatory[i]) {
                bio->g_exc_ns[post] += dg;
            } else {
                bio->g_inh_ns[post] += dg;
            }

            /* Online STDP LTD on plastic excitatory synapses (1.05x depression bias) */
            if (bio->is_excitatory[i] && bio->trace_post[post] > 1e-6f) {
                float dw = -bio->stdp_lr_scale * bio->stdp_a_minus * bio->trace_post[post];
                float old_w = syn->weight_ns;
                syn->weight_ns = wet_clampf(old_w + dw, BIO_W_MIN_NS, BIO_W_MAX_NS);
                bio->cumulative_weight_drift_ns += wet_fabsf(syn->weight_ns - old_w);
            }
        }

        /* B) Incoming synapses (pre -> i): Online STDP LTP on plastic excitatory synapses */
        for (int pre = 0; pre < BIO_NUM_NEURONS; ++pre) {
            if (!bio->is_excitatory[pre]) continue;
            bio_synapse_t* syn = &bio->synapses[pre][i];
            if (!syn->exists) continue;

            if (bio->trace_pre[pre] > 1e-6f) {
                float dw = bio->stdp_lr_scale * bio->stdp_a_plus * bio->trace_pre[pre];
                float old_w = syn->weight_ns;
                syn->weight_ns = wet_clampf(old_w + dw, BIO_W_MIN_NS, BIO_W_MAX_NS);
                bio->cumulative_weight_drift_ns += wet_fabsf(syn->weight_ns - old_w);
            }
        }
    }

    /* 5. Update 8x8 MEA Extracellular Voltages & 50.0 ms Sliding Spike History */
    uint16_t head = bio->spike_history_head;
    float total_rate_sum = 0.0f;
    const float window_s = (float)(BIO_SPIKE_HISTORY_LEN * bio->dt_ms) * 0.001f; /* 0.05 s */

    for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        /* Forward volume conduction LFP/spike pickup (mV -> V, resting baseline centered at 0 V) + applied stim voltage */
        float v_pick_mv = 0.0f;
        for (int i = 0; i < BIO_NUM_NEURONS; ++i) {
            float v_sig = bio->spikes_now[i] ? (30.0f - bio->e_leak_mv) : (bio->v_m_mv[i] - bio->e_leak_mv);
            v_pick_mv += bio->pickup_matrix[ch][i] * v_sig;
        }
        /* Report extracellular voltage in Volts (stim + attenuated biological LFP, zero baseline) */
        bio->mea_voltage_v[ch] = bio->ext_stim_v[ch] + (v_pick_mv * 1e-3f);

        /* Hardware Blanking Suppression: silence artifact and biological false-positives during post-stimulus discharge */
        if (!pulse_active_this_tick[ch] && blank_this_tick[ch]) {
            bio->mea_voltage_v[ch] = 0.0f;
            bio->spikes_now[ch] = 0;
        }

        /* Rolling 500-tick (50 ms) spike count */
        uint8_t old_spk = bio->spike_history[ch][head];
        uint8_t new_spk = bio->spikes_now[ch];
        bio->spike_history[ch][head] = new_spk;

        if (bio->spike_count_50ms[ch] >= old_spk) {
            bio->spike_count_50ms[ch] = (uint16_t)(bio->spike_count_50ms[ch] - old_spk + new_spk);
        } else {
            bio->spike_count_50ms[ch] = new_spk;
        }

        bio->channel_rate_hz[ch] = (float)bio->spike_count_50ms[ch] / window_s;
        total_rate_sum += bio->channel_rate_hz[ch];
    }

    bio->spike_history_head = (uint16_t)((head + 1U) % BIO_SPIKE_HISTORY_LEN);
    bio->population_rate_hz = total_rate_sum / (float)BIO_NUM_CHANNELS;

    /* Decrement blanking ticks at tick end so 1-tick (0.1 ms) blanking persists for a full tick */
    for (int ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        if (bio->stim_blanking_ticks[ch] > 0) {
            bio->stim_blanking_ticks[ch]--;
        }
    }

    bio->tick_count++;
}

uint32_t biophysics_get_spikes_window(const bio_state_t* bio, uint8_t channel, float window_ms) {
    if (!bio || channel >= BIO_NUM_CHANNELS) return 0U;

    uint32_t n_ticks = (window_ms > 0.0f) ? (uint32_t)(window_ms / (float)bio->dt_ms + 0.5f) : 1U;
    if (n_ticks == 0U) n_ticks = 1U;
    if (n_ticks > BIO_SPIKE_HISTORY_LEN) n_ticks = BIO_SPIKE_HISTORY_LEN;

    uint32_t count = 0U;
    int idx = (int)bio->spike_history_head - 1;
    for (uint32_t k = 0; k < n_ticks; ++k) {
        if (idx < 0) idx += BIO_SPIKE_HISTORY_LEN;
        count += bio->spike_history[channel][idx];
        idx--;
    }
    return count;
}

float biophysics_get_weight(const bio_state_t* bio, uint8_t pre, uint8_t post) {
    if (!bio || pre >= BIO_NUM_NEURONS || post >= BIO_NUM_NEURONS) return 0.0f;
    if (!bio->synapses[pre][post].exists) return 0.0f;
    return bio->synapses[pre][post].weight_ns;
}
