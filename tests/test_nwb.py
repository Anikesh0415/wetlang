"""
tests/test_nwb.py — Project Janus v2.2 (R2)
NWB read/write integration tests.

All tests run offline (no network). Synthetic .nwb files are created in
a tmp directory using h5py directly so we have no pynwb dependency in CI.
"""

from __future__ import annotations

import datetime
import io
import os
import struct
import tempfile
from typing import Optional

import numpy as np
import pytest

try:
    import h5py
except ImportError:
    pytest.skip("h5py not installed", allow_module_level=True)

from wetlang.nwb import (
    read_nwb_recording,
    iter_nwb_chunks,
    export_to_nwb,
    _find_series,
    _read_timestamps,
    _validate_timestamps,
)


# ---------------------------------------------------------------------------
# Helpers — synthetic NWB creation
# ---------------------------------------------------------------------------


def _make_nwb(
    path: str,
    n_samples: int = 200,
    n_channels: int = 4,
    dtype: type = np.int16,
    conversion: float = 1e-6,
    offset: float = 0.0,
    has_channel_conversion: bool = False,
    sample_rate: float = 10_000.0,
    use_timestamps: bool = True,
    has_units: bool = False,
    make_monotonic: bool = True,
) -> None:
    """Write a minimal valid NWB HDF5 file."""
    rng = np.random.default_rng(42)
    raw = rng.integers(-32768, 32767, (n_samples, n_channels), dtype=np.int16).astype(dtype)

    with h5py.File(path, "w") as f:
        f.attrs["neurodata_type"] = "NWBFile"
        f.attrs["nwb_version"] = "2.7.0"
        f.attrs["session_description"] = "test"
        f.attrs["identifier"] = "test-nwb"
        f.attrs["session_start_time"] = "2024-01-01T00:00:00+00:00"
        f.attrs["file_create_date"] = "2024-01-01T00:00:00+00:00"

        acq = f.require_group("acquisition")
        series = acq.create_group("TestSeries")
        series.attrs["neurodata_type"] = "ElectricalSeries"
        series.attrs["namespace"] = "core"
        series.attrs["description"] = "synthetic test series"

        ds = series.create_dataset("data", data=raw)
        ds.attrs["conversion"] = conversion
        ds.attrs["offset"] = offset
        ds.attrs["unit"] = "volts"

        if has_channel_conversion:
            cc = rng.uniform(0.9, 1.1, n_channels)
            series.create_dataset("channel_conversion", data=cc.astype(np.float64))

        if use_timestamps:
            ts = np.arange(n_samples, dtype=np.float64) / sample_rate
            if not make_monotonic:
                ts[5] = ts[4]  # duplicate → not strictly monotonic
            series.create_dataset("timestamps", data=ts)
        else:
            # Store starting_time with rate attribute
            st_ds = series.create_dataset("starting_time", data=0.0)
            st_ds.attrs["rate"] = sample_rate
            st_ds.attrs["unit"] = "seconds"

        if has_units:
            units = f.require_group("units")
            units.attrs["neurodata_type"] = "Units"
            units.create_dataset("id", data=np.array([0, 1, 2], dtype=np.int32))
            units.create_dataset("spike_times", data=np.array([0.001, 0.005, 0.010]))


# ---------------------------------------------------------------------------
# Tests — basic read
# ---------------------------------------------------------------------------


def test_read_nwb_basic_shape():
    """read_nwb_recording returns correct shape (N, C)."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=100, n_channels=8)
        result = read_nwb_recording(path)
        assert result["data"].shape == (100, 8), f"Unexpected shape: {result['data'].shape}"
        assert result["data"].dtype == np.float32
        assert result["timestamps"].shape == (100,)
        assert result["timestamps"].dtype == np.float64
    finally:
        os.unlink(path)


def test_read_nwb_int16_conversion():
    """Integer data cast to float BEFORE multiplying by conversion (no overflow)."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=50, n_channels=2, dtype=np.int16, conversion=1e-6)
        result = read_nwb_recording(path)
        # int16 max = 32767; * 1e-6 ≈ 0.03 V — values must be small
        assert np.all(np.abs(result["data"]) < 1.0), "Conversion likely applied incorrectly"
    finally:
        os.unlink(path)


def test_read_nwb_channel_conversion():
    """Per-channel gain (channel_conversion) is applied correctly."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=50, n_channels=4, conversion=1.0, has_channel_conversion=True)
        result = read_nwb_recording(path)
        assert result["channel_conversion"].shape == (4,)
        assert not np.all(result["channel_conversion"] == 1.0), "Expected non-trivial ch_conv"
    finally:
        os.unlink(path)


def test_read_nwb_1d_data_normalized_to_2d():
    """1D data (N,) is normalized to (N, 1)."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        with h5py.File(path, "w") as f:
            f.attrs.update({
                "neurodata_type": "NWBFile",
                "nwb_version": "2.7.0",
                "session_description": "test",
                "identifier": "1d-test",
                "session_start_time": "2024-01-01T00:00:00+00:00",
                "file_create_date": "2024-01-01T00:00:00+00:00",
            })
            acq = f.require_group("acquisition")
            s = acq.create_group("TestSeries")
            s.attrs["neurodata_type"] = "ElectricalSeries"
            ds = s.create_dataset("data", data=np.arange(60, dtype=np.float32))
            ds.attrs["conversion"] = 1.0
            ds.attrs["offset"] = 0.0
            s.create_dataset("timestamps", data=np.arange(60, dtype=np.float64) / 1000)

        result = read_nwb_recording(path)
        assert result["data"].shape == (60, 1), f"Expected (60,1), got {result['data'].shape}"
    finally:
        os.unlink(path)


def test_read_nwb_starting_time_rate():
    """Timestamps are reconstructed from starting_time + rate when no timestamps dataset."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=200, n_channels=1, use_timestamps=False, sample_rate=20_000.0)
        result = read_nwb_recording(path)
        ts = result["timestamps"]
        assert len(ts) == 200
        # Check spacing: 1/20000 = 50 µs
        np.testing.assert_allclose(np.diff(ts), 1 / 20_000.0, rtol=1e-9)
    finally:
        os.unlink(path)


def test_read_nwb_non_monotonic_timestamps_raises():
    """Non-monotonic timestamps raise ValueError."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=50, n_channels=2, make_monotonic=False)
        with pytest.raises(ValueError, match="monotonically"):
            read_nwb_recording(path)
    finally:
        os.unlink(path)


def test_read_nwb_missing_series_raises():
    """KeyError raised when requested series_name does not exist."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=10, n_channels=2)
        with pytest.raises(KeyError, match="NonExistent"):
            read_nwb_recording(path, series_name="NonExistent")
    finally:
        os.unlink(path)


def test_read_nwb_units_table():
    """Units table is read when present."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=50, n_channels=2, has_units=True)
        result = read_nwb_recording(path)
        assert "id" in result["units"], "Expected 'id' column in units"
    finally:
        os.unlink(path)


def test_read_nwb_missing_units_returns_empty():
    """Missing /units table returns empty dict (no error)."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=50, n_channels=2, has_units=False)
        result = read_nwb_recording(path)
        assert result["units"] == {}
    finally:
        os.unlink(path)


# ---------------------------------------------------------------------------
# Tests — iter_nwb_chunks
# ---------------------------------------------------------------------------


def test_iter_nwb_chunks_total_samples():
    """All samples are yielded across chunks."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        n_samples = 350
        _make_nwb(path, n_samples=n_samples, n_channels=4)
        total = 0
        for chunk, ts in iter_nwb_chunks(path, chunk_size=100):
            # halo=0 so chunks don't overlap
            total += len(chunk)
            assert chunk.dtype == np.float32
            assert chunk.shape[1] == 4
        assert total == n_samples
    finally:
        os.unlink(path)


def test_iter_nwb_chunks_channel_subset():
    """channel_ids subset is respected."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=100, n_channels=8)
        for chunk, _ in iter_nwb_chunks(path, chunk_size=50, channel_ids=[0, 2, 4]):
            assert chunk.shape[1] == 3
    finally:
        os.unlink(path)


def test_iter_nwb_chunks_invalid_channel_raises():
    """channel_ids out of range raises IndexError."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=100, n_channels=4)
        with pytest.raises(IndexError):
            for _ in iter_nwb_chunks(path, chunk_size=50, channel_ids=[0, 99]):
                pass
    finally:
        os.unlink(path)


# ---------------------------------------------------------------------------
# Tests — export_to_nwb
# ---------------------------------------------------------------------------


def test_export_to_nwb_roundtrip():
    """export_to_nwb writes a valid file that can be read back."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        n, c = 500, 16
        rng = np.random.default_rng(7)
        vm_data = {
            "timestamps": np.arange(n, dtype=np.float64) / 10_000.0,
            "voltages": rng.normal(0.0, 5e-3, (n, c)).astype(np.float32),
            "channel_labels": [f"ch{i}" for i in range(c)],
        }
        export_to_nwb(path, vm_data, session_description="export roundtrip test")

        # Read back
        result = read_nwb_recording(path, series_name="WetLangSim")
        assert result["data"].shape == (n, c), f"Unexpected shape: {result['data'].shape}"
        assert result["timestamps"].shape == (n,)
    finally:
        os.unlink(path)


def test_export_to_nwb_default_start_time():
    """export_to_nwb works with no explicit session_start_time."""
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        vm_data = {
            "timestamps": np.array([0.0, 0.001, 0.002]),
            "voltages": np.zeros((3, 2), dtype=np.float32),
        }
        export_to_nwb(path, vm_data)
        with h5py.File(path, "r") as f:
            assert "file_create_date" in f.attrs
    finally:
        os.unlink(path)


# ---------------------------------------------------------------------------
# Tests — _validate_timestamps edge cases
# ---------------------------------------------------------------------------


def test_validate_timestamps_nan_raises():
    ts = np.array([0.0, np.nan, 0.002])
    with pytest.raises(ValueError, match="non-finite"):
        _validate_timestamps(ts)


def test_validate_timestamps_inf_raises():
    ts = np.array([0.0, np.inf, 0.002])
    with pytest.raises(ValueError, match="non-finite"):
        _validate_timestamps(ts)


def test_validate_timestamps_empty_ok():
    _validate_timestamps(np.array([]))  # Should not raise


def test_validate_timestamps_single_ok():
    _validate_timestamps(np.array([1.0]))  # single point, no diff to check


# ---------------------------------------------------------------------------
# Tests — CLI Integration
# ---------------------------------------------------------------------------


def test_cli_nwb_inspect(capsys):
    """wetlang nwb inspect prints metadata summary."""
    from wetlang.cli import main as cli_main

    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        path = tf.name
    try:
        _make_nwb(path, n_samples=100, n_channels=8)
        ret = cli_main(["nwb", "inspect", path])
        assert ret == 0
        captured = capsys.readouterr()
        assert "Series Name" in captured.out
        assert "Channels       : 8" in captured.out
        assert "Total Samples  : 100" in captured.out
    finally:
        os.unlink(path)


def test_cli_nwb_replay(capsys):
    """wetlang nwb replay streams chunks and optionally exports."""
    from wetlang.cli import main as cli_main

    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf1, \
         tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf2:
        in_path = tf1.name
        out_path = tf2.name
    try:
        _make_nwb(in_path, n_samples=250, n_channels=4)
        ret = cli_main(["nwb", "replay", in_path, "--chunk-size", "100", "--export-nwb", out_path])
        assert ret == 0
        captured = capsys.readouterr()
        assert "Replay complete: 3 chunks (250 samples) processed." in captured.out
        assert f"Exported replay data to '{out_path}'." in captured.out
        assert os.path.exists(out_path)
    finally:
        if os.path.exists(in_path):
            os.unlink(in_path)
        if os.path.exists(out_path):
            os.unlink(out_path)

