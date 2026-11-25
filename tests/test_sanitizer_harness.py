"""
WetLang Pillar 1: ASan / UBSan & Invariant Verification Suite
Verifies:
  1. Static Arena zero-malloc allocation & dirty memory resilience
  2. Adversarial corrupted bytecode rejection (truncation, magic tampering, CRC32 flip)
  3. 50,000 Biophysics continuous steps with material-dependent asymmetric rails (Pt [-0.6V, +0.8V])
  4. Microfluidics MEMS inline transducer overpressure (>50 kPa) & throttled recoil relief
  5. AER SPSC ring buffer pointer wrap-around & exact dropped-event accounting
  6. 64-bit AttoCoulomb resolution (0.1 fC sub-pA leakage integration with zero truncation)
"""

import ctypes
import os
import sys
from pathlib import Path

# FFI ctypes struct definition
class WetSanitizerResult(ctypes.Structure):
    _fields_ = [
        ("arena_passed", ctypes.c_uint32),
        ("corrupted_bytecode_passed", ctypes.c_uint32),
        ("biophysics_passed", ctypes.c_uint32),
        ("mems_passed", ctypes.c_uint32),
        ("aer_passed", ctypes.c_uint32),
        ("attocoulomb_passed", ctypes.c_uint32),
        ("all_passed", ctypes.c_uint32),
    ]


def _load_wetvm():
    proj_root = Path(__file__).resolve().parent.parent
    lib_name = "wetvm.dll" if sys.platform == "win32" else ("wetvm.dylib" if sys.platform == "darwin" else "wetvm.so")
    dll_path = proj_root / "native" / "bin" / lib_name
    if not dll_path.exists():
        dll_path = proj_root / "native" / lib_name
    if not dll_path.exists():
        dll_path = proj_root / "bin" / lib_name
    return ctypes.CDLL(str(dll_path))


def test_sanitizer_and_invariant_harness():
    lib = _load_wetvm()
    lib.wet_run_sanitizer_harness_c.argtypes = [ctypes.POINTER(WetSanitizerResult)]
    lib.wet_run_sanitizer_harness_c.restype = ctypes.c_int

    result = WetSanitizerResult()
    res = lib.wet_run_sanitizer_harness_c(ctypes.byref(result))

    print("\n--- Pillar 1: Sanitizer & Invariant Harness Results ---")
    print(f"  [1] Arena Zero-Malloc & Dirty Memory: {'PASS' if result.arena_passed else 'FAIL'}")
    print(f"  [2] Corrupted Bytecode Hardening:     {'PASS' if result.corrupted_bytecode_passed else 'FAIL'}")
    print(f"  [3] Biophysics & Asymmetric Clamping: {'PASS' if result.biophysics_passed else 'FAIL'}")
    print(f"  [4] MEMS Overpressure & Recoil:       {'PASS' if result.mems_passed else 'FAIL'}")
    print(f"  [5] AER Ring Buffer & Drop Telemetry: {'PASS' if result.aer_passed else 'FAIL'}")
    print(f"  [6] 64-bit AttoCoulomb Resolution:    {'PASS' if result.attocoulomb_passed else 'FAIL'}")

    assert res == 0, "Native sanitizer harness reported failure"
    assert result.arena_passed == 1
    assert result.corrupted_bytecode_passed == 1
    assert result.biophysics_passed == 1
    assert result.mems_passed == 1
    assert result.aer_passed == 1
    assert result.attocoulomb_passed == 1
    assert result.all_passed == 1
