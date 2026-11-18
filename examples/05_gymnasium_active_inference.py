"""
Example 05: Farama Gymnasium Reinforcement Learning & Active Inference Loop
Demonstrates training a closed-loop agent on living neural tissue dynamics.
"""

import numpy as np
from wetlang import WetworldGymEnv


def run_active_inference_agent(episodes: int = 5, steps_per_episode: int = 50):
    print("Initializing Wetworld Farama Gymnasium Environment...")
    env = WetworldGymEnv(steps_per_action=5)

    for ep in range(1, episodes + 1):
        obs, info = env.reset()
        total_reward = 0.0
        print(f"\n--- Starting Episode {ep}/{episodes} ---")
        print(f"Initial Observation shape: {obs.shape} | Baseline Rate: {info['population_rate_hz']:.1f} Hz")

        for step in range(1, steps_per_episode + 1):
            # Target stimulation policy: sample charge-balanced biphasic pulses
            action = env.action_space.sample()

            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward

            if step % 10 == 0 or step == steps_per_episode:
                print(f"  Step {step:2d} | Firing Rate: {info['population_rate_hz']:5.1f} Hz | Step Reward: {reward:+.3f} | Cumulative: {total_reward:+.3f}")

            if terminated or truncated:
                print("Episode terminated early.")
                break

        print(f"Episode {ep} Finished. Total Homeostatic Reward: {total_reward:.3f}")

    env.close()
    print("\nActive inference agent execution finished.")


if __name__ == "__main__":
    run_active_inference_agent()
