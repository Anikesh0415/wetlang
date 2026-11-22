"""
WetLang: Domain-Specific Programming Language & Cyber-Physical Engine
for Neural Organoid Computing on Microelectrode Arrays (MEA) & Microfluidics.
"""

__version__ = "1.1.0"
__author__ = "Anikesh Tiwari (Surat, Gujarat, India) / Wetworld"
__license__ = "Apache-2.0"

import sys
from pathlib import Path

# Add wetlang package root to sys.path
_pkg_root = Path(__file__).resolve().parent
if str(_pkg_root) not in sys.path:
    sys.path.insert(0, str(_pkg_root))

from wetlang.compiler.token import Dimension
from wetlang.compiler.lexer import Lexer
from wetlang.compiler.parser import Parser
from wetlang.compiler.semantic import SemanticAnalyzer
from wetlang.compiler.emitter import BytecodeEmitter, compile_source, disassemble
from wetlang.compiler.crypto_signer import sign_bytecode, verify_bytecode_signature
from wetlang.compiler.isa import Opcode, Capability
from wetlang.compiler.nir_bridge import NIRGraph, validate_dales_principle, decompose_to_dales_principle

from wetlang.bindings.runtime import WetVM, WetRuntime, WetVMError
from wetlang.bindings.ffi import WetStatus, WetTelemetry, WetActuatorTelemetry, WetVMConfig
from wetlang.bindings.scheduler import WetScheduler, WetSchedulerConfig, WetSchedulerStats, WetStimCommand

from wetlang.sandbox.universal_organoid_sandbox import UniversalOrganoidSandbox, OrganoidNode
from wetlang.sandbox.gym_env import WetworldGymEnv

__all__ = [
    "compile_source",
    "disassemble",
    "Lexer",
    "Parser",
    "SemanticAnalyzer",
    "BytecodeEmitter",
    "sign_bytecode",
    "verify_bytecode_signature",
    "Opcode",
    "Capability",
    "Dimension",
    "NIRGraph",
    "validate_dales_principle",
    "decompose_to_dales_principle",
    "WetVM",
    "WetRuntime",
    "WetVMError",
    "WetStatus",
    "WetTelemetry",
    "WetActuatorTelemetry",
    "WetVMConfig",
    "WetScheduler",
    "WetSchedulerConfig",
    "WetSchedulerStats",
    "WetStimCommand",
    "UniversalOrganoidSandbox",
    "OrganoidNode",
    "WetworldGymEnv",
]
