#ifndef WETVM_API_H
#define WETVM_API_H

#include <stdint.h>
#include <stddef.h>
#include "wetvm_types.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Export / Import visibility macro */
#if defined(_WIN32) || defined(__CYGWIN__)
  #ifdef WET_BUILDING_DLL
    #define WET_EXPORT __declspec(dllexport)
  #else
    #define WET_EXPORT __declspec(dllimport)
  #endif
#else
  #if defined(__GNUC__) && __GNUC__ >= 4
    #define WET_EXPORT __attribute__((visibility("default")))
  #else
    #define WET_EXPORT
  #endif
#endif

/* Opaque Virtual Machine Instance Pointer */
typedef struct wet_vm_instance wet_vm_t;

/* VM Configuration */
typedef struct {
    double   dt_ms;            /* Simulation timestep in ms (default: 0.1 ms) */
    uint32_t max_stack_depth;  /* Max operand stack capacity (default: 1024) */
    uint32_t max_locals;       /* Max local variable slots (default: 256) */
    uint32_t channel_count;    /* Number of MEA channels (default: 64) */
    uint32_t max_ops_per_tick; /* Per-tick watchdog instruction limit (default: 100,000 / 2,000 for MCU) */
} wet_vm_config_t;

/* Cycle-Accurate Telemetry Output */
typedef struct {
    uint64_t current_tick;         /* Number of executed ticks */
    double   sim_time_ms;          /* Total simulation time in ms */
    float    voltages[64];         /* Instantaneous channel potentials (V) */
    uint8_t  spikes[64];           /* Binary spike raster (1 = spiked this tick) */
    float    population_rate_hz;   /* Estimated population firing rate (Hz) */
    float    last_charge_nc[64];   /* Cumulative or last injected charge (nC) */
} wet_telemetry_t;

/* Cyber-Physical Hardware Actuator Telemetry */
typedef struct {
    float    pump_rates_ul_min[8];   /* Rate for 8 microfluidic pumps */
    float    pump_dispensed_ul[8];   /* Cumulative dispensed volume */
    uint8_t  valve_states[8];        /* State of 8 valves (0=closed, 1=open) */
    int32_t  motor_positions[4];     /* Step positions for 4 motors */
    float    motor_speeds_rpm[4];    /* Speeds for 4 motors */
    float    ambient_temperature_c;  /* Ambient incubator temperature (C) */
    float    fluid_pressure_kpa[4];  /* Microfluidic pressure (kPa) */
} wet_actuator_telemetry_t;

/* =========================================================================
 * Public C-ABI API Functions
 * ========================================================================= */

/**
 * Creates and initializes a new WetVM instance.
 * If config is NULL, default configuration values are used.
 */
WET_EXPORT wet_vm_t* wet_create_vm(const wet_vm_config_t* config);

/**
 * Creates a WetVM instance using caller-supplied static arena memory (zero dynamic malloc).
 */
WET_EXPORT wet_vm_t* wet_create_vm_arena(
    void* arena_buf,
    size_t arena_bytes,
    const wet_vm_config_t* config
);

/**
 * Destroys the VM instance and releases all associated memory.
 */
WET_EXPORT void wet_free_vm(wet_vm_t* vm);

/**
 * Phase 3: Configures electrode material and physical geometric surface area.
 */
WET_EXPORT void wet_configure_electrode(
    wet_vm_t* vm,
    uint8_t material,
    float area_um2
);

/**
 * Phase 3: Actuates hardware charge-recovery switch to discharge residual DC Faradaic charge.
 */
WET_EXPORT void wet_active_discharge(
    wet_vm_t* vm,
    uint8_t channel
);

/**
 * Phase 3: Actuates hardware charge-recovery switch on all channels.
 */
WET_EXPORT void wet_active_discharge_all(
    wet_vm_t* vm
);

/**
 * Phase 3: Enables microfluidic valve-pump dead-head overpressure interlock.
 */
WET_EXPORT void wet_enable_dead_head_protection(
    wet_vm_t* vm,
    uint8_t enable
);

/**
 * Phase 3: Ring-0 Life Support Supervisor shutdown (terminates baseline life support).
 */
WET_EXPORT void wet_life_supervisor_shutdown(
    wet_vm_t* vm
);

/**
 * Validates, loads, and parses WBC binary bytecode into the VM.
 * Resets execution registers (pc, sp, tick_count, is_halted).
 * If loading fails, an error message is written into err_buf (if provided).
 */
WET_EXPORT wet_status_t wet_load_bytecode(
    wet_vm_t* vm,
    const uint8_t* code_bytes,
    size_t size,
    char* err_buf,
    size_t err_buf_len
);

/**
 * Executes instructions until the next SYNC_TICK yield, SLEEP_TICKS, HALT, or error.
 * Advances current_tick by 1 and sim_time_ms by config->dt_ms.
 * Caller allocates out_telem; if non-NULL, it is populated with current state.
 */
WET_EXPORT wet_status_t wet_step_tick(
    wet_vm_t* vm,
    wet_telemetry_t* out_telem
);

/**
 * Executes up to `ticks` consecutive ticks.
 * Returns WET_OK if all ticks executed successfully, or early status on HALT/error.
 * executed_ticks receives the actual number of ticks completed.
 * out_telem receives final state (if non-NULL).
 */
WET_EXPORT wet_status_t wet_run_ticks(
    wet_vm_t* vm,
    uint32_t ticks,
    uint32_t* executed_ticks,
    wet_telemetry_t* out_telem
);

/**
 * Injects a biphasic electrical stimulus onto the designated MEA channel.
 */
WET_EXPORT wet_status_t wet_inject_stimulus(
    wet_vm_t* vm,
    uint8_t channel,
    float voltage_v,
    float phase1_ms,
    float phase2_ms
);

/**
 * Queries current telemetry state into caller-allocated struct.
 */
WET_EXPORT wet_status_t wet_get_telemetry(
    wet_vm_t* vm,
    wet_telemetry_t* out_telem
);

/**
 * Queries current cyber-physical hardware actuator telemetry into caller-allocated struct.
 */
WET_EXPORT wet_status_t wet_get_actuator_telemetry(
    wet_vm_t* vm,
    wet_actuator_telemetry_t* out_act_telem
);

/**
 * Returns string pointer to the last error message recorded on the VM.
 */
WET_EXPORT const char* wet_get_last_error(wet_vm_t* vm);

/**
 * Returns a static descriptive string for the given status code.
 */
WET_EXPORT const char* wet_status_to_string(wet_status_t status);

#ifdef __cplusplus
}
#endif

#endif /* WETVM_API_H */
