"""Tests for Pure-C Closed-Loop Hooks, SET_BLANKING (0x62), Shannon Runtime Safety & R4.1 Determinism."""

import math
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib
import pytest

from bindings.ffi import (
    WetClosedLoopCmd,
    WetClosedLoopSnapshot,
    WetStatus,
    WetVMFFI,
    WetVMConfig,
)
from bindings.runtime import WetVM, WetVMError

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NATIVE_INC_DIR = os.path.join(REPO_ROOT, "native", "include")
NATIVE_BIN_DIR = os.path.join(REPO_ROOT, "native", "bin")
C99_TEST_SRC = os.path.join(REPO_ROOT, "tests", "test_c99_closed_loop.c")


def _find_c99_compiler() -> str:
    clang = r"C:\Program Files\LLVM\bin\clang.exe"
    if os.path.isfile(clang):
        return clang
    found = shutil.which("clang") or shutil.which("gcc")
    if found:
        return found
    raise RuntimeError("No C99 compiler (clang/gcc) found")


def _build_wbc_bytes(code_bytes: bytes, capabilities: int = 0x0001, channels: int = 64) -> bytes:
    header_size = 32
    sec_entry_size = 12
    code_offset = header_size + sec_entry_size
    file_size = code_offset + len(code_bytes)

    sec_hdr = struct.pack("<HHII", 3, 0, code_offset, len(code_bytes))
    hdr_zero = struct.pack(
        "<4sBBHIIIIfI",
        b"WETB",
        1,
        0,
        capabilities,
        file_size,
        0,
        1,
        channels,
        0.5,
        1,
    )
    crc = zlib.crc32(hdr_zero + sec_hdr + code_bytes) & 0xFFFFFFFF
    hdr = struct.pack(
        "<4sBBHIIIIfI",
        b"WETB",
        1,
        0,
        capabilities,
        file_size,
        crc,
        1,
        channels,
        0.5,
        1,
    )
    return hdr + sec_hdr + code_bytes


def test_standalone_c99_closed_loop_binary():
    """Compile and run standalone C99 test binary with -std=c99 -Wall -Wextra -Werror -pedantic (zero Python GIL)."""
    compiler = _find_c99_compiler()
    temp_dir = tempfile.mkdtemp(prefix="wet_c99_closed_loop_")
    try:
        exe_name = "test_c99_closed_loop.exe" if sys.platform == "win32" else "test_c99_closed_loop"
        exe_path = os.path.join(temp_dir, exe_name)

        if sys.platform == "win32":
            wetvm_lib = os.path.join(NATIVE_BIN_DIR, "wetvm.lib")
            msvcrt_lib = os.path.join(NATIVE_BIN_DIR, "msvcrt.lib")
            kernel32_lib = os.path.join(NATIVE_BIN_DIR, "kernel32.lib")
            cmd = [
                compiler,
                "-std=c99",
                "-Wall",
                "-Wextra",
                "-Werror",
                "-pedantic",
                "-DWET_NOSTDLIB_EXE",
                "-I",
                NATIVE_INC_DIR,
                C99_TEST_SRC,
                wetvm_lib,
                msvcrt_lib,
                kernel32_lib,
                "-nostdlib",
                "-Xlinker",
                "/subsystem:console",
                "-Xlinker",
                "/entry:wet_c99_entry",
                "-o",
                exe_path,
            ]
        else:
            ext = ".so" if sys.platform != "darwin" else ".dylib"
            wetvm_orig = os.path.join(NATIVE_BIN_DIR, f"wetvm{ext}")
            libwetvm_alias = os.path.join(NATIVE_BIN_DIR, f"libwetvm{ext}")
            if os.path.isfile(wetvm_orig) and not os.path.isfile(libwetvm_alias):
                shutil.copy2(wetvm_orig, libwetvm_alias)

            cmd = [
                compiler,
                "-std=c99",
                "-Wall",
                "-Wextra",
                "-Werror",
                "-pedantic",
                "-I",
                NATIVE_INC_DIR,
                C99_TEST_SRC,
                "-L",
                NATIVE_BIN_DIR,
                f"-Wl,-rpath,{NATIVE_BIN_DIR}",
                "-lwetvm",
                "-lm",
                "-lpthread",
                "-o",
                exe_path,
            ]

        compile_res = subprocess.run(cmd, capture_output=True, text=True)
        assert compile_res.returncode == 0, (
            f"C99 compilation failed:\nSTDOUT: {compile_res.stdout}\nSTDERR: {compile_res.stderr}"
        )
        assert compile_res.stderr.strip() == "", f"C99 warnings emitted:\n{compile_res.stderr}"

        env = os.environ.copy()
        if sys.platform == "win32":
            env["PATH"] = NATIVE_BIN_DIR + os.pathsep + env.get("PATH", "")
        else:
            env["LD_LIBRARY_PATH"] = NATIVE_BIN_DIR + os.pathsep + env.get("LD_LIBRARY_PATH", "")
            env["DYLD_LIBRARY_PATH"] = NATIVE_BIN_DIR + os.pathsep + env.get("DYLD_LIBRARY_PATH", "")

        run_res = subprocess.run([exe_path], capture_output=True, text=True, env=env, timeout=30)
        assert run_res.returncode == 0, (
            f"C99 binary failed (rc={run_res.returncode}):\nSTDOUT: {run_res.stdout}\nSTDERR: {run_res.stderr}"
        )
        assert "ALL C99 CLOSED-LOOP & BLANKING TESTS PASSED" in run_res.stdout
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


def test_python_wetvm_closed_loop_hook_and_blanking():
    """Smoke-test Python WetVM closed-loop hook registration, blanking validation, and runtime Shannon safety."""
    calls = []

    def py_hook(snap: WetClosedLoopSnapshot, cmd: WetClosedLoopCmd) -> None:
        calls.append((int(snap.tick), int(snap.blanking_active[0])))
        if snap.tick == 1:
            cmd.trigger = 1
            cmd.is_current = 0
            cmd.channel = 0
            cmd.amplitude = 0.5
            cmd.phase1_ms = 0.1
            cmd.phase2_ms = 0.1
            cmd.interphase_ms = 0.0

    with WetVM(WetVMConfig(dt_ms=0.1)) as vm:
        vm.configure_blanking(0.2, enable_spatial=False)
        with pytest.raises(WetVMError) as exc_low:
            vm.configure_blanking(0.05, enable_spatial=False)
        assert exc_low.value.status == WetStatus.WET_ERR_INVALID_ARG

        with pytest.raises(WetVMError) as exc_nan:
            vm.configure_blanking(float("nan"), enable_spatial=False)
        assert exc_nan.value.status == WetStatus.WET_ERR_INVALID_ARG

        vm.register_closed_loop_hook(py_hook)
        wbc = _build_wbc_bytes(b"\x02\x01")
        vm.load_bytecode(wbc)
        executed, telem = vm.run_ticks(6)
        assert executed == 6
        assert int(telem.current_tick) == 6
        assert len(calls) == 6
        # Ticks 2, 3 active stim; ticks 4, 5 are 0.2ms post-stim blanking; tick 6 unblanked
        assert [c[1] for c in calls] == [0, 1, 1, 1, 1, 0]

        vm.register_closed_loop_hook(None)
        vm.run_ticks(3)
        assert len(calls) == 6


def test_python_set_blanking_opcode_and_shannon_runtime():
    """Verify Opcode 0x62 (SET_BLANKING <HfB) and runtime Shannon check via Python WetVM."""
    # SET_BLANKING ch=0xFFFF, 0.1ms, spatial=0; SYNC_TICK; HALT
    code = struct.pack("<BHfB", 0x62, 0xFFFF, 0.1, 0) + b"\x02\x01"
    wbc = _build_wbc_bytes(code)

    with WetVM(WetVMConfig(dt_ms=0.1)) as vm:
        assert vm.verify_bytecode(wbc) == "OK"
        vm.load_bytecode(wbc)
        vm.step_tick()

        # Configure area = 1e-4 cm^2 on channel 0 -> Q=1 uC gives log10(D*Q)=4.0 > 1.75
        vm.configure_electrode_area(0, 1e-4)
        vm.inject_current_stimulus(0, 0.0, 0.5, 0.5)  # Q=0 must succeed

        with pytest.raises(WetVMError) as exc_sh:
            vm.inject_current_stimulus(0, 1000.0, 1.0, 1.0)
        assert exc_sh.value.status == WetStatus.WET_ERR_CHARGE_DENSITY_EXCEEDED


def test_python_ffi_rng_seed_and_noise_control():
    """Verify deterministic R4.1 seed and noiseless toggle from Python WetVM."""
    with WetVM(WetVMConfig(dt_ms=0.1)) as vm1, WetVM(WetVMConfig(dt_ms=0.1)) as vm2:
        vm1.set_noise_enabled(False)
        vm2.set_noise_enabled(False)
        vm1.set_rng_seed(77777)
        vm2.set_rng_seed(77777)
        wbc = _build_wbc_bytes(b"\x02\x01")
        vm1.load_bytecode(wbc)
        vm2.load_bytecode(wbc)
        _, t1 = vm1.run_ticks(50)
        _, t2 = vm2.run_ticks(50)
        assert list(t1.voltages) == list(t2.voltages)
        assert sum(t1.spikes) == 0

        ffi = WetVMFFI()
        assert ffi.configure_blanking(vm1._handle, 0.1, False) == WetStatus.WET_OK
        assert ffi.configure_blanking(vm1._handle, 25.0, False) == WetStatus.WET_ERR_INVALID_ARG
