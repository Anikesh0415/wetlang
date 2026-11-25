"""
Organoid CartPole Active Inference / Free Energy Principle (FEP) Benchmark
==========================================================================
Biological agent balancing an inverted pendulum by minimizing variational free energy.
Operates in closed-loop with OrganoidCartPoleEnv and WetworldGymEnv.

Active Inference Protocol:
- Balanced Upright (|theta| <= 0.05 rad):
    Predictable 20 Hz periodic sensory pulses delivered to sensory channels.
    Sensory entropy H -> low, Variational Free Energy F -> low.
- Tilted / Falling (|theta| > 0.08 rad):
    Unpredictable high-entropy chaotic stimulation bursts.
    Sensory entropy H -> high, Variational Free Energy F -> high.
- Action Selection:
    Agent evaluates Expected Free Energy G(a) for Left/Right motor actions
    to maintain low-entropy upright sensory equilibrium.
"""

import sys
import os
import argparse
import time
from pathlib import Path
from typing import Tuple, Dict, Any, Optional

# Ensure root repository directory is in sys.path
_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

import numpy as np

from sandbox.gym_env import OrganoidCartPoleEnv


class CartPoleFEPAgent:
    """
    Active Inference Agent for CartPole Balancing.
    Maintains a predictive generative model of cart-pole kinematics.
    """
    def __init__(
        self,
        obs_dim: int = 132,
        action_dim: int = 2,
        learning_rate: float = 0.05,
        temperature: float = 0.5,
    ):
        self.obs_dim = obs_dim
        self.action_dim = action_dim
        self.lr = learning_rate
        self.temperature = temperature

        # Generative model transition matrices for 4 cartpole states [x, x_dot, theta, theta_dot]
        self.transition_weights = np.zeros((action_dim, 4, 4), dtype=np.float32)
        for a in range(action_dim):
            self.transition_weights[a] = np.eye(4, dtype=np.float32)
            self.transition_weights[a, 0, 1] = 0.02
            self.transition_weights[a, 2, 3] = 0.02
        self.action_delta = np.array([
            [0.0, -0.20, 0.0, +0.03],  # a=0: push left
            [0.0, +0.20, 0.0, -0.03],  # a=1: push right
        ], dtype=np.float32)

        # Prior preferences: upright pole (theta=0, theta_dot=0, cart centered x=0)
        self.prior_target = np.array([0.0, 0.0, 0.0, 0.0], dtype=np.float32)
        self.prior_precisions = np.array([1.0, 0.5, 20.0, 5.0], dtype=np.float32)

        self.last_state = None
        self.last_action = 0
        self.last_pred_error = 0.0

    @staticmethod
    def _compute_neural_shannon_entropy(
        state: np.ndarray,
        spike_counts: Optional[np.ndarray] = None,
        kin_dim: int = 4,
    ) -> Optional[float]:
        """
        Computes Shannon entropy H = -sum(p_ch * log2(p_ch)) across the 64 MEA
        channels from observed spike counts and extracellular voltage energy.
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
        is_predictable: bool = True,
        spike_counts: Optional[np.ndarray] = None,
        prediction_error: Optional[float] = None,
        stim_dispersion_entropy: float = 0.0,
    ) -> float:
        """Computes variational free energy surrogate F(s) = Pragmatic Surprise + Shannon/Predictive Entropy."""
        delta = state[:4] - self.prior_target
        surprise = 0.5 * np.sum(self.prior_precisions * (delta ** 2))

        h_neural = self._compute_neural_shannon_entropy(state, spike_counts=spike_counts, kin_dim=4)
        err = self.last_pred_error if prediction_error is None else float(prediction_error)

        if h_neural is not None:
            h_pred = float(0.5 * np.log2(1.0 + (err / 0.05) ** 2))
            entropy = h_neural + h_pred + float(stim_dispersion_entropy)
        else:
            p_fb = np.array([0.98, 0.02], dtype=np.float64) if is_predictable else np.full(16, 1.0 / 16.0, dtype=np.float64)
            entropy = float(-np.sum(p_fb * np.log2(p_fb)))

        return float(surprise + entropy)

    def select_action(
        self,
        obs: np.ndarray,
        spike_counts: Optional[np.ndarray] = None,
    ) -> Tuple[int, float]:
        """Selects action minimizing Expected Free Energy G(a) using learned transition_weights."""
        cartpole_state = obs[:4]
        expected_fe = np.zeros(self.action_dim, dtype=np.float32)

        motor_bonus = np.zeros(self.action_dim, dtype=np.float32)
        if spike_counts is not None and len(spike_counts) >= 64:
            spk64 = np.asarray(spike_counts[:64], dtype=np.float32)
        elif len(obs) >= 132:
            spk64 = np.asarray(obs[4 + 64:4 + 128], dtype=np.float32)
        else:
            spk64 = None
        if spk64 is not None:
            left_m = float(spk64[60] + spk64[62])
            right_m = float(spk64[61] + spk64[63])
            tot_m = left_m + right_m
            if tot_m > 0.0:
                motor_bonus[0] = 0.15 * (left_m / tot_m)
                motor_bonus[1] = 0.15 * (right_m / tot_m)

        for a in range(self.action_dim):
            pred_state = np.dot(self.transition_weights[a], cartpole_state) + self.action_delta[a]
            pred_x, _, pred_theta, pred_theta_dot = pred_state

            g_a = (
                20.0 * (float(pred_theta) ** 2)
                + 5.0 * (float(pred_theta_dot) ** 2)
                + 1.0 * (float(pred_x) ** 2)
                - float(motor_bonus[a])
            )
            expected_fe[a] = float(g_a)

        logits = -expected_fe / max(self.temperature, 0.01)
        exp_logits = np.exp(logits - np.max(logits))
        probs = exp_logits / np.sum(exp_logits)

        action = int(np.random.choice(self.action_dim, p=probs))
        self.last_state = cartpole_state.copy()
        self.last_action = action

        return action, float(np.min(expected_fe))

    def update_generative_model(self, obs: np.ndarray) -> float:
        """Online variational learning of cartpole transitions."""
        if self.last_state is None:
            return 0.0
        current_state = obs[:4]
        pred_state = np.dot(self.transition_weights[self.last_action], self.last_state) + self.action_delta[self.last_action]
        error = current_state - pred_state

        grad = np.outer(error, self.last_state)
        self.transition_weights[self.last_action] = np.clip(
            self.transition_weights[self.last_action] + self.lr * grad,
            -3.0,
            3.0,
        )
        err_norm = float(np.linalg.norm(error))
        self.last_pred_error = err_norm
        return err_norm


def run_cartpole_fep(
    episodes: int = 10,
    max_steps_per_episode: int = 300,
    seed: int = 42,
) -> Dict[str, Any]:
    """Runs closed-loop Active Inference / FEP CartPole balancing benchmark."""
    np.random.seed(seed)

    print("=" * 78)
    print(" WetLang Closed-Loop AI Benchmark: Organoid CartPole Active Inference (FEP)")
    print("=" * 78)
    print(f" Episodes: {episodes} | Max Steps: {max_steps_per_episode} | Seed: {seed}")
    print(" Principle: Variational Free Energy & Sensory Entropy Minimization")
    print(" Feedback: 20 Hz Coherent (Upright) vs Chaotic Multi-Channel Burst (Tilted)")
    print(" Substrate: C99 MISRA-C Pre-Allocated Arena VM + Farama Gymnasium")
    print("-" * 78)

    env = OrganoidCartPoleEnv(
        steps_per_action=5,
        max_steps=max_steps_per_episode,
        max_episode_steps=max_steps_per_episode * 3 + 10,
    )
    agent = CartPoleFEPAgent(obs_dim=132, action_dim=2)

    history = {
        "episodes": [],
        "survival_steps": [],
        "rewards": [],
        "mean_free_energy": [],
        "prediction_errors": [],
    }

    t_start = time.time()
    zero_stim = np.zeros(4, dtype=np.float32)

    for ep in range(1, episodes + 1):
        obs, info = env.reset(seed=seed + ep)
        total_reward = 0.0
        step_count = 0
        fe_list = []
        err_list = []
        spike_counts = info.get("window_spike_counts")

        while True:
            step_count += 1
            action, expected_g = agent.select_action(obs, spike_counts=spike_counts)

            obs, reward, terminated, truncated, info = env.step(action)
            spike_counts = info.get("window_spike_counts")
            total_reward += reward

            theta = info.get("theta", 0.0)
            is_upright = abs(theta) <= 0.05
            stim_entropy = 0.0
            fb_obs = obs

            if not (terminated or truncated):
                if is_upright:
                    # Coherent periodic feedback on channel 4 + immediate C99 stepping
                    env.wetworld.inject_stimulus(4, 0.4, 0.1, 0.1)
                else:
                    # Broadband chaotic burst across feedback channels 4..7 + immediate stepping
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
                fb_obs = np.concatenate([obs[:4], wet_fb.astype(np.float32)])
                spike_counts = fb_info.get("window_spike_counts", spike_counts)

            err = agent.update_generative_model(obs)
            err_list.append(err)

            fe = agent.compute_variational_free_energy(
                fb_obs,
                is_predictable=is_upright,
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
        history["survival_steps"].append(step_count)
        history["rewards"].append(total_reward)
        history["mean_free_energy"].append(mean_fe)
        history["prediction_errors"].append(mean_err)

        print(
            f" Ep {ep:2d}/{episodes:2d} | "
            f"Steps Survived: {step_count:3d}/{max_steps_per_episode:3d} | "
            f"FreeEnergy F: {mean_fe:6.2f} | "
            f"PredError: {mean_err:5.3f} | "
            f"Reward: {total_reward:+6.2f}"
        )

    t_elapsed = time.time() - t_start
    env.close()

    mean_steps = float(np.mean(history["survival_steps"]))
    max_steps_seen = int(np.max(history["survival_steps"]))
    mean_reward = float(np.mean(history["rewards"]))

    print("-" * 78)
    print(f" Active Inference Benchmark Complete in {t_elapsed:.2f}s ({episodes / t_elapsed:.1f} ep/s)")
    print(f" Mean Steps Survived: {mean_steps:.1f} | Max Steps Survived: {max_steps_seen}")
    print(f" Mean Variational Free Energy: {np.mean(history['mean_free_energy']):.2f} | Mean Reward: {mean_reward:+.2f}")
    print("=" * 78)

    return history


def main():
    parser = argparse.ArgumentParser(description="Organoid CartPole Active Inference / FEP Benchmark")
    parser.add_argument("--episodes", type=int, default=10, help="Number of episodes")
    parser.add_argument("--max-steps", type=int, default=300, help="Maximum steps per episode")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()

    run_cartpole_fep(
        episodes=args.episodes,
        max_steps_per_episode=args.max_steps,
        seed=args.seed,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
