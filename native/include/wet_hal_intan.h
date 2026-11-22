#ifndef WET_HAL_INTAN_H
#define WET_HAL_INTAN_H

#include <stdint.h>
#include <stddef.h>
#include "wet_hal.h"

#ifdef __cplusplus
extern "C" {
#endif

/* =========================================================================
 * Intan RHS2116 Electrophysiology DAQ Driver Specification
 * 16-Channel Bidirectional SPI Interface
 * ========================================================================= */

#define INTAN_RHS2116_NUM_CHANNELS 16
#define INTAN_SPI_WORD_BITS        32
#define INTAN_PIPELINE_DELAY_WORDS 2
#define INTAN_COMPLIANCE_RAIL_VOLT 7.0f

/* SPI Command Opcode prefixes */
#define INTAN_CMD_CONVERT 0x00U /* 00xxxxxx: Convert channel [3:0] */
#define INTAN_CMD_WRITE   0x80U /* 10xxxxxx: Write register [7:0] */
#define INTAN_CMD_READ    0xC0U /* 11xxxxxx: Read register [7:0] */

/* Command Control Flags */
#define INTAN_FLAG_M_COMPLIANCE_CLEAR 0x800000U /* Bit 23: M flag */
#define INTAN_FLAG_U_UPDATE_LATCH     0x400000U /* Bit 22: U flag */

/* Current Range Selectors */
typedef enum {
    INTAN_RANGE_1X   = 0, /* 10 nA step,   range: 10 nA .. 2.55 uA */
    INTAN_RANGE_10X  = 1, /* 100 nA step,  range: 100 nA .. 25.5 uA */
    INTAN_RANGE_100X = 2  /* 10 uA step,   range: 1.0 uA .. 2.55 mA */
} intan_current_range_t;

/* Intan 32-bit SPI Command Word Structure */
typedef struct {
    uint8_t  opcode;   /* 0x00=Convert, 0x80=Write, 0xC0=Read */
    uint8_t  channel;  /* 0..15 */
    uint8_t  reg;      /* Register address 0..63 */
    uint16_t data;     /* 16-bit register payload */
    uint8_t  flag_m;   /* Compliance clear flag */
    uint8_t  flag_u;   /* Update / Latch flag */
} intan_spi_command_t;

/* Intan Hardware / HIL State */
typedef struct {
    /* SPI State */
    uint32_t tx_pipeline[INTAN_PIPELINE_DELAY_WORDS + 1];
    uint32_t rx_pipeline[INTAN_PIPELINE_DELAY_WORDS + 1];
    uint32_t pipeline_index;

    /* Register File (64 x 16-bit registers) */
    uint16_t registers[64];

    /* Channel DAC Configuration (16 channels) */
    struct {
        uint8_t               dac_val_p1;
        uint8_t               dac_val_p2;
        intan_current_range_t range;
        int32_t               current_pA;
        uint32_t              duration_us;
        uint8_t               enabled;
        uint8_t               charge_recovery_on;
        float                 impedance_ohms;
        float                 impedance_phase_rad;
    } channels[INTAN_RHS2116_NUM_CHANNELS];

    /* Compliance Monitor */
    uint16_t compliance_rail_mask; /* Bitmask of channels currently railed */
    uint32_t total_compliance_trips;

    /* Impedance Module Configuration */
    float    zcheck_freq_hz;
    float    zcheck_probe_current_pA;

    /* HIL Fault Injection Hooks */
    uint8_t  fault_force_compliance_rail;
    uint8_t  fault_spi_crc_error;
    uint8_t  fault_bus_timeout;
    uint32_t transaction_count;
} intan_device_state_t;

/* =========================================================================
 * Intan RHS2116 Driver APIs
 * ========================================================================= */

/**
 * Creates and registers an Intan RHS2116 DAQ driver instance.
 */
WET_EXPORT wet_hal_driver_t* wet_hal_intan_create(wet_hal_mode_t mode);

/**
 * Destroys an Intan RHS2116 driver instance.
 */
WET_EXPORT void wet_hal_intan_destroy(wet_hal_driver_t* drv);

/**
 * Low-level 32-bit SPI word exchange.
 */
WET_EXPORT uint32_t wet_hal_intan_spi_transfer(wet_hal_driver_t* drv, uint32_t mosi_word);

/**
 * Encodes a 32-bit SPI command word.
 */
WET_EXPORT uint32_t wet_hal_intan_encode_cmd(const intan_spi_command_t* cmd);

/**
 * Decodes a 32-bit SPI command word.
 */
WET_EXPORT void wet_hal_intan_decode_cmd(uint32_t word, intan_spi_command_t* cmd);

/**
 * Configures constant current stimulation on channel (10 nA - 2.55 mA).
 */
WET_EXPORT wet_hal_status_t wet_hal_intan_set_stim_current(
    wet_hal_driver_t* drv,
    uint8_t channel,
    int32_t current_pA,
    uint32_t duration_us
);

/**
 * Queries compliance rail register.
 */
WET_EXPORT uint16_t wet_hal_intan_get_compliance_status(wet_hal_driver_t* drv);

/**
 * Clears compliance rail register (issues command with M flag).
 */
WET_EXPORT void wet_hal_intan_clear_compliance(wet_hal_driver_t* drv);

/**
 * Performs in-situ 1 kHz AC impedance test on channel.
 */
WET_EXPORT wet_hal_status_t wet_hal_intan_measure_impedance(
    wet_hal_driver_t* drv,
    uint8_t channel,
    float freq_hz,
    float* out_mag_ohms,
    float* out_phase_rad
);

/**
 * Enables / disables active hardware charge recovery switch on channel.
 */
WET_EXPORT wet_hal_status_t wet_hal_intan_set_charge_recovery(
    wet_hal_driver_t* drv,
    uint8_t channel,
    uint8_t enable
);

/**
 * HIL Fault Injection: Inject simulated compliance railing or bus errors.
 */
WET_EXPORT void wet_hal_intan_inject_fault(
    wet_hal_driver_t* drv,
    uint8_t force_rail,
    uint8_t spi_error,
    uint8_t bus_timeout
);

#ifdef __cplusplus
}
#endif

#endif /* WET_HAL_INTAN_H */
