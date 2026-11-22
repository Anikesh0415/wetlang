"""
WetLang E2E Test Suite Package
"""

import os
import sys

# Ensure project root is in sys.path
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from .common import (
    HAS_COMPILER,
    HAS_NATIVE_VM,
    HAS_BIOPHYSICS,
    HAS_INTERLOCKS,
    HAS_BENCHMARKS,
    WetLangE2ETestCase,
    require_feature,
    skip_if_unavailable,
    require_compiler,
    require_native_vm,
    require_biophysics,
    require_interlocks,
    require_benchmarks,
)

__all__ = [
    "HAS_COMPILER",
    "HAS_NATIVE_VM",
    "HAS_BIOPHYSICS",
    "HAS_INTERLOCKS",
    "HAS_BENCHMARKS",
    "WetLangE2ETestCase",
    "require_feature",
    "skip_if_unavailable",
    "require_compiler",
    "require_native_vm",
    "require_biophysics",
    "require_interlocks",
    "require_benchmarks",
]
