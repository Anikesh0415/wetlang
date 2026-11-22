"""
WetLang v1.1 - Section 1 Independent Audit Verification Tests
Validates:
1. Dimensional analysis for Ohm's Law (Resistance, Conductance, V=I*R, I=V*G, V/I=R, I/V=G).
2. Strict dimensionless checking for transcendental functions (exp, log, sqrt, pow).
3. Anti-rollback sequence counter verification in VM bytecode loader.
4. Channel capability checking for reference and recording-only channel indices.
5. CFG loop sync_tick dominance verification across nested and branching control flow.
"""

import pytest
from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.semantic import SemanticAnalyzer, SemanticError
from compiler.emitter import BytecodeEmitter
from compiler.token import Dimension
from bindings.runtime import WetRuntime, WetVMConfig, WetVMError


def compile_src(src: str, sequence_counter: int = 1):
    tokens = Lexer(src).tokenize()
    ast = Parser(tokens).parse()
    analyzer = SemanticAnalyzer(ast)
    analyzer.analyze()
    return BytecodeEmitter().compile(ast, sequence_counter=sequence_counter)


def test_ohms_law_dimensional_analysis():
    """Validates that V / I yields Resistance and I / V yields Conductance (Ohm's Law)."""
    src_valid = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    let v: Voltage = 0.4V;
    let i: Current = 10uA;
    let r = v / i;
    let g = i / v;
    let v_calc = i * r;
    let i_calc = v * g;
    """
    tokens = Lexer(src_valid).tokenize()
    ast = Parser(tokens).parse()
    analyzer = SemanticAnalyzer(ast)
    analyzer.analyze()
    
    # Check that dimensions are correctly inferred
    for stmt in ast.declarations:
        if hasattr(stmt, "name") and stmt.name == "r":
            dim = analyzer.node_dimensions.get(id(stmt.initializer))
            assert dim == Dimension.RESISTANCE, f"Expected RESISTANCE for v/i, got {dim}"
        elif hasattr(stmt, "name") and stmt.name == "g":
            dim = analyzer.node_dimensions.get(id(stmt.initializer))
            assert dim == Dimension.CONDUCTANCE, f"Expected CONDUCTANCE for i/v, got {dim}"
        elif hasattr(stmt, "name") and stmt.name == "v_calc":
            dim = analyzer.node_dimensions.get(id(stmt.initializer))
            assert dim == Dimension.VOLTAGE, f"Expected VOLTAGE for i*r, got {dim}"
        elif hasattr(stmt, "name") and stmt.name == "i_calc":
            dim = analyzer.node_dimensions.get(id(stmt.initializer))
            assert dim == Dimension.CURRENT, f"Expected CURRENT for v*g, got {dim}"


def test_transcendental_dimensionless_check_happy():
    """Dimensionless arguments to exp(), log(), sqrt() succeed."""
    src = """
    let x = 0.5;
    let y = exp(x);
    let z = sqrt(y);
    let w = log(z);
    """
    tokens = Lexer(src).tokenize()
    ast = Parser(tokens).parse()
    SemanticAnalyzer(ast).analyze()


def test_transcendental_dimensional_mismatch_rejected():
    """Passing a physical dimension into exp() or sqrt() must raise ERR_DIMENSIONAL_MISMATCH."""
    src_bad_exp = """
    let v: Voltage = 100mV;
    let y = exp(v);
    """
    tokens = Lexer(src_bad_exp).tokenize()
    ast = Parser(tokens).parse()
    with pytest.raises(SemanticError) as exc_info:
        SemanticAnalyzer(ast).analyze()
    assert exc_info.value.error_code == "ERR_DIMENSIONAL_MISMATCH"
    assert "dimensionless" in str(exc_info.value).lower()

    src_bad_sqrt = """
    let t: Time = 10ms;
    let y = sqrt(t);
    """
    tokens = Lexer(src_bad_sqrt).tokenize()
    ast = Parser(tokens).parse()
    with pytest.raises(SemanticError) as exc_info:
        SemanticAnalyzer(ast).analyze()
    assert exc_info.value.error_code == "ERR_DIMENSIONAL_MISMATCH"


def test_cfg_sync_tick_post_dominance_nested_blocks():
    """Nested blocks carrying stim are safely validated if sync_tick post-dominates."""
    src_valid = """
    grid mea[8, 8];
    channel ch = mea[0, 1];
    while (true) {
        stim_biphasic(ch, 0.4V, 100us, 100us);
        {
            let a = 1;
        }
        sync_tick;
    }
    """
    tokens = Lexer(src_valid).tokenize()
    ast = Parser(tokens).parse()
    SemanticAnalyzer(ast).analyze()


def test_cfg_sync_tick_branching_rejection():
    """If sync_tick is inside a branch without an else branch, it fails CFG post-dominance."""
    src_invalid = """
    grid mea[8, 8];
    channel ch = mea[0, 1];
    while (true) {
        stim_biphasic(ch, 0.4V, 100us, 100us);
        if (true) {
            sync_tick;
        }
    }
    """
    tokens = Lexer(src_invalid).tokenize()
    ast = Parser(tokens).parse()
    with pytest.raises(SemanticError) as exc_info:
        SemanticAnalyzer(ast).analyze()
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"


def test_reference_channel_static_rejection():
    """Stimulating a reference or recording-only electrode index is rejected at compile time."""
    src_ref = """
    grid mea[8, 8];
    channel ch_ref = mea[0, 0] mode: Reference;
    channel ch_stim = mea[0, 0];
    stim_biphasic(ch_ref, 0.4V, 100us, 100us);
    """
    tokens = Lexer(src_ref).tokenize()
    ast = Parser(tokens).parse()
    with pytest.raises(SemanticError) as exc_info:
        SemanticAnalyzer(ast).analyze()
    assert exc_info.value.error_code == "ERR_STIM_ON_REFERENCE_CHANNEL"


def test_anti_rollback_security_verification():
    """Bytecode with sequence_counter < min_sequence_counter must be rejected by runtime."""
    src = """
    grid mea[8, 8];
    channel ch = mea[0, 1];
    stim_biphasic(ch, 0.4V, 100us, 100us);
    sync_tick;
    """
    # Compile with sequence_counter = 1
    wbc_v1 = compile_src(src, sequence_counter=1)

    # Runtime requiring minimum sequence counter = 2
    cfg_strict = WetVMConfig(min_sequence_counter=2)
    with WetRuntime(config=cfg_strict) as rt:
        with pytest.raises(WetVMError) as exc_info:
            rt.load_bytecode(wbc_v1)
        assert "Anti-rollback" in str(exc_info.value) or "CAPABILITY_DENIED" in str(exc_info.value)

    # Compile with sequence_counter = 2
    wbc_v2 = compile_src(src, sequence_counter=2)
    with WetRuntime(config=cfg_strict) as rt:
        rt.load_bytecode(wbc_v2) # Must succeed!
