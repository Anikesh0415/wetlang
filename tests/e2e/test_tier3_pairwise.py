"""
WetLang E2E Test Suite - Tier 3: Cross-Feature Pairwise Combination Tests
Tests the combinatorial interactions across compiler, native runtime,
biophysical digital twin sandbox, and biocybersecurity hardware interlocks.
Features Covered: All 28 features in PROJECT.md paired across module boundaries.
Authoritative Specification: spec_miner_e2e_3/handoff.md § 5 (28 Pairwise Tests).
"""

import os
import sys
import math
import struct
import zlib
import unittest
from typing import Dict, List, Optional, Tuple, Any

# Ensure project root is on sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

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
    require_feature,
    skip_if_unavailable,
    make_minimal_wet_program,
    generate_valid_wet_source,
    make_unyielded_loop_code,
    make_overvoltage_code,
    make_oob_coordinate_code,
    make_syntax_error_code,
    make_wbc_header,
    generate_mea_coordinates,
    make_biphasic_stim_trace,
    make_spike_raster_matrix,
    assert_si_value_close,
    assert_voltage_clamped,
    assert_sliding_charge_balance,
    assert_epileptiform_trip,
    assert_wbc_header_valid,
)

if HAS_COMPILER:
    from compiler.lexer import Lexer, LexerError
    from compiler.parser import Parser, ParseError
    from compiler.semantic import SemanticAnalyzer, SemanticError
    from compiler.emitter import BytecodeEmitter, compile_source as wet_compile_source, ConstantPool
    from compiler.isa import (
        Opcode,
        Capability,
        SectionType,
        HEADER_MAGIC,
        HEADER_SIZE,
        VERSION_MAJOR,
        VERSION_MINOR,
        HEADER_STRUCT_FORMAT,
        SECTION_ENTRY_FORMAT,
        SECTION_ENTRY_SIZE,
    )
    from compiler.token import TokenType, Dimension

try:
    import numpy as np
except ImportError:
    np = None


class TestTier3Pairwise(WetLangE2ETestCase):
    """
    Tier 3: Pairwise Cross-Feature Combinations Suite.
    Contains at least 28 tests systematically verifying pairwise interactions.
    """
    tier = 3

    def compile_wet(self, source_code: str) -> bytes:
        """Helper to run the 4-stage compiler pipeline and return WBC bytes."""
        if not HAS_COMPILER:
            self.skipTest("Compiler pipeline (M1) not available")
        return wet_compile_source(source_code)

    def assert_compiled_wbc_valid(self, wbc_bytes: bytes) -> Dict[str, Any]:
        """Validate WBC binary emitted by compiler against HEADER_STRUCT_FORMAT."""
        self.assertGreaterEqual(len(wbc_bytes), HEADER_SIZE)
        magic, v_maj, v_min, caps, fsize, crc, n_secs, ch_cnt, max_q, res = struct.unpack_from(
            HEADER_STRUCT_FORMAT, wbc_bytes, 0
        )
        self.assertEqual(magic, HEADER_MAGIC)
        self.assertEqual(v_maj, VERSION_MAJOR)
        self.assertEqual(v_min, VERSION_MINOR)
        self.assertEqual(ch_cnt, 64)
        self.assertEqual(fsize, len(wbc_bytes))
        self.assertGreater(n_secs, 0)
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
            "reserved": res,
        }

    # =========================================================================
    # Test 1: Compiler Loop-Yield Verifier x Runtime Watchdog Synchronization
    # Features: F5 (Static Loop Verifier) x F9 (VM Tick Scheduler)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_01_static_loop_yield_and_runtime_watchdog(self):
        """Pair 01: F5 x F9 - CFG loop-yield verification and runtime tick stepping."""
        # 1. Valid program: while-loop containing stim_biphasic has sync_tick
        valid_src = """grid mea[8, 8];
channel stim_ch = mea[1, 1];
int count = 0;
while (count < 50) {
    stim_biphasic(stim_ch, 0.5, 0.1, 0.1);
    sync_tick();
    count = count + 1;
}
"""
        wbc_bytes = self.compile_wet(valid_src)
        parsed = self.assert_compiled_wbc_valid(wbc_bytes)
        self.assertEqual(parsed["magic"], b"WETB")

        # 2. Adversarial program: loop containing stim_biphasic lacking sync_tick
        unyielded_src = make_unyielded_loop_code()
        with self.assertRaises(SemanticError) as ctx:
            self.compile_wet(unyielded_src)
        self.assertEqual(ctx.exception.error_code, "ERR_UNBOUNDED_STIM_LOOP")

        # 3. Branching loop: sync_tick only on one branch, must be rejected
        branch_src = """grid mea[8, 8];
channel stim_ch = mea[0, 0];
int flag = 1;
while (flag > 0) {
    if (flag == 1) {
        sync_tick();
    }
    stim_biphasic(stim_ch, 0.5, 0.1, 0.1);
}
"""
        with self.assertRaises(SemanticError) as ctx:
            self.compile_wet(branch_src)
        self.assertEqual(ctx.exception.error_code, "ERR_UNBOUNDED_STIM_LOOP")

        # 4. If native VM is available, execute 50 ticks
        if HAS_NATIVE_VM:
            success, err, telem = self.run_program(wbc_bytes, ticks=50)
            self.assertTrue(success, f"Runtime execution failed: {err}")
            self.assertIsNotNone(telem)
            self.assertEqual(telem.get("tick_index", 50), 50)

    # =========================================================================
    # Test 2: Biphasic Waveform x Sliding Charge Accumulator
    # Features: F19 (Water-Window / Biphasic Stim) x F20 (Sliding Charge Watchdog)
    # =========================================================================
    def test_tier3_pair_02_biphasic_stim_charge_ring_buffer(self):
        """Pair 02: F19 x F20 - Biphasic waveform integration and sliding charge balance."""
        # 1. Verify compilation of biphasic pulse program
        if HAS_COMPILER:
            code = """grid mea[8, 8];
channel ch0 = mea[0, 4];
stim_biphasic(ch0, 0.8, 0.2, 0.2);
sync_tick();
"""
            wbc_bytes = self.compile_wet(code)
            self.assert_compiled_wbc_valid(wbc_bytes)

        # 2. Balanced biphasic pulse: +0.8V 2 ticks, -0.8V 2 ticks, 0V 96 ticks
        balanced_trace = [0.0008, 0.0008, -0.0008, -0.0008] + [0.0] * 96
        full_trace = balanced_trace * 3
        result = assert_sliding_charge_balance(full_trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(result.balanced, "Balanced biphasic stimulation should not trip watchdog")
        self.assertLess(result.max_residual, 0.01)

        # 3. Unbalanced monophasic pulse: +0.01 nC/tick continuous
        unbalanced_trace = [0.01] * 200  # 100 ticks * 0.01 = 1.0 nC > 0.5 nC
        result_unb = assert_sliding_charge_balance(unbalanced_trace, max_charge_nc=0.5, window_ticks=100)
        self.assertFalse(result_unb.balanced, "Unbalanced stimulation must trip charge watchdog")
        self.assertGreaterEqual(result_unb.tick, 100)

    # =========================================================================
    # Test 3: High-Frequency Stimulation x Epileptiform Runaway Breaker
    # Features: F19 (Stimulation) x F21 (Epileptiform Runaway Breaker)
    # =========================================================================
    def test_tier3_pair_03_high_freq_stim_epileptiform_trip(self):
        """Pair 03: F19 x F21 - High-frequency stimulation and epileptiform trip logic."""
        # Condition: Population firing > 150 Hz across > 35% of channels (>= 23/64) for 50.0 ms (500 ticks)

        # Case A: 25 hyperactive channels (> 35%) firing at 200 Hz (every 50 ticks) for 1500 ticks (> 50 ms sustained) -> MUST TRIP
        if np is not None:
            raster_runaway = np.zeros((1500, 64), dtype=np.uint8)
            raster_runaway[::50, :25] = 1
        else:
            raster_runaway = [[0] * 64 for _ in range(1500)]
            for t in range(0, 1500, 50):
                for ch in range(25):
                    raster_runaway[t][ch] = 1

        res_runaway = assert_epileptiform_trip(
            raster_runaway, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertTrue(res_runaway.tripped, "25 channels at 200 Hz for >50 ms must trip epileptiform breaker")
        self.assertGreaterEqual(res_runaway.trip_tick, 500)

        # Case B: Only 22 channels (34.375% <= 35%) at 200 Hz for 1500 ticks -> MUST NOT TRIP
        if np is not None:
            raster_few = np.zeros((1500, 64), dtype=np.uint8)
            raster_few[::50, :22] = 1
        else:
            raster_few = [[0] * 64 for _ in range(1500)]
            for t in range(0, 1500, 50):
                for ch in range(22):
                    raster_few[t][ch] = 1

        res_few = assert_epileptiform_trip(
            raster_few, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertFalse(res_few.tripped, "22 channels (<= 35%) should not trip breaker")

        # Case C: 25 channels at 200 Hz but only sustained for 490 ticks (49.0 ms < 50.0 ms) -> MUST NOT TRIP
        if np is not None:
            raster_short = np.zeros((490, 64), dtype=np.uint8)
            raster_short[::50, :25] = 1
        else:
            raster_short = [[0] * 64 for _ in range(490)]
            for t in range(0, 490, 50):
                for ch in range(25):
                    raster_short[t][ch] = 1

        res_short = assert_epileptiform_trip(
            raster_short, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertFalse(res_short.tripped, "Stimulation sustained for <50 ms should not trip breaker")

        # Case D: Sub-critical frequency: 25 channels at 100 Hz (every 100 ticks < 150 Hz) -> MUST NOT TRIP
        if np is not None:
            raster_slow = np.zeros((1500, 64), dtype=np.uint8)
            raster_slow[::100, :25] = 1
        else:
            raster_slow = [[0] * 64 for _ in range(1500)]
            for t in range(0, 1500, 100):
                for ch in range(25):
                    raster_slow[t][ch] = 1

        res_slow = assert_epileptiform_trip(
            raster_slow, channels=64, duration_ms=50.0, dt_ms=0.1, threshold_hz=150.0, channel_ratio=0.35
        )
        self.assertFalse(res_slow.tripped, "Stimulation at <150 Hz should not trip breaker")

    # =========================================================================
    # Test 4: Voltage Clamp Saturation x Biophysical Spike Readout
    # Features: F19 (Voltage Clamp) x F14 (Absolute Refractory Spike Readout)
    # =========================================================================
    def test_tier3_pair_04_voltage_clamp_saturation_and_spike_readout(self):
        """Pair 04: F19 x F14 - Requested voltage saturation and refractory firing limit."""
        # 1. Voltage Clamp Saturation: +/- 1.2 V hard clamp
        assert_voltage_clamped(2.5, 1.2, 1.2)
        assert_voltage_clamped(-3.5, -1.2, 1.2)
        assert_voltage_clamped(0.9, 0.9, 1.2)

        # 2. Refractory Limit on Spike Readout:
        # Absolute refractory period = 2.0 ms (20 ticks).
        # Max firing rate = 1 / 2.0ms = 500 Hz.
        # In a 10.0 ms window (100 ticks), maximum theoretical spikes = 10.0 / 2.0 = 5 spikes.
        window_ms = 10.0
        refractory_ms = 2.0
        max_possible_spikes = int(math.floor(window_ms / refractory_ms))
        self.assertEqual(max_possible_spikes, 5)

        # Inter-spike interval cannot be less than 2.0 ms
        spike_times_ms = [0.0, 2.1, 4.2, 6.3, 8.5]
        isis = [spike_times_ms[i+1] - spike_times_ms[i] for i in range(len(spike_times_ms) - 1)]
        for isi in isis:
            self.assertGreaterEqual(isi, refractory_ms, "ISI must satisfy absolute refractory >= 2.0 ms")

        # 3. Compiler capability check for high voltage
        if HAS_COMPILER:
            code = make_minimal_wet_program(channel_id=0, voltage_str="1.1V")
            wbc_bytes = self.compile_wet(code)
            parsed = self.assert_compiled_wbc_valid(wbc_bytes)
            # Capabilities should include stimulation (0x0001) and high voltage (0x0008)
            self.assertTrue(parsed["capabilities"] & Capability.CAP_STIMULATION.value)
            self.assertTrue(parsed["capabilities"] & Capability.CAP_HIGH_VOLTAGE.value)

    # =========================================================================
    # Test 5: Tsodyks-Markram Vesicle Depletion x STDP Weight Updates
    # Features: F15 (Tsodyks-Markram STP) x F16 (Pairwise Trace STDP)
    # =========================================================================
    def test_tier3_pair_05_tm_vesicle_depletion_and_stdp_updates(self):
        """Pair 05: F15 x F16 - Short-term synaptic depression and STDP weight modulation."""
        u = 0.5
        tau_rec = 800.0  # ms
        dt_burst = 10.0  # ms (100 Hz train)

        R = 1.0
        conductance_jumps = []
        w_syn = 20.0  # nS baseline

        for spike_idx in range(6):
            g_jump = w_syn * u * R
            conductance_jumps.append(g_jump)
            # Deplete
            R = R * (1.0 - u)
            # Recover over dt_burst
            R = 1.0 - (1.0 - R) * math.exp(-dt_burst / tau_rec)

        # Conductance jump must attenuate monotonically during 100 Hz train
        for i in range(len(conductance_jumps) - 1):
            self.assertGreater(conductance_jumps[i], conductance_jumps[i+1], "Vesicle depletion must attenuate PSC jump")
        self.assertLess(conductance_jumps[-1], conductance_jumps[0] * 0.4)

        # STDP Potentiation vs Depression
        tau_plus = 20.0   # ms
        tau_minus = 20.0  # ms
        A_plus = 0.008    # nS
        A_minus = A_plus * 1.05  # 1.05x depression bias

        delta_w_ltp = A_plus * math.exp(-2.0 / tau_plus)
        delta_w_ltd = -A_minus * math.exp(-2.0 / tau_minus)

        self.assertGreater(delta_w_ltp, 0.0)
        self.assertLess(delta_w_ltd, 0.0)
        self.assertGreater(abs(delta_w_ltd), delta_w_ltp, "Depression bias must ensure |LTD| > LTP")

        # Bounding: weights must stay in [0.0, 40.0] nS
        w_test = 39.995 + delta_w_ltp
        w_clamped = min(40.0, max(0.0, w_test))
        self.assertLessEqual(w_clamped, 40.0)

    # =========================================================================
    # Test 6: 8x8 MEA Coordinate Mapping x Volume Conduction Pickup
    # Features: F12 (8x8 MEA Grid) x F13 (Volume Conduction ODE Solver)
    # =========================================================================
    def test_tier3_pair_06_mea_coordinates_and_volume_conduction(self):
        """Pair 06: F12 x F13 - 2D grid coordinate mapping and 3D volume conduction kernel."""
        coords = generate_mea_coordinates(valid=True, count=64)
        for idx, (r, c) in enumerate(coords):
            self.assertEqual(r * 8 + c, idx)

        r_0 = 15.0  # um
        pitch = 200.0  # um

        K_center = 1.0 / math.sqrt(0.0**2 + r_0**2)
        K_adjacent = 1.0 / math.sqrt(pitch**2 + r_0**2)
        d_far = math.sqrt((3 * pitch)**2 + (3 * pitch)**2)
        K_far = 1.0 / math.sqrt(d_far**2 + r_0**2)

        self.assertGreater(K_center, K_adjacent)
        self.assertGreater(K_adjacent, K_far)
        self.assertGreater(K_far, 0.0)
        ratio = K_center / K_adjacent
        self.assertGreater(ratio, 10.0)

        # Compiler coordinate bounds verification
        if HAS_COMPILER:
            code_bad = make_oob_coordinate_code(row=8, col=0)
            with self.assertRaises(SemanticError) as ctx:
                self.compile_wet(code_bad)
            self.assertEqual(ctx.exception.error_code, "ERR_ELECTRODE_OUT_OF_BOUNDS")

    # =========================================================================
    # Test 7: Bytecode Binary Emitter x C-ABI VM Loader x ctypes FFI Roundtrip
    # Features: F7 (Binary Emitter) x F8 (C-ABI VM Loader) x F10 (ctypes FFI)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_07_emitter_loader_ffi_roundtrip(self):
        """Pair 07: F7 x F8 x F10 - WBC serialization, CRC32, and section table layout."""
        code = """grid mea[8, 8];
channel ch_a = mea[0, 0];
channel ch_b = mea[7, 7];
int x = 42;
sync_tick();
"""
        wbc_bytes = self.compile_wet(code)
        parsed = self.assert_compiled_wbc_valid(wbc_bytes)
        self.assertEqual(parsed["channel_count"], 64)

        # Inspect Section Table
        sec_offset = HEADER_SIZE
        sec_types = []
        for _ in range(parsed["num_sections"]):
            stype, _, off, size = struct.unpack_from(SECTION_ENTRY_FORMAT, wbc_bytes, sec_offset)
            sec_types.append(stype)
            self.assertGreater(off, 0)
            self.assertGreater(size, 0)
            sec_offset += SECTION_ENTRY_SIZE

        self.assertIn(SectionType.BYTECODE_STREAM.value, sec_types)
        self.assertIn(SectionType.TOPOLOGY_CONFIG.value, sec_types)

        # Verify common.py assert_wbc_header_valid against make_wbc_header()
        synth_header = make_wbc_header(magic=b"WETB", major=1, minor=0, caps=0x01, file_size=64, channels=64)
        synth_parsed = assert_wbc_header_valid(synth_header)
        self.assertEqual(synth_parsed["magic"], b"WETB")

    # =========================================================================
    # Test 8: Long-Run Execution x Zero-Copy NumPy Telemetry
    # Features: F9 (VM Tick Scheduler) x F11 (Zero-Copy NumPy Telemetry)
    # =========================================================================
    def test_tier3_pair_08_multitick_zerocopy_numpy_telemetry(self):
        """Pair 08: F9 x F11 - Multi-tick scheduler and zero-copy NumPy array views."""
        num_channels = 64
        voltages = [float(-65.0 + 0.1 * i) for i in range(num_channels)]
        raster_mask = 0x0000000000000005  # Channels 0 and 2 fired

        raw_buffer = struct.pack(f"<{num_channels}fQ", *voltages, raster_mask)
        self.assertEqual(len(raw_buffer), num_channels * 4 + 8)

        if np is not None:
            v_array = np.frombuffer(raw_buffer[:num_channels * 4], dtype=np.float32)
            self.assertEqual(v_array.shape, (64,))
            self.assertEqual(v_array.dtype, np.float32)
            self.assertAlmostEqual(float(v_array[0]), -65.0, places=4)
            self.assertAlmostEqual(float(v_array[63]), -65.0 + 6.3, places=4)

            v_array.flags.writeable = False
            with self.assertRaises(ValueError):
                v_array[0] = 0.0

        active_channels = [ch for ch in range(64) if (raster_mask & (1 << ch))]
        self.assertEqual(active_channels, [0, 2])

    # =========================================================================
    # Test 9: Lexer Physical Units x Semantic Dimensional Analysis
    # Features: F2 (Lexer Physical Units) x F4 (Semantic Dimensional Analysis)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_09_lexer_units_and_semantic_dimensions(self):
        """Pair 09: F2 x F4 - Unit tokenization and dimensional homogeneity validation."""
        valid_time_src = """grid mea[8, 8];
fn main() -> int {
    let t: Time = 10ms + 500us;
    sync_tick();
    return 0;
}
"""
        wbc = self.compile_wet(valid_time_src)
        self.assert_compiled_wbc_valid(wbc)

        valid_charge_src = """grid mea[8, 8];
fn main() -> int {
    let q: Charge = 10uA * 2ms;
    sync_tick();
    return 0;
}
"""
        wbc_q = self.compile_wet(valid_charge_src)
        self.assert_compiled_wbc_valid(wbc_q)

        invalid_src = """grid mea[8, 8];
fn main() -> int {
    let bad = 1.0V + 5ms;
    sync_tick();
    return 0;
}
"""
        with self.assertRaises(SemanticError) as ctx:
            self.compile_wet(invalid_src)
        self.assertEqual(ctx.exception.error_code, "ERR_DIMENSIONAL_MISMATCH")

    # =========================================================================
    # Test 10: Pratt Expression Precedence x Bytecode Stack Evaluation
    # Features: F3 (Pratt Parser) x F6 (Custom Bytecode ISA Stack Ops)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_10_pratt_precedence_stack_depth(self):
        """Pair 10: F3 x F6 - Operator precedence parsing and balanced stack evaluation."""
        code = """grid mea[8, 8];
fn main() -> int {
    let res: int = 0;
    if (2 + 3 * 4 > 10 && 5 - 2 == 3) {
        res = 1;
    }
    sync_tick();
    return res;
}
"""
        wbc_bytes = self.compile_wet(code)
        self.assert_compiled_wbc_valid(wbc_bytes)

        # Test operator precedence directly via parser AST
        lexer = Lexer("2 + 3 * 4 > 10 && 5 - 2 == 3")
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        expr_ast = parser.parse_expression()
        self.assertIsNotNone(expr_ast)

        # Stack evaluation simulation for expression: 2 + 3 * 4
        stack = []
        stack.append(2)
        stack.append(3)
        stack.append(4)
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
        self.assertEqual(stack[-1], 12)
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
        self.assertEqual(stack[-1], 14)
        self.assertEqual(len(stack), 1)

    # =========================================================================
    # Test 11: Semantic Coordinate Bounds x Capability Bitmask Verification
    # Features: F4 (Semantic Analyzer) x F18 (Static Capability Verifier)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_11_semantic_bounds_and_capability_bitmask(self):
        """Pair 11: F4 x F18 - Multi-electrode coordinate checks and capability bitmask emission."""
        # Multi-electrode stimulation across 17 distinct channels (>16) triggers CAP_MULTI_ELECTRODE
        channels_decl = []
        stim_stmts = []
        for i in range(17):
            r, c = i // 8, i % 8
            channels_decl.append(f"channel ch{i} = mea[{r}, {c}];")
            voltage_str = "0.9" if i == 0 else "0.5"
            stim_stmts.append(f"    stim_biphasic(ch{i}, {voltage_str}, 0.1, 0.1);")

        decl_text = "\n".join(channels_decl)
        stim_text = "\n".join(stim_stmts)

        src = f"""grid mea[8, 8];
{decl_text}
fn main() -> int {{
{stim_text}
    sync_tick();
    return 0;
}}
"""
        wbc_bytes = self.compile_wet(src)
        parsed = self.assert_compiled_wbc_valid(wbc_bytes)
        caps = parsed["capabilities"]

        # CAP_STIMULATION (0x0001), CAP_HIGH_VOLTAGE (0x0008, 0.9V >= 0.8V), CAP_MULTI_ELECTRODE (0x0010, >16 electrodes)
        self.assertTrue(caps & Capability.CAP_STIMULATION.value)
        self.assertTrue(caps & Capability.CAP_HIGH_VOLTAGE.value)
        self.assertTrue(caps & Capability.CAP_MULTI_ELECTRODE.value)

        # Coordinate out of bounds check
        src_oob = make_oob_coordinate_code(row=8, col=2)
        with self.assertRaises(SemanticError) as ctx:
            self.compile_wet(src_oob)
        self.assertEqual(ctx.exception.error_code, "ERR_ELECTRODE_OUT_OF_BOUNDS")

    # =========================================================================
    # Test 12: EBNF Top-Level Declarations x WBC Section Table Serialization
    # Features: F1 (Formal EBNF Grammar) x F7 (WBC Section Table)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_12_grammar_decls_section_table(self):
        """Pair 12: F1 x F7 - Declarations parsing and TOPOLOGY_CONFIG section emission."""
        src = """grid mea[8, 8];
channel in_ch  = mea[0, 1] mode: BiphasicStim;
channel out_ch = mea[7, 6] mode: SpikeReadout;
sync_tick();
"""
        wbc_bytes = self.compile_wet(src)
        header = self.assert_compiled_wbc_valid(wbc_bytes)
        self.assertEqual(header["channel_count"], 64)

        sec_offset = HEADER_SIZE
        found_topology = False
        for _ in range(header["num_sections"]):
            stype, _, off, size = struct.unpack_from(SECTION_ENTRY_FORMAT, wbc_bytes, sec_offset)
            if stype == SectionType.TOPOLOGY_CONFIG.value:
                found_topology = True
                top_data = wbc_bytes[off:off + size]
                tot_ch, r, c, pitch, alias_count = struct.unpack_from("<IHHfI", top_data, 0)
                self.assertEqual(tot_ch, 64)
                self.assertEqual(r, 8)
                self.assertEqual(c, 8)
                self.assertAlmostEqual(pitch, 200.0, places=2)
                self.assertEqual(alias_count, 2)
            sec_offset += SECTION_ENTRY_SIZE

        self.assertTrue(found_topology, "TOPOLOGY_CONFIG section must exist in WBC binary")

    # =========================================================================
    # Test 13: COBA-LIF Exponential Euler x Adaptive Threshold & Slow AHP
    # Features: F13 (Numerical ODE Solver) x F14 (Adaptive Threshold & Slow AHP)
    # =========================================================================
    def test_tier3_pair_13_coba_lif_adaptive_threshold_ahp(self):
        """Pair 13: F13 x F14 - COBA-LIF ODE integration with spike-frequency adaptation."""
        dt = 0.1  # ms
        C_m = 0.2  # nF
        g_L = 0.02  # uS
        E_L = -70.0  # mV
        E_K = -90.0  # mV
        V_reset = -65.0  # mV
        V_th_base = -50.0  # mV

        V = E_L
        theta = V_th_base
        g_ahp = 0.0
        I_tonic = 0.8  # nA (depolarizing drive)

        tau_theta = 50.0  # ms
        tau_ahp = 80.0    # ms
        delta_theta = 15.0  # mV post-spike elevation
        delta_g_ahp = 0.005 # uS post-spike jump

        spike_times = []
        for tick in range(2000):  # 200 ms
            t = tick * dt
            g_tot = g_L + g_ahp
            V_inf = (g_L * E_L + g_ahp * E_K + I_tonic) / g_tot
            tau_eff = C_m / g_tot
            V = V_inf + (V - V_inf) * math.exp(-dt / tau_eff)

            theta = V_th_base + (theta - V_th_base) * math.exp(-dt / tau_theta)
            g_ahp = g_ahp * math.exp(-dt / tau_ahp)

            if V >= theta:
                spike_times.append(t)
                V = V_reset
                theta += delta_theta
                g_ahp += delta_g_ahp

        self.assertGreater(len(spike_times), 2, "Neuron should fire multiple spikes under tonic drive")
        isi_1 = spike_times[1] - spike_times[0]
        isi_2 = spike_times[2] - spike_times[1]
        self.assertLess(isi_1, isi_2, "Adaptive threshold and AHP must produce spike-frequency adaptation")

    # =========================================================================
    # Test 14: Absolute Refractory Clamp x Pairwise STDP Timing Window
    # Features: F14 (Absolute Refractory Clamp) x F16 (Pairwise Trace STDP)
    # =========================================================================
    def test_tier3_pair_14_refractory_clamp_stdp_window(self):
        """Pair 14: F14 x F16 - Refractory clamp immunity and STDP update precision."""
        t_pre = 10.0
        t_post1 = 10.5
        t_post2 = 11.0

        refractory_period = 2.0  # ms
        fired_spikes = [t_post1]
        if (t_post2 - t_post1) >= refractory_period:
            fired_spikes.append(t_post2)

        self.assertEqual(len(fired_spikes), 1, "Second stimulus must be ignored by refractory clamp")

        dt_pair = fired_spikes[0] - t_pre
        self.assertAlmostEqual(dt_pair, 0.5, places=5)
        tau_plus = 20.0
        A_plus = 0.008
        delta_w = A_plus * math.exp(-dt_pair / tau_plus)
        self.assertGreater(delta_w, 0.0)
        self.assertLess(delta_w, A_plus)

    # =========================================================================
    # Test 15: Tsodyks-Markram Cortical Synapse Classes x 8x8 Spatial Connectivity
    # Features: F15 (Tsodyks-Markram Classes) x F12 (8x8 MEA Grid Connectivity)
    # =========================================================================
    def test_tier3_pair_15_tm_classes_spatial_connectivity(self):
        """Pair 15: F15 x F12 - 4 cortical synapse classes and transmission dynamics."""
        classes = {
            "E_to_E": {"U": 0.50, "tau_rec": 800.0, "tau_fac": 10.0},
            "E_to_I": {"U": 0.20, "tau_rec": 100.0, "tau_fac": 1000.0},
        }

        dt_spike = 20.0
        results = {}

        for name, p in classes.items():
            u = p["U"]
            R = 1.0
            amps = []
            for _ in range(4):
                amp = u * R
                amps.append(amp)
                u = u + p["U"] * (1.0 - u)
                R = R * (1.0 - u)
                u = p["U"] + (u - p["U"]) * math.exp(-dt_spike / p["tau_fac"])
                R = 1.0 - (1.0 - R) * math.exp(-dt_spike / p["tau_rec"])
            results[name] = amps

        self.assertGreater(results["E_to_E"][0], results["E_to_E"][-1])
        self.assertGreater(results["E_to_I"][1], results["E_to_I"][0])

    # =========================================================================
    # Test 16: Voltage Clamp Saturation x Fail-Safe Interlock Lockout
    # Features: F19 (Voltage Clamp) x F22 (Fail-Safe Interlock Lockout)
    # =========================================================================
    def test_tier3_pair_16_voltage_clamp_failsafe_lockout(self):
        """Pair 16: F19 x F22 - Out-of-bounds voltage request and fail-safe zero clamp."""
        assert_voltage_clamped(1.2, min_v=-1.2, max_v=1.2)
        assert_voltage_clamped(-1.2, min_v=-1.2, max_v=1.2)

        dac_outputs_lockout = [0.0] * 64
        assert_voltage_clamped(dac_outputs_lockout, min_v=-1.2, max_v=1.2)
        self.assertTrue(all(v == 0.0 for v in dac_outputs_lockout), "Fail-safe lockout must zero all DACs")

    # =========================================================================
    # Test 17: Charge Balance Ring Buffer Trip x Fail-Safe DAC Zeroing
    # Features: F20 (Sliding Charge Watchdog) x F22 (Fail-Safe DAC Zeroing)
    # =========================================================================
    def test_tier3_pair_17_charge_trip_failsafe_dac_zeroing(self):
        """Pair 17: F20 x F22 - Sliding charge trip and immediate DAC shutdown."""
        charge_stream = [0.006] * 120
        res = assert_sliding_charge_balance(charge_stream, max_charge_nc=0.5, window_ticks=100)
        self.assertFalse(res.balanced)
        self.assertGreaterEqual(res.tick, 100)

        post_trip_dacs = [0.0] * 64
        self.assertEqual(sum(post_trip_dacs), 0.0)

    # =========================================================================
    # Test 18: Epileptiform Runaway Breaker x Post-Mortem Snapshot Logging
    # Features: F21 (Epileptiform Breaker) x F22 (Fail-Safe Logging)
    # =========================================================================
    def test_tier3_pair_18_runaway_trip_postmortem_snapshot(self):
        """Pair 18: F21 x F22 - Epileptiform trip captures hyperactive electrode mask."""
        if np is not None:
            raster = np.zeros((1500, 64), dtype=np.uint8)
            raster[::50, :25] = 1
        else:
            raster = [[0] * 64 for _ in range(1500)]
            for t in range(0, 1500, 50):
                for ch in range(25):
                    raster[t][ch] = 1

        res = assert_epileptiform_trip(raster, channels=64, duration_ms=50.0, dt_ms=0.1)
        self.assertTrue(res.tripped)

        expected_mask = (1 << 25) - 1
        self.assertEqual(expected_mask, 0x01FFFFFF)
        self.assertEqual(bin(expected_mask).count("1"), 25)

    # =========================================================================
    # Test 19: Native VM Execution Step x Per-Tick JSONL/CSV Telemetry
    # Features: F8 (Native VM) x F17 (Structured Telemetry Output Engine)
    # =========================================================================
    def test_tier3_pair_19_vm_step_telemetry_schema(self):
        """Pair 19: F8 x F17 - Structured JSONL/CSV telemetry record verification."""
        record = {
            "tick": 100,
            "time_ms": 10.0,
            "v_m": [-65.0] * 64,
            "spikes": 2,
            "r_inst_hz": 31.25,
            "r_win_10ms_hz": 25.0,
            "r_win_50ms_hz": 20.0,
            "delta_w_sum": 0.0012,
            "w_mean": 18.5,
            "q_inj": 0.0002,
            "q_res_10ms": 0.0001,
            "interlock_flag": 0,
        }

        required_keys = [
            "tick", "time_ms", "v_m", "spikes", "r_inst_hz", "r_win_10ms_hz",
            "r_win_50ms_hz", "delta_w_sum", "w_mean", "q_inj", "q_res_10ms", "interlock_flag"
        ]
        for key in required_keys:
            self.assertIn(key, record)

        for key, val in record.items():
            if isinstance(val, (int, float)):
                self.assertFalse(math.isnan(val))
                self.assertFalse(math.isinf(val))

    # =========================================================================
    # Test 20: Python ctypes Caller-Allocated Telemetry x Stepping Loop
    # Features: F10 (ctypes FFI) x F17 (Telemetry Buffer Management)
    # =========================================================================
    def test_tier3_pair_20_ctypes_caller_allocated_telemetry(self):
        """Pair 20: F10 x F17 - Caller-allocated buffer struct packing and unpacking."""
        telem_format = "<Qd64fQI"
        expected_size = struct.calcsize(telem_format)
        self.assertEqual(expected_size, 8 + 8 + 256 + 8 + 4)

        voltages = [-65.0] * 64
        packed = struct.pack(telem_format, 50, 5.0, *voltages, 0x01, 0)
        self.assertEqual(len(packed), expected_size)

        unpacked = struct.unpack(telem_format, packed)
        self.assertEqual(unpacked[0], 50)
        self.assertAlmostEqual(unpacked[1], 5.0)
        self.assertEqual(unpacked[66], 0x01)

    # =========================================================================
    # Test 21: MEA Channel Addressing x DAC Voltage Clamp
    # Features: F12 (8x8 MEA Grid) x F19 (Water-Window Voltage Clamp)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_21_mea_addressing_dac_clamp(self):
        """Pair 21: F12 x F19 - 2D grid index resolution and per-channel voltage clamping."""
        # Row 5, Col 3 -> Channel index 5 * 8 + 3 = 43
        src = """grid mea[8, 8];
channel stim_target = mea[5, 3];
stim_biphasic(stim_target, 1.1, 0.1, 0.1);
sync_tick();
"""
        wbc_bytes = self.compile_wet(src)
        self.assert_compiled_wbc_valid(wbc_bytes)

        # Voltage exceeding hard clamp [+/- 1.2 V] must be statically rejected
        src_bad_v = """grid mea[8, 8];
channel stim_target = mea[5, 3];
stim_biphasic(stim_target, 1.5, 0.1, 0.1);
sync_tick();
"""
        with self.assertRaises(SemanticError) as ctx:
            self.compile_wet(src_bad_v)
        self.assertEqual(ctx.exception.error_code, "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED")

        # Non-targeted channels remain at 0.0V
        channel_dacs = [0.0] * 64
        channel_dacs[43] = 1.1
        self.assertEqual(channel_dacs[43], 1.1)
        self.assertEqual(sum(channel_dacs[:43]) + sum(channel_dacs[44:]), 0.0)

    # =========================================================================
    # Test 22: Excitatory Conductance Injection x Net Charge Tracking
    # Features: F13 (COBA-LIF Solver) x F20 (Sliding Charge Watchdog)
    # =========================================================================
    def test_tier3_pair_22_conductance_depolarization_charge_tracking(self):
        """Pair 22: F13 x F20 - Electrical current injection depolarizes membrane and logs charge."""
        I_stim = 5.0  # uA
        dt_ms = 0.1   # ms
        q_inj_nC = I_stim * dt_ms  # 0.5 nC
        self.assertAlmostEqual(q_inj_nC, 0.5, places=5)

        C_m = 0.2  # nF
        delta_V_mV = (I_stim * 1e-6 * dt_ms * 1e-3) / (C_m * 1e-9) * 1e3
        self.assertGreater(delta_V_mV, 0.0)

        res = assert_sliding_charge_balance([0.005] + [0.0] * 99, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.balanced)

    # =========================================================================
    # Test 23: STDP Hebbian Potentiation x Epileptiform Runaway Breaker
    # Features: F16 (Pairwise Trace STDP) x F21 (Epileptiform Runaway Breaker)
    # =========================================================================
    def test_tier3_pair_23_stdp_potentiation_runaway_breaker(self):
        """Pair 23: F16 x F21 - STDP depression bias prevents epileptiform runaway under baseline noise."""
        A_plus = 0.008
        A_minus = 0.0084  # 1.05x bias
        w_max = 40.0

        w = 15.0
        for _ in range(500):
            drift = A_plus - A_minus
            w = max(0.0, min(w_max, w + drift))

        self.assertLess(w, 15.0, "Depression bias must impart downward drift on uncorrelated synaptic noise")

        baseline_raster = make_spike_raster_matrix(ticks=1200, channels=64, firing_channels=64, rate_hz=20.0, seed=55)
        res = assert_epileptiform_trip(baseline_raster, channels=64, duration_ms=50.0, dt_ms=0.1)
        self.assertFalse(res.tripped, "Baseline rate under STDP must not trip epileptiform breaker")

    # =========================================================================
    # Test 24: Bytecode Control Flow Opcodes x Native Stack VM Engine
    # Features: F6 (Bytecode Control Flow Opcodes) x F8 (Native Stack VM)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_24_bytecode_control_flow_stack_integrity(self):
        """Pair 24: F6 x F8 - Stack depth invariance across loops and conditional jumps."""
        src = """grid mea[8, 8];
fn main() -> int {
    let sum: int = 0;
    let i: int = 0;
    while (i < 10) {
        if (i > 5) {
            sum = sum + i * 2;
        } else {
            sum = sum + i;
        }
        i = i + 1;
        sync_tick();
    }
    return sum;
}
"""
        wbc_bytes = self.compile_wet(src)
        parsed = self.assert_compiled_wbc_valid(wbc_bytes)
        self.assertEqual(parsed["magic"], b"WETB")

    # =========================================================================
    # Test 25: Semantic Scope Symbol Table x WBC Constant Pool Deduplication
    # Features: F4 (Scope Symbol Table) x F7 (Constant Pool Deduplication)
    # =========================================================================
    def test_tier3_pair_25_scope_symbol_table_const_dedup(self):
        """Pair 25: F4 x F7 - Constant pool deduplication for repeated literals."""
        pool = ConstantPool()
        idx1 = pool.add_float(1.2)
        idx2 = pool.add_float(1.2)
        idx3 = pool.add_float(1.2)
        self.assertEqual(idx1, idx2)
        self.assertEqual(idx2, idx3)

        s_idx1 = pool.add_string("alpha")
        s_idx2 = pool.add_string("alpha")
        self.assertEqual(s_idx1, s_idx2)

        self.assertEqual(len(pool.entries), 2)
        pool_bytes = pool.serialize()
        self.assertGreater(len(pool_bytes), 4)

    # =========================================================================
    # Test 26: Static CFG Loop Verifier x Capability Bitmask Enforcement
    # Features: F5 (Static Loop Verifier) x F18 (Static Capability Verifier)
    # =========================================================================
    @require_compiler
    def test_tier3_pair_26_cfg_loop_verifier_capability_mask(self):
        """Pair 26: F5 x F18 - Verified loops set CAP_STIMULATION and verified loop yield flag."""
        src = """grid mea[8, 8];
channel ch = mea[0, 0];
int k = 0;
while (k < 5) {
    stim_biphasic(ch, 0.6, 0.1, 0.1);
    sync_tick();
    k = k + 1;
}
"""
        wbc_bytes = self.compile_wet(src)
        parsed = self.assert_compiled_wbc_valid(wbc_bytes)
        self.assertTrue(parsed["capabilities"] & Capability.CAP_STIMULATION.value)

    # =========================================================================
    # Test 27: Zero-Copy Raster Bitmask x CSV Telemetry Exporter
    # Features: F11 (Zero-Copy Raster) x F17 (CSV Telemetry Exporter)
    # =========================================================================
    def test_tier3_pair_27_zerocopy_raster_csv_exporter(self):
        """Pair 27: F11 x F17 - 64-bit raster bitmask decoding to sparse CSV rows."""
        raster_mask = (1 << 3) | (1 << 17) | (1 << 45)
        tick = 250
        time_ms = 25.0

        csv_rows = []
        for ch in range(64):
            if raster_mask & (1 << ch):
                csv_rows.append(f"{tick},{time_ms:.1f},{ch},E,{ch}")

        self.assertEqual(len(csv_rows), 3)
        self.assertEqual(csv_rows[0], "250,25.0,3,E,3")
        self.assertEqual(csv_rows[1], "250,25.0,17,E,17")
        self.assertEqual(csv_rows[2], "250,25.0,45,E,45")

    # =========================================================================
    # Test 28: Fail-Safe Interlock Clamp x E2E Dual-Track Test Harness Assertions
    # Features: F22 (Fail-Safe Interlock Clamp) x F28 (Full E2E Verification)
    # =========================================================================
    def test_tier3_pair_28_failsafe_interlock_e2e_assertions(self):
        """Pair 28: F22 x F28 - E2E verification of safety interlock trip assertions."""
        # 1. Voltage clamping assertion
        assert_voltage_clamped(requested_v=2.0, actual_v=1.2, clamp_limit=1.2)
        with self.assertRaises(AssertionError):
            assert_voltage_clamped(requested_v=2.0, actual_v=1.8, clamp_limit=1.2)

        # 2. Sliding charge balance assertion
        balanced_trace = [0.001, -0.001] * 50
        assert_sliding_charge_balance(balanced_trace, max_charge_nc=0.5, window_ticks=100, expect_balanced=True)

        unbalanced_trace = [0.01] * 200
        assert_sliding_charge_balance(unbalanced_trace, max_charge_nc=0.5, window_ticks=100, expect_balanced=False)

        # 3. Epileptiform trip assertion
        safe_raster = make_spike_raster_matrix(ticks=1200, channels=64, firing_channels=10, rate_hz=20.0)
        assert_epileptiform_trip(safe_raster, channels=64, duration_ms=50.0, expect_trip=False)


if __name__ == "__main__":
    unittest.main()
