"""
WetLang Compiler — FinalSpark Neuroplatform Reference Simulator (Project Janus v2.2, R3)
Target: --target=neuroplatform

Emits a Neuroplatform-compatible execution trace instead of a raw .wbc binary.
Neuroplatform uses a REST API + MEA-based wetware compute substrate.

This reference simulator validates WetLang programs against the Neuroplatform
stimulation constraints (charge limit, impedance, blanking) using the same
biophysics model as the main VM but adapted for the Neuroplatform MEA geometry
(4×4 = 16 active electrodes, 500 µm pitch, typical impedance 100–500 kΩ).
"""

from __future__ import annotations

import json
import struct
import time
import warnings
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


class NeuroplatformSimError(Exception):
    """Raised when a program violates Neuroplatform hardware constraints."""


# Neuroplatform hardware limits
_NP_MAX_CHANNELS = 16          # 4×4 MEA
_NP_MAX_VOLTAGE_V = 1.2        # ±1.2 V hard limit
_NP_MAX_CURRENT_UA = 100.0     # 100 µA per electrode
_NP_MIN_BLANKING_MS = 0.5      # Neuroplatform blanking minimum
_NP_MAX_BLANKING_MS = 10.0     # Neuroplatform blanking maximum
_NP_ELECTRODE_AREA_CM2 = 7850e-8  # 7850 µm² typical for FinalSpark probes
_NP_IMPEDANCE_OHMS = 150_000.0  # typical 150 kΩ


class NeuroplatformRefSim:
    """Reference simulator for --target=neuroplatform.

    Processes a list of wetlang AST nodes (from the emitter's IR) and
    validates them against Neuroplatform hardware constraints.
    Outputs a JSON-serialisable execution trace that mirrors the
    Neuroplatform REST API request format.

    Parameters
    ----------
    n_ticks       : Simulation duration in VM ticks (100 µs each).
    mea_shape     : MEA geometry (rows, cols). Default (4, 4).
    impedance_ohms: Electrode impedance for voltage→current conversion.
    seed          : RNG seed for synthetic recording noise.
    """

    def __init__(
        self,
        n_ticks: int = 10_000,
        mea_shape: Tuple[int, int] = (4, 4),
        impedance_ohms: float = _NP_IMPEDANCE_OHMS,
        seed: int = 0,
    ) -> None:
        self.n_ticks = n_ticks
        self.mea_shape = mea_shape
        self.n_channels = mea_shape[0] * mea_shape[1]
        self.impedance_ohms = impedance_ohms
        self._rng = np.random.default_rng(seed)
        self._events: List[Dict[str, Any]] = []
        self._blanking_active = np.zeros(self.n_channels, dtype=bool)
        self._blanking_countdown = np.zeros(self.n_channels, dtype=int)
        self._tick = 0
        self._violation_count = 0

    # ------------------------------------------------------------------
    # Event injection (called by the emitter backend)
    # ------------------------------------------------------------------

    def stim_biphasic(
        self,
        channel: int,
        amplitude_v: float,
        phase1_ms: float,
        phase2_ms: float,
        interphase_ms: float = 0.0,
    ) -> None:
        """Inject a biphasic stimulation event and validate constraints."""
        self._check_channel(channel)
        self._check_voltage(channel, amplitude_v)

        # Estimate current from voltage + impedance
        i_ua = abs(amplitude_v) / self.impedance_ohms * 1e6
        self._check_current(channel, i_ua)
        self._check_shannon(channel, i_ua, phase1_ms, phase2_ms)

        self._events.append({
            "tick": self._tick,
            "timestamp_us": self._tick * 100,
            "type": "stim_biphasic",
            "channel": channel,
            "amplitude_v": amplitude_v,
            "phase1_ms": phase1_ms,
            "phase2_ms": phase2_ms,
            "interphase_ms": interphase_ms,
        })

        # Set blanking for this channel
        blanking_ms = max(_NP_MIN_BLANKING_MS, min(_NP_MAX_BLANKING_MS, phase1_ms + phase2_ms))
        blanking_ticks = int(blanking_ms * 10)  # 10 ticks per ms (100 µs tick)
        self._blanking_countdown[channel] = blanking_ticks
        self._blanking_active[channel] = True

    def set_blanking(self, channel: int, duration_ms: float) -> None:
        """Set explicit blanking window."""
        if duration_ms < _NP_MIN_BLANKING_MS or duration_ms > _NP_MAX_BLANKING_MS:
            raise NeuroplatformSimError(
                f"Neuroplatform blanking {duration_ms:.2f} ms outside "
                f"[{_NP_MIN_BLANKING_MS}, {_NP_MAX_BLANKING_MS}] ms"
            )
        ticks = int(duration_ms * 10)
        if channel == 0xFFFF:
            self._blanking_countdown[:] = ticks
            self._blanking_active[:] = True
        else:
            self._check_channel(channel)
            self._blanking_countdown[channel] = ticks
            self._blanking_active[channel] = True

    def advance_tick(self) -> None:
        """Advance simulation by one tick (100 µs)."""
        # Update blanking counters
        active = self._blanking_countdown > 0
        self._blanking_countdown[active] -= 1
        self._blanking_active[~active] = False
        self._tick += 1

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    def to_json(self) -> str:
        """Return the execution trace as a JSON string (Neuroplatform API format)."""
        trace = {
            "format": "neuroplatform_trace_v1",
            "n_ticks": self._tick,
            "mea_shape": list(self.mea_shape),
            "n_channels": self.n_channels,
            "tick_period_us": 100,
            "violation_count": self._violation_count,
            "events": self._events,
        }
        return json.dumps(trace, indent=2)

    def run_ticks(self, n: Optional[int] = None) -> None:
        """Advance the simulation for n ticks (None = self.n_ticks)."""
        for _ in range(n if n is not None else self.n_ticks):
            self.advance_tick()

    def synthetic_recording(
        self,
        duration_ticks: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Generate a synthetic MEA recording with realistic noise."""
        n = duration_ticks or self.n_ticks
        t = np.arange(n, dtype=np.float64) * 100e-6  # seconds
        # Background noise: 5 µV RMS
        noise = self._rng.normal(0.0, 5e-6, (n, self.n_channels)).astype(np.float32)
        # Synthetic spikes: random Poisson events
        spike_times = {}
        for ch in range(self.n_channels):
            rate = self._rng.uniform(0.1, 5.0)  # Hz
            n_spikes = self._rng.poisson(rate * n * 100e-6)
            if n_spikes > 0:
                spike_idx = self._rng.choice(n, size=n_spikes, replace=False)
                spike_times[ch] = sorted(spike_idx.tolist())
                for idx in spike_idx:
                    noise[idx, ch] += self._rng.choice([-1, 1]) * self._rng.uniform(50e-6, 200e-6)
        return {
            "data": noise,
            "timestamps": t.astype(np.float32),
            "spike_times": spike_times,
            "sample_rate_hz": 10_000.0,
        }

    # ------------------------------------------------------------------
    # Constraint checks
    # ------------------------------------------------------------------

    def _check_channel(self, channel: int) -> None:
        if channel != 0xFFFF and not (0 <= channel < self.n_channels):
            raise NeuroplatformSimError(
                f"Channel {channel} out of range [0, {self.n_channels - 1}] for {self.mea_shape} MEA"
            )

    def _check_voltage(self, channel: int, amplitude_v: float) -> None:
        if abs(amplitude_v) > _NP_MAX_VOLTAGE_V + 1e-9:
            self._violation_count += 1
            raise NeuroplatformSimError(
                f"Channel {channel}: voltage {amplitude_v:.3f} V exceeds "
                f"Neuroplatform limit ±{_NP_MAX_VOLTAGE_V} V"
            )

    def _check_current(self, channel: int, i_ua: float) -> None:
        if i_ua > _NP_MAX_CURRENT_UA + 1e-9:
            self._violation_count += 1
            raise NeuroplatformSimError(
                f"Channel {channel}: estimated current {i_ua:.2f} µA exceeds "
                f"Neuroplatform limit {_NP_MAX_CURRENT_UA} µA"
            )

    def _check_shannon(
        self, channel: int, i_ua: float, phase1_ms: float, phase2_ms: float
    ) -> None:
        """Verify Shannon k-limit: log10(D*Q) ≤ 1.75."""
        import math
        area_cm2 = _NP_ELECTRODE_AREA_CM2
        Q_uc = i_ua * 1e-6 * max(phase1_ms, phase2_ms) * 1e-3 * 1e6  # µC
        if Q_uc <= 0.0:
            return
        D = Q_uc / area_cm2  # µC/cm²
        k = math.log10(D * Q_uc)
        if k > 1.75 + 1e-9:
            self._violation_count += 1
            warnings.warn(
                f"Neuroplatform channel {channel}: Shannon k={k:.3f} > 1.75 "
                f"(Q={Q_uc:.4f} µC, D={D:.2f} µC/cm²)",
                UserWarning,
                stacklevel=4,
            )
