"""
WetLang Compiler - Token Definitions and Physical Units
Zero external dependencies. Hand-crafted from first principles.
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Optional, Dict, Tuple


class Dimension(Enum):
    """Physical dimensions supported by the WetLang type system."""
    NONE = "NONE"
    TIME = "TIME"
    VOLTAGE = "VOLTAGE"
    CURRENT = "CURRENT"
    CHARGE = "CHARGE"
    FREQUENCY = "FREQUENCY"
    LENGTH = "LENGTH"
    VOLUME = "VOLUME"
    FLOW_RATE = "FLOW_RATE"
    PRESSURE = "PRESSURE"


class TokenType(Enum):
    # End of File
    EOF = auto()

    # Literals
    INT_LIT = auto()
    FLOAT_LIT = auto()
    BOOL_LIT = auto()
    STRING_LIT = auto()
    PHYSICAL_LIT = auto()

    # Identifiers
    IDENTIFIER = auto()

    # Keywords - MEA & Hardware Topology
    GRID = auto()
    CHANNEL = auto()
    MODE = auto()
    ORGANOID = auto()
    TISSUE = auto()
    CONNECT = auto()
    PORT = auto()
    PUMP = auto()
    VALVE = auto()
    MOTOR = auto()
    SENSOR = auto()
    ACTUATOR = auto()

    # Channel Mode Enum Literals
    BIPHASIC_STIM = auto()
    SPIKE_READOUT = auto()
    VOLTAGE_SENSE = auto()
    BIDIRECTIONAL = auto()

    # Keywords - Declarations & Types
    FN = auto()
    LET = auto()
    MUT = auto()
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    STRING = auto()

    # Physical Type Keywords
    TYPE_VOLTAGE = auto()
    TYPE_CURRENT = auto()
    TYPE_TIME = auto()
    TYPE_FREQUENCY = auto()
    TYPE_LENGTH = auto()
    TYPE_CHARGE = auto()

    # Keywords - Closed-Loop Control
    STREAM = auto()
    BIND = auto()
    CYCLE = auto()

    # Keywords - Control Flow
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    IN = auto()
    RETURN = auto()

    # Keywords - Domain Biophysical Primitives
    STIM_BIPHASIC = auto()
    MODULATE_STDP = auto()
    SYNC_TICK = auto()
    READ_SPIKES = auto()
    READ_VOLTAGE = auto()
    POP_FIRING_RATE = auto()
    READ_POPULATION_RATE = auto()
    PUMP_SET_RATE = auto()
    PUMP_DISPENSE = auto()
    VALVE_SET = auto()
    VALVE_OPEN = auto()
    VALVE_CLOSE = auto()
    MOTOR_STEP = auto()
    READ_PRESSURE = auto()
    READ_TEMPERATURE = auto()

    # Boolean Literals
    TRUE = auto()
    FALSE = auto()

    # Operators - Arithmetic
    PLUS = auto()           # +
    MINUS = auto()          # -
    STAR = auto()           # *
    SLASH = auto()          # /
    PERCENT = auto()        # %

    # Operators - Relational
    EQ_EQ = auto()          # ==
    NOT_EQ = auto()         # !=
    LT = auto()             # <
    LT_EQ = auto()          # <=
    GT = auto()             # >
    GT_EQ = auto()          # >=

    # Operators - Logical
    AND_AND = auto()        # &&
    OR_OR = auto()          # ||
    NOT = auto()            # !

    # Operators - Assignment & Flow
    ASSIGN = auto()         # =
    ARROW_RIGHT = auto()    # ->
    ARROW_LEFT = auto()     # <-
    DOT_DOT = auto()        # ..

    # Delimiters
    LPAREN = auto()         # (
    RPAREN = auto()         # )
    LBRACE = auto()         # {
    RBRACE = auto()         # }
    LBRACKET = auto()       # [
    RBRACKET = auto()       # ]
    COMMA = auto()          # ,
    COLON = auto()          # :
    SEMICOLON = auto()      # ;
    DOT = auto()            # .


# Unit suffix mapping: suffix -> (Dimension, scale_factor_to_SI_base)
UNIT_SUFFIXES: Dict[str, Tuple[Dimension, float]] = {
    # Time (base: seconds)
    "s": (Dimension.TIME, 1.0),
    "ms": (Dimension.TIME, 1e-3),
    "us": (Dimension.TIME, 1e-6),

    # Voltage (base: volts)
    "V": (Dimension.VOLTAGE, 1.0),
    "mV": (Dimension.VOLTAGE, 1e-3),
    "uV": (Dimension.VOLTAGE, 1e-6),

    # Current (base: amperes)
    "A": (Dimension.CURRENT, 1.0),
    "uA": (Dimension.CURRENT, 1e-6),
    "nA": (Dimension.CURRENT, 1e-9),
    "pA": (Dimension.CURRENT, 1e-12),

    # Charge (base: coulombs)
    "C": (Dimension.CHARGE, 1.0),
    "nC": (Dimension.CHARGE, 1e-9),
    "pC": (Dimension.CHARGE, 1e-12),

    # Frequency (base: hertz)
    "Hz": (Dimension.FREQUENCY, 1.0),

    # Length (base: meters)
    "mm": (Dimension.LENGTH, 1e-3),
    "um": (Dimension.LENGTH, 1e-6),

    # Volume & Microfluidics
    "uL": (Dimension.VOLUME, 1e-9),
    "mL": (Dimension.VOLUME, 1e-6),
    "uL/min": (Dimension.FLOW_RATE, 1e-9 / 60.0),
    "mL/min": (Dimension.FLOW_RATE, 1e-6 / 60.0),
    "rpm": (Dimension.FREQUENCY, 1.0 / 60.0),
    "degC": (Dimension.NONE, 1.0),

    # Pressure (base: Pascals)
    "Pa": (Dimension.PRESSURE, 1.0),
    "kPa": (Dimension.PRESSURE, 1000.0),
    "mmHg": (Dimension.PRESSURE, 133.322),
}

# Sorted unit suffixes by descending length so multi-char suffixes match before single-char (e.g. "ms" before "s")
SORTED_UNIT_SUFFIXES = sorted(UNIT_SUFFIXES.keys(), key=lambda s: len(s), reverse=True)


KEYWORDS: Dict[str, TokenType] = {
    "grid": TokenType.GRID,
    "channel": TokenType.CHANNEL,
    "mode": TokenType.MODE,
    "organoid": TokenType.ORGANOID,
    "tissue": TokenType.TISSUE,
    "connect": TokenType.CONNECT,
    "port": TokenType.PORT,
    "pump": TokenType.PUMP,
    "valve": TokenType.VALVE,
    "motor": TokenType.MOTOR,
    "sensor": TokenType.SENSOR,
    "actuator": TokenType.ACTUATOR,
    "BiphasicStim": TokenType.BIPHASIC_STIM,
    "SpikeReadout": TokenType.SPIKE_READOUT,
    "VoltageSense": TokenType.VOLTAGE_SENSE,
    "Bidirectional": TokenType.BIDIRECTIONAL,
    "fn": TokenType.FN,
    "let": TokenType.LET,
    "mut": TokenType.MUT,
    "int": TokenType.INT,
    "float": TokenType.FLOAT,
    "bool": TokenType.BOOL,
    "string": TokenType.STRING,
    "Voltage": TokenType.TYPE_VOLTAGE,
    "Current": TokenType.TYPE_CURRENT,
    "Time": TokenType.TYPE_TIME,
    "Frequency": TokenType.TYPE_FREQUENCY,
    "Length": TokenType.TYPE_LENGTH,
    "Charge": TokenType.TYPE_CHARGE,
    "stream": TokenType.STREAM,
    "bind": TokenType.BIND,
    "cycle": TokenType.CYCLE,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "while": TokenType.WHILE,
    "for": TokenType.FOR,
    "in": TokenType.IN,
    "return": TokenType.RETURN,
    "stim_biphasic": TokenType.STIM_BIPHASIC,
    "modulate_stdp": TokenType.MODULATE_STDP,
    "sync_tick": TokenType.SYNC_TICK,
    "read_spikes": TokenType.READ_SPIKES,
    "read_voltage": TokenType.READ_VOLTAGE,
    "pop_firing_rate": TokenType.POP_FIRING_RATE,
    "read_population_rate": TokenType.READ_POPULATION_RATE,
    "pump_set_rate": TokenType.PUMP_SET_RATE,
    "pump_dispense": TokenType.PUMP_DISPENSE,
    "valve_set": TokenType.VALVE_SET,
    "valve_open": TokenType.VALVE_OPEN,
    "valve_close": TokenType.VALVE_CLOSE,
    "motor_step": TokenType.MOTOR_STEP,
    "read_pressure": TokenType.READ_PRESSURE,
    "read_temperature": TokenType.READ_TEMPERATURE,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
}


@dataclass
class Token:
    """Represents a scanned lexical token with position and dimensional metadata."""
    type: TokenType
    value: Any
    line: int
    column: int
    dimension: Dimension = Dimension.NONE
    si_value: Optional[float] = None
    raw_text: str = ""

    def __repr__(self) -> str:
        if self.dimension != Dimension.NONE:
            return f"Token({self.type.name}, val={self.value!r}, si={self.si_value}, dim={self.dimension.value}, L{self.line}:C{self.column})"
        return f"Token({self.type.name}, val={self.value!r}, L{self.line}:C{self.column})"
