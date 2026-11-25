#ifndef WET_BUILDING_DLL
#define WET_BUILDING_DLL
#endif

#include "../include/wet_crt.h"
#include "../include/wetvm_types.h"
#include "../include/wetvm_api.h"
#include "../include/wetvm_vm.h"
#include "../include/wet_hal.h"

#if defined(_WIN32)
int _fltused = 0x9875;
#endif

/* Forward declarations of internal functions in wetvm_vm.c */
extern wet_status_t wet_vm_load_bytecode_internal(
    struct wet_vm_instance* vm,
    const uint8_t* code_bytes,
    size_t size,
    char* err_buf,
    size_t err_buf_len
);

extern wet_status_t wet_verify_bytecode_internal(
    const uint8_t* bytecode,
    size_t size,
    char* err_buf,
    size_t err_buf_len
);

extern wet_status_t wet_vm_snapshot_internal(
    const struct wet_vm_instance* vm,
    uint8_t* buffer,
    size_t* inout_len
);

extern wet_status_t wet_vm_restore_internal(
    struct wet_vm_instance* vm,
    const uint8_t* buffer,
    size_t len
);

WET_EXPORT wet_vm_t* wet_create_vm(const wet_vm_config_t* config) {
    struct wet_vm_instance* vm = (struct wet_vm_instance*)calloc(1, sizeof(struct wet_vm_instance));
    if (!vm) return NULL;

    /* Apply configuration with sensible defaults */
    if (config) {
        vm->config.dt_ms = (config->dt_ms > 0.0) ? config->dt_ms : 0.1;
        vm->config.max_stack_depth = (config->max_stack_depth > 0) ? config->max_stack_depth : 1024;
        vm->config.max_locals = (config->max_locals > 0) ? config->max_locals : 256;
        vm->config.channel_count = (config->channel_count > 0)
                                    ? config->channel_count : 64;
        if (vm->config.channel_count > 64U) {
            vm->config.channel_count = 64U;
        }
        vm->config.max_ops_per_tick = (config->max_ops_per_tick > 0) ? config->max_ops_per_tick : 100000U;
        vm->config.min_sequence_counter = config->min_sequence_counter;
    } else {
        vm->config.dt_ms = 0.1;
        vm->config.max_stack_depth = 1024;
        vm->config.max_locals = 256;
        vm->config.channel_count = 64;
        vm->config.max_ops_per_tick = 100000U;
        vm->config.min_sequence_counter = 0;
    }

    vm->max_stack = vm->config.max_stack_depth;
    vm->stack = (wet_value_t*)calloc(vm->max_stack, sizeof(wet_value_t));
    if (!vm->stack) {
        free(vm);
        return NULL;
    }

    vm->max_locals = vm->config.max_locals;
    vm->locals = (wet_value_t*)calloc(vm->max_locals, sizeof(wet_value_t));
    if (!vm->locals) {
        free(vm->stack);
        free(vm);
        return NULL;
    }

    vm->max_call_depth = 64;
    vm->call_stack = (wet_call_frame_t*)calloc(vm->max_call_depth, sizeof(wet_call_frame_t));
    if (!vm->call_stack) {
        free(vm->locals);
        free(vm->stack);
        free(vm);
        return NULL;
    }

    vm->grid_rows = 8;
    vm->grid_cols = 8;
    vm->last_error[0] = '\0';

    /* Initialize cyber-physical life support actuator states */
    vm->ambient_temperature_c = 37.0f;
    for (int p = 0; p < 4; ++p) {
        vm->fluid_pressure_kpa[p] = 101.325f;
    }

    /* Ring-0 Life Support Supervisor Initialization */
    vm->life_supervisor.supervisor_active = 1;
    vm->life_supervisor.maintenance_temperature_c = 37.0f;
    for (int i = 0; i < 8; ++i) {
        vm->life_supervisor.maintenance_perfusion_ul_min[i] = 1.5f;
    }

    biophysics_init(&vm->bio, vm->config.dt_ms, 0);
    interlocks_init(&vm->interlocks);

    return vm;
}

WET_EXPORT wet_vm_t* wet_create_vm_arena(
    void* arena_buf,
    size_t arena_bytes,
    const wet_vm_config_t* config
) {
    if (!arena_buf || arena_bytes == 0) return NULL;

    uint32_t stack_depth = (config && config->max_stack_depth > 0) ? config->max_stack_depth : 1024U;
    uint32_t max_locals = (config && config->max_locals > 0) ? config->max_locals : 256U;
    uint32_t call_depth = 64U;

    /* Overflow-safe byte size calculations */
    if ((size_t)stack_depth > (SIZE_MAX / sizeof(wet_value_t)) / 2U ||
        (size_t)max_locals > (SIZE_MAX / sizeof(wet_value_t)) / 2U ||
        (size_t)call_depth > (SIZE_MAX / sizeof(wet_call_frame_t)) / 2U) {
        return NULL;
    }

    size_t stack_bytes = (size_t)stack_depth * sizeof(wet_value_t);
    size_t locals_bytes = (size_t)max_locals * sizeof(wet_value_t);
    size_t call_bytes = (size_t)call_depth * sizeof(wet_call_frame_t);

    /* Align arena base to 128 bytes (WET_CACHELINE_SIZE) for DMA & cache coherency */
    uint8_t* raw_ptr = (uint8_t*)arena_buf;
    uintptr_t u = (uintptr_t)raw_ptr;
    if (u > UINTPTR_MAX - 127U) return NULL;
    uintptr_t aligned_u = (u + 127U) & ~((uintptr_t)127U);
    size_t align_pad = (size_t)(aligned_u - u);
    if (arena_bytes <= align_pad) return NULL;
    size_t avail = arena_bytes - align_pad;

    size_t vm_sz = sizeof(struct wet_vm_instance);
    if (vm_sz > SIZE_MAX - 127U) return NULL;
    size_t off_stack = (vm_sz + 127U) & ~((size_t)127U);
    if (avail < off_stack) return NULL;

    size_t tail_avail = avail - off_stack;
    if (stack_bytes > tail_avail) return NULL;
    tail_avail -= stack_bytes;
    if (locals_bytes > tail_avail) return NULL;
    tail_avail -= locals_bytes;
    if (call_bytes > tail_avail) return NULL;

    uint8_t* ptr = (uint8_t*)aligned_u;
    struct wet_vm_instance* vm = (struct wet_vm_instance*)ptr;
    memset(vm, 0, sizeof(struct wet_vm_instance));

    vm->arena_allocated = 1;
    vm->arena_base = raw_ptr;
    vm->arena_total_bytes = arena_bytes;
    size_t end_rel = off_stack + stack_bytes + locals_bytes + call_bytes;
    size_t mark_off = align_pad + end_rel;
    if (mark_off <= arena_bytes - 15U) {
        mark_off = (mark_off + 15U) & ~((size_t)15U);
    }
    if (mark_off > arena_bytes) mark_off = arena_bytes;
    vm->arena_mark_offset = mark_off;
    vm->arena_bump_offset = mark_off;

    if (config) {
        vm->config = *config;
        if (vm->config.dt_ms <= 0.0) vm->config.dt_ms = 0.1;
        if (vm->config.max_stack_depth == 0) vm->config.max_stack_depth = stack_depth;
        if (vm->config.max_locals == 0) vm->config.max_locals = max_locals;
        if (vm->config.channel_count == 0) vm->config.channel_count = 64;
        if (vm->config.channel_count > 64U) vm->config.channel_count = 64U;
        if (vm->config.max_ops_per_tick == 0) vm->config.max_ops_per_tick = 100000U;
    } else {
        vm->config.dt_ms = 0.1;
        vm->config.max_stack_depth = stack_depth;
        vm->config.max_locals = max_locals;
        vm->config.channel_count = 64;
        vm->config.max_ops_per_tick = 100000U;
    }

    ptr = (uint8_t*)aligned_u + off_stack;
    vm->max_stack = stack_depth;
    vm->stack = (wet_value_t*)ptr;
    ptr += stack_bytes;

    vm->max_locals = max_locals;
    vm->locals = (wet_value_t*)ptr;
    ptr += locals_bytes;

    vm->max_call_depth = call_depth;
    vm->call_stack = (wet_call_frame_t*)ptr;

    vm->grid_rows = 8;
    vm->grid_cols = 8;
    vm->last_error[0] = '\0';
    vm->ambient_temperature_c = 37.0f;
    for (int p = 0; p < 4; ++p) {
        vm->fluid_pressure_kpa[p] = 101.325f;
    }

    vm->life_supervisor.supervisor_active = 1;
    vm->life_supervisor.maintenance_temperature_c = 37.0f;
    for (int i = 0; i < 8; ++i) {
        vm->life_supervisor.maintenance_perfusion_ul_min[i] = 1.5f;
    }

    biophysics_init(&vm->bio, vm->config.dt_ms, 0);
    interlocks_init(&vm->interlocks);

    return vm;
}

WET_EXPORT void wet_free_vm(wet_vm_t* vm) {
    if (!vm) return;

    if (vm->hal) {
        wet_hal_destroy(vm->hal);
        vm->hal = NULL;
    }

    if (!vm->arena_allocated) {
        if (vm->constants) {
            for (size_t i = 0; i < vm->num_constants; ++i) {
                if (vm->constants[i].str_alloc) {
                    free(vm->constants[i].str_alloc);
                    vm->constants[i].str_alloc = NULL;
                }
            }
            free(vm->constants);
            vm->constants = NULL;
        }

        if (vm->bytecode_raw) {
            free(vm->bytecode_raw);
            vm->bytecode_raw = NULL;
        }

        if (vm->stack) {
            free(vm->stack);
            vm->stack = NULL;
        }

        if (vm->locals) {
            free(vm->locals);
            vm->locals = NULL;
        }

        if (vm->call_stack) {
            free(vm->call_stack);
            vm->call_stack = NULL;
        }

        free(vm);
    } else {
        /*
         * Defense-in-depth: Secure volatile memory scrubbing across the ENTIRE arena buffer
         * (instance, stack, locals, call_stack, bytecode_raw, and constant pool).
         */
        uint8_t* base = vm->arena_base;
        size_t total_sz = vm->arena_total_bytes;
        if (base && total_sz > 0) {
            volatile uint8_t* scrub_p = (volatile uint8_t*)base;
            for (size_t i = 0; i < total_sz; ++i) {
                scrub_p[i] = 0;
            }
        } else {
            volatile uint8_t* scrub_p = (volatile uint8_t*)vm;
            for (size_t i = 0; i < sizeof(struct wet_vm_instance); i++) {
                scrub_p[i] = 0;
            }
        }
    }
}

WET_EXPORT wet_status_t wet_load_bytecode(
    wet_vm_t* vm,
    const uint8_t* code_bytes,
    size_t size,
    char* err_buf,
    size_t err_buf_len
) {
    if (!vm) {
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "Null VM pointer");
        }
        return WET_ERR_NULL_PTR;
    }
    return wet_vm_load_bytecode_internal(vm, code_bytes, size, err_buf, err_buf_len);
}

WET_EXPORT wet_status_t wet_step_tick(
    wet_vm_t* vm,
    wet_telemetry_t* out_telem
) {
    if (!vm) return WET_ERR_NULL_PTR;
    return wet_vm_step_internal(vm, out_telem);
}

WET_EXPORT wet_status_t wet_run_ticks(
    wet_vm_t* vm,
    uint32_t ticks,
    uint32_t* executed_ticks,
    wet_telemetry_t* out_telem
) {
    if (!vm) return WET_ERR_NULL_PTR;

    uint32_t executed = 0;
    wet_status_t status = WET_OK;

    for (uint32_t i = 0; i < ticks; ++i) {
        status = wet_vm_step_internal(vm, out_telem);
        if (status != WET_OK) {
            break;
        }
        executed++;
    }

    if (executed_ticks) {
        *executed_ticks = executed;
    }

    return status;
}

WET_EXPORT wet_status_t wet_inject_stimulus(
    wet_vm_t* vm,
    uint8_t channel,
    float voltage_v,
    float phase1_ms,
    float phase2_ms
) {
    if (!vm) return WET_ERR_NULL_PTR;
    if (channel >= vm->config.channel_count) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Channel %u out of bounds (max %u)", channel, vm->config.channel_count);
        return WET_ERR_OUT_OF_BOUNDS_CH;
    }
    if (vm->interlocks.locked) {
        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
        return WET_ERR_INTERLOCK_LOCKED;
    }

    if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_BIPHASIC, voltage_v, channel)) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Capability denied for wet_inject_stimulus on ch %u (req %.2fV)", channel, voltage_v);
        return WET_ERR_CAPABILITY_DENIED;
    }

    /* Per-Phase Charge Density Limit (Shannon Model): prevent massive biphasic pulses with net=0 */
    if (phase1_ms > 0.0f && phase2_ms > 0.0f) {
        float q_p1 = (fabsf(voltage_v) / vm->bio.electrode_impedance_kohm) * 1000.0f * phase1_ms;
        float q_p2 = (fabsf(voltage_v) / vm->bio.electrode_impedance_kohm) * 1000.0f * phase2_ms;
        if (q_p1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_p2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
            vm->interlocks.locked = 1;
            vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
            vm->interlocks.tripped_channel = channel;
            vm->interlocks.trip_tick = vm->current_tick;
            vm->interlocks.trip_value = q_p1 > q_p2 ? q_p1 : q_p2;
            snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
                     "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
                     channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
            snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
            return WET_ERR_CHARGE_DENSITY_EXCEEDED;
        }
    }

    /* Active charge recovery: if previous pulse had pending Phase 2 counter-charge, discharge it */
    bio_stim_pulse_t* prev_p = &vm->bio.stim_pulses[channel];
    if (prev_p->active && prev_p->phase2_ticks_left > 0) {
        float i_ua = (prev_p->phase2_amp_v / vm->bio.electrode_impedance_kohm) * 1000.0f;
        vm->discharge_charge_nc[channel] += i_ua * (float)vm->bio.dt_ms * (float)prev_p->phase2_ticks_left;
    }

    float clamped_v = interlocks_clamp_voltage_dynamic(&vm->interlocks, channel, voltage_v);
    biophysics_schedule_stim(&vm->bio, channel, clamped_v, phase1_ms, phase2_ms);
    vm->voltages[channel] = clamped_v;
    float i_ma = clamped_v / vm->bio.electrode_impedance_kohm;
    vm->last_charge_nc[channel] = i_ma * (phase1_ms - phase2_ms);
    return WET_OK;
}

WET_EXPORT wet_status_t wet_get_telemetry(
    wet_vm_t* vm,
    wet_telemetry_t* out_telem
) {
    if (!vm || !out_telem) return WET_ERR_NULL_PTR;

    out_telem->current_tick = vm->current_tick;
    out_telem->sim_time_ms = vm->sim_time_ms;
    out_telem->population_rate_hz = vm->population_rate_hz;
    memcpy(out_telem->voltages, vm->voltages, sizeof(float) * 64);
    memcpy(out_telem->spikes, vm->spikes, sizeof(uint8_t) * 64);
    memcpy(out_telem->last_charge_nc, vm->last_charge_nc, sizeof(float) * 64);

    return WET_OK;
}

WET_EXPORT wet_status_t wet_get_spikes_window(
    const wet_vm_t* vm,
    uint32_t lookback_ticks,
    uint32_t* out_counts,
    size_t out_capacity
) {
    if (!vm || !out_counts) return WET_ERR_NULL_PTR;
    if (out_capacity == 0) return WET_OK;

    uint32_t n_ticks = lookback_ticks;
    if (n_ticks > BIO_SPIKE_HISTORY_LEN) {
        n_ticks = BIO_SPIKE_HISTORY_LEN;
    }

    size_t n_ch = (out_capacity < BIO_NUM_CHANNELS) ? out_capacity : (size_t)BIO_NUM_CHANNELS;
    for (size_t ch = 0; ch < n_ch; ++ch) {
        uint32_t count = 0U;
        int idx = (int)vm->bio.spike_history_head - 1;
        for (uint32_t k = 0; k < n_ticks; ++k) {
            if (idx < 0) idx += BIO_SPIKE_HISTORY_LEN;
            count += vm->bio.spike_history[ch][idx];
            idx--;
        }
        out_counts[ch] = count;
    }
    for (size_t ch = n_ch; ch < out_capacity; ++ch) {
        out_counts[ch] = 0U;
    }

    return WET_OK;
}

WET_EXPORT wet_status_t wet_get_actuator_telemetry(
    wet_vm_t* vm,
    wet_actuator_telemetry_t* out_act_telem
) {
    if (!vm || !out_act_telem) return WET_ERR_NULL_PTR;

    for (int i = 0; i < 8; ++i) {
        out_act_telem->pump_rates_ul_min[i] = vm->pump_rates_ul_min[i];
        out_act_telem->pump_dispensed_ul[i] = vm->pump_dispensed_ul[i];
        out_act_telem->valve_states[i] = vm->valve_states[i];
    }
    for (int i = 0; i < 4; ++i) {
        out_act_telem->motor_positions[i] = vm->motor_positions[i];
        out_act_telem->motor_speeds_rpm[i] = vm->motor_speeds_rpm[i];
        out_act_telem->fluid_pressure_kpa[i] = vm->fluid_pressure_kpa[i];
    }
    out_act_telem->ambient_temperature_c = vm->ambient_temperature_c;
    return WET_OK;
}

WET_EXPORT const char* wet_get_last_error(wet_vm_t* vm) {
    if (!vm) return "NULL VM pointer";
    return vm->last_error;
}

WET_EXPORT const char* wet_status_to_string(wet_status_t status) {
    switch (status) {
        case WET_OK:
            return "WET_OK: Operation successful";
        case WET_ERR_INVALID_MAGIC:
            return "WET_ERR_INVALID_MAGIC: Invalid WBC header magic";
        case WET_ERR_CRC_MISMATCH:
            return "WET_ERR_CRC_MISMATCH: Bytecode CRC32 checksum mismatch";
        case WET_ERR_UNSUPPORTED_VERSION:
            return "WET_ERR_UNSUPPORTED_VERSION: Unsupported bytecode version";
        case WET_ERR_MALFORMED_SECTION:
            return "WET_ERR_MALFORMED_SECTION: Malformed bytecode or section table";
        case WET_ERR_STACK_OVERFLOW:
            return "WET_ERR_STACK_OVERFLOW: Operand stack overflow";
        case WET_ERR_STACK_UNDERFLOW:
            return "WET_ERR_STACK_UNDERFLOW: Operand stack underflow";
        case WET_ERR_INVALID_OPCODE:
            return "WET_ERR_INVALID_OPCODE: Unrecognized or invalid opcode";
        case WET_ERR_OUT_OF_BOUNDS_CH:
            return "WET_ERR_OUT_OF_BOUNDS_CH: Channel index out of bounds";
        case WET_ERR_DIVISION_BY_ZERO:
            return "WET_ERR_DIVISION_BY_ZERO: Division by zero";
        case WET_ERR_NULL_PTR:
            return "WET_ERR_NULL_PTR: Null pointer argument";
        case WET_ERR_ALLOC_FAILED:
            return "WET_ERR_ALLOC_FAILED: Memory allocation failed";
        case WET_ERR_HALTED:
            return "WET_ERR_HALTED: Virtual machine is halted";
        case WET_ERR_CHARGE_IMBALANCE:
            return "WET_ERR_CHARGE_IMBALANCE: Net charge imbalance exceeded safety threshold (0.5 nC over 10 ms)";
        case WET_ERR_EPILEPTIFORM_RUNAWAY:
            return "WET_ERR_EPILEPTIFORM_RUNAWAY: Epileptiform runaway firing breaker tripped (>150 Hz on >35% channels for 50 ms)";
        case WET_ERR_CAPABILITY_DENIED:
            return "WET_ERR_CAPABILITY_DENIED: Capability permission denied by bytecode security manifest";
        case WET_ERR_INTERLOCK_LOCKED:
            return "WET_ERR_INTERLOCK_LOCKED: Hardware interlock locked out; all stimulation disabled";
        case WET_ERR_CHARGE_DENSITY_EXCEEDED:
            return "WET_ERR_CHARGE_DENSITY_EXCEEDED: Single-phase charge density exceeded Shannon safety limit";
        case WET_ERR_FOCAL_EXCITOTOXICITY:
            return "WET_ERR_FOCAL_EXCITOTOXICITY: Focal excitotoxicity limit exceeded";
        case WET_ERR_SHEAR_STRESS_EXCEEDED:
            return "WET_ERR_SHEAR_STRESS_EXCEEDED: Requested microfluidic pump rate exceeds safe shear stress limit (15.0 uL/min)";
        case WET_ERR_SECURITY_UNTRUSTED:
            return "WET_ERR_SECURITY_UNTRUSTED: Bytecode failed cryptographic security signature verification";
        case WET_ERR_ACTUATOR_FAULT:
            return "WET_ERR_ACTUATOR_FAULT: Cyber-physical actuator execution fault or invalid parameter";
        case WET_ERR_THERMAL_LIMIT:
            return "WET_ERR_THERMAL_LIMIT: Temperature exceeded maximum biological threshold (38.0 C)";
        case WET_ERR_BUBBLE_DETECTED:
            return "WET_ERR_BUBBLE_DETECTED: Fluidic optical bubble detector tripped (cavitation hazard)";
        case WET_ERR_COMPLIANCE_RAILED:
            return "WET_ERR_COMPLIANCE_RAILED: Stimulator output voltage saturated ASIC compliance rail (+/-7.0 V)";
        case WET_ERR_BYTECODE_VERIFICATION:
            return "WET_ERR_BYTECODE_VERIFICATION: WBC binary failed static bytecode verifier checks";
        case WET_ERR_QUEUE_EMPTY:
            return "WET_ERR_QUEUE_EMPTY: Telemetry or command queue is empty";
        default:
            return "WET_ERR_UNKNOWN: Unknown error status";
    }
}

/* =========================================================================
 * Phase 3 Hardware Readiness & Safety Implementations
 * ========================================================================= */

WET_EXPORT void wet_configure_electrode(wet_vm_t* vm, uint8_t material, float area_um2) {
    if (!vm) return;
    interlocks_configure_electrode(&vm->interlocks, material, area_um2);
}

WET_EXPORT void wet_active_discharge(wet_vm_t* vm, uint8_t channel) {
    if (!vm || channel >= BIO_NUM_CHANNELS) return;

    wet_hal_status_t hal_st = WET_HAL_OK;
    if (vm->hal != NULL) {
        hal_st = wet_hal_active_discharge(vm->hal, (uint16_t)channel);
    }

    bio_stim_pulse_t* p = &vm->bio.stim_pulses[channel];
    p->active = 0;
    p->phase1_ticks_left = 0;
    p->interphase_ticks_left = 0;
    p->phase2_ticks_left = 0;
    p->voltage_v = 0.0f;
    p->phase1_amp_v = 0.0f;
    p->phase2_amp_v = 0.0f;
    vm->bio.ext_stim_v[channel] = 0.0f;
    vm->bio.tick_charge_nc[channel] = 0.0f;
    vm->bio.last_stim_current_ua[channel] = 0.0f;

    if (vm->bio.stim_blanking_ticks[channel] < vm->bio.default_blanking_ticks) {
        vm->bio.stim_blanking_ticks[channel] = vm->bio.default_blanking_ticks;
    }

    if (hal_st == WET_HAL_OK) {
        vm->bio.v_double_layer_v[channel] = 0.0f;
    }

    interlocks_active_discharge(&vm->interlocks, channel);
    vm->voltages[channel] = 0.0f;
    vm->last_charge_nc[channel] = 0.0f;
    vm->discharge_charge_nc[channel] = 0.0f;
}

WET_EXPORT void wet_active_discharge_all(wet_vm_t* vm) {
    if (!vm) return;
    for (uint8_t ch = 0; ch < BIO_NUM_CHANNELS; ++ch) {
        wet_active_discharge(vm, ch);
    }
}

WET_EXPORT void wet_enable_dead_head_protection(wet_vm_t* vm, uint8_t enable) {
    if (!vm) return;
    interlocks_enable_dead_head_protection(&vm->interlocks, enable);
}

WET_EXPORT void wet_life_supervisor_shutdown(wet_vm_t* vm) {
    if (!vm) return;
    vm->life_supervisor.supervisor_active = 0;
    for (int p = 0; p < 8; ++p) {
        vm->pump_rates_ul_min[p] = 0.0f;
    }
}

WET_EXPORT void wet_configure_blanking(wet_vm_t* vm, float blanking_ms, uint8_t enable_spatial) {
    if (!vm) return;
    biophysics_set_blanking_window(&vm->bio, blanking_ms, enable_spatial);
}

WET_EXPORT wet_status_t wet_inject_current_stimulus(
    wet_vm_t* vm,
    uint8_t channel,
    float current_ua,
    float phase1_ms,
    float phase2_ms
) {
    if (!vm) return WET_ERR_NULL_PTR;
    if (channel >= vm->config.channel_count) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Channel %u out of bounds (max %u)", channel, vm->config.channel_count);
        return WET_ERR_OUT_OF_BOUNDS_CH;
    }
    if (vm->interlocks.locked) {
        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
        return WET_ERR_INTERLOCK_LOCKED;
    }

    if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_CURRENT, 0.0f, channel)) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Capability denied for wet_inject_current_stimulus on ch %u", channel);
        return WET_ERR_CAPABILITY_DENIED;
    }

    /* Randles Interface check: V_elec = I * Rs + V_dl */
    float v_elec = (current_ua / 1000.0f) * vm->bio.r_solution_kohm + vm->bio.v_double_layer_v[channel];
    wet_status_t comp_st = interlocks_check_compliance(&vm->interlocks, vm->current_tick, channel, v_elec);
    if (comp_st != WET_OK) {
        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
        return comp_st;
    }

    /* Dynamic EIS Faradaic Current Density Clamp when channel impedance is calibrated */
    if (channel < INTERLOCK_NUM_CHANNELS &&
        vm->interlocks.impedance[channel].z_magnitude_ohms > 0.0f &&
        vm->interlocks.max_faradaic_current_density_ua_cm2 > 0.0f) {
        float area_um2 = (vm->interlocks.electrode_area_um2 > 0.0f) ? vm->interlocks.electrode_area_um2 : 5000.0f;
        float i_safe_ua = vm->interlocks.max_faradaic_current_density_ua_cm2 * (area_um2 * 1e-8f);
        if (i_safe_ua > 0.0f && fabsf(current_ua) > i_safe_ua) {
            float sign = (current_ua >= 0.0f) ? 1.0f : -1.0f;
            current_ua = sign * i_safe_ua;
            vm->interlocks.clamp_events++;
            vm->interlocks.dynamic_impedance_clamp_events++;
            v_elec = (current_ua / 1000.0f) * vm->bio.r_solution_kohm + vm->bio.v_double_layer_v[channel];
        }
    }

    /* Shannon charge density limit */
    if (phase1_ms > 0.0f && phase2_ms > 0.0f) {
        float q_p1 = fabsf(current_ua) * 1e-3f * phase1_ms;
        float q_p2 = fabsf(current_ua) * 1e-3f * phase2_ms;
        if (q_p1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_p2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
            vm->interlocks.locked = 1;
            vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
            vm->interlocks.tripped_channel = channel;
            vm->interlocks.trip_tick = vm->current_tick;
            vm->interlocks.trip_value = q_p1 > q_p2 ? q_p1 : q_p2;
            snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
                     "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
                     channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
            snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
            return WET_ERR_CHARGE_DENSITY_EXCEEDED;
        }
    }

    biophysics_schedule_stim_current(&vm->bio, channel, current_ua, phase1_ms, phase2_ms, 0.0f);
    vm->voltages[channel] = v_elec;
    vm->last_charge_nc[channel] = (current_ua * 1e-3f) * (phase1_ms - phase2_ms);
    return WET_OK;
}

WET_EXPORT wet_status_t wet_verify_bytecode(
    const uint8_t* bytecode,
    size_t size,
    char* err_buf,
    size_t err_buf_len
) {
    return wet_verify_bytecode_internal(bytecode, size, err_buf, err_buf_len);
}

WET_EXPORT wet_status_t wet_vm_snapshot(
    const wet_vm_t* vm,
    uint8_t* buffer,
    size_t* inout_len
) {
    return wet_vm_snapshot_internal(vm, buffer, inout_len);
}

WET_EXPORT wet_status_t wet_vm_restore(
    wet_vm_t* vm,
    const uint8_t* buffer,
    size_t len
) {
    return wet_vm_restore_internal(vm, buffer, len);
}

WET_EXPORT void wet_set_environmental_sensors(
    wet_vm_t* vm,
    float ph,
    float do_pct,
    float co2_pct,
    uint8_t bubble_sensor_id,
    uint8_t bubble_state,
    float flow_rate_ul_min
) {
    if (!vm) return;
    if (ph > 0.0f) vm->ph_level = ph;
    if (do_pct > 0.0f) vm->dissolved_oxygen_pct = do_pct;
    if (co2_pct > 0.0f) vm->dissolved_co2_pct = co2_pct;
    if (bubble_sensor_id < 8) {
        vm->bubble_detected[bubble_sensor_id] = bubble_state ? 1 : 0;
        vm->fluid_flow_rate_ul_min[bubble_sensor_id] = flow_rate_ul_min;
    }
}

WET_EXPORT void wet_set_temperature(
    wet_vm_t* vm,
    float temp_c
) {
    if (!vm) return;
    vm->ambient_temperature_c = temp_c;
}

WET_EXPORT void wet_set_channel_banks(
    wet_vm_t* vm,
    uint64_t ref_mask,
    uint64_t rec_mask
) {
    if (!vm) return;
    interlocks_set_channel_banks(&vm->interlocks, ref_mask, rec_mask);
}

WET_EXPORT wet_status_t wet_vm_get_synapse_matrix(
    const wet_vm_t* vm,
    float* out_matrix,
    size_t out_capacity_floats
) {
    if (!vm || !out_matrix) return WET_ERR_NULL_PTR;
    if (out_capacity_floats < (size_t)(BIO_NUM_NEURONS * BIO_NUM_NEURONS)) {
        return WET_ERR_OUT_OF_BOUNDS_CH;
    }
    for (size_t i = 0; i < BIO_NUM_NEURONS; ++i) {
        for (size_t j = 0; j < BIO_NUM_NEURONS; ++j) {
            if (vm->bio.synapses[i][j].exists) {
                out_matrix[i * BIO_NUM_NEURONS + j] = vm->bio.synapses[i][j].weight_ns;
            } else {
                out_matrix[i * BIO_NUM_NEURONS + j] = 0.0f;
            }
        }
    }
    return WET_OK;
}

WET_EXPORT float wet_vm_get_synapse_weight(
    const wet_vm_t* vm,
    uint8_t pre,
    uint8_t post
) {
    if (!vm || pre >= BIO_NUM_NEURONS || post >= BIO_NUM_NEURONS) return 0.0f;
    return biophysics_get_weight(&vm->bio, pre, post);
}

WET_EXPORT float wet_clamp_voltage_vm(wet_vm_t* vm, float requested_v) {
    if (!vm) return requested_v;
    return interlocks_clamp_voltage(&vm->interlocks, requested_v);
}

WET_EXPORT void wet_set_electrode_impedance(
    wet_vm_t* vm,
    uint8_t channel,
    float z_magnitude_ohms,
    float z_phase_rad,
    uint64_t tick
) {
    if (!vm) return;
    interlocks_set_electrode_impedance(&vm->interlocks, channel, z_magnitude_ohms, z_phase_rad, tick);
}

WET_EXPORT void wet_set_current_density_limit(wet_vm_t* vm, float max_ua_cm2) {
    if (!vm) return;
    interlocks_set_current_density_limit(&vm->interlocks, max_ua_cm2);
}

WET_EXPORT float wet_clamp_voltage_dynamic_vm(wet_vm_t* vm, uint8_t channel, float requested_v) {
    if (!vm) return requested_v;
    return interlocks_clamp_voltage_dynamic(&vm->interlocks, channel, requested_v);
}
