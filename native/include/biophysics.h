#ifndef WET_BIOPHYSICS_H
#define WET_BIOPHYSICS_H

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/* =========================================================================
 * WetLang In-Silico Biophysical Digital Twin (64-Neuron 8x8 MEA)
 * =========================================================================
 * - Fixed integration timestep: dt = 0.1 ms
 * - Conductance-Based Leaky Integrate-and-Fire (COBA-LIF) + slow AHP
 * - Exact Exponential Euler numerical integration
 * - Absolute refractory period: 2.0 ms (20 ticks -> max 500 Hz single neuron)
 * - Relative refractory period: dynamic threshold (+15 mV, tau = 10 ms)
 * - Tsodyks-Markram Short-Term Plasticity (4 classes: E->E, E->I, I->E, I->I)
 * - Online Pairwise Trace STDP (1.05x LTD bias, [0, 40 nS], Dale's principle)
 * - 8x8 MEA Volume Conduction (200 um pitch) forward pickup & cross-talk
 * ========================================================================= */

#define BIO_NUM_NEURONS      64
#define BIO_NUM_CHANNELS     64
#define BIO_GRID_ROWS        8
#define BIO_GRID_COLS        8
#define BIO_PITCH_UM         200.0f

/* Absolute refractory period: 2.0 ms at dt = 0.1 ms -> 20 ticks */
#define BIO_ABS_REFRACT_MS   2.0f
#define BIO_ABS_REFRACT_TICKS 20

/* Synaptic weight hard bounds (nS) */
#define BIO_W_MIN_NS         0.0f
#define BIO_W_MAX_NS         40.0f

/* Spike history ring buffer per channel for sliding-window readout (500 ticks = 50.0 ms) */
#define BIO_SPIKE_HISTORY_LEN 500

/* Synapse Class Enumeration (Tsodyks-Markram) */
typedef enum {
    SYN_CLASS_EE = 0, /* Excitatory -> Excitatory (Depressing) */
    SYN_CLASS_EI = 1, /* Excitatory -> Inhibitory (Facilitating) */
    SYN_CLASS_IE = 2, /* Inhibitory -> Excitatory (Depressing) */
    SYN_CLASS_II = 3  /* Inhibitory -> Inhibitory (Moderately depressing) */
} bio_syn_class_t;

/* Directed Synapse Structure */
typedef struct {
    uint8_t  exists;      /* 1 if connected, 0 otherwise */
    uint8_t  syn_class;   /* bio_syn_class_t */
    float    weight_ns;   /* Conductance weight in [0.0, 40.0] nS (always >= 0; sign via E_rev) */
    /* Tsodyks-Markram STP state */
    float    u_stp;       /* Utilization of synaptic efficacy */
    float    x_stp;       /* Fraction of available vesicles */
    float    U_base;      /* Baseline release probability */
    float    tau_rec_ms;  /* Recovery time constant (ms) */
    float    tau_fac_ms;  /* Facilitation time constant (ms) */
} bio_synapse_t;

/* Active Biphasic Stimulation Pulse Schedule per Channel */
typedef struct {
    uint8_t  active;
    float    voltage_v;         /* Clamped amplitude (V) */
    uint32_t phase1_ticks_left; /* Cathodic / Phase 1 remaining ticks */
    uint32_t interphase_ticks_left; /* Interphase gap (0 V) remaining ticks */
    uint32_t phase2_ticks_left; /* Anodic / Phase 2 remaining ticks */
    float    phase1_amp_v;      /* Phase 1 voltage */
    float    phase2_amp_v;      /* Phase 2 counter-balancing voltage */
} bio_stim_pulse_t;

/* Complete Biophysical State */
typedef struct {
    double   dt_ms;
    uint64_t tick_count;
    uint64_t rng_state;

    /* Neuron type: 1 = Excitatory (80%, 51 neurons), 0 = Inhibitory (20%, 13 neurons) */
    uint8_t  is_excitatory[BIO_NUM_NEURONS];

    /* 3D coordinates in micrometers (x, y on 8x8 grid, z offset) */
    float    pos_x_um[BIO_NUM_NEURONS];
    float    pos_y_um[BIO_NUM_NEURONS];
    float    pos_z_um[BIO_NUM_NEURONS];

    /* COBA-LIF state variables */
    float    v_m_mv[BIO_NUM_NEURONS];         /* Membrane potential (mV), resting -70 mV */
    float    v_thresh_mv[BIO_NUM_NEURONS];    /* Dynamic firing threshold (mV), base -50 mV */
    float    g_exc_ns[BIO_NUM_NEURONS];       /* Excitatory synaptic conductance (nS) */
    float    g_inh_ns[BIO_NUM_NEURONS];       /* Inhibitory synaptic conductance (nS) */
    float    g_ahp_ns[BIO_NUM_NEURONS];       /* Slow after-hyperpolarization conductance (nS) */
    uint16_t refract_ticks[BIO_NUM_NEURONS];  /* Remaining absolute refractory ticks */

    /* STDP Eligibility Traces per Neuron */
    float    trace_pre[BIO_NUM_NEURONS];      /* Pre-synaptic trace (tau_plus = 20 ms) */
    float    trace_post[BIO_NUM_NEURONS];     /* Post-synaptic trace (tau_minus = 20 ms) */
    float    stdp_lr_scale;                   /* Dynamic STDP learning rate multiplier */
    float    cumulative_weight_drift_ns;      /* Cumulative |dw| across all plastic synapses */

    /* Dense 64x64 Synaptic Matrix */
    bio_synapse_t synapses[BIO_NUM_NEURONS][BIO_NUM_NEURONS];

    /* 8x8 MEA Volume Conduction Forward Matrix (channel <- neuron) */
    float    pickup_matrix[BIO_NUM_CHANNELS][BIO_NUM_NEURONS];

    /* Active stimulation pulses & instantaneous electrode voltages */
    bio_stim_pulse_t stim_pulses[BIO_NUM_CHANNELS];
    float    ext_stim_v[BIO_NUM_CHANNELS];       /* Applied electrode voltage this tick (V) */
    float    mea_voltage_v[BIO_NUM_CHANNELS];    /* Extracellular pickup + stim potential (V) */
    float    tick_charge_nc[BIO_NUM_CHANNELS];   /* Charge injected this tick (nC) */

    /* Spike outputs and rolling 50.0 ms history ring buffer */
    uint8_t  spikes_now[BIO_NUM_NEURONS];
    uint8_t  spike_history[BIO_NUM_CHANNELS][BIO_SPIKE_HISTORY_LEN];
    uint16_t spike_history_head;
    uint16_t spike_count_50ms[BIO_NUM_CHANNELS]; /* Running count over last 500 ticks */
    float    channel_rate_hz[BIO_NUM_CHANNELS];
    float    population_rate_hz;

    /* Biophysical constants */
    float    c_m_pf;          /* Membrane capacitance (200 pF) */
    float    g_leak_ns;       /* Leak conductance (10 nS -> tau_m = 20 ms) */
    float    e_leak_mv;       /* Leak reversal (-70 mV) */
    float    e_reset_mv;      /* Reset potential (-75 mV) */
    float    e_thresh_base_mv;/* Base spike threshold (-50 mV) */
    float    e_exc_mv;        /* Excitatory reversal (0 mV) */
    float    e_inh_mv;        /* Inhibitory reversal (-80 mV) */
    float    e_k_mv;          /* Potassium / AHP reversal (-90 mV) */
    float    tau_exc_ms;      /* AMPA decay (5.0 ms) */
    float    tau_inh_ms;      /* GABA_A decay (10.0 ms) */
    float    tau_ahp_ms;      /* Slow AHP decay (80.0 ms) */
    float    tau_thresh_ms;   /* Dynamic threshold decay (10.0 ms) */
    float    tau_stdp_plus_ms;/* STDP LTP window (20.0 ms) */
    float    tau_stdp_minus_ms;/* STDP LTD window (20.0 ms) */
    float    stdp_a_plus;     /* LTP amplitude (0.20 nS) */
    float    stdp_a_minus;    /* LTD amplitude (0.21 nS = 1.05x bias) */
    float    electrode_impedance_kohm; /* Electrode-electrolyte impedance (50 kOhm) */
    uint16_t stim_blanking_ticks[BIO_NUM_CHANNELS]; /* Post-stimulus amplifier artifact blanking ticks */
    uint16_t default_blanking_ticks; /* Configurable baseline blanking duration in ticks (e.g. 20 = 2.0 ms) */
    uint8_t  spatial_blanking_enabled; /* 1 = propagate attenuated blanking to adjacent MEA channels */

    /* Randles Equivalent Circuit Interface Model (Electrode-Electrolyte Interface) */
    float    r_solution_kohm;        /* Solution bulk resistance Rs (e.g. 2.0 kOhm) */
    float    r_charge_transfer_kohm; /* Faradaic charge transfer resistance Rct (e.g. 5000.0 kOhm = 5 MOhm) */
    float    c_double_layer_pf[BIO_NUM_CHANNELS];  /* Helmholtz double-layer capacitance Cdl */
    float    v_double_layer_v[BIO_NUM_CHANNELS];   /* Instantaneous polarization voltage Vdl(t) */
    float    last_stim_current_ua[BIO_NUM_CHANNELS]; /* Last injected constant current */
    float    max_compliance_voltage_v; /* Maximum ASIC compliance voltage (e.g. 7.0 V) */
} bio_state_t;

/* Lifecycle & Simulation Functions */
void biophysics_init(bio_state_t* bio, double dt_ms, uint64_t seed);
void biophysics_reset(bio_state_t* bio);

/* Schedule a biphasic stimulation pulse on a channel (already clamped by interlocks) */
void biophysics_schedule_stim(
    bio_state_t* bio,
    uint8_t channel,
    float clamped_voltage_v,
    float phase1_ms,
    float phase2_ms
);

void biophysics_schedule_stim_ext(
    bio_state_t* bio,
    uint8_t channel,
    float clamped_voltage_v,
    float phase1_ms,
    float phase2_ms,
    float interphase_ms
);

/* Schedule a constant-current stimulation pulse on a channel (Randles interface model) */
void biophysics_schedule_stim_current(
    bio_state_t* bio,
    uint8_t channel,
    float current_ua,
    float phase1_ms,
    float phase2_ms,
    float interphase_ms
);

/* Configure post-stimulus blanking window in milliseconds */
void biophysics_set_blanking_window(bio_state_t* bio, float blanking_ms, uint8_t enable_spatial);

/* Query instantaneous Randles polarization and total electrode potential */
void biophysics_get_randles_state(
    const bio_state_t* bio,
    uint8_t channel,
    float* out_v_dl_v,
    float* out_v_elec_v
);

/* Direct instantaneous voltage override (used for fail-safe zeroing or external injection) */
void biophysics_zero_all_stim(bio_state_t* bio);

/* Modulate STDP weight directly (bounded within [0, 40 nS], respecting Dale's principle) */
void biophysics_modulate_stdp(bio_state_t* bio, uint8_t pre, uint8_t post, float delta_w_ns);

/* Advance entire 64-neuron network by 1 fixed timestep (dt = 0.1 ms) */
void biophysics_step_tick(bio_state_t* bio);

/* Query spike count on a channel over a sliding window (up to 50.0 ms) */
uint32_t biophysics_get_spikes_window(const bio_state_t* bio, uint8_t channel, float window_ms);

/* Query synaptic weight between pre and post neurons */
float biophysics_get_weight(const bio_state_t* bio, uint8_t pre, uint8_t post);

#ifdef __cplusplus
}
#endif

#endif /* WET_BIOPHYSICS_H */
