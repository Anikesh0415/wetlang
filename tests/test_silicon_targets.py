"""
WetLang Test Suite: Project Janus Neuromorphic Silicon Targets (Sprint Task 2)
Tests:
  - Compilation target flags (--target=sim, --target=finalspark, --target=spinnaker, --target=embedded)
  - Standalone C header generation (model_compiled.h) for embedded microcontrollers (STM32 / ESP32)
  - SpiNNaker ARM968 target header generation with sark.h / spin1_api.h includes
  - Bytecode preservation and array size validation
  - Zero-malloc static arena memory layout verification
"""

import os
import tempfile
import pytest
from compiler.emitter import (
    Target,
    compile_source,
    emit_c_embedded_header,
    compile_to_embedded_header,
)
from compiler.compiler_cli import main as wetc_main


def test_target_enum_variants():
    """Verify all Project Janus targets exist."""
    assert Target.SIM == "sim"
    assert Target.FINALSPARK == "finalspark"
    assert Target.SPINNAKER == "spinnaker"
    assert Target.EMBEDDED == "embedded"
    assert Target.CL_SDK == "cl_sdk"
    assert Target.NEUROPLATFORM == "neuroplatform"


def test_emit_c_embedded_header_basic():
    """Verify C header generation produces valid C syntax and static arena declarations."""
    src = "grid mea[8, 8]; sync_tick();"
    wbc = compile_source(src, target="embedded")
    header = emit_c_embedded_header(wbc, model_name="test_organoid", target="embedded")

    assert "#ifndef WET_MODEL_TEST_ORGANOID_H" in header
    assert "#define WET_STATIC_ARENA_SIZE 65536" in header
    assert "static const uint8_t wet_bytecode_test_organoid[" in header
    assert "static uint8_t g_wet_static_arena_test_organoid[WET_STATIC_ARENA_SIZE];" in header
    assert "wet_embedded_init_test_organoid" in header
    assert "wet_embedded_step_test_organoid" in header
    assert "wet_get_compiled_bytecode_test_organoid" in header


def test_emit_c_spinnaker_header():
    """Verify SpiNNaker target includes neuromorphic sark / spin1 headers."""
    src = "grid mea[8, 8]; sync_tick();"
    header = compile_to_embedded_header(src, target="spinnaker", model_name="spinn_core")

    assert "SpiNNaker Neuromorphic Core" in header
    assert "#include <sark.h>" in header
    assert "#include <spin1_api.h>" in header
    assert "wet_bytecode_spinn_core" in header


def test_cli_target_embedded_compilation(tmp_path):
    """Verify wetc CLI compiles .wet to standalone .h with --target=embedded."""
    src_file = tmp_path / "model.wet"
    src_file.write_text("grid mea[8, 8]; sync_tick();", encoding="utf-8")
    out_h = tmp_path / "model.h"

    ret = wetc_main([str(src_file), "--target=embedded", "-o", str(out_h)])
    assert ret == 0
    assert out_h.exists()

    content = out_h.read_text(encoding="utf-8")
    assert "WET_STATIC_ARENA_SIZE" in content
    assert "wet_bytecode_model" in content


def test_cl_sdk_target_emission():
    """Verify --target=cl_sdk generates syntactically valid Python that executes with CLSDKRefSim."""
    import ast
    from compiler.cl_sdk_ref_sim import CLSDKRefSim

    src = "grid mea[8, 8]; stim_biphasic(0, 0.4V, 0.2ms, 0.2ms); set_blanking(1.0ms); sync_tick();"
    py_code = compile_source(src, target="cl_sdk")
    assert "CLSDKRefSim" in py_code
    assert "sim.set_blanking" in py_code

    ast.parse(py_code)

    loc = {}
    exec(py_code, loc)
    assert "run_closed_loop" in loc
    res = loc["run_closed_loop"]()
    assert "snapshots" in res
    assert len(res["snapshots"]) == 1000


def test_neuroplatform_target_emission():
    """Verify --target=neuroplatform generates valid Python that executes with NeuroplatformRefSim."""
    import ast
    import json
    from compiler.neuroplatform_ref_sim import NeuroplatformRefSim

    src = "grid mea[4, 4]; stim_biphasic(0, 0.4V, 0.2ms, 0.2ms); set_blanking(1.0ms); sync_tick();"
    py_code = compile_source(src, target="neuroplatform")
    assert "NeuroplatformRefSim" in py_code
    assert "sim.stim_biphasic" in py_code

    ast.parse(py_code)

    loc = {}
    exec(py_code, loc)
    assert "run_protocol" in loc
    trace_json = loc["run_protocol"]()
    trace = json.loads(trace_json)
    assert trace["format"] == "neuroplatform_trace_v1"
    assert len(trace["events"]) >= 1

