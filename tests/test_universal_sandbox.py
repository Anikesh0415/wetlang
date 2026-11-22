"""
Universal Multi-Organoid Sandbox & Pre-Done Web Sandbox Test Suite
==================================================================
Tests:
1. Single-organoid execution in UniversalOrganoidSandbox.
2. 16-organoid cluster orchestration (WW-16 biological array).
3. 1,024-organoid parametric cluster scaling.
4. Axonal conduction delay buffer timing across organoids.
5. Compile-time & runtime Krogh Cylinder anoxia detection.
6. Gymnasium (gymnasium.Env) standard sandbox compliance.
7. Closed-loop Active Inference RL loop on WetworldGymEnv.
8. snnTorch biophysical ODE cross-validation.
"""

import unittest
import numpy as np

from sandbox.universal_organoid_sandbox import UniversalOrganoidSandbox
from sandbox.gym_env import WetworldGymEnv
from sandbox.snntorch_cross_validation import run_snntorch_cross_validation
from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.semantic import SemanticAnalyzer, SemanticError
from compiler.emitter import BytecodeEmitter


class TestUniversalSandbox(unittest.TestCase):

    def test_01_single_organoid_sandbox(self):
        """Verify 1-organoid instantiation, stepping, and telemetry."""
        sb = UniversalOrganoidSandbox()
        org_id = sb.create_organoid("Cortex_1", cells=100_000, radius_um=150.0, perfusion_ul_min=2.0)
        self.assertEqual(org_id, 0)
        telem = sb.step(ticks=10)
        self.assertEqual(telem["total_organoids"], 1)
        self.assertEqual(telem["alive_organoids"], 1)
        self.assertAlmostEqual(telem["sim_time_ms"], 1.0, places=3)
        sb.close()

    def test_02_16_organoid_cluster_sandbox(self):
        """Verify 16-organoid WW-16 biological array with bidirectional interconnects."""
        sb = UniversalOrganoidSandbox()
        ids = sb.create_cluster("WW16_Well", count=16, cells_per_organoid=50_000)
        self.assertEqual(len(ids), 16)

        # Wire linear chain of organoids: Well_0 -> Well_1 -> ... -> Well_15
        for i in range(15):
            sb.connect(f"WW16_Well_{i}", f"WW16_Well_{i+1}", delay_ms=2.0, weight=1.2)

        telem = sb.step(ticks=20)
        self.assertEqual(telem["total_organoids"], 16)
        self.assertEqual(telem["alive_organoids"], 16)
        self.assertEqual(telem["active_axonal_tracts"], 15)
        sb.close()

    def test_03_1024_parametric_cluster_scaling(self):
        """Verify scaling from 1 to 1,024 organoid nodes without memory exhaustion."""
        sb = UniversalOrganoidSandbox()
        ids = sb.create_cluster("HyperCluster", count=1024, cells_per_organoid=10_000)
        self.assertEqual(len(ids), 1024)
        self.assertEqual(len(sb.organoids), 1024)
        sb.close()

    def test_04_axonal_conduction_delay_timing(self):
        """Verify inter-organoid action potentials travel with exact physical delay."""
        sb = UniversalOrganoidSandbox(dt_ms=0.1)
        sb.create_organoid("SensoryNode")
        sb.create_organoid("MotorNode")

        # 5.0 ms delay = 50 ticks
        sb.connect("SensoryNode", "MotorNode", source_channel=0, target_channel=0, delay_ms=5.0, weight=1.0)
        self.assertEqual(sb.tracts[0].conduction_delay_ticks, 50)

        # Force a spike on SensoryNode channel 0
        sb.organoids[0].last_spikes[0] = 1
        # Step 1 tick: spike enters axonal tract
        sb.step(1)
        self.assertEqual(len(sb.inflight_spikes), 1)
        deliver_tick = sb.inflight_spikes[0][0]
        self.assertEqual(deliver_tick, 51)  # tick 1 + 50 ticks delay
        sb.close()

    def test_05_krogh_anoxia_compile_check(self):
        """Verify compiler strictly prevents unperfused organoids exceeding 200 um radius."""
        code_necrotic = """
        organoid AnoxicBrain {
            radius: 300um; // Exceeds 200 um limit without perfusion
        }
        fn main() { sync_tick(); }
        """
        ast = Parser(Lexer(code_necrotic).tokenize()).parse()
        with self.assertRaises(SemanticError) as ctx:
            SemanticAnalyzer(ast).analyze()
        self.assertEqual(ctx.exception.error_code, "ERR_KROGH_ANOXIA_VIOLATION")

    def test_06_gymnasium_env_compliance(self):
        """Verify WetworldGymEnv conforms to Gymnasium standard interface."""
        env = WetworldGymEnv()
        obs, info = env.reset()

        self.assertEqual(obs.shape, (128,))
        self.assertEqual(obs.dtype, np.float32)
        self.assertIn("population_rate_hz", info)

        # Step random action
        action = env.action_space.sample()
        obs2, reward, terminated, truncated, info2 = env.step(action)

        self.assertEqual(obs2.shape, (128,))
        self.assertIsInstance(reward, float)
        self.assertIsInstance(terminated, bool)
        self.assertIsInstance(truncated, bool)
        env.close()

    def test_07_gymnasium_active_inference_loop(self):
        """Verify 50 closed-loop Active Inference cycles in Gymnasium sandbox."""
        env = WetworldGymEnv(steps_per_action=5)
        obs, _ = env.reset()
        total_reward = 0.0

        for _ in range(50):
            action = np.zeros(4, dtype=np.float32)
            obs, reward, terminated, truncated, _ = env.step(action)
            total_reward += reward
            if terminated or truncated:
                break

        self.assertIsInstance(total_reward, float)
        env.close()

    def test_08_snntorch_biophysical_ode_convergence(self):
        """Verify Wetworld C99 LIF matches snnTorch PyTorch reference with r > 0.90."""
        res = run_snntorch_cross_validation(steps=60)
        self.assertTrue(res["validation_passed"], f"snnTorch alignment failed: {res}")
        self.assertGreater(res["pearson_correlation"], 0.90)


if __name__ == "__main__":
    unittest.main()
