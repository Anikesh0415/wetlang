"""
WetLang Test Suite: Parser Diagnostics & Compiler Pipeline
Tests lexer tokenization, physical units, Pratt precedence, AST construction,
diagnostics, and disassembler round-trip.
"""

import pytest
import struct
import zlib
from compiler.token import (
    Token,
    TokenType,
    Dimension,
    UNIT_SUFFIXES,
)
from compiler.lexer import (
    Lexer,
    LexerError,
)
from compiler.parser import (
    Parser,
    ParseError,
)
from compiler.ast_nodes import (
    ProgramNode,
    GridDeclNode,
    ChannelDeclNode,
    FnDeclNode,
    StreamDeclNode,
    LetStmtNode,
    AssignStmtNode,
    StimStmtNode,
    ModulateStmtNode,
    SyncTickStmtNode,
    IfStmtNode,
    WhileStmtNode,
    ForStmtNode,
    ReturnStmtNode,
    ExprStmtNode,
    BinaryOpNode,
    UnaryOpNode,
    LiteralNode,
    PhysicalLiteralNode,
    IdentifierNode,
    CallNode,
    IndexNode,
    DomainCallNode,
)
from compiler.isa import (
    HEADER_MAGIC,
    HEADER_SIZE,
    VERSION_MAJOR,
    VERSION_MINOR,
    HEADER_STRUCT_FORMAT,
    Capability,
    SectionType,
    Opcode,
)
from compiler.emitter import (
    BytecodeEmitter,
    disassemble,
)
from compiler.compiler_cli import compile_source


# =========================================================================
# Lexer Tests
# =========================================================================

def test_lexer_keywords_and_identifiers():
    source = "grid channel fn stream bind cycle let mut if else while for in return stim_biphasic sync_tick"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    expected_types = [
        TokenType.GRID,
        TokenType.CHANNEL,
        TokenType.FN,
        TokenType.STREAM,
        TokenType.BIND,
        TokenType.CYCLE,
        TokenType.LET,
        TokenType.MUT,
        TokenType.IF,
        TokenType.ELSE,
        TokenType.WHILE,
        TokenType.FOR,
        TokenType.IN,
        TokenType.RETURN,
        TokenType.STIM_BIPHASIC,
        TokenType.SYNC_TICK,
        TokenType.EOF,
    ]
    assert [t.type for t in tokens] == expected_types


def test_lexer_physical_literals_si_scaling():
    source = "10ms 200us 1.5s 0.8V 50mV 100uV 10uA 500nA 25pA 0.5nC 100pC 150Hz 200um 2mm"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    expected = [
        (TokenType.PHYSICAL_LIT, Dimension.TIME, pytest.approx(10e-3)),
        (TokenType.PHYSICAL_LIT, Dimension.TIME, pytest.approx(200e-6)),
        (TokenType.PHYSICAL_LIT, Dimension.TIME, pytest.approx(1.5)),
        (TokenType.PHYSICAL_LIT, Dimension.VOLTAGE, pytest.approx(0.8)),
        (TokenType.PHYSICAL_LIT, Dimension.VOLTAGE, pytest.approx(50e-3)),
        (TokenType.PHYSICAL_LIT, Dimension.VOLTAGE, pytest.approx(100e-6)),
        (TokenType.PHYSICAL_LIT, Dimension.CURRENT, pytest.approx(10e-6)),
        (TokenType.PHYSICAL_LIT, Dimension.CURRENT, pytest.approx(500e-9)),
        (TokenType.PHYSICAL_LIT, Dimension.CURRENT, pytest.approx(25e-12)),
        (TokenType.PHYSICAL_LIT, Dimension.CHARGE, pytest.approx(0.5e-9)),
        (TokenType.PHYSICAL_LIT, Dimension.CHARGE, pytest.approx(100e-12)),
        (TokenType.PHYSICAL_LIT, Dimension.FREQUENCY, pytest.approx(150.0)),
        (TokenType.PHYSICAL_LIT, Dimension.LENGTH, pytest.approx(200e-6)),
        (TokenType.PHYSICAL_LIT, Dimension.LENGTH, pytest.approx(2e-3)),
    ]

    for i, (exp_type, exp_dim, exp_si) in enumerate(expected):
        tok = tokens[i]
        assert tok.type == exp_type
        assert tok.dimension == exp_dim
        assert tok.si_value == exp_si


def test_lexer_line_column_tracking():
    source = "let x = 10;\nlet y = 20;"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    assert tokens[0].value == "let"
    assert tokens[0].line == 1
    assert tokens[0].column == 1

    # 'let' on line 2
    tok_let2 = [t for t in tokens if t.line == 2 and t.type == TokenType.LET][0]
    assert tok_let2.line == 2
    assert tok_let2.column == 1


def test_lexer_comment_skipping():
    source = """
    // Single line comment
    let a = 1; /* inline block comment */ let b = 2;
    /* multi-line
       block
       comment */
    let c = 3;
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    names = [t.value for t in tokens if t.type == TokenType.IDENTIFIER]
    assert names == ["a", "b", "c"]


def test_lexer_unterminated_block_comment():
    source = "/* unterminated block comment"
    lexer = Lexer(source)
    with pytest.raises(LexerError) as exc_info:
        lexer.tokenize()
    assert "Unterminated block comment" in str(exc_info.value)


def test_lexer_unterminated_string():
    source = 'let s = "unterminated string;'
    lexer = Lexer(source)
    with pytest.raises(LexerError) as exc_info:
        lexer.tokenize()
    assert "Unterminated string literal" in str(exc_info.value)


# =========================================================================
# Pratt Parser & Precedence Tests
# =========================================================================

def test_parser_arithmetic_precedence():
    # 2 + 3 * 4 should parse as 2 + (3 * 4)
    source = "let x = 2 + 3 * 4;"
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    stmt = prog.declarations[0]
    assert isinstance(stmt, LetStmtNode)
    expr = stmt.initializer
    assert isinstance(expr, BinaryOpNode)
    assert expr.op == "+"
    assert isinstance(expr.left, LiteralNode) and expr.left.value == 2
    assert isinstance(expr.right, BinaryOpNode)
    assert expr.right.op == "*"
    assert expr.right.left.value == 3
    assert expr.right.right.value == 4


def test_parser_logical_operator_precedence():
    # a || b && c should parse as a || (b && c)
    source = "let r = a || b && c;"
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    stmt = prog.declarations[0]
    expr = stmt.initializer
    assert isinstance(expr, BinaryOpNode)
    assert expr.op == "||"
    assert isinstance(expr.left, IdentifierNode) and expr.left.name == "a"
    assert isinstance(expr.right, BinaryOpNode)
    assert expr.right.op == "&&"


def test_parser_parentheses_override():
    # (2 + 3) * 4
    source = "let x = (2 + 3) * 4;"
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    stmt = prog.declarations[0]
    expr = stmt.initializer
    assert isinstance(expr, BinaryOpNode)
    assert expr.op == "*"
    assert isinstance(expr.left, BinaryOpNode) and expr.left.op == "+"


def test_parser_unary_operators():
    source = "let x = -5; let y = !flag;"
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    stmt1 = prog.declarations[0]
    assert isinstance(stmt1.initializer, UnaryOpNode)
    assert stmt1.initializer.op == "-"

    stmt2 = prog.declarations[1]
    assert isinstance(stmt2.initializer, UnaryOpNode)
    assert stmt2.initializer.op == "!"


# =========================================================================
# AST Declarations & Statements Tests
# =========================================================================

def test_parser_grid_and_channel_declarations():
    source = """
    grid mea[8, 8];
    channel stim_ch = mea[0, 2] mode: BiphasicStim;
    channel sense_ch = mea[7, 5];
    """
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    assert len(prog.declarations) == 3
    grid_decl = prog.declarations[0]
    assert isinstance(grid_decl, GridDeclNode)
    assert grid_decl.name == "mea"

    ch1 = prog.declarations[1]
    assert isinstance(ch1, ChannelDeclNode)
    assert ch1.name == "stim_ch"
    assert ch1.mode == "BiphasicStim"
    assert isinstance(ch1.target, IndexNode)

    ch2 = prog.declarations[2]
    assert isinstance(ch2, ChannelDeclNode)
    assert ch2.name == "sense_ch"


def test_parser_function_and_control_flow():
    source = """
    fn process(count: int) -> int {
        let mut i = 0;
        while (i < count) {
            if (i == 5) {
                return i;
            } else {
                i = i + 1;
            }
        }
        return 0;
    }
    """
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    fn_node = prog.declarations[0]
    assert isinstance(fn_node, FnDeclNode)
    assert fn_node.name == "process"
    assert len(fn_node.params) == 1
    assert fn_node.return_type == "int"
    assert len(fn_node.body.statements) == 3


def test_parser_for_loop():
    source = """
    for idx in 0 .. 16 {
        sync_tick();
    }
    """
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    for_stmt = prog.declarations[0]
    assert isinstance(for_stmt, ForStmtNode)
    assert for_stmt.var_name == "idx"
    assert len(for_stmt.body.statements) == 1
    assert isinstance(for_stmt.body.statements[0], SyncTickStmtNode)


def test_parser_stream_declaration():
    source = """
    stream ClosedLoop {
        bind sensor -> motor;
        bind motor <- sensor;
        cycle {
            sync_tick();
        }
    }
    """
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    stream_node = prog.declarations[0]
    assert isinstance(stream_node, StreamDeclNode)
    assert stream_node.name == "ClosedLoop"
    assert len(stream_node.items) == 3


def test_parser_domain_primitives():
    source = """
    stim_biphasic(ch, 0.8 V, 200 us, 200 us);
    modulate_stdp(1.2);
    let spikes = read_spikes(ch, 20.0);
    let v = read_voltage(ch);
    let rate = pop_firing_rate(10.0);
    sync_tick();
    """
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    prog = parser.parse()

    assert isinstance(prog.declarations[0], StimStmtNode)
    assert isinstance(prog.declarations[1], ModulateStmtNode)
    assert isinstance(prog.declarations[2], LetStmtNode)
    assert isinstance(prog.declarations[2].initializer, DomainCallNode)
    assert prog.declarations[2].initializer.func_name == "read_spikes"
    assert isinstance(prog.declarations[3].initializer, DomainCallNode)
    assert prog.declarations[3].initializer.func_name == "read_voltage"
    assert isinstance(prog.declarations[4].initializer, DomainCallNode)
    assert prog.declarations[4].initializer.func_name == "pop_firing_rate"
    assert isinstance(prog.declarations[5], SyncTickStmtNode)


def test_parser_error_diagnostics():
    source = "let x = ;"
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    with pytest.raises(ParseError) as exc_info:
        parser.parse()
    assert "Expected expression" in str(exc_info.value)
    assert exc_info.value.line == 1
    assert exc_info.value.column == 9


# =========================================================================
# Disassembler & Bytecode Round-Trip Tests
# =========================================================================

def test_compiler_bytecode_binary_header_and_disasm():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 2];
    let mut i = 0;
    while (i < 10) {
        stim_biphasic(ch, 0.8 V, 200 us, 200 us);
        sync_tick();
        i = i + 1;
    }
    """
    bytecode = compile_source(source)

    # 1. Header Validation
    assert len(bytecode) >= HEADER_SIZE
    magic, v_maj, v_min, caps, fsize, crc, n_secs, ch_cnt, max_q, res = struct.unpack_from(HEADER_STRUCT_FORMAT, bytecode, 0)
    assert magic == HEADER_MAGIC
    assert v_maj == VERSION_MAJOR
    assert v_min == VERSION_MINOR
    assert fsize == len(bytecode)
    assert n_secs == 5
    assert ch_cnt == 64
    assert max_q == pytest.approx(0.5)

    # Verify Capabilities: STIMULATION bit must be set
    assert (caps & Capability.CAP_STIMULATION) != 0

    # 2. Checksum Verification
    # Recompute CRC32 with checksum field set to 0
    zeroed = bytearray(bytecode)
    struct.pack_into("<I", zeroed, 12, 0)
    expected_crc = zlib.crc32(bytes(zeroed)) & 0xFFFFFFFF
    assert crc == expected_crc

    # 3. Disassembler Output Verification
    disasm_text = disassemble(bytecode)
    assert "WBC Binary Disassembly" in disasm_text
    assert "STIM_BIPHASIC" in disasm_text
    assert "SYNC_TICK" in disasm_text
    assert "HALT" in disasm_text


def test_compile_benchmark_01():
    with open("benchmarks/01_active_inference_closed_loop.wet", "r", encoding="utf-8") as f:
        src = f.read()
    bcode = compile_source(src)
    assert len(bcode) > HEADER_SIZE
    assert bcode[:4] == HEADER_MAGIC


def test_compile_benchmark_02():
    with open("benchmarks/02_polychronous_reservoir_classifier.wet", "r", encoding="utf-8") as f:
        src = f.read()
    bcode = compile_source(src)
    assert len(bcode) > HEADER_SIZE
    assert bcode[:4] == HEADER_MAGIC


def test_compile_benchmark_03():
    with open("benchmarks/03_homeostatic_stabilization_and_stress.wet", "r", encoding="utf-8") as f:
        src = f.read()
    bcode = compile_source(src)
    assert len(bcode) > HEADER_SIZE
    assert bcode[:4] == HEADER_MAGIC

