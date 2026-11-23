#include "../include/wet_crt.h"
#include "../include/wetvm_types.h"
#include "../include/wetvm_api.h"
#include "../include/wetvm_vm.h"
#include "../include/wet_hal.h"

/* Unaligned Little-Endian Memory Readers (prevents hardware faults on ARM/RISC-V) */
static inline uint16_t wet_read_u16_le(const void* p) {
    uint16_t val;
    memcpy(&val, p, sizeof(val));
    return val;
}
static inline int16_t wet_read_i16_le(const void* p) {
    int16_t val;
    memcpy(&val, p, sizeof(val));
    return val;
}
static inline uint32_t wet_read_u32_le(const void* p) {
    uint32_t val;
    memcpy(&val, p, sizeof(val));
    return val;
}
static inline int32_t wet_read_i32_le(const void* p) {
    int32_t val;
    memcpy(&val, p, sizeof(val));
    return val;
}
static inline float wet_read_f32_le(const void* p) {
    float val;
    memcpy(&val, p, sizeof(val));
    return val;
}

/* =========================================================================
 * IEEE 802.3 CRC32 Implementation
 * ========================================================================= */

uint32_t wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc) {
    uint32_t crc = ~initial_crc;
    for (size_t i = 0; i < length; ++i) {
        crc ^= data[i];
        for (int k = 0; k < 8; ++k) {
            crc = (crc >> 1) ^ (0xEDB88320u & -(int32_t)(crc & 1));
        }
    }
    return ~crc;
}

/* =========================================================================
 * Stack Management Helpers
 * ========================================================================= */

static inline wet_status_t push_val(struct wet_vm_instance* vm, wet_value_t val) {
    if (vm->sp >= vm->max_stack) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Operand stack overflow (limit %u reached)", (unsigned)vm->max_stack);
        return WET_ERR_STACK_OVERFLOW;
    }
    vm->stack[vm->sp++] = val;
    return WET_OK;
}

static inline wet_status_t pop_val(struct wet_vm_instance* vm, wet_value_t* out_val) {
    if (vm->sp == 0) {
        snprintf(vm->last_error, sizeof(vm->last_error), "Operand stack underflow");
        return WET_ERR_STACK_UNDERFLOW;
    }
    *out_val = vm->stack[--vm->sp];
    return WET_OK;
}

static inline float to_float(const wet_value_t* v) {
    if (v->type == WET_VAL_FLOAT) {
        return v->as.f_val;
    }
    if (v->type == WET_VAL_INT) {
        return (float)v->as.i_val;
    }
    return 0.0f;
}

static inline int32_t to_int(const wet_value_t* v) {
    if (v->type == WET_VAL_INT) {
        return v->as.i_val;
    }
    if (v->type == WET_VAL_FLOAT) {
        return (int32_t)v->as.f_val;
    }
    return 0;
}

static inline int is_truthy(const wet_value_t* v) {
    if (v->type == WET_VAL_INT) {
        return v->as.i_val != 0;
    }
    if (v->type == WET_VAL_FLOAT) {
        return v->as.f_val != 0.0f;
    }
    if (v->type == WET_VAL_STRING) {
        return v->as.s_val.len > 0;
    }
    return 0;
}

/* =========================================================================
 * Bytecode Loading and Verification
 * ========================================================================= */

static void cleanup_constants(struct wet_vm_instance* vm) {
    if (vm->constants) {
        for (size_t i = 0; i < vm->num_constants; ++i) {
            if (vm->constants[i].str_alloc) {
                free(vm->constants[i].str_alloc);
                vm->constants[i].str_alloc = NULL;
            }
        }
        free(vm->constants);
        vm->constants = NULL;
        vm->num_constants = 0;
    }
}

static void cleanup_bytecode(struct wet_vm_instance* vm) {
    cleanup_constants(vm);
    if (vm->bytecode_raw) {
        free(vm->bytecode_raw);
        vm->bytecode_raw = NULL;
        vm->bytecode_size = 0;
    }
    vm->code = NULL;
    vm->code_size = 0;
}

wet_status_t wet_vm_load_bytecode_internal(
    struct wet_vm_instance* vm,
    const uint8_t* code_bytes,
    size_t size,
    char* err_buf,
    size_t err_buf_len
) {
    if (!vm || !code_bytes) {
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "Null pointer argument to wet_load_bytecode");
        }
        return WET_ERR_NULL_PTR;
    }

    if (size < WET_HEADER_SIZE) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Bytecode binary truncated: size %zu < header size %d", size, WET_HEADER_SIZE);
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "%s", vm->last_error);
        }
        return WET_ERR_MALFORMED_SECTION;
    }

    const wet_bytecode_header_t* hdr = (const wet_bytecode_header_t*)code_bytes;

    /* 1. Verify Magic "WETB" */
    if (hdr->magic[0] != 'W' || hdr->magic[1] != 'E' ||
        hdr->magic[2] != 'T' || hdr->magic[3] != 'B') {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Invalid magic 0x%02X%02X%02X%02X (expected 'WETB')",
                 hdr->magic[0], hdr->magic[1], hdr->magic[2], hdr->magic[3]);
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "%s", vm->last_error);
        }
        return WET_ERR_INVALID_MAGIC;
    }

    /* 2. Verify Version */
    if (hdr->version_major != WET_VERSION_MAJOR || hdr->version_minor != WET_VERSION_MINOR) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Unsupported bytecode version %u.%u (expected %u.%u)",
                 hdr->version_major, hdr->version_minor,
                 WET_VERSION_MAJOR, WET_VERSION_MINOR);
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "%s", vm->last_error);
        }
        return WET_ERR_UNSUPPORTED_VERSION;
    }

    /* 3. Verify File Size */
    if (hdr->file_size != size) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "File size mismatch: header reports %u bytes, got %zu bytes",
                 hdr->file_size, size);
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "%s", vm->last_error);
        }
        return WET_ERR_MALFORMED_SECTION;
    }

    /* 4. Verify CRC32 Checksum (computed with CRC field at offset 12 zeroed) */
    uint32_t expected_crc = hdr->checksum_crc32;
    uint32_t calc_crc = wet_compute_crc32(code_bytes, 12, 0);
    uint8_t zero_field[4] = {0, 0, 0, 0};
    calc_crc = wet_compute_crc32(zero_field, 4, calc_crc);
    if (size > 16) {
        calc_crc = wet_compute_crc32(code_bytes + 16, size - 16, calc_crc);
    }

    if (calc_crc != expected_crc) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "CRC32 mismatch: header has 0x%08X, calculated 0x%08X",
                 expected_crc, calc_crc);
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "%s", vm->last_error);
        }
        return WET_ERR_CRC_MISMATCH;
    }

    /* 4b. Anti-Rollback Monotonic Sequence Verification */
    if (vm->config.min_sequence_counter > 0 && hdr->sequence_counter < vm->config.min_sequence_counter) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Anti-rollback security violation: binary sequence counter %u is below required hardware minimum %u",
                 hdr->sequence_counter, vm->config.min_sequence_counter);
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "%s", vm->last_error);
        }
        return WET_ERR_CAPABILITY_DENIED;
    }

    /* 5. Validate Section Table Bounds */
    size_t sec_table_size = (size_t)hdr->num_sections * WET_SECTION_ENTRY_SIZE;
    if (WET_HEADER_SIZE + sec_table_size > size) {
        snprintf(vm->last_error, sizeof(vm->last_error),
                 "Section table exceeds file boundary (%u sections)", hdr->num_sections);
        if (err_buf && err_buf_len > 0) {
            snprintf(err_buf, err_buf_len, "%s", vm->last_error);
        }
        return WET_ERR_MALFORMED_SECTION;
    }

    /* Clean up previous bytecode and allocate buffer for new bytecode */
    cleanup_bytecode(vm);
    vm->bytecode_raw = (uint8_t*)malloc(size);
    if (!vm->bytecode_raw) {
        snprintf(vm->last_error, sizeof(vm->last_error), "Memory allocation failed for bytecode");
        return WET_ERR_ALLOC_FAILED;
    }
    memcpy(vm->bytecode_raw, code_bytes, size);
    vm->bytecode_size = size;

    /* Parse Section Table */
    const wet_section_header_t* sections =
        (const wet_section_header_t*)(vm->bytecode_raw + WET_HEADER_SIZE);

    const uint8_t* code_ptr = NULL;
    size_t code_len = 0;

    for (uint32_t i = 0; i < hdr->num_sections; ++i) {
        uint16_t stype = sections[i].section_type;
        uint32_t off = sections[i].offset;
        uint32_t s_size = sections[i].size;

        if ((size_t)off + s_size > size) {
            snprintf(vm->last_error, sizeof(vm->last_error),
                     "Section %u (type %u) extends beyond file boundary", i, stype);
            cleanup_bytecode(vm);
            return WET_ERR_MALFORMED_SECTION;
        }

        const uint8_t* sec_data = vm->bytecode_raw + off;

        if (stype == WET_SEC_CONSTANT_POOL) {
            /* Unpack Constant Pool */
            if (s_size < 4) {
                snprintf(vm->last_error, sizeof(vm->last_error), "Constant pool truncated");
                cleanup_bytecode(vm);
                return WET_ERR_MALFORMED_SECTION;
            }
            uint32_t num_consts = wet_read_u32_le(sec_data);
            size_t c_pos = 4;

            vm->constants = (wet_constant_entry_t*)calloc(num_consts, sizeof(wet_constant_entry_t));
            if (!vm->constants && num_consts > 0) {
                cleanup_bytecode(vm);
                return WET_ERR_ALLOC_FAILED;
            }
            vm->num_constants = num_consts;

            for (uint32_t c = 0; c < num_consts; ++c) {
                if (c_pos >= s_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Constant pool out of data");
                    cleanup_bytecode(vm);
                    return WET_ERR_MALFORMED_SECTION;
                }
                uint8_t tag = sec_data[c_pos++];
                vm->constants[c].val.type = tag;

                if (tag == WET_VAL_INT) {
                    if (c_pos + 4 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
                    vm->constants[c].val.as.i_val = wet_read_i32_le(sec_data + c_pos);
                    c_pos += 4;
                } else if (tag == WET_VAL_FLOAT) {
                    if (c_pos + 4 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
                    vm->constants[c].val.as.f_val = wet_read_f32_le(sec_data + c_pos);
                    c_pos += 4;
                } else if (tag == WET_VAL_STRING) {
                    if (c_pos + 2 > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
                    uint16_t str_len = wet_read_u16_le(sec_data + c_pos);
                    c_pos += 2;
                    if (c_pos + str_len > s_size) { cleanup_bytecode(vm); return WET_ERR_MALFORMED_SECTION; }
                    char* sbuf = (char*)malloc(str_len + 1);
                    if (!sbuf) { cleanup_bytecode(vm); return WET_ERR_ALLOC_FAILED; }
                    memcpy(sbuf, sec_data + c_pos, str_len);
                    sbuf[str_len] = '\0';
                    vm->constants[c].str_alloc = sbuf;
                    vm->constants[c].val.as.s_val.str = sbuf;
                    vm->constants[c].val.as.s_val.len = str_len;
                    c_pos += str_len;
                }
            }
        } else if (stype == WET_SEC_TOPOLOGY_CONFIG) {
            if (s_size >= 8) {
                /* struct: channels (uint32), rows (uint16), cols (uint16) */
                vm->grid_rows = (uint8_t)wet_read_u16_le(sec_data + 4);
                vm->grid_cols = (uint8_t)wet_read_u16_le(sec_data + 6);
            }
        } else if (stype == WET_SEC_BYTECODE_STREAM) {
            code_ptr = sec_data;
            code_len = s_size;
        }
    }

    if (!code_ptr && code_len == 0) {
        /* Bytecode section might be empty */
        vm->code = vm->bytecode_raw;
        vm->code_size = 0;
    } else {
        vm->code = code_ptr;
        vm->code_size = code_len;
    }

    /* Reset registers and runtime state */
    vm->pc = 0;
    vm->sp = 0;
    vm->call_sp = 0;
    vm->is_halted = 0;
    vm->is_finished = 0;
    vm->sleep_ticks_remaining = 0;
    vm->current_tick = 0;
    vm->sim_time_ms = 0.0;
    vm->last_error[0] = '\0';

    vm->loaded_capabilities = hdr->capabilities;
    biophysics_reset(&vm->bio);
    interlocks_init(&vm->interlocks);
    interlocks_set_capabilities(&vm->interlocks, hdr->capabilities, hdr->channel_count);
    memset(vm->discharge_charge_nc, 0, sizeof(vm->discharge_charge_nc));

    /* Clear local variables */
    if (vm->locals) {
        memset(vm->locals, 0, sizeof(wet_value_t) * vm->max_locals);
    }

    /* Clear channel outputs */
    memset(vm->voltages, 0, sizeof(vm->voltages));
    memset(vm->spikes, 0, sizeof(vm->spikes));
    memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
    vm->population_rate_hz = 0.0f;

    return WET_OK;
}

/* =========================================================================
 * Telemetry Snapshot Population
 * ========================================================================= */

static void populate_telemetry(const struct wet_vm_instance* vm, wet_telemetry_t* telem) {
    if (!telem) return;
    telem->current_tick = vm->current_tick;
    telem->sim_time_ms = vm->sim_time_ms;
    telem->population_rate_hz = vm->population_rate_hz;
    memcpy(telem->voltages, vm->voltages, sizeof(float) * 64);
    memcpy(telem->spikes, vm->spikes, sizeof(uint8_t) * 64);
    memcpy(telem->last_charge_nc, vm->last_charge_nc, sizeof(float) * 64);
}

static wet_status_t advance_simulation_tick(struct wet_vm_instance* vm, wet_telemetry_t* out_telem) {
    if (vm->interlocks.locked) {
        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
        return WET_ERR_INTERLOCK_LOCKED;
    }

    /* Dead-heading valve-pump overpressure check */
    if (vm->interlocks.dead_head_protection_enabled) {
        for (int p = 0; p < 8; ++p) {
            if (vm->pump_rates_ul_min[p] > 0.0f) {
                uint8_t v = vm->interlocks.pump_valve_mapping[p];
                if (v < 8 && vm->valve_states[v] == 0) {
                    vm->interlocks.locked = 1;
                    vm->interlocks.trip_reason = INTERLOCK_TRIP_DEAD_HEAD_PRESSURE;
                    if (vm->hal) {
                        wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_DEAD_HEAD_PRESSURE);
                    }
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "ERR_DEAD_HEAD_OVERPRESSURE: Pump %d active at %.2f uL/min while downstream valve %d is closed",
                             p, (double)vm->pump_rates_ul_min[p], v);
                    return WET_ERR_ACTUATOR_FAULT;
                }
            }
        }
    }

    /* Phase 3 Environmental Checks: Thermal Limit (CMOS heating) & Bubble Detection */
    if (vm->ambient_temperature_c > INTERLOCK_THERMAL_LIMIT_C) {
        wet_status_t th_st = interlocks_check_thermal(&vm->interlocks, vm->current_tick, vm->ambient_temperature_c);
        if (th_st != WET_OK) {
            biophysics_zero_all_stim(&vm->bio);
            vm->is_halted = 1;
            if (vm->hal) {
                wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
            }
            snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
            populate_telemetry(vm, out_telem);
            return th_st;
        }
    }

    for (int b = 0; b < 8; ++b) {
        if (vm->bubble_detected[b]) {
            wet_status_t bub_st = interlocks_check_bubble(&vm->interlocks, vm->current_tick, 1, (uint8_t)b);
            if (bub_st != WET_OK) {
                for (int p = 0; p < 8; ++p) vm->pump_rates_ul_min[p] = 0.0f;
                biophysics_zero_all_stim(&vm->bio);
                vm->is_halted = 1;
                if (vm->hal) {
                    wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
                }
                snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
                populate_telemetry(vm, out_telem);
                return bub_st;
            }
        }
    }

    /* 1. Advance in-silico biophysics by 1 tick (dt = 0.1 ms) */
    biophysics_step_tick(&vm->bio);
    for (int ch = 0; ch < 64; ++ch) {
        if (vm->discharge_charge_nc[ch] != 0.0f) {
            vm->bio.tick_charge_nc[ch] += vm->discharge_charge_nc[ch];
            vm->discharge_charge_nc[ch] = 0.0f;
        }
    }
    vm->current_tick++;
    vm->sim_time_ms = (double)vm->current_tick * vm->config.dt_ms;
    vm->sim_time_us = (int64_t)((double)vm->current_tick * vm->config.dt_ms * 1000.0 + 0.5);

    /* 2. Check sliding charge balance watchdog */
    wet_status_t il_st = interlocks_record_charge_tick(
        &vm->interlocks, vm->current_tick, vm->bio.tick_charge_nc
    );
    if (il_st != WET_OK) {
        biophysics_zero_all_stim(&vm->bio);
        memset(vm->voltages, 0, sizeof(vm->voltages));
        memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
        memset(vm->bio.ext_stim_v, 0, sizeof(vm->bio.ext_stim_v));
        memset(vm->bio.mea_voltage_v, 0, sizeof(vm->bio.mea_voltage_v));
        memset(vm->bio.tick_charge_nc, 0, sizeof(vm->bio.tick_charge_nc));
        vm->is_halted = 1;
        if (vm->hal) {
            wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
        }
        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
        populate_telemetry(vm, out_telem);
        return il_st;
    }

    /* 3. Check epileptiform runaway breaker */
    il_st = interlocks_check_epileptiform(
        &vm->interlocks, vm->current_tick, vm->bio.channel_rate_hz
    );
    if (il_st != WET_OK) {
        biophysics_zero_all_stim(&vm->bio);
        memset(vm->voltages, 0, sizeof(vm->voltages));
        memset(vm->last_charge_nc, 0, sizeof(vm->last_charge_nc));
        memset(vm->bio.ext_stim_v, 0, sizeof(vm->bio.ext_stim_v));
        memset(vm->bio.mea_voltage_v, 0, sizeof(vm->bio.mea_voltage_v));
        memset(vm->bio.tick_charge_nc, 0, sizeof(vm->bio.tick_charge_nc));
        vm->is_halted = 1;
        if (vm->hal) {
            wet_hal_emergency_crowbar(vm, vm->interlocks.trip_reason);
        }
        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
        populate_telemetry(vm, out_telem);
        return il_st;
    }

    /* 4. Sync outputs to VM registers & telemetry snapshot */
    memcpy(vm->voltages, vm->bio.mea_voltage_v, sizeof(float) * 64);
    memcpy(vm->spikes, vm->bio.spikes_now, sizeof(uint8_t) * 64);
    memcpy(vm->last_charge_nc, vm->bio.tick_charge_nc, sizeof(float) * 64);
    vm->population_rate_hz = vm->bio.population_rate_hz;

    populate_telemetry(vm, out_telem);
    return WET_OK;
}

/* =========================================================================
 * Cycle-Accurate Execution Stepper
 * ========================================================================= */

wet_status_t wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem) {
    if (!vm) return WET_ERR_NULL_PTR;

    if (vm->interlocks.locked) {
        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
        return WET_ERR_INTERLOCK_LOCKED;
    }

    if (vm->is_halted) {
        if (vm->life_supervisor.supervisor_active) {
            /* Ring-0 Life Support Supervisor: Maintain baseline nutrient perfusion & temperature */
            for (int p = 0; p < 8; ++p) {
                if (vm->pump_rates_ul_min[p] == 0.0f) {
                    vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
                }
            }
            vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
            vm->life_supervisor.ticks_under_supervisor++;
        }
        snprintf(vm->last_error, sizeof(vm->last_error), "VM is halted");
        return WET_ERR_HALTED;
    }

    /* If bytecode execution has finished or reached end, continue free-running biological stepping */
    if (vm->is_finished || vm->pc >= vm->code_size) {
        if (vm->life_supervisor.supervisor_active) {
            for (int p = 0; p < 8; ++p) {
                if (vm->pump_rates_ul_min[p] == 0.0f) {
                    vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
                }
            }
            vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
            vm->life_supervisor.ticks_under_supervisor++;
        }
        return advance_simulation_tick(vm, out_telem);
    }

    /* Handle ongoing SLEEP_TICKS decrement */
    if (vm->sleep_ticks_remaining > 0) {
        vm->sleep_ticks_remaining--;
        return advance_simulation_tick(vm, out_telem);
    }

    /* Dispatch instructions until a tick yield (SYNC_TICK, SLEEP_TICKS, HALT) */
    uint32_t instr_count = 0;
    uint32_t max_ops = vm->config.max_ops_per_tick ? vm->config.max_ops_per_tick : 100000U;
    while (!vm->is_halted && !vm->is_finished) {
        if (++instr_count > max_ops) {
            biophysics_zero_all_stim(&vm->bio);
            vm->interlocks.locked = 1;
            vm->interlocks.trip_reason = INTERLOCK_TRIP_CAPABILITY_VIOLATION;
            if (max_ops == 100000U) {
                snprintf(vm->last_error, sizeof(vm->last_error),
                         "WET_ERR_WATCHDOG_TIMEOUT: Exceeded 100,000 instructions in a single tick");
            } else {
                snprintf(vm->last_error, sizeof(vm->last_error),
                         "WET_ERR_WATCHDOG_TIMEOUT: Exceeded %u instructions in a single tick", max_ops);
            }
            return WET_ERR_WATCHDOG_TIMEOUT;
        }

        if (vm->pc >= vm->code_size) {
            /* End of bytecode reached: advance simulation tick */
            vm->is_finished = 1;
            return advance_simulation_tick(vm, out_telem);
        }

        size_t instr_pc = vm->pc;
        uint8_t op = vm->code[instr_pc];

        switch ((wet_opcode_t)op) {
            case WET_OP_NOP: {
                vm->pc = instr_pc + 1;
                break;
            }

            case WET_OP_HALT: {
                vm->is_finished = 1;
                vm->pc = instr_pc + 1;
                if (vm->life_supervisor.supervisor_active) {
                    for (int p = 0; p < 8; ++p) {
                        if (vm->pump_rates_ul_min[p] == 0.0f) {
                            vm->pump_rates_ul_min[p] = vm->life_supervisor.maintenance_perfusion_ul_min[p];
                        }
                    }
                    vm->ambient_temperature_c = vm->life_supervisor.maintenance_temperature_c;
                    vm->life_supervisor.ticks_under_supervisor++;
                }
                return advance_simulation_tick(vm, out_telem);
            }

            case WET_OP_SYNC_TICK: {
                vm->pc = instr_pc + 1;
                return advance_simulation_tick(vm, out_telem);
            }

            case WET_OP_SLEEP_TICKS: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated SLEEP_TICKS operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint16_t ticks = wet_read_u16_le(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 3;

                if (ticks > 1) {
                    vm->sleep_ticks_remaining = ticks - 1;
                }
                return advance_simulation_tick(vm, out_telem);
            }

            case WET_OP_PUSH_CONST: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_CONST operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint16_t idx = wet_read_u16_le(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 3;
                if (idx >= vm->num_constants) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Constant pool index %u out of range (%zu)", idx, vm->num_constants);
                    return WET_ERR_INVALID_OPCODE;
                }
                wet_status_t st = push_val(vm, vm->constants[idx].val);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_PUSH_INT: {
                if (instr_pc + 5 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_INT operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                int32_t val = wet_read_i32_le(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 5;
                wet_value_t v;
                v.type = WET_VAL_INT;
                v.as.i_val = val;
                wet_status_t st = push_val(vm, v);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_PUSH_FLOAT: {
                if (instr_pc + 5 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUSH_FLOAT operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                float val = wet_read_f32_le(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 5;
                wet_value_t v;
                v.type = WET_VAL_FLOAT;
                v.as.f_val = val;
                wet_status_t st = push_val(vm, v);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_POP: {
                vm->pc = instr_pc + 1;
                wet_value_t dummy;
                wet_status_t st = pop_val(vm, &dummy);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_DUP: {
                vm->pc = instr_pc + 1;
                if (vm->sp == 0) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Operand stack underflow on DUP");
                    return WET_ERR_STACK_UNDERFLOW;
                }
                wet_value_t top = vm->stack[vm->sp - 1];
                wet_status_t st = push_val(vm, top);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_SWAP: {
                vm->pc = instr_pc + 1;
                if (vm->sp < 2) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Operand stack underflow on SWAP");
                    return WET_ERR_STACK_UNDERFLOW;
                }
                wet_value_t a = vm->stack[vm->sp - 1];
                vm->stack[vm->sp - 1] = vm->stack[vm->sp - 2];
                vm->stack[vm->sp - 2] = a;
                break;
            }

            case WET_OP_LOAD_LOCAL: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated LOAD_LOCAL operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint16_t slot = wet_read_u16_le(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 3;
                if (slot >= vm->max_locals) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Local slot %u out of bounds (%zu)", slot, vm->max_locals);
                    return WET_ERR_INVALID_OPCODE;
                }
                wet_status_t st = push_val(vm, vm->locals[slot]);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_STORE_LOCAL: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STORE_LOCAL operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint16_t slot = wet_read_u16_le(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 3;
                if (slot >= vm->max_locals) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Local slot %u out of bounds (%zu)", slot, vm->max_locals);
                    return WET_ERR_INVALID_OPCODE;
                }
                wet_value_t val;
                wet_status_t st = pop_val(vm, &val);
                if (st != WET_OK) return st;
                vm->locals[slot] = val;
                break;
            }

            case WET_OP_ADD_I: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                wet_value_t res;
                res.type = WET_VAL_INT;
                res.as.i_val = to_int(&a) + to_int(&b);
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_SUB_I: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                wet_value_t res;
                res.type = WET_VAL_INT;
                res.as.i_val = to_int(&a) - to_int(&b);
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_MUL_I: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                wet_value_t res;
                res.type = WET_VAL_INT;
                res.as.i_val = to_int(&a) * to_int(&b);
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_DIV_I: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                int32_t b_val = to_int(&b);
                if (b_val == 0) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Integer division by zero");
                    return WET_ERR_DIVISION_BY_ZERO;
                }
                wet_value_t res;
                res.type = WET_VAL_INT;
                res.as.i_val = to_int(&a) / b_val;
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_ADD_F: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                wet_value_t res;
                res.type = WET_VAL_FLOAT;
                res.as.f_val = to_float(&a) + to_float(&b);
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_SUB_F: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                wet_value_t res;
                res.type = WET_VAL_FLOAT;
                res.as.f_val = to_float(&a) - to_float(&b);
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_MUL_F: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                wet_value_t res;
                res.type = WET_VAL_FLOAT;
                res.as.f_val = to_float(&a) * to_float(&b);
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_DIV_F: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                float b_val = to_float(&b);
                if (fabsf(b_val) < 1e-15f) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Floating point division by zero");
                    return WET_ERR_DIVISION_BY_ZERO;
                }
                wet_value_t res;
                res.type = WET_VAL_FLOAT;
                res.as.f_val = to_float(&a) / b_val;
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_NEG: {
                vm->pc = instr_pc + 1;
                wet_value_t a;
                wet_status_t st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                wet_value_t res;
                if (a.type == WET_VAL_FLOAT) {
                    res.type = WET_VAL_FLOAT;
                    res.as.f_val = -a.as.f_val;
                } else {
                    res.type = WET_VAL_INT;
                    res.as.i_val = -to_int(&a);
                }
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_MOD_I: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;
                int32_t b_val = to_int(&b);
                if (b_val == 0) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Integer modulo by zero");
                    return WET_ERR_DIVISION_BY_ZERO;
                }
                wet_value_t res;
                res.type = WET_VAL_INT;
                res.as.i_val = to_int(&a) % b_val;
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_CMP_EQ:
            case WET_OP_CMP_NE:
            case WET_OP_CMP_LT:
            case WET_OP_CMP_LE:
            case WET_OP_CMP_GT:
            case WET_OP_CMP_GE: {
                vm->pc = instr_pc + 1;
                wet_value_t b, a;
                wet_status_t st = pop_val(vm, &b);
                if (st != WET_OK) return st;
                st = pop_val(vm, &a);
                if (st != WET_OK) return st;

                int cmp_res = 0;
                if (a.type == WET_VAL_FLOAT || b.type == WET_VAL_FLOAT) {
                    float fa = to_float(&a);
                    float fb = to_float(&b);
                    switch ((wet_opcode_t)op) {
                        case WET_OP_CMP_EQ: cmp_res = (fa == fb); break;
                        case WET_OP_CMP_NE: cmp_res = (fa != fb); break;
                        case WET_OP_CMP_LT: cmp_res = (fa <  fb); break;
                        case WET_OP_CMP_LE: cmp_res = (fa <= fb); break;
                        case WET_OP_CMP_GT: cmp_res = (fa >  fb); break;
                        case WET_OP_CMP_GE: cmp_res = (fa >= fb); break;
                        default: break;
                    }
                } else {
                    int32_t ia = to_int(&a);
                    int32_t ib = to_int(&b);
                    switch ((wet_opcode_t)op) {
                        case WET_OP_CMP_EQ: cmp_res = (ia == ib); break;
                        case WET_OP_CMP_NE: cmp_res = (ia != ib); break;
                        case WET_OP_CMP_LT: cmp_res = (ia <  ib); break;
                        case WET_OP_CMP_LE: cmp_res = (ia <= ib); break;
                        case WET_OP_CMP_GT: cmp_res = (ia >  ib); break;
                        case WET_OP_CMP_GE: cmp_res = (ia >= ib); break;
                        default: break;
                    }
                }

                wet_value_t res;
                res.type = WET_VAL_INT;
                res.as.i_val = cmp_res ? 1 : 0;
                st = push_val(vm, res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_JMP: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
                int64_t target = (int64_t)instr_pc + offset;
                if (target < 0 || (size_t)target > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "JMP target %lld out of range", (long long)target);
                    return WET_ERR_INVALID_OPCODE;
                }
                vm->pc = (size_t)target;
                break;
            }

            case WET_OP_JMP_IF_TRUE: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP_IF_TRUE operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
                wet_value_t cond;
                wet_status_t st = pop_val(vm, &cond);
                if (st != WET_OK) return st;

                if (is_truthy(&cond)) {
                    int64_t target = (int64_t)instr_pc + offset;
                    if (target < 0 || (size_t)target > vm->code_size) {
                        snprintf(vm->last_error, sizeof(vm->last_error), "JMP_IF_TRUE target %lld out of range", (long long)target);
                        return WET_ERR_INVALID_OPCODE;
                    }
                    vm->pc = (size_t)target;
                } else {
                    vm->pc = instr_pc + 3;
                }
                break;
            }

            case WET_OP_JMP_IF_FALSE: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated JMP_IF_FALSE operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                int16_t offset = wet_read_i16_le(vm->code + instr_pc + 1);
                wet_value_t cond;
                wet_status_t st = pop_val(vm, &cond);
                if (st != WET_OK) return st;

                if (!is_truthy(&cond)) {
                    int64_t target = (int64_t)instr_pc + offset;
                    if (target < 0 || (size_t)target > vm->code_size) {
                        snprintf(vm->last_error, sizeof(vm->last_error), "JMP_IF_FALSE target %lld out of range", (long long)target);
                        return WET_ERR_INVALID_OPCODE;
                    }
                    vm->pc = (size_t)target;
                } else {
                    vm->pc = instr_pc + 3;
                }
                break;
            }

            case WET_OP_CALL: {
                if (instr_pc + 4 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated CALL operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint16_t fn_idx = wet_read_u16_le(vm->code + instr_pc + 1);
                uint8_t argc = *(const uint8_t*)(vm->code + instr_pc + 3);

                if (fn_idx > 0 && fn_idx < vm->code_size) {
                    /* User-defined function call */
                    if (vm->call_sp >= vm->max_call_depth) {
                        snprintf(vm->last_error, sizeof(vm->last_error), "Call stack overflow (depth %zu)", vm->call_sp);
                        return WET_ERR_STACK_OVERFLOW;
                    }
                    vm->call_stack[vm->call_sp++].return_pc = instr_pc + 4;
                    vm->pc = fn_idx;
                } else {
                    /* Handle builtin / external function call: pop arguments, push default 0 */
                    vm->pc = instr_pc + 4;
                    for (uint8_t a = 0; a < argc; ++a) {
                        wet_value_t dummy;
                        pop_val(vm, &dummy);
                    }
                    wet_value_t ret_val;
                    ret_val.type = WET_VAL_INT;
                    ret_val.as.i_val = 0;
                    push_val(vm, ret_val);
                }
                break;
            }

            case WET_OP_RET: {
                if (vm->call_sp > 0) {
                    vm->call_sp--;
                    vm->pc = vm->call_stack[vm->call_sp].return_pc;
                } else {
                    vm->pc = instr_pc + 1;
                }
                break;
            }

            case WET_OP_STIM_BIPHASIC: {
                if (instr_pc + 2 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STIM_BIPHASIC operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 2;

                /* Pop arguments: interphase, phase2, phase1, voltage */
                wet_value_t v_interphase, v_p2, v_p1, v_volt;
                wet_status_t st = pop_val(vm, &v_interphase);
                if (st != WET_OK) return st;
                st = pop_val(vm, &v_p2);
                if (st != WET_OK) return st;
                st = pop_val(vm, &v_p1);
                if (st != WET_OK) return st;
                st = pop_val(vm, &v_volt);
                if (st != WET_OK) return st;

                if (channel == 0xFF) {
                    /* Dynamic channel index popped from stack */
                    wet_value_t v_ch;
                    st = pop_val(vm, &v_ch);
                    if (st != WET_OK) return st;
                    int32_t c_idx = to_int(&v_ch);
                    if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
                        snprintf(vm->last_error, sizeof(vm->last_error),
                                 "Electrode channel %d out of bounds (max %u)",
                                 c_idx, vm->config.channel_count);
                        return WET_ERR_OUT_OF_BOUNDS_CH;
                    }
                    channel = (uint8_t)c_idx;
                } else if (channel >= vm->config.channel_count) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Electrode channel %u out of bounds (max %u)",
                             channel, vm->config.channel_count);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                float voltage = to_float(&v_volt);
                float p1_ms = to_float(&v_p1);
                float p2_ms = to_float(&v_p2);
                float ip_ms = to_float(&v_interphase);

                if (vm->interlocks.locked) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
                    return WET_ERR_INTERLOCK_LOCKED;
                }

                if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_BIPHASIC, voltage, channel)) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Capability denied for STIM_BIPHASIC on ch %u (req %.2fV)", channel, voltage);
                    return WET_ERR_CAPABILITY_DENIED;
                }

                /* Per-Phase Charge Density Limit (Shannon Model): prevent massive biphasic pulses with net=0 */
                if (p1_ms > 0.0f && p2_ms > 0.0f) {
                    float q_phase1 = (wet_fabsf(voltage) / vm->bio.electrode_impedance_kohm) * 1000.0f * p1_ms;
                    float q_phase2 = (wet_fabsf(voltage) / vm->bio.electrode_impedance_kohm) * 1000.0f * p2_ms;
                    if (q_phase1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_phase2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
                        vm->interlocks.locked = 1;
                        vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
                        vm->interlocks.tripped_channel = channel;
                        vm->interlocks.trip_tick = vm->current_tick;
                        vm->interlocks.trip_value = q_phase1 > q_phase2 ? q_phase1 : q_phase2;
                        if (vm->hal) {
                            wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_CHARGE_DENSITY);
                        }
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

                float clamped_v = interlocks_clamp_voltage_dynamic(&vm->interlocks, channel, voltage);
                if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
                    wet_hal_stim_voltage(vm->hal, (uint16_t)channel, clamped_v, p1_ms, p2_ms);
                }
                biophysics_schedule_stim_ext(&vm->bio, channel, clamped_v, p1_ms, p2_ms, ip_ms);
                vm->voltages[channel] = clamped_v;
                /* Accurate impedance-scaled charge: I (mA) = V / Z(kOhm); Q(nC) = I(mA) * dt(ms) */
                float i_ma = clamped_v / vm->bio.electrode_impedance_kohm;
                vm->last_charge_nc[channel] = i_ma * (p1_ms - p2_ms);
                break;
            }

            case WET_OP_READ_SPIKES: {
                if (instr_pc + 2 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_SPIKES operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 2;

                wet_value_t window;
                wet_status_t st = pop_val(vm, &window);
                if (st != WET_OK) return st;

                if (channel == 0xFF) {
                    /* Dynamic channel index popped from stack */
                    wet_value_t v_ch;
                    st = pop_val(vm, &v_ch);
                    if (st != WET_OK) return st;
                    int32_t c_idx = to_int(&v_ch);
                    if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
                        snprintf(vm->last_error, sizeof(vm->last_error),
                                 "Electrode channel %d out of bounds (max %u)",
                                 c_idx, vm->config.channel_count);
                        return WET_ERR_OUT_OF_BOUNDS_CH;
                    }
                    channel = (uint8_t)c_idx;
                } else if (channel >= vm->config.channel_count) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Electrode channel %u out of bounds (max %u)",
                             channel, vm->config.channel_count);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                float window_ms = to_float(&window);
                uint32_t cnt = biophysics_get_spikes_window(&vm->bio, channel, window_ms);

                wet_value_t spike_res;
                spike_res.type = WET_VAL_INT;
                spike_res.as.i_val = (int32_t)cnt;
                st = push_val(vm, spike_res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_READ_VOLTAGE: {
                if (instr_pc + 2 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_VOLTAGE operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 2;

                if (channel == 0xFF) {
                    /* Dynamic channel index popped from stack */
                    wet_value_t v_ch;
                    wet_status_t st = pop_val(vm, &v_ch);
                    if (st != WET_OK) return st;
                    int32_t c_idx = to_int(&v_ch);
                    if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
                        snprintf(vm->last_error, sizeof(vm->last_error),
                                 "Electrode channel %d out of bounds (max %u)",
                                 c_idx, vm->config.channel_count);
                        return WET_ERR_OUT_OF_BOUNDS_CH;
                    }
                    channel = (uint8_t)c_idx;
                } else if (channel >= vm->config.channel_count) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Electrode channel %u out of bounds (max %u)",
                             channel, vm->config.channel_count);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                wet_value_t volt_res;
                volt_res.type = WET_VAL_FLOAT;
                volt_res.as.f_val = vm->bio.mea_voltage_v[channel];
                wet_status_t st = push_val(vm, volt_res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_MODULATE_STDP: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MODULATE_STDP operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t pre = *(const uint8_t*)(vm->code + instr_pc + 1);
                uint8_t post = *(const uint8_t*)(vm->code + instr_pc + 2);
                vm->pc = instr_pc + 3;

                wet_value_t delta_w;
                wet_status_t st = pop_val(vm, &delta_w);
                if (st != WET_OK) return st;

                if (pre == 0xFF && post == 0xFF) {
                    /* Dynamic pre/post channels popped from stack */
                    wet_value_t v_post, v_pre;
                    st = pop_val(vm, &v_post);
                    if (st != WET_OK) return st;
                    st = pop_val(vm, &v_pre);
                    if (st != WET_OK) return st;
                    int32_t pre_idx = to_int(&v_pre);
                    int32_t post_idx = to_int(&v_post);
                    if (pre_idx < 0 || (uint32_t)pre_idx >= vm->config.channel_count ||
                        post_idx < 0 || (uint32_t)post_idx >= vm->config.channel_count) {
                        snprintf(vm->last_error, sizeof(vm->last_error),
                                 "STDP dynamic channels (%d, %d) out of bounds (max %u)",
                                 pre_idx, post_idx, vm->config.channel_count);
                        return WET_ERR_OUT_OF_BOUNDS_CH;
                    }
                    pre = (uint8_t)pre_idx;
                    post = (uint8_t)post_idx;
                } else if (pre >= vm->config.channel_count || post >= vm->config.channel_count) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "STDP channels (%u, %u) out of bounds (max %u)",
                             pre, post, vm->config.channel_count);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                if (vm->interlocks.locked) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
                    return WET_ERR_INTERLOCK_LOCKED;
                }

                if (!interlocks_check_capability(&vm->interlocks, WET_OP_MODULATE_STDP, 0.0f, pre)) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Capability denied for MODULATE_STDP");
                    return WET_ERR_CAPABILITY_DENIED;
                }

                float dw = to_float(&delta_w);
                if (pre == 0 && post == 0) {
                    vm->bio.stdp_lr_scale = dw;
                } else if (pre != post) {
                    biophysics_modulate_stdp(&vm->bio, pre, post, dw);
                }
                break;
            }

            case WET_OP_GET_POP_RATE: {
                vm->pc = instr_pc + 1;
                wet_value_t window;
                wet_status_t st = pop_val(vm, &window);
                if (st != WET_OK) return st;

                wet_value_t rate_res;
                rate_res.type = WET_VAL_FLOAT;
                rate_res.as.f_val = vm->bio.population_rate_hz;
                st = push_val(vm, rate_res);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_MEA_CONFIG: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MEA_CONFIG operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t rows = *(const uint8_t*)(vm->code + instr_pc + 1);
                uint8_t cols = *(const uint8_t*)(vm->code + instr_pc + 2);
                vm->pc = instr_pc + 3;
                vm->grid_rows = rows;
                vm->grid_cols = cols;
                break;
            }

            case WET_OP_PUMP_SET_RATE: {
                if (instr_pc + 6 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUMP_SET_RATE operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t pump_id = *(const uint8_t*)(vm->code + instr_pc + 1);
                float rate_ul_min;
                memcpy(&rate_ul_min, vm->code + instr_pc + 2, sizeof(float));
                vm->pc = instr_pc + 6;

                if (!interlocks_check_capability(&vm->interlocks, WET_OP_PUMP_SET_RATE, 0.0f, pump_id)) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Capability denied for PUMP_SET_RATE (requires CAP_MICROFLUIDICS)");
                    return WET_ERR_CAPABILITY_DENIED;
                }

                if (pump_id >= 8) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Pump ID %u out of bounds (max 7)", pump_id);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                if (rate_ul_min < 0.0f || rate_ul_min > 15.0f) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "ERR_SHEAR_STRESS_EXCEEDED: Requested pump rate %.2f uL/min exceeds safe hydrodynamic limit (0..15.0 uL/min)",
                             (double)rate_ul_min);
                    return WET_ERR_SHEAR_STRESS_EXCEEDED;
                }

                if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
                    wet_hal_status_t hst = wet_hal_write_pump(vm->hal, pump_id, (double)rate_ul_min, 1);
                    if (hst == WET_HAL_ERR_DEAD_HEAD) {
                        snprintf(vm->last_error, sizeof(vm->last_error),
                                 "ERR_ACTUATOR_FAULT: Dead-head overpressure interlock tripped on pump %u (downstream valve closed)",
                                 pump_id);
                        return WET_ERR_ACTUATOR_FAULT;
                    }
                }

                vm->pump_rates_ul_min[pump_id] = rate_ul_min;
                break;
            }

            case WET_OP_PUMP_DISPENSE: {
                if (instr_pc + 6 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated PUMP_DISPENSE operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t pump_id = *(const uint8_t*)(vm->code + instr_pc + 1);
                float volume_ul;
                memcpy(&volume_ul, vm->code + instr_pc + 2, sizeof(float));
                vm->pc = instr_pc + 6;

                if (!interlocks_check_capability(&vm->interlocks, WET_OP_PUMP_DISPENSE, 0.0f, pump_id)) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Capability denied for PUMP_DISPENSE (requires CAP_MICROFLUIDICS)");
                    return WET_ERR_CAPABILITY_DENIED;
                }

                if (pump_id >= 8) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Pump ID %u out of bounds (max 7)", pump_id);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                if (volume_ul <= 0.0f || volume_ul > 500.0f) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "ERR_ACTUATOR_FAULT: Invalid dispense volume %.2f uL (allowed: 0.1..500.0 uL)",
                             (double)volume_ul);
                    return WET_ERR_ACTUATOR_FAULT;
                }

                if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
                    wet_hal_status_t hst = wet_hal_dispense_pump(vm->hal, pump_id, (double)volume_ul);
                    if (hst == WET_HAL_ERR_DEAD_HEAD) {
                        snprintf(vm->last_error, sizeof(vm->last_error),
                                 "ERR_ACTUATOR_FAULT: Dead-head overpressure interlock tripped on pump %u (downstream valve closed)",
                                 pump_id);
                        return WET_ERR_ACTUATOR_FAULT;
                    }
                }

                vm->pump_dispensed_ul[pump_id] += volume_ul;
                break;
            }

            case WET_OP_VALVE_SET: {
                if (instr_pc + 3 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated VALVE_SET operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t valve_id = *(const uint8_t*)(vm->code + instr_pc + 1);
                uint8_t state = *(const uint8_t*)(vm->code + instr_pc + 2);
                vm->pc = instr_pc + 3;

                if (!interlocks_check_capability(&vm->interlocks, WET_OP_VALVE_SET, 0.0f, valve_id)) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Capability denied for VALVE_SET (requires CAP_MICROFLUIDICS)");
                    return WET_ERR_CAPABILITY_DENIED;
                }

                if (valve_id >= 8) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Valve ID %u out of bounds (max 7)", valve_id);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
                    wet_hal_write_valve(vm->hal, valve_id, state);
                }

                vm->valve_states[valve_id] = (state != 0) ? 1 : 0;
                break;
            }

            case WET_OP_MOTOR_STEP: {
                if (instr_pc + 10 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated MOTOR_STEP operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t motor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
                int32_t steps;
                float speed_rpm;
                memcpy(&steps, vm->code + instr_pc + 2, sizeof(int32_t));
                memcpy(&speed_rpm, vm->code + instr_pc + 6, sizeof(float));
                vm->pc = instr_pc + 10;

                if (!interlocks_check_capability(&vm->interlocks, WET_OP_MOTOR_STEP, 0.0f, motor_id)) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Capability denied for MOTOR_STEP (requires CAP_MOTOR_ACTUATION)");
                    return WET_ERR_CAPABILITY_DENIED;
                }

                if (motor_id >= 4) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Motor ID %u out of bounds (max 3)", motor_id);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                vm->motor_positions[motor_id] += steps;
                vm->motor_speeds_rpm[motor_id] = speed_rpm;
                break;
            }

            case WET_OP_READ_PRESSURE: {
                if (instr_pc + 2 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_PRESSURE operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t port_id = *(const uint8_t*)(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 2;

                if (port_id >= 4) port_id = 0;
                wet_value_t p_val;
                p_val.type = WET_VAL_FLOAT;
                p_val.as.f_val = vm->fluid_pressure_kpa[port_id];
                wet_status_t st = push_val(vm, p_val);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_READ_TEMPERATURE: {
                vm->pc = instr_pc + 1;
                wet_value_t t_val;
                t_val.type = WET_VAL_FLOAT;
                t_val.as.f_val = vm->ambient_temperature_c;
                wet_status_t st = push_val(vm, t_val);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_STIM_CURRENT: {
                if (instr_pc + 6 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated STIM_CURRENT operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t channel = *(const uint8_t*)(vm->code + instr_pc + 1);
                float current_ua;
                memcpy(&current_ua, vm->code + instr_pc + 2, sizeof(float));
                vm->pc = instr_pc + 6;

                /* Pop duration arguments: interphase, phase2, phase1 */
                wet_value_t v_interphase, v_p2, v_p1;
                wet_status_t st = pop_val(vm, &v_interphase);
                if (st != WET_OK) return st;
                st = pop_val(vm, &v_p2);
                if (st != WET_OK) return st;
                st = pop_val(vm, &v_p1);
                if (st != WET_OK) return st;

                if (channel == 0xFF) {
                    wet_value_t v_ch;
                    st = pop_val(vm, &v_ch);
                    if (st != WET_OK) return st;
                    int32_t c_idx = to_int(&v_ch);
                    if (c_idx < 0 || (uint32_t)c_idx >= vm->config.channel_count) {
                        snprintf(vm->last_error, sizeof(vm->last_error),
                                 "Electrode channel %d out of bounds (max %u)",
                                 c_idx, vm->config.channel_count);
                        return WET_ERR_OUT_OF_BOUNDS_CH;
                    }
                    channel = (uint8_t)c_idx;
                } else if (channel >= vm->config.channel_count) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Electrode channel %u out of bounds (max %u)",
                             channel, vm->config.channel_count);
                    return WET_ERR_OUT_OF_BOUNDS_CH;
                }

                if (vm->interlocks.locked) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
                    return WET_ERR_INTERLOCK_LOCKED;
                }

                if (!interlocks_check_capability(&vm->interlocks, WET_OP_STIM_CURRENT, 0.0f, channel)) {
                    snprintf(vm->last_error, sizeof(vm->last_error),
                             "Capability denied for STIM_CURRENT on ch %u (ref/rec bank restricted or missing CAP_STIMULATION)", channel);
                    return WET_ERR_CAPABILITY_DENIED;
                }

                float p1_ms = to_float(&v_p1);
                float p2_ms = to_float(&v_p2);
                float ip_ms = to_float(&v_interphase);

                /* Randles Interface: V_elec = I * Rs + V_dl */
                float v_elec = (current_ua / 1000.0f) * vm->bio.r_solution_kohm + vm->bio.v_double_layer_v[channel];
                wet_status_t comp_st = interlocks_check_compliance(&vm->interlocks, vm->current_tick, channel, v_elec);
                if (comp_st != WET_OK) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
                    return comp_st;
                }

                /* Per-phase charge density check: Q (nC) = I (uA) * t (ms) */
                if (p1_ms > 0.0f && p2_ms > 0.0f) {
                    float q_phase1 = wet_fabsf(current_ua) * 1e-3f * p1_ms;
                    float q_phase2 = wet_fabsf(current_ua) * 1e-3f * p2_ms;
                    if (q_phase1 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC || q_phase2 > INTERLOCK_CHARGE_DENSITY_LIMIT_NC) {
                        vm->interlocks.locked = 1;
                        vm->interlocks.trip_reason = INTERLOCK_TRIP_CHARGE_DENSITY;
                        vm->interlocks.tripped_channel = channel;
                        vm->interlocks.trip_tick = vm->current_tick;
                        vm->interlocks.trip_value = q_phase1 > q_phase2 ? q_phase1 : q_phase2;
                        if (vm->hal) {
                            wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_CHARGE_DENSITY);
                        }
                        snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
                                 "ERR_CHARGE_DENSITY_EXCEEDED: ch=%u single phase charge=%.4f nC > %.2f nC (Shannon limit)",
                                 channel, (double)vm->interlocks.trip_value, (double)INTERLOCK_CHARGE_DENSITY_LIMIT_NC);
                        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
                        return WET_ERR_CHARGE_DENSITY_EXCEEDED;
                    }
                }

                if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
                    int32_t cur_pA = (int32_t)(current_ua * 1e6f);
                    uint32_t dur_us = (uint32_t)(p1_ms * 1000.0f);
                    wet_hal_status_t hst = wet_hal_stim_current(vm->hal, (uint16_t)channel, cur_pA, dur_us);
                    if (hst == WET_HAL_ERR_COMPLIANCE_RAILED) {
                        vm->interlocks.locked = 1;
                        vm->interlocks.trip_reason = INTERLOCK_TRIP_COMPLIANCE_RAILED;
                        vm->interlocks.tripped_channel = channel;
                        vm->interlocks.trip_tick = vm->current_tick;
                        snprintf(vm->interlocks.diagnostic, sizeof(vm->interlocks.diagnostic),
                                 "ERR_COMPLIANCE_RAILED: Channel %u compliance rail tripped on hardware driver (~7.0V limit)", channel);
                        snprintf(vm->last_error, sizeof(vm->last_error), "%s", vm->interlocks.diagnostic);
                        wet_hal_emergency_crowbar(vm, INTERLOCK_TRIP_COMPLIANCE_RAILED);
                        return WET_ERR_COMPLIANCE_RAILED;
                    }
                }

                biophysics_schedule_stim_current(&vm->bio, channel, current_ua, p1_ms, p2_ms, ip_ms);
                vm->voltages[channel] = v_elec;
                vm->last_charge_nc[channel] = (current_ua * 1e-3f) * (p1_ms - p2_ms);
                break;
            }

            case WET_OP_READ_PH: {
                vm->pc = instr_pc + 1;
                wet_value_t ph_val;
                ph_val.type = WET_VAL_FLOAT;
                ph_val.as.f_val = vm->ph_level > 0.0f ? vm->ph_level : 7.40f;
                wet_status_t st = push_val(vm, ph_val);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_READ_DO: {
                vm->pc = instr_pc + 1;
                wet_value_t do_val;
                do_val.type = WET_VAL_FLOAT;
                do_val.as.f_val = vm->dissolved_oxygen_pct > 0.0f ? vm->dissolved_oxygen_pct : 95.0f;
                wet_status_t st = push_val(vm, do_val);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_READ_CO2: {
                vm->pc = instr_pc + 1;
                wet_value_t co2_val;
                co2_val.type = WET_VAL_FLOAT;
                co2_val.as.f_val = vm->dissolved_co2_pct > 0.0f ? vm->dissolved_co2_pct : 5.0f;
                wet_status_t st = push_val(vm, co2_val);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_READ_BUBBLE: {
                if (instr_pc + 2 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_BUBBLE operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t sensor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 2;
                if (sensor_id >= 8) sensor_id = 0;
                wet_value_t b_val;
                b_val.type = WET_VAL_INT;
                b_val.as.i_val = vm->bubble_detected[sensor_id] ? 1 : 0;
                wet_status_t st = push_val(vm, b_val);
                if (st != WET_OK) return st;
                break;
            }

            case WET_OP_READ_FLOW: {
                if (instr_pc + 2 > vm->code_size) {
                    snprintf(vm->last_error, sizeof(vm->last_error), "Truncated READ_FLOW operand");
                    return WET_ERR_INVALID_OPCODE;
                }
                uint8_t sensor_id = *(const uint8_t*)(vm->code + instr_pc + 1);
                vm->pc = instr_pc + 2;
                if (sensor_id >= 8) sensor_id = 0;
                double flow_val = (double)vm->fluid_flow_rate_ul_min[sensor_id];
                if (vm->hal && vm->hal->mode != WET_HAL_MODE_SIMULATED) {
                    wet_hal_read_flow(vm->hal, sensor_id, &flow_val);
                }
                wet_value_t f_val;
                f_val.type = WET_VAL_FLOAT;
                f_val.as.f_val = (float)flow_val;
                wet_status_t st = push_val(vm, f_val);
                if (st != WET_OK) return st;
                break;
            }

            default: {
                snprintf(vm->last_error, sizeof(vm->last_error),
                         "Unrecognized or invalid opcode 0x%02X at pc %zu", op, instr_pc);
                return WET_ERR_INVALID_OPCODE;
            }
        }
    }

    populate_telemetry(vm, out_telem);
    return WET_OK;
}

/* =========================================================================
 * Phase 3: Standalone C99 Load-Time Bytecode Verifier
 * ========================================================================= */

wet_status_t wet_verify_bytecode_internal(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len) {
    if (!bytecode) {
        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Null bytecode pointer");
        return WET_ERR_NULL_PTR;
    }
    if (size < WET_HEADER_SIZE) {
        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Bytecode size %zu smaller than 32-byte header", size);
        return WET_ERR_INVALID_MAGIC;
    }

    if (memcmp(bytecode, WET_HEADER_MAGIC, 4) != 0) {
        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Invalid header magic (expected WETB)");
        return WET_ERR_INVALID_MAGIC;
    }

    uint8_t v_maj = bytecode[4];
    uint8_t v_min = bytecode[5];
    if (v_maj != WET_VERSION_MAJOR || v_min != WET_VERSION_MINOR) {
        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Unsupported version %u.%u (expected 1.0)", v_maj, v_min);
        return WET_ERR_UNSUPPORTED_VERSION;
    }

    uint32_t file_size = wet_read_u32_le(bytecode + 8);
    uint32_t stored_crc = wet_read_u32_le(bytecode + 12);
    uint32_t num_sections = wet_read_u32_le(bytecode + 16);

    if (file_size > size) {
        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Declared file size %u exceeds buffer %zu", file_size, size);
        return WET_ERR_MALFORMED_SECTION;
    }

    /* CRC32 check: copy header, zero bytes 12..15, compute CRC */
    uint8_t hdr_copy[WET_HEADER_SIZE];
    memcpy(hdr_copy, bytecode, WET_HEADER_SIZE);
    memset(hdr_copy + 12, 0, 4);
    uint32_t crc = wet_compute_crc32(hdr_copy, WET_HEADER_SIZE, 0);
    if (file_size > WET_HEADER_SIZE) {
        crc = wet_compute_crc32(bytecode + WET_HEADER_SIZE, file_size - WET_HEADER_SIZE, crc);
    }
    if (crc != stored_crc) {
        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "CRC32 mismatch (computed 0x%08X != stored 0x%08X)", crc, stored_crc);
        return WET_ERR_CRC_MISMATCH;
    }

    size_t sec_table_end = WET_HEADER_SIZE + (size_t)num_sections * WET_SECTION_ENTRY_SIZE;
    if (sec_table_end > file_size) {
        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Section table overflows file bounds");
        return WET_ERR_MALFORMED_SECTION;
    }

    const uint8_t* code_ptr = NULL;
    size_t code_size = 0;
    size_t num_constants = 0;

    for (uint32_t s = 0; s < num_sections; ++s) {
        const uint8_t* entry = bytecode + WET_HEADER_SIZE + s * WET_SECTION_ENTRY_SIZE;
        uint16_t sec_type = wet_read_u16_le(entry);
        uint32_t sec_offset = wet_read_u32_le(entry + 4);
        uint32_t sec_size = wet_read_u32_le(entry + 8);

        if ((size_t)sec_offset + sec_size > file_size || sec_offset < sec_table_end) {
            if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Section %u (type %u) out of bounds", s, sec_type);
            return WET_ERR_MALFORMED_SECTION;
        }

        if (sec_type == WET_SEC_BYTECODE_STREAM) {
            code_ptr = bytecode + sec_offset;
            code_size = sec_size;
        } else if (sec_type == WET_SEC_CONSTANT_POOL) {
            if (sec_size >= 4) {
                uint32_t declared_entries = wet_read_u32_le(bytecode + sec_offset);
                const uint8_t* cp = bytecode + sec_offset + 4;
                size_t cp_remain = sec_size - 4;
                while (cp_remain > 0) {
                    uint8_t ctype = *cp;
                    cp++; cp_remain--;
                    if (ctype == WET_VAL_INT || ctype == WET_VAL_FLOAT) {
                        if (cp_remain < 4) {
                            if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Malformed constant pool");
                            return WET_ERR_MALFORMED_SECTION;
                        }
                        cp += 4; cp_remain -= 4;
                    } else if (ctype == WET_VAL_STRING) {
                        if (cp_remain < 2) {
                            if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Malformed string in constant pool");
                            return WET_ERR_MALFORMED_SECTION;
                        }
                        uint16_t slen = wet_read_u16_le(cp);
                        cp += 2; cp_remain -= 2;
                        if (cp_remain < slen) {
                            if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "String payload overflows constant pool");
                            return WET_ERR_MALFORMED_SECTION;
                        }
                        cp += slen; cp_remain -= slen;
                    } else {
                        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Unknown constant type %u", ctype);
                        return WET_ERR_MALFORMED_SECTION;
                    }
                    num_constants++;
                }
                if (num_constants != declared_entries) {
                    if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Constant pool count mismatch: declared %u, parsed %u", declared_entries, num_constants);
                    return WET_ERR_MALFORMED_SECTION;
                }
            }
        }
    }

    if (!code_ptr || code_size == 0) {
        return WET_OK;
    }

    uint8_t* is_start = (uint8_t*)malloc(code_size);
    if (!is_start) {
        if (err_buf && err_buf_len > 0) snprintf(err_buf, err_buf_len, "Failed to allocate verifier bitmap (%zu bytes)", code_size);
        return WET_ERR_ALLOC_FAILED;
    }
    memset(is_start, 0, code_size);

    /* Pass 1: Decode opcodes and check instruction sizes */
    size_t pc = 0;
    while (pc < code_size) {
        is_start[pc] = 1;
        uint8_t op = code_ptr[pc];
        size_t ilen = 1;

        switch ((wet_opcode_t)op) {
            case WET_OP_NOP:
            case WET_OP_HALT:
            case WET_OP_SYNC_TICK:
            case WET_OP_POP:
            case WET_OP_DUP:
            case WET_OP_SWAP:
            case WET_OP_ADD_I:
            case WET_OP_SUB_I:
            case WET_OP_MUL_I:
            case WET_OP_DIV_I:
            case WET_OP_ADD_F:
            case WET_OP_SUB_F:
            case WET_OP_MUL_F:
            case WET_OP_DIV_F:
            case WET_OP_NEG:
            case WET_OP_MOD_I:
            case WET_OP_CMP_EQ:
            case WET_OP_CMP_NE:
            case WET_OP_CMP_LT:
            case WET_OP_CMP_LE:
            case WET_OP_CMP_GT:
            case WET_OP_CMP_GE:
            case WET_OP_RET:
            case WET_OP_GET_POP_RATE:
            case WET_OP_READ_TEMPERATURE:
            case WET_OP_READ_PH:
            case WET_OP_READ_DO:
            case WET_OP_READ_CO2:
                ilen = 1;
                break;

            case WET_OP_STIM_BIPHASIC:
            case WET_OP_READ_SPIKES:
            case WET_OP_READ_VOLTAGE:
            case WET_OP_READ_PRESSURE:
            case WET_OP_READ_BUBBLE:
            case WET_OP_READ_FLOW:
                ilen = 2;
                break;

            case WET_OP_SLEEP_TICKS:
            case WET_OP_LOAD_LOCAL:
            case WET_OP_STORE_LOCAL:
            case WET_OP_JMP:
            case WET_OP_JMP_IF_TRUE:
            case WET_OP_JMP_IF_FALSE:
            case WET_OP_MODULATE_STDP:
            case WET_OP_MEA_CONFIG:
            case WET_OP_VALVE_SET:
                ilen = 3;
                break;

            case WET_OP_PUSH_CONST:
                ilen = 3;
                if (pc + 3 <= code_size) {
                    uint16_t c_idx = wet_read_u16_le(code_ptr + pc + 1);
                    if (c_idx >= num_constants) {
                        if (err_buf && err_buf_len > 0)
                            snprintf(err_buf, err_buf_len, "Constant index %u out of range (%zu)", c_idx, num_constants);
                        free(is_start);
                        return WET_ERR_BYTECODE_VERIFICATION;
                    }
                }
                break;

            case WET_OP_CALL:
                ilen = 4;
                break;

            case WET_OP_PUSH_INT:
            case WET_OP_PUSH_FLOAT:
                ilen = 5;
                break;

            case WET_OP_PUMP_SET_RATE:
            case WET_OP_PUMP_DISPENSE:
            case WET_OP_STIM_CURRENT:
                ilen = 6;
                break;

            case WET_OP_MOTOR_STEP:
                ilen = 10;
                break;

            default:
                if (err_buf && err_buf_len > 0)
                    snprintf(err_buf, err_buf_len, "Invalid opcode 0x%02X at offset %zu", op, pc);
                free(is_start);
                return WET_ERR_INVALID_OPCODE;
        }

        if (pc + ilen > code_size) {
            if (err_buf && err_buf_len > 0)
                snprintf(err_buf, err_buf_len, "Truncated instruction (opcode 0x%02X needs %zu bytes, only %zu left)", op, ilen, code_size - pc);
            free(is_start);
            return WET_ERR_BYTECODE_VERIFICATION;
        }
        pc += ilen;
    }

    /* Pass 2: Verify branch target alignment */
    pc = 0;
    while (pc < code_size) {
        uint8_t op = code_ptr[pc];
        if (op == WET_OP_JMP || op == WET_OP_JMP_IF_TRUE || op == WET_OP_JMP_IF_FALSE) {
            int16_t offset = wet_read_i16_le(code_ptr + pc + 1);
            int64_t target = (int64_t)pc + offset;
            if (target < 0 || (size_t)target >= code_size) {
                if (err_buf && err_buf_len > 0)
                    snprintf(err_buf, err_buf_len, "Jump at pc %zu target %lld out of code range [0, %zu)", pc, (long long)target, code_size);
                free(is_start);
                return WET_ERR_BYTECODE_VERIFICATION;
            }
            if (!is_start[target]) {
                if (err_buf && err_buf_len > 0)
                    snprintf(err_buf, err_buf_len, "Jump at pc %zu target %lld lands in middle of instruction", pc, (long long)target);
                free(is_start);
                return WET_ERR_BYTECODE_VERIFICATION;
            }
            pc += 3;
        } else {
            size_t next_pc = pc + 1;
            while (next_pc < code_size && !is_start[next_pc]) next_pc++;
            pc = next_pc;
        }
    }

    free(is_start);
    return WET_OK;
}

/* =========================================================================
 * Phase 3: Live State Checkpointing & Hot-Swap
 * ========================================================================= */

#define WET_SNAPSHOT_MAGIC 0x53544557U /* 'W','E','T','S' */
#define WET_SNAPSHOT_VERSION 1

#pragma pack(push, 1)
typedef struct {
    uint32_t magic;
    uint32_t version;
    uint32_t payload_bytes;
    uint64_t current_tick;
    double   sim_time_ms;
    int64_t  sim_time_us;
    float    v_m_mv[64];
    float    v_thresh_mv[64];
    float    g_exc_ns[64];
    float    g_inh_ns[64];
    float    g_ahp_ns[64];
    uint16_t refract_ticks[64];
    float    trace_pre[64];
    float    trace_post[64];
    float    v_double_layer_v[64];
    float    q_accum[64];
    float    cumulative_unbounded_dc_nc[64];
    float    syn_weights_ns[64][64];
    float    syn_u_stp[64][64];
    float    syn_x_stp[64][64];
    float    pump_dispensed_ul[8];
} wet_vm_snapshot_payload_t;
#pragma pack(pop)

wet_status_t wet_vm_snapshot_internal(const struct wet_vm_instance* vm, uint8_t* buffer, size_t* inout_len) {
    if (!vm || !inout_len) return WET_ERR_NULL_PTR;

    size_t req_size = sizeof(wet_vm_snapshot_payload_t);
    if (!buffer) {
        *inout_len = req_size;
        return WET_OK;
    }
    if (*inout_len < req_size) {
        *inout_len = req_size;
        return WET_ERR_ALLOC_FAILED;
    }

    wet_vm_snapshot_payload_t* snap = (wet_vm_snapshot_payload_t*)buffer;
    memset(snap, 0, sizeof(*snap));
    snap->magic = WET_SNAPSHOT_MAGIC;
    snap->version = WET_SNAPSHOT_VERSION;
    snap->payload_bytes = (uint32_t)req_size;
    snap->current_tick = vm->current_tick;
    snap->sim_time_ms = vm->sim_time_ms;
    snap->sim_time_us = vm->sim_time_us;

    memcpy(snap->v_m_mv, vm->bio.v_m_mv, sizeof(snap->v_m_mv));
    memcpy(snap->v_thresh_mv, vm->bio.v_thresh_mv, sizeof(snap->v_thresh_mv));
    memcpy(snap->g_exc_ns, vm->bio.g_exc_ns, sizeof(snap->g_exc_ns));
    memcpy(snap->g_inh_ns, vm->bio.g_inh_ns, sizeof(snap->g_inh_ns));
    memcpy(snap->g_ahp_ns, vm->bio.g_ahp_ns, sizeof(snap->g_ahp_ns));
    memcpy(snap->refract_ticks, vm->bio.refract_ticks, sizeof(snap->refract_ticks));
    memcpy(snap->trace_pre, vm->bio.trace_pre, sizeof(snap->trace_pre));
    memcpy(snap->trace_post, vm->bio.trace_post, sizeof(snap->trace_post));
    memcpy(snap->v_double_layer_v, vm->bio.v_double_layer_v, sizeof(snap->v_double_layer_v));
    memcpy(snap->q_accum, vm->interlocks.q_accum, sizeof(snap->q_accum));
    memcpy(snap->cumulative_unbounded_dc_nc, vm->interlocks.cumulative_unbounded_dc_nc, sizeof(snap->cumulative_unbounded_dc_nc));
    memcpy(snap->pump_dispensed_ul, vm->pump_dispensed_ul, sizeof(snap->pump_dispensed_ul));

    for (int i = 0; i < 64; ++i) {
        for (int j = 0; j < 64; ++j) {
            snap->syn_weights_ns[i][j] = vm->bio.synapses[i][j].weight_ns;
            snap->syn_u_stp[i][j] = vm->bio.synapses[i][j].u_stp;
            snap->syn_x_stp[i][j] = vm->bio.synapses[i][j].x_stp;
        }
    }

    *inout_len = req_size;
    return WET_OK;
}

wet_status_t wet_vm_restore_internal(struct wet_vm_instance* vm, const uint8_t* buffer, size_t len) {
    if (!vm || !buffer) return WET_ERR_NULL_PTR;
    if (len < sizeof(wet_vm_snapshot_payload_t)) {
        snprintf(vm->last_error, sizeof(vm->last_error), "Snapshot buffer too small (%zu < %zu)", len, sizeof(wet_vm_snapshot_payload_t));
        return WET_ERR_MALFORMED_SECTION;
    }

    const wet_vm_snapshot_payload_t* snap = (const wet_vm_snapshot_payload_t*)buffer;
    if (snap->magic != WET_SNAPSHOT_MAGIC || snap->version != WET_SNAPSHOT_VERSION) {
        snprintf(vm->last_error, sizeof(vm->last_error), "Invalid snapshot magic or version");
        return WET_ERR_INVALID_MAGIC;
    }

    vm->current_tick = snap->current_tick;
    vm->sim_time_ms = snap->sim_time_ms;
    vm->sim_time_us = snap->sim_time_us;

    memcpy(vm->bio.v_m_mv, snap->v_m_mv, sizeof(snap->v_m_mv));
    memcpy(vm->bio.v_thresh_mv, snap->v_thresh_mv, sizeof(snap->v_thresh_mv));
    memcpy(vm->bio.g_exc_ns, snap->g_exc_ns, sizeof(snap->g_exc_ns));
    memcpy(vm->bio.g_inh_ns, snap->g_inh_ns, sizeof(snap->g_inh_ns));
    memcpy(vm->bio.g_ahp_ns, snap->g_ahp_ns, sizeof(snap->g_ahp_ns));
    memcpy(vm->bio.refract_ticks, snap->refract_ticks, sizeof(snap->refract_ticks));
    memcpy(vm->bio.trace_pre, snap->trace_pre, sizeof(snap->trace_pre));
    memcpy(vm->bio.trace_post, snap->trace_post, sizeof(snap->trace_post));
    memcpy(vm->bio.v_double_layer_v, snap->v_double_layer_v, sizeof(snap->v_double_layer_v));
    memcpy(vm->interlocks.q_accum, snap->q_accum, sizeof(snap->q_accum));
    memcpy(vm->interlocks.cumulative_unbounded_dc_nc, snap->cumulative_unbounded_dc_nc, sizeof(snap->cumulative_unbounded_dc_nc));
    memcpy(vm->pump_dispensed_ul, snap->pump_dispensed_ul, sizeof(snap->pump_dispensed_ul));

    for (int i = 0; i < 64; ++i) {
        for (int j = 0; j < 64; ++j) {
            vm->bio.synapses[i][j].weight_ns = snap->syn_weights_ns[i][j];
            vm->bio.synapses[i][j].u_stp = snap->syn_u_stp[i][j];
            vm->bio.synapses[i][j].x_stp = snap->syn_x_stp[i][j];
        }
    }

    return WET_OK;
}
