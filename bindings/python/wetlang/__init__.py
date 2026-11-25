"""
WetLang Python Package Interface (bindings/python/wetlang)
Mirrors root wetlang package for standard distribution.
"""

import sys
from pathlib import Path

# Ensure root repository is on sys.path
_root = str(Path(__file__).resolve().parent.parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

from wetlang import (
    compile,
    compile_to_embedded_header,
    load,
    VirtualMachine,
    WetworldGymEnv,
    Target,
    tensors,
    gym,
    WetStatus,
    WetVMConfig,
    WetTelemetry,
    WetRuntime,
    WetVMError,
    __version__,
    __all__,
)
