#ifndef WETVM_VM_H
#define WETVM_VM_H

#include "wetvm_api.h"
#include "wetvm_types.h"
#include "biophysics.h"
#include "interlocks.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Tagged value types */
typedef enum {
    WET_VAL_INT    = 1,
    WET_VAL_FLOAT  = 2,
    WET_VAL_STRING = 3
} wet_val_type_t;

/* Tagged Value representation for Operand Stack and Locals */
typedef struct {
    uint8_t type; /* wet_val_type_t */
    union {
        int32_t i_val;
        float   f_val;
        struct {
            const char* str;
            uint16_t    len;
        } s_val;
    } as;
} wet_value_t;

/* Constant Pool Entry */
typedef struct {
    wet_value_t val;
    char*       str_alloc; /* Owned allocation for string constants */
} wet_constant_entry_t;

/* Call Frame for CALL / RET */
typedef struct {
    size_t return_pc;
} wet_call_frame_t;

/* Ring-0 Life Support Supervisor (M6 Life Support Subsystem) */
typedef struct {
    uint8_t  supervisor_active;            /* 1 = Ring-0 supervisor autonomous maintenance active */
    float    maintenance_perfusion_ul_min[8]; /* Baseline nutrient flow rates */
    float    maintenance_temperature_c;      /* Target incubator temperature (37.0 C) */
    uint64_t ticks_under_supervisor;
} wet_life_supervisor_t;

/* Forward declaration for Hardware Abstraction Layer context */
struct wet_hal_context;

/* Internal VM instance structure */
struct wet_vm_instance {
    wet_vm_config_t config;

    /* Raw bytecode buffer */
    uint8_t* bytecode_raw;
    size_t   bytecode_size;

    /* Bytecode Stream section pointers */
    const uint8_t* code;
    size_t         code_size;
    size_t         pc;

    /* Constant Pool */
    wet_constant_entry_t* constants;
    size_t                num_constants;

    /* Operand Stack */
    wet_value_t* stack;
    size_t       sp;         /* Stack pointer: index of next free slot */
    size_t       max_stack;

    /* Local Variables */
    wet_value_t* locals;
    size_t       max_locals;

    /* Call Stack for CALL / RET */
    wet_call_frame_t* call_stack;
    size_t            call_sp;
    size_t            max_call_depth;

    /* Execution State */
    uint64_t current_tick;
    double   sim_time_ms;
    int64_t  sim_time_us;        /* Microsecond monotonic time (avoids float32 loss) */
    int      is_halted;
    int      is_finished;
    uint16_t sleep_ticks_remaining;
    uint8_t  arena_allocated;    /* 1 if created in static arena memory */
    uint8_t* arena_base;         /* Caller-supplied arena base pointer */
    size_t   arena_total_bytes;  /* Total caller-supplied arena buffer size */
    size_t   arena_mark_offset;  /* Offset after static stack/locals/call_stack */
    size_t   arena_bump_offset;  /* Current bump allocator offset inside arena */

    /* Channel States (64 channels) */
    float    voltages[64];
    uint8_t  spikes[64];
    float    last_charge_nc[64];
    float    discharge_charge_nc[64];
    float    population_rate_hz;

    /* Grid topology */
    uint8_t  grid_rows;
    uint8_t  grid_cols;

    /* Embedded Biophysical Digital Twin (M3) & Hardware Watchdog Interlocks (M4) */
    bio_state_t       bio;
    interlock_state_t interlocks;
    uint16_t          loaded_capabilities;

    /* Ring-0 Autonomous Life Support Supervisor */
    wet_life_supervisor_t life_supervisor;

    /* Cyber-Physical Hardware Actuator State (M5 HAL) */
    float    pump_rates_ul_min[8];
    float    pump_dispensed_ul[8];
    uint8_t  valve_states[8];
    int32_t  motor_positions[4];
    float    motor_speeds_rpm[4];
    float    ambient_temperature_c;
    float    fluid_pressure_kpa[4];

    /* Phase 3 Environmental & Cyber-Physical Sensors */
    float    ph_level;              /* e.g. 7.40 */
    float    dissolved_oxygen_pct;  /* e.g. 95.0 % */
    float    dissolved_co2_pct;     /* e.g. 5.0 % */
    uint8_t  bubble_detected[8];    /* 1 if bubble detected on tubing line */
    float    fluid_flow_rate_ul_min[8]; /* flow sensor readouts */

    /* Hardware Abstraction Layer Context (M1 HAL) */
    struct wet_hal_context* hal;

    /* Pure-C Closed-Loop Hook & Determinism Controls (Janus v2.2) */
    wet_closed_loop_hook_fn closed_loop_hook;
    void*                   closed_loop_user_data;
    uint64_t                rng_seed;
    uint8_t                 rng_seed_set;
    uint8_t                 noise_enabled;

    /* Error reporting buffer */
    char     last_error[256];
};

/* Internal VM execution and validation declarations */
uint32_t wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc);
wet_status_t wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem);
wet_status_t wet_verify_bytecode_internal(const uint8_t* bytecode, size_t size, char* err_buf, size_t err_buf_len);
wet_status_t wet_vm_apply_stim_voltage_internal(
    struct wet_vm_instance* vm,
    uint8_t channel,
    float voltage_v,
    float p1_ms,
    float p2_ms,
    float ip_ms
);
wet_status_t wet_vm_apply_stim_current_internal(
    struct wet_vm_instance* vm,
    uint8_t channel,
    float current_ua,
    float p1_ms,
    float p2_ms,
    float ip_ms
);

#ifdef __cplusplus
}
#endif

#endif /* WETVM_VM_H */
