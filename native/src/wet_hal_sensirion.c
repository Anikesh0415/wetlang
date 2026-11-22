#include "../include/wet_crt.h"
#include "../include/wet_hal_sensirion.h"

/* Forward declaration of vtable operations */
static wet_hal_status_t sensirion_op_init(wet_hal_driver_t* drv, void* config);
static wet_hal_status_t sensirion_op_shutdown(wet_hal_driver_t* drv);
static wet_hal_status_t sensirion_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason);
static wet_hal_status_t sensirion_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
static wet_hal_status_t sensirion_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min);

static const wet_hal_ops_t s_sensirion_ops = {
    .init              = sensirion_op_init,
    .shutdown          = sensirion_op_shutdown,
    .emergency_stop    = sensirion_op_emergency_stop,
    .step_tick         = sensirion_op_step_tick,
    .stim_voltage      = NULL,
    .stim_current      = NULL,
    .read_ephys        = NULL,
    .measure_impedance = NULL,
    .active_discharge  = NULL,
    .write_pump        = NULL,
    .dispense_volume   = NULL,
    .write_valve       = NULL,
    .read_flow         = sensirion_op_read_flow,
    .read_pressure     = NULL,
};

/* =========================================================================
 * Sensirion CRC-8 Algorithm (Poly 0x31: x^8 + x^5 + x^4 + 1, Init 0xFF)
 * ========================================================================= */

uint8_t wet_hal_sensirion_crc8(const uint8_t* data, size_t len) {
    if (!data) return 0;
    uint8_t crc = SENSIRION_CRC8_INIT;

    for (size_t i = 0; i < len; ++i) {
        crc ^= data[i];
        for (int b = 0; b < 8; ++b) {
            if (crc & 0x80U) {
                crc = (uint8_t)((crc << 1) ^ SENSIRION_CRC8_POLYNOMIAL);
            } else {
                crc = (uint8_t)(crc << 1);
            }
        }
    }
    return crc;
}

int wet_hal_sensirion_validate_crc(const uint8_t word_and_crc[3]) {
    if (!word_and_crc) return 0;
    uint8_t computed = wet_hal_sensirion_crc8(word_and_crc, 2);
    return (computed == word_and_crc[2]) ? 1 : 0;
}

/* =========================================================================
 * Sensirion SHDLC Protocol (SLI Series RS-485 / RS-232)
 * ========================================================================= */

size_t wet_hal_shdlc_encode(
    uint8_t address,
    uint8_t command,
    const uint8_t* payload,
    uint8_t payload_len,
    uint8_t* out_buf,
    size_t out_buf_max
) {
    if (!out_buf || out_buf_max < 6) return 0;

    /* Compute checksum: ~((address + command + length + sum(payload)) & 0xFF) */
    uint32_t sum = address + command + payload_len;
    for (uint8_t i = 0; i < payload_len; ++i) {
        sum += payload ? payload[i] : 0;
    }
    uint8_t checksum = (uint8_t)(~(sum & 0xFFU));

    size_t pos = 0;
    out_buf[pos++] = SHDLC_FRAME_START_STOP;

    /* Helper lambda to stuff a single byte */
    #define STUFF_BYTE(b) do { \
        uint8_t val = (uint8_t)(b); \
        if (val == 0x7E || val == 0x7D || val == 0x11 || val == 0x13) { \
            if (pos + 2 >= out_buf_max) return 0; \
            out_buf[pos++] = SHDLC_FRAME_ESCAPE; \
            out_buf[pos++] = (uint8_t)(val ^ SHDLC_ESCAPE_MASK); \
        } else { \
            if (pos + 1 >= out_buf_max) return 0; \
            out_buf[pos++] = val; \
        } \
    } while (0)

    STUFF_BYTE(address);
    STUFF_BYTE(command);
    STUFF_BYTE(payload_len);

    for (uint8_t i = 0; i < payload_len; ++i) {
        STUFF_BYTE(payload[i]);
    }

    STUFF_BYTE(checksum);

    if (pos >= out_buf_max) return 0;
    out_buf[pos++] = SHDLC_FRAME_START_STOP;

    #undef STUFF_BYTE
    return pos;
}

int wet_hal_shdlc_decode(
    const uint8_t* raw_buf,
    size_t raw_len,
    uint8_t* out_address,
    uint8_t* out_command,
    uint8_t* out_payload,
    uint8_t* out_payload_len
) {
    if (!raw_buf || raw_len < 6 || !out_address || !out_command || !out_payload || !out_payload_len) {
        return 0;
    }

    /* Verify framing delimiters */
    if (raw_buf[0] != SHDLC_FRAME_START_STOP || raw_buf[raw_len - 1] != SHDLC_FRAME_START_STOP) {
        return 0;
    }

    /* Unstuff bytes between start and stop */
    uint8_t unstuffed[SHDLC_MAX_FRAME_SIZE];
    size_t un_len = 0;
    size_t i = 1;

    while (i < raw_len - 1) {
        uint8_t b = raw_buf[i++];
        if (b == SHDLC_FRAME_ESCAPE) {
            if (i >= raw_len - 1) return 0; /* Malformed escape */
            uint8_t esc_b = raw_buf[i++];
            if (esc_b != 0x5E && esc_b != 0x5D && esc_b != 0x31 && esc_b != 0x33) {
                return 0; /* Illegal stuffing sequence: reject frame immediately */
            }
            unstuffed[un_len++] = (uint8_t)(esc_b ^ SHDLC_ESCAPE_MASK);
        } else {
            unstuffed[un_len++] = b;
        }
        if (un_len >= SHDLC_MAX_FRAME_SIZE) return 0;
    }

    /* Need at least address (1), command (1), length (1), checksum (1) = 4 bytes */
    if (un_len < 4) return 0;

    uint8_t addr = unstuffed[0];
    uint8_t cmd  = unstuffed[1];
    uint8_t plen = unstuffed[2];
    uint8_t rx_chk = unstuffed[un_len - 1];

    if (un_len != (size_t)(3 + plen + 1)) {
        return 0; /* Length mismatch */
    }

    /* Verify checksum */
    uint32_t sum = 0;
    for (size_t k = 0; k < un_len - 1; ++k) {
        sum += unstuffed[k];
    }
    uint8_t expected_chk = (uint8_t)(~(sum & 0xFFU));
    if (rx_chk != expected_chk) {
        return 0; /* Checksum failure */
    }

    *out_address = addr;
    *out_command = cmd;
    *out_payload_len = plen;
    for (uint8_t p = 0; p < plen; ++p) {
        out_payload[p] = unstuffed[3 + p];
    }
    return 1;
}

/* =========================================================================
 * Sensirion Driver Implementation
 * ========================================================================= */

wet_hal_driver_t* wet_hal_sensirion_create(wet_hal_mode_t mode) {
    wet_hal_driver_t* drv = (wet_hal_driver_t*)calloc(1, sizeof(wet_hal_driver_t));
    if (!drv) return NULL;

    sensirion_device_state_t* state = (sensirion_device_state_t*)calloc(1, sizeof(sensirion_device_state_t));
    if (!state) {
        free(drv);
        return NULL;
    }

    state->i2c_address = SENSIRION_I2C_ADDR_DEFAULT;
    state->scale_factor = 10.0f; /* 10 (uL/min)^-1 for SLF3S-0600x -> 0.1 uL/min resolution */
    state->current_flow_ul_min = 0.0;
    state->measurement_active = 0;
    state->shdlc_address = 0x00;

    const char* name = "Sensirion_SLF3x";
    for (int i = 0; i < 31 && name[i]; ++i) drv->name[i] = name[i];
    drv->driver_type = WET_HAL_DRIVER_FLOW;
    drv->mode = mode;
    drv->ops = &s_sensirion_ops;
    drv->context = state;

    return drv;
}

void wet_hal_sensirion_destroy(wet_hal_driver_t* drv) {
    if (!drv) return;
    if (drv->context) free(drv->context);
    free(drv);
}

wet_hal_status_t wet_hal_sensirion_start_measurement(
    wet_hal_driver_t* drv,
    uint16_t cmd
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;

    if (state->fault_nak_address) {
        return WET_HAL_ERR_IO;
    }

    state->active_command = cmd;
    state->measurement_active = 1;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_sensirion_stop_measurement(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;

    state->active_command = SENSIRION_CMD_STOP_CONT;
    state->measurement_active = 0;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_sensirion_read_flow(
    wet_hal_driver_t* drv,
    double* out_flow_ul_min
) {
    if (!drv || !drv->context || !out_flow_ul_min) return WET_HAL_ERR_NULL_PTR;
    sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;

    state->total_i2c_reads++;

    if (state->fault_nak_address) {
        return WET_HAL_ERR_IO;
    }

    /* Convert current flow to raw 16-bit signed integer word */
    int16_t raw_flow = (int16_t)(state->current_flow_ul_min * (double)state->scale_factor);
    state->raw_flow_ticks = raw_flow;

    uint8_t packet[3];
    packet[0] = (uint8_t)((raw_flow >> 8) & 0xFFU);
    packet[1] = (uint8_t)(raw_flow & 0xFFU);
    packet[2] = wet_hal_sensirion_crc8(packet, 2);

    /* Check CRC fault injection */
    if (state->fault_corrupt_crc) {
        packet[2] ^= 0x55U; /* Invert CRC bits */
    }

    if (!wet_hal_sensirion_validate_crc(packet)) {
        state->crc_errors++;
        return WET_HAL_ERR_CRC_MISMATCH;
    }

    int16_t rx_raw = (int16_t)(((uint16_t)packet[0] << 8) | (uint16_t)packet[1]);
    *out_flow_ul_min = (double)rx_raw / (double)state->scale_factor;
    return WET_HAL_OK;
}

void wet_hal_sensirion_hil_set_flow(
    wet_hal_driver_t* drv,
    double flow_ul_min
) {
    if (!drv || !drv->context) return;
    sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
    state->current_flow_ul_min = flow_ul_min;
}

void wet_hal_sensirion_inject_fault(
    wet_hal_driver_t* drv,
    uint8_t corrupt_crc,
    uint8_t nak_addr
) {
    if (!drv || !drv->context) return;
    sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
    state->fault_corrupt_crc = corrupt_crc;
    state->fault_nak_address = nak_addr;
}

/* =========================================================================
 * Vtable Callbacks
 * ========================================================================= */

static wet_hal_status_t sensirion_op_init(wet_hal_driver_t* drv, void* config) {
    (void)config;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    drv->is_initialized = 1;
    drv->is_active = 1;
    return WET_HAL_OK;
}

static wet_hal_status_t sensirion_op_shutdown(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    wet_hal_sensirion_stop_measurement(drv);
    drv->is_active = 0;
    return WET_HAL_OK;
}

static wet_hal_status_t sensirion_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
    (void)reason;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    sensirion_device_state_t* state = (sensirion_device_state_t*)drv->context;
    state->current_flow_ul_min = 0.0;
    return wet_hal_sensirion_stop_measurement(drv);
}

static wet_hal_status_t sensirion_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
    (void)current_tick;
    (void)dt_ms;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    return WET_HAL_OK;
}

static wet_hal_status_t sensirion_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min) {
    (void)sensor_id;
    return wet_hal_sensirion_read_flow(drv, out_flow_ul_min);
}
