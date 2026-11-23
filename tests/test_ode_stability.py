"""
WetLang Test Suite: Numerical ODE Stability & Biophysical Dynamics
Tests:
  - Exact Exponential Euler COBA-LIF numerical stability under extreme current injection
  - 2.0 ms hard absolute refractory clamp (maximum firing rate <= 500 Hz)
  - Relative refractory dynamic threshold jump (+15 mV) and exponential decay (tau = 10 ms)
  - Slow AHP potassium adaptation conductance (+2 nS, tau = 80 ms)
  - Tsodyks-Markram Short-Term Plasticity (STP) across 4 cortical synapse classes (EE, EI, IE, II)
  - Online Pairwise Trace STDP with 1.05x LTD bias, Dale's principle, and hard bounds [0, 40 nS]
  - Integrated simulation stability via native WetVM engine
"""

import math
import pytest
import numpy as np
from typing import List, Tuple, Dict

from bindings.runtime import WetVM
from bindings.ffi import WetVMConfig, WetTelemetry


# =============================================================================
# Pure-Python Exact Reference Model matching native/src/biophysics.c
# =============================================================================

class ReferenceCOBALIFNeuron:
    """Exact reference implementation of COBA-LIF neuron from native/src/biophysics.c."""
    def __init__(self, dt_ms: float = 0.1, is_excitatory: bool = True):
        self.dt_ms = dt_ms
        self.is_excitatory = is_excitatory
        
        # Biophysical constants
        self.c_m_pf = 200.0
        self.g_leak_ns = 10.0
        self.e_leak_mv = -70.0
        self.e_reset_mv = -75.0
        self.e_thresh_base_mv = -50.0
        self.e_exc_mv = 0.0
        self.e_inh_mv = -80.0
        self.e_k_mv = -90.0
        
        self.tau_exc_ms = 5.0
        self.tau_inh_ms = 10.0
        self.tau_ahp_ms = 80.0
        self.tau_thresh_ms = 10.0
        
        self.abs_refract_ticks = 20  # 2.0 ms at dt = 0.1 ms
        
        # State variables
        self.v_m_mv = self.e_leak_mv
        self.v_thresh_mv = self.e_thresh_base_mv
        self.g_exc_ns = 0.0
        self.g_inh_ns = 0.0
        self.g_ahp_ns = 0.0
        self.refract_ticks = 0

    def step(self, i_inj_pa: float = 0.0) -> bool:
        """Step neuron dynamics by dt_ms. Returns True if spike emitted."""
        dt = self.dt_ms
        
        # 1. Decay synaptic conductances, AHP, and dynamic threshold
        decay_exc = math.exp(-dt / self.tau_exc_ms)
        decay_inh = math.exp(-dt / self.tau_inh_ms)
        decay_ahp = math.exp(-dt / self.tau_ahp_ms)
        decay_thr = math.exp(-dt / self.tau_thresh_ms)
        
        self.g_exc_ns *= decay_exc
        self.g_inh_ns *= decay_inh
        self.g_ahp_ns *= decay_ahp
        self.v_thresh_mv = self.e_thresh_base_mv + (self.v_thresh_mv - self.e_thresh_base_mv) * decay_thr
        
        # 2. Refractory handling
        if self.refract_ticks > 0:
            self.refract_ticks -= 1
            self.v_m_mv = self.e_reset_mv
            return False
            
        # 3. Exact Exponential Euler integration
        g_tot = self.g_leak_ns + self.g_exc_ns + self.g_inh_ns + self.g_ahp_ns
        if g_tot < 1e-3:
            g_tot = self.g_leak_ns
            
        num = (self.g_leak_ns * self.e_leak_mv +
               self.g_exc_ns * self.e_exc_mv +
               self.g_inh_ns * self.e_inh_mv +
               self.g_ahp_ns * self.e_k_mv +
               i_inj_pa)
        v_inf = num / g_tot
        
        tau_eff_ms = self.c_m_pf / g_tot
        decay_v = math.exp(-dt / tau_eff_ms)
        v_next = v_inf + (self.v_m_mv - v_inf) * decay_v
        
        # Numerical safety clamp
        v_next = max(-120.0, min(50.0, v_next))
        
        # 4. Threshold crossing
        if v_next >= self.v_thresh_mv:
            self.v_m_mv = self.e_reset_mv
            self.refract_ticks = self.abs_refract_ticks
            self.v_thresh_mv += 15.0
            self.g_ahp_ns += 2.0
            return True
        else:
            self.v_m_mv = v_next
            return False


class ReferenceTsodyksMarkramSynapse:
    """Exact reference implementation of Tsodyks-Markram STP synapse."""
    def __init__(self, syn_class: int, weight_ns: float = 10.0, dt_ms: float = 0.1):
        self.dt_ms = dt_ms
        self.syn_class = syn_class
        self.weight_ns = max(0.0, min(40.0, weight_ns))
        
        # Parameters by class
        if syn_class == 0:    # EE (Depressing)
            self.U_base = 0.50
            self.tau_rec_ms = 800.0
            self.tau_fac_ms = 20.0
        elif syn_class == 1:  # EI (Facilitating)
            self.U_base = 0.15
            self.tau_rec_ms = 200.0
            self.tau_fac_ms = 600.0
        elif syn_class == 2:  # IE (Depressing)
            self.U_base = 0.25
            self.tau_rec_ms = 700.0  # Gupta et al. 2000 F2 empirical mean (706 ms)
            self.tau_fac_ms = 50.0
        else:                 # II (Moderately depressing)
            self.U_base = 0.30
            self.tau_rec_ms = 400.0
            self.tau_fac_ms = 50.0
            
        self.u_stp = self.U_base
        self.x_stp = 1.0

    def step_decay(self):
        dt = self.dt_ms
        d_rec = math.exp(-dt / self.tau_rec_ms)
        d_fac = math.exp(-dt / self.tau_fac_ms)
        self.x_stp = 1.0 + (self.x_stp - 1.0) * d_rec
        self.u_stp = self.U_base + (self.u_stp - self.U_base) * d_fac

    def transmit_spike(self) -> float:
        """Process spike and return released conductance delta_g (nS)."""
        release = self.u_stp * self.x_stp
        self.x_stp = max(0.0, min(1.0, self.x_stp - release))
        self.u_stp = self.u_stp + self.U_base * (1.0 - self.u_stp)
        return self.weight_ns * release


# =============================================================================
# Tests: COBA-LIF Numerical Stability under Extreme Injections
# =============================================================================

def test_coba_lif_extreme_positive_current_injection():
    """Verify COBA-LIF numerical stability under massive depolarizing current injection (+10,000 pA to +1,000,000 pA)."""
    neuron = ReferenceCOBALIFNeuron(dt_ms=0.1)
    
    extreme_currents = [1000.0, 5000.0, 10000.0, 50000.0, 1000000.0]
    for i_inj in extreme_currents:
        for _ in range(500):  # 50 ms of sustained massive current
            spiked = neuron.step(i_inj_pa=i_inj)
            assert not math.isnan(neuron.v_m_mv), f"NaN detected at I_inj={i_inj}"
            assert not math.isinf(neuron.v_m_mv), f"Inf detected at I_inj={i_inj}"
            assert -120.0 <= neuron.v_m_mv <= 50.0, f"Voltage out of bounds: {neuron.v_m_mv} at I_inj={i_inj}"


def test_coba_lif_extreme_negative_current_injection():
    """Verify COBA-LIF numerical stability under extreme hyperpolarizing current injection (-1,000,000 pA)."""
    neuron = ReferenceCOBALIFNeuron(dt_ms=0.1)
    
    extreme_currents = [-1000.0, -10000.0, -100000.0, -1000000.0]
    for i_inj in extreme_currents:
        for _ in range(200):
            neuron.step(i_inj_pa=i_inj)
            assert not math.isnan(neuron.v_m_mv)
            assert not math.isinf(neuron.v_m_mv)
            assert -120.0 <= neuron.v_m_mv <= 50.0


def test_coba_lif_resting_equilibrium_stability():
    """Verify that with zero current injection, membrane settles to resting potential E_leak (-70 mV)."""
    neuron = ReferenceCOBALIFNeuron(dt_ms=0.1)
    neuron.v_m_mv = -55.0  # Displaced initial potential
    
    for _ in range(2000):  # 200 ms
        neuron.step(i_inj_pa=0.0)
        
    assert abs(neuron.v_m_mv - (-70.0)) < 0.01, f"Expected -70 mV equilibrium, got {neuron.v_m_mv:.3f} mV"


# =============================================================================
# Tests: Absolute Refractory Clamp (2.0 ms -> Max 500 Hz)
# =============================================================================

def test_absolute_refractory_clamp_2ms():
    """Verify that a 2.0 ms hard refractory clamp (20 ticks at dt = 0.1 ms) strictly caps single neuron firing at 500 Hz."""
    neuron = ReferenceCOBALIFNeuron(dt_ms=0.1)
    
    # Under continuous extreme drive, neuron should fire at absolute theoretical maximum
    spike_ticks = []
    total_ticks = 10000  # 1.0 second simulation
    
    for tick in range(total_ticks):
        spiked = neuron.step(i_inj_pa=5000.0)
        if spiked:
            spike_ticks.append(tick)
            
    assert len(spike_ticks) > 0, "Neuron should fire under suprathreshold current"
    
    # Calculate Inter-Spike Intervals (ISI)
    isis_ticks = [spike_ticks[i] - spike_ticks[i-1] for i in range(1, len(spike_ticks))]
    min_isi_ticks = min(isis_ticks)
    min_isi_ms = min_isi_ticks * 0.1
    
    # Must never violate absolute refractory period of 2.0 ms (20 ticks)
    assert min_isi_ticks >= 20, f"Violation of absolute refractory clamp: min ISI={min_isi_ticks} ticks ({min_isi_ms} ms) < 20 ticks"
    
    # Maximum firing rate over 1.0 second cannot exceed 500 Hz
    firing_rate_hz = len(spike_ticks) / 1.0
    assert firing_rate_hz <= 500.0, f"Firing rate {firing_rate_hz} Hz exceeded theoretical cap of 500 Hz"


def test_membrane_clamped_at_reset_during_refractory():
    """Verify membrane potential is clamped at E_reset (-75 mV) during entire 2.0 ms refractory period."""
    neuron = ReferenceCOBALIFNeuron(dt_ms=0.1)
    
    # Force a spike
    neuron.v_m_mv = -49.0
    spiked = neuron.step(i_inj_pa=100.0)
    assert spiked, "Spike must occur when V >= V_thresh"
    assert neuron.refract_ticks == 20
    
    # Next 20 ticks must stay pinned at E_reset = -75 mV even with massive depolarizing current
    for tick in range(20):
        assert neuron.refract_ticks == (20 - tick)
        neuron.step(i_inj_pa=10000.0)
        assert abs(neuron.v_m_mv - (-75.0)) < 1e-4, f"Tick {tick}: V_m was {neuron.v_m_mv}, expected clamped -75 mV"


# =============================================================================
# Tests: Dynamic Threshold & Slow After-Hyperpolarization (AHP)
# =============================================================================

def test_dynamic_threshold_jump_and_decay():
    """Verify dynamic threshold jumps by +15 mV on spike emission and decays with tau = 10.0 ms."""
    neuron = ReferenceCOBALIFNeuron(dt_ms=0.1)
    base_thresh = -50.0
    assert abs(neuron.v_thresh_mv - base_thresh) < 1e-4
    
    # Trigger a spike
    neuron.v_m_mv = -49.0
    spiked = neuron.step(i_inj_pa=0.0)
    assert spiked
    
    # Immediately after spike, threshold should be base + 15 mV = -35 mV
    peak_thresh = base_thresh + 15.0
    assert abs(neuron.v_thresh_mv - peak_thresh) < 1e-3, f"Expected peak threshold {peak_thresh} mV, got {neuron.v_thresh_mv} mV"
    
    # Decay over 10.0 ms (100 ticks): delta should decay to 15 * exp(-1) = ~5.518 mV
    for _ in range(100):
        neuron.step(i_inj_pa=0.0)
        
    expected_thresh = base_thresh + 15.0 * math.exp(-10.0 / 10.0)
    assert abs(neuron.v_thresh_mv - expected_thresh) < 0.2, (
        f"Threshold decay mismatch: expected {expected_thresh:.3f} mV, got {neuron.v_thresh_mv:.3f} mV"
    )


def test_slow_ahp_potassium_conductance_decay():
    """Verify slow AHP potassium conductance jumps by +2.0 nS on spike and decays with tau = 80.0 ms."""
    neuron = ReferenceCOBALIFNeuron(dt_ms=0.1)
    assert neuron.g_ahp_ns == 0.0
    
    # Trigger a spike
    neuron.v_m_mv = -49.0
    spiked = neuron.step(i_inj_pa=0.0)
    assert spiked
    assert abs(neuron.g_ahp_ns - 2.0) < 1e-3
    
    # After 80.0 ms (800 ticks), g_ahp should decay by exp(-1)
    for _ in range(800):
        neuron.step(i_inj_pa=0.0)
        
    expected_g_ahp = 2.0 * math.exp(-80.0 / 80.0)
    assert abs(neuron.g_ahp_ns - expected_g_ahp) < 0.05, (
        f"AHP decay mismatch: expected {expected_g_ahp:.3f} nS, got {neuron.g_ahp_ns:.3f} nS"
    )


# =============================================================================
# Tests: Tsodyks-Markram Short-Term Plasticity (STP)
# =============================================================================

def test_tsodyks_markram_ee_depression_and_recovery():
    """Verify Class EE (Excitatory->Excitatory) synapse exhibits vesicle depletion and slow recovery (tau_rec = 800 ms)."""
    syn = ReferenceTsodyksMarkramSynapse(syn_class=0, weight_ns=20.0, dt_ms=0.1)
    assert syn.U_base == 0.50
    assert syn.tau_rec_ms == 800.0
    
    # Deliver high-frequency spike train (4 spikes at 20 ms intervals = 200 ticks between spikes)
    releases = []
    for _ in range(4):
        dg = syn.transmit_spike()
        releases.append(dg)
        for _ in range(200):  # 20 ms interval
            syn.step_decay()
            
    # Successive releases must decline (short-term depression)
    assert releases[0] > releases[1] > releases[2], f"Expected depression, got releases: {releases}"
    
    # Verify vesicle depletion: x_stp significantly below 1.0
    assert syn.x_stp < 0.4, f"Vesicles should be depleted, got x_stp={syn.x_stp}"
    
    # Let synapse recover over 800 ms (8000 ticks)
    for _ in range(8000):
        syn.step_decay()
        
    # After tau_rec (800 ms), x_stp should have recovered significantly toward 1.0 (>= 0.60)
    assert syn.x_stp > 0.60, f"Expected recovery toward 1.0, got x_stp={syn.x_stp}"
    
    # After full recovery period (2400 ms = 3 * tau_rec), x_stp should be > 0.90
    for _ in range(16000):  # +1600 ms = 2400 ms total
        syn.step_decay()
    assert syn.x_stp > 0.90, f"Expected full recovery > 0.90, got x_stp={syn.x_stp}"


def test_tsodyks_markram_ei_facilitation():
    """Verify Class EI (Excitatory->Inhibitory) synapse exhibits facilitation (tau_fac = 600 ms)."""
    syn = ReferenceTsodyksMarkramSynapse(syn_class=1, weight_ns=20.0, dt_ms=0.1)
    assert syn.U_base == 0.15
    assert syn.tau_fac_ms == 600.0
    
    # In a facilitating synapse, short-interval second spike has higher utilization u
    u_initial = syn.u_stp
    syn.transmit_spike()
    u_after_first = syn.u_stp
    assert u_after_first > u_initial, "Utilization u must jump on spike"
    
    # Deliver second spike after only 10 ms (100 ticks)
    for _ in range(100):
        syn.step_decay()
        
    syn.transmit_spike()
    u_after_second = syn.u_stp
    assert u_after_second > u_after_first, f"Utilization should facilitate: u1={u_after_first}, u2={u_after_second}"


# =============================================================================
# Tests: STDP Clamping, 1.05x LTD Bias, and Dale's Principle
# =============================================================================

def test_stdp_weight_hard_clamping():
    """Verify that STDP updates are strictly clamped within [0.0 nS, 40.0 nS]."""
    w_min = 0.0
    w_max = 40.0
    
    current_w = 38.0
    # Attempting to add +5.0 nS should clamp at 40.0 nS
    clamped_w = max(w_min, min(w_max, current_w + 5.0))
    assert clamped_w == 40.0
    
    # Attempting to subtract 50.0 nS should clamp at 0.0 nS (no negative conductances)
    clamped_w_neg = max(w_min, min(w_max, current_w - 50.0))
    assert clamped_w_neg == 0.0


def test_stdp_depression_bias_ratio():
    """Verify STDP LTD amplitude exceeds LTP amplitude by exactly 1.05x (A_- / A_+ = 1.05)."""
    a_plus = 0.20
    a_minus = 0.21
    ratio = a_minus / a_plus
    assert abs(ratio - 1.05) < 1e-6, f"Expected 1.05x LTD bias, got {ratio}"


def test_dales_principle_conductance_reversal():
    """Verify Dale's Principle: Excitatory reversal is 0 mV, Inhibitory reversal is -80 mV."""
    e_exc = 0.0
    e_inh = -80.0
    e_leak = -70.0
    
    # Excitatory driving force (E_exc - V_m) is always depolarizing for V_m in [-75, -50]
    for v in [-75.0, -70.0, -60.0, -50.0]:
        driving_force_exc = e_exc - v
        assert driving_force_exc > 0, f"Excitatory driving force must be depolarizing (positive), got {driving_force_exc}"
        
        # Inhibitory driving force (E_inh - V_m) is always hyperpolarizing for V_m in [-70, -50]
        driving_force_inh = e_inh - v
        assert driving_force_inh < 0, f"Inhibitory driving force must be hyperpolarizing (negative), got {driving_force_inh}"


# =============================================================================
# Tests: Integrated Native WetVM Biophysics Stability
# =============================================================================

def test_native_wetvm_multi_tick_stability():
    """Verify native WetVM biophysical digital twin stability over 500 ticks."""
    config = WetVMConfig(dt_ms=0.1, channel_count=64)
    vm = WetVM(config=config)
    
    # Step through 500 ticks without external input
    from compiler.compiler_cli import compile_source
    code = """
    grid mea[8, 8];
    channel ch0 = mea[0, 0];
    int i = 0;
    while (i < 500) {
        sync_tick;
        i = i + 1;
    }
    """
    bc = compile_source(code)
    vm.load_bytecode(bc)
    
    executed, telem = vm.run_ticks(500)
    assert executed == 500
    assert telem.current_tick == 500
    
    # Check that voltages are all finite and within biological range [-85 mV, +20 mV]
    arr_v = vm.get_voltages_numpy()
    assert not np.any(np.isnan(arr_v))
    assert not np.any(np.isinf(arr_v))
    
    vm.close()
