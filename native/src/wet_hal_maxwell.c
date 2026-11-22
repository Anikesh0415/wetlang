#include "../include/wet_crt.h"
#include "../include/wet_hal_maxwell.h"

/* Forward declaration of vtable operations */
static wet_hal_status_t maxwell_op_init(wet_hal_driver_t* drv, void* config);
static wet_hal_status_t maxwell_op_shutdown(wet_hal_driver_t* drv);
static wet_hal_status_t maxwell_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason);
static wet_hal_status_t maxwell_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
static wet_hal_status_t maxwell_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
static wet_hal_status_t maxwell_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us);
static wet_hal_status_t maxwell_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count);
static wet_hal_status_t maxwell_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
static wet_hal_status_t maxwell_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel);

static const wet_hal_ops_t s_maxwell_ops = {
    .init              = maxwell_op_init,
    .shutdown          = maxwell_op_shutdown,
    .emergency_stop    = maxwell_op_emergency_stop,
    .step_tick         = maxwell_op_step_tick,
    .stim_voltage      = maxwell_op_stim_voltage,
    .stim_current      = maxwell_op_stim_current,
    .read_ephys        = maxwell_op_read_ephys,
    .measure_impedance = maxwell_op_measure_impedance,
    .active_discharge  = maxwell_op_active_discharge,
    .write_pump        = NULL,
    .dispense_volume   = NULL,
    .write_valve       = NULL,
    .read_flow         = NULL,
    .read_pressure     = NULL,
};

/* =========================================================================
 * MaxWell MaxOne HD-MEA Implementation
 * ========================================================================= */

wet_hal_driver_t* wet_hal_maxwell_create(wet_hal_mode_t mode) {
    wet_hal_driver_t* drv = (wet_hal_driver_t*)calloc(1, sizeof(wet_hal_driver_t));
    if (!drv) return NULL;

    maxwell_device_state_t* state = (maxwell_device_state_t*)calloc(1, sizeof(maxwell_device_state_t));
    if (!state) {
        free(drv);
        return NULL;
    }

    /* Initialize default 1-to-1 routing for first 1024 electrodes */
    for (uint32_t ch = 0; ch < MAXWELL_RECORDING_CHANNELS; ++ch) {
        state->routing_matrix[ch] = (uint16_t)ch;
        state->channel_active[ch] = 1;
        state->channel_voltages[ch] = -0.070f; /* -70 mV baseline */
        state->channel_spikes[ch] = 0;
    }
    state->sequence_state = MAXWELL_SEQ_IDLE;

    const char* name = "MaxWell_MaxOne";
    for (int i = 0; i < 31 && name[i]; ++i) drv->name[i] = name[i];
    drv->driver_type = WET_HAL_DRIVER_EPHYS;
    drv->mode = mode;
    drv->ops = &s_maxwell_ops;
    drv->context = state;

    return drv;
}

void wet_hal_maxwell_destroy(wet_hal_driver_t* drv) {
    if (!drv) return;
    if (drv->context) free(drv->context);
    free(drv);
}

wet_hal_status_t wet_hal_maxwell_route_channels(
    wet_hal_driver_t* drv,
    const uint16_t* electrode_indices,
    uint32_t count
) {
    if (!drv || !drv->context || !electrode_indices) return WET_HAL_ERR_NULL_PTR;
    if (count > MAXWELL_RECORDING_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;

    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;

    for (uint32_t ch = 0; ch < count; ++ch) {
        uint16_t elec_idx = electrode_indices[ch];
        if (elec_idx >= MAXWELL_TOTAL_ELECTRODES) {
            return WET_HAL_ERR_OUT_OF_BOUNDS;
        }
        state->routing_matrix[ch] = elec_idx;
        state->channel_active[ch] = 1;
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_maxwell_connect_stim(
    wet_hal_driver_t* drv,
    uint8_t stim_unit,
    uint16_t electrode_id
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (stim_unit >= MAXWELL_STIMULATION_UNITS || electrode_id >= MAXWELL_TOTAL_ELECTRODES) {
        return WET_HAL_ERR_OUT_OF_BOUNDS;
    }

    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    state->stim_units[stim_unit].connected_electrode = electrode_id;
    state->stim_units[stim_unit].is_connected = 1;
    return WET_HAL_OK;
}

void wet_hal_maxwell_sequence_clear(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    state->sequence_length = 0;
    state->sequence_playback_index = 0;
    state->sequence_state = MAXWELL_SEQ_IDLE;
}

wet_hal_status_t wet_hal_maxwell_sequence_append(
    wet_hal_driver_t* drv,
    uint32_t timestamp_us,
    uint8_t stim_unit,
    uint16_t electrode_id,
    float voltage_mv,
    uint16_t duration_us
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (stim_unit >= MAXWELL_STIMULATION_UNITS || electrode_id >= MAXWELL_TOTAL_ELECTRODES) {
        return WET_HAL_ERR_OUT_OF_BOUNDS;
    }

    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    if (state->sequence_length >= MAXWELL_MAX_SEQUENCE_STEPS) {
        return WET_HAL_ERR_BUFFER_FULL;
    }

    /* 1. Strict Voltage Limit Clamping: <= 1000 mV */
    float clamped_mv = voltage_mv;
    if (clamped_mv > MAXWELL_VOLTAGE_LIMIT_MV) {
        clamped_mv = MAXWELL_VOLTAGE_LIMIT_MV;
        state->voltage_clamp_events++;
    } else if (clamped_mv < -MAXWELL_VOLTAGE_LIMIT_MV) {
        clamped_mv = -MAXWELL_VOLTAGE_LIMIT_MV;
        state->voltage_clamp_events++;
    }

    /* 2. Platinum Charge Injection Capacity Protection:
     * Area = 132.25 um^2 = 1.3225e-6 cm^2.
     * Pt safe CIC = 0.10 mC/cm^2 = 0.10e-3 C/cm^2.
     * Q_max = 0.10e-3 * 1.3225e-6 C = 0.13225 nC.
     * Phase charge: Q = (V_clamped / Z_elec) * duration.
     * Assuming baseline Pt microelectrode impedance Z ~ 300 kOhm (0.3 MOhm):
     * I = V / Z = (clamped_mv / 300) uA.
     * Q (nC) = I (uA) * t (ms) = (clamped_mv / 300.0) * (duration_us / 1000.0). */
    float dur_ms = (float)duration_us / 1000.0f;
    float abs_mv = wet_fabsf(clamped_mv);
    float phase_charge_nc = (abs_mv / 300.0f) * dur_ms;

    if (phase_charge_nc > MAXWELL_MAX_PHASE_CHARGE_NC || state->fault_force_charge_violation) {
        state->charge_limit_violations++;
        return WET_HAL_ERR_INTERLOCK;
    }

    /* Convert clamped voltage to 335 DAC bits */
    int16_t dac_val = (int16_t)((clamped_mv / MAXWELL_VOLTAGE_LIMIT_MV) * (float)MAXWELL_MAX_DAC_BITS);

    maxwell_seq_step_t* step = &state->sequence_buffer[state->sequence_length++];
    step->timestamp_us = timestamp_us;
    step->stim_unit_id = stim_unit;
    step->electrode_id = electrode_id;
    step->dac_val = dac_val;
    step->phase_duration_us = duration_us;

    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_maxwell_sequence_arm(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    if (state->sequence_length == 0) return WET_HAL_ERR_IO;

    state->sequence_playback_index = 0;
    state->sequence_state = MAXWELL_SEQ_ARMED;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_maxwell_sequence_start(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    if (state->sequence_state != MAXWELL_SEQ_ARMED) return WET_HAL_ERR_IO;

    state->sequence_state = MAXWELL_SEQ_RUNNING;
    state->sequence_start_time_us = wet_hal_get_time_us();
    return WET_HAL_OK;
}

maxwell_seq_state_t wet_hal_maxwell_sequence_get_state(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return MAXWELL_SEQ_ERROR;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    return state->sequence_state;
}

wet_hal_status_t wet_hal_maxwell_stim_voltage(
    wet_hal_driver_t* drv,
    uint8_t stim_unit,
    uint16_t electrode_id,
    float voltage_mv,
    float phase1_ms,
    float phase2_ms
) {
    (void)phase2_ms;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (stim_unit >= MAXWELL_STIMULATION_UNITS || electrode_id >= MAXWELL_TOTAL_ELECTRODES) {
        return WET_HAL_ERR_OUT_OF_BOUNDS;
    }

    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;

    /* Clamp voltage to +/- 1000 mV */
    float clamped_mv = voltage_mv;
    if (clamped_mv > MAXWELL_VOLTAGE_LIMIT_MV) {
        clamped_mv = MAXWELL_VOLTAGE_LIMIT_MV;
        state->voltage_clamp_events++;
    } else if (clamped_mv < -MAXWELL_VOLTAGE_LIMIT_MV) {
        clamped_mv = -MAXWELL_VOLTAGE_LIMIT_MV;
        state->voltage_clamp_events++;
    }

    /* Check Pt charge injection capacity */
    float abs_mv = wet_fabsf(clamped_mv);
    float phase_charge_nc = (abs_mv / 300.0f) * phase1_ms;

    if (phase_charge_nc > MAXWELL_MAX_PHASE_CHARGE_NC || state->fault_force_charge_violation) {
        state->charge_limit_violations++;
        return WET_HAL_ERR_INTERLOCK;
    }

    int16_t dac_val = (int16_t)((clamped_mv / MAXWELL_VOLTAGE_LIMIT_MV) * (float)MAXWELL_MAX_DAC_BITS);
    state->stim_units[stim_unit].connected_electrode = electrode_id;
    state->stim_units[stim_unit].is_connected = 1;
    state->stim_units[stim_unit].current_dac_val = dac_val;
    state->stim_units[stim_unit].phase1_charge_nc = phase_charge_nc;

    return WET_HAL_OK;
}

void wet_hal_maxwell_inject_fault(
    wet_hal_driver_t* drv,
    uint8_t force_charge_violation,
    uint8_t drop_frames
) {
    if (!drv || !drv->context) return;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    state->fault_force_charge_violation = force_charge_violation;
    state->fault_bus_dropped_frame = drop_frames;
}

/* =========================================================================
 * Vtable Callbacks
 * ========================================================================= */

static wet_hal_status_t maxwell_op_init(wet_hal_driver_t* drv, void* config) {
    (void)config;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    drv->is_initialized = 1;
    drv->is_active = 1;
    return WET_HAL_OK;
}

static wet_hal_status_t maxwell_op_shutdown(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    for (int i = 0; i < MAXWELL_STIMULATION_UNITS; ++i) {
        state->stim_units[i].is_connected = 0;
        state->stim_units[i].current_dac_val = 0;
    }
    state->sequence_state = MAXWELL_SEQ_IDLE;
    drv->is_active = 0;
    return WET_HAL_OK;
}

static wet_hal_status_t maxwell_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
    (void)reason;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;

    /* Disconnect and zero all 32 stimulation units; clear sequence buffer */
    for (int i = 0; i < MAXWELL_STIMULATION_UNITS; ++i) {
        state->stim_units[i].current_dac_val = 0;
        state->stim_units[i].is_connected = 0;
    }
    state->sequence_state = MAXWELL_SEQ_IDLE;
    state->sequence_playback_index = 0;
    return WET_HAL_OK;
}

static wet_hal_status_t maxwell_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
    (void)current_tick;
    (void)dt_ms;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;

    if (state->sequence_state == MAXWELL_SEQ_RUNNING) {
        /* Advance sequence playback */
        if (state->sequence_playback_index < state->sequence_length) {
            state->sequence_playback_index++;
        }
        if (state->sequence_playback_index >= state->sequence_length) {
            state->sequence_state = MAXWELL_SEQ_DONE;
        }
    }
    return WET_HAL_OK;
}

static wet_hal_status_t maxwell_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms) {
    if (!drv) return WET_HAL_ERR_NULL_PTR;
    uint8_t stim_unit = (uint8_t)(channel % MAXWELL_STIMULATION_UNITS);
    float voltage_mv = voltage_v * 1000.0f;
    return wet_hal_maxwell_stim_voltage(drv, stim_unit, channel, voltage_mv, p1_ms, p2_ms);
}

static wet_hal_status_t maxwell_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us) {
    if (!drv) return WET_HAL_ERR_NULL_PTR;
    /* Approximate voltage from current: V = I * Z (with Z ~ 300 kOhm) */
    double current_amps = (double)current_pA * 1e-12;
    double voltage_v = current_amps * 300000.0;
    float dur_ms = (float)duration_us / 1000.0f;
    return maxwell_op_stim_voltage(drv, channel, (float)voltage_v, dur_ms, dur_ms);
}

static wet_hal_status_t maxwell_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count) {
    if (!drv || !voltages_out || !spikes_out) return WET_HAL_ERR_NULL_PTR;
    uint32_t count = channel_count < MAXWELL_RECORDING_CHANNELS ? channel_count : MAXWELL_RECORDING_CHANNELS;
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;

    for (uint32_t i = 0; i < count; ++i) {
        voltages_out[i] = state->channel_voltages[i];
        spikes_out[i] = state->channel_spikes[i];
    }
    return WET_HAL_OK;
}

static wet_hal_status_t maxwell_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad) {
    (void)channel;
    (void)freq_hz;
    if (!drv || !out_mag_ohms || !out_phase_rad) return WET_HAL_ERR_NULL_PTR;
    *out_mag_ohms = 300000.0f; /* 300 kOhm typical for 132.25 um^2 Pt */
    *out_phase_rad = -0.785f;
    return WET_HAL_OK;
}

static wet_hal_status_t maxwell_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    uint8_t stim_unit = (uint8_t)(channel % MAXWELL_STIMULATION_UNITS);
    maxwell_device_state_t* state = (maxwell_device_state_t*)drv->context;
    state->stim_units[stim_unit].current_dac_val = 0;
    state->stim_units[stim_unit].phase1_charge_nc = 0.0f;
    state->stim_units[stim_unit].phase2_charge_nc = 0.0f;
    return WET_HAL_OK;
}
