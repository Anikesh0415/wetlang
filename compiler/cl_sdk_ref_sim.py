"""
WetLang Compiler — Closed-Loop SDK Reference Simulator (Project Janus v2.2, R3)
Target: --target=cl_sdk

Emits Python-level closed-loop SDK event callbacks instead of bare bytecode.
Used for rapid offline testing of closed-loop logic without hardware.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import numpy as np


class CLSDKRefSimError(Exception):
    """Raised when the CL SDK reference sim cannot execute an operation."""


class ClosedLoopSnapshot:
    """Mirrors wet_closed_loop_snapshot_t from wetvm_api.h."""

    __slots__ = (
        "tick",
        "channel_voltages_mv",
        "channel_spike_flags",
        "blanking_active",
        "pop_firing_rate_hz",
        "timestamp_us",
    )

    def __init__(
        self,
        tick: int,
        n_channels: int = 64,
        rng: Optional[np.random.Generator] = None,
    ) -> None:
        rng = rng or np.random.default_rng(tick)
        self.tick: int = tick
        self.channel_voltages_mv: np.ndarray = rng.normal(0.0, 5.0, n_channels).astype(np.float32)
        self.channel_spike_flags: np.ndarray = (rng.random(n_channels) > 0.98).astype(np.uint8)
        self.blanking_active: bool = False
        self.pop_firing_rate_hz: float = float(np.sum(self.channel_spike_flags)) * 1e4
        self.timestamp_us: int = tick * 100  # 100 µs per tick

    def __repr__(self) -> str:
        spikes = int(np.sum(self.channel_spike_flags))
        return (
            f"ClosedLoopSnapshot(tick={self.tick}, "
            f"spikes={spikes}, "
            f"rate={self.pop_firing_rate_hz:.1f} Hz, "
            f"blanking={self.blanking_active})"
        )


class ClosedLoopCommand:
    """Mirrors wet_closed_loop_cmd_t from wetvm_api.h."""

    __slots__ = ("stim_channel", "stim_amplitude_ua", "stim_duration_ms", "inhibit")

    def __init__(
        self,
        stim_channel: int = 0,
        stim_amplitude_ua: float = 0.0,
        stim_duration_ms: float = 0.0,
        inhibit: bool = False,
    ) -> None:
        self.stim_channel = stim_channel
        self.stim_amplitude_ua = stim_amplitude_ua
        self.stim_duration_ms = stim_duration_ms
        self.inhibit = inhibit


class CLSDKRefSim:
    """Reference simulator for the WetLang Closed-Loop SDK target.

    Executes a simplified closed-loop tick loop:
    1. Generate a synthetic snapshot at each tick.
    2. Call the registered hook (if any).
    3. Apply blanking if set via SET_BLANKING opcode.
    4. Record results.

    Parameters
    ----------
    n_ticks     : Total simulation ticks.
    n_channels  : Number of electrode channels.
    tick_period_us: Tick period in microseconds (default 100 µs = 10 kHz).
    seed        : RNG seed for reproducibility.
    """

    def __init__(
        self,
        n_ticks: int = 1000,
        n_channels: int = 64,
        tick_period_us: float = 100.0,
        seed: int = 42,
    ) -> None:
        self.n_ticks = n_ticks
        self.n_channels = n_channels
        self.tick_period_us = tick_period_us
        self._rng = np.random.default_rng(seed)
        self._hook: Optional[Any] = None  # callable(snapshot) -> ClosedLoopCommand
        self._blanking_ms: float = 0.0
        self._blanking_channel: int = 0xFFFF  # 0xFFFF = global
        self._blanking_ticks: int = 0
        self._snapshots: List[ClosedLoopSnapshot] = []
        self._commands: List[Optional[ClosedLoopCommand]] = []

    def register_closed_loop_hook(self, hook: Any) -> None:
        """Register a Python callable as the closed-loop hook.

        The hook receives a ClosedLoopSnapshot and returns a ClosedLoopCommand.
        """
        self._hook = hook

    def set_blanking(self, channel: int, duration_ms: float) -> None:
        """Configure blanking (mirrors WET_OP_SET_BLANKING)."""
        if duration_ms < 0.1 or duration_ms > 20.0:
            raise CLSDKRefSimError(
                f"Blanking duration {duration_ms:.3f} ms out of valid range [0.1, 20.0]"
            )
        self._blanking_ms = duration_ms
        self._blanking_channel = channel
        self._blanking_ticks = int(duration_ms * 1e-3 / (self.tick_period_us * 1e-6))

    def run(self) -> Dict[str, Any]:
        """Execute the simulation loop.

        Returns
        -------
        dict with keys:
            snapshots : List[ClosedLoopSnapshot]
            commands  : List[Optional[ClosedLoopCommand]]
            spike_counts : np.ndarray shape (n_ticks,)
            timestamps_us : np.ndarray shape (n_ticks,)
        """
        self._snapshots = []
        self._commands = []
        blanking_countdown = 0

        for tick in range(self.n_ticks):
            snap = ClosedLoopSnapshot(tick, self.n_channels, self._rng)

            # Apply blanking
            if blanking_countdown > 0:
                snap.blanking_active = True
                blanking_countdown -= 1

            cmd: Optional[ClosedLoopCommand] = None
            if self._hook is not None and not snap.blanking_active:
                try:
                    cmd = self._hook(snap)
                except Exception as exc:
                    raise CLSDKRefSimError(f"Hook raised exception at tick {tick}: {exc}") from exc

                # If hook issues a stim, trigger blanking
                if cmd is not None and cmd.stim_amplitude_ua != 0.0:
                    blanking_countdown = self._blanking_ticks

            self._snapshots.append(snap)
            self._commands.append(cmd)

        spike_counts = np.array(
            [int(np.sum(s.channel_spike_flags)) for s in self._snapshots], dtype=np.int32
        )
        timestamps_us = np.array([s.timestamp_us for s in self._snapshots], dtype=np.int64)

        return {
            "snapshots": self._snapshots,
            "commands": self._commands,
            "spike_counts": spike_counts,
            "timestamps_us": timestamps_us,
        }
