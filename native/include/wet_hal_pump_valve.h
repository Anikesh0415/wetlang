#ifndef WET_HAL_PUMP_VALVE_H
#define WET_HAL_PUMP_VALVE_H

#include <stdint.h>
#include <stddef.h>
#include "wet_hal.h"

#ifdef __cplusplus
extern "C" {
#endif

/* =========================================================================
 * Microfluidic Pump & Valve Protocol Specifications
 * Harvard Apparatus RS-232 & CAN-bus (ISO 11898-1/2) Microfluidics
 * ========================================================================= */

#define WET_MAX_PUMPS             8
#define WET_MAX_VALVES            8
#define WET_CAN_MAX_PAYLOAD       8
#define WET_CAN_QUEUE_CAPACITY    128

/* Harvard Apparatus Prompt Return Codes */
typedef enum {
    HARVARD_PROMPT_IDLE        = ':', /* Prompt : (pump stopped / idle) */
    HARVARD_PROMPT_INFUSING    = '>', /* Prompt > (pump infusing) */
    HARVARD_PROMPT_WITHDRAWING = '<', /* Prompt < (pump withdrawing) */
    HARVARD_PROMPT_STALLED     = '*', /* Prompt * (motor stalled / alarm) */
    HARVARD_PROMPT_TARGET_DONE = 'T', /* Prompt T* (target volume reached) */
    HARVARD_PROMPT_INVALID     = '?'
} harvard_prompt_t;

/* Harvard RS-232 Device Configuration */
typedef struct {
    uint8_t address;          /* Daisy-chain address 00..99 (0 = master) */
    uint8_t fast_mode;        /* 1 = use '@' prefix for sub-50 ms execution */
    double  rate_ul_min;      /* Current programmed infusion rate */
    double  infused_volume_ul;/* Cumulative dispensed volume */
    uint8_t is_running;       /* 1 = infusing, 2 = withdrawing, 0 = stopped */
    uint8_t is_stalled;       /* 1 = stall condition */
} harvard_pump_state_t;

/* CAN Message Frame (ISO 11898-1/2) */
typedef struct {
    uint32_t id;                       /* 11-bit standard or 29-bit extended ID */
    uint8_t  is_extended;              /* 1 = 29-bit CAN 2.0B, 0 = 11-bit standard */
    uint8_t  is_rtr;                   /* Remote Transmission Request */
    uint8_t  dlc;                      /* Data Length Code (0..8) */
    uint8_t  data[WET_CAN_MAX_PAYLOAD];/* Frame payload */
    uint64_t timestamp_us;             /* Monotonic arrival/tx timestamp */
} wet_can_frame_t;

/* CAN Message Type IDs */
#define CAN_ID_EMCY_BASE          0x080U /* Emergency frame: 0x080 + NodeID */
#define CAN_ID_TPDO1_BASE         0x180U /* Telemetry transmit: 0x180 + NodeID */
#define CAN_ID_RPDO1_BASE         0x200U /* Pump rate command: 0x200 + NodeID */
#define CAN_ID_RPDO2_BASE         0x300U /* Valve state command: 0x300 + NodeID */
#define CAN_ID_HEARTBEAT_BASE     0x700U /* Heartbeat: 0x700 + NodeID */

/* Valve & Pump Microfluidics State */
typedef struct {
    /* Harvard RS-232 Pumps (up to 8) */
    harvard_pump_state_t pumps[WET_MAX_PUMPS];

    /* Micro-pinch / Solenoid Valve States (0=Closed, 1=Open) */
    uint8_t              valve_states[WET_MAX_VALVES];

    /* Dead-Head Overpressure Interlock Configuration */
    uint8_t              dead_head_enabled;
    uint8_t              valve_for_pump[WET_MAX_PUMPS]; /* Associated downstream valve */
    uint32_t             dead_head_trip_count;

    /* CAN-bus Loopback & Queue */
    wet_can_frame_t      can_tx_queue[WET_CAN_QUEUE_CAPACITY];
    uint32_t             can_tx_head;
    uint32_t             can_tx_tail;
    uint32_t             can_tx_count;

    wet_can_frame_t      can_rx_queue[WET_CAN_QUEUE_CAPACITY];
    uint32_t             can_rx_head;
    uint32_t             can_rx_tail;
    uint32_t             can_rx_count;

    /* Telemetry Counters */
    uint32_t             total_rs232_tx;
    uint32_t             total_can_frames_tx;
    uint32_t             total_can_frames_rx;
    uint32_t             total_emcy_frames;

    /* HIL Fault Injection */
    uint8_t              fault_inject_stall;
    uint8_t              fault_inject_can_drop;
    uint8_t              fault_inject_rs232_timeout;
} microfluidic_state_t;

/* =========================================================================
 * Microfluidic Pump & Valve APIs
 * ========================================================================= */

/**
 * Creates and registers a microfluidic pump & valve driver instance.
 */
WET_EXPORT wet_hal_driver_t* wet_hal_microfluidics_create(wet_hal_mode_t mode);

/**
 * Destroys microfluidic driver instance.
 */
WET_EXPORT void wet_hal_microfluidics_destroy(wet_hal_driver_t* drv);

/**
 * Encodes a Harvard Apparatus RS-232 command string into out_buf.
 * (e.g. "@irate 1.500 u/m\r", "01 stp\r", etc.)
 */
WET_EXPORT int wet_hal_harvard_format_cmd(
    uint8_t address,
    uint8_t fast_mode,
    const char* cmd_name,
    const char* args,
    char* out_buf,
    size_t out_buf_len
);

/**
 * Parses a Harvard Apparatus prompt response string.
 */
WET_EXPORT harvard_prompt_t wet_hal_harvard_parse_response(
    const char* resp_buf,
    size_t resp_len
);

/**
 * Commands Harvard pump rate and run state.
 * Performs dead-head overpressure interlock check if downstream valve is closed!
 */
WET_EXPORT wet_hal_status_t wet_hal_pump_set_rate(
    wet_hal_driver_t* drv,
    uint8_t pump_id,
    double rate_ul_min,
    uint8_t run_flag
);

/**
 * Dispenses a specific volume in µL.
 */
WET_EXPORT wet_hal_status_t wet_hal_pump_dispense(
    wet_hal_driver_t* drv,
    uint8_t pump_id,
    double volume_ul
);

/**
 * Immediately stops a pump.
 */
WET_EXPORT wet_hal_status_t wet_hal_pump_stop(
    wet_hal_driver_t* drv,
    uint8_t pump_id
);

/**
 * Sets valve state (0 = closed, 1 = open).
 */
WET_EXPORT wet_hal_status_t wet_hal_valve_set_state(
    wet_hal_driver_t* drv,
    uint8_t valve_id,
    uint8_t state
);

/**
 * Configures the associated downstream valve for dead-head overpressure protection.
 */
WET_EXPORT void wet_hal_pump_bind_downstream_valve(
    wet_hal_driver_t* drv,
    uint8_t pump_id,
    uint8_t valve_id
);

/**
 * Encodes and transmits a CAN frame (ISO 11898-1/2).
 */
WET_EXPORT wet_hal_status_t wet_hal_can_send(
    wet_hal_driver_t* drv,
    const wet_can_frame_t* frame
);

/**
 * Receives the next available CAN frame from Rx queue.
 */
WET_EXPORT wet_hal_status_t wet_hal_can_recv(
    wet_hal_driver_t* drv,
    wet_can_frame_t* out_frame
);

/**
 * Emits an Emergency (EMCY) frame on the CAN bus.
 */
WET_EXPORT wet_hal_status_t wet_hal_can_send_emcy(
    wet_hal_driver_t* drv,
    uint8_t node_id,
    uint16_t error_code,
    uint8_t error_register
);

/**
 * HIL Fault Injection: Inject stall condition, CAN frame drop, or serial timeout.
 */
WET_EXPORT void wet_hal_microfluidics_inject_fault(
    wet_hal_driver_t* drv,
    uint8_t stall,
    uint8_t can_drop,
    uint8_t timeout
);

#ifdef __cplusplus
}
#endif

#endif /* WET_HAL_PUMP_VALVE_H */
