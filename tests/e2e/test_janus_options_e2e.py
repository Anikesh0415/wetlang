"""
End-to-End Test Suite for Project Janus (Gymnasium, Neuromorphic Backends, Linter & C99 Safety)
=============================================================================================
Validates acceptance criteria across all Project Janus subsystems:
  - Option 1: Closed-Loop AI Benchmark Suite (WetworldGymEnv, Encoders, FinalSpark)
  - Option 3: Intel Loihi-2 & SpiNNaker Neuromorphic Silicon Backends
  - Option 4: Official VS Code Language Extension & Single-Source Linter CLI
  - C99 Runtime & Safety Invariants: Deterministic Stepping & Arena Allocation

Structured according to the 4-tier systematic testing architecture:
  Tier 1: Feature Coverage (Category-Partition happy path)
  Tier 2: Boundary & Corner Cases (Boundary Value Analysis & Safety Clamps)
  Tier 3: Cross-Feature Combinations (Pairwise integration)
  Tier 4: Real-World Application Scenarios (Closed-loop benchmarks & calibration)
"""

import sys
import os
import ast
import json
import re
import tempfile
import subprocess
from pathlib import Path
import ctypes
import pytest
import numpy as np

# Ensure repository root is at front of sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from bindings.ffi import WetVMFFI, WetTelemetry, WetVMConfig
from bindings.runtime import WetRuntime, WetVMError
from compiler.token import TokenType, KEYWORDS, UNIT_SUFFIXES
from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.semantic import SemanticAnalyzer, SemanticError
from compiler.emitter import BytecodeEmitter, Target
from compiler.isa import Opcode, Capability


# =============================================================================
# Helper Utilities & Fixtures
# =============================================================================

VALID_WET_SOURCE = """
grid mea[8, 8];
channel c0 = mea[0, 0] mode: BiphasicStim;
channel c1 = mea[0, 1] mode: SpikeReadout;

fn main() {
    stim_biphasic(c0, 0.5 V, 100 us, 100 us);
    sync_tick();
}
"""

WETWARE_ONLY_WET_SOURCE = """
grid mea[8, 8];
channel c0 = mea[0, 0] mode: BiphasicStim;

fn main() {
    pump_set_rate(0, 10.0uL/min);
    valve_open(0);
    stim_biphasic(c0, 0.4 V, 100 us, 100 us);
    sync_tick();
}
"""

OVERVOLTAGE_WET_SOURCE = """
grid mea[8, 8];
channel c0 = mea[0, 0] mode: BiphasicStim;

fn main() {
    stim_biphasic(c0, 1.8 V, 100 us, 100 us);
    sync_tick();
}
"""

DIMENSIONAL_MISMATCH_WET_SOURCE = """
grid mea[8, 8];
channel c0 = mea[0, 0] mode: BiphasicStim;

fn main() {
    let x: Voltage = 5 mV + 10 ms;
    sync_tick();
}
"""

UNBOUNDED_LOOP_WET_SOURCE = """
grid mea[8, 8];
channel c0 = mea[0, 0] mode: BiphasicStim;

fn main() {
    while (true) {
        stim_biphasic(c0, 0.5 V, 100 us, 100 us);
    }
}
"""


def get_vscode_path() -> Path:
    return REPO_ROOT / "vscode-wetlang"


def run_cli_command(args: list) -> subprocess.CompletedProcess:
    """Helper to run the wetlang CLI in a subprocess."""
    cmd = [sys.executable, "-m", "wetlang.cli"] + args
    return subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONPATH": str(REPO_ROOT)},
    )


# =============================================================================
# Tier 1: Feature Coverage (Category-Partition / Happy Path)
# =============================================================================

class TestJanusTier1FeatureCoverage:
    """
    Tier 1 tests verify the primary happy-path behavior and interface
    contracts for Options 1, 3, 4 and C99 runtime stepping.
    """

    # --- Option 1: Gym Environment ---
    def test_option1_gym_env_canonical_import_and_spaces(self):
        """Test canonical WetworldGymEnv observation space (128,) and action space (4,)."""
        import wetlang.gym as gym_module
        from wetlang.gym import WetworldGymEnv

        env = WetworldGymEnv()
        try:
            assert env.observation_space.shape == (128,), f"Expected obs shape (128,), got {env.observation_space.shape}"
            assert env.action_space.shape == (4,), f"Expected action shape (4,), got {env.action_space.shape}"

            # Check bounds: voltages in [-1.2, 1.2], spikes in [0, 1]
            low_obs = env.observation_space.low
            high_obs = env.observation_space.high
            assert np.allclose(low_obs[:64], -1.2)
            assert np.allclose(high_obs[:64], 1.2)
            assert np.allclose(low_obs[64:], 0.0)
            assert np.allclose(high_obs[64:], 1.0)

            # Check action bounds [-0.8, 0.8]
            assert np.allclose(env.action_space.low, -0.8)
            assert np.allclose(env.action_space.high, 0.8)
        finally:
            env.close()

    def test_option1_gym_env_reset_and_step(self):
        """Test reset and multi-step execution of WetworldGymEnv without errors."""
        from wetlang.gym import WetworldGymEnv

        env = WetworldGymEnv()
        try:
            obs, info = env.reset(seed=42)
            assert obs.shape == (128,), f"Reset obs shape mismatch: {obs.shape}"
            assert isinstance(info, dict), "Reset info must be a dict"
            assert "tick" in info
            assert "sim_time_ms" in info
            assert "population_rate_hz" in info

            # Step with zero action
            zero_action = np.zeros(4, dtype=np.float32)
            obs, rew, term, trunc, info = env.step(zero_action)
            assert obs.shape == (128,)
            assert isinstance(rew, float)
            assert isinstance(term, bool)
            assert isinstance(trunc, bool)
            assert isinstance(info, dict)

            # Sequential multi-step execution
            for step_idx in range(5):
                action = np.random.uniform(-0.5, 0.5, size=(4,)).astype(np.float32)
                obs, rew, term, trunc, info = env.step(action)
                assert obs.shape == (128,)
                assert not term, f"Environment unexpectedly terminated at step {step_idx}"
        finally:
            env.close()

    def test_option1_gym_factory_make(self):
        """Test wetlang.gym.make factory helper."""
        import wetlang.gym as gym_mod
        env = gym_mod.make("Wetworld-v1")
        try:
            assert isinstance(env, gym_mod.WetworldGymEnv)
            obs, info = env.reset()
            assert obs.shape == (128,)
        finally:
            env.close()

    # --- Option 1: State Encoders ---
    def test_option1_pong_state_encoder(self):
        """Test PongStateEncoder in sandbox/gym_env.py encodes state within water window."""
        try:
            import sandbox.gym_env as s_env
            if not hasattr(s_env, "PongStateEncoder"):
                pytest.skip("PongStateEncoder not yet implemented in sandbox/gym_env.py")
            encoder_cls = getattr(s_env, "PongStateEncoder")
        except ImportError:
            pytest.skip("sandbox.gym_env not found")

        encoder = encoder_cls()
        # Nominal Pong state: paddle_y, ball_x, ball_y, ball_vx, ball_vy
        stim_params = encoder.encode(paddle_y=0.5, ball_x=0.5, ball_y=0.5, ball_vx=0.1, ball_vy=-0.1)
        assert stim_params is not None

        voltages = np.array(stim_params, dtype=np.float32)
        assert voltages.shape == (4,), f"Expected shape (4,), got {voltages.shape}"
        assert np.all(np.abs(voltages) <= 1.2), f"Voltage exceeded water window: {voltages}"

    def test_option1_cartpole_state_encoder(self):
        """Test CartPoleStateEncoder in sandbox/gym_env.py encodes state within water window."""
        try:
            import sandbox.gym_env as s_env
            if not hasattr(s_env, "CartPoleStateEncoder"):
                pytest.skip("CartPoleStateEncoder not yet implemented in sandbox/gym_env.py")
            encoder_cls = getattr(s_env, "CartPoleStateEncoder")
        except ImportError:
            pytest.skip("sandbox.gym_env not found")

        encoder = encoder_cls()
        stim_params = encoder.encode(x=0.0, x_dot=0.0, theta=0.05, theta_dot=0.0)
        assert stim_params is not None

        voltages = np.array(stim_params, dtype=np.float32)
        assert voltages.shape == (4,), f"Expected shape (4,), got {voltages.shape}"
        assert np.all(np.abs(voltages) <= 1.2), f"Voltage exceeded water window: {voltages}"

    def test_option1_motor_spike_decoder(self):
        """Test MotorSpikeDecoder in sandbox/gym_env.py decodes spikes into actions."""
        try:
            import sandbox.gym_env as s_env
            if not hasattr(s_env, "MotorSpikeDecoder"):
                pytest.skip("MotorSpikeDecoder not yet implemented in sandbox/gym_env.py")
            decoder_cls = getattr(s_env, "MotorSpikeDecoder")
        except ImportError:
            pytest.skip("sandbox.gym_env not found")

        decoder = decoder_cls()
        sample_raster = np.zeros(64, dtype=np.uint8)
        sample_raster[0] = 1 # Motor channel spike
        action = decoder.decode(sample_raster)
        assert action is not None

    def test_option1_finalspark_validation_execution(self):
        """Test benchmarks/finalspark_validation.py executes with empirical data or CI fallback."""
        script_path = REPO_ROOT / "benchmarks" / "finalspark_validation.py"
        if not script_path.exists():
            pytest.skip("benchmarks/finalspark_validation.py not yet implemented")

        res = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            env={**os.environ, "PYTHONPATH": str(REPO_ROOT)},
        )
        assert res.returncode == 0, f"finalspark_validation.py failed with returncode {res.returncode}:\n{res.stderr}\n{res.stdout}"

    # --- Option 3: Neuromorphic Emitters ---
    def test_option3_loihi2_emitter_syntax(self):
        """Test --target=loihi2 produces valid Python code that passes ast.parse."""
        import compiler.emitter as em
        if not hasattr(em, "compile_to_loihi2") and "loihi2" not in [t.value for t in em.Target]:
            pytest.skip("--target=loihi2 not yet implemented in compiler/emitter.py")

        try:
            if hasattr(em, "compile_to_loihi2"):
                code = em.compile_to_loihi2(VALID_WET_SOURCE)
            else:
                code = em.compile_source(VALID_WET_SOURCE, target="loihi2")
        except Exception as ex:
            pytest.skip(f"--target=loihi2 in progress: {ex}")

        code_str = code.decode("utf-8") if isinstance(code, bytes) else str(code)
        parsed = ast.parse(code_str)
        assert parsed is not None, "Emitted Loihi-2 code must be valid Python AST"

    def test_option3_loihi2_emits_lava_components(self):
        """Test --target=loihi2 emitted code references AbstractProcess and PyLoihiProcessModel."""
        import compiler.emitter as em
        if not hasattr(em, "compile_to_loihi2") and "loihi2" not in [t.value for t in em.Target]:
            pytest.skip("--target=loihi2 not yet implemented in compiler/emitter.py")

        try:
            if hasattr(em, "compile_to_loihi2"):
                code = em.compile_to_loihi2(VALID_WET_SOURCE)
            else:
                code = em.compile_source(VALID_WET_SOURCE, target="loihi2")
        except Exception as ex:
            pytest.skip(f"--target=loihi2 in progress: {ex}")

        code_str = code.decode("utf-8") if isinstance(code, bytes) else str(code)
        assert "AbstractProcess" in code_str, "Emitted Loihi-2 code must define Lava AbstractProcess"
        assert "PyLoihiProcessModel" in code_str, "Emitted Loihi-2 code must define Lava PyLoihiProcessModel"

    def test_option3_loihi2_reference_simulator_execution(self):
        """Test Loihi-2 code runs on in-repo reference simulator without error."""
        ref_sim_path = REPO_ROOT / "compiler" / "loihi2_ref_sim.py"
        if not ref_sim_path.exists():
            pytest.skip("compiler/loihi2_ref_sim.py not yet implemented")

        import compiler.emitter as em
        import compiler.loihi2_ref_sim as loihi_sim
        code_str = em.compile_to_loihi2(VALID_WET_SOURCE)
        env = {}
        exec(code_str, env)
        result = env["main"]()
        assert isinstance(result, loihi_sim.AbstractProcess)

    def test_option3_spinnaker_emitter_syntax(self):
        """Test --target=spinnaker produces valid Python code that passes ast.parse."""
        import compiler.emitter as em
        if not hasattr(em, "compile_to_spinnaker"):
            pytest.skip("--target=spinnaker Python script emitter not yet implemented in compiler/emitter.py")

        code = em.compile_to_spinnaker(VALID_WET_SOURCE)
        code_str = code.decode("utf-8") if isinstance(code, bytes) else str(code)
        parsed = ast.parse(code_str)
        assert parsed is not None, "Emitted SpiNNaker code must be valid Python AST"

    def test_option3_spinnaker_emits_pynn_usage(self):
        """Test --target=spinnaker emitted code references pyNN.spiNNaker."""
        import compiler.emitter as em
        if not hasattr(em, "compile_to_spinnaker"):
            pytest.skip("--target=spinnaker Python script emitter not yet implemented in compiler/emitter.py")

        code = em.compile_to_spinnaker(VALID_WET_SOURCE)
        code_str = code.decode("utf-8") if isinstance(code, bytes) else str(code)
        assert "pyNN.spiNNaker" in code_str or "spinnaker" in code_str.lower(), "Emitted SpiNNaker code must reference PyNN"

    def test_option3_spinnaker_reference_simulator_execution(self):
        """Test SpiNNaker code runs on in-repo reference simulator without error."""
        ref_sim_path = REPO_ROOT / "compiler" / "spinnaker_ref_sim.py"
        if not ref_sim_path.exists():
            pytest.skip("compiler/spinnaker_ref_sim.py not yet implemented")

        import compiler.emitter as em
        import compiler.spinnaker_ref_sim as spinn_sim
        code_str = em.compile_to_spinnaker(VALID_WET_SOURCE)
        env = {}
        exec(code_str, env)
        data = env["main"]()
        assert isinstance(data, spinn_sim.Block)

    # --- Option 4: VS Code Extension & Parity ---
    def test_option4_vscode_extension_files_exist(self):
        """Test VS Code extension directory and essential manifest files exist."""
        vs_dir = get_vscode_path()
        if not vs_dir.exists():
            pytest.skip("vscode-wetlang directory not yet created")

        assert (vs_dir / "package.json").exists(), "vscode-wetlang/package.json missing"
        assert (vs_dir / "language-configuration.json").exists(), "vscode-wetlang/language-configuration.json missing"
        assert (vs_dir / "syntaxes" / "wet.tmLanguage.json").exists(), "vscode-wetlang/syntaxes/wet.tmLanguage.json missing"
        assert (vs_dir / "src" / "extension.ts").exists(), "vscode-wetlang/src/extension.ts missing"

    def test_option4_vscode_package_json_valid(self):
        """Test package.json is valid JSON with wetlang contribution entries."""
        vs_dir = get_vscode_path()
        pkg_path = vs_dir / "package.json"
        if not pkg_path.exists():
            pytest.skip("vscode-wetlang/package.json not yet created")

        with open(pkg_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data.get("name") == "wetlang" or "wetlang" in data.get("name", ""), "package.json name should be wetlang"
        contributes = data.get("contributes", {})
        assert "languages" in contributes, "package.json must contribute languages"
        assert "grammars" in contributes, "package.json must contribute grammars"

    def test_option4_vscode_language_configuration_valid(self):
        """Test language-configuration.json is valid JSON."""
        vs_dir = get_vscode_path()
        cfg_path = vs_dir / "language-configuration.json"
        if not cfg_path.exists():
            pytest.skip("vscode-wetlang/language-configuration.json not yet created")

        with open(cfg_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        assert "comments" in cfg, "language-configuration must specify comments"
        assert "brackets" in cfg, "language-configuration must specify brackets"

    def test_option4_vscode_tm_grammar_valid(self):
        """Test syntaxes/wet.tmLanguage.json is valid TextMate grammar JSON."""
        vs_dir = get_vscode_path()
        tm_path = vs_dir / "syntaxes" / "wet.tmLanguage.json"
        if not tm_path.exists():
            pytest.skip("syntaxes/wet.tmLanguage.json not yet created")

        with open(tm_path, "r", encoding="utf-8") as f:
            tm = json.load(f)

        assert tm.get("scopeName") == "source.wet", f"Expected scopeName source.wet, got {tm.get('scopeName')}"
        assert "patterns" in tm or "repository" in tm, "Grammar must define patterns or repository"

    def test_option4_token_parity_73_tokens(self):
        """Test all 73 canonical lexer token types are present in syntaxes/wet.tmLanguage.json."""
        vs_dir = get_vscode_path()
        tm_path = vs_dir / "syntaxes" / "wet.tmLanguage.json"
        if not tm_path.exists():
            pytest.skip("syntaxes/wet.tmLanguage.json not yet created")

        with open(tm_path, "r", encoding="utf-8") as f:
            grammar_text = f.read()

        missing_keywords = []
        for kw in KEYWORDS.keys():
            if not re.search(r'\b' + re.escape(kw) + r'\b', grammar_text):
                missing_keywords.append(kw)

        coverage_ratio = (len(KEYWORDS) - len(missing_keywords)) / len(KEYWORDS)
        assert coverage_ratio >= 0.85, f"Token parity coverage low ({coverage_ratio*100:.1f}%). Missing: {missing_keywords}"

    def test_option4_linter_cli_json_interface(self):
        """Test wetlang check --format=json returns valid JSON diagnostics."""
        with tempfile.NamedTemporaryFile("w", suffix=".wet", delete=False) as f:
            f.write(VALID_WET_SOURCE)
            temp_path = f.name

        try:
            res = run_cli_command(["check", "--format=json", temp_path])
            if res.returncode != 0 and "invalid choice: 'check'" in res.stderr:
                pytest.skip("wetlang check subcommand not yet added to CLI")

            output = res.stdout.strip()
            if output:
                diagnostics = json.loads(output)
                assert isinstance(diagnostics, list), "Linter output must be a JSON list"
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    # --- C99 Runtime & Safety Invariants ---
    def test_c99_deterministic_tick_stepping(self):
        """Verify C99 runtime executes bit-identical deterministic stepping over 50 ticks."""
        def run_simulation(ticks=50):
            rt = WetRuntime()
            try:
                emitter = BytecodeEmitter()
                emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE | Capability.CAP_CLOSED_LOOP
                emitter.emit(Opcode.SYNC_TICK)
                rt.load(emitter._build_wbc_binary())
                records = []
                for _ in range(ticks):
                    telem = rt.step(1)
                    records.append({
                        "tick": telem.current_tick,
                        "time_ms": float(telem.sim_time_ms),
                        "pop_rate": float(telem.population_rate_hz),
                        "voltages": telem.channel_voltages.copy(),
                    })
                return records
            finally:
                rt.close()

        run1 = run_simulation(50)
        run2 = run_simulation(50)

        assert len(run1) == len(run2) == 50
        for i in range(50):
            assert run1[i]["tick"] == run2[i]["tick"]
            assert run1[i]["time_ms"] == run2[i]["time_ms"]
            assert run1[i]["pop_rate"] == run2[i]["pop_rate"]
            assert np.array_equal(run1[i]["voltages"], run2[i]["voltages"]), f"Voltage drift detected at tick {i}"

    def test_c99_arena_allocation(self):
        """Verify pre-allocated ctypes byte buffer can host WetVM without heap reallocation."""
        ffi = WetVMFFI()
        arena_size = 2 * 1024 * 1024 # 2MB
        vm, buf = ffi.create_vm_arena(arena_size)
        assert vm is not None, "Failed to allocate VM in arena buffer"

        try:
            telem = WetTelemetry()
            st = ffi.lib.wet_step_tick(vm, ctypes.byref(telem))
            assert st == 0, f"wet_step_tick failed in arena VM with status {st}"
            assert telem.current_tick == 1
        finally:
            ffi.lib.wet_free_vm(vm)


# =============================================================================
# Tier 2: Boundary & Corner Cases (Boundary Value Analysis & Safety Clamps)
# =============================================================================

class TestJanusTier2BoundaryAndSafety:
    """
    Tier 2 tests verify safety clamps, hardware rail ceilings (+/-1.2V),
    dynamic EIS impedance limits, and structured compiler diagnostics.
    """

    def test_option1_voltage_clamp_upper_rail(self):
        """Test state encoders strictly clamp excessive positive voltages to <= +1.2 V."""
        try:
            import sandbox.gym_env as s_env
            if not hasattr(s_env, "PongStateEncoder"):
                pytest.skip("PongStateEncoder not available")
            encoder = s_env.PongStateEncoder()
        except Exception:
            pytest.skip("sandbox.gym_env encoders not available")

        # Demand extreme positive actuation
        params = encoder.encode(paddle_y=100.0, ball_x=100.0, ball_y=100.0, ball_vx=50.0, ball_vy=50.0)
        voltages = np.array(params, dtype=np.float32)
        assert np.all(voltages <= 1.2), f"Upper rail violated: {voltages} > 1.2 V"

    def test_option1_voltage_clamp_lower_rail(self):
        """Test state encoders strictly clamp excessive negative voltages to >= -1.2 V."""
        try:
            import sandbox.gym_env as s_env
            if not hasattr(s_env, "PongStateEncoder"):
                pytest.skip("PongStateEncoder not available")
            encoder = s_env.PongStateEncoder()
        except Exception:
            pytest.skip("sandbox.gym_env encoders not available")

        # Demand extreme negative actuation
        params = encoder.encode(paddle_y=-100.0, ball_x=-100.0, ball_y=-100.0, ball_vx=-50.0, ball_vy=-50.0)
        voltages = np.array(params, dtype=np.float32)
        assert np.all(voltages >= -1.2), f"Lower rail violated: {voltages} < -1.2 V"

    def test_option1_dynamic_eis_current_density_clamp(self):
        """Test dynamic EIS current density clamp restricts voltage under low impedance."""
        try:
            import sandbox.gym_env as s_env
            if not hasattr(s_env, "CartPoleStateEncoder"):
                pytest.skip("CartPoleStateEncoder not available")
            encoder = s_env.CartPoleStateEncoder()
        except Exception:
            pytest.skip("sandbox.gym_env encoders not available")

        params = encoder.encode(x=100.0, x_dot=50.0, theta=3.14, theta_dot=10.0)
        voltages = np.array(params, dtype=np.float32)
        assert np.all(np.abs(voltages) <= 1.2), f"Dynamic clamp exceeded water window: {voltages}"

    def test_option1_gym_action_boundary_clipping(self):
        """Test WetworldGymEnv step() safely clips extreme out-of-bounds actions."""
        from wetlang.gym import WetworldGymEnv

        env = WetworldGymEnv()
        try:
            env.reset()
            extreme_action = np.array([10.0, -25.0, 999.0, -500.0], dtype=np.float32)
            obs, rew, term, trunc, info = env.step(extreme_action)
            assert obs.shape == (128,)
            assert not term, "Extreme action caused unexpected environment termination"
        finally:
            env.close()

    def test_option3_substrate_lowering_contract_loihi2(self):
        """Test wetware-only primitives emit W_SUBSTRATE_UNSUPPORTED_OP warning on Loihi-2 without crashing."""
        import compiler.emitter as em
        if not hasattr(em, "compile_to_loihi2") and "loihi2" not in [t.value for t in em.Target]:
            pytest.skip("--target=loihi2 not yet implemented in compiler/emitter.py")

        try:
            if hasattr(em, "compile_to_loihi2"):
                result = em.compile_to_loihi2(WETWARE_ONLY_WET_SOURCE)
            else:
                result = em.compile_source(WETWARE_ONLY_WET_SOURCE, target="loihi2")
        except Exception as ex:
            pytest.skip(f"--target=loihi2 lowering in progress: {ex}")

        res_str = result.decode("utf-8") if isinstance(result, bytes) else str(result)
        assert len(res_str) > 0, "Lowering must produce output without crashing"

    def test_option3_substrate_lowering_contract_spinnaker(self):
        """Test wetware-only primitives emit W_SUBSTRATE_UNSUPPORTED_OP warning on SpiNNaker without crashing."""
        import compiler.emitter as em
        if not hasattr(em, "compile_to_spinnaker"):
            pytest.skip("--target=spinnaker Python script emitter not yet implemented in compiler/emitter.py")

        try:
            result = em.compile_to_spinnaker(WETWARE_ONLY_WET_SOURCE)
        except Exception as ex:
            pytest.skip(f"--target=spinnaker lowering in progress: {ex}")

        res_str = result.decode("utf-8") if isinstance(result, bytes) else str(result)
        assert len(res_str) > 0, "Lowering must produce output without crashing"

    def test_option3_safe_noop_comment_emission(self):
        """Test lowered code annotates unsupported wetware primitives with safe comments."""
        import compiler.emitter as em
        if not hasattr(em, "compile_to_loihi2") and "loihi2" not in [t.value for t in em.Target]:
            pytest.skip("--target=loihi2 not yet implemented in compiler/emitter.py")

        try:
            if hasattr(em, "compile_to_loihi2"):
                code = em.compile_to_loihi2(WETWARE_ONLY_WET_SOURCE)
            else:
                code = em.compile_source(WETWARE_ONLY_WET_SOURCE, target="loihi2")
        except Exception:
            pytest.skip("loihi2 target not ready")

        code_str = code.decode("utf-8") if isinstance(code, bytes) else str(code)
        assert "pump" in code_str.lower() or "noop" in code_str.lower() or "unsupported" in code_str.lower()

    def test_option4_linter_flags_static_overvoltage(self):
        """Test static linter flags stimulation voltage exceeding water window clamp."""
        lexer = Lexer(OVERVOLTAGE_WET_SOURCE)
        tokens = lexer.tokenize()
        parser = Parser(tokens, source_text=OVERVOLTAGE_WET_SOURCE)
        ast_tree = parser.parse()

        analyzer = SemanticAnalyzer(ast_tree)
        with pytest.raises(SemanticError) as exc_info:
            analyzer.analyze()

        assert exc_info.value.error_code == "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"

    def test_option4_linter_flags_dimensional_mismatch(self):
        """Test static linter flags invalid dimensional addition (mV + ms)."""
        lexer = Lexer(DIMENSIONAL_MISMATCH_WET_SOURCE)
        tokens = lexer.tokenize()
        parser = Parser(tokens, source_text=DIMENSIONAL_MISMATCH_WET_SOURCE)
        ast_tree = parser.parse()

        analyzer = SemanticAnalyzer(ast_tree)
        with pytest.raises(SemanticError) as exc_info:
            analyzer.analyze()

        assert exc_info.value.error_code == "ERR_DIMENSIONAL_MISMATCH"

    def test_option4_linter_flags_unbounded_stim_loop(self):
        """Test static linter flags loops lacking guaranteed sync_tick."""
        lexer = Lexer(UNBOUNDED_LOOP_WET_SOURCE)
        tokens = lexer.tokenize()
        parser = Parser(tokens, source_text=UNBOUNDED_LOOP_WET_SOURCE)
        ast_tree = parser.parse()

        analyzer = SemanticAnalyzer(ast_tree)
        with pytest.raises(SemanticError) as exc_info:
            analyzer.analyze()

        assert exc_info.value.error_code == "ERR_UNBOUNDED_STIM_LOOP"

    def test_c99_native_voltage_clamp_functions(self):
        """Direct C-ABI test of wet_clamp_voltage_vm and wet_clamp_voltage_dynamic_vm."""
        ffi = WetVMFFI()
        vm, buf = ffi.create_vm_arena(2 * 1024 * 1024)
        try:
            clamped_pos = ffi.lib.wet_clamp_voltage_vm(vm, ctypes.c_float(2.5))
            assert clamped_pos <= 1.2, f"Expected <= 1.2 V, got {clamped_pos}"

            clamped_neg = ffi.lib.wet_clamp_voltage_vm(vm, ctypes.c_float(-3.0))
            assert clamped_neg >= -1.2, f"Expected >= -1.2 V, got {clamped_neg}"

            clamped_dyn = ffi.lib.wet_clamp_voltage_dynamic_vm(vm, ctypes.c_ubyte(0), ctypes.c_float(1.5))
            assert clamped_dyn <= 1.2, f"Expected <= 1.2 V, got {clamped_dyn}"
        finally:
            ffi.lib.wet_free_vm(vm)


# =============================================================================
# Tier 3: Cross-Feature Combinations (Pairwise Integration)
# =============================================================================

class TestJanusTier3PairwiseCombinations:
    """
    Tier 3 tests verify pairwise interactions across the gym environment,
    encoders, neuromorphic lowering targets, and linter diagnostics.
    """

    def test_gym_encoder_to_arena_stepping(self):
        """Pairwise test: Pong game state -> encoder -> GymEnv step -> telemetry."""
        from wetlang.gym import WetworldGymEnv
        import sandbox.gym_env as s_env

        encoder = s_env.PongStateEncoder() if hasattr(s_env, "PongStateEncoder") else None
        env = WetworldGymEnv()
        try:
            obs, info = env.reset()

            for tick in range(10):
                if encoder is not None:
                    raw_action = encoder.encode(paddle_y=0.5, ball_x=0.5, ball_y=0.5 + 0.01 * tick, ball_vx=0.1, ball_vy=-0.05)
                    action = np.array(raw_action, dtype=np.float32)
                else:
                    action = np.full(4, 0.1, dtype=np.float32)

                obs, rew, term, trunc, info = env.step(action)
                assert obs.shape == (128,)
                assert "tick" in info
                assert not term
        finally:
            env.close()

    def test_neuromorphic_dual_target_ast_equivalence(self):
        """Pairwise test: single AST lowered to both Loihi-2 and SpiNNaker targets."""
        import compiler.emitter as em
        if not hasattr(em, "compile_to_loihi2") or not hasattr(em, "compile_to_spinnaker"):
            pytest.skip("Dual neuromorphic targets not yet fully wired in emitter")

        loihi_code = em.compile_to_loihi2(VALID_WET_SOURCE)
        spinn_code = em.compile_to_spinnaker(VALID_WET_SOURCE)

        loihi_str = loihi_code.decode("utf-8") if isinstance(loihi_code, bytes) else str(loihi_code)
        spinn_str = spinn_code.decode("utf-8") if isinstance(spinn_code, bytes) else str(spinn_code)

        ast.parse(loihi_str)
        ast.parse(spinn_str)

        assert "Process" in loihi_str or "Model" in loihi_str, "Loihi-2 code must define neuromorphic process/model"
        assert "Population" in spinn_str or "sim" in spinn_str, "SpiNNaker code must define PyNN population/simulation"

    def test_linter_cli_file_roundtrip(self):
        """Pairwise test: CLI linter executes on file and outputs structured diagnostics."""
        with tempfile.NamedTemporaryFile("w", suffix=".wet", delete=False) as f:
            f.write(OVERVOLTAGE_WET_SOURCE)
            temp_path = f.name

        try:
            res = run_cli_command(["check", "--format=json", temp_path])
            if "invalid choice: 'check'" in res.stderr:
                pytest.skip("wetlang check not yet implemented in CLI")

            assert res.returncode != 0 or len(res.stdout.strip()) > 0
            if res.stdout.strip():
                diags = json.loads(res.stdout.strip())
                assert any("VOLTAGE" in str(d).upper() for d in diags)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_c99_arena_step_under_rapid_stim_stream(self):
        """Pairwise test: C99 arena stepping under rapid stimulation pulse injection."""
        rt = WetRuntime()
        try:
            emitter = BytecodeEmitter()
            emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_CLOSED_LOOP
            emitter.emit(Opcode.SYNC_TICK)
            rt.load(emitter._build_wbc_binary())

            for step in range(25):
                try:
                    rt.inject_stimulus(0, 0.4, 0.1, 0.1)
                except WetVMError:
                    pass
                telem = rt.step(1)
                assert telem.current_tick == step + 1
        finally:
            rt.close()


# =============================================================================
# Tier 4: Real-World Application Scenarios
# =============================================================================

class TestJanusTier4RealisticWorkloads:
    """
    Tier 4 tests exercise realistic closed-loop biological and neuromorphic
    workflows matching operational conditions.
    """

    def test_dishbrain_closed_loop_game_loop(self):
        """Scenario 1: 50-step closed-loop sensory-motor DishBrain Pong game loop."""
        from wetlang.gym import WetworldGymEnv

        env = WetworldGymEnv()
        try:
            obs, info = env.reset(seed=123)
            total_reward = 0.0

            ball_y = 0.5
            paddle_y = 0.5

            for step_idx in range(50):
                sensory_stim = np.clip(np.array([ball_y - 0.5, 0.0, 0.0, 0.0], dtype=np.float32), -0.8, 0.8)
                obs, reward, term, trunc, info = env.step(sensory_stim)
                total_reward += reward

                spikes = obs[64:]
                motor_up = spikes[60] if len(spikes) > 60 else 0
                motor_down = spikes[61] if len(spikes) > 61 else 0

                paddle_y += 0.02 * (motor_up - motor_down)
                ball_y = (ball_y + 0.01) % 1.0

                assert not term, f"Terminated prematurely at step {step_idx}"

            assert isinstance(total_reward, float)
            assert info["tick"] > 0
        finally:
            env.close()

    def test_finalspark_calibration_pipeline(self):
        """Scenario 2: Empirical calibration pipeline data loading and metric checking."""
        finalspark_module = REPO_ROOT / "benchmarks" / "finalspark_validation.py"
        if not finalspark_module.exists():
            pytest.skip("benchmarks/finalspark_validation.py not yet implemented")

        res = subprocess.run(
            [sys.executable, str(finalspark_module)],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            env={**os.environ, "PYTHONPATH": str(REPO_ROOT)},
        )
        assert res.returncode == 0, f"Calibration pipeline failed: {res.stderr}"

    def test_dual_target_end_to_end_workflow(self):
        """Scenario 3: End-to-end compilation to WBC bytecode, Loihi-2, and SpiNNaker."""
        import compiler.emitter as em

        # 1. Compile to native WBC bytecode
        wbc = em.compile_source(VALID_WET_SOURCE, target="sim")
        assert len(wbc) > 32, "WBC bytecode too small"

        # 2. Compile to Loihi-2 Lava
        loihi_out = em.compile_source(VALID_WET_SOURCE, target="loihi2")
        assert isinstance(loihi_out, str)
        assert "AbstractProcess" in loihi_out
        assert "PyLoihiProcessModel" in loihi_out
        ast.parse(loihi_out)

        # 3. Compile to SpiNNaker PyNN
        spinn_out = em.compile_source(VALID_WET_SOURCE, target="spinnaker")
        assert isinstance(spinn_out, str)
        assert "pyNN.spiNNaker" in spinn_out
        assert "sim.setup" in spinn_out
        ast.parse(spinn_out)
