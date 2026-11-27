#include "../include/wet_crt.h"
#include "../include/wet_hal_pump_valve.h"

/* Forward declaration of vtable operations */
static wet_hal_status_t microfluidics_op_init(wet_hal_driver_t* drv, void* config);
static wet_hal_status_t microfluidics_op_shutdown(wet_hal_driver_t* drv);
static wet_hal_status_t microfluidics_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason);
static wet_hal_status_t microfluidics_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);
static wet_hal_status_t microfluidics_op_write_pump(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag);
static wet_hal_status_t microfluidics_op_dispense_volume(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul);
static wet_hal_status_t microfluidics_op_write_valve(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t state);
static wet_hal_status_t microfluidics_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min);
static wet_hal_status_t microfluidics_op_read_pressure(wet_hal_driver_t* drv, uint8_t port_id, float* out_kpa);

static const wet_hal_ops_t s_microfluidics_ops = {
    .init              = microfluidics_op_init,
    .shutdown          = microfluidics_op_shutdown,
    .emergency_stop    = microfluidics_op_emergency_stop,
    .step_tick         = microfluidics_op_step_tick,
    .stim_voltage      = NULL,
    .stim_current      = NULL,
    .read_ephys        = NULL,
    .measure_impedance = NULL,
    .active_discharge  = NULL,
    .write_pump        = microfluidics_op_write_pump,
    .dispense_volume   = microfluidics_op_dispense_volume,
    .write_valve       = microfluidics_op_write_valve,
    .read_flow         = microfluidics_op_read_flow,
    .read_pressure     = microfluidics_op_read_pressure,
};

/* =========================================================================
 * Harvard Apparatus RS-232 & CAN Implementation
 * ========================================================================= */

int wet_hal_harvard_format_cmd(
    uint8_t address,
    uint8_t fast_mode,
    const char* cmd_name,
    const char* args,
    char* out_buf,
    size_t out_buf_len
) {
    if (!cmd_name || !out_buf || out_buf_len < 4) return -1;

    size_t pos = 0;

    /* 1. Daisy-chain address prefix if non-zero: e.g. "01 " */
    if (address > 0) {
        if (pos + 3 >= out_buf_len) return -1;
        out_buf[pos++] = (char)('0' + (address / 10) % 10);
        out_buf[pos++] = (char)('0' + (address % 10));
        out_buf[pos++] = ' ';
    }

    /* 2. Fast mode prefix '@' (bypasses screen update for <50 ms response) */
    if (fast_mode) {
        if (pos + 1 >= out_buf_len) return -1;
        out_buf[pos++] = '@';
    }

    /* 3. Command name */
    for (size_t i = 0; cmd_name[i] != '\0'; ++i) {
        if (pos + 1 >= out_buf_len) return -1;
        out_buf[pos++] = cmd_name[i];
    }

    /* 4. Arguments if present */
    if (args && args[0] != '\0') {
        if (pos + 1 >= out_buf_len) return -1;
        out_buf[pos++] = ' ';
        for (size_t i = 0; args[i] != '\0'; ++i) {
            if (pos + 1 >= out_buf_len) return -1;
            out_buf[pos++] = args[i];
        }
    }

    /* 5. Terminator '\r' */
    if (pos + 1 >= out_buf_len) return -1;
    out_buf[pos++] = '\r';
    out_buf[pos] = '\0';

    return (int)pos;
}

harvard_prompt_t wet_hal_harvard_parse_response(
    const char* resp_buf,
    size_t resp_len
) {
    if (!resp_buf || resp_len == 0) return HARVARD_PROMPT_INVALID;

    /* Skip trailing whitespace / newlines */
    size_t end = resp_len;
    while (end > 0 && (resp_buf[end - 1] == ' ' || resp_buf[end - 1] == '\t' ||
                       resp_buf[end - 1] == '\r' || resp_buf[end - 1] == '\n' ||
                       resp_buf[end - 1] == '\0')) {
        end--;
    }
    if (end == 0) return HARVARD_PROMPT_INVALID;

    size_t p = end - 1;
    char c = resp_buf[p];

    /* Check prefix before prompt: optional address digits or preceding delimiter */
    size_t pre = p;
    if (c == '*' && pre > 0 && resp_buf[pre - 1] == 'T') {
        pre--;
    }
    while (pre > 0 && resp_buf[pre - 1] >= '0' && resp_buf[pre - 1] <= '9') {
        pre--;
    }
    if (pre > 0) {
        char before = resp_buf[pre - 1];
        if (before != ' ' && before != '\t' && before != '\r' && before != '\n') {
            return HARVARD_PROMPT_INVALID;
        }
    }

    if (c == ':') return HARVARD_PROMPT_IDLE;
    if (c == '>') return HARVARD_PROMPT_INFUSING;
    if (c == '<') return HARVARD_PROMPT_WITHDRAWING;
    if (c == '*') {
        if (p > 0 && resp_buf[p - 1] == 'T') {
            return HARVARD_PROMPT_TARGET_DONE;
        }
        return HARVARD_PROMPT_STALLED;
    }

    return HARVARD_PROMPT_INVALID;
}

wet_hal_driver_t* wet_hal_microfluidics_create(wet_hal_mode_t mode) {
    wet_hal_driver_t* drv = (wet_hal_driver_t*)calloc(1, sizeof(wet_hal_driver_t));
    if (!drv) return NULL;

    microfluidic_state_t* state = (microfluidic_state_t*)calloc(1, sizeof(microfluidic_state_t));
    if (!state) {
        free(drv);
        return NULL;
    }

    state->dead_head_enabled = 1;
    state->max_pressure_kpa = 50.0f; /* 50.0 kPa burst safety limit for PDMS microfluidic bond */
    state->throttled_bypass_active = 0;
    wet_hal_serial_init(&state->serial_transport);
    state->serial_configured = 0U;
    state->serial_baud_rate = 115200U;
    state->serial_timeout_ms = 1000U;
    state->last_harvard_prompt = HARVARD_PROMPT_INVALID;
    for (int i = 0; i < WET_MAX_PUMPS; ++i) {
        state->pumps[i].address = (uint8_t)i;
        state->pumps[i].fast_mode = 1;
        state->valve_for_pump[i] = (uint8_t)i; /* 1-to-1 default valve pairing */
        state->valve_states[i] = 1;            /* Default open */
        state->pressure_kpa[i] = 0.0f;
    }

    const char* name = "Microfluidics_HAL";
    for (int i = 0; i < 31 && name[i]; ++i) drv->name[i] = name[i];
    drv->driver_type = WET_HAL_DRIVER_PUMP;
    drv->mode = mode;
    drv->ops = &s_microfluidics_ops;
    drv->context = state;

    return drv;
}

void wet_hal_microfluidics_destroy(wet_hal_driver_t* drv) {
    if (!drv) return;
    if (drv->context) {
        microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
        wet_hal_serial_close(&state->serial_transport);
        free(drv->context);
    }
    free(drv);
}

static wet_hal_status_t microfluidics_physical_exchange(
    microfluidic_state_t* state,
    uint8_t pump_id,
    const char* cmd_name,
    const char* args
) {
    char cmd_buf[128];
    int cmd_len = wet_hal_harvard_format_cmd(
        state->pumps[pump_id].address,
        state->pumps[pump_id].fast_mode,
        cmd_name,
        args,
        cmd_buf,
        sizeof(cmd_buf)
    );
    if (cmd_len < 0) return WET_HAL_ERR_OUT_OF_BOUNDS;

    wet_hal_status_t wst = wet_hal_serial_write_frame(&state->serial_transport, cmd_buf, (size_t)cmd_len);
    if (wst != WET_HAL_OK) return wst;

    char rx_buf[256];
    size_t rx_len = 0U;
    wet_hal_status_t rst = wet_hal_serial_read_frame(
        &state->serial_transport,
        rx_buf,
        sizeof(rx_buf),
        state->serial_timeout_ms,
        &rx_len
    );
    if (rst != WET_HAL_OK) return rst;

    size_t copy_len = (rx_len < sizeof(state->last_rx_frame) - 1U) ? rx_len : (sizeof(state->last_rx_frame) - 1U);
    memcpy(state->last_rx_frame, rx_buf, copy_len);
    state->last_rx_frame[copy_len] = '\0';

    harvard_prompt_t prompt = wet_hal_harvard_parse_response(rx_buf, rx_len);
    state->last_harvard_prompt = prompt;
    if (prompt == HARVARD_PROMPT_STALLED) {
        state->pumps[pump_id].is_stalled = 1U;
        state->pumps[pump_id].is_running = 0U;
        return WET_HAL_ERR_IO;
    }
    if (prompt == HARVARD_PROMPT_INVALID) {
        return WET_HAL_ERR_IO;
    }
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_microfluidics_open_serial(
    wet_hal_driver_t* drv,
    const char* port_name,
    uint32_t baud_rate,
    uint32_t timeout_ms
) {
    if (!drv || !drv->context || !port_name) return WET_HAL_ERR_NULL_PTR;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    if (state->serial_configured && wet_hal_serial_is_open(&state->serial_transport)) {
        wet_hal_serial_close(&state->serial_transport);
    }
    wet_hal_status_t st = wet_hal_serial_open(&state->serial_transport, port_name, baud_rate, timeout_ms);
    if (st != WET_HAL_OK) {
        state->serial_configured = 0U;
        return st;
    }
    state->serial_configured = 1U;
    state->serial_baud_rate = baud_rate ? baud_rate : 115200U;
    state->serial_timeout_ms = timeout_ms ? timeout_ms : 1000U;
    return WET_HAL_OK;
}

void wet_hal_microfluidics_close_serial(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    wet_hal_serial_close(&state->serial_transport);
    state->serial_configured = 0U;
}

wet_hal_status_t wet_hal_pump_set_rate(
    wet_hal_driver_t* drv,
    uint8_t pump_id,
    double rate_ul_min,
    uint8_t run_flag
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (pump_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;

    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;

    /* Check Dead-Head Overpressure Interlock:
     * If pump is commanded to run (rate > 0 and run_flag), verify downstream valve is OPEN
     * and inline MEMS transducer does not report overpressure (> max_pressure_kpa). */
    if (state->dead_head_enabled && run_flag && rate_ul_min > 0.0) {
        uint8_t valve_id = state->valve_for_pump[pump_id];
        int valve_closed = (valve_id < WET_MAX_VALVES && state->valve_states[valve_id] == 0);
        int overpressure = (state->pressure_kpa[pump_id] > state->max_pressure_kpa);
        if (valve_closed || overpressure) {
            state->dead_head_trip_count++;
            state->throttled_bypass_active = 1; /* Engage high-resistance capillary bypass to prevent recoil shockwave */
            return WET_HAL_ERR_DEAD_HEAD;
        }
    }

    if (state->fault_inject_stall) {
        state->pumps[pump_id].is_stalled = 1;
        state->pumps[pump_id].is_running = 0;
        return WET_HAL_ERR_IO;
    }

    if (state->fault_inject_rs232_timeout) {
        return WET_HAL_ERR_TIMEOUT;
    }

    if (drv->mode == WET_HAL_MODE_PHYSICAL &&
        state->serial_configured &&
        wet_hal_serial_is_open(&state->serial_transport)) {
        wet_hal_status_t xst = WET_HAL_OK;
        if (!run_flag || rate_ul_min <= 0.0) {
            xst = microfluidics_physical_exchange(state, pump_id, "stp", NULL);
        } else {
            char args[64];
            snprintf(args, sizeof(args), "%.3f u/m", rate_ul_min);
            xst = microfluidics_physical_exchange(state, pump_id, "irate", args);
        }
        if (xst != WET_HAL_OK) return xst;
    }

    state->pumps[pump_id].rate_ul_min = rate_ul_min;
    state->pumps[pump_id].is_running = run_flag ? 1 : 0;
    state->total_rs232_tx++;

    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_pump_dispense(
    wet_hal_driver_t* drv,
    uint8_t pump_id,
    double volume_ul
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (pump_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;

    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;

    /* Dead-Head check */
    if (state->dead_head_enabled && volume_ul > 0.0) {
        uint8_t valve_id = state->valve_for_pump[pump_id];
        int valve_closed = (valve_id < WET_MAX_VALVES && state->valve_states[valve_id] == 0);
        int overpressure = (state->pressure_kpa[pump_id] > state->max_pressure_kpa);
        if (valve_closed || overpressure) {
            state->dead_head_trip_count++;
            state->throttled_bypass_active = 1;
            return WET_HAL_ERR_DEAD_HEAD;
        }
    }

    if (state->fault_inject_stall) {
        state->pumps[pump_id].is_stalled = 1;
        state->pumps[pump_id].is_running = 0;
        return WET_HAL_ERR_IO;
    }

    if (state->fault_inject_rs232_timeout) {
        return WET_HAL_ERR_TIMEOUT;
    }

    if (drv->mode == WET_HAL_MODE_PHYSICAL &&
        state->serial_configured &&
        wet_hal_serial_is_open(&state->serial_transport)) {
        char args[64];
        snprintf(args, sizeof(args), "%.3f u", volume_ul);
        wet_hal_status_t xst = microfluidics_physical_exchange(state, pump_id, "tvolume", args);
        if (xst != WET_HAL_OK) return xst;
    }

    state->pumps[pump_id].infused_volume_ul += volume_ul;
    state->total_rs232_tx++;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_pump_stop(
    wet_hal_driver_t* drv,
    uint8_t pump_id
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (pump_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;

    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;

    if (drv->mode == WET_HAL_MODE_PHYSICAL &&
        state->serial_configured &&
        wet_hal_serial_is_open(&state->serial_transport)) {
        wet_hal_status_t xst = microfluidics_physical_exchange(state, pump_id, "stp", NULL);
        if (xst != WET_HAL_OK) return xst;
    }

    state->pumps[pump_id].is_running = 0;
    state->pumps[pump_id].rate_ul_min = 0.0;
    state->total_rs232_tx++;
    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_valve_set_state(
    wet_hal_driver_t* drv,
    uint8_t valve_id,
    uint8_t val_state
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    if (valve_id >= WET_MAX_VALVES) return WET_HAL_ERR_OUT_OF_BOUNDS;

    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    state->valve_states[valve_id] = (val_state != 0) ? 1 : 0;
    return WET_HAL_OK;
}

void wet_hal_pump_bind_downstream_valve(
    wet_hal_driver_t* drv,
    uint8_t pump_id,
    uint8_t valve_id
) {
    if (!drv || !drv->context) return;
    if (pump_id >= WET_MAX_PUMPS || valve_id >= WET_MAX_VALVES) return;

    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    state->valve_for_pump[pump_id] = valve_id;
}

wet_hal_status_t wet_hal_can_send(
    wet_hal_driver_t* drv,
    const wet_can_frame_t* frame
) {
    if (!drv || !drv->context || !frame) return WET_HAL_ERR_NULL_PTR;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;

    /* Enforce ISO 11898-1 limits & ID boundaries */
    if (frame->dlc > 8) {
        return WET_HAL_ERR_OUT_OF_BOUNDS;
    }
    if (!frame->is_extended && frame->id > 0x7FFU) {
        return WET_HAL_ERR_OUT_OF_BOUNDS;
    }
    if (frame->is_extended && frame->id > 0x1FFFFFFFU) {
        return WET_HAL_ERR_OUT_OF_BOUNDS;
    }

    if (state->fault_inject_can_drop) {
        return WET_HAL_OK; /* Mock frame drop */
    }

    if (state->can_tx_count >= WET_CAN_QUEUE_CAPACITY) {
        return WET_HAL_ERR_BUFFER_FULL;
    }

    state->can_tx_queue[state->can_tx_tail] = *frame;
    state->can_tx_tail = (state->can_tx_tail + 1) % WET_CAN_QUEUE_CAPACITY;
    state->can_tx_count++;
    state->total_can_frames_tx++;

    /* In HIL loopback mode, copy transmitted frame into RX queue for bidirectional loopback */
    if (drv->mode == WET_HAL_MODE_HIL_LOOPBACK) {
        if (state->can_rx_count < WET_CAN_QUEUE_CAPACITY) {
            state->can_rx_queue[state->can_rx_tail] = *frame;
            state->can_rx_tail = (state->can_rx_tail + 1) % WET_CAN_QUEUE_CAPACITY;
            state->can_rx_count++;
        }
    }

    /* In HIL loopback mode, automatically handle Process Data Objects (PDOs) ONLY for standard 11-bit frames */
    if (!frame->is_extended) {
        uint32_t base_id = frame->id & ~0x7FU;
        uint8_t node_id = (uint8_t)(frame->id & 0x7FU);

        if (base_id == CAN_ID_RPDO1_BASE && node_id < WET_MAX_PUMPS) {
            /* RPDO1: Float32 rate + 1 byte run flag */
            if (frame->dlc >= 5) {
                float rate;
                memcpy(&rate, frame->data, sizeof(float));
                uint8_t run_flag = frame->data[4];
                wet_hal_pump_set_rate(drv, node_id, (double)rate, run_flag);
            }
        } else if (base_id == CAN_ID_RPDO2_BASE) {
            /* RPDO2: Valve bitmask */
            if (frame->dlc >= 1) {
                uint8_t mask = frame->data[0];
                for (uint8_t v = 0; v < WET_MAX_VALVES; ++v) {
                    state->valve_states[v] = (mask & (1U << v)) ? 1 : 0;
                }
            }
        }
    }

    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_can_recv(
    wet_hal_driver_t* drv,
    wet_can_frame_t* out_frame
) {
    if (!drv || !drv->context || !out_frame) return WET_HAL_ERR_NULL_PTR;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;

    if (state->can_rx_count == 0) {
        return WET_HAL_ERR_TIMEOUT;
    }

    *out_frame = state->can_rx_queue[state->can_rx_head];
    state->can_rx_head = (state->can_rx_head + 1) % WET_CAN_QUEUE_CAPACITY;
    state->can_rx_count--;
    state->total_can_frames_rx++;

    return WET_HAL_OK;
}

wet_hal_status_t wet_hal_can_send_emcy(
    wet_hal_driver_t* drv,
    uint8_t node_id,
    uint16_t error_code,
    uint8_t error_register
) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;

    wet_can_frame_t frame;
    memset(&frame, 0, sizeof(frame));
    frame.id = CAN_ID_EMCY_BASE + (node_id & 0x7FU);
    frame.is_extended = 0;
    frame.dlc = 8;
    frame.data[0] = (uint8_t)(error_code & 0xFFU);
    frame.data[1] = (uint8_t)((error_code >> 8) & 0xFFU);
    frame.data[2] = error_register;

    state->total_emcy_frames++;
    return wet_hal_can_send(drv, &frame);
}

void wet_hal_microfluidics_inject_fault(
    wet_hal_driver_t* drv,
    uint8_t stall,
    uint8_t can_drop,
    uint8_t timeout
) {
    if (!drv || !drv->context) return;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    state->fault_inject_stall = stall;
    state->fault_inject_can_drop = can_drop;
    state->fault_inject_rs232_timeout = timeout;
}

/* =========================================================================
 * Vtable Callbacks
 * ========================================================================= */

static wet_hal_status_t microfluidics_op_init(wet_hal_driver_t* drv, void* config) {
    (void)config;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    drv->is_initialized = 1;
    drv->is_active = 1;
    return WET_HAL_OK;
}

static wet_hal_status_t microfluidics_op_shutdown(wet_hal_driver_t* drv) {
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    for (int i = 0; i < WET_MAX_PUMPS; ++i) {
        state->pumps[i].is_running = 0;
        state->pumps[i].rate_ul_min = 0.0;
    }
    drv->is_active = 0;
    return WET_HAL_OK;
}

static wet_hal_status_t microfluidics_op_emergency_stop(wet_hal_driver_t* drv, uint32_t reason) {
    (void)reason;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;

    /* Instantly halt all 8 syringe pumps */
    for (int i = 0; i < WET_MAX_PUMPS; ++i) {
        state->pumps[i].is_running = 0;
        state->pumps[i].rate_ul_min = 0.0;
    }

    if (drv->mode == WET_HAL_MODE_PHYSICAL &&
        state->serial_configured &&
        wet_hal_serial_is_open(&state->serial_transport)) {
        char cmd_buf[32];
        int clen = wet_hal_harvard_format_cmd(
            state->pumps[0].address, state->pumps[0].fast_mode, "stp", NULL, cmd_buf, sizeof(cmd_buf)
        );
        if (clen > 0) {
            wet_hal_serial_write_frame(&state->serial_transport, cmd_buf, (size_t)clen);
        }
    }

    /* Broadcast CAN emergency stop frame */
    wet_hal_can_send_emcy(drv, 0, 0x1000, 0x01);
    return WET_HAL_OK;
}

static wet_hal_status_t microfluidics_op_step_tick(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms) {
    (void)current_tick;
    if (!drv || !drv->context) return WET_HAL_ERR_NULL_PTR;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;

    /* Integrate infused volume */
    for (int i = 0; i < WET_MAX_PUMPS; ++i) {
        if (state->pumps[i].is_running) {
            double vol_tick = state->pumps[i].rate_ul_min * (dt_ms / 60000.0);
            state->pumps[i].infused_volume_ul += vol_tick;
        }
    }
    return WET_HAL_OK;
}

static wet_hal_status_t microfluidics_op_write_pump(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag) {
    return wet_hal_pump_set_rate(drv, pump_id, rate_ul_min, run_flag);
}

static wet_hal_status_t microfluidics_op_dispense_volume(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul) {
    return wet_hal_pump_dispense(drv, pump_id, volume_ul);
}

static wet_hal_status_t microfluidics_op_write_valve(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t state) {
    return wet_hal_valve_set_state(drv, valve_id, state);
}

static wet_hal_status_t microfluidics_op_read_flow(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min) {
    if (!drv || !drv->context || !out_flow_ul_min) return WET_HAL_ERR_NULL_PTR;
    if (sensor_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    *out_flow_ul_min = state->pumps[sensor_id].is_running ? state->pumps[sensor_id].rate_ul_min : 0.0;
    return WET_HAL_OK;
}

void wet_hal_pump_set_inline_pressure(
    wet_hal_driver_t* drv,
    uint8_t pump_id,
    float pressure_kpa
) {
    if (!drv || !drv->context || pump_id >= WET_MAX_PUMPS) return;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    state->pressure_kpa[pump_id] = pressure_kpa;
}

static wet_hal_status_t microfluidics_op_read_pressure(wet_hal_driver_t* drv, uint8_t port_id, float* out_kpa) {
    if (!drv || !drv->context || !out_kpa) return WET_HAL_ERR_NULL_PTR;
    if (port_id >= WET_MAX_PUMPS) return WET_HAL_ERR_OUT_OF_BOUNDS;
    microfluidic_state_t* state = (microfluidic_state_t*)drv->context;
    *out_kpa = state->pressure_kpa[port_id];
    return WET_HAL_OK;
}
