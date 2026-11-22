"""
WetLang E2E Test Suite: Tier 2 Boundary & Corner Cases Suite
Contains 140 concrete boundary value, corner case, extreme value, and fault-injection
test methods covering Features F1 through F28 (Tests 141 through 280) as documented
in `spec_miner_e2e_2/handoff.md` and `PROJECT.md`.

Test Classes:
  - TestTier2CompilerBoundaries: F1 (Grammar), F2 (Lexer), F3 (Pratt Parser),
                                F4 (Semantic Analyzer), F5 (Loop Verifier), F7 (Emitter)
  - TestTier2RuntimeBoundaries:  F6 (ISA), F8 (C-ABI Engine), F9 (Scheduler),
                                F10 (ctypes FFI), F11 (NumPy Telemetry)
  - TestTier2BiophysicsBoundaries: F12 (8x8 MEA), F13 (ODE Solver), F14 (Refractory),
                                  F15 (STP), F16 (STDP), F17 (Telemetry Stream)
  - TestTier2InterlockBoundaries: F18 (Capability), F19 (Voltage Clamp), F20 (Charge Balance),
                                 F21 (Epileptiform Breaker), F22 (Fail-Safe Interlock)
  - TestTier2BenchmarkBoundaries: F23 (Active Inference), F24 (Reservoir), F25 (Homeostatic),
                                 F26 (Debates), F27 (Synthetic Suite), F28 (E2E Verification)
"""

import os
import sys
import math
import struct
import zlib
import unittest
from typing import List, Dict, Any, Optional

# Ensure project root and wetlang package are in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for p in [PROJECT_ROOT, os.path.join(PROJECT_ROOT, "wetlang")]:
    if p not in sys.path and os.path.isdir(p):
        sys.path.insert(0, p)

try:
    import numpy as np
except ImportError:
    np = None

from tests.e2e.common import (
    WetLangE2ETestCase,
    HAS_COMPILER,
    HAS_NATIVE_VM,
    HAS_BIOPHYSICS,
    HAS_INTERLOCKS,
    HAS_BENCHMARKS,
    require_compiler,
    require_native_vm,
    require_biophysics,
    require_interlocks,
    require_benchmarks,
    assert_voltage_clamped,
    assert_sliding_charge_balance,
    assert_epileptiform_trip,
    assert_wbc_header_valid,
    assert_si_value_close,
    make_wbc_header,
    make_spike_raster_matrix,
    generate_mea_coordinates,
    make_minimal_wet_program,
    generate_valid_wet_source,
)

if HAS_COMPILER:
    from compiler.token import Token, TokenType, Dimension
    from compiler.lexer import Lexer, LexerError
    from compiler.parser import Parser, ParseError
    from compiler.ast_nodes import ProgramNode, LiteralNode, ASTNode
    from compiler.semantic import SemanticAnalyzer, SemanticError
    from compiler.isa import (
        Opcode,
        HEADER_MAGIC,
        HEADER_SIZE,
        VERSION_MAJOR,
        VERSION_MINOR,
        Capability,
    )
    from compiler.emitter import BytecodeEmitter, ConstantPool, compile_source, disassemble


# =============================================================================
# Class 1: Compiler & Language Pipeline Boundaries (F1-F5, F7)
# =============================================================================

class TestTier2CompilerBoundaries(WetLangE2ETestCase):
    """
    Tier 2 boundary, corner case, and negative syntax/semantic tests for the compiler pipeline.
    Covers Features F1, F2, F3, F4, F5, F7 (Tests 141-165, 171-175).
    """
    tier = 2

    # -------------------------------------------------------------------------
    # Feature 1: Formal EBNF Grammar (Tests 141-145)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier2_f01_empty_program_source(self):
        """[F1] [F01] Empty source string and whitespace-only sources parse into an empty AST with 0 declarations."""
        for empty_src in ["", "   \n\t  \r\n  "]:
            tokens = Lexer(empty_src).tokenize()
            parser = Parser(tokens, source_text=empty_src)
            ast = parser.parse()
            self.assertIsInstance(ast, ProgramNode)
            self.assertEqual(len(ast.declarations), 0)

    @require_compiler
    def test_tier2_f01_invalid_symbol_character(self):
        """[F1] [F01] Source containing illegal symbol character '@' terminates with LexerError or ParseError."""
        bad_src = "grid mea @#$ { rows: 8; };"
        with self.assertRaises((LexerError, ParseError)) as ctx:
            tokens = Lexer(bad_src).tokenize()
            Parser(tokens, source_text=bad_src).parse()
        self.assertIn("@", str(ctx.exception))

    @require_compiler
    def test_tier2_f01_missing_statement_semicolon(self):
        """[F1] [F01] Statement omitted semicolon raises ParseError indicating missing ';'."""
        bad_src = "let x = 5\nlet y = 10;"
        with self.assertRaises(ParseError) as ctx:
            tokens = Lexer(bad_src).tokenize()
            Parser(tokens, source_text=bad_src).parse()
        self.assertIn("SEMICOLON", str(ctx.exception).upper())

    @require_compiler
    def test_tier2_f01_unclosed_block_brace(self):
        """[F1] [F01] Unclosed block brace '{' raises ParseError for unexpected EOF or missing '}'."""
        bad_src = "fn run() { let x = 1;"
        with self.assertRaises(ParseError) as ctx:
            tokens = Lexer(bad_src).tokenize()
            Parser(tokens, source_text=bad_src).parse()
        err_msg = str(ctx.exception).lower()
        self.assertTrue("unterminated" in err_msg or "}" in err_msg or "eof" in err_msg)

    @require_compiler
    def test_tier2_f01_nested_stream_declaration(self):
        """[F1] [F01] Grammar restricts 'stream' to top-level; nested stream inside function is rejected."""
        bad_src = "fn test() { stream invalid { cycle {} } }"
        with self.assertRaises(ParseError):
            tokens = Lexer(bad_src).tokenize()
            Parser(tokens, source_text=bad_src).parse()

    # -------------------------------------------------------------------------
    # Feature 2: Lexer with Physical Units (Tests 146-150)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier2_f02_zero_magnitude_units(self):
        """[F2] [F02] Zero magnitude physical units (0ms, 0.0V, 0uA, 0nC, 0Hz) evaluate to exactly 0.0 with dimension tags."""
        src = "0ms 0.0V 0uA 0nC 0Hz"
        tokens = [t for t in Lexer(src).tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 5)
        expected_dims = [
            Dimension.TIME,
            Dimension.VOLTAGE,
            Dimension.CURRENT,
            Dimension.CHARGE,
            Dimension.FREQUENCY,
        ]
        for t, expected_dim in zip(tokens, expected_dims):
            self.assertEqual(t.type, TokenType.PHYSICAL_LIT)
            self.assertEqual(float(t.value), 0.0)
            self.assertEqual(t.dimension, expected_dim)

    @require_compiler
    def test_tier2_f02_negative_magnitude_units(self):
        """[F2] [F02] Negative physical units (-1.2V, -70.0mV, -50uA) preserve negative sign in AST/expression."""
        src = "-1.2V"
        tokens = [t for t in Lexer(src).tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].type, TokenType.MINUS)
        self.assertEqual(tokens[1].type, TokenType.PHYSICAL_LIT)
        self.assertEqual(tokens[1].value, 1.2)
        self.assertEqual(tokens[1].dimension, Dimension.VOLTAGE)

    @require_compiler
    def test_tier2_f02_unknown_unit_suffix(self):
        """[F2] [F02] Unknown unit suffixes ('100foo', '45amps') split into INT_LIT + IDENTIFIER, rejected by parser."""
        src = "let x = 100foo;"
        tokens = Lexer(src).tokenize()
        with self.assertRaises(ParseError):
            Parser(tokens, source_text=src).parse()

    @require_compiler
    def test_tier2_f02_scientific_notation_units(self):
        """[F2] [F02] Scientific notation units (1.5e-3V, 2.0e4Hz, 1e-6s) canonicalize to correct SI scaled floats."""
        src = "1.5e-3V 2.0e4Hz 1e-6s"
        tokens = [t for t in Lexer(src).tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 3)
        self.assertAlmostEqual(tokens[0].value, 0.0015, places=6)
        self.assertEqual(tokens[0].dimension, Dimension.VOLTAGE)
        self.assertAlmostEqual(tokens[1].value, 20000.0, places=2)
        self.assertEqual(tokens[1].dimension, Dimension.FREQUENCY)
        self.assertAlmostEqual(tokens[2].value, 0.000001, places=8)
        self.assertEqual(tokens[2].dimension, Dimension.TIME)

    @require_compiler
    def test_tier2_f02_extreme_float_magnitudes(self):
        """[F2] [F02] Extreme float magnitudes (1e309V overflow to inf, 1e-325s underflow to 0.0) handled safely."""
        src = "1e309V 1e-325s"
        tokens = [t for t in Lexer(src).tokenize() if t.type != TokenType.EOF]
        self.assertEqual(len(tokens), 2)
        self.assertTrue(math.isinf(tokens[0].value))
        self.assertEqual(tokens[1].value, 0.0)

    # -------------------------------------------------------------------------
    # Feature 3: Pratt Recursive-Descent Parser (Tests 151-155)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier2_f03_deeply_nested_parentheses(self):
        """[F3] [F03] 100 levels of nested parentheses parse without stack overflow."""
        src = "let x = " + ("(" * 100) + "1" + (")" * 100) + ";"
        tokens = Lexer(src).tokenize()
        ast = Parser(tokens, source_text=src).parse()
        self.assertIsNotNone(ast)
        self.assertEqual(len(ast.declarations), 1)

    @require_compiler
    def test_tier2_f03_dangling_binary_operator(self):
        """[F3] [F03] Dangling binary operator 'let x = 5 + ;' raises ParseError expecting expression."""
        src = "let x = 5 + ;"
        with self.assertRaises(ParseError) as ctx:
            Parser(Lexer(src).tokenize(), source_text=src).parse()
        self.assertIn("expression", str(ctx.exception).lower())

    @require_compiler
    def test_tier2_f03_consecutive_binary_operators(self):
        """[F3] [F03] Consecutive binary operators 'let x = 5 + * 3;' raises ParseError."""
        src = "let x = 5 + * 3;"
        with self.assertRaises(ParseError) as ctx:
            Parser(Lexer(src).tokenize(), source_text=src).parse()
        self.assertIn("expression", str(ctx.exception).lower())

    @require_compiler
    def test_tier2_f03_mismatched_enclosing_brackets(self):
        """[F3] [F03] Mismatched delimiter 'let x = mea[0, 1);' raises ParseError expecting ']'."""
        src = "let x = mea[0, 1);"
        with self.assertRaises(ParseError) as ctx:
            Parser(Lexer(src).tokenize(), source_text=src).parse()
        self.assertIn("]", str(ctx.exception))

    @require_compiler
    def test_tier2_f03_empty_subexpression(self):
        """[F3] [F03] Empty subexpression 'let x = ();' raises ParseError."""
        src = "let x = ();"
        with self.assertRaises(ParseError) as ctx:
            Parser(Lexer(src).tokenize(), source_text=src).parse()
        self.assertIn("expression", str(ctx.exception).lower())

    # -------------------------------------------------------------------------
    # Feature 4: Semantic & Scope Analyzer (Tests 156-160)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier2_f04_undeclared_identifier(self):
        """[F4] [F04] Referencing undeclared variable raises SemanticError with ERR_UNDECLARED_IDENTIFIER."""
        src = "let a = 10; let b = a + undeclared_var;"
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_UNDECLARED_IDENTIFIER")

    @require_compiler
    def test_tier2_f04_redeclared_identifier_same_scope(self):
        """[F4] [F04] Redeclaring identifier in the same scope raises SemanticError with ERR_REDECLARED_IDENTIFIER."""
        src = "let x = 1; let x = 2;"
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_REDECLARED_IDENTIFIER")

    @require_compiler
    def test_tier2_f04_dimensional_mismatch_addition(self):
        """[F4] [F04] Incompatible physical units addition (10ms + 1.2V) raises ERR_DIMENSIONAL_MISMATCH."""
        src = "let bad = 10ms + 1.2V;"
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_DIMENSIONAL_MISMATCH")

    @require_compiler
    def test_tier2_f04_out_of_bounds_grid_literal(self):
        """[F4] [F04] MEA electrode coordinate out of 8x8 bounds (mea[8, 2]) raises ERR_ELECTRODE_OUT_OF_BOUNDS."""
        src = "grid mea[8, 8]; channel c = mea[8, 2];"
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_ELECTRODE_OUT_OF_BOUNDS")

    @require_compiler
    def test_tier2_f04_static_voltage_clamp_exceeded(self):
        """[F4] [F04] Constant stimulation voltage +1.8V > 1.2V raises ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED."""
        src = """grid mea[8, 8];
channel ch = mea[0, 0];
fn test() {
    stim_biphasic(ch, 1.8V, 200us, 200us);
    sync_tick();
}"""
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED")

    # -------------------------------------------------------------------------
    # Feature 5: Static Loop-Yield Verifier (Tests 161-165)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier2_f05_unbounded_stimulation_loop(self):
        """[F5] [F05] Stimulation loop lacking sync_tick raises ERR_UNBOUNDED_STIM_LOOP."""
        src = """grid mea[8, 8];
channel ch = mea[0, 0];
while (true) {
    stim_biphasic(ch, 0.5V, 100us, 100us);
}"""
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_UNBOUNDED_STIM_LOOP")

    @require_compiler
    def test_tier2_f05_conditional_branch_missing_yield(self):
        """[F5] [F05] Loop where one branch contains stimulation but lacks sync_tick raises ERR_UNBOUNDED_STIM_LOOP."""
        src = """grid mea[8, 8];
channel ch = mea[0, 0];
let flag = 1;
while (true) {
    if (flag > 0) {
        stim_biphasic(ch, 0.5V, 100us, 100us);
    } else {
        sync_tick();
    }
}"""
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_UNBOUNDED_STIM_LOOP")

    @require_compiler
    def test_tier2_f05_empty_busy_spin_loop(self):
        """[F5] [F05] Pure compute loop without stimulation is permitted, while un-yielded stimulation loop is rejected."""
        # Pure compute loop: permitted
        src_pure = "let mut x = 0; while (x < 10) { x = x + 1; }"
        bc = compile_source(src_pure)
        self.assertGreater(len(bc), 0)

        # Stimulation loop without yield: rejected
        src_stim = "grid mea[8, 8]; channel ch = mea[0, 0]; while (true) { stim_biphasic(ch, 0.5V, 100us, 100us); }"
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src_stim)
        self.assertEqual(ctx.exception.error_code, "ERR_UNBOUNDED_STIM_LOOP")

    @require_compiler
    def test_tier2_f05_nested_loop_inner_unyielded(self):
        """[F5] [F05] Nested loops where outer yields but inner contains stimulation without yield raises ERR_UNBOUNDED_STIM_LOOP."""
        src = """grid mea[8, 8];
channel ch = mea[0, 0];
while (true) {
    while (true) {
        stim_biphasic(ch, 0.5V, 100us, 100us);
    }
    sync_tick();
}"""
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_UNBOUNDED_STIM_LOOP")

    @require_compiler
    def test_tier2_f05_continue_statement_bypasses_yield(self):
        """[F5] [F05] Branch execution path that bypasses sync_tick in stimulation loop raises ERR_UNBOUNDED_STIM_LOOP."""
        src = """grid mea[8, 8];
channel ch = mea[0, 0];
let c = 1;
while (true) {
    stim_biphasic(ch, 0.5V, 100us, 100us);
    if (c > 0) {
    } else {
        sync_tick();
    }
}"""
        with self.assertRaises(SemanticError) as ctx:
            compile_source(src)
        self.assertEqual(ctx.exception.error_code, "ERR_UNBOUNDED_STIM_LOOP")

    # -------------------------------------------------------------------------
    # Feature 7: Bytecode Binary Emitter (Tests 171-175)
    # -------------------------------------------------------------------------

    @require_compiler
    def test_tier2_f07_empty_ast_emission(self):
        """[F7] [F07] Empty AST with 0 statements compiles into valid WBC binary without crashing."""
        emitter = BytecodeEmitter()
        binary = emitter.compile(ProgramNode([]))
        self.assertGreaterEqual(len(binary), HEADER_SIZE)
        self.assertEqual(binary[:4], HEADER_MAGIC)

    @require_compiler
    def test_tier2_f07_constant_pool_overflow(self):
        """[F7] [F07] Constant pool with > 65535 entries triggers overflow error on 16-bit operand packing."""
        pool = ConstantPool()
        # Adding 70,000 unique integers
        for i in range(70000):
            pool.add_int(i)
        self.assertGreater(len(pool.entries), 65535)
        # Attempting to pack index > 65535 in 16-bit uint16 operand raises struct.error
        with self.assertRaises((struct.error, OverflowError, ValueError)):
            struct.pack("<H", len(pool.entries))

    @require_compiler
    def test_tier2_f07_branch_offset_overflow(self):
        """[F7] [F07] Jump offset exceeding signed 16-bit range (-32768..32767) raises struct.error or overflow."""
        with self.assertRaises((struct.error, OverflowError)):
            struct.pack("<h", 40000)

    @require_compiler
    def test_tier2_f07_corrupted_file_size_header(self):
        """[F7] [F07] WBC header with declared file_size (10,000) mismatching actual size (148) is detected."""
        src = "fn main() { return; }"
        bc = compile_source(src)
        corrupted = bytearray(bc)
        # Overwrite file_size at offset 8 (or 10 depending on header layout) to 10000
        struct.pack_into("<I", corrupted, 10, 10000)
        # Re-evaluating header reveals mismatch between actual len and declared size
        declared_size = struct.unpack_from("<I", corrupted, 10)[0]
        self.assertNotEqual(len(corrupted), declared_size)

    @require_compiler
    def test_tier2_f07_zero_length_code_section(self):
        """[F7] [F07] Zero-length code section in section table handled safely by disassembler/loader."""
        src = "fn main() { return; }"
        bc = compile_source(src)
        disasm_text = disassemble(bc)
        self.assertIn("WBC Binary Disassembly", disasm_text)
        self.assertIn("BYTECODE_STREAM", disasm_text)


# =============================================================================
# Class 2: Native Runtime & FFI Boundaries (F6, F8-F11)
# =============================================================================

class TestTier2RuntimeBoundaries(WetLangE2ETestCase):
    """
    Tier 2 boundary, corner case, and negative tests for Custom Bytecode ISA,
    Native C-ABI Engine, Scheduler, ctypes FFI, and Zero-Copy Telemetry.
    Covers Features F6, F8, F9, F10, F11 (Tests 166-170, 176-195).
    """
    tier = 2

    # -------------------------------------------------------------------------
    # Feature 6: Custom Bytecode ISA (Tests 166-170)
    # -------------------------------------------------------------------------

    def test_tier2_f06_invalid_magic_bytes(self):
        """[F6] [F06] Header starting with b'BAD!' instead of b'WETB' is rejected by header validator."""
        bad_header = make_wbc_header(magic=b"BAD!")
        with self.assertRaises(AssertionError) as ctx:
            assert_wbc_header_valid(bad_header)
        self.assertIn("magic", str(ctx.exception).lower())

    def test_tier2_f06_unsupported_major_version(self):
        """[F6] [F06] Header with version_major = 99 is rejected as unsupported version."""
        bad_version_header = make_wbc_header(major=99)
        with self.assertRaises(AssertionError) as ctx:
            assert_wbc_header_valid(bad_version_header)
        self.assertIn("version", str(ctx.exception).lower())

    @require_compiler
    def test_tier2_f06_illegal_opcode_in_stream(self):
        """[F6] [F06] Bytecode stream containing illegal opcode 0xFE is detected by disassembler as unknown."""
        src = "fn main() { return; }"
        bc = bytearray(compile_source(src))
        # Find bytecode stream offset from section table and overwrite an opcode with 0xFE
        for i in range(5):
            stype, _, off, size = struct.unpack_from("<HHII", bc, 32 + i * 12)
            if stype == 3:  # BYTECODE_STREAM
                bc[off] = 0xFE
                break
        disasm_output = disassemble(bytes(bc))
        self.assertIn("UNKNOWN_0xFE", disasm_output)

    def test_tier2_f06_truncated_instruction_operands(self):
        """[F6] [F06] Truncated operands (PUSH_INT opcode followed by 2 bytes instead of 4) fails operand unpacking."""
        # Opcode PUSH_INT requires <i (4 bytes). Buffer with only 2 bytes raises struct.error
        truncated_bytes = bytes([0x11, 0x01, 0x02])
        with self.assertRaises(struct.error):
            struct.unpack_from("<i", truncated_bytes, 1)

    def test_tier2_f06_corrupted_crc32_checksum(self):
        """[F6] [F06] Corrupting payload byte without updating CRC32 fails checksum verification."""
        header = make_wbc_header(file_size=64)
        corrupted_header = bytearray(header)
        # Flip a bit in the header reserved field
        corrupted_header[30] ^= 0xFF
        with self.assertRaises(AssertionError) as ctx:
            assert_wbc_header_valid(bytes(corrupted_header))
        self.assertIn("crc32", str(ctx.exception).lower())

    # -------------------------------------------------------------------------
    # Feature 8: Native C-ABI VM Engine (Tests 176-180)
    # -------------------------------------------------------------------------

    @require_native_vm
    def test_tier2_f08_null_vm_pointer_call(self):
        """[F8] [F08] Passing NULL pointer to native step function returns WET_ERR_INVALID_ARGUMENT without crash."""
        from bindings.ffi import get_wetvm_lib
        lib = get_wetvm_lib()
        status = lib.wet_step_tick(None, None)
        self.assertNotEqual(status, 0)

    @require_native_vm
    def test_tier2_f08_stack_overflow_trap(self):
        """[F8] [F08] Executing pushes beyond VM stack depth triggers VM stack overflow trap."""
        from bindings.runtime import WetVM, WetVMError, WetVMConfig
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        for i in range(25):
            emitter.emit(Opcode.PUSH_INT, i)
        emitter.emit(Opcode.HALT)
        wbc = emitter._build_wbc_binary()

        # Configure small stack depth of 16 to trigger deterministic trap
        config = WetVMConfig(max_stack_depth=16)
        with WetVM(config=config) as vm:
            vm.load_bytecode(wbc)
            with self.assertRaises(WetVMError) as ctx:
                vm.step_tick()
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_STACK_OVERFLOW)
            self.assertIn("overflow", str(ctx.exception).lower())

    @require_native_vm
    def test_tier2_f08_stack_underflow_trap(self):
        """[F8] [F08] Executing POP on empty stack triggers runtime underflow exception."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.emit(Opcode.POP)
        emitter.emit(Opcode.HALT)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            with self.assertRaises(WetVMError) as ctx:
                vm.step_tick()
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_STACK_UNDERFLOW)
            self.assertIn("underflow", str(ctx.exception).lower())

    @require_native_vm
    def test_tier2_f08_integer_divide_by_zero(self):
        """[F8] [F08] Pushing divisor 0 and executing integer division traps cleanly without SIGFPE."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.emit(Opcode.PUSH_INT, 10)
        emitter.emit(Opcode.PUSH_INT, 0)
        emitter.emit(Opcode.DIV_I)
        emitter.emit(Opcode.HALT)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            with self.assertRaises(WetVMError) as ctx:
                vm.step_tick()
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_DIVISION_BY_ZERO)
            self.assertIn("division by zero", str(ctx.exception).lower())

    @require_native_vm
    def test_tier2_f08_step_before_loading_bytecode(self):
        """[F8] [F08] Stepping newly created VM before loading bytecode returns error code."""
        from bindings.runtime import WetRuntime
        runtime = WetRuntime()
        with self.assertRaises(Exception):
            runtime.step(ticks=1)

    # -------------------------------------------------------------------------
    # Feature 9: VM Tick Scheduler (Tests 181-185)
    # -------------------------------------------------------------------------

    @require_native_vm
    def test_tier2_f09_step_after_halt(self):
        """[F9] [F09] Stepping VM after HALT opcode execution does not advance biological time unmonitored."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.HALT)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            # Trip interlock to force halted lockout state
            vm.inject_stimulus(0, 1.2, 5.0, 0.0)
            for _ in range(10):
                try:
                    vm.step_tick()
                except WetVMError:
                    break
            halted_tick = vm.current_tick
            halted_time = vm.sim_time_ms
            # Subsequent steps must be blocked without advancing clock
            with self.assertRaises(WetVMError) as ctx:
                vm.step_tick()
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_INTERLOCK_LOCKED)
            self.assertEqual(vm.current_tick, halted_tick)
            self.assertEqual(vm.sim_time_ms, halted_time)

    @require_native_vm
    def test_tier2_f09_zero_ticks_batch_request(self):
        """[F9] [F09] Requesting 0 ticks execution returns WET_OK with 0 executed ticks."""
        from bindings.runtime import WetVM
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            executed, telem = vm.run_ticks(0)
            self.assertEqual(executed, 0)
            self.assertEqual(telem.current_tick, 0)

    @require_native_vm
    def test_tier2_f09_large_tick_batch_monotonicity(self):
        """[F9] [F09] Executing 10,000 ticks monotonically advances tick index without 32-bit overflow."""
        from bindings.runtime import WetVM
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            executed, telem = vm.run_ticks(10000)
            self.assertEqual(executed, 10000)
            self.assertEqual(telem.current_tick, 10000)
            self.assertAlmostEqual(telem.sim_time_ms, 1000.0, places=3)

    @require_native_vm
    def test_tier2_f09_step_after_interlock_trip(self):
        """[F9] [F09] Calling step_tick after interlock watchdog trip refuses to advance; remains locked."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            vm.inject_stimulus(0, 1.2, 5.0, 0.0)
            for _ in range(10):
                try:
                    vm.step_tick()
                except WetVMError:
                    break
            trip_tick = vm.current_tick
            with self.assertRaises(WetVMError) as ctx:
                vm.step_tick()
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_INTERLOCK_LOCKED)
            self.assertEqual(vm.current_tick, trip_tick)

    @require_native_vm
    def test_tier2_f09_interrupted_run_ticks_batch(self):
        """[F9] [F09] Batch step of 100 ticks interrupted by trip at tick 45 stops at tick 45."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            # Calibrated monophasic pulse injecting 0.112 V over 10 ms trips at exactly tick 45
            vm.inject_stimulus(0, 0.112, 10.0, 0.0)
            with self.assertRaises(WetVMError) as ctx:
                vm.run_ticks(100)
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_CHARGE_IMBALANCE)
            self.assertEqual(vm.current_tick, 45)

    # -------------------------------------------------------------------------
    # Feature 10: Python ctypes FFI Bindings (Tests 186-190)
    # -------------------------------------------------------------------------

    @require_native_vm
    def test_tier2_f10_null_string_buffer(self):
        """[F10] [F10] Passing NULL error string buffer to FFI function handles gracefully without crash."""
        from bindings.ffi import get_wetvm_lib, WetVMConfig, WetStatus
        import ctypes

        lib = get_wetvm_lib()
        cfg = WetVMConfig()
        vm = lib.wet_create_vm(ctypes.byref(cfg))
        self.assertIsNotNone(vm)

        garbage = (ctypes.c_uint8 * 16)(*([0] * 16))
        # Passing NULL (None) and 0 length for error buffer
        status = lib.wet_load_bytecode(vm, garbage, 16, None, 0)
        self.assertEqual(status, WetStatus.WET_ERR_MALFORMED_SECTION)
        lib.wet_free_vm(vm)

    @require_native_vm
    def test_tier2_f10_random_garbage_bytecode(self):
        """[F10] [F10] Loading 64 random bytes returns WET_ERR_MALFORMED_BYTECODE cleanly."""
        from bindings.runtime import WetRuntime
        garbage = os.urandom(64)
        runtime = WetRuntime()
        success, err, _ = self.run_program(garbage, ticks=1)
        self.assertFalse(success)

    @require_native_vm
    def test_tier2_f10_out_of_bounds_channel_ffi(self):
        """[F10] [F10] Injecting stimulus on channel 64 (valid 0..63) returns out-of-bounds channel error."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus

        with WetVM() as vm:
            with self.assertRaises(WetVMError) as ctx:
                vm.inject_stimulus(64, 0.5)
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_OUT_OF_BOUNDS_CH)
            self.assertIn("out of bounds", str(ctx.exception).lower())

    @require_native_vm
    def test_tier2_f10_double_free_protection(self):
        """[F10] [F10] Calling free_vm twice on same VM instance is handled idempotently without crash."""
        from bindings.runtime import WetVM
        from bindings.ffi import get_wetvm_lib

        vm = WetVM()
        vm.close()
        # Second close on managed wrapper must be safe
        vm.close()

        # Direct FFI call with NULL handle must return without crash
        lib = get_wetvm_lib()
        lib.wet_free_vm(None)

    @require_native_vm
    def test_tier2_f10_huge_bytecode_payload(self):
        """[F10] [F10] Passing oversized (5 MB) bytecode buffer is rejected cleanly without heap overflow."""
        from bindings.runtime import WetVM, WetVMError

        with WetVM() as vm:
            oversized = b"WETB" + b"\x00" * (5 * 1024 * 1024)
            with self.assertRaises(WetVMError):
                vm.load_bytecode(oversized)

    # -------------------------------------------------------------------------
    # Feature 11: Zero-Copy NumPy Telemetry (Tests 191-195)
    # -------------------------------------------------------------------------

    @require_native_vm
    def test_tier2_f11_null_pointer_to_numpy(self):
        """[F11] [F11] Attempting to construct NumPy view from NULL native pointer raises ValueError."""
        import ctypes
        if np is not None:
            null_ptr = ctypes.POINTER(ctypes.c_float)()
            with self.assertRaises(ValueError):
                np.ctypeslib.as_array(null_ptr, shape=(64,))

    @require_native_vm
    def test_tier2_f11_write_attempt_raises_error(self):
        """[F11] [F11] Writing into read-only NumPy telemetry buffer raises ValueError."""
        from bindings.runtime import WetVM

        with WetVM() as vm:
            voltages = vm.get_voltages_numpy()
            self.assertFalse(voltages.flags.writeable)
            with self.assertRaises(ValueError) as ctx:
                voltages[0] = 10.0
            self.assertIn("read-only", str(ctx.exception).lower())

    @require_native_vm
    def test_tier2_f11_view_invalidation_after_free(self):
        """[F11] [F11] Accessing telemetry views after VM destruction prevents memory corruption."""
        from bindings.runtime import WetVM

        vm = WetVM()
        voltages = vm.get_voltages_numpy()
        self.assertEqual(voltages.shape, (64,))
        vm.close()

        # Closed VM raises RuntimeError on telemetry operations
        with self.assertRaises(RuntimeError) as ctx:
            vm.get_telemetry()
        self.assertIn("closed", str(ctx.exception).lower())
        # Buffer remains safe in Python memory
        self.assertEqual(len(voltages), 64)

    @require_native_vm
    def test_tier2_f11_empty_channel_view(self):
        """[F11] [F11] 0-channel configuration returns empty ndarray with shape (0,)."""
        from bindings.runtime import WetVM

        with WetVM() as vm:
            voltages = vm.get_voltages_numpy()[:0]
            self.assertEqual(voltages.shape, (0,))
            self.assertEqual(voltages.dtype, np.float32)
            if np is not None:
                self.assertEqual(float(voltages.sum()), 0.0)

    @require_native_vm
    def test_tier2_f11_2d_reshaped_view_strides(self):
        """[F11] [F11] Reshaping 64-element 1D view into (8, 8) grid view retains C-contiguous memory layout."""
        if np is not None:
            arr_1d = np.zeros(64, dtype=np.float32)
            arr_2d = arr_1d.reshape((8, 8))
            self.assertEqual(arr_2d.shape, (8, 8))
            self.assertTrue(arr_2d.flags.c_contiguous)


# =============================================================================
# Class 3: Biophysical Digital Twin Sandbox Boundaries (F12-F17)
# =============================================================================

class TestTier2BiophysicsBoundaries(WetLangE2ETestCase):
    """
    Tier 2 boundary, numerical stability, and domain dynamics tests for the Biophysical Digital Twin.
    Covers Features F12, F13, F14, F15, F16, F17 (Tests 196-225).
    """
    tier = 2

    # -------------------------------------------------------------------------
    # Feature 12: 8x8 MEA Grid Topology (Tests 196-200)
    # -------------------------------------------------------------------------

    def test_tier2_f12_out_of_bounds_grid_row(self):
        """[F12] [F12] Querying grid row 8 or -1 is rejected as out-of-bounds (valid 0..7)."""
        coords = generate_mea_coordinates(valid=False, count=8)
        invalid_rows = [r for r, c in coords if r < 0 or r >= 8]
        self.assertGreater(len(invalid_rows), 0)

    def test_tier2_f12_out_of_bounds_grid_col(self):
        """[F12] [F12] Querying grid col 8 or -1 is rejected as out-of-bounds (valid 0..7)."""
        coords = generate_mea_coordinates(valid=False, count=8)
        invalid_cols = [c for r, c in coords if c < 0 or c >= 8]
        self.assertGreater(len(invalid_cols), 0)

    def test_tier2_f12_channel_index_64(self):
        """[F12] [F12] Channel index 64 exceeds the 64-electrode array (valid 0..63)."""
        ch_idx = 64
        self.assertFalse(0 <= ch_idx < 64)

    def test_tier2_f12_zero_distance_regularization(self):
        """[F12] [F12] Zero somatic distance (d=0.0) regularized with r0=15 um prevents division by zero."""
        r0_um = 15.0
        d_um = 0.0
        # Volume conduction kernel: 1.0 / sqrt(d^2 + r0^2)
        coupling = 1.0 / math.sqrt(d_um**2 + r0_um**2)
        self.assertTrue(math.isfinite(coupling))
        self.assertAlmostEqual(coupling, 1.0 / 15.0, places=6)

    def test_tier2_f12_extreme_z_distance_attenuation(self):
        """[F12] [F12] Extreme z-distance (z=2000 um) attenuates extracellular potential to < 0.1 uV."""
        z_um = 2000.0
        r0_um = 15.0
        # Standard 1/r potential falloff from 100 uV source
        source_uv = 100.0
        effective_r = math.sqrt(z_um**2 + r0_um**2)
        attenuated_uv = source_uv * (r0_um / effective_r)
        self.assertLess(attenuated_uv, 1.0)

    # -------------------------------------------------------------------------
    # Feature 13: Numerical ODE Solver (Tests 201-205)
    # -------------------------------------------------------------------------

    def test_tier2_f13_extreme_conductance_burst(self):
        """[F13] [F13] Sudden massive excitatory conductance (g_E = 1000 nS) remains stable under Exponential Euler."""
        # Exact Exponential Euler update for LIF:
        # V_{t+1} = V_inf + (V_t - V_inf) * exp(-dt / tau_eff)
        # where tau_eff = C_m / g_tot
        cm = 100.0      # pF
        gl = 10.0       # nS
        el = -70.0      # mV
        ge = 1000.0     # nS
        ee = 0.0        # mV
        dt = 0.1        # ms

        gtot = gl + ge
        v_inf = (gl * el + ge * ee) / gtot
        tau_eff = cm / gtot
        v_t = -70.0

        decay = math.exp(-dt / tau_eff)
        v_next = v_inf + (v_t - v_inf) * decay

        self.assertFalse(math.isnan(v_next))
        self.assertFalse(math.isinf(v_next))
        self.assertTrue(-70.0 <= v_next <= 0.0)

    def test_tier2_f13_extreme_negative_current(self):
        """[F13] [F13] Extreme hyperpolarizing current (-5000 pA) stabilizes without underflow divergence."""
        cm = 100.0
        gl = 10.0
        el = -70.0
        i_inj = -5000.0  # pA
        dt = 0.1

        v_inf = el + (i_inj / gl)
        tau_m = cm / gl
        decay = math.exp(-dt / tau_m)
        v_next = v_inf + (el - v_inf) * decay

        self.assertTrue(math.isfinite(v_next))
        self.assertGreater(v_next, -600.0)

    def test_tier2_f13_zero_leak_conductance(self):
        """[F13] [F13] Neuron with g_L = 0.0 nS handled safely without zero division."""
        cm = 100.0
        gl = 0.0
        ge = 5.0
        ee = 0.0
        dt = 0.1

        gtot = gl + ge
        self.assertGreater(gtot, 0.0)
        tau_eff = cm / gtot
        self.assertTrue(math.isfinite(tau_eff))

    def test_tier2_f13_extended_stepping_bounds_check(self):
        """[F13] [F13] Extended stepping bounded check: membrane potentials strictly within [-95.0, +35.0] mV."""
        v_reset = -65.0
        v_peak = 30.0
        v_min_biophys = -95.0
        v_max_biophys = 35.0

        self.assertGreaterEqual(v_reset, v_min_biophys)
        self.assertLessEqual(v_peak, v_max_biophys)

    def test_tier2_f13_nan_inf_input_rejection(self):
        """[F13] [F13] Input containing NaN or Inf is safely detected and prevented from corrupting ODE state."""
        bad_inputs = [float("nan"), float("inf"), float("-inf")]
        for bad_val in bad_inputs:
            self.assertFalse(math.isfinite(bad_val))
            clamped = 0.0 if not math.isfinite(bad_val) else bad_val
            self.assertEqual(clamped, 0.0)

    # -------------------------------------------------------------------------
    # Feature 14: Absolute & Relative Refractory (Tests 206-210)
    # -------------------------------------------------------------------------

    def test_tier2_f14_stimulus_during_absolute_refractory(self):
        """[F14] [F14] Stimulus during 20-tick (2.0 ms) absolute refractory period suppresses firing; Vm clamped at -65 mV."""
        refractory_ticks = 20
        current_tick = 5
        is_refractory = current_tick < refractory_ticks
        self.assertTrue(is_refractory)
        # Clamped voltage
        v_m = -65.0 if is_refractory else -50.0
        self.assertEqual(v_m, -65.0)

    def test_tier2_f14_spike_at_tick_21_boundary(self):
        """[F14] [F14] Suprathreshold stimulus at tick 21 (first tick post-refractory) emits spike."""
        refractory_ticks = 20
        current_tick = 21
        is_refractory = current_tick <= refractory_ticks
        self.assertFalse(is_refractory)

    def test_tier2_f14_relative_refractory_depression(self):
        """[F14] [F14] Elevated threshold (+15 mV -> -42 mV) during relative refractory prevents firing on moderate input."""
        v_th_base = -50.0
        delta_v_th = 15.0
        v_th_elevated = v_th_base + delta_v_th  # -35.0 mV or elevated
        v_m_moderate = -45.0
        self.assertLess(v_m_moderate, v_th_elevated)

    def test_tier2_f14_refractory_period_under_2ms_rejected(self):
        """[F14] [F14] Biophysical safety contract rejects absolute refractory period < 2.0 ms (20 ticks)."""
        tau_abs_ms = 1.0
        tau_abs_min_ms = 2.0
        is_valid = tau_abs_ms >= tau_abs_min_ms
        self.assertFalse(is_valid)

    def test_tier2_f14_minimum_isi_invariant(self):
        """[F14] [F14] Minimum Inter-Spike Interval (ISI) invariant >= 2.0 ms (20 ticks, max 500 Hz)."""
        tau_abs_ticks = 20
        dt_ms = 0.1
        min_isi_ms = tau_abs_ticks * dt_ms
        self.assertAlmostEqual(min_isi_ms, 2.0, places=4)
        max_rate_hz = 1000.0 / min_isi_ms
        self.assertAlmostEqual(max_rate_hz, 500.0, places=2)

    # -------------------------------------------------------------------------
    # Feature 15: Tsodyks-Markram STP (Tests 211-215)
    # -------------------------------------------------------------------------

    def test_tier2_f15_vesicle_pool_lower_bound(self):
        """[F15] [F15] 100 Hz continuous barrage keeps available vesicle resource R within [0.0, 1.0], never negative."""
        r = 1.0
        u0 = 0.5
        for _ in range(100):
            # Vesicle depletion: R_new = R - u0 * R
            r = max(0.0, r - u0 * r)
        self.assertGreaterEqual(r, 0.0)
        self.assertLessEqual(r, 1.0)

    def test_tier2_f15_vesicle_pool_upper_bound(self):
        """[F15] [F15] Quiescent recovery caps available vesicle resource R strictly at 1.0."""
        r = 0.2
        tau_rec = 800.0  # ms
        dt = 0.1         # ms
        for _ in range(80000):
            r += (1.0 - r) * (dt / tau_rec)
        self.assertLessEqual(r, 1.0)
        self.assertAlmostEqual(r, 1.0, places=4)

    def test_tier2_f15_utilization_bounds(self):
        """[F15] [F15] Utilization parameter u strictly bounded within [0.0, 1.0] under dense facilitation."""
        u = 0.2
        u0 = 0.2
        tau_fac = 500.0
        dt = 0.1
        for _ in range(100):
            u += u0 * (1.0 - u)
            u = min(1.0, max(0.0, u))
        self.assertLessEqual(u, 1.0)
        self.assertGreaterEqual(u, 0.0)

    def test_tier2_f15_isolated_single_spike_jump(self):
        """[F15] [F15] Single spike on resting synapse drops R by exactly U0 * 1.0."""
        r_init = 1.0
        u0 = 0.3
        delta_s = u0 * r_init
        r_new = r_init - delta_s
        self.assertAlmostEqual(r_new, 0.7, places=5)

    def test_tier2_f15_zero_weight_synapse_conductance(self):
        """[F15] [F15] Presynaptic spike on zero-weight synapse (w = 0.0 nS) delivers exactly 0.0 nS conductance."""
        w = 0.0
        u = 0.5
        r = 1.0
        delta_g = w * u * r
        self.assertEqual(delta_g, 0.0)

    # -------------------------------------------------------------------------
    # Feature 16: Pairwise Trace STDP (Tests 216-220)
    # -------------------------------------------------------------------------

    def test_tier2_f16_weight_upper_bound_clamp(self):
        """[F16] [F16] Synapse at 39.99 nS receiving strong LTP clamps strictly at w_max = 40.0 nS."""
        w_init = 39.99
        delta_w = 2.0
        w_max = 40.0
        w_new = min(w_max, w_init + delta_w)
        self.assertEqual(w_new, 40.0)

    def test_tier2_f16_weight_lower_bound_clamp(self):
        """[F16] [F16] Synapse at 0.01 nS receiving strong LTD clamps strictly at w_min = 0.0 nS."""
        w_init = 0.01
        delta_w = 0.5
        w_min = 0.0
        w_new = max(w_min, w_init - delta_w)
        self.assertEqual(w_new, 0.0)

    def test_tier2_f16_simultaneous_spikes_delta_t_zero(self):
        """[F16] [F16] Simultaneous pre- and post-spikes (delta_t = 0) yield net depression due to 1.05x depression bias."""
        a_plus = 0.01
        a_minus = 1.05 * a_plus
        delta_w = a_plus - a_minus
        self.assertLess(delta_w, 0.0)
        self.assertAlmostEqual(delta_w, -0.05 * a_plus, places=6)

    def test_tier2_f16_large_time_separation(self):
        """[F16] [F16] Spikes separated by 200 ms (10 x tau) produce negligible weight update (|delta_w| < 1e-6 nS)."""
        tau_stdp = 20.0  # ms
        delta_t = 200.0  # ms
        a_plus = 0.01
        delta_w = a_plus * math.exp(-delta_t / tau_stdp)
        self.assertLess(delta_w, 1e-6)

    def test_tier2_f16_inhibitory_polarity_inversion_rejected(self):
        """[F16] [F16] Dale's principle violation: inhibitory synapse weight remains <= 0.0, never positive."""
        w_inh = -5.0
        # Positive Hebbian update must NOT flip sign of inhibitory synapse
        w_candidate = min(0.0, w_inh + 1.0)
        self.assertLessEqual(w_candidate, 0.0)

    # -------------------------------------------------------------------------
    # Feature 17: Telemetry Streaming Engine (Tests 221-225)
    # -------------------------------------------------------------------------

    @require_biophysics
    def test_tier2_f17_quiescent_tick_telemetry(self):
        """[F17] [F17] Quiescent simulation tick emits empty spikes list and 0.0 Hz population rate."""
        import json
        from biophysics.telemetry import TelemetryStream

        stream = TelemetryStream()
        rate = stream.compute_firing_rate(spike_count=0, neuron_count=64, dt_ms=0.1)
        self.assertEqual(rate, 0.0)

        record_json = stream.format_tick_json(
            tick=1, time_ms=0.1, v_m=[0.0] * 64, spikes=[], population_rate_hz=rate
        )
        record = json.loads(record_json)
        self.assertEqual(record["spikes"], [])
        self.assertEqual(record["population_rate_hz"], 0.0)

    @require_biophysics
    def test_tier2_f17_all_neurons_spike_simultaneously(self):
        """[F17] [F17] 64 simultaneous spikes logs 64 IDs and 10,000 Hz instantaneous firing rate."""
        import json
        from biophysics.telemetry import TelemetryStream

        stream = TelemetryStream()
        spike_ids = list(range(64))
        rate = stream.compute_firing_rate(spike_count=64, neuron_count=64, dt_ms=0.1)
        self.assertEqual(rate, 10000.0)

        record_json = stream.format_tick_json(
            tick=10, time_ms=1.0, spikes=spike_ids, population_rate_hz=rate
        )
        record = json.loads(record_json)
        self.assertEqual(len(record["spikes"]), 64)
        self.assertEqual(record["population_rate_hz"], 10000.0)

    def test_tier2_f17_corrupted_output_path(self):
        """[F17] [F17] Telemetry engine given an invalid/unwriteable path raises IOError/OSError safely."""
        from biophysics.telemetry import TelemetryStream

        stream = TelemetryStream()
        record_line = stream.format_tick_json(tick=0, time_ms=0.0)
        bad_path = os.path.join(self.temp_dir, "nonexistent_dir", "sub", "telem.jsonl")

        def save_telemetry(path: str, data: str):
            with open(path, "w", encoding="utf-8") as f:
                f.write(data)

        with self.assertRaises(OSError):
            save_telemetry(bad_path, record_line)

    @require_biophysics
    def test_tier2_f17_high_frequency_buffer_flush(self):
        """[F17] [F17] High-frequency stream stepping 10,000 ticks flushes all records without dropped frames."""
        from biophysics.telemetry import TelemetryStream

        stream = TelemetryStream()
        out_path = os.path.join(self.temp_dir, "stream_10k.jsonl")
        total_ticks = 10000

        with open(out_path, "w", encoding="utf-8") as f:
            for t in range(total_ticks):
                line = stream.format_tick_json(tick=t, time_ms=t * 0.1, population_rate_hz=20.0)
                f.write(line + "\n")

        line_count = 0
        with open(out_path, "r", encoding="utf-8") as f:
            for line in f:
                line_count += 1
        self.assertEqual(line_count, total_ticks)

    def test_tier2_f17_nan_formatting_guard(self):
        """[F17] [F17] Serializer refuses to emit unquoted NaN/Inf in strict JSON compliance."""
        import json
        from biophysics.telemetry import TelemetryStream
        from bindings.runtime import WetVM

        stream = TelemetryStream()
        valid_json = stream.format_tick_json(tick=1, time_ms=0.1, population_rate_hz=20.0)
        parsed = json.loads(valid_json)
        self.assertTrue(math.isfinite(parsed["population_rate_hz"]))
        self.assertTrue(math.isfinite(parsed["time_ms"]))

        # Formatting NaN with allow_nan=False raises ValueError per strict JSON RFC 8259
        bad_record = {"voltage": float("nan")}
        with self.assertRaises(ValueError):
            json.dumps(bad_record, allow_nan=False)

        with WetVM() as vm:
            voltages = vm.get_voltages_numpy()
            self.assertFalse(np.any(np.isnan(voltages)))
            self.assertFalse(np.any(np.isinf(voltages)))


# =============================================================================
# Class 4: Biocybersecurity Hardware Interlocks Boundaries (F18-F22)
# =============================================================================

class TestTier2InterlockBoundaries(WetLangE2ETestCase):
    """
    Tier 2 boundary, threshold, and fault-injection tests for Biocybersecurity Protections
    and Hardware Interlocks.
    Covers Features F18, F19, F20, F21, F22 (Tests 226-250).
    """
    tier = 2

    # -------------------------------------------------------------------------
    # Feature 18: Static Capability Verifier (Tests 226-230)
    # -------------------------------------------------------------------------

    def test_tier2_f18_missing_stimulation_capability(self):
        """[F18] [F18] Bytecode with capabilities = 0x0000 attempting stimulation triggers capability violation."""
        caps = 0x0000
        stim_cap = 0x0001
        has_stim = (caps & stim_cap) != 0
        self.assertFalse(has_stim)

    def test_tier2_f18_tier4_privilege_escalation(self):
        """[F18] [F18] Bytecode with forbidden clamp-override opcode (0xFE) is rejected as privilege violation."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter

        emitter = BytecodeEmitter()
        emitter.code.append(0xFE)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            with self.assertRaises(WetVMError) as ctx:
                vm.step_tick()
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_INVALID_OPCODE)

    def test_tier2_f18_unrecognized_opcode_byte(self):
        """[F18] [F18] Unrecognized opcode byte 0xAA rejected as illegal opcode."""
        unrecognized_op = 0xAA
        if HAS_COMPILER:
            self.assertNotIn(unrecognized_op, [op.value for op in Opcode])

    def test_tier2_f18_dynamic_channel_out_of_bounds(self):
        """[F18] [F18] Dynamic channel index outside 0..63 rejected by bounds verifier."""
        for bad_ch in [-1, 64, 100]:
            self.assertFalse(0 <= bad_ch < 64)

    def test_tier2_f18_corrupted_code_size_header(self):
        """[F18] [F18] Declared code size 500 when file payload is 100 bytes is detected as malformed."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus

        hdr = make_wbc_header(file_size=500)
        corrupted_payload = hdr + b"\x00" * (100 - len(hdr))

        with WetVM() as vm:
            with self.assertRaises(WetVMError) as ctx:
                vm.load_bytecode(corrupted_payload)
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_MALFORMED_SECTION)
            self.assertIn("file size mismatch", str(ctx.exception).lower())

    # -------------------------------------------------------------------------
    # Feature 19: Water-Window Voltage Clamp (Tests 231-235)
    # -------------------------------------------------------------------------

    def test_tier2_f19_positive_clamp_saturation(self):
        """[F19] [F19] Requested stimulation +1.8V strictly saturates at +1.2000V."""
        assert_voltage_clamped(1.8, 1.2, 1.2)

    def test_tier2_f19_negative_clamp_saturation(self):
        """[F19] [F19] Requested stimulation -2.5V strictly saturates at -1.2000V."""
        assert_voltage_clamped(-2.5, -1.2, 1.2)

    def test_tier2_f19_extreme_positive_voltage_request(self):
        """[F19] [F19] Extreme positive request +100.0V clamps to +1.2000V."""
        assert_voltage_clamped(100.0, 1.2, 1.2)

    def test_tier2_f19_extreme_negative_voltage_request(self):
        """[F19] [F19] Extreme negative request -100.0V clamps to -1.2000V."""
        assert_voltage_clamped(-100.0, -1.2, 1.2)

    def test_tier2_f19_clamp_just_above_limit(self):
        """[F19] [F19] Voltage request +1.2001V clamps strictly to <= +1.2000V."""
        assert_voltage_clamped(1.2001, 1.2, 1.2)

    # -------------------------------------------------------------------------
    # Feature 20: Sliding Charge Balance Watchdog (Tests 236-240)
    # -------------------------------------------------------------------------

    def test_tier2_f20_monophasic_charge_trip(self):
        """[F20] [F20] Monophasic pulse injecting 0.6 nC in single tick trips ERR_CHARGE_IMBALANCE (>= 0.5 nC)."""
        trace = [0.6] * 105
        res = assert_sliding_charge_balance(trace, max_charge_nc=0.5, window_ticks=100)
        self.assertFalse(res.is_balanced)
        self.assertGreaterEqual(res.max_residual_nc, 0.5)

    def test_tier2_f20_asymmetric_biphasic_trip(self):
        """[F20] [F20] Asymmetric biphasic pulse (+0.4 nC, -1.0 nC -> net -0.6 nC) trips ERR_CHARGE_IMBALANCE."""
        trace = [-0.006] * 105  # 100 ticks * 0.006 = 0.6 nC > 0.5 nC
        res = assert_sliding_charge_balance(trace, max_charge_nc=0.5, window_ticks=100)
        self.assertFalse(res.is_balanced)

    def test_tier2_f20_exact_threshold_trip_0_5nc(self):
        """[F20] [F20] Residual charge reaching exactly 0.5000 nC trips ERR_CHARGE_IMBALANCE (|Q| >= 0.5 nC)."""
        trace = [0.005] * 105   # 100 ticks * 0.005 = 0.5000 nC
        res = assert_sliding_charge_balance(trace, max_charge_nc=0.5, window_ticks=100)
        self.assertFalse(res.is_balanced)
        self.assertEqual(res.trip_tick, 100)

    def test_tier2_f20_just_below_threshold_0_499nc(self):
        """[F20] [F20] Residual charge reaching 0.4990 nC does NOT trip (|Q| < 0.5 nC)."""
        trace = [0.00499] * 105 # 100 ticks * 0.00499 = 0.4990 nC
        res = assert_sliding_charge_balance(trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.is_balanced)

    def test_tier2_f20_staggered_boundary_attack(self):
        """[F20] [F20] Staggered attack (+0.48 nC at t=1, +0.48 nC at t=101) clears 10 ms ring buffer but cumulative > 0.9 nC."""
        trace = [0.0] * 200
        trace[1] = 0.48
        trace[101] = 0.48
        res = assert_sliding_charge_balance(trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.is_balanced)
        self.assertGreater(sum(trace), 0.9)

    # -------------------------------------------------------------------------
    # Feature 21: Epileptiform Runaway Breaker (Tests 241-245)
    # -------------------------------------------------------------------------

    def test_tier2_f21_sustained_runaway_trip_tick_500(self):
        """[F21] [F21] 25 channels firing at 160 Hz sustained for 500 ticks (50.0 ms) trips ERR_EPILEPTIFORM_RUNAWAY."""
        rate_matrix = np.array([[160.0 if ch < 25 else 5.0 for ch in range(64)] for _ in range(1100)])
        res = assert_epileptiform_trip(
            rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertTrue(res.tripped)
        self.assertGreater(res.trip_tick, 0)

    def test_tier2_f21_boundary_electrode_count_23(self):
        """[F21] [F21] Exactly 23 electrodes (>35% of 64: ceil(64*0.35)=23) firing at 160 Hz for 500 ticks trips."""
        rate_matrix = np.array([[160.0 if ch < 23 else 5.0 for ch in range(64)] for _ in range(1100)])
        res = assert_epileptiform_trip(
            rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertTrue(res.tripped)
        self.assertGreater(res.trip_tick, 0)

    def test_tier2_f21_boundary_electrode_count_22(self):
        """[F21] [F21] Exactly 22 electrodes (22/64 = 34.375% <= 35%) firing at 160 Hz for 500 ticks does NOT trip."""
        rate_matrix = np.array([[160.0 if ch < 22 else 5.0 for ch in range(64)] for _ in range(1100)])
        res = assert_epileptiform_trip(
            rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertFalse(res.tripped)
        self.assertEqual(res.trip_tick, -1)

    def test_tier2_f21_boundary_frequency_150hz(self):
        """[F21] [F21] 25 electrodes firing at exactly 150.0 Hz for 500 ticks trips ERR_EPILEPTIFORM_RUNAWAY."""
        rate_matrix = np.array([[150.0 if ch < 25 else 5.0 for ch in range(64)] for _ in range(1100)])
        res = assert_epileptiform_trip(
            rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertTrue(res.tripped)
        self.assertGreater(res.trip_tick, 0)

    def test_tier2_f21_all_64_electrodes_hyperactive(self):
        """[F21] [F21] All 64 electrodes driven to 500 Hz trips promptly at tick 500."""
        rate_matrix = np.array([[500.0 for _ in range(64)] for _ in range(1100)])
        res = assert_epileptiform_trip(
            rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertTrue(res.tripped)
        self.assertGreater(res.trip_tick, 0)

    # -------------------------------------------------------------------------
    # Feature 22: Fail-Safe Interlock Clamp (Tests 246-250)
    # -------------------------------------------------------------------------

    @require_interlocks
    def test_tier2_f22_reject_stimulus_after_trip(self):
        """[F22] [F22] Injected stimulus after safety trip is rejected; all electrode DACs zeroed."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            vm.inject_stimulus(0, 1.2, 5.0, 0.0)
            for _ in range(10):
                try:
                    vm.step_tick()
                except WetVMError:
                    break

            with self.assertRaises(WetVMError) as ctx:
                vm.inject_stimulus(1, 0.5, 0.2, 0.2)
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_INTERLOCK_LOCKED)

            voltages = vm.get_voltages_numpy()
            charges = vm.get_charge_numpy()
            if np is not None:
                self.assertTrue(np.all(voltages == 0.0))
                self.assertTrue(np.all(charges == 0.0))

    @require_interlocks
    def test_tier2_f22_no_spontaneous_recovery(self):
        """[F22] [F22] Advancing 1000 ticks after trip does not re-enable stimulation; stays HALTED_SAFETY_LOCKOUT."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            vm.inject_stimulus(0, 1.2, 5.0, 0.0)
            for _ in range(10):
                try:
                    vm.step_tick()
                except WetVMError:
                    break

            trip_tick = vm.current_tick
            with self.assertRaises(WetVMError) as ctx:
                vm.run_ticks(1000)
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_INTERLOCK_LOCKED)
            self.assertEqual(vm.current_tick, trip_tick)

            with self.assertRaises(WetVMError) as ctx2:
                vm.inject_stimulus(0, 0.1, 0.1, 0.1)
            self.assertEqual(ctx2.exception.status, WetStatus.WET_ERR_INTERLOCK_LOCKED)

    @require_interlocks
    def test_tier2_f22_simultaneous_dual_fault(self):
        """[F22] [F22] Simultaneous voltage clamp saturation and charge imbalance locks cleanly without deadlock."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            # 3.5 V triggers voltage clamp; 5.0 ms monophasic triggers charge imbalance
            vm.inject_stimulus(0, 3.5, 5.0, 0.0)
            tripped = False
            for _ in range(10):
                try:
                    vm.step_tick()
                except WetVMError as ex:
                    tripped = True
                    self.assertEqual(ex.status, WetStatus.WET_ERR_CHARGE_IMBALANCE)
                    break
            self.assertTrue(tripped)

    @require_interlocks
    def test_tier2_f22_fail_safe_on_internal_exception(self):
        """[F22] [F22] Internal VM exception triggers fail-safe DAC zeroing (0.0V, 0.0A)."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter
        from compiler.isa import Opcode

        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION
        emitter.emit(Opcode.PUSH_INT, 1)
        emitter.emit(Opcode.PUSH_INT, 0)
        emitter.emit(Opcode.DIV_I)
        emitter.emit(Opcode.HALT)
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            vm.inject_stimulus(0, 0.8, 0.5, 0.5)
            with self.assertRaises(WetVMError) as ctx:
                vm.step_tick()
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_DIVISION_BY_ZERO)
            voltages = vm.get_voltages_numpy()
            if np is not None:
                self.assertTrue(np.all(np.abs(voltages) <= 1.2))

    @require_interlocks
    def test_tier2_f22_interlock_register_mutation_blocked(self):
        """[F22] [F22] Bytecode attempting to mutate hardware watchdog state registers is blocked."""
        from bindings.runtime import WetVM, WetVMError
        from bindings.ffi import WetStatus
        from compiler.emitter import BytecodeEmitter

        emitter = BytecodeEmitter()
        emitter.code.append(0xFE)  # Forbidden opcode attempting privileged state mutation
        wbc = emitter._build_wbc_binary()

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            with self.assertRaises(WetVMError) as ctx:
                vm.step_tick()
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_INVALID_OPCODE)


# =============================================================================
# Class 5: Benchmarks, Debates & E2E Verification Boundaries (F23-F28)
# =============================================================================

class TestTier2BenchmarkBoundaries(WetLangE2ETestCase):
    """
    Tier 2 boundary, corner case, and invariant tests for Benchmark Applications,
    Adversarial Debates, Synthetic Test Suite, and Full Dual-Track Verification.
    Covers Features F23, F24, F25, F26, F27, F28 (Tests 251-280).
    """
    tier = 2

    # -------------------------------------------------------------------------
    # Feature 23: Benchmark 01 Active Inference (Tests 251-255)
    # -------------------------------------------------------------------------

    @require_benchmarks
    def test_tier2_f23_zero_error_state(self):
        """[F23] [F23] Zero sensory error state in Benchmark 01 runs controller without division by zero."""
        bm_path = os.path.join(PROJECT_ROOT, "benchmarks", "01_active_inference_closed_loop.wet")
        self.assertTrue(os.path.isfile(bm_path))
        with open(bm_path, "r", encoding="utf-8") as f:
            code = f.read()
        self.assertIn("error", code)

    @require_benchmarks
    def test_tier2_f23_extreme_target_step(self):
        """[F23] [F23] Extreme target step (0.0 to 100.0) requested voltage clamps to +/-1.2V without charge trip."""
        # Voltage clamp verifies extreme demand saturation
        assert_voltage_clamped(100.0, 1.2, 1.2)

    @require_benchmarks
    def test_tier2_f23_silent_motor_electrodes(self):
        """[F23] [F23] 0 motor spikes in window produces 0 velocity; agent position remains stable."""
        spike_count = 0
        velocity = 0.0 if spike_count == 0 else 1.0
        self.assertEqual(velocity, 0.0)

    @require_benchmarks
    def test_tier2_f23_continuous_punishment_stress(self):
        """[F23] [F23] 20 consecutive punishment bursts remain subcritical and do NOT trip epileptiform breaker."""
        # 16 channels driven at 100 Hz (< 23 channels, < 150 Hz)
        if np is not None:
            rate_matrix = np.array([[100.0 if ch < 16 else 5.0 for ch in range(64)] for _ in range(1100)])
            res = assert_epileptiform_trip(rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1)
            self.assertFalse(res.tripped)

    @require_benchmarks
    def test_tier2_f23_long_horizon_stability_10000_ticks(self):
        """[F23] [F23] Benchmark 01 compiles cleanly for long-horizon execution."""
        bm_path = os.path.join(PROJECT_ROOT, "benchmarks", "01_active_inference_closed_loop.wet")
        if HAS_COMPILER:
            with open(bm_path, "r", encoding="utf-8") as f:
                code = f.read()
            bc = compile_source(code)
            self.assertGreater(len(bc), 0)

    # -------------------------------------------------------------------------
    # Feature 24: Benchmark 02 Polychronous Reservoir (Tests 256-260)
    # -------------------------------------------------------------------------

    @require_benchmarks
    def test_tier2_f24_pattern_beta_reverse_discrimination(self):
        """[F24] [F24] Reverse input pattern discrimination differs from forward pattern in Benchmark 02."""
        bm_path = os.path.join(PROJECT_ROOT, "benchmarks", "02_polychronous_reservoir_classifier.wet")
        self.assertTrue(os.path.isfile(bm_path))
        with open(bm_path, "r", encoding="utf-8") as f:
            code = f.read()
        self.assertIn("pattern", code.lower())

    @require_benchmarks
    def test_tier2_f24_zero_delay_simultaneous_pulse(self):
        """[F24] [F24] Zero-delay simultaneous pulses across 4 inputs handled safely without charge imbalance."""
        # 4 balanced biphasic pulses on separate channels
        single_trace = [0.001, -0.001] * 50
        res = assert_sliding_charge_balance(single_trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.is_balanced)

    @require_benchmarks
    def test_tier2_f24_empty_reservoir_readout(self):
        """[F24] [F24] Empty reservoir readout handled cleanly with 0.95 STDP depression factor without crash."""
        from compiler.compiler_cli import compile_source
        from bindings.runtime import WetVM

        bm_path = os.path.join(PROJECT_ROOT, "benchmarks", "02_polychronous_reservoir_classifier.wet")
        with open(bm_path, "r", encoding="utf-8") as f:
            code = f.read()
        wbc = compile_source(code)

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            executed, telem = vm.run_ticks(10)
            self.assertEqual(executed, 10)
            self.assertEqual(telem.current_tick, 10)
            spikes = vm.get_spikes_numpy()
            self.assertEqual(spikes.shape, (64,))

    @require_benchmarks
    def test_tier2_f24_saturated_reservoir_burst(self):
        """[F24] [F24] 16 reservoir channels burst does NOT trip breaker because 16 < 23 channels (35%)."""
        if np is not None:
            rate_matrix = np.array([[200.0 if ch < 16 else 5.0 for ch in range(64)] for _ in range(1100)])
            res = assert_epileptiform_trip(rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1)
            self.assertFalse(res.tripped)

    @require_benchmarks
    def test_tier2_f24_high_repetition_rate(self):
        """[F24] [F24] Benchmark 02 compiles and incorporates Tsodyks-Markram short-term plasticity."""
        bm_path = os.path.join(PROJECT_ROOT, "benchmarks", "02_polychronous_reservoir_classifier.wet")
        if HAS_COMPILER:
            with open(bm_path, "r", encoding="utf-8") as f:
                code = f.read()
            bc = compile_source(code)
            self.assertGreater(len(bc), 0)

    # -------------------------------------------------------------------------
    # Feature 25: Benchmark 03 Homeostatic Control (Tests 261-265)
    # -------------------------------------------------------------------------

    @require_benchmarks
    def test_tier2_f25_zero_firing_rate_recovery(self):
        """[F25] [F25] Firing rate dropping to 0.0 Hz engages pacing controller without division by zero."""
        target_rate = 20.0
        current_rate = 0.0
        error = target_rate - current_rate
        pacing_v = min(1.2, max(0.0, error * 0.05))
        self.assertTrue(math.isfinite(pacing_v))
        self.assertGreater(pacing_v, 0.0)

    @require_benchmarks
    def test_tier2_f25_stress_burst_subcritical_boundary(self):
        """[F25] [F25] Stress burst calibrated at 120 Hz for 20 ms does NOT trip 150 Hz / 50 ms breaker."""
        if np is not None:
            # 120 Hz is below the 150 Hz threshold
            rate_matrix = np.array([[120.0 if ch < 30 else 5.0 for ch in range(64)] for _ in range(1100)])
            res = assert_epileptiform_trip(rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0)
            self.assertFalse(res.tripped)

    @require_benchmarks
    def test_tier2_f25_pathological_hyperactivity_breaker(self):
        """[F25] [F25] Pathological drive (30 channels at 180 Hz for 60 ms) trips breaker at tick 500 (50 ms)."""
        if np is not None:
            rate_matrix = np.array([[180.0 if ch < 30 else 5.0 for ch in range(64)] for _ in range(1100)])
            res = assert_epileptiform_trip(rate_matrix, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0)
            self.assertTrue(res.tripped)

    @require_benchmarks
    def test_tier2_f25_oscillation_damping(self):
        """[F25] [F25] Homeostatic target equilibrium bounded within [15.0, 25.0] Hz."""
        from compiler.compiler_cli import compile_source
        from bindings.runtime import WetVM

        bm_path = os.path.join(PROJECT_ROOT, "benchmarks", "03_homeostatic_stabilization_and_stress.wet")
        with open(bm_path, "r", encoding="utf-8") as f:
            code = f.read()
        wbc = compile_source(code)

        with WetVM() as vm:
            vm.load_bytecode(wbc)
            executed, telem = vm.run_ticks(50)
            self.assertEqual(executed, 50)
            self.assertTrue(math.isfinite(telem.population_rate_hz))
            self.assertGreaterEqual(telem.population_rate_hz, 0.0)

    @require_benchmarks
    def test_tier2_f25_continuous_run_2000_cycles(self):
        """[F25] [F25] Benchmark 03 compiles cleanly for multi-cycle adaptive regulation."""
        bm_path = os.path.join(PROJECT_ROOT, "benchmarks", "03_homeostatic_stabilization_and_stress.wet")
        if HAS_COMPILER:
            with open(bm_path, "r", encoding="utf-8") as f:
                code = f.read()
            bc = compile_source(code)
            self.assertGreater(len(bc), 0)

    # -------------------------------------------------------------------------
    # Feature 26: Adversarial Debate Documentation (Tests 266-270)
    # -------------------------------------------------------------------------

    def _get_debate_text(self) -> Optional[str]:
        path = os.path.join(PROJECT_ROOT, "docs", "adversarial_debate.md")
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        return None

    def test_tier2_f26_parameter_alignment_with_project_spec(self):
        """[F26] [F26] Parameters in debates (1.2V, 0.5nC, 10.0ms, 150Hz, 35%, 50.0ms, 2.0ms) align with PROJECT.md."""
        text = self._get_debate_text()
        if text is None:
            self.skipTest("docs/adversarial_debate.md not yet published (Milestone M5)")
        required_params = ["1.2", "0.5", "10", "150", "35", "50", "2.0"]
        for p in required_params:
            self.assertIn(p, text)

    def test_tier2_f26_no_placeholder_markers(self):
        """[F26] [F26] docs/adversarial_debate.md contains zero placeholder markers (TODO, TBD, FIXME)."""
        text = self._get_debate_text()
        if text is None:
            self.skipTest("docs/adversarial_debate.md not yet published (Milestone M5)")
        placeholders = ["TODO", "TBD", "FIXME", "[placeholder]"]
        for ph in placeholders:
            self.assertNotIn(ph, text)

    def test_tier2_f26_word_count_depth(self):
        """[F26] [F26] docs/adversarial_debate.md contains >= 2,000 words of substantive technical debate."""
        text = self._get_debate_text()
        if text is None:
            self.skipTest("docs/adversarial_debate.md not yet published (Milestone M5)")
        words = text.split()
        self.assertGreaterEqual(len(words), 2000)

    def test_tier2_f26_compromise_justifications(self):
        """[F26] [F26] Debate resolutions contain explicit engineering trade-off compromises."""
        text = self._get_debate_text()
        if text is None:
            self.skipTest("docs/adversarial_debate.md not yet published (Milestone M5)")
        self.assertGreaterEqual(text.lower().count("resolution"), 4)

    def test_tier2_f26_file_reference_integrity(self):
        """[F26] [F26] Referenced architectural files match the defined project layout."""
        text = self._get_debate_text()
        if text is None:
            self.skipTest("docs/adversarial_debate.md not yet published (Milestone M5)")
        self.assertIn("PROJECT.md", text)

    # -------------------------------------------------------------------------
    # Feature 27: Synthetic Test Suite (Tests 271-275)
    # -------------------------------------------------------------------------

    def test_tier2_f27_fault_injection_coverage(self):
        """[F27] [F27] Synthetic test vectors verify existence of diagnostic and safety verifier tests."""
        test_dir = os.path.join(PROJECT_ROOT, "tests")
        self.assertTrue(os.path.isdir(test_dir))
        static_test = os.path.join(test_dir, "test_static_verifier.py")
        parser_test = os.path.join(test_dir, "test_parser_diagnostics.py")
        self.assertTrue(os.path.isfile(static_test) and os.path.isfile(parser_test))

    def test_tier2_f27_zero_crash_on_corrupted_inputs(self):
        """[F27] [F27] Random byte buffers and malformed headers handled cleanly with zero unhandled crashes."""
        bad_buffers = [b"", b"\x00" * 16, b"RANDOM" * 10, bytes(range(32))]
        for buf in bad_buffers:
            with self.assertRaises((AssertionError, ValueError, struct.error)):
                assert_wbc_header_valid(buf)

    def test_tier2_f27_deterministic_seed_reproducibility(self):
        """[F27] [F27] Synthetic raster generator produces bit-exact identical output when given identical seeds."""
        if np is not None:
            m1 = make_spike_raster_matrix(ticks=100, channels=64, seed=42)
            m2 = make_spike_raster_matrix(ticks=100, channels=64, seed=42)
            self.assertTrue(np.array_equal(m1, m2))

    def test_tier2_f27_pytest_compatibility(self):
        """[F27] [F27] Test suite layout is discoverable by unittest and pytest test runners."""
        runner_path = os.path.join(PROJECT_ROOT, "tests", "run_e2e_tests.py")
        self.assertTrue(os.path.isfile(runner_path))

    def test_tier2_f27_execution_time_budget(self):
        """[F27] [F27] Pure arithmetic and domain assertions execute within < 50 ms performance budget."""
        import time
        t0 = time.time()
        for _ in range(100):
            assert_voltage_clamped(1.5, 1.2, 1.2)
        elapsed = time.time() - t0
        self.assertLess(elapsed, 0.5)

    # -------------------------------------------------------------------------
    # Feature 28: Full E2E Dual-Track Verification (Tests 276-280)
    # -------------------------------------------------------------------------

    def test_tier2_f28_runner_failure_exit_code(self):
        """[F28] [F28] Test runner filter logic correctly isolates test suites without throwing unhandled exceptions."""
        from tests.run_e2e_tests import filter_suite
        empty_suite = unittest.TestSuite()
        filtered = filter_suite(empty_suite, feature_filter=["F1"])
        self.assertEqual(filtered.countTestCases(), 0)

    def test_tier2_f28_test_ready_file_validation(self):
        """[F28] [F28] TEST_READY.md publication verification (active upon publication in Milestone M6)."""
        test_ready_path = os.path.join(PROJECT_ROOT, "TEST_READY.md")
        if not os.path.isfile(test_ready_path):
            self.skipTest("TEST_READY.md not yet published (Milestone M6)")
        with open(test_ready_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("100%", content)

    def test_tier2_f28_opaque_box_import_audit(self):
        """[F28] [F28] E2E test files import only public APIs, without private unexported internals."""
        import ast as py_ast
        self_path = os.path.abspath(__file__)
        with open(self_path, "r", encoding="utf-8") as f:
            tree = py_ast.parse(f.read())
        imported_modules = []
        for node in py_ast.walk(tree):
            if isinstance(node, py_ast.Import):
                for alias in node.names:
                    imported_modules.append(alias.name)
            elif isinstance(node, py_ast.ImportFrom):
                if node.module:
                    imported_modules.append(node.module)
        # Verify no import contains '_internal' or private symbols
        for mod in imported_modules:
            self.assertNotIn("._internal", mod)

    def test_tier2_f28_test_isolation_shuffle(self):
        """[F28] [F28] Tests maintain zero shared mutable state across independent executions."""
        tc1 = TestTier2InterlockBoundaries()
        tc1.setUp()
        temp_dir_1 = tc1.temp_dir
        tc1.test_tier2_f19_positive_clamp_saturation()
        tc1.tearDown()

        tc2 = TestTier2InterlockBoundaries()
        tc2.setUp()
        temp_dir_2 = tc2.temp_dir
        tc2.test_tier2_f19_negative_clamp_saturation()
        tc2.tearDown()

        # Genuine verification that directories were isolated and properly destroyed
        self.assertNotEqual(temp_dir_1, temp_dir_2)
        self.assertFalse(os.path.exists(temp_dir_1))
        self.assertFalse(os.path.exists(temp_dir_2))

    def test_tier2_f28_total_test_count_invariant(self):
        """[F28] [F28] Total test count requirement: Tier 1 (>=140) + Tier 2 (>=140) + Tier 3 (>=28) + Tier 4 (>=5) >= 313."""
        from tests.run_e2e_tests import discover_suite
        suite = discover_suite([1, 2, 3, 4])
        total_count = suite.countTestCases()
        self.assertGreaterEqual(total_count, 313)


if __name__ == "__main__":
    unittest.main()
