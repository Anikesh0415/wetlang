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
    int      is_halted;
    int      is_finished;
    uint16_t sleep_ticks_remaining;

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

    /* Cyber-Physical Hardware Actuator State (M5 HAL) */
    float    pump_rates_ul_min[8];
    float    pump_dispensed_ul[8];
    uint8_t  valve_states[8];
    int32_t  motor_positions[4];
    float    motor_speeds_rpm[4];
    float    ambient_temperature_c;
    float    fluid_pressure_kpa[4];

    /* Error reporting buffer */
    char     last_error[256];
};

/* Internal VM execution and validation declarations */
uint32_t wet_compute_crc32(const uint8_t* data, size_t length, uint32_t initial_crc);
wet_status_t wet_vm_step_internal(struct wet_vm_instance* vm, wet_telemetry_t* out_telem);

#ifdef __cplusplus
}
#endif

#endif /* WETVM_VM_H */
