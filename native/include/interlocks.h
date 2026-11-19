#ifndef WET_INTERLOCKS_H
#define WET_INTERLOCKS_H

#include <stdint.h>
#include <stddef.h>
#include "wetvm_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* =========================================================================
 * WetLang Cycle-Accurate Biocybersecurity Hardware Watchdog & Interlocks
 * =========================================================================
 * 1. Water-Window Voltage Clamp: Hard clamp [-1.2 V, +1.2 V]
 * 2. Sliding Charge-Balance Ring Buffer:
 *    - 100-tick (10.0 ms at dt=0.1 ms) per-electrode circular buffer
 *    - Trip ERR_CHARGE_IMBALANCE if |Q_accum[ch]| >= 0.5 nC
 * 3. Epileptiform Runaway Firing Breaker:
 *    - Monitors sliding 50.0 ms firing rate per channel
 *    - Hyperactive channel: firing_rate > 150.0 Hz
 *    - Fraction threshold: > 35% of 64 channels (>= 23 channels)
 *    - Sustained duration: 500 consecutive ticks (50.0 ms)
 *    - Trip ERR_EPILEPTIFORM_RUNAWAY -> immediately zero DACs & lock VM
 * 4. Fail-Safe Interlock Lockout:
 *    - Once tripped, zeroes all stimulation voltages (0.0 V) and blocks
 *      further stimulation/execution until explicit hardware reset.
 * ========================================================================= */

#define INTERLOCK_NUM_CHANNELS          64
#define INTERLOCK_VOLTAGE_LIMIT_V       1.2f
#define INTERLOCK_CHARGE_WINDOW_TICKS   100     /* 10.0 ms at dt = 0.1 ms */
#define INTERLOCK_CHARGE_LIMIT_NC       0.5f    /* 0.5 nC per electrode */
#define INTERLOCK_EPILEPSY_RATE_HZ      150.0f  /* > 150 Hz */
#define INTERLOCK_EPILEPSY_MIN_CHANNELS 23      /* > 35% of 64 (22.4 -> 23) */
#define INTERLOCK_EPILEPSY_SUSTAIN_TICKS 500    /* 50.0 ms at dt = 0.1 ms */

/* Hardened Biocybersecurity Extensions (Audit Remediation) */
#define INTERLOCK_DC_DRIFT_LIMIT_NC     1.0f    /* 1.0 nC cumulative unrecovered DC charge */
#define INTERLOCK_BLEED_DECAY_PER_TICK  0.99999f/* tau = 10.0 s (100,000 ticks) */
#define INTERLOCK_CHARGE_DENSITY_LIMIT_NC 0.40f /* 0.40 nC max per single pulse phase (Shannon limit) */
#define INTERLOCK_FOCAL_RATE_HZ         150.0f  /* 150 Hz focal rate */
#define INTERLOCK_FOCAL_SUSTAIN_TICKS   2500    /* 250.0 ms sustained focal hyperactivity */
#define INTERLOCK_DUTY_CYCLE_LIMIT      0.05f   /* 5% max stimulation duty cycle */
#define INTERLOCK_DUTY_CYCLE_DECAY      0.9999f /* tau = 1.0 s (10,000 ticks) */
#define INTERLOCK_THERMAL_LIMIT_C       38.0f   /* 38.0 C max incubator / CMOS die temperature */
#define INTERLOCK_COMPLIANCE_LIMIT_V    7.0f    /* 7.0 V Intan RHS2116 compliance rail */

/* Phase 3 Electrochemical Water-Window & Material CIC Limits */
typedef enum {
    WET_ELEC_PLATINUM = 0,  /* 0.10 mC/cm^2 (water-window limit: 0.05..0.15 mC/cm^2) */
    WET_ELEC_TIN      = 1,  /* 0.90 mC/cm^2 (Titanium Nitride) */
    WET_ELEC_IROX     = 2,  /* 2.00 mC/cm^2 (Iridium Oxide / SIROF) */
    WET_ELEC_PEDOT    = 3,  /* 5.00 mC/cm^2 (Conductive Polymer PEDOT:PSS) */
    WET_ELEC_CUSTOM   = 4
} wet_electrode_material_t;

typedef enum {
    INTERLOCK_TRIP_NONE                = 0,
    INTERLOCK_TRIP_CHARGE_IMBALANCE    = 1,
    INTERLOCK_TRIP_EPILEPTIFORM_RUNAWAY= 2,
    INTERLOCK_TRIP_CAPABILITY_VIOLATION= 3,
    INTERLOCK_TRIP_VOLTAGE_OVERRIDE    = 4,
    INTERLOCK_TRIP_DC_DRIFT            = 5,
    INTERLOCK_TRIP_CHARGE_DENSITY      = 6,
    INTERLOCK_TRIP_FOCAL_EXCITOTOXICITY= 7,
    INTERLOCK_TRIP_DEAD_HEAD_PRESSURE  = 8,
    INTERLOCK_TRIP_THERMAL_LIMIT       = 9,
    INTERLOCK_TRIP_BUBBLE_DETECTED     = 10,
    INTERLOCK_TRIP_COMPLIANCE_RAILED   = 11
} interlock_trip_reason_t;

typedef struct {
    /* Fail-safe lockout state */
    uint8_t  locked;
    uint8_t  trip_reason;          /* interlock_trip_reason_t */
    uint8_t  tripped_channel;
    uint64_t trip_tick;
    float    trip_value;           /* Measured charge (nC) or hyperactive count */
    char     diagnostic[256];

    /* Water-window clamp statistics */
    uint64_t clamp_events;

    /* 10.0 ms (100-tick) sliding charge balance ring buffer per electrode */
    float    q_ring[INTERLOCK_NUM_CHANNELS][INTERLOCK_CHARGE_WINDOW_TICKS];
    float    q_accum[INTERLOCK_NUM_CHANNELS];
    uint16_t q_head;

    /* Long-horizon leaky DC charge integrator (10.0 s bleed time constant) */
    float    q_dc[INTERLOCK_NUM_CHANNELS];

    /* Phase 3: Unbounded Cumulative DC Charge Accumulator (no leaky decay; resets ONLY on active discharge) */
    float    cumulative_unbounded_dc_nc[INTERLOCK_NUM_CHANNELS];

    /* Phase 3: Electrode Material & Area Parameterization */
    uint8_t  electrode_material;   /* wet_electrode_material_t */
    float    electrode_area_um2;   /* e.g. 132.25 um^2 for MaxOne, or 5000 um^2 for macro */
    float    max_charge_per_phase_nc; /* Dynamic limit = CIC * Area */
    float    max_cumulative_dc_nc;    /* Dynamic persistent DC limit */

    /* Phase 3: Microfluidic Dead-Heading Pressure Interlock */
    uint8_t  dead_head_protection_enabled;
    uint8_t  pump_valve_mapping[8]; /* Maps pump ID to downstream pinch valve ID */

    /* 50.0 ms (500-tick) sustained epileptiform runaway counter */
    uint32_t hyperactive_consecutive_ticks;
    uint32_t last_hyperactive_channel_count;

    /* Per-channel focal hyperactivity & stimulation duty cycle monitors */
    uint32_t focal_hyperactive_ticks[INTERLOCK_NUM_CHANNELS];
    float    stim_duty_filter[INTERLOCK_NUM_CHANNELS];

    /* Authorized bytecode capabilities */
    uint16_t authorized_capabilities;
    uint32_t authorized_channels;

    /* Typed Channel Banks / Capabilities (Bug C-05 Remediation) */
    uint64_t reference_channels_mask;      /* Cannot be stimulated */
    uint64_t recording_only_channels_mask; /* Cannot be stimulated */
} interlock_state_t;

/* Initialize / reset watchdog state */
void interlocks_init(interlock_state_t* il);
void interlocks_set_capabilities(interlock_state_t* il, uint16_t caps, uint32_t channel_count);
void interlocks_set_channel_banks(interlock_state_t* il, uint64_t ref_mask, uint64_t rec_mask);

/* Phase 3 Electrochemical & Hardware Interlock API */
void interlocks_configure_electrode(interlock_state_t* il, uint8_t material, float area_um2);
void interlocks_active_discharge(interlock_state_t* il, uint8_t channel);
void interlocks_active_discharge_all(interlock_state_t* il);
void interlocks_enable_dead_head_protection(interlock_state_t* il, uint8_t enable);

/* Environmental & Compliance Safety Checks */
wet_status_t interlocks_check_thermal(interlock_state_t* il, uint64_t current_tick, float temp_c);
wet_status_t interlocks_check_bubble(interlock_state_t* il, uint64_t current_tick, uint8_t bubble_detected, uint8_t sensor_id);
wet_status_t interlocks_check_compliance(interlock_state_t* il, uint64_t current_tick, uint8_t channel, float v_elec_v);

/* Static authorization check for an opcode against loaded bytecode capabilities */
int interlocks_check_capability(const interlock_state_t* il, uint8_t opcode, float voltage_v, uint8_t channel);

/* Clamp requested stimulation voltage to [-1.2 V, +1.2 V] */
float interlocks_clamp_voltage(interlock_state_t* il, float requested_v);

/* Advance 10.0 ms charge ring buffer with this tick's per-channel injected charge (nC).
 * Returns WET_OK or WET_ERR_CHARGE_IMBALANCE (locking the watchdog on trip). */
wet_status_t interlocks_record_charge_tick(
    interlock_state_t* il,
    uint64_t current_tick,
    const float tick_charge_nc[INTERLOCK_NUM_CHANNELS]
);

/* Evaluate epileptiform runaway breaker using per-channel firing rates (Hz).
 * Returns WET_OK or WET_ERR_EPILEPTIFORM_RUNAWAY (locking the watchdog on trip). */
wet_status_t interlocks_check_epileptiform(
    interlock_state_t* il,
    uint64_t current_tick,
    const float channel_rates_hz[INTERLOCK_NUM_CHANNELS]
);

#ifdef __cplusplus
}
#endif

#endif /* WET_INTERLOCKS_H */
