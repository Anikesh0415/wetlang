"""
WetLang - The Neural Organoid Computing Platform & Neuromorphic Runtime
Project Janus: Dual-Substrate Execution for Biological Wetware & Neuromorphic Silicon.
"""

from typing import Union
from pathlib import Path

from compiler.emitter import compile_source, compile_to_embedded_header, Target
from wetlang.vm import VirtualMachine
from wetlang import tensors
from wetlang import gym

from bindings.ffi import WetStatus, WetVMConfig, WetTelemetry
from bindings.runtime import WetRuntime, WetVMError

__version__ = "2.1.2"


def compile(source: str, target: str = "sim") -> bytes:
    """Compiles .wet source code string directly to .wbc binary bytecode."""
    return compile_source(source, target=target)


def load(source_or_file: Union[str, Path, bytes], target: str = "sim") -> VirtualMachine:
    """Loads a .wet source string, .wet file, or .wbc binary into a VirtualMachine."""
    return VirtualMachine(source_or_file, target=target)


__all__ = [
    "compile",
    "compile_to_embedded_header",
    "load",
    "VirtualMachine",
    "Target",
    "tensors",
    "gym",
    "WetStatus",
    "WetVMConfig",
    "WetTelemetry",
    "WetRuntime",
    "WetVMError",
    "__version__",
]
