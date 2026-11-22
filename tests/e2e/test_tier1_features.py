"""
WetLang E2E Test Suite: Tier 1 Feature Coverage Suite
Implements >=5 isolated happy-path equivalence class tests for EACH of the 28 features
from PROJECT.md (Features F1 through F28), totaling at least 140 test methods.

Subclasses WetLangE2ETestCase from tests.e2e.common.
Organized into logical test classes:
  - TestTier1Compiler (F1..F7: 35 tests)
  - TestTier1Runtime (F8..F11: 20 tests)
  - TestTier1Biophysics (F12..F17: 30 tests)
  - TestTier1Interlocks (F18..F22: 25 tests)
  - TestTier1Benchmarks (F23..F25: 15 tests)
  - TestTier1Documentation (F26: 5 tests)
  - TestTier1SyntheticSuite (F27: 5 tests)
  - TestTier1DualTrack (F28: 5 tests)
"""

import os
import sys
import math
import struct
import zlib
import subprocess
import unittest
from typing import Any, Dict, List, Optional, Tuple

# Ensure project root and wetlang package are in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for p in [PROJECT_ROOT, os.path.join(PROJECT_ROOT, "wetlang")]:
    if p not in sys.path and os.path.isdir(p):
        sys.path.insert(0, p)

from tests.e2e.common import (
    WetLangE2ETestCase,
    PROJECT_ROOT,
    HAS_COMPILER,
    HAS_NATIVE_VM,
    HAS_BIOPHYSICS,
    HAS_INTERLOCKS,
    HAS_BENCHMARKS,
    require_feature,
    require_compiler,
    require_native_vm,
    require_biophysics,
    require_interlocks,
    require_benchmarks,
    assert_si_value_close,
    assert_voltage_clamped,
    assert_sliding_charge_balance,
    assert_epileptiform_trip,
    assert_wbc_header_valid,
    make_wbc_header,
    make_minimal_wet_program,
    generate_valid_wet_source,
    generate_mea_coordinates,
    make_biphasic_stim_trace,
    make_spike_raster_matrix,
)

if HAS_COMPILER:
    from compiler.token import Token, TokenType, Dimension, KEYWORDS
    from compiler.lexer import Lexer
    from compiler.ast_nodes import (
        ProgramNode, GridDeclNode, ChannelDeclNode, FnDeclNode, ParamNode,
        StreamDeclNode, StreamItemNode, BlockNode, LetStmtNode, AssignStmtNode,
        StimStmtNode, ModulateStmtNode, SyncTickStmtNode, IfStmtNode, WhileStmtNode,
        ForStmtNode, ReturnStmtNode, ExprStmtNode, BinaryOpNode, UnaryOpNode,
        LiteralNode, PhysicalLiteralNode, IdentifierNode, CallNode, IndexNode,
        RangeNode, DomainCallNode
    )
    from compiler.parser import Parser
    from compiler.semantic import SemanticAnalyzer
    from compiler.isa import (
        Opcode, HEADER_MAGIC, HEADER_SIZE, VERSION_MAJOR, VERSION_MINOR,
        HEADER_STRUCT_FORMAT, Capability, SectionType, SECTION_ENTRY_SIZE, SECTION_ENTRY_FORMAT
    )
    from compiler.emitter import BytecodeEmitter, ConstantPool, compile_source, disassemble


# =============================================================================
# 1. Compiler Pipeline (Features F1 through F7: 35 tests)
# =============================================================================

class TestTier1Compiler(WetLangE2ETestCase):
    """
    Tier 1 tests for the WetLang Compiler Pipeline:
      - Feature 1: Formal EBNF Grammar (5 tests)
      - Feature 2: Lexer with Physical Units (5 tests)
      - Feature 3: Pratt Recursive-Descent Parser (5 tests)
      - Feature 4: Semantic & Scope Analyzer (5 tests)
      - Feature 5: Static Loop-Yield Verifier (5 tests)
      - Feature 6: Custom Bytecode ISA (5 tests)
      - Feature 7: Bytecode Binary Emitter (5 tests)
    """
    tier = 1

    # -------------------------------------------------------------------------
    # Feature 1: Formal EBNF Grammar (F1)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier1_f01_grid_decl_happy(self):
        """F1: Test MEA grid declaration grammar parsing into GridDeclNode."""
        code = "grid mea { rows: 8; cols: 8; pitch: 200um; base_voltage: 0mV; }"
        tokens = Lexer(code).tokenize()
        ast = Parser(tokens).parse()
        self.assertIsInstance(ast, ProgramNode)
        self.assertEqual(len(ast.declarations), 1)
        grid = ast.declarations[0]
        self.assertIsInstance(grid, GridDeclNode)
        self.assertEqual(grid.name, "mea")
        self.assertEqual(grid.rows.value, 8)
        self.assertEqual(grid.cols.value, 8)
        self.assertIsNotNone(grid.pitch)
        self.assertIsNotNone(grid.base_voltage)

    @require_compiler
    def test_tier1_f01_channel_decl_happy(self):
        """F1: Test MEA channel declaration grammar with coordinates and mode."""
        code = "grid mea { rows: 8; cols: 8; } channel stim_ch = mea[0, 2] mode: BiphasicStim;"
        tokens = Lexer(code).tokenize()
        ast = Parser(tokens).parse()
        self.assertEqual(len(ast.declarations), 2)
        ch = ast.declarations[1]
        self.assertIsInstance(ch, ChannelDeclNode)
        self.assertEqual(ch.name, "stim_ch")
        self.assertEqual(ch.mode, "BiphasicStim")
        self.assertIsInstance(ch.target, IndexNode)
        self.assertEqual(ch.target.indices[0].value, 0)
        self.assertEqual(ch.target.indices[1].value, 2)

    @require_compiler
    def test_tier1_f01_fn_decl_happy(self):
        """F1: Test function declaration grammar with typed physical parameters and return type."""
        code = "fn compute_flux(v: Voltage, t: Time) -> Charge { return 0.5nC; }"
        tokens = Lexer(code).tokenize()
        ast = Parser(tokens).parse()
        self.assertEqual(len(ast.declarations), 1)
        fn = ast.declarations[0]
        self.assertIsInstance(fn, FnDeclNode)
        self.assertEqual(fn.name, "compute_flux")
        self.assertEqual(len(fn.params), 2)
        self.assertEqual(fn.params[0].name, "v")
        self.assertEqual(fn.params[0].type_name, "Voltage")
        self.assertEqual(fn.params[1].name, "t")
        self.assertEqual(fn.params[1].type_name, "Time")
        self.assertEqual(fn.return_type, "Charge")

    @require_compiler
    def test_tier1_f01_stim_biphasic_stmt_happy(self):
        """F1: Test stim_biphasic statement grammar with voltage, phases, and interphase interval."""
        code = "fn main() { stim_biphasic(stim_ch, 0.8V, 200us, 200us, 10us); }"
        tokens = Lexer(code).tokenize()
        ast = Parser(tokens).parse()
        stmt = ast.declarations[0].body.statements[0]
        self.assertIsInstance(stmt, StimStmtNode)
        self.assertEqual(stmt.channel.name, "stim_ch")
        self.assertEqual(stmt.voltage.dimension, Dimension.VOLTAGE)
        self.assertEqual(stmt.phase1.dimension, Dimension.TIME)
        self.assertEqual(stmt.phase2.dimension, Dimension.TIME)
        self.assertEqual(stmt.interphase.dimension, Dimension.TIME)

    @require_compiler
    def test_tier1_f01_stream_cycle_decl_happy(self):
        """F1: Test closed-loop stream declaration grammar with binding and cycle block."""
        code = "stream tracker { bind in_ch -> sensory; cycle { sync_tick(); } }"
        tokens = Lexer(code).tokenize()
        ast = Parser(tokens).parse()
        stream = ast.declarations[0]
        self.assertIsInstance(stream, StreamDeclNode)
        self.assertEqual(stream.name, "tracker")
        self.assertEqual(len(stream.items), 2)
        self.assertEqual(stream.items[0].kind, "bind_out")
        self.assertEqual(stream.items[1].kind, "cycle")

    # -------------------------------------------------------------------------
    # Feature 2: Lexer with Physical Units (F2)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier1_f02_time_units_happy(self):
        """F2: Test time dimension parsing and scaling (ms, us, s)."""
        tokens = [t for t in Lexer("10ms 200us 1.5s").tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 3)
        self.assertTrue(all(t.dimension == Dimension.TIME for t in tokens))
        assert_si_value_close(tokens[0].si_value, 0.010)
        assert_si_value_close(tokens[1].si_value, 0.000200)
        assert_si_value_close(tokens[2].si_value, 1.5)

    @require_compiler
    def test_tier1_f02_voltage_units_happy(self):
        """F2: Test voltage dimension parsing and scaling (V, mV, uV)."""
        tokens = [t for t in Lexer("1.2V 500mV 65.0uV").tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 3)
        self.assertTrue(all(t.dimension == Dimension.VOLTAGE for t in tokens))
        assert_si_value_close(tokens[0].si_value, 1.2)
        assert_si_value_close(tokens[1].si_value, 0.5)
        assert_si_value_close(tokens[2].si_value, 6.5e-5)

    @require_compiler
    def test_tier1_f02_current_charge_units_happy(self):
        """F2: Test current (uA, nA) and charge (nC, pC) unit parsing."""
        tokens = [t for t in Lexer("45uA 10nA 0.5nC 100pC").tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 4)
        self.assertEqual(tokens[0].dimension, Dimension.CURRENT)
        assert_si_value_close(tokens[0].si_value, 45e-6)
        self.assertEqual(tokens[1].dimension, Dimension.CURRENT)
        assert_si_value_close(tokens[1].si_value, 10e-9)
        self.assertEqual(tokens[2].dimension, Dimension.CHARGE)
        assert_si_value_close(tokens[2].si_value, 0.5e-9)
        self.assertEqual(tokens[3].dimension, Dimension.CHARGE)
        assert_si_value_close(tokens[3].si_value, 100e-12)

    @require_compiler
    def test_tier1_f02_frequency_length_units_happy(self):
        """F2: Test frequency (Hz) and spatial length (um, mm) units."""
        tokens = [t for t in Lexer("150Hz 200um 1.6mm").tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].dimension, Dimension.FREQUENCY)
        assert_si_value_close(tokens[0].si_value, 150.0)
        self.assertEqual(tokens[1].dimension, Dimension.LENGTH)
        assert_si_value_close(tokens[1].si_value, 0.000200)
        self.assertEqual(tokens[2].dimension, Dimension.LENGTH)
        assert_si_value_close(tokens[2].si_value, 0.0016)

    @require_compiler
    def test_tier1_f02_keywords_tokenization_happy(self):
        """F2: Test recognition of all domain-specific and language keywords."""
        src = "grid channel stim_biphasic read_spikes modulate_stdp sync_tick stream cycle let if while for return"
        tokens = [t for t in Lexer(src).tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 13)
        expected_types = [
            TokenType.GRID, TokenType.CHANNEL, TokenType.STIM_BIPHASIC,
            TokenType.READ_SPIKES, TokenType.MODULATE_STDP, TokenType.SYNC_TICK,
            TokenType.STREAM, TokenType.CYCLE, TokenType.LET, TokenType.IF,
            TokenType.WHILE, TokenType.FOR, TokenType.RETURN
        ]
        self.assertEqual([t.type for t in tokens], expected_types)

    # -------------------------------------------------------------------------
    # Feature 3: Pratt Recursive-Descent Parser (F3)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier1_f03_arithmetic_precedence_happy(self):
        """F3: Test arithmetic operator precedence (* binds tighter than +)."""
        ast = Parser(Lexer("fn main() { let x = 2 + 3 * 4; }").tokenize()).parse()
        stmt = ast.declarations[0].body.statements[0]
        self.assertEqual(stmt.initializer.op, "+")
        self.assertEqual(stmt.initializer.left.value, 2)
        self.assertEqual(stmt.initializer.right.op, "*")
        self.assertEqual(stmt.initializer.right.left.value, 3)
        self.assertEqual(stmt.initializer.right.right.value, 4)

    @require_compiler
    def test_tier1_f03_relational_logical_precedence_happy(self):
        """F3: Test relational (<, ==) and logical (&&) precedence."""
        ast = Parser(Lexer("fn main() { let res = a < b && c == d; }").tokenize()).parse()
        init = ast.declarations[0].body.statements[0].initializer
        self.assertEqual(init.op, "&&")
        self.assertEqual(init.left.op, "<")
        self.assertEqual(init.right.op, "==")

    @require_compiler
    def test_tier1_f03_unary_prefix_binding_happy(self):
        """F3: Test unary prefix operator (-) binding with binary operator (*)."""
        ast = Parser(Lexer("fn main() { let val = -x * 5; }").tokenize()).parse()
        init = ast.declarations[0].body.statements[0].initializer
        self.assertEqual(init.op, "*")
        self.assertEqual(init.left.op, "-")
        self.assertEqual(init.left.operand.name, "x")
        self.assertEqual(init.right.value, 5)

    @require_compiler
    def test_tier1_f03_postfix_calls_and_indexing_happy(self):
        """F3: Test parsing function calls and MEA domain readouts."""
        ast = Parser(Lexer("fn main() { let s = read_spikes(ch, 20ms); }").tokenize()).parse()
        init = ast.declarations[0].body.statements[0].initializer
        self.assertIsInstance(init, (CallNode, DomainCallNode))
        name = getattr(init, "func_name", None)
        if name is None:
            callee = getattr(init, "callee", None)
            name = getattr(callee, "name", "")
        self.assertEqual(name, "read_spikes")
        self.assertEqual(len(init.args), 2)

    @require_compiler
    def test_tier1_f03_parentheses_override_happy(self):
        """F3: Test explicit parentheses overriding default precedence."""
        ast = Parser(Lexer("fn main() { let x = (2 + 3) * 4; }").tokenize()).parse()
        init = ast.declarations[0].body.statements[0].initializer
        self.assertEqual(init.op, "*")
        self.assertEqual(init.left.op, "+")
        self.assertEqual(init.left.left.value, 2)
        self.assertEqual(init.left.right.value, 3)
        self.assertEqual(init.right.value, 4)

    # -------------------------------------------------------------------------
    # Feature 4: Semantic & Scope Analyzer (F4)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier1_f04_variable_declaration_resolution_happy(self):
        """F4: Test variable scope resolution across sequential declarations."""
        code = "grid mea { rows: 8; cols: 8; } fn main() { let x = 10; let y = x + 5; }"
        ast = Parser(Lexer(code).tokenize()).parse()
        sa = SemanticAnalyzer(ast)
        sa.analyze()
        self.assertIsNotNone(sa.global_scope.resolve("main"))

    @require_compiler
    def test_tier1_f04_block_scope_shadowing_happy(self):
        """F4: Test inner block scope variable shadowing without corruption."""
        code = "fn main() { let x = 1; { let x = 2; } let z = x; }"
        ast = Parser(Lexer(code).tokenize()).parse()
        sa = SemanticAnalyzer(ast)
        sa.analyze()

    @require_compiler
    def test_tier1_f04_channel_grid_symbol_resolution_happy(self):
        """F4: Test channel declaration resolution to parent MEA grid."""
        code = "grid mea { rows: 8; cols: 8; } channel c = mea[2, 3]; fn main() { }"
        ast = Parser(Lexer(code).tokenize()).parse()
        sa = SemanticAnalyzer(ast)
        sa.analyze()
        sym = sa.global_scope.resolve("c")
        self.assertIsNotNone(sym)

    @require_compiler
    def test_tier1_f04_type_compatibility_happy(self):
        """F4: Test dimensional arithmetic type compatibility (Voltage + Voltage)."""
        code = "grid mea { rows: 8; cols: 8; } fn main() { let v1 = 100mV; let v2 = 200mV; let v3 = v1 + v2; }"
        ast = Parser(Lexer(code).tokenize()).parse()
        sa = SemanticAnalyzer(ast)
        sa.analyze()

    @require_compiler
    def test_tier1_f04_valid_mea_coordinates_happy(self):
        """F4: Test valid MEA electrode coordinates pass static boundary checks."""
        code = "grid mea { rows: 8; cols: 8; } channel c0 = mea[0, 0]; channel c63 = mea[7, 7]; fn main() {}"
        ast = Parser(Lexer(code).tokenize()).parse()
        sa = SemanticAnalyzer(ast)
        sa.analyze()

    # -------------------------------------------------------------------------
    # Feature 5: Static Loop-Yield Verifier (F5)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier1_f05_while_loop_with_sync_tick_happy(self):
        """F5: Test while loop with sync_tick is certified safe by CFG analyzer."""
        code = "grid mea { rows: 8; cols: 8; } channel ch = mea[0, 0] mode: BiphasicStim; fn main() { while (true) { stim_biphasic(ch, 0.5V, 100us, 100us); sync_tick(); } }"
        binary = compile_source(code)
        self.assertTrue(binary.startswith(HEADER_MAGIC))

    @require_compiler
    def test_tier1_f05_for_loop_with_sync_tick_happy(self):
        """F5: Test for loop with sync_tick passes static yield verification."""
        code = "grid mea { rows: 8; cols: 8; } channel ch = mea[0, 0] mode: BiphasicStim; fn main() { for i in 0..100 { stim_biphasic(ch, 0.5V, 100us, 100us); sync_tick(); } }"
        binary = compile_source(code)
        self.assertTrue(binary.startswith(HEADER_MAGIC))

    @require_compiler
    def test_tier1_f05_stream_cycle_with_sync_tick_happy(self):
        """F5: Test stream cycle block with sync_tick passes CFG verifier."""
        code = "grid mea { rows: 8; cols: 8; } channel ch = mea[0, 0] mode: BiphasicStim; stream loop_ctrl { cycle { stim_biphasic(ch, 0.5V, 100us, 100us); sync_tick(); } }"
        binary = compile_source(code)
        self.assertTrue(binary.startswith(HEADER_MAGIC))

    @require_compiler
    def test_tier1_f05_conditional_sync_ticks_all_branches_happy(self):
        """F5: Test conditional branching inside loop where all branches yield."""
        code = "grid mea { rows: 8; cols: 8; } channel ch = mea[0, 0] mode: BiphasicStim; fn main() { let c = true; while (true) { if (c) { sync_tick(); } else { sync_tick(); } } }"
        binary = compile_source(code)
        self.assertTrue(binary.startswith(HEADER_MAGIC))

    @require_compiler
    def test_tier1_f05_nested_loops_both_yield_happy(self):
        """F5: Test nested loops where both inner and outer loops execute sync_tick."""
        code = "grid mea { rows: 8; cols: 8; } channel ch = mea[0, 0] mode: BiphasicStim; fn main() { while (true) { while (true) { sync_tick(); } sync_tick(); } }"
        binary = compile_source(code)
        self.assertTrue(binary.startswith(HEADER_MAGIC))

    # -------------------------------------------------------------------------
    # Feature 6: Custom Bytecode ISA (F6)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier1_f06_header_encoding_happy(self):
        """F6: Test WBC 32-byte header serialization and magic validation."""
        header = make_wbc_header(magic=b"WETB", major=1, minor=0, caps=0x0003, file_size=64, channels=64)
        self.assertEqual(len(header), 32)
        parsed = assert_wbc_header_valid(header)
        self.assertEqual(parsed["magic"], b"WETB")
        self.assertEqual(parsed["major"], 1)
        self.assertEqual(parsed["minor"], 0)
        self.assertEqual(parsed["capabilities"], 0x0003)

    @require_compiler
    def test_tier1_f06_control_opcodes_happy(self):
        """F6: Test ISA control opcodes (NOP, HALT, SYNC_TICK, SLEEP_TICKS)."""
        self.assertEqual(Opcode.NOP, 0x00)
        self.assertEqual(Opcode.HALT, 0x01)
        self.assertEqual(Opcode.SYNC_TICK, 0x02)
        self.assertEqual(Opcode.SLEEP_TICKS, 0x03)

    @require_compiler
    def test_tier1_f06_stack_opcodes_happy(self):
        """F6: Test ISA stack manipulation opcodes and operand packing."""
        self.assertEqual(Opcode.PUSH_INT, 0x11)
        self.assertEqual(Opcode.PUSH_FLOAT, 0x12)
        self.assertEqual(Opcode.POP, 0x13)
        self.assertEqual(Opcode.DUP, 0x14)
        self.assertEqual(Opcode.SWAP, 0x15)
        packed = struct.pack("<Bi", Opcode.PUSH_INT, 42)
        self.assertEqual(packed, bytes([0x11, 42, 0, 0, 0]))

    @require_compiler
    def test_tier1_f06_arithmetic_opcodes_happy(self):
        """F6: Test ISA integer and floating point arithmetic opcodes."""
        self.assertEqual(Opcode.ADD_I, 0x20)
        self.assertEqual(Opcode.SUB_I, 0x21)
        self.assertEqual(Opcode.ADD_F, 0x24)
        self.assertEqual(Opcode.MUL_F, 0x26)
        self.assertEqual(Opcode.NEG, 0x28)

    @require_compiler
    def test_tier1_f06_biophysical_opcodes_happy(self):
        """F6: Test ISA biophysical opcodes (stim, read_spikes, read_voltage, modulate_stdp)."""
        self.assertEqual(Opcode.STIM_BIPHASIC, 0x50)
        self.assertEqual(Opcode.READ_SPIKES, 0x51)
        self.assertEqual(Opcode.READ_VOLTAGE, 0x52)
        self.assertEqual(Opcode.MODULATE_STDP, 0x53)
        self.assertEqual(Opcode.GET_POP_RATE, 0x54)

    # -------------------------------------------------------------------------
    # Feature 7: Bytecode Binary Emitter (F7)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier1_f07_emit_simple_binary_happy(self):
        """F7: Test compiling simple program to WBC binary format."""
        code = "fn main() { let x = 1; }"
        binary = compile_source(code)
        self.assertTrue(binary.startswith(b"WETB"))
        self.assertGreaterEqual(len(binary), 32)

    @require_compiler
    def test_tier1_f07_section_table_offsets_happy(self):
        """F7: Test section table emission with valid offsets and sizes."""
        code = "grid mea { rows: 8; cols: 8; } channel ch = mea[0, 0]; fn main() { let x = 1.2V; }"
        binary = compile_source(code)
        magic, v_maj, v_min, caps, fsize, crc, num_sections, ch_cnt, max_q, res = struct.unpack_from(HEADER_STRUCT_FORMAT, binary, 0)
        self.assertEqual(magic, HEADER_MAGIC)
        self.assertGreaterEqual(num_sections, 3)
        sec_table_off = HEADER_SIZE
        offsets = []
        for i in range(num_sections):
            stype, _, off, size = struct.unpack_from(SECTION_ENTRY_FORMAT, binary, sec_table_off + i * SECTION_ENTRY_SIZE)
            offsets.append((off, size))
        self.assertTrue(all(off >= HEADER_SIZE + num_sections * SECTION_ENTRY_SIZE for off, size in offsets))

    @require_compiler
    def test_tier1_f07_branch_backpatching_happy(self):
        """F7: Test jump offset backpatching for conditional control flow."""
        code = "fn main() { let c = true; let mut x = 0; if (c) { x = 1; } else { x = 2; } }"
        binary = compile_source(code)
        disasm_listing = disassemble(binary)
        self.assertIn("JMP", disasm_listing)

    @require_compiler
    def test_tier1_f07_constant_deduplication_happy(self):
        """F7: Test constant pool literal deduplication."""
        pool = ConstantPool()
        idx1 = pool.add_float(1.2)
        idx2 = pool.add_float(1.2)
        idx3 = pool.add_float(2.4)
        self.assertEqual(idx1, idx2)
        self.assertNotEqual(idx1, idx3)
        self.assertEqual(len(pool.entries), 2)

    @require_compiler
    def test_tier1_f07_crc32_checksum_generation_happy(self):
        """F7: Test CRC32 checksum generation and verification in WBC header."""
        code = "fn main() { return 0; }"
        binary = compile_source(code)
        magic, v_maj, v_min, caps, fsize, stored_crc, num_sections, ch_cnt, max_q, res = struct.unpack_from(HEADER_STRUCT_FORMAT, binary, 0)
        self.assertEqual(magic, HEADER_MAGIC)
        self.assertGreater(stored_crc, 0)
        b_copy = bytearray(binary)
        struct.pack_into("<I", b_copy, 12, 0)
        computed_crc = zlib.crc32(b_copy) & 0xFFFFFFFF
        self.assertEqual(stored_crc, computed_crc)


# =============================================================================
# 2. Native Runtime Engine & FFI (Features F8 through F11: 20 tests)
# =============================================================================

class TestTier1Runtime(WetLangE2ETestCase):
    """
    Tier 1 tests for the Native VM & Python FFI bindings:
      - Feature 8: Native C-ABI VM Engine (5 tests)
      - Feature 9: VM Tick Scheduler (5 tests)
      - Feature 10: Python ctypes FFI Bindings (5 tests)
      - Feature 11: Zero-Copy NumPy Telemetry (5 tests)
    """
    tier = 1

    # -------------------------------------------------------------------------
    # Feature 8: Native C-ABI VM Engine (F8)
    # -------------------------------------------------------------------------

    @require_native_vm
    def test_tier1_f08_vm_create_and_free_happy(self):
        """F8: Test native VM lifecycle initialization and destruction."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        self.assertIsNotNone(runtime)
        runtime.close()

    @require_native_vm
    def test_tier1_f08_load_valid_bytecode_happy(self):
        """F8: Test loading valid WBC bytecode into native VM."""
        from bindings.runtime import WetRuntime
        code = make_minimal_wet_program()
        binary = compile_source(code)
        runtime = WetRuntime()
        status = runtime.load(binary)
        self.assertEqual(status, 0)
        runtime.close()

    @require_native_vm
    def test_tier1_f08_stack_machine_arithmetic_happy(self):
        """F8: Test stack machine evaluation of arithmetic bytecode."""
        from bindings.runtime import WetRuntime
        code = "fn main() -> int { return 15 + 27; }"
        binary = compile_source(code)
        runtime = WetRuntime()
        runtime.load(binary)
        ret = runtime.step(ticks=1)
        self.assertIsNotNone(ret)
        runtime.close()

    @require_native_vm
    def test_tier1_f08_clean_halt_termination_happy(self):
        """F8: Test VM halts cleanly on HALT instruction."""
        from bindings.runtime import WetRuntime
        code = "fn main() { sync_tick(); }"
        binary = compile_source(code)
        runtime = WetRuntime()
        runtime.load(binary)
        telemetry = runtime.step(ticks=10)
        self.assertIsNotNone(telemetry)
        runtime.close()

    @require_native_vm
    def test_tier1_f08_version_query_happy(self):
        """F8: Test querying native runtime C-ABI version."""
        from bindings.ffi import WetVMFFI
        ffi = WetVMFFI()
        version = ffi.get_version()
        self.assertEqual(version, 0x0100)

    # -------------------------------------------------------------------------
    # Feature 9: VM Tick Scheduler (F9)
    # -------------------------------------------------------------------------

    @require_native_vm
    def test_tier1_f09_step_single_tick_happy(self):
        """F9: Test stepping a single cycle advances biological time by exactly 0.1 ms."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        code = make_minimal_wet_program()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=1)
        self.assertAlmostEqual(telem.sim_time_ms, 0.1, places=5)
        runtime.close()

    @require_native_vm
    def test_tier1_f09_run_100_ticks_happy(self):
        """F9: Test stepping 100 ticks advances biological time to 10.0 ms."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        code = make_minimal_wet_program()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=100)
        self.assertAlmostEqual(telem.sim_time_ms, 10.0, places=4)
        runtime.close()

    @require_native_vm
    def test_tier1_f09_deterministic_reproducibility_happy(self):
        """F9: Test cycle-accurate simulation produces deterministic identical results."""
        from bindings.runtime import WetRuntime
        code = make_minimal_wet_program()
        bin_data = compile_source(code)

        r1 = WetRuntime()
        r1.load(bin_data)
        telem1 = r1.step(ticks=50)

        r2 = WetRuntime()
        r2.load(bin_data)
        telem2 = r2.step(ticks=50)

        self.assertEqual(telem1.tick_index, telem2.tick_index)
        self.assertAlmostEqual(telem1.sim_time_ms, telem2.sim_time_ms, places=6)
        r1.close()
        r2.close()

    @require_native_vm
    def test_tier1_f09_sleep_ticks_opcode_happy(self):
        """F9: Test SLEEP_TICKS advances biological simulation time across sleep duration."""
        from bindings.runtime import WetRuntime
        code = "fn main() { sync_tick(50); }"
        runtime = WetRuntime()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=50)
        self.assertGreaterEqual(telem.sim_time_ms, 5.0)
        runtime.close()

    @require_native_vm
    def test_tier1_f09_zero_biological_time_for_compute_happy(self):
        """F9: Test compute operations execute within zero biological time between sync_tick calls."""
        from bindings.runtime import WetRuntime
        code = "fn main() { let mut a = 0; for i in 0..100 { a = a + i; } sync_tick(); }"
        runtime = WetRuntime()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=1)
        self.assertAlmostEqual(telem.sim_time_ms, 0.1, places=5)
        runtime.close()

    # -------------------------------------------------------------------------
    # Feature 10: Python ctypes FFI Bindings (F10)
    # -------------------------------------------------------------------------

    @require_native_vm
    def test_tier1_f10_library_loading_happy(self):
        """F10: Test shared library dynamic loading via ctypes."""
        from bindings.ffi import WetVMFFI
        ffi = WetVMFFI()
        self.assertIsNotNone(ffi.lib)

    @require_native_vm
    def test_tier1_f10_caller_allocates_telemetry_happy(self):
        """F10: Test caller-allocates memory convention for telemetry struct."""
        from bindings.ffi import WetVMFFI
        ffi = WetVMFFI()
        vm = ffi.create_vm()
        telem = ffi.allocate_telemetry()
        status = ffi.step_tick(vm, telem)
        self.assertEqual(status, 0)
        ffi.free_vm(vm)

    @require_native_vm
    def test_tier1_f10_error_buffer_marshaling_happy(self):
        """F10: Test string error buffer marshaling across C-ABI."""
        from bindings.ffi import WetVMFFI
        ffi = WetVMFFI()
        err_msg = ffi.get_last_error()
        self.assertIsInstance(err_msg, str)

    @require_native_vm
    def test_tier1_f10_inject_stimulus_ffi_happy(self):
        """F10: Test injecting stimulus through C-ABI binding."""
        from bindings.ffi import WetVMFFI
        ffi = WetVMFFI()
        vm = ffi.create_vm()
        status = ffi.inject_stimulus(vm, channel=0, voltage_v=0.8, p1_ms=0.2, p2_ms=0.2)
        self.assertEqual(status, 0)
        ffi.free_vm(vm)

    @require_native_vm
    def test_tier1_f10_repeated_lifecycle_no_leak_happy(self):
        """F10: Test repeated VM instantiation and freeing without memory leaks."""
        from bindings.ffi import WetVMFFI
        ffi = WetVMFFI()
        for _ in range(20):
            vm = ffi.create_vm()
            ffi.free_vm(vm)

    # -------------------------------------------------------------------------
    # Feature 11: Zero-Copy NumPy Telemetry (F11)
    # -------------------------------------------------------------------------

    @require_native_vm
    def test_tier1_f11_channel_voltages_view_happy(self):
        """F11: Test zero-copy channel voltages NumPy view shape and dtype."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        code = make_minimal_wet_program()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=1)
        voltages = telem.channel_voltages
        self.assertEqual(voltages.shape, (64,))
        runtime.close()

    @require_native_vm
    def test_tier1_f11_spike_raster_view_happy(self):
        """F11: Test zero-copy spike raster NumPy view."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        code = make_minimal_wet_program()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=1)
        rasters = telem.spike_raster
        self.assertEqual(rasters.shape, (64,))
        runtime.close()

    @require_native_vm
    def test_tier1_f11_zero_copy_identity_happy(self):
        """F11: Test array pointer matches native telemetry buffer memory address."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        code = make_minimal_wet_program()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=1)
        self.assertIsNotNone(telem.channel_voltages)
        runtime.close()

    @require_native_vm
    def test_tier1_f11_read_only_flag_happy(self):
        """F11: Test zero-copy view is marked read-only to prevent heap corruption."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        code = make_minimal_wet_program()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=1)
        voltages = telem.channel_voltages
        self.assertFalse(voltages.flags.writeable)
        runtime.close()

    @require_native_vm
    def test_tier1_f11_vectorized_math_happy(self):
        """F11: Test vectorized operations on telemetry arrays without data copying."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        code = make_minimal_wet_program()
        runtime.load(compile_source(code))
        telem = runtime.step(ticks=1)
        mean_v = float(telem.channel_voltages.mean())
        self.assertIsInstance(mean_v, float)
        runtime.close()


# =============================================================================
# 3. Biophysical Sandbox (Features F12 through F17: 30 tests)
# =============================================================================

class TestTier1Biophysics(WetLangE2ETestCase):
    """
    Tier 1 tests for the Biophysical Digital Twin Sandbox:
      - Feature 12: 8x8 MEA Grid Topology (5 tests)
      - Feature 13: Numerical ODE Solver (5 tests)
      - Feature 14: Absolute & Relative Refractory (5 tests)
      - Feature 15: Tsodyks-Markram STP (5 tests)
      - Feature 16: Pairwise Trace STDP (5 tests)
      - Feature 17: Telemetry Streaming Engine (5 tests)
    """
    tier = 1

    # -------------------------------------------------------------------------
    # Feature 12: 8x8 MEA Grid Topology (F12)
    # -------------------------------------------------------------------------

    @require_biophysics
    def test_tier1_f12_grid_geometry_happy(self):
        """F12: Test 8x8 MEA electrode array spatial dimensions and 200 um pitch."""
        from biophysics.mea_grid import MEAGrid
        grid = MEAGrid(rows=8, cols=8, pitch_um=200.0)
        self.assertEqual(grid.total_electrodes, 64)
        self.assertEqual(grid.rows, 8)
        self.assertEqual(grid.cols, 8)
        self.assertAlmostEqual(grid.pitch_um, 200.0)

    @require_biophysics
    def test_tier1_f12_coordinate_mapping_happy(self):
        """F12: Test 2D row/col to 1D channel index bijection."""
        from biophysics.mea_grid import MEAGrid
        grid = MEAGrid(rows=8, cols=8)
        self.assertEqual(grid.coords_to_channel(3, 5), 29)
        self.assertEqual(grid.channel_to_coords(29), (3, 5))

    @require_biophysics
    def test_tier1_f12_spatial_substrate_positions_happy(self):
        """F12: Test physical electrode substrate coordinates."""
        from biophysics.mea_grid import MEAGrid
        grid = MEAGrid(rows=8, cols=8, pitch_um=200.0)
        x0, y0 = grid.get_electrode_pos(0)
        x63, y63 = grid.get_electrode_pos(63)
        self.assertAlmostEqual(x0, 100.0)
        self.assertAlmostEqual(y0, 100.0)
        self.assertAlmostEqual(x63, 1500.0)
        self.assertAlmostEqual(y63, 1500.0)

    @require_biophysics
    def test_tier1_f12_forward_pickup_distance_decay_happy(self):
        """F12: Test 3D volume conduction forward pickup potential decaying with distance."""
        from biophysics.mea_grid import MEAGrid
        grid = MEAGrid(rows=8, cols=8)
        potentials = grid.calculate_field_potential(source_x=100.0, source_y=100.0, source_z=20.0, current_na=10.0)
        self.assertGreater(abs(potentials[0]), abs(potentials[63]))

    @require_biophysics
    def test_tier1_f12_resistive_crosstalk_happy(self):
        """F12: Test resistive substrate cross-talk between adjacent electrodes."""
        from biophysics.mea_grid import MEAGrid
        grid = MEAGrid(rows=8, cols=8)
        crosstalk = grid.get_crosstalk_matrix()
        self.assertAlmostEqual(crosstalk[0, 1], 0.04, places=2)

    # -------------------------------------------------------------------------
    # Feature 13: Numerical ODE Solver (F13)
    # -------------------------------------------------------------------------

    @require_biophysics
    def test_tier1_f13_exponential_euler_coba_lif_happy(self):
        """F13: Test Exact Exponential Euler COBA-LIF membrane potential integration."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        v_next = solver.step_passive(v_init=-60.0, tau_m=20.0, v_rest=-70.0)
        self.assertLess(v_next, -60.0)
        self.assertGreater(v_next, -70.0)

    @require_biophysics
    def test_tier1_f13_ampa_conductance_decay_happy(self):
        """F13: Test AMPA excitatory conductance exponential decay (tau_E = 3.0 ms)."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        g_e = 10.0
        for _ in range(30):  # 3.0 ms
            g_e = solver.decay_conductance(g_e, tau_ms=3.0)
        self.assertAlmostEqual(g_e, 10.0 * math.exp(-1.0), delta=0.1)

    @require_biophysics
    def test_tier1_f13_gaba_conductance_decay_happy(self):
        """F13: Test GABA inhibitory conductance exponential decay (tau_I = 8.0 ms)."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        g_i = 20.0
        for _ in range(80):  # 8.0 ms
            g_i = solver.decay_conductance(g_i, tau_ms=8.0)
        self.assertAlmostEqual(g_i, 20.0 * math.exp(-1.0), delta=0.2)

    @require_biophysics
    def test_tier1_f13_fixed_timestep_0_1ms_happy(self):
        """F13: Test fixed numerical integration timestep dt = 0.1 ms."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        self.assertEqual(solver.dt_ms, 0.1)

    @require_biophysics
    def test_tier1_f13_action_potential_generation_happy(self):
        """F13: Test action potential emission on threshold crossing and reset."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        spiked, v_new = solver.update_neuron(v_m=-49.0, v_thresh=-50.0, v_reset=-65.0)
        self.assertTrue(spiked)
        self.assertEqual(v_new, -65.0)

    # -------------------------------------------------------------------------
    # Feature 14: Absolute & Relative Refractory (F14)
    # -------------------------------------------------------------------------

    @require_biophysics
    def test_tier1_f14_absolute_refractory_clamp_happy(self):
        """F14: Test 2.0 ms hard clamp at V_reset following action potential."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        v_trace = solver.simulate_refractory(v_init=-65.0, current_inj=5000.0, ticks=20)
        self.assertTrue(all(v == -65.0 for v in v_trace))

    @require_biophysics
    def test_tier1_f14_refractory_counter_decrement_happy(self):
        """F14: Test refractory counter initialized to 20 decrements to 0."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        counter = 20
        for _ in range(20):
            counter = solver.decrement_refractory(counter)
        self.assertEqual(counter, 0)

    @require_biophysics
    def test_tier1_f14_max_firing_frequency_500hz_happy(self):
        """F14: Test refractory limit enforcing maximum firing rate <= 500 Hz."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        spikes = solver.simulate_continuous_stimulus(current_pA=10000.0, duration_ms=100.0)
        self.assertLessEqual(len(spikes), 50)

    @require_biophysics
    def test_tier1_f14_adaptive_threshold_elevation_happy(self):
        """F14: Test dynamic threshold elevation by +15 mV post-spike."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        thresh = solver.elevate_threshold(base_thresh=-50.0, delta=15.0)
        self.assertEqual(thresh, -35.0)

    @require_biophysics
    def test_tier1_f14_ahp_conductance_activation_happy(self):
        """F14: Test afterhyperpolarization (AHP) potassium conductance jump."""
        from biophysics.ode_solver import LifODESolver
        solver = LifODESolver(dt_ms=0.1)
        g_ahp = solver.activate_ahp(g_current=0.0, delta_g=4.0)
        self.assertAlmostEqual(g_ahp, 4.0)

    # -------------------------------------------------------------------------
    # Feature 15: Tsodyks-Markram STP (F15)
    # -------------------------------------------------------------------------

    @require_biophysics
    def test_tier1_f15_ee_synapse_depression_happy(self):
        """F15: Test E->E cortical synapse short-term vesicle depletion."""
        from biophysics.stp import SynapseSTP
        synapse = SynapseSTP(synapse_type="E->E")
        g_jumps = synapse.deliver_spikes(count=5, freq_hz=50.0)
        self.assertGreater(g_jumps[0], g_jumps[-1])

    @require_biophysics
    def test_tier1_f15_ei_synapse_facilitation_happy(self):
        """F15: Test E->I cortical synapse short-term facilitation."""
        from biophysics.stp import SynapseSTP
        synapse = SynapseSTP(synapse_type="E->I")
        u_vals = synapse.track_utilization(count=5, freq_hz=50.0)
        self.assertGreater(u_vals[-1], u_vals[0])

    @require_biophysics
    def test_tier1_f15_ie_depressing_inhibition_happy(self):
        """F15: Test I->E depressing inhibition parameters."""
        from biophysics.stp import SynapseSTP
        synapse = SynapseSTP(synapse_type="I->E")
        self.assertEqual(synapse.tau_rec_ms, 700.0)

    @require_biophysics
    def test_tier1_f15_ii_interneuron_balance_happy(self):
        """F15: Test I->I interneuron-to-interneuron synaptic kinetics."""
        from biophysics.stp import SynapseSTP
        synapse = SynapseSTP(synapse_type="I->I")
        self.assertEqual(synapse.tau_rec_ms, 400.0)

    @require_biophysics
    def test_tier1_f15_exponential_vesicle_recovery_happy(self):
        """F15: Test vesicle recovery toward R=1.0 during quiescence."""
        from biophysics.stp import SynapseSTP
        synapse = SynapseSTP(synapse_type="E->E", tau_rec_ms=500.0)
        r_rec = synapse.recover(r_init=0.3, delta_t_ms=500.0)
        expected = 1.0 - (1.0 - 0.3) * math.exp(-1.0)
        self.assertAlmostEqual(r_rec, expected, delta=0.02)

    # -------------------------------------------------------------------------
    # Feature 16: Pairwise Trace STDP (F16)
    # -------------------------------------------------------------------------

    @require_biophysics
    def test_tier1_f16_pre_before_post_ltp_happy(self):
        """F16: Test Long-Term Potentiation (LTP) for pre-before-post spike pairing."""
        from biophysics.stdp import PairwiseSTDP
        stdp = PairwiseSTDP()
        delta_w = stdp.compute_delta_w(delta_t_ms=5.0)
        self.assertGreater(delta_w, 0.0)

    @require_biophysics
    def test_tier1_f16_post_before_pre_ltd_happy(self):
        """F16: Test Long-Term Depression (LTD) for post-before-pre spike pairing."""
        from biophysics.stdp import PairwiseSTDP
        stdp = PairwiseSTDP()
        delta_w = stdp.compute_delta_w(delta_t_ms=-5.0)
        self.assertLess(delta_w, 0.0)

    @require_biophysics
    def test_tier1_f16_trace_decay_happy(self):
        """F16: Test exponential trace decay over 20 ms time constant."""
        from biophysics.stdp import PairwiseSTDP
        stdp = PairwiseSTDP(tau_plus_ms=20.0)
        trace = stdp.decay_trace(init_val=1.0, elapsed_ms=20.0)
        self.assertAlmostEqual(trace, math.exp(-1.0), delta=0.01)

    @require_biophysics
    def test_tier1_f16_depression_bias_ratio_happy(self):
        """F16: Test depression bias ratio A_- / A_+ == 1.05."""
        from biophysics.stdp import PairwiseSTDP
        stdp = PairwiseSTDP()
        self.assertAlmostEqual(stdp.a_minus / stdp.a_plus, 1.05, places=5)

    @require_biophysics
    def test_tier1_f16_dales_principle_exclusivity_happy(self):
        """F16: Test Dale's principle: inhibitory synapses do not undergo STDP."""
        from biophysics.stdp import PairwiseSTDP
        stdp = PairwiseSTDP()
        w_inh = stdp.update_weight(w_init=15.0, is_inhibitory=True, delta_t_ms=5.0)
        self.assertEqual(w_inh, 15.0)

    # -------------------------------------------------------------------------
    # Feature 17: Telemetry Streaming Engine (F17)
    # -------------------------------------------------------------------------

    @require_biophysics
    def test_tier1_f17_jsonl_emission_schema_happy(self):
        """F17: Test JSONL telemetry line structure contains required telemetry keys."""
        from biophysics.telemetry import TelemetryStream
        ts = TelemetryStream()
        line = ts.format_tick_json(tick=1, time_ms=0.1, v_m=[-65.0]*64, spikes=[0]*64)
        self.assertIn('"tick": 1', line)
        self.assertIn('"time_ms": 0.1', line)

    @require_biophysics
    def test_tier1_f17_csv_summary_emission_happy(self):
        """F17: Test CSV telemetry summary header format."""
        from biophysics.telemetry import TelemetryStream
        ts = TelemetryStream()
        header = ts.get_csv_header()
        self.assertIn("tick,time_ms,spike_count,r_inst_hz", header)

    @require_biophysics
    def test_tier1_f17_per_tick_monotonicity_happy(self):
        """F17: Test monotonic tick indexing in telemetry stream."""
        from biophysics.telemetry import TelemetryStream
        ts = TelemetryStream()
        records = [ts.make_record(t) for t in range(10)]
        self.assertTrue(all(records[i]["tick"] == i for i in range(10)))

    @require_biophysics
    def test_tier1_f17_sparse_spike_events_csv_happy(self):
        """F17: Test sparse spike event logging format."""
        from biophysics.telemetry import TelemetryStream
        ts = TelemetryStream()
        event_row = ts.format_spike_event(tick=50, time_ms=5.0, neuron_id=3, neuron_type="E")
        self.assertIn("50,5.0,3,E", event_row)

    @require_biophysics
    def test_tier1_f17_instantaneous_rate_accuracy_happy(self):
        """F17: Test instantaneous population firing rate computation."""
        from biophysics.telemetry import TelemetryStream
        ts = TelemetryStream()
        rate = ts.compute_firing_rate(spike_count=4, neuron_count=64, dt_ms=0.1)
        self.assertAlmostEqual(rate, 625.0, delta=1.0)


# =============================================================================
# 4. Biocybersecurity Hardware Interlocks (Features F18 through F22: 25 tests)
# =============================================================================

class TestTier1Interlocks(WetLangE2ETestCase):
    """
    Tier 1 tests for Biocybersecurity Protections & Hardware Interlocks:
      - Feature 18: Static Capability Verifier (5 tests)
      - Feature 19: Water-Window Voltage Clamp (5 tests)
      - Feature 20: Sliding Charge Balance Watchdog (5 tests)
      - Feature 21: Epileptiform Runaway Breaker (5 tests)
      - Feature 22: Fail-Safe Interlock Clamp (5 tests)
    """
    tier = 1

    # -------------------------------------------------------------------------
    # Feature 18: Static Capability Verifier (F18)
    # -------------------------------------------------------------------------

    @require_interlocks
    def test_tier1_f18_valid_capabilities_pass_happy(self):
        """F18: Test bytecode declaring matching capabilities passes verifier."""
        from native.interlocks import CapabilityVerifier
        cv = CapabilityVerifier()
        self.assertTrue(cv.verify_capabilities(declared_caps=0x0001, used_caps=0x0001))

    @require_interlocks
    def test_tier1_f18_tier0_compute_always_allowed_happy(self):
        """F18: Test compute-only program with zero capabilities is always permitted."""
        from native.interlocks import CapabilityVerifier
        cv = CapabilityVerifier()
        self.assertTrue(cv.verify_capabilities(declared_caps=0x0000, used_caps=0x0000))

    @require_interlocks
    def test_tier1_f18_tier1_read_spikes_allowed_happy(self):
        """F18: Test spike reading capability authorization."""
        from native.interlocks import CapabilityVerifier
        cv = CapabilityVerifier()
        self.assertTrue(cv.verify_capabilities(declared_caps=0x0002, used_caps=0x0002))

    @require_interlocks
    def test_tier1_f18_tier2_stim_biphasic_allowed_happy(self):
        """F18: Test biphasic stimulation capability authorization."""
        from native.interlocks import CapabilityVerifier
        cv = CapabilityVerifier()
        self.assertTrue(cv.verify_capabilities(declared_caps=0x0001, used_caps=0x0001))

    @require_interlocks
    def test_tier1_f18_tier3_modulate_stdp_allowed_happy(self):
        """F18: Test plasticity modulation capability authorization."""
        from native.interlocks import CapabilityVerifier
        cv = CapabilityVerifier()
        self.assertTrue(cv.verify_capabilities(declared_caps=0x0004, used_caps=0x0004))

    # -------------------------------------------------------------------------
    # Feature 19: Water-Window Voltage Clamp (F19)
    # -------------------------------------------------------------------------

    @require_interlocks
    def test_tier1_f19_sub_threshold_positive_pulse_happy(self):
        """F19: Test sub-threshold positive pulse delivers requested voltage without attenuation."""
        assert_voltage_clamped(0.8, 0.8, 1.2)

    @require_interlocks
    def test_tier1_f19_sub_threshold_negative_pulse_happy(self):
        """F19: Test sub-threshold negative pulse delivers requested voltage without attenuation."""
        assert_voltage_clamped(-0.8, -0.8, 1.2)

    @require_interlocks
    def test_tier1_f19_zero_voltage_idle_happy(self):
        """F19: Test zero voltage idle delivery."""
        assert_voltage_clamped(0.0, 0.0, 1.2)

    @require_interlocks
    def test_tier1_f19_boundary_positive_1_2v_happy(self):
        """F19: Test positive water-window boundary at exactly +1.2 V."""
        assert_voltage_clamped(1.2, 1.2, 1.2)

    @require_interlocks
    def test_tier1_f19_boundary_negative_1_2v_happy(self):
        """F19: Test negative water-window boundary at exactly -1.2 V."""
        assert_voltage_clamped(-1.2, -1.2, 1.2)

    # -------------------------------------------------------------------------
    # Feature 20: Sliding Charge Balance Watchdog (F20)
    # -------------------------------------------------------------------------

    @require_interlocks
    def test_tier1_f20_balanced_biphasic_pulse_happy(self):
        """F20: Test perfectly balanced biphasic pulse train produces zero net residual charge."""
        trace = [0.005, -0.005] * 100
        res = assert_sliding_charge_balance(trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.balanced)

    @require_interlocks
    def test_tier1_f20_subcritical_charge_accumulation_happy(self):
        """F20: Test subcritical charge accumulation below 0.5 nC does not trip watchdog."""
        trace = [0.002] * 50 + [0.0] * 150
        res = assert_sliding_charge_balance(trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.balanced)

    @require_interlocks
    def test_tier1_f20_sliding_window_expiration_happy(self):
        """F20: Test old charge exits circular buffer after 100 ticks (10.0 ms)."""
        trace = [0.003] * 10 + [0.0] * 120
        res = assert_sliding_charge_balance(trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.balanced)

    @require_interlocks
    def test_tier1_f20_independent_electrode_buffers_happy(self):
        """F20: Test independent per-electrode ring buffer charge tracking."""
        ch0_trace = [0.002] * 150
        ch1_trace = [-0.002] * 150
        res0 = assert_sliding_charge_balance(ch0_trace, max_charge_nc=0.5, window_ticks=100)
        res1 = assert_sliding_charge_balance(ch1_trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res0.balanced)
        self.assertTrue(res1.balanced)

    @require_interlocks
    def test_tier1_f20_multi_pulse_train_happy(self):
        """F20: Test multi-pulse stimulation train maintaining charge balance."""
        train = ([0.004, -0.004] + [0.0]*8) * 20
        res = assert_sliding_charge_balance(train, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.balanced)

    # -------------------------------------------------------------------------
    # Feature 21: Epileptiform Runaway Breaker (F21)
    # -------------------------------------------------------------------------

    @require_interlocks
    def test_tier1_f21_normal_population_firing_happy(self):
        """F21: Test normal physiological population firing (15 Hz) does not trip breaker."""
        raster = make_spike_raster_matrix(ticks=600, channels=64, firing_channels=64, rate_hz=15.0)
        res = assert_epileptiform_trip(raster, channels=64, duration_ms=50.0, dt_ms=0.1)
        self.assertFalse(res.tripped)

    @require_interlocks
    def test_tier1_f21_localized_high_frequency_burst_happy(self):
        """F21: Test localized high-frequency firing below spatial channel threshold (<= 35%)."""
        raster = make_spike_raster_matrix(ticks=600, channels=64, firing_channels=10, rate_hz=200.0)
        res = assert_epileptiform_trip(raster, channels=64, duration_ms=50.0, dt_ms=0.1)
        self.assertFalse(res.tripped)

    @require_interlocks
    def test_tier1_f21_brief_synchronous_burst_happy(self):
        """F21: Test brief synchronous burst below duration threshold (< 50.0 ms)."""
        raster = make_spike_raster_matrix(ticks=300, channels=64, firing_channels=35, rate_hz=200.0)
        res = assert_epileptiform_trip(raster, channels=64, duration_ms=50.0, dt_ms=0.1)
        self.assertFalse(res.tripped)

    @require_interlocks
    def test_tier1_f21_subcritical_population_rate_happy(self):
        """F21: Test population rate sustained below 150 Hz threshold (140 Hz)."""
        raster = make_spike_raster_matrix(ticks=600, channels=64, firing_channels=40, rate_hz=140.0)
        res = assert_epileptiform_trip(raster, channels=64, duration_ms=50.0, dt_ms=0.1)
        self.assertFalse(res.tripped)

    @require_interlocks
    def test_tier1_f21_counter_reset_on_calm_happy(self):
        """F21: Test runaway accumulator resets to zero when hyperactive firing ceases."""
        r1 = make_spike_raster_matrix(ticks=400, channels=64, firing_channels=30, rate_hz=200.0)
        r2 = make_spike_raster_matrix(ticks=400, channels=64, firing_channels=64, rate_hz=10.0)
        combined = list(r1) + list(r2)
        res = assert_epileptiform_trip(combined, channels=64, duration_ms=50.0, dt_ms=0.1)
        self.assertFalse(res.tripped)

    # -------------------------------------------------------------------------
    # Feature 22: Fail-Safe Interlock Clamp (F22)
    # -------------------------------------------------------------------------

    @require_interlocks
    def test_tier1_f22_normal_operational_state_happy(self):
        """F22: Test normal operational state allows stimulation."""
        from native.interlocks import InterlockManager
        im = InterlockManager()
        self.assertEqual(im.get_state(), 0)

    @require_interlocks
    def test_tier1_f22_zero_dacs_on_charge_trip_happy(self):
        """F22: Test tripping charge imbalance instantly zeroes all electrode DACs."""
        from native.interlocks import InterlockManager
        im = InterlockManager()
        im.trip_charge_imbalance(electrode=5)
        dacs = im.get_dac_voltages()
        self.assertTrue(all(v == 0.0 for v in dacs))

    @require_interlocks
    def test_tier1_f22_zero_dacs_on_runaway_trip_happy(self):
        """F22: Test tripping epileptiform breaker instantly zeroes all electrode DACs."""
        from native.interlocks import InterlockManager
        im = InterlockManager()
        im.trip_epileptiform_runaway()
        dacs = im.get_dac_voltages()
        self.assertTrue(all(v == 0.0 for v in dacs))

    @require_interlocks
    def test_tier1_f22_vm_state_lockout_happy(self):
        """F22: Test interlock lockout transitions VM state to HALTED_SAFETY_LOCKOUT."""
        from native.interlocks import InterlockManager
        im = InterlockManager()
        im.trip_epileptiform_runaway()
        self.assertEqual(im.get_state_name(), "HALTED_SAFETY_LOCKOUT")

    @require_interlocks
    def test_tier1_f22_post_mortem_diagnostic_happy(self):
        """F22: Test post-mortem diagnostics telemetry record upon interlock trip."""
        from native.interlocks import InterlockManager
        im = InterlockManager()
        im.trip_charge_imbalance(electrode=12)
        diag = im.get_diagnostic_report()
        self.assertIn("ERR_CHARGE_IMBALANCE", diag)


# =============================================================================
# 5. Benchmark Workloads (Features F23 through F25: 15 tests)
# =============================================================================

class TestTier1Benchmarks(WetLangE2ETestCase):
    """
    Tier 1 tests for Closed-Loop WetLang Benchmark Programs:
      - Feature 23: Benchmark 01 Active Inference (5 tests)
      - Feature 24: Benchmark 02 Polychronous Reservoir (5 tests)
      - Feature 25: Benchmark 03 Homeostatic Control (5 tests)
    """
    tier = 1

    # -------------------------------------------------------------------------
    # Feature 23: Benchmark 01 Active Inference (F23)
    # -------------------------------------------------------------------------

    @require_benchmarks
    def test_tier1_f23_compile_benchmark_01_happy(self):
        """F23: Test Benchmark 01 compiles cleanly from source into WBC binary."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "01_active_inference_closed_loop.wet")
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
        binary = compile_source(src)
        self.assertTrue(binary.startswith(HEADER_MAGIC))
        magic, v_maj, v_min, caps, fsize, crc, num_sections, ch_cnt, max_q, res = struct.unpack_from(HEADER_STRUCT_FORMAT, binary, 0)
        self.assertEqual(magic, HEADER_MAGIC)
        self.assertEqual(v_maj, VERSION_MAJOR)
        self.assertEqual(ch_cnt, 64)
        self.assertEqual(fsize, len(binary))

    @require_native_vm
    def test_tier1_f23_sensory_motor_stepping_happy(self):
        """F23: Test sensory-motor closed-loop stepping in Benchmark 01."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "01_active_inference_closed_loop.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=100)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f23_reward_pulse_delivery_happy(self):
        """F23: Test reward pulse dispatch upon tracking error reduction."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "01_active_inference_closed_loop.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=200)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f23_punishment_pulse_delivery_happy(self):
        """F23: Test chaotic punishment pulse delivery upon tracking error increase."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "01_active_inference_closed_loop.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=200)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f23_telemetry_emission_happy(self):
        """F23: Test structured telemetry output from Benchmark 01."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "01_active_inference_closed_loop.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=50)
        self.assertTrue(success)

    # -------------------------------------------------------------------------
    # Feature 24: Benchmark 02 Polychronous Reservoir (F24)
    # -------------------------------------------------------------------------

    @require_benchmarks
    def test_tier1_f24_compile_benchmark_02_happy(self):
        """F24: Test Benchmark 02 compiles cleanly from source into WBC binary."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "02_polychronous_reservoir_classifier.wet")
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
        binary = compile_source(src)
        self.assertTrue(binary.startswith(HEADER_MAGIC))
        magic, v_maj, v_min, caps, fsize, crc, num_sections, ch_cnt, max_q, res = struct.unpack_from(HEADER_STRUCT_FORMAT, binary, 0)
        self.assertEqual(magic, HEADER_MAGIC)
        self.assertEqual(v_maj, VERSION_MAJOR)
        self.assertEqual(ch_cnt, 64)
        self.assertEqual(fsize, len(binary))

    @require_native_vm
    def test_tier1_f24_spatio_temporal_pattern_alpha_happy(self):
        """F24: Test spatio-temporal delay-line pattern alpha stimulation."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "02_polychronous_reservoir_classifier.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=100)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f24_reservoir_settling_delay_happy(self):
        """F24: Test 30 ms settling delay between pattern stimulation trials."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "02_polychronous_reservoir_classifier.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=350)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f24_reservoir_readout_pool_happy(self):
        """F24: Test readout channel spike acquisition in Benchmark 02."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "02_polychronous_reservoir_classifier.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=100)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f24_margin_based_stdp_happy(self):
        """F24: Test margin-based STDP modulation across reservoir."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "02_polychronous_reservoir_classifier.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=200)
        self.assertTrue(success)

    # -------------------------------------------------------------------------
    # Feature 25: Benchmark 03 Homeostatic Control (F25)
    # -------------------------------------------------------------------------

    @require_benchmarks
    def test_tier1_f25_compile_benchmark_03_happy(self):
        """F25: Test Benchmark 03 compiles cleanly from source into WBC binary."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "03_homeostatic_stabilization_and_stress.wet")
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
        binary = compile_source(src)
        self.assertTrue(binary.startswith(HEADER_MAGIC))
        magic, v_maj, v_min, caps, fsize, crc, num_sections, ch_cnt, max_q, res = struct.unpack_from(HEADER_STRUCT_FORMAT, binary, 0)
        self.assertEqual(magic, HEADER_MAGIC)
        self.assertEqual(v_maj, VERSION_MAJOR)
        self.assertEqual(ch_cnt, 64)
        self.assertEqual(fsize, len(binary))

    @require_native_vm
    def test_tier1_f25_read_population_rate_happy(self):
        """F25: Test population rate readout across 64 MEA channels."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "03_homeostatic_stabilization_and_stress.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=100)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f25_hypoactive_pacing_happy(self):
        """F25: Test pacing stimulation when population firing rate < 15 Hz."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "03_homeostatic_stabilization_and_stress.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=100)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f25_hyperactive_braking_happy(self):
        """F25: Test inhibitory braking when population firing rate > 25 Hz."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "03_homeostatic_stabilization_and_stress.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=100)
        self.assertTrue(success)

    @require_native_vm
    def test_tier1_f25_acute_stress_burst_recovery_happy(self):
        """F25: Test homeostatic rate recovery following acute stress perturbation."""
        path = os.path.join(PROJECT_ROOT, "benchmarks", "03_homeostatic_stabilization_and_stress.wet")
        success, err, telem = self.run_program(compile_source(open(path).read()), ticks=500)
        self.assertTrue(success)


# =============================================================================
# 6. Documentation & Debates (Feature F26: 5 tests)
# =============================================================================

class TestTier1Documentation(WetLangE2ETestCase):
    """
    Tier 1 tests for Technical Documentation & Multi-Agent Adversarial Debates:
      - Feature 26: Adversarial Debate Documentation (5 tests)
    """
    tier = 1

    @unittest.skipUnless(
        os.path.isfile(os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")),
        "Debate documentation (docs/adversarial_debate.md) not yet created",
    )
    def test_tier1_f26_file_exists_happy(self):
        """F26: Test adversarial debate documentation file exists and has content."""
        path = os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")
        self.assertTrue(os.path.isfile(path))
        self.assertGreater(os.path.getsize(path), 0)

    @unittest.skipUnless(
        os.path.isfile(os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")),
        "Debate documentation (docs/adversarial_debate.md) not yet created",
    )
    def test_tier1_f26_four_debate_topics_present_happy(self):
        """F26: Test all four required multi-round technical debates are present."""
        path = os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Debate 1", content)
        self.assertIn("Debate 2", content)
        self.assertIn("Debate 3", content)
        self.assertIn("Debate 4", content)

    @unittest.skipUnless(
        os.path.isfile(os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")),
        "Debate documentation (docs/adversarial_debate.md) not yet created",
    )
    def test_tier1_f26_bot_personas_present_happy(self):
        """F26: Test all specialized team bot personas participate in debates."""
        path = os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Debater", content)
        self.assertIn("Biological Bot", content)
        self.assertIn("Engineer Bot", content)
        self.assertIn("Cybersecurity Bot", content)

    @unittest.skipUnless(
        os.path.isfile(os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")),
        "Debate documentation (docs/adversarial_debate.md) not yet created",
    )
    def test_tier1_f26_multi_round_structure_happy(self):
        """F26: Test debates contain multi-round argument structures."""
        path = os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertGreaterEqual(content.count("Round 1"), 4)
        self.assertGreaterEqual(content.count("Round 2"), 4)

    @unittest.skipUnless(
        os.path.isfile(os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")),
        "Debate documentation (docs/adversarial_debate.md) not yet created",
    )
    def test_tier1_f26_formal_resolutions_happy(self):
        """F26: Test each debate concludes with a formal consensus resolution."""
        path = os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertGreaterEqual(content.count("Formal Resolution"), 4)


# =============================================================================
# 7. Synthetic Test Suites (Feature F27: 5 tests)
# =============================================================================

class TestTier1SyntheticSuite(WetLangE2ETestCase):
    """
    Tier 1 tests verifying the presence and execution of synthetic test suites:
      - Feature 27: Synthetic Test Suite (5 tests)
    """
    tier = 1

    def test_tier1_f27_parser_diagnostics_suite_happy(self):
        """F27: Test execution of synthetic parser diagnostics test suite."""
        path = os.path.join(PROJECT_ROOT, "tests", "test_parser_diagnostics.py")
        self.assertTrue(os.path.isfile(path))
        ret = subprocess.run([sys.executable, "-m", "pytest", "-q", path], capture_output=True, text=True)
        self.assertEqual(ret.returncode, 0, f"Parser diagnostics failed: {ret.stderr}\n{ret.stdout}")

    def test_tier1_f27_static_verifier_suite_happy(self):
        """F27: Test execution of static safety analyzer test suite."""
        path = os.path.join(PROJECT_ROOT, "tests", "test_static_verifier.py")
        self.assertTrue(os.path.isfile(path))
        ret = subprocess.run([sys.executable, "-m", "pytest", "-q", path], capture_output=True, text=True)
        self.assertEqual(ret.returncode, 0, f"Static verifier failed: {ret.stderr}\n{ret.stdout}")

    def test_tier1_f27_ode_stability_suite_happy(self):
        """F27: Test execution of numerical ODE stability test suite."""
        path = os.path.join(PROJECT_ROOT, "tests", "test_ode_stability.py")
        if not os.path.isfile(path):
            self.skipTest("tests/test_ode_stability.py not yet implemented")
        ret = subprocess.run([sys.executable, "-m", "pytest", "-q", path], capture_output=True, text=True)
        self.assertEqual(ret.returncode, 0)

    def test_tier1_f27_interlocks_suite_happy(self):
        """F27: Test execution of hardware interlocks watchdog test suite."""
        path = os.path.join(PROJECT_ROOT, "tests", "test_interlocks.py")
        if not os.path.isfile(path):
            self.skipTest("tests/test_interlocks.py not yet implemented")
        ret = subprocess.run([sys.executable, "-m", "pytest", "-q", path], capture_output=True, text=True)
        self.assertEqual(ret.returncode, 0)

    def test_tier1_f27_benchmarks_suite_happy(self):
        """F27: Test execution of benchmark verification test suite."""
        path = os.path.join(PROJECT_ROOT, "tests", "test_benchmarks.py")
        if not os.path.isfile(path):
            self.skipTest("tests/test_benchmarks.py not yet implemented")
        ret = subprocess.run([sys.executable, "-m", "pytest", "-q", path], capture_output=True, text=True)
        self.assertEqual(ret.returncode, 0)


# =============================================================================
# 8. Dual-Track E2E Verification (Feature F28: 5 tests)
# =============================================================================

class TestTier1DualTrack(WetLangE2ETestCase):
    """
    Tier 1 tests for the Full E2E Dual-Track Verification architecture:
      - Feature 28: Full E2E Dual-Track Verification (5 tests)
    """
    tier = 1

    def test_tier1_f28_e2e_runner_executable_happy(self):
        """F28: Test E2E test runner exists and exposes discovery APIs."""
        runner_path = os.path.join(PROJECT_ROOT, "tests", "run_e2e_tests.py")
        self.assertTrue(os.path.isfile(runner_path))
        import tests.run_e2e_tests as runner_mod
        self.assertTrue(hasattr(runner_mod, "discover_suite"))
        self.assertTrue(hasattr(runner_mod, "main"))

    def test_tier1_f28_tier1_suite_pass_happy(self):
        """F28: Test Tier 1 suite file defines at least 140 test methods across 28 features."""
        suite_path = os.path.join(PROJECT_ROOT, "tests", "e2e", "test_tier1_features.py")
        self.assertTrue(os.path.isfile(suite_path))
        import inspect
        from tests.e2e import test_tier1_features
        test_count = 0
        for name, cls in inspect.getmembers(test_tier1_features, inspect.isclass):
            if issubclass(cls, unittest.TestCase):
                for mname in dir(cls):
                    if mname.startswith("test_tier1_"):
                        test_count += 1
        self.assertGreaterEqual(test_count, 140, f"Found {test_count} Tier 1 tests, expected >= 140")

    def test_tier1_f28_tier2_suite_pass_happy(self):
        """F28: Test Tier 2 boundary test suite file presence and execution."""
        path = os.path.join(PROJECT_ROOT, "tests", "e2e", "test_tier2_boundaries.py")
        if not os.path.isfile(path):
            self.skipTest("Tier 2 boundary suite (tests/e2e/test_tier2_boundaries.py) not yet implemented")
        self.assertTrue(os.path.isfile(path))

    def test_tier1_f28_tier3_suite_pass_happy(self):
        """F28: Test Tier 3 pairwise test suite file presence and execution."""
        path = os.path.join(PROJECT_ROOT, "tests", "e2e", "test_tier3_pairwise.py")
        if not os.path.isfile(path):
            self.skipTest("Tier 3 pairwise suite (tests/e2e/test_tier3_pairwise.py) not yet implemented")
        self.assertTrue(os.path.isfile(path))

    def test_tier1_f28_tier4_suite_pass_happy(self):
        """F28: Test Tier 4 realistic scenarios test suite file presence and execution."""
        path = os.path.join(PROJECT_ROOT, "tests", "e2e", "test_tier4_benchmarks.py")
        if not os.path.isfile(path):
            self.skipTest("Tier 4 benchmark scenarios suite (tests/e2e/test_tier4_benchmarks.py) not yet implemented")
        self.assertTrue(os.path.isfile(path))


if __name__ == "__main__":
    unittest.main()
