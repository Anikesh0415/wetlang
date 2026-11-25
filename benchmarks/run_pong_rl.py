"""
DishBrain Pong Reinforcement Learning Benchmark
===============================================
PyTorch Neural Policy Network coupled with Reward-Modulated STDP (R-STDP).
Operates in closed-loop with DishBrainPongEnv and WetworldGymEnv.

Plasticity Mechanics:
- Forward pass: Computes action probabilities pi(a|s) using PyTorch MLP.
- Hebbian Eligibility Trace:
    e_ij(t) = e_ij(t-1) * exp(-dt / tau_e) + (grad_log_pi)_{ij}
- Dopaminergic / Reward Modulation:
    delta_W = eta * (R(t) - R_baseline) * e_ij(t)
- Plasticity Metrics:
    - Weight Frobenius norm ||W||_F
    - Eligibility trace magnitude ||E||_1
    - Delta W norm ||delta_W||_F
    - Hit rate & rally lengths
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
import torch
import torch.nn as nn
import torch.nn.functional as F

from sandbox.gym_env import DishBrainPongEnv


class RSTDPPolicyNet(nn.Module):
    """
    2-Layer PyTorch Policy Network with Reward-Modulated STDP (R-STDP) Eligibility Traces.
    """
    def __init__(
        self,
        obs_dim: int = 133,
        hidden_dim: int = 64,
        action_dim: int = 2,
        lr: float = 0.005,
        tau_e: float = 20.0,  # Eligibility trace decay time constant (steps)
        gamma_baseline: float = 0.95,  # Moving average baseline decay
    ):
        super().__init__()
        self.obs_dim = obs_dim
        self.hidden_dim = hidden_dim
        self.action_dim = action_dim
        self.lr = lr
        self.decay_e = float(np.exp(-1.0 / tau_e))
        self.gamma_baseline = gamma_baseline

        # Synaptic layers + biological motor-spike coupling gain
        self.fc1 = nn.Linear(obs_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, action_dim)
        self.motor_gain = nn.Parameter(torch.tensor([0.25], dtype=torch.float32))

        # Initialize eligibility traces matching weight matrices
        self.e1 = torch.zeros_like(self.fc1.weight.data)
        self.e2 = torch.zeros_like(self.fc2.weight.data)

        # Baseline reward tracker for advantage estimation
        self.running_reward = 0.0
        self.total_plasticity_updates = 0

    def forward(
        self,
        x: torch.Tensor,
        motor_bias: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        h = torch.tanh(self.fc1(x))
        logits = self.fc2(h)
        if motor_bias is not None:
            logits = logits + self.motor_gain * motor_bias
        probs = F.softmax(logits, dim=-1)
        return probs, h

    @staticmethod
    def _compute_motor_bias(
        obs: np.ndarray,
        spike_counts: Optional[np.ndarray] = None,
        kin_dim: int = 5,
    ) -> torch.Tensor:
        """Extracts organoid motor-bank spike asymmetry (channels 60,62 vs 61,63)."""
        if spike_counts is not None and len(spike_counts) >= 64:
            spk64 = np.asarray(spike_counts[:64], dtype=np.float32)
        elif len(obs) >= kin_dim + 128:
            spk64 = np.asarray(obs[kin_dim + 64:kin_dim + 128], dtype=np.float32)
        else:
            return torch.zeros((1, 2), dtype=torch.float32)

        left_act = float(spk64[60] + spk64[62])
        right_act = float(spk64[61] + spk64[63])
        return torch.tensor([[left_act, right_act]], dtype=torch.float32)

    def select_action(
        self,
        obs: np.ndarray,
        spike_counts: Optional[np.ndarray] = None,
    ) -> Tuple[int, torch.Tensor, torch.Tensor]:
        """Selects discrete action coupled with organoid motor spikes and updates eligibility traces."""
        x = torch.from_numpy(obs).float().unsqueeze(0)
        motor_bias = self._compute_motor_bias(obs, spike_counts=spike_counts, kin_dim=5)
        probs, h = self.forward(x, motor_bias=motor_bias)
        dist = torch.distributions.Categorical(probs)
        action = dist.sample()

        # Compute gradient of log pi(a|s) with respect to layer weights
        log_prob = dist.log_prob(action)
        self.zero_grad()
        log_prob.backward()

        with torch.no_grad():
            # Update eligibility traces: E <- E * decay + grad
            if self.fc1.weight.grad is not None:
                self.e1 = self.e1 * self.decay_e + self.fc1.weight.grad
            if self.fc2.weight.grad is not None:
                self.e2 = self.e2 * self.decay_e + self.fc2.weight.grad

        return int(action.item()), probs.detach(), h.detach()

    def update_rstdp(self, reward: float) -> Dict[str, float]:
        """
        Applies dopamine/reward modulation to eligibility traces:
        delta_W = lr * (R - baseline) * E
        """
        with torch.no_grad():
            advantage = reward - self.running_reward
            self.running_reward = (
                self.gamma_baseline * self.running_reward + (1.0 - self.gamma_baseline) * reward
            )

            # Modulate weights by advantage and eligibility traces
            delta_w1 = self.lr * advantage * self.e1
            delta_w2 = self.lr * advantage * self.e2

            self.fc1.weight.data += delta_w1
            self.fc2.weight.data += delta_w2

            # Compute plasticity metrics
            norm_w = float(torch.norm(self.fc1.weight.data) + torch.norm(self.fc2.weight.data))
            norm_e = float(torch.sum(torch.abs(self.e1)) + torch.sum(torch.abs(self.e2)))
            norm_delta = float(torch.norm(delta_w1) + torch.norm(delta_w2))
            self.total_plasticity_updates += 1

            return {
                "norm_w": norm_w,
                "norm_e": norm_e,
                "norm_delta": norm_delta,
                "advantage": float(advantage),
                "running_reward": float(self.running_reward),
            }

    def reset_traces(self) -> None:
        """Resets eligibility traces between episodes."""
        self.e1.zero_()
        self.e2.zero_()


def _apply_biological_rstdp(wetworld: Any, action: int, advantage: float) -> None:
    """
    Couples reward advantage into the C99 biological organoid substrate:
    - Uses WetworldGymEnv.modulate_stdp(pre, post, dw) when available to directly
      potentiate/depress sensory (0..3) -> motor (60..63) synapses.
    - Otherwise pairs a safe charge-balanced associative reinforcement pulse (0.25 V)
      onto the rewarded motor bank (60,62 or 61,63) to drive native C99 STDP.
    """
    if abs(advantage) < 1e-3:
        return

    target_bank = (61, 63) if (action == 1 and advantage > 0) or (action == 0 and advantage < 0) else (60, 62)
    modulate_fn = getattr(wetworld, "modulate_stdp", None)
    if callable(modulate_fn):
        dw_ns = float(np.clip(0.05 * advantage, -0.5, 0.5))
        for pre in range(4):
            for post in target_bank:
                modulate_fn(pre, post, dw_ns)
        return

    # Fallback associative Hebbian pairing on motor channels (never overwritten by sensory encoders)
    for ch in target_bank:
        wetworld.inject_stimulus(ch, 0.25, 0.1, 0.1)


def run_pong_rl(
    episodes: int = 10,
    max_steps_per_episode: int = 200,
    seed: int = 42,
    render: bool = False,
) -> Dict[str, Any]:
    """Runs closed-loop DishBrain Pong RL training benchmark with R-STDP."""
    torch.manual_seed(seed)
    np.random.seed(seed)

    print("=" * 78)
    print(" WetLang Closed-Loop AI Benchmark: DishBrain Pong RL (R-STDP)")
    print("=" * 78)
    print(f" Episodes: {episodes} | Max Steps: {max_steps_per_episode} | Seed: {seed}")
    print(" Learning Rule: Reward-Modulated STDP (PyTorch Traces + C99 Organoid STDP)")
    print(" Substrate: C99 MISRA-C Pre-Allocated Arena VM + Farama Gymnasium")
    print("-" * 78)

    env = DishBrainPongEnv(steps_per_action=5, max_steps=max_steps_per_episode)
    policy = RSTDPPolicyNet(obs_dim=133, hidden_dim=64, action_dim=2, lr=0.01)

    history = {
        "episodes": [],
        "rewards": [],
        "hits": [],
        "misses": [],
        "rallies": [],
        "weight_norms": [],
        "trace_magnitudes": [],
        "delta_norms": [],
        "bio_weight_drifts": [],
    }

    t_start = time.time()

    for ep in range(1, episodes + 1):
        obs, info = env.reset(seed=seed + ep)
        policy.reset_traces()
        w_bio_init = env.wetworld.get_synapse_matrix()
        total_reward = 0.0
        ep_hits = 0
        ep_misses = 0
        max_rally = 0
        step_count = 0
        last_metrics = {"norm_w": 0.0, "norm_e": 0.0, "norm_delta": 0.0}
        spike_counts = info.get("window_spike_counts")

        while True:
            step_count += 1
            action, probs, _ = policy.select_action(obs, spike_counts=spike_counts)
            obs, reward, terminated, truncated, info = env.step(action)
            spike_counts = info.get("window_spike_counts")
            total_reward += reward

            if info.get("hit_occurred"):
                ep_hits += 1
            if info.get("miss_occurred"):
                ep_misses += 1
            max_rally = max(max_rally, info.get("rally_count", 0))

            # Apply R-STDP update modulated by immediate step reward
            last_metrics = policy.update_rstdp(reward)
            if not (terminated or truncated):
                _apply_biological_rstdp(env.wetworld, action, last_metrics["advantage"])

            if terminated or truncated:
                break

        w_bio_end = env.wetworld.get_synapse_matrix()
        bio_drift_ns = float(np.sum(np.abs(w_bio_end - w_bio_init)))

        # Log episode metrics
        history["episodes"].append(ep)
        history["rewards"].append(total_reward)
        history["hits"].append(ep_hits)
        history["misses"].append(ep_misses)
        history["rallies"].append(max_rally)
        history["weight_norms"].append(last_metrics["norm_w"])
        history["trace_magnitudes"].append(last_metrics["norm_e"])
        history["delta_norms"].append(last_metrics["norm_delta"])
        history["bio_weight_drifts"].append(bio_drift_ns)

        hit_rate = (ep_hits / (ep_hits + ep_misses)) * 100.0 if (ep_hits + ep_misses) > 0 else 0.0
        print(
            f" Ep {ep:2d}/{episodes:2d} | "
            f"Steps: {step_count:3d} | "
            f"Hits: {ep_hits:2d} | "
            f"Miss: {ep_misses:2d} | "
            f"HitRate: {hit_rate:5.1f}% | "
            f"MaxRally: {max_rally:2d} | "
            f"Reward: {total_reward:+6.2f} | "
            f"||W||: {last_metrics['norm_w']:5.2f} | "
            f"||E||: {last_metrics['norm_e']:6.2f} | "
            f"||dW||: {last_metrics['norm_delta']:6.4f} | "
            f"Bio|dW|: {bio_drift_ns:5.2f} nS"
        )

    t_elapsed = time.time() - t_start
    env.close()

    total_hits = sum(history["hits"])
    total_misses = sum(history["misses"])
    overall_hit_rate = (total_hits / (total_hits + total_misses)) * 100.0 if (total_hits + total_misses) > 0 else 0.0
    mean_reward = float(np.mean(history["rewards"]))

    print("-" * 78)
    print(f" Training Complete in {t_elapsed:.2f}s ({episodes / t_elapsed:.1f} ep/s)")
    print(f" Total Hits: {total_hits} | Total Misses: {total_misses} | Overall Hit Rate: {overall_hit_rate:.1f}%")
    print(f" Mean Episode Reward: {mean_reward:+.2f} | Final Synaptic Norm: {history['weight_norms'][-1]:.2f}")
    print("=" * 78)

    return history


def main():
    parser = argparse.ArgumentParser(description="DishBrain Pong PyTorch RL with R-STDP")
    parser.add_argument("--episodes", type=int, default=10, help="Number of training episodes")
    parser.add_argument("--max-steps", type=int, default=200, help="Maximum steps per episode")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--render", action="store_true", help="Render environment")
    args = parser.parse_args()

    run_pong_rl(
        episodes=args.episodes,
        max_steps_per_episode=args.max_steps,
        seed=args.seed,
        render=args.render,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
