"""
Tests for Remediation 2:
- Compiler target dispatch in compile_source(), wetlang.compile(), and wetlang.cli
- Lexer UTF-8 BOM handling across Lexer and wetlang check --format=json
"""

import ast
import json
from pathlib import Path

import pytest

from compiler.lexer import Lexer
from compiler.token import TokenType
from compiler.emitter import compile_source, compile_to_embedded_header
import wetlang
from wetlang.cli import main as wetlang_cli_main


SAMPLE_WET = """\
grid mea[8, 8];
channel c0 = mea[0, 0] mode: BiphasicStim;

fn main() {
    stim_biphasic(c0, 0.5 V, 100 us, 100 us);
    sync_tick();
}
"""


def test_lexer_strips_utf8_bom():
    bom_src = "\ufeff" + SAMPLE_WET
    tokens = Lexer(bom_src).tokenize()
    assert len(tokens) > 0
    assert tokens[0].type == TokenType.GRID
    assert tokens[0].value == "grid"


def test_cli_check_json_handles_utf8_bom(tmp_path, capsys):
    src_file = tmp_path / "bom_sample.wet"
    src_file.write_bytes(b"\xef\xbb\xbf" + SAMPLE_WET.encode("utf-8"))

    ret = wetlang_cli_main(["check", "--format=json", str(src_file)])
    captured = capsys.readouterr()
    assert ret == 0
    diags = json.loads(captured.out)
    assert diags == []


def test_compile_source_target_dispatch():
    wbc = compile_source(SAMPLE_WET, target="sim")
    assert isinstance(wbc, bytes)
    assert len(wbc) > 32

    loihi_py = compile_source(SAMPLE_WET, target="loihi2")
    assert isinstance(loihi_py, str)
    assert "AbstractProcess" in loihi_py
    assert "PyLoihiProcessModel" in loihi_py
    ast.parse(loihi_py)

    spinn_py = compile_source(SAMPLE_WET, target="spinnaker")
    assert isinstance(spinn_py, str)
    assert "pyNN.spiNNaker" in spinn_py
    assert "sim.setup" in spinn_py
    ast.parse(spinn_py)

    assert wetlang.compile(SAMPLE_WET, target="loihi2") == loihi_py
    assert wetlang.compile(SAMPLE_WET, target="spinnaker") == spinn_py

    with pytest.raises(ValueError, match="Unsupported compilation target"):
        compile_source(SAMPLE_WET, target="unknown_substrate")


def test_compile_to_embedded_header_spinnaker_preserves_bytecode():
    header = compile_to_embedded_header(SAMPLE_WET, target="spinnaker", model_name="spinn_test")
    assert "#include <sark.h>" in header
    assert "wet_bytecode_spinn_test" in header


def test_cli_compile_targets_and_sign_rejection(tmp_path):
    src_file = tmp_path / "prog.wet"
    src_file.write_text(SAMPLE_WET, encoding="utf-8")

    # loihi2 -> .py
    assert wetlang_cli_main(["compile", str(src_file), "--target", "loihi2"]) == 0
    loihi_out = tmp_path / "prog.py"
    assert loihi_out.is_file()
    ast.parse(loihi_out.read_text(encoding="utf-8"))

    # spinnaker -> .py
    spinn_out = tmp_path / "prog_spinn.py"
    assert wetlang_cli_main(["compile", str(src_file), "--target", "spinnaker", "-o", str(spinn_out)]) == 0
    assert spinn_out.is_file()
    ast.parse(spinn_out.read_text(encoding="utf-8"))

    # embedded -> .h
    assert wetlang_cli_main(["compile", str(src_file), "--target", "embedded"]) == 0
    header_out = tmp_path / "prog.h"
    assert header_out.is_file()
    assert "wet_bytecode_prog" in header_out.read_text(encoding="utf-8")

    # sim -> .wbc
    assert wetlang_cli_main(["compile", str(src_file), "--target", "sim"]) == 0
    wbc_out = tmp_path / "prog.wbc"
    assert wbc_out.is_file()
    assert len(wbc_out.read_bytes()) > 32

    # --sign disallowed on text targets
    assert wetlang_cli_main(["compile", str(src_file), "--target", "loihi2", "--sign", "secret"]) == 1
    assert wetlang_cli_main(["compile", str(src_file), "--target", "spinnaker", "--sign", "secret"]) == 1
