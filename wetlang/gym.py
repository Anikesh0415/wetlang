"""
WetLang Gymnasium Standard RL Interface
Exports WetworldGymEnv for Farama Gymnasium / PyTorch Reinforcement Learning agents.
"""

from sandbox.gym_env import WetworldGymEnv

def make(env_name: str = "Wetworld-v1", **kwargs) -> WetworldGymEnv:
    """Factory helper matching gym.make('Wetworld-v1')."""
    return WetworldGymEnv(**kwargs)

__all__ = ["WetworldGymEnv", "make"]
