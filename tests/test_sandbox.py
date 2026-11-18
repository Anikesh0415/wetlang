import unittest
import numpy as np
from wetlang.sandbox import UniversalOrganoidSandbox, WetworldGymEnv
from wetlang.sandbox.snntorch_cross_validation import run_snntorch_cross_validation


class TestWetLangSandbox(unittest.TestCase):
    def test_multi_organoid_orchestration(self):
        sb = UniversalOrganoidSandbox(dt_ms=0.1)
        sb.create_cluster("Cluster", count=4)
        sb.connect("Cluster_0", "Cluster_1", delay_ms=5.0, weight=1.0)
        status = sb.step(10)
        self.assertEqual(status["total_organoids"], 4)
        sb.close()

    def test_gymnasium_compliance(self):
        env = WetworldGymEnv()
        obs, info = env.reset()
        self.assertEqual(obs.shape, (128,))
        obs2, reward, terminated, truncated, _ = env.step(env.action_space.sample())
        self.assertEqual(obs2.shape, (128,))
        env.close()

    def test_snntorch_cross_validation(self):
        res = run_snntorch_cross_validation(steps=60)
        self.assertTrue(res["validation_passed"])
        self.assertGreater(res["pearson_correlation"], 0.99)


if __name__ == "__main__":
    unittest.main()
