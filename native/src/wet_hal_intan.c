#include "../include/wet_crt.h"
#include "../include/wet_hal_intan.h"

/* Forward declaration of vtable operations */
static wet_hal_status_t intan_op_init(wet_hal_driver_t* drv, void* config);
static wet_hal_status_t intan_op_shutdown(wet_hal_driver_t* drv);
static wet_hal_status_t intan_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason);
static wet_hal_status_t intan_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
static wet_hal_status_t intan_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
static wet_hal_status_t intan_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us);
static wet_hal_status_t intan_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count);
static wet_hal_status_t intan_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
static wet_hal_status_t intan_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel);

static const wet_hal_ops_t s_intan_ops = {
    .init              = intan_op_init,
    .shutdown          = intan_op_shutdown,
    .emergency_stop    = intan_op_emergency_stop,
    .step_tick         = intan_op_step_tick,
    .stim_voltage      = intan_op_stim_voltage,
    .stim_current      = intan_op_stim_current,
    .read_ephys        = intan_op_read_ephys,
    .measure_impedance = intan_op_measure_impedance,
    .active_discharge  = intan_op_active_discharge,
    .write_pump        = NULL,
    .dispense_volume   = NULL,
    .write_valve       = NULL,
    .read_flow         = NULL,
    .read_pressure     = NULL,
};

/* =========================================================================
 * Intan RHS2116 Protocol Implementation
 * ========================================================================= */

uint32_t wet_hal_intan_encode_cmd(const intan_spi_command_t* cmd) {
    if (!cmd) return 0;
    uint32_t word = 0;

    switch (cmd->opcode) {
        case INTAN_CMD_CONVERT:
            word = ((uint32_t)INTAN_CMD_CONVERT << 24)
                 | ((uint32_t)(cmd->flag_m ? 1 : 0) << 23)
                 | (((uint32_t)cmd->channel & 0x0FU) << 16);
            break;

        case INTAN_CMD_WRITE:
            word = ((uint32_t)INTAN_CMD_WRITE << 24)
                 | ((uint32_t)(cmd->flag_u ? 1 : 0) << 22)
                 | (((uint32_t)cmd->reg & 0x3FU) << 16)
                 | ((uint32_t)cmd->data & 0xFFFFU);
            break;

        case INTAN_CMD_READ:
            word = ((uint32_t)INTAN_CMD_READ << 24)
                 | ((uint32_t)(cmd->flag_m ? 1 : 0) << 23)
                 | (((uint32_t)cmd->reg & 0x3FU) << 16);
            break;

        default:
            word = 0;
            break;
    }
    return word;
}

void wet_hal_intan_decode_cmd(uint32_t word, intan_spi_command_t* cmd) {
    if (!cmd) return;
    memset(cmd, 0, sizeof(intan_spi_command_t));

    uint8_t op_prefix = (uint8_t)((word >> 24) & 0xC0U);
    cmd->opcode = op_prefix;

    if (op_prefix == INTAN_CMD_CONVERT) {
        cmd->flag_m = (uint8_t)((word >> 23) & 1U);
        cmd->channel = (uint8_t)((word >> 16) & 0x0FU);
    } else if (op_prefix == INTAN_CMD_WRITE) {
        cmd->flag_u = (uint8_t)((word >> 22) & 1U);
        cmd->reg = (uint8_t)((word >> 16) & 0x3FU);
        cmd->data = (uint16_t)(word & 0xFFFFU);
    } else if (op_prefix == INTAN_CMD_READ) {
        cmd->flag_m = (uint8_t)((word >> 23) & 1U);
        cmd->reg = (uint8_t)((word >> 16) & 0x3FU);
    }
}

uint32_t wet_hal_intan_spi_transfer(wet_hal_driver_t* drv, uint32_t mosi_word) {
    if (!drv || !drv->context) return 0xFFFFFFFFU;
    intan_device_state_t* state = (intan_device_state_t*)drv->context;

    state->transaction_count++;
    if (state->fault_bus_timeout) {
        return 0xFFFFFFFFU; /* Bus floating / timed out */
    }

    /* Pipelined MISO delay: shift register (2 command words pipeline) */
    uint32_t miso_out = state->rx_pipeline[0];
    state->rx_pipeline[0] = state->rx_pipeline[1];

    /* Decode incoming MOSI command to generate corresponding future response */
    intan_spi_command_t cmd;
    wet_hal_intan_decode_cmd(mosi_word, &cmd);

    uint32_t response_val = 0;

    if (cmd.flag_m) {
        state->compliance_rail_mask = 0; /* M flag clears compliance rail */
    }

    if (cmd.opcode == INTAN_CMD_CONVERT) {
        /* Convert channel analog potential: 16-bit ADC count */
        uint8_t ch = cmd.channel;
        if (ch < INTAN_RHS2116_NUM_CHANNELS) {
            /* Simulated reading: baseline resting potential + impedance */
            int16_t adc_val = (int16_t)(-1400); /* ~ -70 mV baseline */
            response_val = ((uint32_t)ch << 16) | ((uint16_t)adc_val);
        }
    } else if (cmd.opcode == INTAN_CMD_READ) {
        uint8_t reg = cmd.reg;
        if (reg < 64) {
            response_val = ((uint32_t)reg << 16) | state->registers[reg];
        }
    } else if (cmd.opcode == INTAN_CMD_WRITE) {
        uint8_t reg = cmd.reg;
        if (reg < 64) {
            state->registers[reg] = cmd.data;
            response_val = ((uint32_t)reg << 16) | cmd.data;
        }
    }

    /* Inject SPI bit error if requested */
    if (state->fault_spi_crc_error) {
        response_val ^= 0x00010000U;
    }

    state->rx_pipeline[1] = response_val;
    return miso_out;
}

wet_hal_driver_t* wet_hal_intan_create(wet_hal_mode_t mode) {
    wet_hal_driver_t* drv = (wet_hal_driver_t*)calloc(1, sizeof(wet_hal_driver_t));
    if (!drv) return NULL;

    intan_device_state_t* state = (intan_device_state_t*)calloc(1, sizeof(intan_device_state_t));
    if (!state) {
        free(drv);
        return NULL;
    }

    /* Initialize default state */
    for (int i = 0; i < INTAN_RHS2116_NUM_CHANNELS; ++i) {
        state->channels[i].impedance_ohms = 150000.0f; /* 150 kOhm typical */
        state->channels[i].impedance_phase_rad = -0.785f; /* -45 deg capacitive */
        state->channels[i].range = INTAN_RANGE_1X;
    }
    state->zcheck_freq_hz = 1000.0f;
    state->zcheck_probe_current_pA = 100000.0f; /* 100 nA */

    /* Copy name */
    const char* name = "Intan_RHS2116";
    for (int i = 0; i < 31 && name[i]; ++i) drv->name[i] = name[i];
    drv->driver_type = WET_HAL_DRIVER_EPHYS;
    drv->mode = mode;
    drv->ops = &s_intan_ops;
    drv->context = state;

    return drv;
}

void wet_hal_intan_destroy(wet_hal_driver_t* drv) {
    if (!drv) return;
    if (drv->context) free(drv->context);
    free(drv);
}

wet_hal_status_t wet_hal_intan_set_stim_current(
    wet_hal_driver_t* drv,
    uint8_t channel,
    int32_t current_pA,
    uint32_t duration_us
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;

    intan_device_state_t* state = (intan_device_state_t*)drv->context;

    /* Current limit check: 10 nA (10,000 pA) to 2.55 mA (2,550,000,000 pA) */
    int64_t abs_pA = current_pA < 0 ? -(int64_t)current_pA : (int64_t)current_pA;
    if (abs_pA > 0 && abs_pA < 10000) {
        abs_pA = 10000; /* Minimum 10 nA step */
    }
    if (abs_pA > 2550000000LL) {
        abs_pA = 2550000000LL; /* Clamp to 2.55 mA */
    }

    /* Select current range */
    intan_current_range_t range;
    uint8_t dac_val;

    if (abs_pA <= 2550000) {
        range = INTAN_RANGE_1X; /* 10 nA step */
        dac_val = (uint8_t)(abs_pA / 10000);
    } else if (abs_pA <= 25500000) {
        range = INTAN_RANGE_10X; /* 100 nA step */
        dac_val = (uint8_t)(abs_pA / 100000);
    } else {
        range = INTAN_RANGE_100X; /* 10 uA step */
        dac_val = (uint8_t)(abs_pA / 10000000);
    }

    state->channels[channel].range = range;
    state->channels[channel].dac_val_p1 = dac_val;
    state->channels[channel].current_pA = current_pA;
    state->channels[channel].duration_us = duration_us;
    state->channels[channel].enabled = (abs_pA > 0) ? 1 : 0;

    /* Compliance Rail Detection: V = I * Z */
    double current_amps = (double)current_pA * 1e-12;
    double compliance_v = wet_fabs(current_amps * (double)state->channels[channel].impedance_ohms);

    if (compliance_v >= (double)INTAN_COMPLIANCE_RAIL_VOLT || state->fault_force_compliance_rail) {
        state->compliance_rail_mask |= (1U << channel);
        state->total_compliance_trips++;
        return WET_HAL_ERR_COMPLIANCE_RAILED;
    }

    /* Encode and perform SPI WRITE with U update flag */
    intan_spi_command_t cmd;
    cmd.opcode = INTAN_CMD_WRITE;
    cmd.flag_u = 1; /* Synchronously latch DAC update */
    cmd.reg = (uint8_t)((current_pA < 0 ? 48 : 32) + channel); /* Positive DACs (32..47) or Negative DACs (48..63) */
    cmd.data = ((uint16_t)range << 8) | (uint16_t)dac_val;
    uint32_t word = wet_hal_intan_encode_cmd(&cmd);
    wet_hal_intan_spi_transfer(drv, word);

    return WET_HAL_OK;
}

uint16_t wet_hal_intan_get_compliance_status(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return 0;
    intan_device_state_t* state = (intan_device_state_t*)drv->context;
    return state->compliance_rail_mask;
}

void wet_hal_intan_clear_compliance(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return;
    intan_device_state_t* state = (intan_device_state_t*)drv->context;
    state->compliance_rail_mask = 0;

    /* Execute CONVERT with M flag */
    intan_spi_command_t cmd;
    cmd.opcode = INTAN_CMD_CONVERT;
    cmd.flag_m = 1;
    cmd.channel = 0;
    uint32_t word = wet_hal_intan_encode_cmd(&cmd);
    wet_hal_intan_spi_transfer(drv, word);
}

wet_hal_status_t wet_hal_intan_measure_impedance(
    wet_hal_driver_t* drv,
    uint8_t channel,
    float freq_hz,
    float* out_mag_ohms,
    float* out_phase_rad
) {
    if (!drv || !drv->context || !out_mag_ohms || !out_phase_rad) return WET_HAL_ERR_NULL_PTR;
    if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;

    intan_device_state_t* state = (intan_device_state_t*)drv->context;

    /* 1 kHz in-situ impedance check */
    state->zcheck_freq_hz = freq_hz > 0.0f ? freq_hz : 1000.0f;
    *out_mag_ohms = state->channels[channel].impedance_ohms;
    *out_phase_rad = state->channels[channel].impedance_phase_rad;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_intan_set_charge_recovery(
    wet_hal_driver_t* drv,
    uint8_t channel,
    uint8_t enable
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;

    intan_device_state_t* state = (intan_device_state_t*)drv->context;
    state->channels[channel].charge_recovery_on = enable ? 1 : 0;

    /* Program RHS2116 current-limited charge recovery DAC (Registers 36-37)
     * avoids instantaneous capacitive dump by limiting recovery current to <= 10 uA */
    if (enable) {
        state->registers[36] = (uint16_t)0x0080U; /* Current-limited recovery mode */
        state->registers[37] = (uint16_t)0x000AU; /* Target 10 uA discharge current limit */
    } else {
        state->registers[36] = 0;
        state->registers[37] = 0;
    }
    return WET_HAL_OK;
}

void wet_hal_intan_inject_fault(
    wet_hal_driver_t* drv,
    uint8_t force_rail,
    uint8_t spi_error,
    uint8_t bus_timeout
) {
    if (!drv || !drv->context) return;
    intan_device_state_t* state = (intan_device_state_t*)drv->context;
    state->fault_force_compliance_rail = force_rail;
    state->fault_spi_crc_error = spi_error;
    state->fault_bus_timeout = bus_timeout;
}

/* =========================================================================
 * Vtable Callbacks
 * ========================================================================= */

static wet_hal_status_t intan_op_init(wet_hal_driver_t* drv, void* config) {
    (void)config;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    drv->is_initialized = 1;
    drv->is_active = 1;
    return WET_HAL_OK;
}

static wet_hal_status_t intan_op_shutdown(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    intan_device_state_t* state = (intan_device_state_t*)drv->context;
    for (int i = 0; i < INTAN_RHS2116_NUM_CHANNELS; ++i) {
        state->channels[i].enabled = 0;
        state->channels[i].current_pA = 0;
        state->channels[i].charge_recovery_on = 1;
    }
    drv->is_active = 0;
    return WET_HAL_OK;
}

static wet_hal_status_t intan_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
    (void)reason;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    intan_device_state_t* state = (intan_device_state_t*)drv->context;

    /* Zero all DAC amplitudes immediately and activate charge recovery switches */
    for (int i = 0; i < INTAN_RHS2116_NUM_CHANNELS; ++i) {
        state->channels[i].dac_val_p1 = 0;
        state->channels[i].dac_val_p2 = 0;
        state->channels[i].current_pA = 0;
        state->channels[i].enabled = 0;
        state->channels[i].charge_recovery_on = 1;
    }
    return WET_HAL_OK;
}

static wet_hal_status_t intan_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
    (void)current_tick;
    (void)dt_ms;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    return WET_HAL_OK;
}

static wet_hal_status_t intan_op_stim_voltage(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;

    intan_device_state_t* state = (intan_device_state_t*)drv->context;
    /* Convert voltage to equivalent current using channel impedance */
    float z_ohms = state->channels[channel].impedance_ohms;
    if (z_ohms <= 0.0f) z_ohms = 150000.0f;
    double current_amps = (double)voltage_v / (double)z_ohms;
    int32_t current_pA = (int32_t)(current_amps * 1e12);

    uint32_t duration_us = (uint32_t)((p1_ms + p2_ms) * 1000.0);
    if (duration_us == 0) duration_us = 1000;

    return wet_hal_intan_set_stim_current(drv, (uint8_t)channel, current_pA, duration_us);
}

static wet_hal_status_t intan_op_stim_current(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us) {
    if (!drv) return WET_HAL_ERR_NULL_PTR;
    if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
    return wet_hal_intan_set_stim_current(drv, (uint8_t)channel, current_pA, duration_us);
}

static wet_hal_status_t intan_op_read_ephys(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count) {
    if (!drv || !voltages_out || !spikes_out) return WET_HAL_ERR_NULL_PTR;
    uint32_t count = channel_count < INTAN_RHS2116_NUM_CHANNELS ? channel_count : INTAN_RHS2116_NUM_CHANNELS;
    for (uint32_t i = 0; i < count; ++i) {
        voltages_out[i] = -0.070f; /* -70 mV */
        spikes_out[i] = 0;
    }
    return WET_HAL_OK;
}

static wet_hal_status_t intan_op_measure_impedance(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad) {
    if (!drv) return WET_HAL_ERR_NULL_PTR;
    if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
    return wet_hal_intan_measure_impedance(drv, (uint8_t)channel, freq_hz, out_mag_ohms, out_phase_rad);
}

static wet_hal_status_t intan_op_active_discharge(wet_hal_driver_t* drv, uint16_t channel) {
    if (!drv) return WET_HAL_ERR_NULL_PTR;
    if (channel >= INTAN_RHS2116_NUM_CHANNELS) return WET_HAL_ERR_OUT_OF_BOUNDS;
    return wet_hal_intan_set_charge_recovery(drv, (uint8_t)channel, 1);
}
