"""
WetLang NWB Integration — Project Janus v2.2 (R2)
Reads and writes Neurodata Without Borders (NWB) HDF5 files.
Core: h5py + numpy only. pynwb used only when available, for validation.
"""

from __future__ import annotations

import os
import datetime
import warnings
from typing import Any, Dict, Generator, Iterable, List, Optional, Sequence, Tuple

import numpy as np

try:
    import h5py
except ImportError as _h5_err:  # pragma: no cover
    raise ImportError(
        "h5py is required for NWB support. Install it with: pip install h5py"
    ) from _h5_err

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def read_nwb_recording(
    path: str,
    series_name: Optional[str] = None,
) -> Dict[str, Any]:
    """Read a full recording from an NWB file.

    Parameters
    ----------
    path:
        Path to the .nwb file.
    series_name:
        Name of an ElectricalSeries / TimeSeries dataset under
        /acquisition or /processing. If None, the first ElectricalSeries
        found is used.

    Returns
    -------
    dict with keys:
        data        : np.ndarray float32 shape (N, C)
        timestamps  : np.ndarray float64 shape (N,) in seconds
        channel_conversion : np.ndarray float64 shape (C,)
        electrodes  : dict  (meta from /general/extracellular_ephys/electrodes)
        units       : dict  (from /units or empty dict)
        series_name : str
        sample_rate : float or None
    """
    path = os.fspath(path)
    with h5py.File(path, "r") as f:
        series_grp = _find_series(f, series_name)
        name = series_grp.name.split("/")[-1]

        raw, conversion, channel_conversion, offset = _read_data_array(series_grp)
        timestamps = _read_timestamps(series_grp)
        _validate_timestamps(timestamps)

        electrodes = _read_electrodes(f)
        units = _read_units(f)

        sample_rate: Optional[float] = None
        if "starting_time" in series_grp:
            rate_attr = series_grp["starting_time"].attrs.get("rate", None)
            if rate_attr is not None:
                sample_rate = float(rate_attr)

    return {
        "data": raw,
        "timestamps": timestamps,
        "channel_conversion": channel_conversion,
        "electrodes": electrodes,
        "units": units,
        "series_name": name,
        "sample_rate": sample_rate,
    }


def iter_nwb_chunks(
    path: str,
    chunk_size: int,
    channel_ids: Optional[Sequence[int]] = None,
    halo: int = 0,
    series_name: Optional[str] = None,
) -> Generator[Tuple[np.ndarray, np.ndarray], None, None]:
    """Yield (data_chunk, timestamps_chunk) from an NWB file without loading all.

    Parameters
    ----------
    path       : Path to the .nwb file.
    chunk_size : Number of samples per chunk (excluding halo).
    channel_ids: Subset of channel indices to return. None = all.
    halo       : Extra samples prepended to each chunk (for filtering context).
    series_name: Specific series to read; None = first ElectricalSeries.

    Yields
    ------
    (data, timestamps) where data is float32 (chunk_size+halo, C).
    """
    path = os.fspath(path)
    with h5py.File(path, "r") as f:
        series_grp = _find_series(f, series_name)
        raw_ds = series_grp["data"]
        total_samples = raw_ds.shape[0]

        conversion = float(series_grp["data"].attrs.get("conversion", 1.0))
        offset = float(series_grp["data"].attrs.get("offset", 0.0))

        # channel_conversion — per-channel gain vector
        if "channel_conversion" in series_grp:
            ch_conv = np.array(series_grp["channel_conversion"], dtype=np.float64)
        else:
            n_ch = raw_ds.shape[1] if raw_ds.ndim > 1 else 1
            ch_conv = np.ones(n_ch, dtype=np.float64)

        # Resolve and sort channel subset
        n_ch = len(ch_conv)
        if channel_ids is None:
            ch_sel = list(range(n_ch))
        else:
            ch_sel_sorted = sorted(set(int(c) for c in channel_ids))
            if any(c < 0 or c >= n_ch for c in ch_sel_sorted):
                raise IndexError(f"channel_ids out of range [0, {n_ch - 1}]")
            # Restore original order after h5py sorted read
            orig_order = [sorted(set(int(c) for c in channel_ids)).index(int(c))
                          for c in channel_ids]
            ch_sel = ch_sel_sorted

        timestamps = _read_timestamps(series_grp)

        for start in range(0, total_samples, chunk_size):
            halo_start = max(0, start - halo)
            end = min(total_samples, start + chunk_size)
            if raw_ds.ndim == 1:
                raw_chunk = raw_ds[halo_start:end][:, np.newaxis].astype(np.float64)
            else:
                raw_chunk = raw_ds[halo_start:end, ch_sel].astype(np.float64)

            # Apply conversion × channel_conversion + offset
            sel_cc = ch_conv[ch_sel] if channel_ids is not None else ch_conv
            data_chunk = (raw_chunk * conversion * sel_cc[np.newaxis, :] + offset).astype(np.float32)
            ts_chunk = timestamps[halo_start:end]
            yield data_chunk, ts_chunk


def export_to_nwb(
    path: str,
    vm_run_data: Dict[str, Any],
    session_description: str = "WetLang simulation run",
    session_start_time: Optional[datetime.datetime] = None,
) -> None:
    """Write a WetVM run result dict to an NWB file.

    Parameters
    ----------
    path              : Output file path (will overwrite if exists).
    vm_run_data       : Dict with keys: spikes (list of dicts), voltages (ndarray N×C),
                        timestamps (ndarray N,), dt_s (float), channel_labels (list).
    session_description: Human-readable session description.
    session_start_time: Datetime of session; defaults to now (UTC).
    """
    path = os.fspath(path)
    if session_start_time is None:
        session_start_time = datetime.datetime.now(datetime.timezone.utc)

    timestamps = np.asarray(vm_run_data.get("timestamps", []), dtype=np.float64)
    voltages = np.asarray(vm_run_data.get("voltages", np.zeros((len(timestamps), 1))), dtype=np.float32)
    if voltages.ndim == 1:
        voltages = voltages[:, np.newaxis]
    channel_labels = vm_run_data.get("channel_labels", [str(i) for i in range(voltages.shape[1])])

    with h5py.File(path, "w") as f:
        # NWB root attributes
        f.attrs["neurodata_type"] = "NWBFile"
        f.attrs["namespace"] = "core"
        f.attrs["nwb_version"] = "2.7.0"
        f.attrs["file_create_date"] = session_start_time.isoformat()
        f.attrs["session_description"] = session_description
        f.attrs["session_start_time"] = session_start_time.isoformat()
        f.attrs["identifier"] = os.path.splitext(os.path.basename(path))[0]

        # /acquisition/WetLangSim
        acq = f.require_group("acquisition")
        series = acq.create_group("WetLangSim")
        series.attrs["neurodata_type"] = "ElectricalSeries"
        series.attrs["namespace"] = "core"
        series.attrs["description"] = "WetLang simulation membrane voltage trace"

        ds = series.create_dataset("data", data=voltages, compression="gzip", compression_opts=4)
        ds.attrs["conversion"] = 1.0
        ds.attrs["offset"] = 0.0
        ds.attrs["unit"] = "volts"

        series.create_dataset("timestamps", data=timestamps)

        # Channel labels
        dt_str = h5py.string_dtype(encoding="utf-8")
        series.create_dataset(
            "channel_conversion",
            data=np.ones(voltages.shape[1], dtype=np.float64)
        )

        # /general
        gen = f.require_group("general")
        gen.attrs["experimenter"] = ["WetLang v2.2"]
        gen.attrs["institution"] = "Project Janus"

    # Optionally validate with pynwb if available
    try:
        import pynwb  # type: ignore
        with pynwb.NWBHDF5IO(path, mode="r") as io:
            io.read()
    except ImportError:
        pass  # pynwb is optional


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _find_series(f: "h5py.File", series_name: Optional[str]) -> "h5py.Group":
    """Locate an ElectricalSeries / TimeSeries in /acquisition or /processing."""
    if series_name is not None:
        for root in ("acquisition", "processing"):
            if root in f and series_name in f[root]:
                grp = f[root][series_name]
                if isinstance(grp, h5py.Group) and "data" in grp:
                    return grp
        # Try nested in processing modules
        if "processing" in f:
            for mod_name, mod in f["processing"].items():
                if isinstance(mod, h5py.Group) and series_name in mod:
                    grp = mod[series_name]
                    if isinstance(grp, h5py.Group) and "data" in grp:
                        return grp
        raise KeyError(f"Series '{series_name}' not found in /acquisition or /processing")

    # Auto-discover: prefer ElectricalSeries
    for root in ("acquisition", "processing"):
        if root not in f:
            continue
        for name, grp in f[root].items():
            if isinstance(grp, h5py.Group) and "data" in grp:
                ns = grp.attrs.get("namespace", b"").decode() if isinstance(grp.attrs.get("namespace", ""), bytes) else grp.attrs.get("namespace", "")
                nt = grp.attrs.get("neurodata_type", b"").decode() if isinstance(grp.attrs.get("neurodata_type", ""), bytes) else grp.attrs.get("neurodata_type", "")
                if nt in ("ElectricalSeries", "TimeSeries") or "data" in grp:
                    return grp
    raise KeyError("No ElectricalSeries or TimeSeries found in /acquisition or /processing")


def _read_data_array(
    series_grp: "h5py.Group",
) -> Tuple[np.ndarray, float, np.ndarray, float]:
    """Read the data dataset, applying conversion and channel_conversion.

    Returns (data_float32_NC, conversion, channel_conversion_array, offset).
    """
    raw_ds = series_grp["data"]
    conversion = float(raw_ds.attrs.get("conversion", 1.0))
    offset = float(raw_ds.attrs.get("offset", 0.0))

    # Cast to float64 BEFORE multiplying (critical: avoids integer overflow)
    raw = np.array(raw_ds, dtype=np.float64)

    # Normalize 1D (N,) → (N, 1)
    if raw.ndim == 1:
        raw = raw[:, np.newaxis]

    n_ch = raw.shape[1]

    # channel_conversion: per-channel gain (shape (C,) or scalar)
    if "channel_conversion" in series_grp:
        ch_conv = np.array(series_grp["channel_conversion"], dtype=np.float64)
        if ch_conv.ndim == 0:
            ch_conv = np.full(n_ch, float(ch_conv))
        elif len(ch_conv) != n_ch:
            warnings.warn(
                f"channel_conversion length {len(ch_conv)} != data channels {n_ch}; using ones",
                RuntimeWarning, stacklevel=4
            )
            ch_conv = np.ones(n_ch, dtype=np.float64)
    else:
        ch_conv = np.ones(n_ch, dtype=np.float64)

    # Apply: data_SI = raw * conversion * channel_conversion[c] + offset
    data = (raw * conversion * ch_conv[np.newaxis, :] + offset).astype(np.float32)
    return data, conversion, ch_conv, offset


def _read_timestamps(series_grp: "h5py.Group") -> np.ndarray:
    """Return a float64 1-D timestamps array in seconds."""
    if "timestamps" in series_grp:
        ts = np.array(series_grp["timestamps"], dtype=np.float64)
        return ts

    # Reconstruct from starting_time + rate
    n = series_grp["data"].shape[0]
    t0 = 0.0
    rate = None
    if "starting_time" in series_grp:
        t0 = float(series_grp["starting_time"][()])
        # Rate is stored as an attribute on the starting_time dataset (NWB spec)
        rate = series_grp["starting_time"].attrs.get("rate", None)
        if rate is not None:
            rate = float(rate)

    if rate is None or rate <= 0:
        raise ValueError(
            "NWB series has no timestamps dataset and no valid starting_time/rate. "
            "Cannot reconstruct timestamps."
        )

    return t0 + np.arange(n, dtype=np.float64) / rate


def _validate_timestamps(ts: np.ndarray) -> None:
    """Raise ValueError for non-finite or non-monotonic timestamps."""
    if len(ts) == 0:
        return
    if not np.all(np.isfinite(ts)):
        raise ValueError("NWB timestamps contain non-finite values (NaN or Inf).")
    diffs = np.diff(ts)
    if not np.all(diffs > 0):
        n_bad = int(np.sum(diffs <= 0))
        raise ValueError(
            f"NWB timestamps are not strictly monotonically increasing "
            f"({n_bad} non-positive intervals found)."
        )


def _read_electrodes(f: "h5py.File") -> Dict[str, Any]:
    """Read /general/extracellular_ephys/electrodes table if present."""
    path = "general/extracellular_ephys/electrodes"
    if path not in f:
        return {}
    tbl = f[path]
    result: Dict[str, Any] = {}
    for col_name in tbl.keys():
        col = tbl[col_name]
        if isinstance(col, h5py.Dataset):
            arr = np.array(col)
            # Decode byte-strings
            if arr.dtype.kind in ("S", "O"):
                try:
                    arr = arr.astype(str)
                except Exception:
                    pass
            result[col_name] = arr
    return result


def _read_units(f: "h5py.File") -> Dict[str, Any]:
    """Read /units table if present (spike sort results)."""
    if "units" not in f:
        return {}
    units_grp = f["units"]
    result: Dict[str, Any] = {}
    for col_name in units_grp.keys():
        col = units_grp[col_name]
        if isinstance(col, h5py.Dataset):
            try:
                arr = np.array(col)
                if arr.dtype.kind in ("S", "O"):
                    try:
                        arr = arr.astype(str)
                    except Exception:
                        pass
                result[col_name] = arr
            except Exception:
                pass  # Skip unreadable columns (VectorIndex, etc.)
    return result
