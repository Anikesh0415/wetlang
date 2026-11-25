"""Project Janus Round-2 Remediation Regression Suite.

Covers every defect and edge case uncovered across Bots 1-5:
1. Option 1 (Biophysics, Gym & FEP):
   - WetworldGymEnv 1 <= channel_count <= 64 bounds validation
   - Multi-tick window_spike_counts accumulation across steps_per_action > 1
   - BiophysicalSafetyClamp.calculate_safe_transient_voltage_magnitude() (0.40 V healthy / 0.005 V degraded EIS)
   - Genuine non-constant Shannon neural entropy in run_pong_fep and run_cartpole_fep
2. Option 3 (Neuromorphic Silicon Backends & Emitter):
   - Loihi-2 & SpiNNaker real execution (>0 spikes from stim_biphasic, accurate read_spikes sum)
   - connect A[0] -> B[0] index, weight, and 500us -> 0.5 ms delay preservation
   - StreamDeclNode SubstrateUnsupportedOpWarning + bounded lowering
   - Water-window 1.8V safe no-op suppression without emitting stim
   - Opcode.STIM_CURRENT emission for 1nA stimulation
3. Option 4 (Compiler Linter, CLI & VS Code Extension):
   - wetlang check --format=json fail-closed on grid huge[300,300]
   - --stdin --filename unsaved buffer + UTF-8 BOM
   - Interprocedural call-graph ERR_UNBOUNDED_STIM_LOOP: while (y < 10) { zap(); y = y + 1; }
   - Negative loop counter init: let mut x = -5000; while (x < 10) { x = x + 1; }
   - Dimensional mixing (100mV + 5.0) and asymmetric Phase 2 (1000ms) charge violation
   - vscode-wetlang/src/extension.ts + out/extension.js execFile (shell: false, zero cp.exec() + --stdin)
4. Systems & Interlocks (C99 Runtime, HAL, AER, Scheduler):
   - ctypes.sizeof(WetHalContext) == 2312
   - NaN / +inf / -inf fail-closed voltage, charge, and compliance interlock checks
   - wet_aer_push ch >= 64 -> -4 drop, post-window quarantine recovery, and 100.0 mV -> 32767 NEO saturation
   - WetStatus.WET_ERR_QUEUE_EMPTY == 28 on empty scheduler telemetry poll
   - wet_scheduler tick-0 immediate stimulus preservation
"""

import ctypes
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import warnings
from pathlib import Path

import numpy as np
import pytest

from bindings.aer import WetAERPacket, WetAERRing, WetNEODetector
from bindings.ffi import WetHalContext, WetStatus, WetVMConfig, load_wetvm_lib
from bindings.scheduler import WetScheduler, WetSchedulerConfig, WetStimCommand
from benchmarks.run_cartpole_fep import CartPoleFEPAgent
from benchmarks.run_pong_fep import ActiveInferenceFEPAgent
from compiler.emitter import (
    SubstrateUnsupportedOpWarning,
    compile_source,
    compile_to_loihi2,
    compile_to_spinnaker,
    disassemble,
)
from sandbox.gym_env import BiophysicalSafetyClamp
from wetlang.gym import WetworldGymEnv

REPO_ROOT = Path(__file__).resolve().parent.parent
VSCODE_DIR = REPO_ROOT / "vscode-wetlang"


# =========================================================================
# 1. Option 1: Gym Bounds, Multi-Tick Spikes, Transient EIS & FEP Entropy
# =========================================================================

def test_gym_channel_count_bounds_guard():
    """WetworldGymEnv enforces 1 <= channel_count <= 64."""
    for bad in (0, -1, 65, 128):
        with pytest.raises(ValueError):
            env_bad = WetworldGymEnv(channel_count=bad)
            env_bad.close()

    for ok in (1, 64):
        env = WetworldGymEnv(channel_count=ok)
        try:
            assert env.channel_count == ok
            assert env.observation_space.shape == (ok * 2,)
        finally:
            env.close()


def test_gym_multi_tick_window_spike_accumulation():
    """steps_per_action > 1 accumulates spikes across all ticks rather than reading only the final tick."""
    env = WetworldGymEnv(steps_per_action=25, channel_count=64)
    try:
        obs0, _ = env.reset(seed=42)
        assert obs0.shape == (128,)

        # Strong sustained sensory stimulation across multiple steps to drive spikes
        total_window_spikes = 0
        total_obs_spikes = 0.0
        for _ in range(10):
            obs, _, terminated, truncated, info = env.step(np.array([0.8, -0.8, 0.8, -0.8], dtype=np.float32))
            assert info["executed_ticks"] == 25
            win_counts = env.window_spike_counts
            assert win_counts.shape == (64,)
            assert win_counts.dtype == np.uint32
            total_window_spikes += int(win_counts.sum())
            total_obs_spikes += float(obs[64:].sum())
            # Window counts can exceed binary presence (multi-spike bursts in 25 ticks)
            assert int(win_counts.sum()) >= int(obs[64:].sum())
            if terminated or truncated:
                break

        assert total_window_spikes > 0
        assert total_obs_spikes > 0.0
    finally:
        env.close()


def test_biophysical_safety_clamp_transient_voltage_healthy_vs_degraded():
    """BiophysicalSafetyClamp computes 0.40 V healthy vs 0.005 V degraded EIS transient magnitudes."""
    healthy = BiophysicalSafetyClamp(
        electrode_area_um2=5000.0,
        z_magnitude_ohms=100000.0,
        cic_mc_cm2=0.10,
        q_shannon_nc=0.40,
    )
    assert healthy.calculate_safe_transient_voltage_magnitude(phase_ms=0.1) == pytest.approx(0.40, rel=1e-6)

    degraded = BiophysicalSafetyClamp(
        electrode_area_um2=5000.0,
        z_magnitude_ohms=1250.0,
        cic_mc_cm2=0.10,
        q_shannon_nc=0.40,
    )
    assert degraded.calculate_safe_transient_voltage_magnitude(phase_ms=0.1) == pytest.approx(0.005, rel=1e-6)
    assert abs(degraded.clamp_biphasic_voltage(0.5, phase_ms=0.1)) == pytest.approx(0.005, rel=1e-6)


@pytest.mark.parametrize("agent_cls,kin_dim", [
    (ActiveInferenceFEPAgent, 5),
    (CartPoleFEPAgent, 4),
])
def test_fep_agents_real_non_constant_neural_shannon_entropy(agent_cls, kin_dim):
    """FEP agents compute real non-constant Shannon entropy across 64 MEA channels."""
    agent = agent_cls()
    state = np.zeros(kin_dim + 128, dtype=np.float32)

    # Zero neural activity -> 0.0 bits
    h_zero = agent._compute_neural_shannon_entropy(state, spike_counts=np.zeros(64), kin_dim=kin_dim)
    assert h_zero == pytest.approx(0.0, abs=1e-9)

    # Single-channel concentrated spikes -> 0.0 bits
    spk_single = np.zeros(64, dtype=np.float32)
    spk_single[0] = 10.0
    h_single = agent._compute_neural_shannon_entropy(state, spike_counts=spk_single, kin_dim=kin_dim)
    assert h_single == pytest.approx(0.0, abs=1e-6)

    # Uniform broadband 64-channel spikes -> log2(64) = 6.0 bits
    spk_uniform = np.ones(64, dtype=np.float32)
    h_uniform = agent._compute_neural_shannon_entropy(state, spike_counts=spk_uniform, kin_dim=kin_dim)
    assert h_uniform == pytest.approx(6.0, rel=1e-4)

    f_low = agent.compute_variational_free_energy(state, spike_counts=spk_single, prediction_error=0.01)
    f_high = agent.compute_variational_free_energy(state, spike_counts=spk_uniform, prediction_error=0.25)
    assert f_high > f_low + 5.0


# =========================================================================
# 2. Option 3: Loihi-2 & SpiNNaker Real Execution, Delays, Warnings, STIM_CURRENT
# =========================================================================

@pytest.mark.parametrize("target", ["loihi2", "spinnaker"])
def test_neuromorphic_real_spiking_and_read_spikes(target):
    """Emitted Loihi-2 & SpiNNaker scripts produce >0 spikes from stim_biphasic and accurate read_spikes sum."""
    src = """
    organoid Org {
        cells: 16;
    }
    grid mea[8, 8];
    channel ch0 = mea[0, 0];

    fn main() {
        stim_biphasic(ch0, 1.0V, 0.5ms, 0.5ms);
        sync_tick(50);
        let s = read_spikes(ch0, 10.0ms);
    }
    """
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        py_code = compile_source(src, target=target)

    ns = {"__name__": f"test_{target}_real_exec"}
    exec(compile(py_code, f"<{target}>", "exec"), ns)
    result = ns["main"]()

    if target == "loihi2":
        total_spikes = sum(sum(1 for x in step if x > 0.0) for step in result.spikes)
        assert total_spikes > 0
        # read_spikes expression on ch0 (index 0) must evaluate cleanly
        ch0_spikes = sum(1 for _s in result.spikes[-100:] if _s[0 % result.n_neurons] > 0.0)
        assert ch0_spikes > 0
    else:
        spiketrains = result.segments[0].spiketrains
        total_spikes = sum(len(st) for st in spiketrains)
        assert total_spikes > 0
        assert len(spiketrains[0]) > 0


@pytest.mark.parametrize("target", ["loihi2", "spinnaker"])
def test_neuromorphic_connect_index_weight_and_us_delay_preservation(target):
    """connect A[0] -> B[0] preserves channel indices, weight, and 500us -> 0.5 ms conversion."""
    src = """
    organoid A { cells: 8; }
    organoid B { cells: 8; }
    connect A[0] -> B[0] with { weight: 0.75; delay: 500us; plasticity: stdp; };
    fn main() {
        sync_tick(2);
    }
    """
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        py_code = compile_source(src, target=target)

    if target == "loihi2":
        assert "add_projection(a, pre_idx=0, post_idx=0, weight=0.75, delay_steps=5, stdp_enabled=True)" in py_code
    else:
        assert "FromListConnector([(0 % a.size, 0 % b.size," in py_code
        assert "0.5000" in py_code
        assert "delay=0.5000" in py_code


@pytest.mark.parametrize("target", ["loihi2", "spinnaker"])
def test_neuromorphic_stream_decl_warning_and_bounded_lowering(target):
    """StreamDeclNode emits SubstrateUnsupportedOpWarning and lowers to bounded 100-tick loop."""
    src = """
    organoid Org { cells: 8; }
    stream closed {
        cycle {
            sync_tick();
        }
    }
    fn main() {
        sync_tick();
    }
    """
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        py_code = compile_source(src, target=target)

    stream_warns = [w for w in caught if issubclass(w.category, SubstrateUnsupportedOpWarning) and "stream" in str(w.message)]
    assert len(stream_warns) >= 1
    assert "W_SUBSTRATE_UNSUPPORTED_OP: bounded lowering of stream 'closed'" in py_code
    assert "for _stream_tick in range(100):" in py_code


@pytest.mark.parametrize("target", ["loihi2", "spinnaker"])
def test_neuromorphic_water_window_1800mv_suppressed_without_stim(target):
    """1.8V stim triggers SubstrateUnsupportedOpWarning and suppresses stimulation emission."""
    src = """
    organoid Org { cells: 8; }
    grid mea[8, 8];
    channel ch0 = mea[0, 0];
    fn main() {
        stim_biphasic(ch0, 1.8V, 0.2ms, 0.2ms);
        sync_tick();
    }
    """
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        py_code = compile_to_loihi2(src) if target == "loihi2" else compile_to_spinnaker(src)

    ww_warns = [
        w for w in caught
        if issubclass(w.category, SubstrateUnsupportedOpWarning) and "electrochemical_water_window" in str(w.message)
    ]
    assert len(ww_warns) >= 1
    assert "# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for electrochemical water-window guard" in py_code
    assert "inject_stimulus" not in py_code
    assert "SpikeSourceArray" not in py_code


def test_emitter_1na_emits_opcode_stim_current():
    """Current-mode 1nA stimulation emits Opcode.STIM_CURRENT in WBC bytecode."""
    src = """
    grid mea[8, 8];
    channel ch0 = mea[0, 0];
    fn main() {
        stim_biphasic(ch0, 1nA, 0.2ms, 0.2ms);
        sync_tick();
    }
    """
    wbc = compile_source(src, target="sim")
    asm = disassemble(wbc)
    assert "STIM_CURRENT" in asm


# =========================================================================
# 3. Option 4: Linter Fail-Closed, --stdin + BOM, Call-Graph, Negative Loop, VS Code
# =========================================================================

def _run_cli_check(args, stdin_text=None):
    cmd = [sys.executable, "-m", "wetlang.cli", "check", "--format=json", *args]
    return subprocess.run(
        cmd,
        input=stdin_text,
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=str(REPO_ROOT),
    )


def test_cli_check_fail_closed_on_invalid_grid_300x300():
    """wetlang check --format=json fails closed (exit 1 + error JSON) on grid huge[300,300]."""
    src = "grid huge[300, 300];\nfn main() { sync_tick(); }\n"
    res = _run_cli_check(["--stdin", "--filename", "unsaved_grid.wet"], stdin_text=src)
    assert res.returncode == 1
    diags = json.loads(res.stdout)
    assert len(diags) >= 1
    assert any(d["code"] == "ERR_INVALID_GRID_DIMENSIONS" and d["severity"] == "error" for d in diags)


def test_cli_check_stdin_filename_unsaved_buffer_with_utf8_bom():
    """--stdin --filename handles UTF-8 BOM and reports diagnostics against the supplied virtual filename."""
    vname = r"C:\tmp\my dir\unsaved buffer.wet"

    ok_src = "\ufeffgrid mea[8, 8];\nchannel ch0 = mea[0, 0];\nfn main() { sync_tick(); }\n"
    res_ok = _run_cli_check(["--stdin", "--filename", vname], stdin_text=ok_src)
    assert res_ok.returncode == 0
    assert json.loads(res_ok.stdout) == []

    bad_src = "\ufeffgrid mea[8, 8];\nchannel ch0 = mea[0, 0];\nfn main() { stim_biphasic(ch0, 2.0V, 0.2ms, 0.2ms); sync_tick(); }\n"
    res_bad = _run_cli_check(["--stdin", "--filename", vname], stdin_text=bad_src)
    assert res_bad.returncode == 1
    diags = json.loads(res_bad.stdout)
    assert any(d["code"] == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED" and d["file"] == vname for d in diags)


def test_cli_check_interprocedural_call_graph_unbounded_stim_loop():
    """while (y < 10) { zap(); y = y + 1; } is caught via call-graph ERR_UNBOUNDED_STIM_LOOP."""
    src = """
    grid mea[8, 8];
    channel c = mea[0, 0];
    fn zap() {
        stim_biphasic(c, 0.5V, 0.2ms, 0.2ms);
    }
    fn main() {
        let mut y = 0;
        while (y < 10) {
            zap();
            y = y + 1;
        }
    }
    """
    res = _run_cli_check(["--stdin", "--filename", "callgraph.wet"], stdin_text=src)
    assert res.returncode == 1
    diags = json.loads(res.stdout)
    assert any(d["code"] == "ERR_UNBOUNDED_STIM_LOOP" for d in diags)


def test_cli_check_negative_loop_counter_init_and_dim_mix_and_asym_phase2():
    """Checks negative loop init (-5000), 100mV + 5.0 dimension mixing, and asymmetric 1000ms Phase 2."""
    neg_src = """
    fn main() {
        let mut x = -5000;
        while (x < 10) {
            x = x + 1;
        }
    }
    """
    res_neg = _run_cli_check(["--stdin", "--filename", "neg.wet"], stdin_text=neg_src)
    assert res_neg.returncode == 1
    assert any(d["code"] == "ERR_UNSYNCED_LOOP" for d in json.loads(res_neg.stdout))

    mix_src = "fn main() { let v = 100mV + 5.0; sync_tick(); }\n"
    res_mix = _run_cli_check(["--stdin", "--filename", "mix.wet"], stdin_text=mix_src)
    assert res_mix.returncode == 1
    assert any(d["code"] == "ERR_DIMENSIONAL_MISMATCH" for d in json.loads(res_mix.stdout))

    asym_src = """
    grid mea[8, 8];
    channel c = mea[0, 0];
    fn main() {
        stim_biphasic(c, 1nA, 0.1ms, 1000ms);
        sync_tick();
    }
    """
    res_asym = _run_cli_check(["--stdin", "--filename", "asym.wet"], stdin_text=asym_src)
    assert res_asym.returncode == 1
    assert any(d["code"] == "ERR_CHARGE_LIMIT_VIOLATION" for d in json.loads(res_asym.stdout))


def test_vscode_extension_uses_execfile_shell_false_and_stdin():
    """Static audit: both src/extension.ts and out/extension.js use execFile (shell: false), --stdin, zero cp.exec(."""
    for rel in ("src/extension.ts", "out/extension.js"):
        txt = (VSCODE_DIR / rel).read_text(encoding="utf-8")
        assert "cp.execFile(" in txt, f"{rel} missing cp.execFile("
        assert "cp.exec(" not in txt, f"{rel} still uses unsafe cp.exec("
        assert "shell: false" in txt, f"{rel} missing shell: false"
        assert "'--stdin'" in txt, f"{rel} missing --stdin flag"
        assert "'--filename'" in txt, f"{rel} missing --filename flag"
        assert "python3" in txt and "python" in txt, f"{rel} missing cross-platform python candidates"


# =========================================================================
# 4. Systems & Interlocks: WetHalContext ABI, NaN Interlocks, AER, Scheduler
# =========================================================================

def test_wet_hal_context_abi_sizeof_2312():
    """WetHalContext ctypes structure matches C sizeof(struct wet_hal_context) == 2312."""
    assert ctypes.sizeof(WetHalContext) == 2312


def test_interlocks_nan_inf_fail_closed_dll():
    """Exported C99 interlock voltage clamps reject NaN/+inf/-inf fail-closed to 0.0 V."""
    lib = load_wetvm_lib()
    lib.interlocks_clamp_voltage.restype = ctypes.c_float
    lib.interlocks_clamp_voltage.argtypes = [ctypes.c_void_p, ctypes.c_float]
    out_v = ctypes.c_float(99.0)

    for bad_val in (float("nan"), float("inf"), float("-inf")):
        assert lib.interlocks_clamp_voltage(None, ctypes.c_float(bad_val)) == 0.0
        assert lib.interlocks_clamp_voltage_dynamic(None, ctypes.c_uint8(0), ctypes.c_float(bad_val)) == 0.0
        out_v.value = 99.0
        tripped = lib.wet_interlock_check_voltage(None, ctypes.c_uint8(0), ctypes.c_float(bad_val), ctypes.byref(out_v))
        assert tripped == 1
        assert out_v.value == 0.0


def test_interlocks_nan_inf_charge_and_compliance_c99_harness():
    """Compile-time C99 probe verifying interlocks_record_charge_tick and interlocks_check_compliance reject NaN/Inf."""
    from native.build import build_with_clang

    clang = r"C:\Program Files\LLVM\bin\clang.exe"
    if not os.path.isfile(clang):
        clang = shutil.which("clang")
    if not clang:
        pytest.skip("clang not available for internal interlocks.c probe")

    c_src = r"""
    #include "wet_crt.h"
    #include "interlocks.h"

    #ifdef _WIN32
    int _fltused = 1;
    #endif

    static float make_nan(void) {
        union { uint32_t u; float f; } v = { 0x7FC00000U };
        return v.f;
    }
    static float make_pos_inf(void) {
        union { uint32_t u; float f; } v = { 0x7F800000U };
        return v.f;
    }
    static float make_neg_inf(void) {
        union { uint32_t u; float f; } v = { 0xFF800000U };
        return v.f;
    }

    WET_EXPORT int run_nan_probe(void) {
        interlock_state_t il;
        float charges[INTERLOCK_NUM_CHANNELS];
        for (int i = 0; i < INTERLOCK_NUM_CHANNELS; ++i) charges[i] = 0.0f;

        interlocks_init(&il);
        charges[0] = make_nan();
        wet_status_t st_nan_q = interlocks_record_charge_tick(&il, 1, charges);
        if (st_nan_q != WET_ERR_CHARGE_IMBALANCE || il.locked != 1) return 10;

        interlocks_init(&il);
        charges[0] = make_pos_inf();
        wet_status_t st_inf_q = interlocks_record_charge_tick(&il, 2, charges);
        if (st_inf_q != WET_ERR_CHARGE_IMBALANCE || il.locked != 1) return 11;

        interlocks_init(&il);
        wet_status_t st_nan_c = interlocks_check_compliance(&il, 3, 0, make_nan());
        if (st_nan_c != WET_ERR_COMPLIANCE_RAILED || il.locked != 1) return 12;

        interlocks_init(&il);
        wet_status_t st_inf_c = interlocks_check_compliance(&il, 4, 0, make_neg_inf());
        if (st_inf_c != WET_ERR_COMPLIANCE_RAILED || il.locked != 1) return 13;

        return 0;
    }
    """
    lib_ext = ".dll" if sys.platform == "win32" else (".dylib" if sys.platform == "darwin" else ".so")
    with tempfile.TemporaryDirectory(prefix="wet_nan_il_", ignore_cleanup_errors=True) as tmp:
        src_p = Path(tmp) / "probe.c"
        dll_p = Path(tmp) / f"probe{lib_ext}"
        src_p.write_text(c_src, encoding="utf-8")
        ok = build_with_clang(
            clang,
            [src_p, REPO_ROOT / "native" / "src" / "interlocks.c"],
            REPO_ROOT / "native" / "include",
            dll_p,
        )
        assert ok, "Failed to build interlocks NaN probe DLL with clang"
        probe_dll = ctypes.CDLL(str(dll_p))
        try:
            probe_dll.run_nan_probe.restype = ctypes.c_int
            assert probe_dll.run_nan_probe() == 0
        finally:
            if os.name == "nt":
                import _ctypes
                _ctypes.FreeLibrary(probe_dll._handle)


def test_wet_aer_bounds_drop_quarantine_recovery_and_neo_saturation():
    """wet_aer_push rejects ch>=64 (-4), recovers after 1s window rollover, and NEO saturates 100mV -> 32767."""
    lib = load_wetvm_lib()
    ring = WetAERRing(capacity=1024, burst_limit_max_hz=5000000, num_channels=64)

    # Out-of-bounds channel >= 64 must return -4 and increment total_dropped
    rc_oob = lib.wet_aer_push(ctypes.byref(ring._c_ring), ctypes.c_uint64(100), ctypes.c_uint32(64), ctypes.c_int16(-100), ctypes.c_uint16(1))
    assert rc_oob == -4
    assert ring._c_ring.total_dropped == 1

    # Quarantine noisy channel 5 (> 250 Hz in same 1-second window)
    for _ in range(251):
        assert ring.push(tick=100, channel=5, amp_uv=-100, flags=1) is True
    rc_quar = lib.wet_aer_push(ctypes.byref(ring._c_ring), ctypes.c_uint64(100), ctypes.c_uint32(5), ctypes.c_int16(-100), ctypes.c_uint16(1))
    assert rc_quar == -3

    # Advance past 1-second window (> 10000 ticks at 0.1 ms) -> channel 5 recovers
    assert ring.push(tick=10102, channel=5, amp_uv=-100, flags=1) is True

    # NEO 100.0 mV spike -> amp_uv saturates cleanly at +32767
    det_ring = WetAERRing(capacity=64, burst_limit_max_hz=5000000, num_channels=64)
    det = WetNEODetector(num_channels=64, threshold_mult=2.0, refract_ticks=5)
    for t in range(10):
        det.process_sample(channel=0, voltage=0.0, current_tick=t, ring=det_ring)
    # Prime baseline at 0.0 then apply a 100.0 mV step across ticks 11-12 so v_curr > 32.767 mV at peak Psi
    det.process_sample(channel=0, voltage=100.0, current_tick=11, ring=det_ring)
    spiked = det.process_sample(channel=0, voltage=100.0, current_tick=12, ring=det_ring)
    assert spiked is True
    pkts = det_ring.pop_batch(8)
    assert len(pkts) >= 1
    assert pkts[0][2] == 32767
    det.close()


def test_scheduler_queue_empty_and_tick0_stim_preservation():
    """wet_scheduler_poll_telemetry returns WET_ERR_QUEUE_EMPTY (28) when empty; tick-0 stim is preserved."""
    lib = load_wetvm_lib()
    assert int(WetStatus.WET_ERR_QUEUE_EMPTY) == 28

    arena_bytes = 512 * 1024
    vm_arena = (ctypes.c_uint8 * arena_bytes)()
    vm_cfg = WetVMConfig(dt_ms=0.1, max_stack_depth=1024, max_locals=256, channel_count=64, max_ops_per_tick=100000)
    vm = lib.wet_create_vm_arena(vm_arena, arena_bytes, ctypes.byref(vm_cfg))
    assert vm is not None

    try:
        sched_cfg = WetSchedulerConfig(
            target_period_us=10,
            enable_core_pinning=False,
            enable_priority_elevation=False,
        )
        sched = WetScheduler(vm, config=sched_cfg, lib=lib)
        try:
            # Empty telemetry poll must return WET_ERR_QUEUE_EMPTY (28)
            assert sched.poll_telemetry() is None
            from bindings.ffi import WetTelemetry
            telem_tmp = WetTelemetry()
            rc_poll = lib.wet_scheduler_poll_telemetry(sched.handle, ctypes.byref(telem_tmp))
            assert rc_poll == int(WetStatus.WET_ERR_QUEUE_EMPTY)

            # Push an immediate stimulus BEFORE tick 0 and verify it is injected & preserved
            cmd = WetStimCommand(channel=2, voltage_v=0.6, phase1_ms=0.2, phase2_ms=0.2, tick_scheduled=0)
            assert lib.wet_scheduler_push_stimulus(sched.handle, ctypes.byref(cmd)) == int(WetStatus.WET_OK)

            rc_step = lib.wet_scheduler_step(sched.handle)
            assert rc_step == int(WetStatus.WET_OK)
            stats = sched.get_stats()
            assert stats.total_ticks == 1
            assert stats.stimuli_injected == 1

            polled = sched.poll_telemetry()
            assert polled is not None
            assert polled.current_tick == 1
            assert polled.last_charge_nc[2] != 0.0
        finally:
            sched.destroy()
    finally:
        lib.wet_free_vm(vm)
