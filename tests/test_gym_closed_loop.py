"""
Test Suite: Milestone 1 Closed-Loop AI Benchmark Suite & Gym Environments
========================================================================
Verifies:
1. Canonical WetworldGymEnv with C99 arena memory pre-allocation (zero heap malloc).
2. PongStateEncoder & CartPoleStateEncoder biophysical safety & dynamic EIS clamping.
3. MotorSpikeDecoder biological spike raster translation.
4. DishBrainPongEnv & OrganoidCartPoleEnv closed-loop step execution.
5. PyTorch RL policy network coupled with R-STDP eligibility traces.
6. Active Inference / Free Energy Principle (FEP) sensory feedback modulation.
7. FinalSpark fs369 empirical validation adapter (live & CI fallback).
"""

import sys
from pathlib import Path
import numpy as np
import pytest
import torch

_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

from wetlang.gym import WetworldGymEnv, make
from sandbox.gym_env import (
    BiophysicalSafetyClamp,
    PongStateEncoder,
    CartPoleStateEncoder,
    MotorSpikeDecoder,
    DishBrainPongEnv,
    OrganoidCartPoleEnv,
)
from benchmarks.run_pong_rl import RSTDPPolicyNet
from benchmarks.run_pong_fep import ActiveInferenceFEPAgent
from benchmarks.finalspark_validation import (
    load_empirical_metrics,
    run_simulated_twin,
    validate_against_finalspark,
    CACHED_EMPIRICAL_BOUNDS,
)


class TestWetworldGymEnv:
    """Tests canonical C99 arena-backed WetworldGymEnv."""

    def test_arena_initialization_and_spaces(self):
        env = WetworldGymEnv(arena_bytes=1024 * 1024, steps_per_action=5)
        assert env.arena_bytes == 1024 * 1024
        assert len(env._arena_buf) == 1024 * 1024
        assert env.observation_space.shape == (128,)
        assert env.action_space.shape == (4,)
        assert env.observation_space.dtype == np.float32
        assert env.action_space.dtype == np.float32

        obs, info = env.reset(seed=123)
        assert obs.shape == (128,)
        assert obs.dtype == np.float32
        assert np.all(obs[:64] >= -1.2)
        assert np.all(obs[:64] <= 1.2)
        assert np.all(obs[64:] >= 0.0)
        assert np.all(obs[64:] <= 1.0)
        assert "population_rate_hz" in info
        assert "arena_bytes" in info
        env.close()

    def test_step_execution_and_telemetry(self):
        env = make(arena_bytes=1024 * 1024, steps_per_action=10)
        obs, info = env.reset()

        # Step with zero stimulation
        obs, reward, term, trunc, info = env.step(np.zeros(4, dtype=np.float32))
        assert obs.shape == (128,)
        assert isinstance(reward, float)
        assert isinstance(term, bool)
        assert isinstance(trunc, bool)
        assert info["executed_ticks"] == 10

        # Step with active biphasic stimulation
        action = np.array([0.4, -0.4, 0.2, -0.2], dtype=np.float32)
        obs, reward, term, trunc, info = env.step(action)
        assert obs.shape == (128,)
        assert not term

        telem = env.get_telemetry()
        assert telem is not None
        assert telem.current_tick >= 20

        # Synapse matrix read
        syn = env.get_synapse_matrix()
        assert syn.shape == (64, 64)

        env.close()


class TestEncodersAndDecoders:
    """Tests biophysical safety clamping, state encoders, and motor decoders."""

    def test_biophysical_safety_clamp(self):
        clamp = BiophysicalSafetyClamp(
            j_limit_ua_cm2=30.0,
            electrode_area_um2=5000.0,
            z_magnitude_ohms=100000.0,
            water_window_low_v=-1.2,
            water_window_high_v=1.2,
        )
        v_safe = clamp.calculate_safe_voltage_magnitude()
        assert v_safe > 0.0

        # Overvoltage clamping check (beyond water window rail)
        v_clamped = clamp.clamp_voltage(2.5)
        assert v_clamped <= 1.2
        v_clamped_neg = clamp.clamp_voltage(-3.0)
        assert v_clamped_neg >= -1.2

        # Voltage exceeding v_safe should be clamped to v_safe
        v_exceeding = clamp.clamp_voltage(0.5)
        assert abs(v_exceeding - v_safe) < 1e-6

        # Voltage below v_safe should pass unchanged
        v_under = v_safe * 0.5
        v_passed = clamp.clamp_voltage(v_under)
        assert abs(v_passed - v_under) < 1e-6

    def test_pong_state_encoder(self):
        encoder = PongStateEncoder(water_window_v=1.2, voltage_scale=0.6)
        # Paddle at y=0, ball at y=0.5 (ball above paddle)
        stim = encoder.encode(paddle_y=0.0, ball_x=0.5, ball_y=0.5, ball_vx=0.04, ball_vy=0.01)
        assert stim.shape == (4,)
        assert stim.dtype == np.float32
        # Channel 0 (above paddle) should be active, Channel 1 (below paddle) should be 0
        assert stim[0] > 0.0
        assert stim[1] == 0.0
        assert np.all(np.abs(stim) <= 1.2)

        # Test extreme inputs: must strictly enforce water window
        extreme_stim = encoder.encode(paddle_y=-10.0, ball_x=10.0, ball_y=10.0, ball_vx=10.0, ball_vy=10.0)
        assert np.all(np.abs(extreme_stim) <= 1.2)

    def test_cartpole_state_encoder(self):
        encoder = CartPoleStateEncoder(water_window_v=1.2, voltage_scale=0.6)
        stim = encoder.encode(x=1.2, x_dot=0.5, theta=0.1, theta_dot=-0.2)
        assert stim.shape == (4,)
        assert stim.dtype == np.float32
        assert np.all(np.abs(stim) <= 1.2)

        # Extreme inputs
        extreme_stim = encoder.encode(x=100.0, x_dot=100.0, theta=10.0, theta_dot=10.0)
        assert np.all(np.abs(extreme_stim) <= 1.2)

    def test_motor_spike_decoder(self):
        decoder = MotorSpikeDecoder()

        # Synthetic spike raster with activity on left channels (60, 62)
        spikes_left = np.zeros(128, dtype=np.uint8)
        spikes_left[64 + 60] = 1
        spikes_left[64 + 62] = 1
        act_left = decoder.decode_discrete(spikes_left)
        assert act_left == 0

        # Synthetic spike raster with activity on right channels (61, 63)
        spikes_right = np.zeros(128, dtype=np.uint8)
        spikes_right[64 + 61] = 1
        spikes_right[64 + 63] = 1
        act_right = decoder.decode_discrete(spikes_right)
        assert act_right == 1

        # Continuous force decode
        force = decoder.decode_continuous(spikes_right)
        assert force > 0.0


class TestClosedLoopEnvironments:
    """Tests reference DishBrainPongEnv and OrganoidCartPoleEnv."""

    def test_dishbrain_pong_env_execution(self):
        env = DishBrainPongEnv(steps_per_action=5, max_steps=50)
        obs, info = env.reset(seed=42)
        assert obs.shape == (133,)  # 5 pong + 128 wetworld

        for step in range(10):
            # Test step with action
            obs, reward, term, trunc, info = env.step(step % 2)
            assert obs.shape == (133,)
            assert isinstance(reward, float)
            assert "hits" in info
            assert "misses" in info
            if term or trunc:
                break
        env.close()

    def test_organoid_cartpole_env_execution(self):
        env = OrganoidCartPoleEnv(steps_per_action=5, max_steps=50)
        obs, info = env.reset(seed=42)
        assert obs.shape == (132,)  # 4 cartpole + 128 wetworld

        for step in range(10):
            obs, reward, term, trunc, info = env.step(step % 2)
            assert obs.shape == (132,)
            assert isinstance(reward, float)
            assert "theta" in info
            if term or trunc:
                break
        env.close()


class TestDualLearningParadigms:
    """Tests PyTorch RL R-STDP and Active Inference FEP learning mechanics."""

    def test_pytorch_rstdp_plasticity(self):
        policy = RSTDPPolicyNet(obs_dim=133, hidden_dim=32, action_dim=2, lr=0.01)
        synthetic_obs = np.random.randn(133).astype(np.float32)

        action, probs, _ = policy.select_action(synthetic_obs)
        assert action in (0, 1)
        assert probs.shape == (1, 2)

        # Eligibility traces should now be non-zero
        assert torch.sum(torch.abs(policy.e1)) > 0.0

        # Initial weight norm
        w_before = float(torch.norm(policy.fc1.weight.data))

        # Apply reward modulation
        metrics = policy.update_rstdp(reward=1.0)
        w_after = float(torch.norm(policy.fc1.weight.data))

        assert metrics["norm_delta"] > 0.0
        assert metrics["norm_w"] > 0.0
        assert metrics["norm_e"] > 0.0
        assert w_before != w_after

    def test_active_inference_fep_modulation(self):
        agent = ActiveInferenceFEPAgent(obs_dim=133, action_dim=2)
        state = np.array([0.0, 0.5, 0.0, 0.0, 0.0], dtype=np.float32)

        # Predictable feedback should have low free energy
        fe_predictable = agent.compute_variational_free_energy(state, is_predictable_feedback=True)
        # Unpredictable feedback should have high free energy
        fe_unpredictable = agent.compute_variational_free_energy(state, is_predictable_feedback=False)

        assert fe_unpredictable > fe_predictable
        assert fe_unpredictable - fe_predictable >= 3.0  # Entropy delta ~ 3.7 bits

        # Action selection
        action, min_g = agent.select_action(np.zeros(133, dtype=np.float32))
        assert action in (0, 1)


class TestFinalSparkEmpiricalValidation:
    """Tests FinalSpark data ingestion and CI fallback."""

    def test_ci_fallback_metrics(self):
        # Path guaranteed not to exist
        fake_path = Path("Z:\\non_existent_drive\\fake.hdf5")
        metrics, is_live = load_empirical_metrics(fake_path)
        assert not is_live
        assert metrics["mean_firing_rate_hz"] == CACHED_EMPIRICAL_BOUNDS["mean_firing_rate_hz"]
        assert metrics["mean_cv_isi"] == CACHED_EMPIRICAL_BOUNDS["mean_cv_isi"]
        assert metrics["mean_burst_fraction"] == CACHED_EMPIRICAL_BOUNDS["mean_burst_fraction"]

    def test_simulated_twin_within_bounds(self):
        sim = run_simulated_twin(steps=30000, steps_per_action=1)
        assert 0.5 <= sim["mean_firing_rate_hz"] <= 25.0
        assert 1.0 <= sim["mean_cv_isi"] <= 8.0
        assert 0.20 <= sim["mean_burst_fraction"] <= 0.90

    def test_validation_function_execution(self):
        passed = validate_against_finalspark(sample_size=1000, sim_steps=30000)
        assert passed is True
