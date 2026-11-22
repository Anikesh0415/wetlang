#ifndef WET_HAL_MAXWELL_H
#define WET_HAL_MAXWELL_H

#include <stdint.h>
#include <stddef.h>
#include "wet_hal.h"

#ifdef __cplusplus
extern "C" {
#endif

/* =========================================================================
 * MaxWell Biosystems MaxOne HD-MEA Driver Specification
 * CMOS High-Density Microelectrode Array Interface
 * ========================================================================= */

#define MAXWELL_TOTAL_ELECTRODES      26400
#define MAXWELL_RECORDING_CHANNELS    1024
#define MAXWELL_STIMULATION_UNITS     32
#define MAXWELL_PITCH_UM              17.5f
#define MAXWELL_ELECTRODE_AREA_UM2    132.25f

/* Electrochemical Safety Bounds for Platinum (Pt) Microelectrodes */
#define MAXWELL_VOLTAGE_LIMIT_MV      1000.0f /* Max safe DAC amplitude */
#define MAXWELL_MAX_DAC_BITS          335     /* Corresponding to 1000 mV */
#define MAXWELL_PT_CIC_MC_CM2         0.10f   /* Pt charge injection capacity */
#define MAXWELL_MAX_PHASE_CHARGE_NC   0.13225f/* Max safe single-phase charge in nC */

/* Sequence Buffer Capacity */
#define MAXWELL_MAX_SEQUENCE_STEPS    4096

typedef enum {
    MAXWELL_SEQ_IDLE    = 0,
    MAXWELL_SEQ_ARMED   = 1,
    MAXWELL_SEQ_RUNNING = 2,
    MAXWELL_SEQ_DONE    = 3,
    MAXWELL_SEQ_ERROR   = 4
} maxwell_seq_state_t;

/* Single step in pre-compiled hardware Sequence buffer */
typedef struct {
    uint32_t timestamp_us;     /* Offset from sequence start in microseconds */
    uint8_t  stim_unit_id;     /* 0..31 */
    uint16_t electrode_id;     /* Target electrode 0..26399 */
    int16_t  dac_val;          /* Voltage DAC value (-335 .. +335) */
    uint16_t phase_duration_us;/* Pulse duration */
} maxwell_seq_step_t;

/* MaxWell Driver State */
typedef struct {
    /* Electrode Routing Matrix (1024 recording channels mapped to 26400 electrodes) */
    uint16_t routing_matrix[MAXWELL_RECORDING_CHANNELS];
    uint8_t  channel_active[MAXWELL_RECORDING_CHANNELS];

    /* 32 Stimulation Units */
    struct {
        uint16_t connected_electrode;
        uint8_t  is_connected;
        int16_t  current_dac_val;
        float    phase1_charge_nc;
        float    phase2_charge_nc;
    } stim_units[MAXWELL_STIMULATION_UNITS];

    /* Hardware Sequence Buffer (to eliminate host OS preemption jitter) */
    maxwell_seq_step_t  sequence_buffer[MAXWELL_MAX_SEQUENCE_STEPS];
    uint32_t            sequence_length;
    uint32_t            sequence_playback_index;
    maxwell_seq_state_t sequence_state;
    uint64_t            sequence_start_time_us;

    /* Channel Readout Cache */
    float    channel_voltages[MAXWELL_RECORDING_CHANNELS];
    uint8_t  channel_spikes[MAXWELL_RECORDING_CHANNELS];

    /* Safety & Interlock Counters */
    uint32_t voltage_clamp_events;
    uint32_t charge_limit_violations;

    /* HIL Fault Injection */
    uint8_t  fault_force_charge_violation;
    uint8_t  fault_bus_dropped_frame;
} maxwell_device_state_t;

/* =========================================================================
 * MaxWell MaxOne Driver APIs
 * ========================================================================= */

/**
 * Creates and registers a MaxWell MaxOne HD-MEA driver instance.
 */
WET_EXPORT wet_hal_driver_t* wet_hal_maxwell_create(wet_hal_mode_t mode);

/**
 * Destroys a MaxWell MaxOne driver instance.
 */
WET_EXPORT void wet_hal_maxwell_destroy(wet_hal_driver_t* drv);

/**
 * Configures the switch matrix to connect 1024 recording channels to specific electrodes.
 */
WET_EXPORT wet_hal_status_t wet_hal_maxwell_route_channels(
    wet_hal_driver_t* drv,
    const uint16_t* electrode_indices,
    uint32_t count
);

/**
 * Connects a stimulation unit to a specific electrode.
 */
WET_EXPORT wet_hal_status_t wet_hal_maxwell_connect_stim(
    wet_hal_driver_t* drv,
    uint8_t stim_unit,
    uint16_t electrode_id
);

/**
 * Clears the hardware sequence buffer.
 */
WET_EXPORT void wet_hal_maxwell_sequence_clear(wet_hal_driver_t* drv);

/**
 * Appends a step to the hardware sequence buffer (enforces voltage and charge safety bounds).
 */
WET_EXPORT wet_hal_status_t wet_hal_maxwell_sequence_append(
    wet_hal_driver_t* drv,
    uint32_t timestamp_us,
    uint8_t stim_unit,
    uint16_t electrode_id,
    float voltage_mv,
    uint16_t duration_us
);

/**
 * Uploads and arms the pre-compiled sequence buffer for jitter-free execution.
 */
WET_EXPORT wet_hal_status_t wet_hal_maxwell_sequence_arm(wet_hal_driver_t* drv);

/**
 * Starts execution of the sequence.
 */
WET_EXPORT wet_hal_status_t wet_hal_maxwell_sequence_start(wet_hal_driver_t* drv);

/**
 * Queries sequence playback status.
 */
WET_EXPORT maxwell_seq_state_t wet_hal_maxwell_sequence_get_state(wet_hal_driver_t* drv);

/**
 * Immediate voltage pulse injection (with Pt safety clamping: <= 1000 mV and <= 0.13225 nC).
 */
WET_EXPORT wet_hal_status_t wet_hal_maxwell_stim_voltage(
    wet_hal_driver_t* drv,
    uint8_t stim_unit,
    uint16_t electrode_id,
    float voltage_mv,
    float phase1_ms,
    float phase2_ms
);

/**
 * HIL Fault Injection: Inject simulated charge violation or frame drop.
 */
WET_EXPORT void wet_hal_maxwell_inject_fault(
    wet_hal_driver_t* drv,
    uint8_t force_charge_violation,
    uint8_t drop_frames
);

#ifdef __cplusplus
}
#endif

#endif /* WET_HAL_MAXWELL_H */
