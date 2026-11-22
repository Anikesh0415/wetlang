#ifndef WET_HAL_H
#define WET_HAL_H

#include <stdint.h>
#include <stddef.h>
#include "wetvm_types.h"
#include "wetvm_api.h"

#ifdef __cplusplus
extern "C" {
#endif

/* =========================================================================
 * WetLang Hardware Abstraction Layer (HAL) Core Architecture
 * Tri-Modal Router: SIMULATED (0), PHYSICAL (1), HIL_LOOPBACK (2)
 * ========================================================================= */

typedef enum {
    WET_HAL_MODE_SIMULATED    = 0, /* In-silico ODE biophysics & virtual registers */
    WET_HAL_MODE_PHYSICAL     = 1, /* Real device drivers (SPI, I2C, RS-232, CAN) */
    WET_HAL_MODE_HIL_LOOPBACK = 2  /* Hardware-in-the-loop mock with bit-level validation */
} wet_hal_mode_t;

typedef enum {
    WET_HAL_DRIVER_EPHYS      = 1, /* Intan RHS2116 / MaxWell MaxOne */
    WET_HAL_DRIVER_PUMP       = 2, /* Harvard Apparatus RS-232 */
    WET_HAL_DRIVER_VALVE      = 3, /* Microfluidic Solenoid / CAN */
    WET_HAL_DRIVER_FLOW       = 4, /* Sensirion I2C / SHDLC */
    WET_HAL_DRIVER_CAN_BUS    = 5  /* CAN-bus transceiver */
} wet_hal_driver_type_t;

typedef enum {
    WET_HAL_OK                   = 0,
    WET_HAL_ERR_NULL_PTR         = -1,
    WET_HAL_ERR_INVALID_MODE     = -2,
    WET_HAL_ERR_DRIVER_NOT_FOUND = -3,
    WET_HAL_ERR_IO               = -4,
    WET_HAL_ERR_TIMEOUT          = -5,
    WET_HAL_ERR_CRC_MISMATCH     = -6,
    WET_HAL_ERR_COMPLIANCE_RAILED= -7,
    WET_HAL_ERR_INTERLOCK        = -8,
    WET_HAL_ERR_DEAD_HEAD        = -9,
    WET_HAL_ERR_OUT_OF_BOUNDS    = -10,
    WET_HAL_ERR_BUS_BUSY         = -11,
    WET_HAL_ERR_NOT_SUPPORTED    = -12,
    WET_HAL_ERR_BUFFER_FULL      = -13
} wet_hal_status_t;

/* Forward declarations */
typedef struct wet_hal_driver wet_hal_driver_t;
typedef struct wet_hal_context wet_hal_context_t;

/* Driver vtable operations */
typedef struct {
    /* Lifecycle */
    wet_hal_status_t (*init)(wet_hal_driver_t* drv, void* config);
    wet_hal_status_t (*shutdown)(wet_hal_driver_t* drv);
    wet_hal_status_t (*emergency_stop)(wet_hal_driver_t* drv, uint32_t reason);
    wet_hal_status_t (*step_tick)(wet_hal_driver_t* drv, uint64_t current_tick, double dt_ms);

    /* Electrophysiology DAQ */
    wet_hal_status_t (*stim_voltage)(wet_hal_driver_t* drv, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
    wet_hal_status_t (*stim_current)(wet_hal_driver_t* drv, uint16_t channel, int32_t current_pA, uint32_t duration_us);
    wet_hal_status_t (*read_ephys)(wet_hal_driver_t* drv, float* voltages_out, uint8_t* spikes_out, uint32_t channel_count);
    wet_hal_status_t (*measure_impedance)(wet_hal_driver_t* drv, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
    wet_hal_status_t (*active_discharge)(wet_hal_driver_t* drv, uint16_t channel);

    /* Microfluidics & Actuators */
    wet_hal_status_t (*write_pump)(wet_hal_driver_t* drv, uint8_t pump_id, double rate_ul_min, uint8_t run_flag);
    wet_hal_status_t (*dispense_volume)(wet_hal_driver_t* drv, uint8_t pump_id, double volume_ul);
    wet_hal_status_t (*write_valve)(wet_hal_driver_t* drv, uint8_t valve_id, uint8_t state);
    wet_hal_status_t (*read_flow)(wet_hal_driver_t* drv, uint8_t sensor_id, double* out_flow_ul_min);
    wet_hal_status_t (*read_pressure)(wet_hal_driver_t* drv, uint8_t port_id, float* out_kpa);
} wet_hal_ops_t;

/* Driver instance structure */
struct wet_hal_driver {
    char                  name[32];
    wet_hal_driver_type_t driver_type;
    wet_hal_mode_t        mode;
    uint8_t               is_initialized;
    uint8_t               is_active;
    const wet_hal_ops_t*  ops;
    void*                 context;
    wet_hal_driver_t*     next;
};

#define WET_HAL_CROWBAR_BLEED_RESISTOR_OHMS 700000.0f /* 700 kOhm: guarantees <= 10 uA surge from +/-7.0 V compliance rail */
#define WET_HAL_MAX_DEAD_HEAD_PRESSURE_KPA  150.0f   /* 150 kPa safety cutoff threshold */
#define WET_HAL_ASYNC_QUEUE_CAPACITY        64

/* Asynchronous Microfluidic Command Packet */
typedef enum {
    WET_ASYNC_CMD_NONE           = 0,
    WET_ASYNC_CMD_PUMP_RATE      = 1,
    WET_ASYNC_CMD_PUMP_DISPENSE  = 2,
    WET_ASYNC_CMD_VALVE_SET      = 3,
    WET_ASYNC_CMD_BUS_RECOVERY   = 4
} wet_async_cmd_type_t;

typedef struct {
    uint8_t  cmd_type;    /* wet_async_cmd_type_t */
    uint8_t  device_id;   /* pump_id or valve_id */
    uint8_t  state;       /* run_flag or valve state */
    uint8_t  padding;
    double   param_val;   /* rate_ul_min or volume_ul */
    uint64_t submit_tick;
} wet_async_cmd_t;

/* HAL Configuration */
typedef struct {
    wet_hal_mode_t mode;
    uint32_t       max_ephys_channels;
    uint32_t       num_pumps;
    uint32_t       num_valves;
    uint32_t       num_flow_sensors;
    uint8_t        enable_dead_head_protection;
    uint8_t        enable_crowbar_fastpath;
    uint8_t        valve_for_pump[8]; /* Associated downstream valve for dead-head protection */
    float          max_line_pressure_kpa; /* Maximum inline fluidic pressure threshold (default 150.0 kPa) */
} wet_hal_config_t;

/* HAL Hardware Statistics & Telemetry */
typedef struct {
    uint64_t total_spi_transactions;
    uint64_t total_i2c_transactions;
    uint64_t total_rs232_commands;
    uint64_t total_can_frames;
    uint64_t total_crowbar_events;
    uint64_t last_crowbar_timestamp_us;
    uint32_t last_crowbar_reason;
    double   crowbar_latency_us;
} wet_hal_telemetry_t;

/* HAL Context / Router Registry */
#define WET_HAL_MAX_DRIVERS 16

struct wet_hal_context {
    wet_hal_mode_t       mode;
    wet_hal_config_t     config;
    wet_vm_t*            vm; /* Attached VM */

    /* Registered Drivers */
    wet_hal_driver_t*    drivers[WET_HAL_MAX_DRIVERS];
    uint32_t             driver_count;

    /* Primary specialized driver slots for zero-search O(1) routing */
    wet_hal_driver_t*    ephys_driver;
    wet_hal_driver_t*    pump_driver;
    wet_hal_driver_t*    valve_driver;
    wet_hal_driver_t*    flow_driver;
    wet_hal_driver_t*    can_driver;

    /* Actuator & Sensor Caches */
    float                pump_rates_ul_min[8];
    uint8_t              valve_states[8];
    double               flow_rates_ul_min[8];
    float                fluid_pressure_kpa[8];
    float                ephys_voltages[64];
    uint8_t              ephys_spikes[64];

    /* Emergency Crowbar Status */
    uint8_t              crowbar_tripped;
    uint32_t             crowbar_reason;
    uint64_t             crowbar_tick;
    uint64_t             crowbar_timestamp_us;

    /* Asynchronous Microfluidics Lockless Command Queue */
    wet_async_cmd_t      async_queue[WET_HAL_ASYNC_QUEUE_CAPACITY];
    volatile uint32_t    async_head;
    volatile uint32_t    async_tail;

    /* Telemetry Counters */
    wet_hal_telemetry_t  telemetry;
};

/* =========================================================================
 * Core HAL API Prototypes
 * ========================================================================= */

WET_EXPORT wet_hal_context_t* wet_hal_create(wet_hal_mode_t mode, const wet_hal_config_t* config);
WET_EXPORT void wet_hal_destroy(wet_hal_context_t* hal);

WET_EXPORT wet_hal_status_t wet_hal_init(wet_vm_t* vm, wet_hal_mode_t mode, const wet_hal_config_t* config);
WET_EXPORT wet_hal_status_t wet_hal_attach(wet_vm_t* vm, wet_hal_context_t* hal);
WET_EXPORT wet_hal_context_t* wet_hal_get_context(wet_vm_t* vm);

WET_EXPORT wet_hal_status_t wet_hal_set_mode(wet_hal_context_t* hal, wet_hal_mode_t mode);
WET_EXPORT wet_hal_mode_t wet_hal_get_mode(const wet_hal_context_t* hal);

WET_EXPORT wet_hal_status_t wet_hal_register_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver);
WET_EXPORT wet_hal_status_t wet_hal_unregister_driver(wet_hal_context_t* hal, wet_hal_driver_t* driver);
WET_EXPORT wet_hal_driver_t* wet_hal_find_driver(wet_hal_context_t* hal, wet_hal_driver_type_t type);

/* Actuator & Sensor Dispatch */
WET_EXPORT wet_hal_status_t wet_hal_write_pump(wet_hal_context_t* hal, uint8_t pump_id, double rate_ul_min, uint8_t run_flag);
WET_EXPORT wet_hal_status_t wet_hal_dispense_pump(wet_hal_context_t* hal, uint8_t pump_id, double volume_ul);
WET_EXPORT wet_hal_status_t wet_hal_write_valve(wet_hal_context_t* hal, uint8_t valve_id, uint8_t state);
WET_EXPORT wet_hal_status_t wet_hal_read_flow(wet_hal_context_t* hal, uint8_t sensor_id, double* out_flow_ul_min);
WET_EXPORT wet_hal_status_t wet_hal_stim_current(wet_hal_context_t* hal, uint16_t channel, int32_t current_pA, uint32_t duration_us);
WET_EXPORT wet_hal_status_t wet_hal_stim_voltage(wet_hal_context_t* hal, uint16_t channel, float voltage_v, float p1_ms, float p2_ms);
WET_EXPORT wet_hal_status_t wet_hal_read_spikes(wet_hal_context_t* hal, uint16_t channel, uint8_t* out_spike_flag);
WET_EXPORT wet_hal_status_t wet_hal_measure_impedance(wet_hal_context_t* hal, uint16_t channel, float freq_hz, float* out_mag_ohms, float* out_phase_rad);
WET_EXPORT wet_hal_status_t wet_hal_active_discharge(wet_hal_context_t* hal, uint16_t channel);

/* Emergency Hardware Crowbar Fast-Path (<100 µs) */
WET_EXPORT void wet_hal_emergency_crowbar(wet_vm_t* vm, uint32_t trip_reason);

/* Asynchronous Microfluidics Queue APIs (Decouples 10 kHz Ephys from slow RS-232 / I2C) */
WET_EXPORT wet_hal_status_t wet_hal_async_enqueue(wet_hal_context_t* hal, const wet_async_cmd_t* cmd);
WET_EXPORT uint32_t wet_hal_process_async_queue(wet_hal_context_t* hal);

/* Standard 9-SCL-pulse I2C bus recovery routine */
WET_EXPORT wet_hal_status_t wet_hal_i2c_bus_recovery(wet_hal_context_t* hal);

/* Physical inline pressure transducer setter for dead-head monitoring */
WET_EXPORT void wet_hal_set_inline_pressure(wet_hal_context_t* hal, uint8_t port, float pressure_kpa);

/* Telemetry & Mapping Accessors */
WET_EXPORT wet_hal_telemetry_t* wet_hal_get_telemetry(wet_hal_context_t* hal);
WET_EXPORT void wet_hal_set_valve_for_pump(wet_hal_context_t* hal, uint8_t pump_id, uint8_t valve_id);

/* High-resolution timer utility (monotonic microseconds) */
WET_EXPORT uint64_t wet_hal_get_time_us(void);

#ifdef __cplusplus
}
#endif

#endif /* WET_HAL_H */
