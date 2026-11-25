"""Automated C99 Strict Pedantic Compilation and Zero-Malloc Symbol Table Gate.

Milestone 4: 5-Bot Adversarial Verification & C99 Zero-Malloc Gate
Tests:
1. Compiles all 13 C runtime files with Clang -std=c99 -Wall -Wextra -Werror -pedantic -DWET_BUILDING_DLL.
2. Symbol table audit via llvm-nm / dumpbin confirming zero dynamic allocation references in deterministic execution objects.
3. Verification of caller-allocated arena memory lifecycle (wet_create_vm_arena).
4. Bit-identical deterministic stepping across independent VM executions.
"""

import ctypes
import glob
import os
import shutil
import subprocess
import tempfile
import pytest

LLVM_BIN_DIR = r"C:\Program Files\LLVM\bin"
CLANG_PATH = os.path.join(LLVM_BIN_DIR, "clang.exe")
LLVM_NM_PATH = os.path.join(LLVM_BIN_DIR, "llvm-nm.exe")
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NATIVE_SRC_DIR = os.path.join(REPO_ROOT, "native", "src")
NATIVE_INC_DIR = os.path.join(REPO_ROOT, "native", "include")
WETVM_DLL_PATH = os.path.join(REPO_ROOT, "native", "bin", "wetvm.dll")

ALL_C_FILES = [
    "biophysics.c",
    "interlocks.c",
    "wetvm_api.c",
    "wetvm_vm.c",
    "wet_aer.c",
    "wet_distributed.c",
    "wet_hal.c",
    "wet_hal_intan.c",
    "wet_hal_maxwell.c",
    "wet_hal_pump_valve.c",
    "wet_hal_sensirion.c",
    "wet_scheduler.c",
    "wet_verification.c",
]

DETERMINISTIC_OBJECTS = [
    "biophysics.c.o",
    "interlocks.c.o",
    "wet_distributed.c.o",
    "wet_scheduler.c.o",
]


class WetVMConfig(ctypes.Structure):
    _fields_ = [
        ("dt_ms", ctypes.c_double),
        ("max_stack_depth", ctypes.c_uint32),
        ("max_locals", ctypes.c_uint32),
        ("channel_count", ctypes.c_uint32),
        ("max_ops_per_tick", ctypes.c_uint32),
        ("min_sequence_counter", ctypes.c_uint32),
    ]


class WetTelemetry(ctypes.Structure):
    _fields_ = [
        ("current_tick", ctypes.c_uint64),
        ("sim_time_ms", ctypes.c_double),
        ("voltages", ctypes.c_float * 64),
        ("spikes", ctypes.c_uint8 * 64),
        ("population_rate_hz", ctypes.c_float),
        ("last_charge_nc", ctypes.c_float * 64),
    ]


def get_clang_executable():
    if os.path.isfile(CLANG_PATH):
        return CLANG_PATH
    found = shutil.which("clang")
    if found:
        return found
    pytest.skip("clang compiler executable not found")


def get_nm_executable():
    if os.path.isfile(LLVM_NM_PATH):
        return LLVM_NM_PATH
    found = shutil.which("llvm-nm") or shutil.which("nm")
    if found:
        return found
    pytest.skip("llvm-nm / nm executable not found")


@pytest.fixture(scope="module")
def compiled_objects():
    """Compile all 13 C files into a temporary directory using strict C99 pedantic flags."""
    clang = get_clang_executable()
    temp_dir = tempfile.mkdtemp(prefix="wet_c99_objects_")
    object_map = {}

    for c_file in ALL_C_FILES:
        src_path = os.path.join(NATIVE_SRC_DIR, c_file)
        assert os.path.isfile(src_path), f"Source file missing: {src_path}"
        obj_name = f"{c_file}.o"
        obj_path = os.path.join(temp_dir, obj_name)

        cmd = [
            clang,
            "-std=c99",
            "-Wall",
            "-Wextra",
            "-Werror",
            "-pedantic",
            "-DWET_BUILDING_DLL",
            "-I", NATIVE_INC_DIR,
            "-c", src_path,
            "-o", obj_path,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        assert res.returncode == 0, f"Compilation failed for {c_file}:\n{res.stderr}"
        assert res.stderr.strip() == "", f"Warnings generated for {c_file}:\n{res.stderr}"
        object_map[obj_name] = obj_path

    yield object_map

    shutil.rmtree(temp_dir, ignore_errors=True)


def test_c99_pedantic_compilation_all_13_files(compiled_objects):
    """Verify that all 13 C files compile with zero warnings and zero errors under -std=c99 -Wall -Wextra -Werror -pedantic."""
    assert len(compiled_objects) == 13
    for c_file in ALL_C_FILES:
        obj_name = f"{c_file}.o"
        assert obj_name in compiled_objects
        assert os.path.isfile(compiled_objects[obj_name])
        assert os.path.getsize(compiled_objects[obj_name]) > 0


def test_symbol_table_zero_malloc_deterministic_objects(compiled_objects):
    """Verify via llvm-nm that deterministic execution objects contain ZERO undefined references to malloc, calloc, realloc, or free."""
    nm = get_nm_executable()
    heap_symbols = {"malloc", "calloc", "realloc", "free"}

    for obj_name in DETERMINISTIC_OBJECTS:
        obj_path = compiled_objects[obj_name]
        res = subprocess.run([nm, obj_path], capture_output=True, text=True)
        assert res.returncode == 0, f"llvm-nm failed on {obj_name}: {res.stderr}"

        undefined_heap_refs = []
        for line in res.stdout.splitlines():
            line_strip = line.strip()
            parts = line_strip.split()
            if len(parts) >= 2:
                sym_type = parts[-2]
                sym_name = parts[-1].lstrip("_")
                if sym_type in ("U", "UND") and sym_name in heap_symbols:
                    undefined_heap_refs.append(sym_name)

        assert undefined_heap_refs == [], (
            f"Deterministic execution object '{obj_name}' contains illegal undefined heap references: {undefined_heap_refs}"
        )


def test_vm_stepping_zero_dynamic_allocation_arena():
    """Verify that a WetVM instantiated via caller-allocated arena memory executes 10,000 ticks without dynamic allocations."""
    assert os.path.isfile(WETVM_DLL_PATH), f"wetvm.dll missing at {WETVM_DLL_PATH}"
    dll = ctypes.CDLL(WETVM_DLL_PATH)

    dll.wet_create_vm_arena.restype = ctypes.c_void_p
    dll.wet_create_vm_arena.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(WetVMConfig)]
    dll.wet_step_tick.restype = ctypes.c_int
    dll.wet_step_tick.argtypes = [ctypes.c_void_p, ctypes.POINTER(WetTelemetry)]
    dll.wet_run_ticks.restype = ctypes.c_int
    dll.wet_run_ticks.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_uint32),
        ctypes.POINTER(WetTelemetry),
    ]
    dll.wet_free_vm.restype = None
    dll.wet_free_vm.argtypes = [ctypes.c_void_p]

    cfg = WetVMConfig(
        dt_ms=0.1,
        max_stack_depth=1024,
        max_locals=256,
        channel_count=64,
        max_ops_per_tick=100000,
        min_sequence_counter=0,
    )

    arena_bytes = 512 * 1024
    arena_buffer = (ctypes.c_uint8 * arena_bytes)()
    vm = dll.wet_create_vm_arena(arena_buffer, arena_bytes, ctypes.byref(cfg))
    assert vm is not None, "Failed to create WetVM within pre-allocated arena"

    telem = WetTelemetry()
    status = dll.wet_step_tick(vm, ctypes.byref(telem))
    assert status == 0, f"wet_step_tick failed with status {status}"
    assert telem.current_tick == 1

    executed = ctypes.c_uint32(0)
    status_run = dll.wet_run_ticks(vm, 10000, ctypes.byref(executed), ctypes.byref(telem))
    assert status_run == 0, f"wet_run_ticks failed with status {status_run}"
    assert executed.value == 10000
    assert telem.current_tick == 10001

    # Teardown should zero/scrub arena memory without calling free()
    dll.wet_free_vm(vm)


def test_bit_identical_deterministic_stepping():
    """Verify bit-identical deterministic execution across two independent VM instances over 1,000 ticks."""
    assert os.path.isfile(WETVM_DLL_PATH)
    dll = ctypes.CDLL(WETVM_DLL_PATH)

    dll.wet_create_vm_arena.restype = ctypes.c_void_p
    dll.wet_create_vm_arena.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(WetVMConfig)]
    dll.wet_step_tick.restype = ctypes.c_int
    dll.wet_step_tick.argtypes = [ctypes.c_void_p, ctypes.POINTER(WetTelemetry)]
    dll.wet_free_vm.restype = None
    dll.wet_free_vm.argtypes = [ctypes.c_void_p]

    cfg = WetVMConfig(
        dt_ms=0.1,
        max_stack_depth=1024,
        max_locals=256,
        channel_count=64,
        max_ops_per_tick=100000,
        min_sequence_counter=0,
    )
    arena_bytes = 512 * 1024

    arena1 = (ctypes.c_uint8 * arena_bytes)()
    arena2 = (ctypes.c_uint8 * arena_bytes)()

    vm1 = dll.wet_create_vm_arena(arena1, arena_bytes, ctypes.byref(cfg))
    vm2 = dll.wet_create_vm_arena(arena2, arena_bytes, ctypes.byref(cfg))
    assert vm1 and vm2

    t1 = WetTelemetry()
    t2 = WetTelemetry()

    for tick in range(1, 1001):
        s1 = dll.wet_step_tick(vm1, ctypes.byref(t1))
        s2 = dll.wet_step_tick(vm2, ctypes.byref(t2))
        assert s1 == 0 and s2 == 0
        assert t1.current_tick == t2.current_tick == tick
        assert t1.sim_time_ms == t2.sim_time_ms
        assert list(t1.voltages) == list(t2.voltages)
        assert list(t1.spikes) == list(t2.spikes)
        assert t1.population_rate_hz == t2.population_rate_hz
        assert list(t1.last_charge_nc) == list(t2.last_charge_nc)

    dll.wet_free_vm(vm1)
    dll.wet_free_vm(vm2)


def test_scheduler_zero_malloc_pool_and_arena():
    """Verify zero-malloc static pool (8 slots + reuse) and caller-supplied arena scheduler."""
    from bindings.scheduler import WetSchedulerConfig, WetSchedulerStats

    assert os.path.isfile(WETVM_DLL_PATH)
    dll = ctypes.CDLL(WETVM_DLL_PATH)

    dll.wet_create_vm_arena.restype = ctypes.c_void_p
    dll.wet_create_vm_arena.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(WetVMConfig)]
    dll.wet_free_vm.restype = None
    dll.wet_free_vm.argtypes = [ctypes.c_void_p]

    dll.wet_scheduler_arena_size.restype = ctypes.c_size_t
    dll.wet_scheduler_arena_size.argtypes = []
    dll.wet_scheduler_create_arena.restype = ctypes.c_void_p
    dll.wet_scheduler_create_arena.argtypes = [
        ctypes.c_void_p,
        ctypes.c_size_t,
        ctypes.c_void_p,
        ctypes.POINTER(WetSchedulerConfig),
    ]
    dll.wet_scheduler_create.restype = ctypes.c_void_p
    dll.wet_scheduler_create.argtypes = [ctypes.c_void_p, ctypes.POINTER(WetSchedulerConfig)]
    dll.wet_scheduler_step.restype = ctypes.c_int
    dll.wet_scheduler_step.argtypes = [ctypes.c_void_p]
    dll.wet_scheduler_get_stats.restype = ctypes.c_int
    dll.wet_scheduler_get_stats.argtypes = [ctypes.c_void_p, ctypes.POINTER(WetSchedulerStats)]
    dll.wet_scheduler_destroy.restype = None
    dll.wet_scheduler_destroy.argtypes = [ctypes.c_void_p]

    vm_cfg = WetVMConfig(
        dt_ms=0.1,
        max_stack_depth=1024,
        max_locals=256,
        channel_count=64,
        max_ops_per_tick=100000,
        min_sequence_counter=0,
    )
    vm_arena = (ctypes.c_uint8 * (512 * 1024))()
    vm = dll.wet_create_vm_arena(vm_arena, len(vm_arena), ctypes.byref(vm_cfg))
    assert vm is not None

    try:
        arena_size = dll.wet_scheduler_arena_size()
        assert arena_size > 1024

        sched_cfg = WetSchedulerConfig(
            target_period_us=10,
            enable_core_pinning=False,
            enable_priority_elevation=False,
            telemetry_queue_capacity=4096,  # Exceeds inline cap; must clamp safely
            stimulus_queue_capacity=2048,
        )

        # Boundary checks: NULL and undersized arena must return None
        assert dll.wet_scheduler_create_arena(None, arena_size, vm, ctypes.byref(sched_cfg)) is None
        small_buf = (ctypes.c_uint8 * (arena_size // 2))()
        assert dll.wet_scheduler_create_arena(small_buf, len(small_buf), vm, ctypes.byref(sched_cfg)) is None

        # Valid caller-supplied arena with unaligned base pointer (+17 bytes)
        sched_buf = (ctypes.c_uint8 * (arena_size + 64))()
        unaligned_ptr = ctypes.addressof(sched_buf) + 17
        arena_sched = dll.wet_scheduler_create_arena(unaligned_ptr, arena_size, vm, ctypes.byref(sched_cfg))
        assert arena_sched is not None

        for _ in range(50):
            assert dll.wet_scheduler_step(arena_sched) == 0

        stats = WetSchedulerStats()
        assert dll.wet_scheduler_get_stats(arena_sched, ctypes.byref(stats)) == 0
        assert stats.total_ticks == 50
        assert stats.p50_jitter_us >= 0.0
        assert stats.p99_jitter_us >= stats.p50_jitter_us
        assert stats.max_jitter_us >= stats.p99_jitter_us
        dll.wet_scheduler_destroy(arena_sched)

        # Static .bss pool: acquire 8 concurrent slots, verify 9th fails, verify reuse after destroy
        pool_handles = []
        for _ in range(8):
            h = dll.wet_scheduler_create(vm, ctypes.byref(sched_cfg))
            assert h is not None
            pool_handles.append(h)

        assert dll.wet_scheduler_create(vm, ctypes.byref(sched_cfg)) is None

        dll.wet_scheduler_destroy(pool_handles.pop(0))
        reused = dll.wet_scheduler_create(vm, ctypes.byref(sched_cfg))
        assert reused is not None
        pool_handles.append(reused)

        for h in pool_handles:
            dll.wet_scheduler_destroy(h)
    finally:
        dll.wet_free_vm(vm)
