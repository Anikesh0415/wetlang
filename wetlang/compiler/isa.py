"""
WetLang Compiler - Instruction Set Architecture (ISA) & WBC Binary Format
Hand-crafted from first principles. Complete opcode table and 32-byte header.
"""

from enum import IntEnum
import struct
from typing import Dict, Tuple


# =========================================================================
# WBC 32-Byte Header Specification
# =========================================================================

HEADER_MAGIC = b"WETB"        # 0x57, 0x45, 0x54, 0x42
HEADER_SIZE = 32              # Fixed 32 bytes
VERSION_MAJOR = 1
VERSION_MINOR = 0

# Header format:
# magic (4s), version_major (B), version_minor (B), capabilities (H),
# file_size (I), checksum_crc32 (I), num_sections (I), channel_count (I),
# max_charge_nc (f), reserved (I)
HEADER_STRUCT_FORMAT = "<4sBBHIIIIfI"
assert struct.calcsize(HEADER_STRUCT_FORMAT) == HEADER_SIZE, "Header struct must be exactly 32 bytes"


# Capability Bitmask Flags
class Capability(IntEnum):
    NONE = 0x0000
    CAP_STIMULATION = 0x0001        # Performs electrical stimulation
    CAP_PLASTICITY = 0x0002         # Modifies STDP synaptic weights
    CAP_CLOSED_LOOP = 0x0004        # Executes sensory-motor feedback stream
    CAP_HIGH_VOLTAGE = 0x0008       # Requests voltages between 0.8 V and 1.2 V
    CAP_MULTI_ELECTRODE = 0x0010    # Uses more than 16 electrodes concurrently
    CAP_MICROFLUIDICS = 0x0020      # Drives physical microfluidic pumps & valves
    CAP_MOTOR_ACTUATION = 0x0040    # Drives physical stepper motors / actuators
    CAP_SIGNATURE_VERIFIED = 0x0080 # Cryptographically signed bytecode


# Section Types
class SectionType(IntEnum):
    CONSTANT_POOL = 1
    TOPOLOGY_CONFIG = 2
    BYTECODE_STREAM = 3
    SAFETY_MANIFEST = 4
    DEBUG_LINE_MAP = 5


# Section entry format: section_type (H), reserved (H), offset (I), size (I)
SECTION_ENTRY_FORMAT = "<HHII"
SECTION_ENTRY_SIZE = struct.calcsize(SECTION_ENTRY_FORMAT) # 12 bytes


# =========================================================================
# Opcode Table (30+ Opcodes)
# =========================================================================

class Opcode(IntEnum):
    # Control
    NOP = 0x00
    HALT = 0x01
    SYNC_TICK = 0x02
    SLEEP_TICKS = 0x03

    # Stack Ops
    PUSH_CONST = 0x10
    PUSH_INT = 0x11
    PUSH_FLOAT = 0x12
    POP = 0x13
    DUP = 0x14
    SWAP = 0x15
    LOAD_LOCAL = 0x16
    STORE_LOCAL = 0x17

    # Arithmetic
    ADD_I = 0x20
    SUB_I = 0x21
    MUL_I = 0x22
    DIV_I = 0x23
    ADD_F = 0x24
    SUB_F = 0x25
    MUL_F = 0x26
    DIV_F = 0x27
    NEG = 0x28
    MOD_I = 0x29

    # Relational & Equality
    CMP_EQ = 0x30
    CMP_NE = 0x31
    CMP_LT = 0x32
    CMP_LE = 0x33
    CMP_GT = 0x34
    CMP_GE = 0x35

    # Control Jumps
    JMP = 0x40
    JMP_IF_TRUE = 0x41
    JMP_IF_FALSE = 0x42
    CALL = 0x43
    RET = 0x44

    # Biophysical & Domain
    STIM_BIPHASIC = 0x50
    READ_SPIKES = 0x51
    READ_VOLTAGE = 0x52
    MODULATE_STDP = 0x53
    GET_POP_RATE = 0x54
    MEA_CONFIG = 0x55

    # Cyber-Physical Hardware Actuation (Pumps, Valves, Motors, Sensors)
    PUMP_SET_RATE = 0x56
    PUMP_DISPENSE = 0x57
    VALVE_SET = 0x58
    MOTOR_STEP = 0x59
    READ_PRESSURE = 0x5A
    READ_TEMPERATURE = 0x5B

    # Phase 3 Electrophysiology & Environmental Sensors
    STIM_CURRENT = 0x5C
    READ_PH = 0x5D
    READ_DO = 0x5E
    READ_CO2 = 0x5F
    READ_BUBBLE = 0x60
    READ_FLOW = 0x61


# Opcode metadata: format strings for operands (little-endian)
# Empty string means no operands.
OPCODE_OPERAND_FORMATS: Dict[Opcode, str] = {
    Opcode.NOP: "",
    Opcode.HALT: "",
    Opcode.SYNC_TICK: "",
    Opcode.SLEEP_TICKS: "<H",          # uint16 ticks
    Opcode.PUSH_CONST: "<H",           # uint16 pool index
    Opcode.PUSH_INT: "<i",             # int32
    Opcode.PUSH_FLOAT: "<f",           # float32
    Opcode.POP: "",
    Opcode.DUP: "",
    Opcode.SWAP: "",
    Opcode.LOAD_LOCAL: "<H",           # uint16 local slot
    Opcode.STORE_LOCAL: "<H",          # uint16 local slot
    Opcode.ADD_I: "",
    Opcode.SUB_I: "",
    Opcode.MUL_I: "",
    Opcode.DIV_I: "",
    Opcode.ADD_F: "",
    Opcode.SUB_F: "",
    Opcode.MUL_F: "",
    Opcode.DIV_F: "",
    Opcode.NEG: "",
    Opcode.MOD_I: "",
    Opcode.CMP_EQ: "",
    Opcode.CMP_NE: "",
    Opcode.CMP_LT: "",
    Opcode.CMP_LE: "",
    Opcode.CMP_GT: "",
    Opcode.CMP_GE: "",
    Opcode.JMP: "<h",                  # int16 branch offset
    Opcode.JMP_IF_TRUE: "<h",          # int16 branch offset
    Opcode.JMP_IF_FALSE: "<h",         # int16 branch offset
    Opcode.CALL: "<HB",                # uint16 fn_idx, uint8 argc
    Opcode.RET: "",
    Opcode.STIM_BIPHASIC: "<B",        # uint8 channel
    Opcode.READ_SPIKES: "<B",          # uint8 channel
    Opcode.READ_VOLTAGE: "<B",         # uint8 channel
    Opcode.MODULATE_STDP: "<BB",       # uint8 pre, uint8 post
    Opcode.GET_POP_RATE: "",
    Opcode.MEA_CONFIG: "<BB",          # uint8 rows, uint8 cols
    Opcode.PUMP_SET_RATE: "<Bf",       # uint8 pump_id, float32 rate_ul_min
    Opcode.PUMP_DISPENSE: "<Bf",       # uint8 pump_id, float32 volume_ul
    Opcode.VALVE_SET: "<BB",           # uint8 valve_id, uint8 state (0/1)
    Opcode.MOTOR_STEP: "<Bif",         # uint8 motor_id, int32 steps, float32 speed_rpm
    Opcode.READ_PRESSURE: "<B",        # uint8 port_id
    Opcode.READ_TEMPERATURE: "",
    Opcode.STIM_CURRENT: "<Bf",        # uint8 channel, float32 current_ua
    Opcode.READ_PH: "",
    Opcode.READ_DO: "",
    Opcode.READ_CO2: "",
    Opcode.READ_BUBBLE: "<B",          # uint8 sensor_id
    Opcode.READ_FLOW: "<B",            # uint8 sensor_id
}

OPCODE_NAMES: Dict[int, str] = {op.value: op.name for op in Opcode}
OPCODE_BY_NAME: Dict[str, Opcode] = {op.name: op for op in Opcode}
