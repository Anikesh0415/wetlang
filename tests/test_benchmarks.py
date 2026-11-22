"""
WetLang Test Suite: Benchmark Execution & Telemetry Generation
Tests:
  - Compilation of 01_active_inference_closed_loop.wet
  - Compilation of 02_polychronous_reservoir_classifier.wet
  - Compilation of 03_homeostatic_stabilization_and_stress.wet
  - End-to-end execution of benchmarks in the native WetVM engine
  - Structured per-tick telemetry (JSONL and CSV) serialization and validation
"""

import os
import json
import struct
import pytest
import numpy as np
from pathlib import Path
from typing import Dict, Any

from compiler.compiler_cli import compile_source
from compiler.isa import (
    HEADER_SIZE,
    HEADER_MAGIC,
    HEADER_STRUCT_FORMAT,
    VERSION_MAJOR,
    VERSION_MINOR,
    Capability,
)
from bindings.runtime import WetVM, WetTelemetryView
from bindings.ffi import WetVMConfig


BENCHMARKS_DIR = Path(__file__).resolve().parent.parent / "benchmarks"


def load_benchmark_source(filename: str) -> str:
    path = BENCHMARKS_DIR / filename
    assert path.is_file(), f"Benchmark file missing: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def assert_wbc_header_valid(wbc_bytes: bytes) -> Dict[str, Any]:
    """Unpacks and validates the WBC 32-byte header."""
    assert len(wbc_bytes) >= HEADER_SIZE, "Bytecode shorter than 32-byte header"
    magic, v_maj, v_min, caps, fsize, crc, n_secs, ch_cnt, max_q, res = struct.unpack_from(
        HEADER_STRUCT_FORMAT, wbc_bytes, 0
    )
    assert magic == HEADER_MAGIC, f"Invalid magic: {magic}"
    assert v_maj == VERSION_MAJOR
    assert v_min == VERSION_MINOR
    assert ch_cnt == 64
    assert fsize == len(wbc_bytes)
    assert n_secs > 0
    return {
        "magic": magic,
        "version_major": v_maj,
        "version_minor": v_min,
        "capabilities": caps,
        "file_size": fsize,
        "checksum_crc32": crc,
        "num_sections": n_secs,
        "channel_count": ch_cnt,
        "max_charge_nc": max_q,
    }


# =============================================================================
# Benchmark Compilation Tests
# =============================================================================

def test_compile_benchmark_01_active_inference():
    """Verify compilation of 01_active_inference_closed_loop.wet into valid WBC binary."""
    src = load_benchmark_source("01_active_inference_closed_loop.wet")
    wbc = compile_source(src)
    header = assert_wbc_header_valid(wbc)
    
    # Must declare stimulation capability
    assert header["capabilities"] & Capability.CAP_STIMULATION.value
    assert header["channel_count"] == 64


def test_compile_benchmark_02_polychronous_reservoir():
    """Verify compilation of 02_polychronous_reservoir_classifier.wet into valid WBC binary."""
    src = load_benchmark_source("02_polychronous_reservoir_classifier.wet")
    wbc = compile_source(src)
    header = assert_wbc_header_valid(wbc)
    
    assert header["capabilities"] & Capability.CAP_STIMULATION.value
    assert header["channel_count"] == 64


def test_compile_benchmark_03_homeostatic_stabilization():
    """Verify compilation of 03_homeostatic_stabilization_and_stress.wet into valid WBC binary."""
    src = load_benchmark_source("03_homeostatic_stabilization_and_stress.wet")
    wbc = compile_source(src)
    header = assert_wbc_header_valid(wbc)
    
    assert header["capabilities"] & Capability.CAP_STIMULATION.value
    assert header["channel_count"] == 64


# =============================================================================
# Benchmark Execution & Stepping Tests in Native WetVM
# =============================================================================

def test_run_benchmark_01_in_wetvm():
    """Verify loading and stepping Benchmark 01 in native WetVM produces valid telemetry."""
    src = load_benchmark_source("01_active_inference_closed_loop.wet")
    wbc = compile_source(src)
    
    config = WetVMConfig(dt_ms=0.1, channel_count=64)
    with WetVM(config=config) as vm:
        vm.load_bytecode(wbc)
        
        # Step 50 ticks
        executed, telem = vm.run_ticks(50)
        assert executed == 50
        assert telem.current_tick == 50
        assert abs(telem.sim_time_ms - 5.0) < 1e-4  # 50 * 0.1 ms = 5.0 ms
        
        # Check telemetry array dimensions and values
        voltages = vm.get_voltages_numpy()
        assert voltages.shape == (64,)
        assert not np.any(np.isnan(voltages))
        assert not np.any(np.isinf(voltages))


def test_run_benchmark_02_in_wetvm():
    """Verify loading and stepping Benchmark 02 in native WetVM produces valid telemetry."""
    src = load_benchmark_source("02_polychronous_reservoir_classifier.wet")
    wbc = compile_source(src)
    
    config = WetVMConfig(dt_ms=0.1, channel_count=64)
    with WetVM(config=config) as vm:
        vm.load_bytecode(wbc)
        
        # Step 100 ticks (10.0 ms)
        executed, telem = vm.run_ticks(100)
        assert executed == 100
        assert telem.current_tick == 100
        assert abs(telem.sim_time_ms - 10.0) < 1e-4
        
        spikes = vm.get_spikes_numpy()
        assert spikes.shape == (64,)


def test_run_benchmark_03_in_wetvm():
    """Verify loading and stepping Benchmark 03 in native WetVM produces valid telemetry."""
    src = load_benchmark_source("03_homeostatic_stabilization_and_stress.wet")
    wbc = compile_source(src)
    
    config = WetVMConfig(dt_ms=0.1, channel_count=64)
    with WetVM(config=config) as vm:
        vm.load_bytecode(wbc)
        
        # Step 100 ticks (10.0 ms)
        executed, telem = vm.run_ticks(100)
        assert executed == 100
        assert telem.current_tick == 100
        assert abs(telem.sim_time_ms - 10.0) < 1e-4


# =============================================================================
# Structured JSONL & CSV Telemetry Emission Tests
# =============================================================================

def test_benchmark_telemetry_jsonl_formatting():
    """Verify formatting of per-tick telemetry into valid JSONL records."""
    src = load_benchmark_source("01_active_inference_closed_loop.wet")
    wbc = compile_source(src)
    
    jsonl_records = []
    with WetVM() as vm:
        vm.load_bytecode(wbc)
        for _ in range(10):
            telem = vm.step_tick()
            record = {
                "tick": int(telem.current_tick),
                "sim_time_ms": round(float(telem.sim_time_ms), 3),
                "pop_rate_hz": round(float(telem.population_rate_hz), 2),
                "mean_v_mv": round(float(np.mean(vm.get_voltages_numpy())), 3),
                "active_spikes": int(np.sum(vm.get_spikes_numpy())),
            }
            jsonl_records.append(json.dumps(record))
            
    assert len(jsonl_records) == 10
    for line in jsonl_records:
        parsed = json.loads(line)
        assert "tick" in parsed
        assert "sim_time_ms" in parsed
        assert "pop_rate_hz" in parsed
        assert "mean_v_mv" in parsed
        assert "active_spikes" in parsed


def test_benchmark_telemetry_csv_formatting():
    """Verify formatting of per-tick telemetry into structured CSV format."""
    src = load_benchmark_source("03_homeostatic_stabilization_and_stress.wet")
    wbc = compile_source(src)
    
    header = "tick,sim_time_ms,pop_rate_hz,active_spikes"
    csv_rows = [header]
    
    with WetVM() as vm:
        vm.load_bytecode(wbc)
        for _ in range(10):
            telem = vm.step_tick()
            row = f"{telem.current_tick},{telem.sim_time_ms:.1f},{telem.population_rate_hz:.2f},{np.sum(vm.get_spikes_numpy())}"
            csv_rows.append(row)
            
    assert len(csv_rows) == 11
    assert csv_rows[0] == header
    for line in csv_rows[1:]:
        parts = line.split(",")
        assert len(parts) == 4
        assert int(parts[0]) >= 1
