"""
WetLang - The Neural Organoid Computing Platform & Neuromorphic Runtime
Project Janus: Dual-Substrate Execution for Biological Wetware & Neuromorphic Silicon.
"""

import sys
from pathlib import Path

# Ensure root repository directory is in sys.path
_root_dir = str(Path(__file__).resolve().parent.parent)
if _root_dir not in sys.path:
    sys.path.insert(0, _root_dir)

from typing import Union

import compiler
import bindings
import bindings.runtime as _runtime
import sandbox
try:
    import biophysics
except ImportError:
    biophysics = None

# Backward-compatibility alias mapping in sys.modules
sys.modules["wetlang.compiler"] = compiler
sys.modules["wetlang.bindings"] = bindings
sys.modules["wetlang.runtime"] = _runtime
sys.modules["wetlang.sandbox"] = sandbox
if biophysics:
    sys.modules["wetlang.biophysics"] = biophysics

from compiler.emitter import compile_source, compile_to_embedded_header, Target
from wetlang.vm import VirtualMachine
from wetlang import tensors
from wetlang import gym
from wetlang.gym import WetworldGymEnv

from bindings.ffi import WetStatus, WetVMConfig, WetTelemetry
from bindings.runtime import WetRuntime, WetVMError

__version__ = "2.1.2"


def compile(source: str, target: str = "sim") -> Union[bytes, str]:
    """Compiles .wet source code string to .wbc bytecode or neuromorphic target script."""
    return compile_source(source, target=target)


def load(source_or_file: Union[str, Path, bytes], target: str = "sim") -> VirtualMachine:
    """Loads a .wet source string, .wet file, or .wbc binary into a VirtualMachine."""
    return VirtualMachine(source_or_file, target=target)


__all__ = [
    "compile",
    "compile_to_embedded_header",
    "load",
    "VirtualMachine",
    "WetworldGymEnv",
    "Target",
    "tensors",
    "gym",
    "WetStatus",
    "WetVMConfig",
    "WetTelemetry",
    "WetRuntime",
    "WetVMError",
    "compiler",
    "bindings",
    "sandbox",
    "biophysics",
    "__version__",
]
