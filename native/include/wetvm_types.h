#ifndef WETVM_TYPES_H
#define WETVM_TYPES_H

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/* =========================================================================
 * WetLang Bytecode (WBC) Binary Header and Constants
 * ========================================================================= */

#define WET_HEADER_MAGIC "WETB"
#define WET_HEADER_MAGIC_INT 0x42544557U /* Little-endian 'W','E','T','B' */
#define WET_HEADER_SIZE 32
#define WET_VERSION_MAJOR 1
#define WET_VERSION_MINOR 0

#define WET_SECTION_ENTRY_SIZE 12

/* Capability Bitmask Flags matching compiler/isa.py */
typedef enum {
    WET_CAP_NONE            = 0x0000,
    WET_CAP_STIMULATION     = 0x0001, /* Performs electrical stimulation */
    WET_CAP_PLASTICITY      = 0x0002, /* Modifies STDP synaptic weights */
    WET_CAP_CLOSED_LOOP     = 0x0004, /* Executes sensory-motor feedback stream */
    WET_CAP_HIGH_VOLTAGE    = 0x0008, /* Requests voltages between 0.8 V and 1.2 V */
    WET_CAP_MULTI_ELECTRODE = 0x0010, /* Uses more than 16 electrodes concurrently */
    WET_CAP_MICROFLUIDICS   = 0x0020, /* Drives physical microfluidic pumps & valves */
    WET_CAP_MOTOR_ACTUATION = 0x0040, /* Drives physical stepper motors / actuators */
    WET_CAP_SIGNATURE_VERIFIED = 0x0080 /* Cryptographically signed bytecode */
} wet_capability_t;

/* Section Types matching compiler/isa.py */
typedef enum {
    WET_SEC_CONSTANT_POOL   = 1,
    WET_SEC_TOPOLOGY_CONFIG = 2,
    WET_SEC_BYTECODE_STREAM = 3,
    WET_SEC_SAFETY_MANIFEST = 4,
    WET_SEC_DEBUG_LINE_MAP  = 5
} wet_section_type_t;

/* Status / Error Codes */
typedef enum {
    WET_OK                     = 0,
    WET_ERR_INVALID_MAGIC      = 1,
    WET_ERR_CRC_MISMATCH       = 2,
    WET_ERR_UNSUPPORTED_VERSION= 3,
    WET_ERR_MALFORMED_SECTION  = 4,
    WET_ERR_STACK_OVERFLOW     = 5,
    WET_ERR_STACK_UNDERFLOW    = 6,
    WET_ERR_INVALID_OPCODE     = 7,
    WET_ERR_OUT_OF_BOUNDS_CH   = 8,
    WET_ERR_DIVISION_BY_ZERO   = 9,
    WET_ERR_NULL_PTR           = 10,
    WET_ERR_ALLOC_FAILED       = 11,
    WET_ERR_HALTED             = 12,
    WET_ERR_CHARGE_IMBALANCE   = 13,
    WET_ERR_EPILEPTIFORM_RUNAWAY = 14,
    WET_ERR_CAPABILITY_DENIED  = 15,
    WET_ERR_INTERLOCK_LOCKED   = 16,
    WET_ERR_WATCHDOG_TIMEOUT   = 17,
    WET_ERR_DC_DRIFT           = 18,
    WET_ERR_CHARGE_DENSITY_EXCEEDED = 19,
    WET_ERR_FOCAL_EXCITOTOXICITY = 20,
    WET_ERR_SHEAR_STRESS_EXCEEDED = 21,
    WET_ERR_SECURITY_UNTRUSTED    = 22,
    WET_ERR_ACTUATOR_FAULT        = 23,
    WET_ERR_THERMAL_LIMIT         = 24,
    WET_ERR_BUBBLE_DETECTED       = 25,
    WET_ERR_COMPLIANCE_RAILED     = 26,
    WET_ERR_BYTECODE_VERIFICATION = 27
} wet_status_t;

/* Opcode Table (30+ Opcodes) matching compiler/isa.py */
typedef enum {
    /* Control */
    WET_OP_NOP          = 0x00,
    WET_OP_HALT         = 0x01,
    WET_OP_SYNC_TICK    = 0x02,
    WET_OP_SLEEP_TICKS  = 0x03, /* <H (uint16) */

    /* Stack Ops */
    WET_OP_PUSH_CONST   = 0x10, /* <H (uint16 pool index) */
    WET_OP_PUSH_INT     = 0x11, /* <i (int32) */
    WET_OP_PUSH_FLOAT   = 0x12, /* <f (float32) */
    WET_OP_POP          = 0x13,
    WET_OP_DUP          = 0x14,
    WET_OP_SWAP         = 0x15,
    WET_OP_LOAD_LOCAL   = 0x16, /* <H (uint16 local slot) */
    WET_OP_STORE_LOCAL  = 0x17, /* <H (uint16 local slot) */

    /* Arithmetic */
    WET_OP_ADD_I        = 0x20,
    WET_OP_SUB_I        = 0x21,
    WET_OP_MUL_I        = 0x22,
    WET_OP_DIV_I        = 0x23,
    WET_OP_ADD_F        = 0x24,
    WET_OP_SUB_F        = 0x25,
    WET_OP_MUL_F        = 0x26,
    WET_OP_DIV_F        = 0x27,
    WET_OP_NEG          = 0x28,
    WET_OP_MOD_I        = 0x29,

    /* Relational & Equality */
    WET_OP_CMP_EQ       = 0x30,
    WET_OP_CMP_NE       = 0x31,
    WET_OP_CMP_LT       = 0x32,
    WET_OP_CMP_LE       = 0x33,
    WET_OP_CMP_GT       = 0x34,
    WET_OP_CMP_GE       = 0x35,

    /* Control Jumps */
    WET_OP_JMP          = 0x40, /* <h (int16 relative branch offset) */
    WET_OP_JMP_IF_TRUE  = 0x41, /* <h (int16 relative branch offset) */
    WET_OP_JMP_IF_FALSE = 0x42, /* <h (int16 relative branch offset) */
    WET_OP_CALL         = 0x43, /* <HB (uint16 fn_idx, uint8 argc) */
    WET_OP_RET          = 0x44,

    /* Biophysical & Domain */
    WET_OP_STIM_BIPHASIC= 0x50, /* <B (uint8 channel) */
    WET_OP_READ_SPIKES  = 0x51, /* <B (uint8 channel) */
    WET_OP_READ_VOLTAGE = 0x52, /* <B (uint8 channel) */
    WET_OP_MODULATE_STDP= 0x53, /* <BB (uint8 pre, uint8 post) */
    WET_OP_GET_POP_RATE = 0x54,
    WET_OP_MEA_CONFIG   = 0x55, /* <BB (uint8 rows, uint8 cols) */

    /* Cyber-Physical Hardware Actuation (Pumps, Valves, Motors, Sensors) */
    WET_OP_PUMP_SET_RATE    = 0x56, /* <Bf (uint8 pump_id, float32 rate_ul_min) */
    WET_OP_PUMP_DISPENSE    = 0x57, /* <Bf (uint8 pump_id, float32 volume_ul) */
    WET_OP_VALVE_SET        = 0x58, /* <BB (uint8 valve_id, uint8 state) */
    WET_OP_MOTOR_STEP       = 0x59, /* <Bif (uint8 motor_id, int32 steps, float32 speed_rpm) */
    WET_OP_READ_PRESSURE    = 0x5A, /* <B (uint8 port_id) */
    WET_OP_READ_TEMPERATURE = 0x5B,

    /* Phase 3 Electrophysiology & Environmental Sensors */
    WET_OP_STIM_CURRENT     = 0x5C, /* <Bf (uint8 channel, float32 current_ua) */
    WET_OP_READ_PH          = 0x5D,
    WET_OP_READ_DO          = 0x5E,
    WET_OP_READ_CO2         = 0x5F,
    WET_OP_READ_BUBBLE      = 0x60, /* <B (uint8 sensor_id) */
    WET_OP_READ_FLOW        = 0x61  /* <B (uint8 sensor_id) */
} wet_opcode_t;

#pragma pack(push, 1)

/* WBC 32-Byte Header Specification (<4sBBHIIIIfI) */
typedef struct {
    uint8_t  magic[4];       /* "WETB" */
    uint8_t  version_major;  /* 1 */
    uint8_t  version_minor;  /* 0 */
    uint16_t capabilities;   /* wet_capability_t bitmask */
    uint32_t file_size;      /* Total file size in bytes */
    uint32_t checksum_crc32; /* CRC32 with bytes 12-15 zeroed */
    uint32_t num_sections;   /* Number of section table entries */
    uint32_t channel_count;  /* MEA channel count (typically 64) */
    float    max_charge_nc;  /* Upper bound static charge limit */
    uint32_t sequence_counter; /* Monotonically increasing anti-rollback security counter (0 = unconstrained) */
} wet_bytecode_header_t;

/* WBC Section Table Entry (<HHII, 12 bytes) */
typedef struct {
    uint16_t section_type;   /* wet_section_type_t */
    uint16_t reserved;       /* Reserved (0) */
    uint32_t offset;         /* Byte offset from start of file */
    uint32_t size;           /* Size of section payload in bytes */
} wet_section_header_t;

#pragma pack(pop)

#ifdef __cplusplus
}
#endif

#endif /* WETVM_TYPES_H */
