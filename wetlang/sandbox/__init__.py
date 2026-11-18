"""
Wetworld Universal Multi-Organoid Sandbox & Cross-Framework Verification Suite
=============================================================================
Provides:
1. UniversalOrganoidSandbox: Scalable multi-organoid cluster orchestration (1 to N organoids).
2. WetworldGymEnv: Farama Gymnasium (OpenAI Gym) standardized RL/active inference environment.
3. SnnTorchCrossValidator: Mathematical ODE & spike validation against external SNN framework.
"""

from .universal_organoid_sandbox import UniversalOrganoidSandbox, OrganoidNode
from .gym_env import WetworldGymEnv

__all__ = [
    "UniversalOrganoidSandbox",
    "OrganoidNode",
    "WetworldGymEnv",
]
