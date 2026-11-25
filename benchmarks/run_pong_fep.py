"""
DishBrain Pong Active Inference / Free Energy Principle (FEP) Benchmark
=======================================================================
Biological agent minimizing variational free energy via predictable (low entropy)
versus unpredictable (high entropy) sensory stimulation feedback (Kagan et al., Neuron 2022).

Free Energy Principle (FEP) Dynamics:
- Goal / Hit Feedback (Predictable, Low Entropy):
    Periodic 20 Hz coherent pulses delivered to designated sensory channel.
    Generates minimal sensory entropy: H_predictable -> 0 bits, F -> low.
- Error / Miss Feedback (Unpredictable, High Entropy):
    Chaotic pseudo-random multi-channel stimulation bursts (100-200 Hz jitter).
    Generates maximal sensory entropy: H_unpredictable -> high bits, F -> high.
- Active Inference Action Selection:
    Selects motor actions minimizing expected free energy:
    G(a) = E_q[ ln q(s'|a) - ln p(s') ] (Pragmatic + Epistemic Value)
"""

import sys
import os
import argparse
import time
from pathlib import Path
from typing import Tuple, Dict, Any, Optional, Sequence

# Ensure root repository directory is in sys.path
_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

import numpy as np

from sandbox.gym_env import DishBrainPongEnv, PongStateEncoder, MotorSpikeDecoder


class ActiveInferenceFEPAgent:
    """
    Active Inference Agent minimizing Variational Free Energy and Sensory Entropy.
    Maintains a predictive generative model of Pong ball trajectory and sensory consequences.
    """
    def __init__(
        self,
        obs_dim: int = 133,
        action_dim: int = 2,
        learning_rate: float = 0.05,
        temperature: float = 0.5,
    ):
        self.obs_dim = obs_dim
        self.action_dim = action_dim
        self.lr = learning_rate
        self.temperature = temperature

        # Generative model: weights predicting next 5 pong kinematic features given state and action
        # Initialized with discrete Euler kinematics and refined online via variational gradient
        self.transition_weights = np.zeros((action_dim, 5, 5), dtype=np.float32)
        for a in range(action_dim):
            self.transition_weights[a] = np.eye(5, dtype=np.float32)
            self.transition_weights[a, 1, 3] = 1.0  # ball_x' = ball_x + ball_vx
            self.transition_weights[a, 2, 4] = 1.0  # ball_y' = ball_y + ball_vy
        self.action_delta = np.array([
            [-0.06, 0.0, 0.0, 0.0, 0.0],  # a=0: paddle down
            [+0.06, 0.0, 0.0, 0.0, 0.0],  # a=1: paddle up
        ], dtype=np.float32)

        # Prior preferences over sensory observation: prefers low paddle-ball distance
        self.prior_target = np.array([0.0, 0.95, 0.0, 0.0, 0.0], dtype=np.float32)
        self.prior_precisions = np.array([5.0, 1.0, 5.0, 1.0, 1.0], dtype=np.float32)

        self.last_state = None
        self.last_action = 0
        self.last_pred_error = 0.0

    @staticmethod
    def _compute_neural_shannon_entropy(
        state: np.ndarray,
        spike_counts: Optional[np.ndarray] = None,
        kin_dim: int = 5,
    ) -> Optional[float]:
        """
        Computes Shannon entropy H = -sum(p_ch * log2(p_ch)) across the 64 MEA
        channels from observed spike counts and extracellular LFP/voltage energy.
        Returns None if only a low-dimensional kinematic vector is provided.
        """
        if spike_counts is not None and len(spike_counts) >= 64:
            spk64 = np.asarray(spike_counts[:64], dtype=np.float64)
        elif len(state) >= kin_dim + 128:
            spk64 = np.asarray(state[kin_dim + 64:kin_dim + 128], dtype=np.float64)
        else:
            spk64 = None

        v64 = np.asarray(state[kin_dim:kin_dim + 64], dtype=np.float64) if len(state) >= kin_dim + 64 else None
        if spk64 is None and v64 is None:
            return None

        act = np.zeros(64, dtype=np.float64)
        if spk64 is not None:
            act += np.maximum(spk64, 0.0)
        if v64 is not None:
            act += np.abs(v64) * 10.0

        total = float(np.sum(act))
        if total <= 1e-9:
            return 0.0
        p = act / total
        p_nz = p[p > 1e-12]
        return float(-np.sum(p_nz * np.log2(p_nz)))

    def compute_variational_free_energy(
        self,
        state: np.ndarray,
        is_predictable_feedback: bool = True,
        spike_counts: Optional[np.ndarray] = None,
        prediction_error: Optional[float] = None,
        stim_dispersion_entropy: float = 0.0,
    ) -> float:
        """
        Computes variational free energy surrogate F(s) = Pragmatic Surprise + Entropy:
        - Live closed-loop path: genuine Shannon entropy of the 64-ch MEA neural state
          + differential predictive entropy from online generative-model error.
        - Low-dimensional kinematic-only fallback: Shannon entropy of coherent (1-channel)
          vs broadband chaotic (16-mode) sensory feedback distributions.
        """
        # Pragmatic surprise (divergence from prior preference: ball near paddle)
        delta = state[:5] - self.prior_target
        surprise = 0.5 * np.sum(self.prior_precisions * (delta ** 2))

        h_neural = self._compute_neural_shannon_entropy(state, spike_counts=spike_counts, kin_dim=5)
        err = self.last_pred_error if prediction_error is None else float(prediction_error)

        if h_neural is not None:
            h_pred = float(0.5 * np.log2(1.0 + (err / 0.05) ** 2))
            entropy = h_neural + h_pred + float(stim_dispersion_entropy)
        else:
            # Kinematic-only fallback (e.g. 5D unit-test state without MEA tensor)
            if is_predictable_feedback:
                p_fb = np.array([0.98, 0.02], dtype=np.float64)
            else:
                p_fb = np.full(16, 1.0 / 16.0, dtype=np.float64)
            entropy = float(-np.sum(p_fb * np.log2(p_fb)))

        return float(surprise + entropy)

    def select_action(
        self,
        obs: np.ndarray,
        spike_counts: Optional[np.ndarray] = None,
    ) -> Tuple[int, float]:
        """
        Evaluates Expected Free Energy G(a) using learned transition_weights[a]
        and organoid motor-bank spike alignment. Selects action minimizing G(a).
        """
        pong_state = obs[:5]
        expected_fe = np.zeros(self.action_dim, dtype=np.float32)

        # Read organoid motor spike bias (left: ch 60,62; right: ch 61,63)
        motor_bonus = np.zeros(self.action_dim, dtype=np.float32)
        if spike_counts is not None and len(spike_counts) >= 64:
            spk64 = np.asarray(spike_counts[:64], dtype=np.float32)
        elif len(obs) >= 133:
            spk64 = np.asarray(obs[5 + 64:5 + 128], dtype=np.float32)
        else:
            spk64 = None
        if spk64 is not None:
            left_m = float(spk64[60] + spk64[62])
            right_m = float(spk64[61] + spk64[63])
            tot_m = left_m + right_m
            if tot_m > 0.0:
                motor_bonus[0] = 0.25 * (left_m / tot_m)
                motor_bonus[1] = 0.25 * (right_m / tot_m)

        for a in range(self.action_dim):
            # Predict next kinematic state using online-learned generative transition model
            pred_state = np.dot(self.transition_weights[a], pong_state) + self.action_delta[a]
            pred_paddle_y = float(np.clip(pred_state[0], -0.8, 0.8))
            future_ball_y = float(pred_state[2] + pred_state[4])
            dist = abs(pred_paddle_y - future_ball_y)

            # Pragmatic expected free energy minus epistemic organoid motor coherence
            g_a = float(dist * 2.0) - float(motor_bonus[a])
            expected_fe[a] = g_a

        # Softmax selection over negative expected free energy (-G / temperature)
        logits = -expected_fe / max(self.temperature, 0.01)
        exp_logits = np.exp(logits - np.max(logits))
        probs = exp_logits / np.sum(exp_logits)

        action = int(np.random.choice(self.action_dim, p=probs))
        self.last_state = pong_state.copy()
        self.last_action = action

        return action, float(np.min(expected_fe))

    def update_generative_model(self, obs: np.ndarray, reward: float) -> float:
        """Online variational learning updating generative transition_weights."""
        if self.last_state is None:
            return 0.0
        current_pong = obs[:5]
        pred_state = np.dot(self.transition_weights[self.last_action], self.last_state) + self.action_delta[self.last_action]
        error = current_pong - pred_state

        # Variational gradient step with mild weight stabilization
        grad = np.outer(error, self.last_state)
        self.transition_weights[self.last_action] = np.clip(
            self.transition_weights[self.last_action] + self.lr * grad,
            -2.0,
            2.0,
        )
        err_norm = float(np.linalg.norm(error))
        self.last_pred_error = err_norm
        return err_norm


def run_pong_fep(
    episodes: int = 10,
    max_steps_per_episode: int = 200,
    seed: int = 42,
) -> Dict[str, Any]:
    """Runs closed-loop Active Inference / FEP DishBrain Pong benchmark."""
    np.random.seed(seed)

    print("=" * 78)
    print(" WetLang Closed-Loop AI Benchmark: DishBrain Pong Active Inference (FEP)")
    print("=" * 78)
    print(f" Episodes: {episodes} | Max Steps: {max_steps_per_episode} | Seed: {seed}")
    print(" Principle: Variational Free Energy & Sensory Entropy Minimization")
    print(" Feedback: 20 Hz Periodic (Hit) vs Chaotic Burst (Miss)")
    print(" Substrate: C99 MISRA-C Pre-Allocated Arena VM + Farama Gymnasium")
    print("-" * 78)

    env = DishBrainPongEnv(
        steps_per_action=5,
        max_steps=max_steps_per_episode,
        max_episode_steps=max_steps_per_episode * 3 + 10,
    )
    agent = ActiveInferenceFEPAgent(obs_dim=133, action_dim=2)

    history = {
        "episodes": [],
        "rewards": [],
        "hits": [],
        "misses": [],
        "rallies": [],
        "mean_free_energy": [],
        "prediction_errors": [],
    }

    t_start = time.time()
    zero_stim = np.zeros(4, dtype=np.float32)

    for ep in range(1, episodes + 1):
        obs, info = env.reset(seed=seed + ep)
        total_reward = 0.0
        ep_hits = 0
        ep_misses = 0
        max_rally = 0
        step_count = 0
        fe_list = []
        err_list = []

        is_predictable = True
        spike_counts = info.get("window_spike_counts")

        while True:
            step_count += 1
            action, expected_g = agent.select_action(obs, spike_counts=spike_counts)

            # Step environment
            obs, reward, terminated, truncated, info = env.step(action)
            spike_counts = info.get("window_spike_counts")
            total_reward += reward

            hit_occurred = info.get("hit_occurred", False)
            miss_occurred = info.get("miss_occurred", False)
            stim_entropy = 0.0
            fb_obs = obs

            if hit_occurred:
                ep_hits += 1
                is_predictable = True
                if not (terminated or truncated):
                    # Coherent periodic feedback on channel 4 + immediate C99 stepping
                    env.wetworld.inject_stimulus(4, 0.4, 0.1, 0.1)
                    wet_fb, _, _, _, fb_info = env.wetworld.step(zero_stim)
                    fb_obs = np.concatenate([obs[:5], wet_fb.astype(np.float32)])
                    spike_counts = fb_info.get("window_spike_counts", spike_counts)
            elif miss_occurred:
                ep_misses += 1
                is_predictable = False
                if not (terminated or truncated):
                    # Broadband chaotic stimulation across feedback channels 4..7 + immediate stepping
                    burst_v = np.random.uniform(-0.6, 0.6, size=4)
                    for idx, ch in enumerate(range(4, 8)):
                        v_pulse = float(burst_v[idx])
                        if abs(v_pulse) < 0.1:
                            v_pulse = 0.25 if v_pulse >= 0 else -0.25
                        env.wetworld.inject_stimulus(ch, v_pulse, 0.1, 0.1)
                    p_stim = np.abs(burst_v) / max(float(np.sum(np.abs(burst_v))), 1e-9)
                    p_nz = p_stim[p_stim > 1e-12]
                    stim_entropy = float(-np.sum(p_nz * np.log2(p_nz)))
                    wet_fb, _, _, _, fb_info = env.wetworld.step(zero_stim)
                    fb_obs = np.concatenate([obs[:5], wet_fb.astype(np.float32)])
                    spike_counts = fb_info.get("window_spike_counts", spike_counts)

            max_rally = max(max_rally, info.get("rally_count", 0))

            err = agent.update_generative_model(obs, reward)
            err_list.append(err)

            fe = agent.compute_variational_free_energy(
                fb_obs,
                is_predictable_feedback=is_predictable,
                spike_counts=spike_counts,
                prediction_error=err,
                stim_dispersion_entropy=stim_entropy,
            )
            fe_list.append(fe)

            if terminated or truncated:
                break

        mean_fe = float(np.mean(fe_list)) if fe_list else 0.0
        mean_err = float(np.mean(err_list)) if err_list else 0.0

        history["episodes"].append(ep)
        history["rewards"].append(total_reward)
        history["hits"].append(ep_hits)
        history["misses"].append(ep_misses)
        history["rallies"].append(max_rally)
        history["mean_free_energy"].append(mean_fe)
        history["prediction_errors"].append(mean_err)

        hit_rate = (ep_hits / (ep_hits + ep_misses)) * 100.0 if (ep_hits + ep_misses) > 0 else 0.0
        print(
            f" Ep {ep:2d}/{episodes:2d} | "
            f"Steps: {step_count:3d} | "
            f"Hits: {ep_hits:2d} | "
            f"Miss: {ep_misses:2d} | "
            f"HitRate: {hit_rate:5.1f}% | "
            f"MaxRally: {max_rally:2d} | "
            f"FreeEnergy F: {mean_fe:6.2f} | "
            f"PredError: {mean_err:5.3f} | "
            f"Reward: {total_reward:+6.2f}"
        )

    t_elapsed = time.time() - t_start
    env.close()

    total_hits = sum(history["hits"])
    total_misses = sum(history["misses"])
    overall_hit_rate = (total_hits / (total_hits + total_misses)) * 100.0 if (total_hits + total_misses) > 0 else 0.0
    mean_reward = float(np.mean(history["rewards"]))

    print("-" * 78)
    print(f" Active Inference Benchmark Complete in {t_elapsed:.2f}s ({episodes / t_elapsed:.1f} ep/s)")
    print(f" Total Hits: {total_hits} | Total Misses: {total_misses} | Overall Hit Rate: {overall_hit_rate:.1f}%")
    print(f" Mean Variational Free Energy: {np.mean(history['mean_free_energy']):.2f} | Mean Reward: {mean_reward:+.2f}")
    print("=" * 78)

    return history


def main():
    parser = argparse.ArgumentParser(description="DishBrain Pong Active Inference / FEP Benchmark")
    parser.add_argument("--episodes", type=int, default=10, help="Number of episodes")
    parser.add_argument("--max-steps", type=int, default=200, help="Maximum steps per episode")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()

    run_pong_fep(
        episodes=args.episodes,
        max_steps_per_episode=args.max_steps,
        seed=args.seed,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
