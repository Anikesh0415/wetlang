"""
WetLang Test Suite: Static Safety & Semantic Verifier
Tests symbol table resolution, MEA coordinate bounds checks, dimensional type checking,
static voltage clamp enforcement, and CFG loop-yield post-dominance verification.
"""

import pytest
import struct
from compiler.semantic import SemanticError
from compiler.compiler_cli import compile_source
from compiler.isa import (
    HEADER_STRUCT_FORMAT,
    HEADER_SIZE,
    Capability,
    SectionType,
    SECTION_ENTRY_FORMAT,
    SECTION_ENTRY_SIZE,
)


# =========================================================================
# Pass 1: Symbol Table & Scope Resolution
# =========================================================================

def test_symbol_resolution_undeclared_identifier():
    source = """
    let a = 10;
    let b = a + undeclared_var;
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNDECLARED_IDENTIFIER"


def test_symbol_resolution_redeclared_identifier():
    source = """
    let x = 10;
    let x = 20;
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_REDECLARED_IDENTIFIER"


def test_symbol_resolution_duplicate_function_params():
    source = """
    fn test_fn(a: int, a: int) {
        return;
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_REDECLARED_IDENTIFIER"


# =========================================================================
# Pass 1: MEA Electrode Coordinate Bounds Verification ([0..7]x[0..7], 0..63)
# =========================================================================

def test_mea_coordinates_valid():
    source = """
    grid mea[8, 8];
    channel ch1 = mea[0, 0];
    channel ch2 = mea[7, 7];
    channel ch3 = mea[0];
    channel ch4 = mea[63];
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_mea_coordinates_row_out_of_bounds():
    source = """
    grid mea[8, 8];
    channel ch = mea[8, 0];
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"
    assert "row coordinate 8" in str(exc_info.value)


def test_mea_coordinates_col_out_of_bounds():
    source = """
    grid mea[8, 8];
    channel ch = mea[2, 8];
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"
    assert "col coordinate 8" in str(exc_info.value)


def test_mea_coordinates_negative_row():
    source = """
    grid mea[8, 8];
    channel ch = mea[-1, 2];
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"
    assert "row coordinate -1" in str(exc_info.value)


def test_mea_coordinates_negative_col():
    source = """
    grid mea[8, 8];
    channel ch = mea[3, -1];
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"
    assert "col coordinate -1" in str(exc_info.value)


def test_mea_coordinates_linear_out_of_bounds():
    source = """
    grid mea[8, 8];
    channel ch = mea[64];
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"
    assert "linear channel 64" in str(exc_info.value)


def test_mea_coordinates_linear_negative():
    source = """
    grid mea[8, 8];
    channel ch = mea[-5];
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"
    assert "linear channel -5" in str(exc_info.value)


def test_mea_coordinates_in_stim_stmt_out_of_bounds():
    source = """
    grid mea[8, 8];
    stim_biphasic(mea[8, 2], 0.5 V, 0.1 ms, 0.1 ms);
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"


# =========================================================================
# Pass 2: Dimensional Type Checking & Arithmetic Homogeneity
# =========================================================================

def test_dimensional_homogeneous_addition():
    source = """
    let v1 = 0.8 V;
    let v2 = 50 mV;
    let v_total = v1 + v2;
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_dimensional_incompatible_addition():
    # Adding Voltage and Time violates dimensional homogeneity
    source = """
    let v = 0.8 V;
    let t = 10 ms;
    let bad = v + t;
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_DIMENSIONAL_MISMATCH"


def test_dimensional_multiplication_current_time_to_charge():
    # Current * Time -> Charge
    source = """
    let i = 10 uA;
    let t = 200 us;
    let q = i * t;
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_dimensional_incompatible_comparison():
    # Cannot compare Voltage and Time
    source = """
    let v = 0.5 V;
    let t = 10 ms;
    let cond = v < t;
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_DIMENSIONAL_MISMATCH"


# =========================================================================
# Pass 2: Static Voltage Clamp Enforcement (+/- 1.2 V)
# =========================================================================

def test_static_voltage_clamp_valid():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stim_biphasic(ch, 0.8 V, 0.1 ms, 0.1 ms);
    stim_biphasic(ch, 1.2 V, 0.1 ms, 0.1 ms);
    stim_biphasic(ch, -1.2 V, 0.1 ms, 0.1 ms);
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_static_voltage_clamp_positive_exceeded():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stim_biphasic(ch, 1.8 V, 0.1 ms, 0.1 ms);
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"
    assert "exceeds hard safety clamp" in str(exc_info.value)


def test_static_voltage_clamp_negative_exceeded():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stim_biphasic(ch, -1.5 V, 0.1 ms, 0.1 ms);
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"


def test_static_voltage_clamp_unitless_float_exceeded():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stim_biphasic(ch, 2.5, 0.1 ms, 0.1 ms);
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"


# =========================================================================
# Pass 3: Static Loop-Yield Verification (CFG Post-Dominance)
# =========================================================================

def test_loop_yield_bounded_while_loop():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    while (true) {
        stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        sync_tick();
    }
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_loop_yield_unbounded_while_loop_rejected():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    while (true) {
        stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        // Missing sync_tick!
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"
    assert "Unbounded stimulation loop detected" in str(exc_info.value)


def test_loop_yield_unbounded_if_branch_rejected():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    let x = 1;
    while (true) {
        if (x > 0) {
            stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
            // Missing sync_tick in this branch!
        } else {
            sync_tick();
        }
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"


def test_loop_yield_bounded_if_branch_accepted():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    let x = 1;
    while (true) {
        if (x > 0) {
            stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        }
        sync_tick(); // Common exit path yields
    }
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_loop_yield_pure_compute_loop_accepted():
    source = """
    let mut count = 0;
    while (count < 100) {
        count = count + 1;
    }
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_loop_yield_unbounded_for_loop_rejected():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    for i in 0 .. 10 {
        stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        // Missing sync_tick!
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"


def test_loop_yield_bounded_for_loop_accepted():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    for i in 0 .. 10 {
        stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        sync_tick();
    }
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_loop_yield_stream_cycle_unbounded_rejected():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stream Controller {
        cycle {
            stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
            // Missing sync_tick in cycle!
        }
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"


def test_loop_yield_stream_cycle_bounded_accepted():
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stream Controller {
        cycle {
            stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
            sync_tick();
        }
    }
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


# =========================================================================
# Remediation Tests: Challenger 2 Security Evasion Hardening
# =========================================================================

def test_loop_yield_nested_block_unbounded_rejected():
    """VULN-1C: Nested BlockNode enclosing stim_biphasic without sync_tick."""
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    while (true) {
        {
            stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        }
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"


def test_loop_yield_inner_while_loop_evasion_rejected():
    """VULN-1A: Inner while(false) with sync_tick cannot satisfy outer stimulation loop."""
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    while (true) {
        stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        while (false) {
            sync_tick();
        }
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"


def test_loop_yield_inner_for_loop_evasion_rejected():
    """VULN-1B: Inner for loop with empty iteration cannot satisfy outer stimulation loop."""
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    while (true) {
        stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        for i in 0 .. 0 {
            sync_tick();
        }
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"


def test_loop_yield_nested_block_if_without_else_rejected():
    """VULN-1D: If-statement without else branch inside block does not guarantee yield."""
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    let a = 0;
    while (true) {
        stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
        {
            if (a > 0) {
                sync_tick();
            }
        }
    }
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"


def test_static_voltage_clamp_constant_folded_addition_exceeded():
    """VULN-2A: Constant-folded voltage addition exceeding clamp limit (+/- 1.2 V)."""
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stim_biphasic(ch, 1.0 V + 0.5 V, 0.1 ms, 0.1 ms);
    sync_tick();
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"


def test_static_voltage_clamp_constant_folded_multiplication_exceeded():
    """VULN-2A: Constant-folded voltage multiplication exceeding clamp limit."""
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stim_biphasic(ch, 0.8 V * 2.0, 0.1 ms, 0.1 ms);
    sync_tick();
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"


def test_static_voltage_clamp_variable_constant_exceeded():
    """VULN-2B: Immutable variable initialized to voltage exceeding clamp limit."""
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    let v = 1.5 V;
    stim_biphasic(ch, v, 0.1 ms, 0.1 ms);
    sync_tick();
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"


def test_negative_high_voltage_capability_and_manifest():
    """VULN-4A: Negative high voltage (-1.0 V) sets CAP_HIGH_VOLTAGE and records max_voltage_seen."""
    source = """
    grid mea[8, 8];
    channel ch = mea[0, 0];
    stim_biphasic(ch, -1.0 V, 0.1 ms, 0.1 ms);
    sync_tick();
    """
    bytecode = compile_source(source)
    caps = struct.unpack_from("<H", bytecode, 6)[0]
    assert bool(caps & Capability.CAP_HIGH_VOLTAGE)

    # Check Section 4: SAFETY_MANIFEST
    sec_table_off = HEADER_SIZE
    n_secs = struct.unpack_from("<I", bytecode, 16)[0]
    manifest_found = False
    for i in range(n_secs):
        stype, _, off, size = struct.unpack_from(SECTION_ENTRY_FORMAT, bytecode, sec_table_off + i * SECTION_ENTRY_SIZE)
        if stype == SectionType.SAFETY_MANIFEST.value:
            m_caps, loop_yield, max_v, max_chg = struct.unpack_from("<IBff", bytecode, off)
            assert bool(m_caps & Capability.CAP_HIGH_VOLTAGE)
            assert max_v == pytest.approx(1.0, rel=1e-3)
            manifest_found = True
            break
    assert manifest_found


def test_mea_coordinates_constant_folded_out_of_bounds():
    """VULN-3A: Constant-folded coordinate expressions exceeding MEA grid bounds."""
    source = """
    grid mea[8, 8];
    channel ch = mea[7 + 1, 0];
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"
    assert "row coordinate 8" in str(exc_info.value)


def test_mea_coordinates_constant_folded_linear_out_of_bounds():
    """VULN-3A: Constant-folded linear coordinate exceeding 0..63."""
    source = """
    grid mea[8, 8];
    channel ch = mea[60 + 4];
    """
    with pytest.raises(SemanticError) as exc_info:
        compile_source(source)
    assert exc_info.value.error_code == "ERR_ELECTRODE_OUT_OF_BOUNDS"
    assert "linear channel 64" in str(exc_info.value)


def test_mea_coordinates_constant_folded_valid_mapping():
    """Valid constant-folded coordinates compile and resolve correctly."""
    source = """
    grid mea[8, 8];
    channel ch = mea[2 + 1, 3 - 1];
    stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
    sync_tick();
    """
    bytecode = compile_source(source)
    assert len(bytecode) > 0


def test_capability_multi_electrode_threshold():
    """VULN-4B: CAP_MULTI_ELECTRODE requires > 16 unique channels, not channel_id >= 16."""
    # Channel 16 alone (index 16) should NOT trigger CAP_MULTI_ELECTRODE
    source_single_16 = """
    grid mea[8, 8];
    channel ch = mea[2, 0];
    stim_biphasic(ch, 0.5 V, 0.1 ms, 0.1 ms);
    sync_tick();
    """
    bc1 = compile_source(source_single_16)
    caps1 = struct.unpack_from("<H", bc1, 6)[0]
    assert not bool(caps1 & Capability.CAP_MULTI_ELECTRODE)

    # 17 distinct channels MUST trigger CAP_MULTI_ELECTRODE
    stims = "\n".join(f"    stim_biphasic(mea[{i}], 0.5 V, 0.1 ms, 0.1 ms);" for i in range(17))
    source_multi_17 = f"""
    grid mea[8, 8];
    while (true) {{
{stims}
        sync_tick();
    }}
    """
    bc2 = compile_source(source_multi_17)
    caps2 = struct.unpack_from("<H", bc2, 6)[0]
    assert bool(caps2 & Capability.CAP_MULTI_ELECTRODE)
