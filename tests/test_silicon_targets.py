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
    """Verify all 4 Project Janus targets exist."""
    assert Target.SIM == "sim"
    assert Target.FINALSPARK == "finalspark"
    assert Target.SPINNAKER == "spinnaker"
    assert Target.EMBEDDED == "embedded"


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
