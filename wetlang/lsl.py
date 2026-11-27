"""
WetLang LSL Integration — Project Janus v2.2 (R3)
Lab Streaming Layer (LSL) adapter for real-time neurophysiology data.

Gracefully handles missing pylsl install — falls back to synthetic data
so the wetlang module can always be imported.
"""

from __future__ import annotations

import threading
import time
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence

import numpy as np

# ---------------------------------------------------------------------------
# Optional pylsl import — runtime guard
# ---------------------------------------------------------------------------
_pylsl: Any = None
_LSL_AVAILABLE = False

try:
    import pylsl as _pylsl  # type: ignore
    _LSL_AVAILABLE = True
except (ImportError, RuntimeError, OSError) as _lsl_err:
    warnings.warn(
        f"pylsl not available ({_lsl_err}). LSLAdapter will run in synthetic mode.",
        ImportWarning,
        stacklevel=1,
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


class LSLAdapter:
    """Bidirectional LSL stream adapter for WetLang closed-loop experiments.

    When pylsl is not installed or no live stream is found, the adapter
    operates in synthetic mode (is_live_lsl = False), generating sinusoidal
    test data so the rest of the pipeline remains exercisable offline.

    Parameters
    ----------
    stream_name  : LSL stream name to search for (default "WetLang").
    n_channels   : Number of channels to expect / generate.
    sample_rate  : Nominal sample rate in Hz (used for synthetic mode).
    timeout_s    : Seconds to wait when resolving a live LSL stream.
    synthetic_freq_hz: Frequency of synthetic sinusoid for each channel.
    """

    is_live_lsl: bool

    def __init__(
        self,
        stream_name: str = "WetLang",
        n_channels: int = 64,
        sample_rate: float = 10_000.0,
        timeout_s: float = 2.0,
        synthetic_freq_hz: float = 10.0,
    ) -> None:
        self.stream_name = stream_name
        self.n_channels = n_channels
        self.sample_rate = sample_rate
        self.timeout_s = timeout_s
        self.synthetic_freq_hz = synthetic_freq_hz

        self._inlet: Any = None
        self._outlet: Any = None
        self._t0: float = time.monotonic()
        self._lock = threading.Lock()
        self._running = False

        self.is_live_lsl = self._try_connect()

    # ------------------------------------------------------------------
    # Connection management
    # ------------------------------------------------------------------

    def _try_connect(self) -> bool:
        """Attempt to find and connect to a live LSL stream.

        Returns True iff a live inlet was successfully opened.
        """
        if not _LSL_AVAILABLE:
            return False
        try:
            streams = _pylsl.resolve_byprop(
                "name", self.stream_name, timeout=self.timeout_s
            )
            if not streams:
                return False
            info = streams[0]
            self._inlet = _pylsl.StreamInlet(info, max_buflen=360)
            self.n_channels = info.channel_count()
            self.sample_rate = info.nominal_srate()
            return True
        except Exception as exc:
            warnings.warn(
                f"LSL connection failed ({exc}); using synthetic mode.",
                RuntimeWarning,
                stacklevel=3,
            )
            return False

    def open_outlet(
        self,
        outlet_name: str = "WetLangOutput",
        outlet_type: str = "Markers",
        n_channels: int = 1,
        channel_format: str = "float32",
    ) -> None:
        """Open an LSL outlet for sending stimulation markers / commands.

        No-op in synthetic mode.
        """
        if not _LSL_AVAILABLE or not self.is_live_lsl:
            return
        try:
            info = _pylsl.StreamInfo(
                outlet_name, outlet_type, n_channels,
                self.sample_rate, channel_format, "wetlang-outlet"
            )
            self._outlet = _pylsl.StreamOutlet(info)
        except Exception as exc:
            warnings.warn(f"Failed to open LSL outlet: {exc}", RuntimeWarning, stacklevel=2)

    def close(self) -> None:
        """Release inlet and outlet resources."""
        with self._lock:
            self._running = False
            if self._inlet is not None:
                try:
                    self._inlet.close_stream()
                except Exception:
                    pass
                self._inlet = None
            self._outlet = None

    # ------------------------------------------------------------------
    # Data reading
    # ------------------------------------------------------------------

    def pull_chunk(
        self,
        max_samples: int = 1024,
        timeout: float = 0.0,
    ) -> tuple[np.ndarray, np.ndarray]:
        """Pull a chunk of samples from the LSL inlet.

        Returns
        -------
        (data, timestamps)
            data       : float32 ndarray shape (N, C) where N <= max_samples
            timestamps : float64 ndarray shape (N,) in LSL clock seconds
        """
        if self.is_live_lsl and self._inlet is not None:
            try:
                chunk, ts = self._inlet.pull_chunk(
                    timeout=timeout, max_samples=max_samples
                )
                if not chunk:
                    return np.empty((0, self.n_channels), dtype=np.float32), np.empty(0)
                data = np.array(chunk, dtype=np.float32)
                if data.ndim == 1:
                    data = data[:, np.newaxis]
                return data, np.array(ts, dtype=np.float64)
            except Exception as exc:
                warnings.warn(f"LSL pull_chunk failed: {exc}", RuntimeWarning, stacklevel=2)

        # Synthetic fallback: generate one-chunk of sinusoidal data
        return self._synthetic_chunk(max_samples)

    def _synthetic_chunk(self, n: int) -> tuple[np.ndarray, np.ndarray]:
        """Generate a synthetic sinusoidal chunk."""
        t_now = time.monotonic() - self._t0
        dt = 1.0 / self.sample_rate
        t = t_now + np.arange(n) * dt
        # Each channel has a slightly different frequency
        freqs = self.synthetic_freq_hz * (1 + np.arange(self.n_channels) * 0.01)
        # shape (n, C)
        data = np.sin(2 * np.pi * freqs[np.newaxis, :] * t[:, np.newaxis]).astype(np.float32)
        timestamps = t.astype(np.float64)
        return data, timestamps

    def pull_sample(self, timeout: float = 0.0) -> tuple[np.ndarray, float]:
        """Pull a single sample. Returns (sample_array, timestamp)."""
        if self.is_live_lsl and self._inlet is not None:
            try:
                sample, ts = self._inlet.pull_sample(timeout=timeout)
                return np.array(sample, dtype=np.float32), float(ts)
            except Exception:
                pass
        # Synthetic fallback
        data, ts = self._synthetic_chunk(1)
        return data[0], float(ts[0])

    # ------------------------------------------------------------------
    # Closed-loop trigger output
    # ------------------------------------------------------------------

    def push_sample(self, values: Sequence[float], timestamp: float = 0.0) -> None:
        """Push a sample to the LSL outlet (e.g., stimulation trigger marker).

        No-op in synthetic mode or if outlet was not opened.
        """
        if not self.is_live_lsl or self._outlet is None:
            return
        try:
            self._outlet.push_sample(list(values), timestamp or _pylsl.local_clock())
        except Exception as exc:
            warnings.warn(f"LSL push_sample failed: {exc}", RuntimeWarning, stacklevel=2)

    # ------------------------------------------------------------------
    # Convenience streaming loop
    # ------------------------------------------------------------------

    def stream_to_callback(
        self,
        callback: Callable[[np.ndarray, np.ndarray], None],
        chunk_size: int = 256,
        max_seconds: Optional[float] = None,
    ) -> None:
        """Block and call `callback(data, timestamps)` for each chunk.

        Parameters
        ----------
        callback    : Receives (data float32 (N,C), timestamps float64 (N,)).
        chunk_size  : Samples per callback invocation.
        max_seconds : Stop after this many seconds (None = run forever).
        """
        self._running = True
        t_start = time.monotonic()
        try:
            while self._running:
                if max_seconds is not None and (time.monotonic() - t_start) >= max_seconds:
                    break
                data, ts = self.pull_chunk(max_samples=chunk_size, timeout=0.01)
                if len(data) > 0:
                    callback(data, ts)
        finally:
            self._running = False

    def stop(self) -> None:
        """Signal streaming loop to stop."""
        self._running = False

    # ------------------------------------------------------------------
    # Context manager support
    # ------------------------------------------------------------------

    def __enter__(self) -> "LSLAdapter":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        mode = "live" if self.is_live_lsl else "synthetic"
        return (
            f"LSLAdapter(stream={self.stream_name!r}, "
            f"n_channels={self.n_channels}, "
            f"sample_rate={self.sample_rate:.1f} Hz, "
            f"mode={mode!r})"
        )
