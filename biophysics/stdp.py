"""
WetLang Pairwise Spike-Timing-Dependent Plasticity (STDP)
Implements online exponential trace STDP with 1.05x depression bias (A_- / A_+ == 1.05),
hard bounding within [w_min, w_max], and Dale's principle preservation on inhibitory synapses.
"""

import math


class PairwiseSTDP:
    """
    Pairwise Spike-Timing-Dependent Plasticity rule.
    Potentiates synapses when pre spikes before post (delta_t > 0).
    Depresses synapses when post spikes before pre (delta_t < 0) with a 1.05x LTD bias.
    """

    def __init__(
        self,
        tau_plus_ms: float = 20.0,
        tau_minus_ms: float = 20.0,
        a_plus: float = 0.20,
        a_minus: float = 0.21,
        w_min: float = 0.0,
        w_max: float = 40.0,
    ):
        self.tau_plus_ms: float = tau_plus_ms
        self.tau_minus_ms: float = tau_minus_ms
        self.a_plus: float = a_plus
        self.a_minus: float = a_minus
        self.w_min: float = w_min
        self.w_max: float = w_max

    def compute_delta_w(self, delta_t_ms: float) -> float:
        """
        Calculates synaptic weight change delta_w (in nS) for a spike timing difference
        delta_t_ms = t_post - t_pre.
          delta_t > 0: LTP  -> +a_plus * exp(-delta_t / tau_plus)
          delta_t < 0: LTD  -> -a_minus * exp(-|delta_t| / tau_minus)
          delta_t == 0: 0.0
        """
        if delta_t_ms > 0.0:
            return self.a_plus * math.exp(-delta_t_ms / self.tau_plus_ms)
        elif delta_t_ms < 0.0:
            return -self.a_minus * math.exp(delta_t_ms / self.tau_minus_ms)
        else:
            return 0.0

    def decay_trace(self, init_val: float, elapsed_ms: float) -> float:
        """
        Exponential decay of pre/post synaptic eligibility traces.
        trace(t) = init_val * exp(-elapsed_ms / tau_plus_ms)
        """
        return init_val * math.exp(-elapsed_ms / self.tau_plus_ms)

    def update_weight(self, w_init: float, is_inhibitory: bool, delta_t_ms: float) -> float:
        """
        Applies STDP update to a synaptic weight under Dale's principle.
        Inhibitory synapses do not undergo STDP.
        Excitatory synapses are updated and hard-bounded in [w_min, w_max].
        """
        if is_inhibitory:
            return w_init

        dw = self.compute_delta_w(delta_t_ms)
        w_new = w_init + dw
        if w_new < self.w_min:
            return self.w_min
        if w_new > self.w_max:
            return self.w_max
        return w_new
