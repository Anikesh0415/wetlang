"""
WetLang Tsodyks-Markram Short-Term Plasticity (STP)
Simulates short-term synaptic depression (vesicle depletion) and facilitation
across four cortical synapse classes: E->E, E->I, I->E, and I->I.
"""

import math
from typing import List, Optional


class SynapseSTP:
    """
    Tsodyks-Markram short-term synaptic plasticity model.
    Tracks vesicle fraction x (0..1) and release probability u (0..1).
    """

    def __init__(
        self,
        synapse_type: str = "E->E",
        tau_rec_ms: Optional[float] = None,
        weight_ns: float = 10.0,
    ):
        self.synapse_type: str = synapse_type
        self.weight_ns: float = weight_ns

        # Cortical synapse class parameterization
        if synapse_type == "E->E":
            self.U_base: float = 0.50
            self.tau_rec_ms: float = 800.0
            self.tau_fac_ms: float = 20.0
        elif synapse_type == "E->I":
            self.U_base: float = 0.15
            self.tau_rec_ms: float = 200.0
            self.tau_fac_ms: float = 600.0
        elif synapse_type == "I->E":
            self.U_base: float = 0.25
            self.tau_rec_ms: float = 700.0
            self.tau_fac_ms: float = 50.0
        elif synapse_type == "I->I":
            self.U_base: float = 0.30
            self.tau_rec_ms: float = 400.0
            self.tau_fac_ms: float = 50.0
        else:
            self.U_base = 0.50
            self.tau_rec_ms = 800.0
            self.tau_fac_ms = 20.0

        if tau_rec_ms is not None:
            self.tau_rec_ms = float(tau_rec_ms)

        self.u: float = self.U_base
        self.x: float = 1.0

    def deliver_spikes(self, count: int, freq_hz: float) -> List[float]:
        """
        Delivers a regular spike train at freq_hz and returns the list of
        effective post-synaptic conductance jumps (nS) produced at each spike.
        """
        if count <= 0:
            return []

        interval_ms = 1000.0 / freq_hz if freq_hz > 0 else 100.0
        g_jumps: List[float] = []

        u = self.U_base
        x = 1.0

        for i in range(count):
            # Facilitation update on spike arrival
            u = u + self.U_base * (1.0 - u)
            # Conductance jump proportional to released vesicles
            g = self.weight_ns * (u * x)
            g_jumps.append(g)

            # Vesicle depletion
            x = x - (u * x)

            # Recovery during inter-spike interval
            if i < count - 1:
                u = self.U_base + (u - self.U_base) * math.exp(-interval_ms / self.tau_fac_ms)
                x = 1.0 - (1.0 - x) * math.exp(-interval_ms / self.tau_rec_ms)

        return g_jumps

    def track_utilization(self, count: int, freq_hz: float) -> List[float]:
        """
        Delivers a regular spike train and returns the utilization parameter u
        immediately after each spike arrival.
        """
        if count <= 0:
            return []

        interval_ms = 1000.0 / freq_hz if freq_hz > 0 else 100.0
        u_vals: List[float] = []

        u = self.U_base

        for i in range(count):
            u = u + self.U_base * (1.0 - u)
            u_vals.append(u)

            if i < count - 1:
                u = self.U_base + (u - self.U_base) * math.exp(-interval_ms / self.tau_fac_ms)

        return u_vals

    def recover(self, r_init: float, delta_t_ms: float) -> float:
        """
        Calculates recovered vesicle fraction R after a quiescent interval delta_t_ms.
        R = 1.0 - (1.0 - r_init) * exp(-delta_t_ms / tau_rec_ms)
        """
        return 1.0 - (1.0 - r_init) * math.exp(-delta_t_ms / self.tau_rec_ms)
