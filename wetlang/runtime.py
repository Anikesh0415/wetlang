"""
WetLang High-Level Virtual Machine Runtime Wrapper (Compatibility Forwarder)
"""
import sys
from pathlib import Path

_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

from bindings.ffi import (
    load_wetvm_lib,
    WetStatus,
    WetVMConfig,
    WetTelemetry,
    WetActuatorTelemetry,
    WetHalMode,
    WetHalConfig,
    WetHalStatus,
)
from bindings.runtime import WetRuntime, WetVMError

__all__ = [
    "load_wetvm_lib",
    "WetStatus",
    "WetVMConfig",
    "WetTelemetry",
    "WetActuatorTelemetry",
    "WetHalMode",
    "WetHalConfig",
    "WetHalStatus",
    "WetRuntime",
    "WetVMError",
]
