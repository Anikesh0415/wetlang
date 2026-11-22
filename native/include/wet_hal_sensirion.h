#ifndef WET_HAL_SENSIRION_H
#define WET_HAL_SENSIRION_H

#include <stdint.h>
#include <stddef.h>
#include "wet_hal.h"

#ifdef __cplusplus
extern "C" {
#endif

/* =========================================================================
 * Sensirion Liquid Flow Meter Driver Specification
 * SLF3x / LPG10 (I2C) & SLI Series (SHDLC over RS-485/RS-232)
 * ========================================================================= */

#define SENSIRION_I2C_ADDR_DEFAULT    0x08U
#define SENSIRION_CRC8_POLYNOMIAL     0x31U /* x^8 + x^5 + x^4 + 1 */
#define SENSIRION_CRC8_INIT           0xFFU

/* I2C 16-bit Command Words */
#define SENSIRION_CMD_START_CONT_H2O  0x3608U /* Water / Aqueous continuous */
#define SENSIRION_CMD_START_CONT_IPA  0x3615U /* Hydrocarbons / IPA */
#define SENSIRION_CMD_STOP_CONT       0x3FF9U /* Stop continuous measurement */
#define SENSIRION_CMD_SOFT_RESET      0x0006U /* General call soft reset */

/* SHDLC Protocol Definitions */
#define SHDLC_FRAME_START_STOP        0x7EU
#define SHDLC_FRAME_ESCAPE            0x7DU
#define SHDLC_ESCAPE_MASK             0x20U
#define SHDLC_MAX_FRAME_SIZE          256

/* Sensirion Flow Driver State */
typedef struct {
    /* I2C Sensor Configuration (SLF3x / LPG10) */
    uint8_t  i2c_address;
    uint16_t active_command;
    uint8_t  measurement_active;
    float    scale_factor;           /* e.g., 10.0 or 500.0 (uL/min)^-1 */
    int16_t  raw_flow_ticks;
    double   current_flow_ul_min;

    /* SHDLC State (SLI series) */
    uint8_t  shdlc_address;
    uint8_t  shdlc_rx_buffer[SHDLC_MAX_FRAME_SIZE];
    size_t   shdlc_rx_len;
    uint8_t  shdlc_in_frame;
    uint8_t  shdlc_escaped;

    /* Telemetry Counters */
    uint32_t total_i2c_reads;
    uint32_t total_shdlc_frames;
    uint32_t crc_errors;

    /* HIL Fault Injection */
    uint8_t  fault_corrupt_crc;
    uint8_t  fault_nak_address;
} sensirion_device_state_t;

/* =========================================================================
 * Sensirion Driver APIs
 * ========================================================================= */

/**
 * Creates and registers a Sensirion Flow Meter driver instance.
 */
WET_EXPORT wet_hal_driver_t* wet_hal_sensirion_create(wet_hal_mode_t mode);

/**
 * Destroys a Sensirion Flow Meter driver instance.
 */
WET_EXPORT void wet_hal_sensirion_destroy(wet_hal_driver_t* drv);

/**
 * Computes Sensirion CRC-8 checksum over buffer (poly 0x31, init 0xFF).
 */
WET_EXPORT uint8_t wet_hal_sensirion_crc8(const uint8_t* data, size_t len);

/**
 * Validates a Sensirion 3-byte measurement word ([MSB] [LSB] [CRC]).
 * Returns 1 if CRC matches, 0 otherwise.
 */
WET_EXPORT int wet_hal_sensirion_validate_crc(const uint8_t word_and_crc[3]);

/**
 * Starts continuous measurement on SLF3x / LPG10 sensor (0x3608 for H2O).
 */
WET_EXPORT wet_hal_status_t wet_hal_sensirion_start_measurement(
    wet_hal_driver_t* drv,
    uint16_t cmd
);

/**
 * Stops continuous measurement on SLF3x / LPG10 sensor (0x3FF9).
 */
WET_EXPORT wet_hal_status_t wet_hal_sensirion_stop_measurement(wet_hal_driver_t* drv);

/**
 * Reads instantaneous liquid flow rate in µL/min.
 */
WET_EXPORT wet_hal_status_t wet_hal_sensirion_read_flow(
    wet_hal_driver_t* drv,
    double* out_flow_ul_min
);

/**
 * Sets raw flow value for HIL simulation.
 */
WET_EXPORT void wet_hal_sensirion_hil_set_flow(
    wet_hal_driver_t* drv,
    double flow_ul_min
);

/**
 * Encodes an SHDLC packet with start/stop flags (0x7E), byte-stuffing, and checksum.
 * Returns length of stuffed frame written to out_buf, or 0 on buffer overflow.
 */
WET_EXPORT size_t wet_hal_shdlc_encode(
    uint8_t address,
    uint8_t command,
    const uint8_t* payload,
    uint8_t payload_len,
    uint8_t* out_buf,
    size_t out_buf_max
);

/**
 * Decodes an unstuffed SHDLC packet, verifying start/stop flags and checksum.
 * Returns 1 on success, 0 on checksum error or invalid framing.
 */
WET_EXPORT int wet_hal_shdlc_decode(
    const uint8_t* raw_buf,
    size_t raw_len,
    uint8_t* out_address,
    uint8_t* out_command,
    uint8_t* out_payload,
    uint8_t* out_payload_len
);

/**
 * HIL Fault Injection: Inject simulated CRC corruption or I2C bus NAK.
 */
WET_EXPORT void wet_hal_sensirion_inject_fault(
    wet_hal_driver_t* drv,
    uint8_t corrupt_crc,
    uint8_t nak_addr
);

#ifdef __cplusplus
}
#endif

#endif /* WET_HAL_SENSIRION_H */
