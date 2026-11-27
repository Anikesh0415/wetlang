"""
tests/test_lsl.py — Project Janus v2.2 (R3)
LSL adapter tests (online mock & offline fallback mode).
"""

from __future__ import annotations

import numpy as np
import pytest
from wetlang.lsl import LSLAdapter


def test_lsl_adapter_offline_mode():
    """When no live LSL daemon is running, adapter runs in synthetic mode."""
    with LSLAdapter(stream_name="NonExistentStream12345", n_channels=16, sample_rate=1000.0, timeout_s=0.1) as adapter:
        assert isinstance(adapter.is_live_lsl, bool)
        # In typical test runner without labstreaminglayer stream:
        assert adapter.n_channels == 16
        assert adapter.sample_rate == 1000.0


def test_lsl_pull_chunk_synthetic():
    """Synthetic pull_chunk returns expected array shapes and types."""
    with LSLAdapter(n_channels=32, sample_rate=1000.0, timeout_s=0.1) as adapter:
        data, ts = adapter.pull_chunk(max_samples=100)
        assert data.shape == (100, 32)
        assert data.dtype == np.float32
        assert len(ts) == 100
        assert ts.dtype == np.float64
        # Timestamps must be monotonic
        assert np.all(np.diff(ts) > 0)


def test_lsl_pull_sample_synthetic():
    """Synthetic pull_sample returns single 1D vector and float timestamp."""
    with LSLAdapter(n_channels=8, sample_rate=1000.0, timeout_s=0.1) as adapter:
        sample, ts = adapter.pull_sample()
        assert sample.shape == (8,)
        assert sample.dtype == np.float32
        assert isinstance(ts, float)


def test_lsl_stream_to_callback_synthetic():
    """stream_to_callback invokes callback with valid chunks and respects max_seconds."""
    chunks_received = []

    def on_chunk(data, ts):
        chunks_received.append((data, ts))

    with LSLAdapter(n_channels=4, sample_rate=1000.0, timeout_s=0.1) as adapter:
        adapter.stream_to_callback(on_chunk, chunk_size=50, max_seconds=0.15)

    assert len(chunks_received) > 0
    first_data, first_ts = chunks_received[0]
    assert first_data.shape == (50, 4)
    assert len(first_ts) == 50


def test_lsl_outlet_and_push_sample():
    """push_sample and open_outlet are safe no-ops or functional without error."""
    with LSLAdapter(n_channels=8, timeout_s=0.1) as adapter:
        adapter.open_outlet("TestOut", n_channels=2)
        adapter.push_sample([1.0, 2.0])
        adapter.close()
