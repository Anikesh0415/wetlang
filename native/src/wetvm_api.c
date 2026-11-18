#ifndef WET_BUILDING_DLL
#define WET_BUILDING_DLL
#endif

#include "../include/wet_crt.h"
#include "../include/wetvm_types.h"
#include "../include/wetvm_api.h"
#include "../include/wetvm_vm.h"

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

WET_EXPORT wet_vm_t* wet_create_vm(const wet_vm_config_t* config) {
    struct wet_vm_instance* vm = (struct wet_vm_instance*)calloc(1, sizeof(struct wet_vm_instance));
    if (!vm) return NULL;

    /* Apply configuration with sensible defaults */
    if (config) {
        vm->config.dt_ms = (config->dt_ms > 0.0) ? config->dt_ms : 0.1;
        vm->config.max_stack_depth = (config->max_stack_depth > 0) ? config->max_stack_depth : 1024;
        vm->config.max_locals = (config->max_locals > 0) ? config->max_locals : 256;
        vm->config.channel_count = (config->channel_count > 0 && config->channel_count <= 64)
                                    ? config->channel_count : 64;
    } else {
        vm->config.dt_ms = 0.1;
        vm->config.max_stack_depth = 1024;
        vm->config.max_locals = 256;
        vm->config.channel_count = 64;
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

    biophysics_init(&vm->bio, vm->config.dt_ms, 0);
    interlocks_init(&vm->interlocks);

    return vm;
}

WET_EXPORT void wet_free_vm(wet_vm_t* vm) {
    if (!vm) return;

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

    float clamped_v = interlocks_clamp_voltage(&vm->interlocks, voltage_v);
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
        default:
            return "WET_ERR_UNKNOWN: Unknown error status";
    }
}
