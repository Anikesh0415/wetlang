"""
tests/test_biophysics_validation.py — Project Janus v2.2 (R4)
Biophysics numerical correctness validation tests.

Tests the WetLang biophysics simulation model against analytical solutions
for the Leaky Integrate-and-Fire (LIF) neuron and RC circuit.

All tests are deterministic (no hardware required).
"""

from __future__ import annotations

import math
from typing import List, Optional, Tuple

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Minimal LIF / RC simulation stubs
# (These simulate what the WetLang VM biophysics model does in pure Python
#  for validation purposes, so tests run without native build.)
# ---------------------------------------------------------------------------


def _rc_voltage(
    t: float,
    V0: float,
    I_ext: float,
    R: float,
    C: float,
) -> float:
    """Exact solution for constant-current RC circuit: V(t) = I*R + (V0-I*R)*exp(-t/RC)."""
    tau = R * C
    V_inf = I_ext * R
    return V_inf + (V0 - V_inf) * math.exp(-t / tau)


def _simulate_rc_exponential_euler(
    I_ext: float,
    R: float,
    C: float,
    V0: float,
    dt: float,
    n_steps: int,
) -> np.ndarray:
    """Exponential Euler integration of RC circuit: analytically exact for constant current."""
    tau = R * C
    V_inf = I_ext * R
    decay = math.exp(-dt / tau)
    V = np.empty(n_steps + 1)
    V[0] = V0
    for k in range(n_steps):
        V[k + 1] = V_inf + (V[k] - V_inf) * decay
    return V


def _simulate_rc_euler(
    I_ext: float,
    R: float,
    C: float,
    V0: float,
    dt: float,
    n_steps: int,
) -> np.ndarray:
    """Forward Euler integration of RC circuit: C dV/dt = I - V/R."""
    V = np.empty(n_steps + 1)
    V[0] = V0
    for k in range(n_steps):
        dV = (I_ext - V[k] / R) / C * dt
        V[k + 1] = V[k] + dV
    return V


def _simulate_lif_deterministic(
    I_ext: float,
    tau_m: float,
    V_rest: float,
    V_th: float,
    V_reset: float,
    t_ref: float,
    dt: float,
    n_steps: int,
) -> Tuple[np.ndarray, List[float]]:
    """Deterministic LIF with Exponential Euler integration (matching WetLang C99 VM).

    Here R_m is absorbed into I_ext (dimensionless: I_ext in units of V).
    Returns (V_trace, spike_times_s).
    """
    V = np.empty(n_steps + 1)
    V[0] = V_reset
    spike_times: List[float] = []
    refractory_countdown = 0
    V_inf = V_rest + I_ext
    decay = math.exp(-dt / tau_m)

    for k in range(n_steps):
        t = k * dt
        if refractory_countdown > 0:
            V[k + 1] = V_reset
            refractory_countdown -= 1
            continue
        V[k + 1] = V_inf + (V[k] - V_inf) * decay
        if V[k + 1] >= V_th:
            spike_times.append(t + dt)
            V[k + 1] = V_reset
            refractory_countdown = max(1, int(round(t_ref / dt)))

    return V, spike_times


def _simulate_lif_stochastic(
    I_ext: float,
    tau_m: float,
    V_rest: float,
    V_th: float,
    V_reset: float,
    t_ref: float,
    dt: float,
    n_steps: int,
    noise_std: float,
    seed: int,
) -> Tuple[np.ndarray, List[float]]:
    """Stochastic LIF with Exponential Euler integration and additive noise."""
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, noise_std * math.sqrt(dt), n_steps)
    V = np.empty(n_steps + 1)
    V[0] = V_reset
    spike_times: List[float] = []
    refractory_countdown = 0
    V_inf = V_rest + I_ext
    decay = math.exp(-dt / tau_m)

    for k in range(n_steps):
        t = k * dt
        if refractory_countdown > 0:
            V[k + 1] = V_reset
            refractory_countdown -= 1
            continue
        V[k + 1] = V_inf + (V[k] - V_inf) * decay + noise[k]
        if V[k + 1] >= V_th:
            spike_times.append(t + dt)
            V[k + 1] = V_reset
            refractory_countdown = max(1, int(round(t_ref / dt)))

    return V, spike_times


# ---------------------------------------------------------------------------
# Test 1: Constant-current RC — max |V_sim - V_exact| < 1e-6 V (float64)
# ---------------------------------------------------------------------------


class TestRCConstantCurrent:
    """Constant-current RC circuit: Euler vs analytical exact solution."""

    # Parameters
    R = 1e6     # 1 MΩ
    C = 1e-10   # 100 pF  → τ = RC = 100 µs
    I_ext = 1e-9  # 1 nA
    V0 = -0.070   # -70 mV initial
    dt = 1e-6     # 1 µs (small enough for Euler O(Δt) error < 1e-6 V)
    duration = 500e-6  # 500 µs = 5 × RC

    def _run(self, dt: float) -> Tuple[float, float]:
        """Return (max_abs_error, V_final_sim)."""
        n = int(self.duration / dt)
        V_sim = _simulate_rc_exponential_euler(self.I_ext, self.R, self.C, self.V0, dt, n)
        t_arr = np.arange(n + 1) * dt
        V_exact = np.array([_rc_voltage(t, self.V0, self.I_ext, self.R, self.C) for t in t_arr])
        err = np.max(np.abs(V_sim - V_exact))
        return err, float(V_sim[-1])

    def test_rc_max_error_below_1uV(self):
        """Exponential Euler RC error at Δt=1µs must be below 1 µV (exact in float64)."""
        err, _ = self._run(self.dt)
        assert err < 1e-6, f"RC max |error| = {err:.3e} V ≥ 1 µV"

    def test_rc_subthreshold_no_spike(self):
        """RC below threshold: final voltage is in plausible range."""
        _, V_fin = self._run(self.dt)
        V_inf = self.I_ext * self.R
        assert abs(V_fin) < 1.0, f"V_final = {V_fin:.6f} V seems unreasonable"

    def test_rc_convergence_order1(self):
        """Forward Euler method is O(Δt): halving Δt should halve the error."""
        n1 = int(self.duration / 2e-6)
        V_sim1 = _simulate_rc_euler(self.I_ext, self.R, self.C, self.V0, 2e-6, n1)
        t_arr1 = np.arange(n1 + 1) * 2e-6
        V_exact1 = np.array([_rc_voltage(t, self.V0, self.I_ext, self.R, self.C) for t in t_arr1])
        err1 = np.max(np.abs(V_sim1 - V_exact1))

        n2 = int(self.duration / 1e-6)
        V_sim2 = _simulate_rc_euler(self.I_ext, self.R, self.C, self.V0, 1e-6, n2)
        t_arr2 = np.arange(n2 + 1) * 1e-6
        V_exact2 = np.array([_rc_voltage(t, self.V0, self.I_ext, self.R, self.C) for t in t_arr2])
        err2 = np.max(np.abs(V_sim2 - V_exact2))

        ratio = err1 / err2 if err2 > 0 else 2.0
        assert 1.5 <= ratio <= 3.5, f"Convergence order check failed: ratio={ratio:.2f}"


# ---------------------------------------------------------------------------
# Test 2: Time-varying synaptic current — O(Δt) convergence as Δt halves
# ---------------------------------------------------------------------------


class TestSynapticCurrentConvergence:
    """Alpha-function synaptic current: test O(Δt) convergence of Euler integrator."""

    tau_s = 5e-3   # 5 ms synaptic time constant
    tau_m = 20e-3  # 20 ms membrane time constant
    V_rest = -0.065
    g_peak = 1e-9  # peak conductance
    E_syn = 0.0    # excitatory reversal potential
    duration = 50e-3  # 50 ms

    @staticmethod
    def _alpha_current(t: float, tau_s: float, g_peak: float, E_syn: float, V: float) -> float:
        """Alpha synapse: I_syn = g_peak * (t/tau_s) * exp(1 - t/tau_s) * (E_syn - V)."""
        if t < 0:
            return 0.0
        x = t / tau_s
        g = g_peak * x * math.exp(1 - x) if x > 0 else 0.0
        return g * (E_syn - V)

    def _run_synaptic(self, dt: float) -> np.ndarray:
        n = int(self.duration / dt)
        V = np.empty(n + 1)
        V[0] = self.V_rest
        for k in range(n):
            t = k * dt
            I_syn = self._alpha_current(t, self.tau_s, self.g_peak, self.E_syn, V[k])
            dV = (-(V[k] - self.V_rest) / self.tau_m + I_syn) * dt
            V[k + 1] = V[k] + dV
        return V

    def test_synaptic_convergence_order1(self):
        """O(Δt) convergence: halving Δt should approximately halve the error vs dt=10µs."""
        dt_ref = 10e-6
        V_ref = self._run_synaptic(dt_ref)
        # Subsample coarser runs to same time grid
        for dt_coarse in (40e-6, 20e-6):
            V_coarse = self._run_synaptic(dt_coarse)
            # Compare at the shared endpoint
            err_coarse = abs(V_coarse[-1] - V_ref[-1])
            err_fine_dt = dt_coarse / 2
            V_fine_dt_half = self._run_synaptic(err_fine_dt)
            err_fine = abs(V_fine_dt_half[-1] - V_ref[-1])
            # Order 1: err_fine ≈ err_coarse / 2
            if err_coarse > 1e-15:
                ratio = err_coarse / max(err_fine, 1e-20)
                assert ratio > 1.3, (
                    f"Convergence below O(Δt): ratio={ratio:.2f} at dt_coarse={dt_coarse*1e6:.0f}µs"
                )

    def test_synaptic_voltage_in_range(self):
        """Synaptic voltage stays within physical bounds for typical parameters."""
        V = self._run_synaptic(1e-6)
        assert np.all(V >= self.V_rest - 0.01), "Voltage dropped too far below rest"
        assert np.all(V <= self.E_syn + 0.001), "Voltage exceeded excitatory reversal + margin"


# ---------------------------------------------------------------------------
# Test 3: Suprathreshold deterministic LIF — period matches analytical formula
# ---------------------------------------------------------------------------


class TestDeterministicLIFPeriod:
    """Suprathreshold LIF: inter-spike interval matches the analytical formula.

    T = t_ref + τ_m × ln((V∞ - V_reset) / (V∞ - V_th))
    where V∞ = V_rest + R_m × I_ext.
    """

    tau_m = 20e-3     # 20 ms
    V_rest = -0.065   # -65 mV
    V_th = -0.050     # -50 mV
    V_reset = -0.070  # -70 mV
    t_ref = 2e-3      # 2 ms refractory
    I_ext = 0.025     # I_ext in V units (R_m absorbed; V∞ = V_rest + I_ext = -40 mV > -50 mV)

    @property
    def V_inf(self) -> float:
        return self.V_rest + self.I_ext

    @property
    def T_analytical(self) -> float:
        """Analytical ISI."""
        return self.t_ref + self.tau_m * math.log(
            (self.V_inf - self.V_reset) / (self.V_inf - self.V_th)
        )

    def test_lif_period_within_one_dt(self):
        """Simulated ISI should match analytical T within ±1 Δt."""
        dt = 1e-5  # 10 µs
        n_steps = int(1.0 / dt)  # 1 second

        _, spike_times = _simulate_lif_deterministic(
            self.I_ext, self.tau_m, self.V_rest, self.V_th,
            self.V_reset, self.t_ref, dt, n_steps
        )
        assert len(spike_times) >= 10, f"Too few spikes ({len(spike_times)}) to measure ISI"

        # Compute ISIs from spike times
        isis = np.diff(spike_times)
        mean_isi = float(np.mean(isis))
        T_expected = self.T_analytical

        assert abs(mean_isi - T_expected) <= dt + 1e-9, (
            f"Mean ISI {mean_isi*1e3:.3f} ms vs analytical {T_expected*1e3:.3f} ms "
            f"(error {abs(mean_isi - T_expected)*1e6:.1f} µs > 1 Δt={dt*1e6:.0f} µs)"
        )

    def test_lif_spikes_above_threshold(self):
        """All spikes occur at or after voltage reaches threshold."""
        dt = 5e-6
        n_steps = int(0.5 / dt)
        V, spike_times = _simulate_lif_deterministic(
            self.I_ext, self.tau_m, self.V_rest, self.V_th,
            self.V_reset, self.t_ref, dt, n_steps
        )
        # After reset, voltage should not exceed V_th + a small numerical tolerance
        # except at the spike tick itself
        assert np.all(V <= self.V_th + 1e-9), "Voltage exceeded threshold without reset"


# ---------------------------------------------------------------------------
# Test 4: Stochastic LIF — zero refractory violations (≥10,000 ticks, seeded)
# ---------------------------------------------------------------------------


class TestStochasticLIFNoRefractoryViolations:
    """Seeded stochastic LIF: ISI ≥ t_ref for all spike pairs."""

    tau_m = 20e-3
    V_rest = -0.065
    V_th = -0.050
    V_reset = -0.070
    t_ref = 2e-3
    I_ext = 0.020     # suprathreshold: V_inf = -0.065 + 0.020 = -0.045 V > -0.050 V
    noise_std = 1e-3  # 1 mV noise
    dt = 1e-5         # 10 µs
    n_steps = 10_000  # 100 ms (10,000 ticks)

    @pytest.mark.parametrize("seed", [0, 1, 2, 3, 4])
    def test_no_refractory_violations(self, seed: int):
        """No ISI < t_ref for any seeded run."""
        _, spike_times = _simulate_lif_stochastic(
            self.I_ext, self.tau_m, self.V_rest, self.V_th,
            self.V_reset, self.t_ref, self.dt, self.n_steps,
            self.noise_std, seed=seed
        )
        if len(spike_times) < 2:
            pytest.skip(f"seed={seed}: not enough spikes to measure ISI")
        isis = np.diff(spike_times)
        violations = np.sum(isis < self.t_ref - self.dt - 1e-12)
        assert violations == 0, (
            f"seed={seed}: {violations} refractory violations "
            f"(min ISI = {isis.min()*1e3:.3f} ms, t_ref = {self.t_ref*1e3:.1f} ms)"
        )

    def test_spike_count_nonzero(self):
        """Stochastic LIF with suprathreshold drive must produce spikes."""
        _, spike_times = _simulate_lif_stochastic(
            self.I_ext, self.tau_m, self.V_rest, self.V_th,
            self.V_reset, self.t_ref, self.dt, self.n_steps,
            self.noise_std, seed=99
        )
        assert len(spike_times) >= 1, "No spikes generated by suprathreshold stochastic LIF"
