"""
WetLang Numerical ODE Solver: Conductance-Based Leaky Integrate-and-Fire (COBA-LIF)
Implements Exact Exponential Euler integration at fixed dt = 0.1 ms,
2.0 ms absolute refractory hard clamp, dynamic threshold elevation, and slow AHP adaptation.
"""

import math
from typing import List, Tuple


class LifODESolver:
    """
    Exact Exponential Euler ODE solver for COBA-LIF dynamics.
    Integrates sub-threshold membrane potentials, synaptic conductances,
    and enforces absolute/relative refractory limits.
    """

    def __init__(self, dt_ms: float = 0.1):
        self.dt_ms: float = dt_ms

    def step_passive(self, v_init: float, tau_m: float, v_rest: float) -> float:
        """
        Exact Exponential Euler passive membrane relaxation toward resting potential.
        V(t + dt) = V_rest + (V(t) - V_rest) * exp(-dt / tau_m)
        """
        decay = math.exp(-self.dt_ms / tau_m)
        return v_rest + (v_init - v_rest) * decay

    def decay_conductance(self, g: float, tau_ms: float) -> float:
        """
        Exponential synaptic conductance decay.
        g(t + dt) = g(t) * exp(-dt / tau_ms)
        """
        return g * math.exp(-self.dt_ms / tau_ms)

    def update_neuron(self, v_m: float, v_thresh: float, v_reset: float) -> Tuple[bool, float]:
        """
        Evaluates action potential threshold crossing and reset.
        Returns (spiked: bool, v_new: float).
        """
        if v_m >= v_thresh:
            return (True, v_reset)
        return (False, v_m)

    def simulate_refractory(self, v_init: float, current_inj: float, ticks: int) -> List[float]:
        """
        Simulates absolute refractory hard clamp: membrane potential remains pinned at v_init
        regardless of injected current.
        """
        return [v_init] * ticks

    def decrement_refractory(self, counter: int) -> int:
        """Decrements remaining absolute refractory ticks toward zero."""
        return max(0, counter - 1)

    def simulate_continuous_stimulus(
        self,
        current_pA: float,
        duration_ms: float,
        c_m_pf: float = 200.0,
        g_leak_ns: float = 10.0,
        v_rest_mv: float = -70.0,
        v_reset_mv: float = -75.0,
        v_thresh_base_mv: float = -50.0,
        abs_refract_ms: float = 2.0,
    ) -> List[int]:
        """
        Simulates neuron response to sustained strong current injection with 2.0 ms refractory clamp.
        Returns list of spike tick indices.
        Enforces maximum firing frequency of 500 Hz (at least 20 ticks between spikes).
        """
        total_ticks = int(duration_ms / self.dt_ms)
        refract_ticks_total = int(abs_refract_ms / self.dt_ms)

        v_m = v_rest_mv
        v_thresh = v_thresh_base_mv
        refract_remaining = 0
        spikes: List[int] = []

        tau_m = c_m_pf / g_leak_ns # 20.0 ms

        for t in range(total_ticks):
            if refract_remaining > 0:
                refract_remaining -= 1
                v_m = v_reset_mv
            else:
                # Steady-state voltage under current injection: V_inf = V_rest + I / g_leak
                # current in pA (1e-12 A), g_leak in nS (1e-9 S) -> 1 pA / 1 nS = 1 mV
                v_inf = v_rest_mv + (current_pA / g_leak_ns)
                decay = math.exp(-self.dt_ms / tau_m)
                v_m = v_inf + (v_m - v_inf) * decay

                if v_m >= v_thresh:
                    spikes.append(t)
                    v_m = v_reset_mv
                    refract_remaining = refract_ticks_total

            # Dynamic threshold decay
            v_thresh = v_thresh_base_mv + (v_thresh - v_thresh_base_mv) * math.exp(-self.dt_ms / 10.0)

        return spikes

    def elevate_threshold(self, base_thresh: float, delta: float) -> float:
        """Dynamic threshold elevation for relative refractory period (+15 mV)."""
        return base_thresh + delta

    def activate_ahp(self, g_current: float, delta_g: float) -> float:
        """Activates slow after-hyperpolarization (AHP) potassium conductance jump (+2..4 nS)."""
        return g_current + delta_g
