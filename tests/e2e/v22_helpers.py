"""Shared opaque-box helpers for WetLang Project Janus v2.2 E2E tests.

Strict lazy-import discipline:
    This module NEVER imports ``wetlang``, ``wetlang.*``, ``bindings.aer``,
    ``bindings.distributed``, ``bindings.runtime``, ``bindings.ffi``,
    ``compiler.*``, ``tests.e2e.common``, or loads ``wetvm.dll`` at module
    top level.
"""

from __future__ import annotations

from collections import deque
from contextlib import contextmanager
from datetime import datetime
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys
import threading
import time
import types
from typing import Any, Iterator, Mapping, Sequence, Union
import uuid

import h5py
import numpy as np


PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]

_SENTINEL = object()


# ---------------------------------------------------------------------------
# Subprocess CLI Runners
# ---------------------------------------------------------------------------


def _build_cli_env(extra_env: Mapping[str, str] | None = None) -> dict[str, str]:
    env = os.environ.copy()
    if extra_env:
        env.update({k: str(v) for k, v in extra_env.items()})
    root_str = str(PROJECT_ROOT)
    existing_pp = env.get("PYTHONPATH", "")
    if existing_pp:
        parts = existing_pp.split(os.pathsep)
        if root_str not in parts:
            env["PYTHONPATH"] = f"{root_str}{os.pathsep}{existing_pp}"
    else:
        env["PYTHONPATH"] = root_str
    env.setdefault("PYTHONIOENCODING", "utf-8")
    return env


def run_wetlang_cli(
    args: Sequence[Union[str, Path]],
    cwd: Union[str, Path, None] = None,
    stdin_text: str | None = None,
    timeout: int = 30,
    env: Mapping[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run ``python -m wetlang.cli <args>`` with UTF-8 I/O and PROJECT_ROOT on PYTHONPATH."""
    cmd = [sys.executable, "-m", "wetlang.cli", *[str(a) for a in args]]
    return subprocess.run(
        cmd,
        cwd=str(cwd if cwd is not None else PROJECT_ROOT),
        input=stdin_text,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        env=_build_cli_env(env),
    )


def run_wetc_cli(
    args: Sequence[Union[str, Path]],
    cwd: Union[str, Path, None] = None,
    timeout: int = 30,
    env: Mapping[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run ``python -m compiler.compiler_cli <args>`` with UTF-8 I/O and PROJECT_ROOT on PYTHONPATH."""
    cmd = [sys.executable, "-m", "compiler.compiler_cli", *[str(a) for a in args]]
    return subprocess.run(
        cmd,
        cwd=str(cwd if cwd is not None else PROJECT_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        env=_build_cli_env(env),
    )


# ---------------------------------------------------------------------------
# Synthetic NWB 2.x Builder & Schema Validator
# ---------------------------------------------------------------------------


def _decode_h5_str(val: Any) -> str:
    if isinstance(val, bytes):
        return val.decode("utf-8", errors="replace")
    if isinstance(val, np.bytes_):
        return bytes(val).decode("utf-8", errors="replace")
    if isinstance(val, np.ndarray):
        if val.ndim == 0:
            return _decode_h5_str(val.item())
        return _decode_h5_str(val.flat[0]) if val.size > 0 else ""
    return str(val)


def _write_electrical_series(
    acq_group: h5py.Group,
    name: str,
    *,
    num_samples: int,
    num_channels: int,
    rate_hz: float,
    starting_time: float,
    explicit_timestamps: bool,
    conversion: float,
    channel_conversion: Sequence[float] | None,
    offset: float,
    dtype: str,
    oned: bool,
    bad_timestamps: Any,
    signal_data: Any,
    electrodes_group: h5py.Group | None,
) -> None:
    series_grp = acq_group.create_group(name)
    series_grp.attrs["neurodata_type"] = "ElectricalSeries"
    series_grp.attrs["namespace"] = "core"
    series_grp.attrs["object_id"] = str(uuid.uuid4())
    series_grp.attrs["description"] = f"Synthetic {name}"
    series_grp.attrs["comments"] = "no comments"

    np_dtype = np.dtype(dtype)
    if signal_data is not None:
        arr = np.asarray(signal_data, dtype=np_dtype)
        if oned and arr.ndim == 2 and arr.shape[1] == 1:
            arr = arr[:, 0]
        elif not oned and arr.ndim == 1:
            arr = arr[:, np.newaxis]
        actual_samples = arr.shape[0]
        actual_channels = 1 if arr.ndim == 1 else arr.shape[1]
    else:
        actual_samples = int(num_samples)
        actual_channels = 1 if oned else int(num_channels)
        t_idx = np.arange(actual_samples, dtype=np.float64) / float(rate_hz)
        if oned:
            wave = 50.0 * np.sin(2.0 * np.pi * 10.0 * t_idx)
            arr = np.asarray(np.rint(wave) if np.issubdtype(np_dtype, np.integer) else wave, dtype=np_dtype)
        else:
            ch_offsets = np.arange(actual_channels, dtype=np.float64)[np.newaxis, :] * 0.4
            wave = 50.0 * np.sin(2.0 * np.pi * 10.0 * t_idx[:, np.newaxis] + ch_offsets)
            arr = np.asarray(np.rint(wave) if np.issubdtype(np_dtype, np.integer) else wave, dtype=np_dtype)

    data_ds = series_grp.create_dataset("data", data=arr)
    data_ds.attrs["conversion"] = float(conversion)
    data_ds.attrs["offset"] = float(offset)
    data_ds.attrs["unit"] = "volts"
    data_ds.attrs["resolution"] = -1.0
    data_ds.attrs["continuity"] = "continuous"

    if channel_conversion is not None:
        cc = np.asarray(channel_conversion, dtype=np.float32)
        cc_ds = series_grp.create_dataset("channel_conversion", data=cc)
        cc_ds.attrs["unit"] = "volts"

    if bad_timestamps is not None or explicit_timestamps:
        ts = float(starting_time) + np.arange(actual_samples, dtype=np.float64) / float(rate_hz)
        if bad_timestamps is not None:
            if isinstance(bad_timestamps, str):
                mode = bad_timestamps.lower()
                mid = min(max(0, actual_samples // 2), max(0, actual_samples - 1))
                if mode == "nan" and actual_samples > 0:
                    ts[mid] = np.nan
                elif mode == "inf" and actual_samples > 0:
                    ts[mid] = np.inf
                elif mode in ("non_monotonic", "backward") and actual_samples >= 2:
                    idx = max(1, mid)
                    ts[idx] = ts[idx - 1] - (1.0 / float(rate_hz))
                elif mode == "duplicate" and actual_samples >= 2:
                    idx = max(1, mid)
                    ts[idx] = ts[idx - 1]
                else:
                    raise ValueError(f"Unsupported bad_timestamps mode: {bad_timestamps!r}")
            else:
                ts = np.asarray(bad_timestamps, dtype=np.float64)
        ts_ds = series_grp.create_dataset("timestamps", data=ts)
        ts_ds.attrs["unit"] = "seconds"
        ts_ds.attrs["interval"] = 1
    else:
        st_ds = series_grp.create_dataset("starting_time", data=np.float64(starting_time))
        st_ds.attrs["rate"] = float(rate_hz)
        st_ds.attrs["unit"] = "seconds"

    if electrodes_group is not None:
        elec_count = len(electrodes_group["id"]) if "id" in electrodes_group else actual_channels
        region_len = min(actual_channels, elec_count)
        reg_ds = series_grp.create_dataset(
            "electrodes",
            data=np.arange(region_len, dtype=np.int64),
        )
        reg_ds.attrs["neurodata_type"] = "DynamicTableRegion"
        reg_ds.attrs["namespace"] = "core"
        reg_ds.attrs["object_id"] = str(uuid.uuid4())
        reg_ds.attrs["description"] = "recorded electrodes"
        reg_ds.attrs["table"] = electrodes_group.ref


def make_synthetic_nwb(
    path: Union[str, Path],
    num_samples: int = 1000,
    num_channels: int = 4,
    rate_hz: float = 10000.0,
    starting_time: float = 0.0,
    explicit_timestamps: bool = False,
    conversion: float = 1e-6,
    channel_conversion: Sequence[float] | None = None,
    offset: float = 0.0,
    dtype: str = "int16",
    spike_times_per_unit: Sequence[Sequence[float]] | None = None,
    include_units: bool = True,
    include_electrodes: bool = True,
    extra_series: Sequence[str] | Mapping[str, Mapping[str, Any]] | None = None,
    oned: bool = False,
    bad_timestamps: Any = None,
    nan_impedance: bool = False,
    missing_electrode_cols: Sequence[str] | None = None,
    signal_data: Any = None,
    series_name: str = "ElectricalSeries",
) -> Path:
    """Create a synthetic NWB 2.x HDF5 file using only h5py + numpy."""
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    utf8_str_dt = h5py.string_dtype(encoding="utf-8")
    now_iso = "2026-01-01T00:00:00+00:00"
    effective_channels = 1 if oned else int(num_channels)
    if signal_data is not None:
        sig_arr = np.asarray(signal_data)
        if sig_arr.ndim == 1:
            effective_channels = 1
        elif sig_arr.ndim >= 2:
            effective_channels = 1 if oned else sig_arr.shape[1]

    with h5py.File(str(out_path), "w") as f:
        # Root NWBFile attributes
        f.attrs["nwb_version"] = "2.6.0"
        f.attrs["neurodata_type"] = "NWBFile"
        f.attrs["namespace"] = "core"
        f.attrs["object_id"] = str(uuid.uuid4())
        f.attrs["specifications"] = "core"

        # Root metadata datasets
        f.create_dataset("identifier", data=f"wetlang-syn-{uuid.uuid4().hex[:12]}", dtype=utf8_str_dt)
        f.create_dataset(
            "session_description",
            data="Synthetic electrophysiology recording for WetLang v2.2 E2E tests",
            dtype=utf8_str_dt,
        )
        f.create_dataset("session_start_time", data=now_iso, dtype=utf8_str_dt)
        f.create_dataset("timestamps_reference_time", data=now_iso, dtype=utf8_str_dt)
        f.create_dataset("file_create_date", data=np.array([now_iso], dtype=object), dtype=utf8_str_dt)

        # Standard top-level NWB groups
        acq_grp = f.create_group("acquisition")
        f.create_group("analysis")
        general_grp = f.create_group("general")
        f.create_group("processing")
        stim_grp = f.create_group("stimulus")
        stim_grp.create_group("presentation")
        stim_grp.create_group("templates")

        # Electrodes & device hierarchy
        electrodes_grp: h5py.Group | None = None
        if include_electrodes:
            devices_grp = general_grp.create_group("devices")
            mea_dev = devices_grp.create_group("mea_device")
            mea_dev.attrs["neurodata_type"] = "Device"
            mea_dev.attrs["namespace"] = "core"
            mea_dev.attrs["object_id"] = str(uuid.uuid4())
            mea_dev.attrs["description"] = "Synthetic 2D MEA device"

            ephys_grp = general_grp.create_group("extracellular_ephys")
            shank0 = ephys_grp.create_group("shank0")
            shank0.attrs["neurodata_type"] = "ElectrodeGroup"
            shank0.attrs["namespace"] = "core"
            shank0.attrs["object_id"] = str(uuid.uuid4())
            shank0.attrs["description"] = "Synthetic MEA shank 0"
            shank0.attrs["location"] = "organoid_surface"
            shank0["device"] = h5py.SoftLink("/general/devices/mea_device")

            electrodes_grp = ephys_grp.create_group("electrodes")
            electrodes_grp.attrs["neurodata_type"] = "DynamicTable"
            electrodes_grp.attrs["namespace"] = "core"
            electrodes_grp.attrs["object_id"] = str(uuid.uuid4())
            electrodes_grp.attrs["description"] = "MEA electrode table"

            id_ds = electrodes_grp.create_dataset(
                "id",
                data=np.arange(effective_channels, dtype=np.int64),
            )
            id_ds.attrs["neurodata_type"] = "ElementIdentifiers"
            id_ds.attrs["namespace"] = "core"
            id_ds.attrs["object_id"] = str(uuid.uuid4())

            missing_cols = set(missing_electrode_cols or ())
            col_specs: list[tuple[str, Any, Any, str]] = [
                ("x", np.arange(effective_channels, dtype=np.float64) * 50.0, None, "x coordinate (um)"),
                ("y", np.zeros(effective_channels, dtype=np.float64), None, "y coordinate (um)"),
                ("z", np.zeros(effective_channels, dtype=np.float64), None, "z coordinate (um)"),
                (
                    "imp",
                    np.full(
                        effective_channels,
                        np.nan if nan_impedance else 100000.0,
                        dtype=np.float64,
                    ),
                    None,
                    "electrode impedance (Ohm)",
                ),
                (
                    "location",
                    np.array(["organoid_cortex"] * effective_channels, dtype=object),
                    utf8_str_dt,
                    "electrode anatomical location",
                ),
                (
                    "filtering",
                    np.array(["300-3000 Hz"] * effective_channels, dtype=object),
                    utf8_str_dt,
                    "hardware filter description",
                ),
                (
                    "group",
                    np.array([shank0.ref] * effective_channels, dtype=h5py.ref_dtype),
                    h5py.ref_dtype,
                    "electrode group object reference",
                ),
                (
                    "group_name",
                    np.array(["shank0"] * effective_channels, dtype=object),
                    utf8_str_dt,
                    "electrode group name",
                ),
            ]
            kept_colnames: list[str] = []
            for cname, cdata, cdtype, cdesc in col_specs:
                if cname in missing_cols:
                    continue
                if cdtype is not None:
                    cds = electrodes_grp.create_dataset(cname, data=cdata, dtype=cdtype)
                else:
                    cds = electrodes_grp.create_dataset(cname, data=cdata)
                cds.attrs["neurodata_type"] = "VectorData"
                cds.attrs["namespace"] = "core"
                cds.attrs["object_id"] = str(uuid.uuid4())
                cds.attrs["description"] = cdesc
                kept_colnames.append(cname)
            electrodes_grp.attrs["colnames"] = np.array(kept_colnames, dtype=object).astype(utf8_str_dt)

        # Primary ElectricalSeries
        _write_electrical_series(
            acq_grp,
            series_name,
            num_samples=num_samples,
            num_channels=num_channels,
            rate_hz=rate_hz,
            starting_time=starting_time,
            explicit_timestamps=explicit_timestamps,
            conversion=conversion,
            channel_conversion=channel_conversion,
            offset=offset,
            dtype=dtype,
            oned=oned,
            bad_timestamps=bad_timestamps,
            signal_data=signal_data,
            electrodes_group=electrodes_grp,
        )

        # Optional extra ElectricalSeries
        if extra_series is not None:
            if isinstance(extra_series, Mapping):
                items = list(extra_series.items())
            else:
                items = [(str(name), {}) for name in extra_series]
            for extra_name, overrides in items:
                if extra_name == series_name:
                    continue
                _write_electrical_series(
                    acq_grp,
                    extra_name,
                    num_samples=int(overrides.get("num_samples", num_samples)),
                    num_channels=int(overrides.get("num_channels", num_channels)),
                    rate_hz=float(overrides.get("rate_hz", rate_hz)),
                    starting_time=float(overrides.get("starting_time", starting_time)),
                    explicit_timestamps=bool(overrides.get("explicit_timestamps", explicit_timestamps)),
                    conversion=float(overrides.get("conversion", conversion)),
                    channel_conversion=overrides.get("channel_conversion", None),
                    offset=float(overrides.get("offset", offset)),
                    dtype=str(overrides.get("dtype", dtype)),
                    oned=bool(overrides.get("oned", oned)),
                    bad_timestamps=overrides.get("bad_timestamps", None),
                    signal_data=overrides.get("signal_data", None),
                    electrodes_group=electrodes_grp,
                )

        # /units ragged spike_times table
        if include_units:
            if spike_times_per_unit is None:
                duration_s = max(float(num_samples) / float(rate_hz), 1e-4)
                units_list: list[list[float]] = [
                    [starting_time + 0.1 * duration_s, starting_time + 0.5 * duration_s],
                    [starting_time + 0.25 * duration_s],
                ]
            else:
                units_list = [list(u) for u in spike_times_per_unit]

            units_grp = f.create_group("units")
            units_grp.attrs["neurodata_type"] = "Units"
            units_grp.attrs["namespace"] = "core"
            units_grp.attrs["object_id"] = str(uuid.uuid4())
            units_grp.attrs["description"] = "Synthetic spike sorted units"
            units_grp.attrs["colnames"] = np.array(["spike_times"], dtype=object).astype(utf8_str_dt)

            flat_spikes: list[float] = []
            excl_indices: list[int] = []
            for unit_spikes in units_list:
                flat_spikes.extend(float(t) for t in unit_spikes)
                excl_indices.append(len(flat_spikes))

            u_id_ds = units_grp.create_dataset(
                "id",
                data=np.arange(len(units_list), dtype=np.int64),
            )
            u_id_ds.attrs["neurodata_type"] = "ElementIdentifiers"
            u_id_ds.attrs["namespace"] = "core"
            u_id_ds.attrs["object_id"] = str(uuid.uuid4())

            st_ds = units_grp.create_dataset(
                "spike_times",
                data=np.asarray(flat_spikes, dtype=np.float64),
            )
            st_ds.attrs["neurodata_type"] = "VectorData"
            st_ds.attrs["namespace"] = "core"
            st_ds.attrs["object_id"] = str(uuid.uuid4())
            st_ds.attrs["description"] = "spike times for each unit (s)"

            sti_ds = units_grp.create_dataset(
                "spike_times_index",
                data=np.asarray(excl_indices, dtype=np.uint64),
            )
            sti_ds.attrs["neurodata_type"] = "VectorIndex"
            sti_ds.attrs["namespace"] = "core"
            sti_ds.attrs["object_id"] = str(uuid.uuid4())
            sti_ds.attrs["target"] = st_ds.ref

    return out_path


def validate_nwb_hdf5_schema(path: Union[str, Path]) -> dict[str, Any]:
    """Validate an NWB 2.x HDF5 file via h5py and (when installed) pynwb.NWBHDF5IO."""
    nwb_path = Path(path)
    errors: list[str] = []
    root_metadata: dict[str, Any] = {}
    nwb_version: str | None = None
    identifier: str | None = None
    acquisition_series: list[str] = []
    has_electrodes = False
    electrode_count = 0
    has_units = False
    unit_count = 0
    stimulus_presentations: list[str] = []
    pynwb_validated = False

    if not nwb_path.is_file():
        return {
            "valid": False,
            "nwb_version": None,
            "identifier": None,
            "root_metadata": {},
            "acquisition_series": [],
            "has_electrodes": False,
            "electrode_count": 0,
            "has_units": False,
            "unit_count": 0,
            "stimulus_presentations": [],
            "pynwb_validated": False,
            "errors": [f"NWB file not found: {nwb_path}"],
        }

    with h5py.File(str(nwb_path), "r") as f:
        # 1. Root attributes
        raw_ver = f.attrs.get("nwb_version")
        if raw_ver is None:
            errors.append("missing root attribute 'nwb_version'")
        else:
            nwb_version = _decode_h5_str(raw_ver)
            if not nwb_version:
                errors.append("empty root attribute 'nwb_version'")

        ndt = f.attrs.get("neurodata_type")
        if ndt is None or _decode_h5_str(ndt) != "NWBFile":
            errors.append(f"invalid or missing root attribute 'neurodata_type': {ndt!r}")

        ns = f.attrs.get("namespace")
        if ns is None or _decode_h5_str(ns) != "core":
            errors.append(f"invalid or missing root attribute 'namespace': {ns!r}")

        obj_id = f.attrs.get("object_id")
        if obj_id is None or not _decode_h5_str(obj_id):
            errors.append("missing or empty root attribute 'object_id'")

        # 2. Root metadata datasets/attributes
        for key in (
            "identifier",
            "session_description",
            "session_start_time",
            "timestamps_reference_time",
            "file_create_date",
        ):
            raw_val: Any = None
            if key in f:
                raw_val = f[key][()]
            elif key in f.attrs:
                raw_val = f.attrs[key]
            else:
                errors.append(f"missing root metadata '{key}'")
                continue

            if key == "file_create_date":
                if isinstance(raw_val, np.ndarray):
                    dates = [_decode_h5_str(x) for x in raw_val.flat]
                elif isinstance(raw_val, (list, tuple)):
                    dates = [_decode_h5_str(x) for x in raw_val]
                else:
                    dates = [_decode_h5_str(raw_val)]
                if not dates or not dates[0]:
                    errors.append("empty 'file_create_date'")
                else:
                    for d_str in dates:
                        try:
                            datetime.fromisoformat(d_str.replace("Z", "+00:00"))
                        except ValueError as exc:
                            errors.append(f"invalid ISO-8601 in 'file_create_date': {d_str!r} ({exc})")
                root_metadata[key] = dates
            else:
                s_val = _decode_h5_str(raw_val)
                root_metadata[key] = s_val
                if not s_val:
                    errors.append(f"empty root metadata '{key}'")
                elif key in ("session_start_time", "timestamps_reference_time"):
                    try:
                        dt = datetime.fromisoformat(s_val.replace("Z", "+00:00"))
                        if dt.tzinfo is None:
                            errors.append(f"'{key}' must be timezone-aware ISO-8601, got {s_val!r}")
                    except ValueError as exc:
                        errors.append(f"invalid ISO-8601 in '{key}': {s_val!r} ({exc})")

        identifier = root_metadata.get("identifier")

        # 3. /acquisition
        if "acquisition" not in f or not isinstance(f["acquisition"], h5py.Group):
            errors.append("missing '/acquisition' group")
        else:
            acq = f["acquisition"]
            acquisition_series = sorted(list(acq.keys()))
            if not acquisition_series:
                errors.append("'/acquisition' contains no series")
            for sname in acquisition_series:
                sgrp = acq[sname]
                if not isinstance(sgrp, h5py.Group):
                    errors.append(f"/acquisition/{sname} is not an HDF5 group")
                    continue
                if "data" not in sgrp or not isinstance(sgrp["data"], h5py.Dataset):
                    errors.append(f"/acquisition/{sname} missing 'data' dataset")
                    continue
                data_ds = sgrp["data"]
                conv = data_ds.attrs.get("conversion")
                offs = data_ds.attrs.get("offset")
                if conv is None or not np.isfinite(float(conv)):
                    errors.append(f"/acquisition/{sname}/data missing finite 'conversion' attr")
                if offs is None or not np.isfinite(float(offs)):
                    errors.append(f"/acquisition/{sname}/data missing finite 'offset' attr")

                has_st = "starting_time" in sgrp
                has_ts = "timestamps" in sgrp
                if not has_st and not has_ts:
                    errors.append(f"/acquisition/{sname} missing both 'starting_time' and 'timestamps'")
                if has_st:
                    st_ds = sgrp["starting_time"]
                    rate = st_ds.attrs.get("rate")
                    if rate is None or not np.isfinite(float(rate)) or float(rate) <= 0.0:
                        errors.append(f"/acquisition/{sname}/starting_time missing valid positive 'rate' attr")
                if has_ts:
                    ts = np.asarray(sgrp["timestamps"][()], dtype=np.float64)
                    if ts.ndim != 1 or ts.shape[0] != data_ds.shape[0]:
                        errors.append(
                            f"/acquisition/{sname}/timestamps shape {ts.shape} != data len {data_ds.shape[0]}"
                        )
                    elif not np.all(np.isfinite(ts)):
                        errors.append(f"/acquisition/{sname}/timestamps contains non-finite values")
                    elif ts.shape[0] >= 2 and not np.all(np.diff(ts) > 0.0):
                        errors.append(f"/acquisition/{sname}/timestamps is not strictly increasing")

        # 4. /general/extracellular_ephys/electrodes
        elec_path = "/general/extracellular_ephys/electrodes"
        if elec_path in f and isinstance(f[elec_path], h5py.Group):
            has_electrodes = True
            egrp = f[elec_path]
            if "id" not in egrp:
                errors.append(f"{elec_path} missing 'id' dataset")
            else:
                electrode_count = int(egrp["id"].shape[0])
            if "colnames" not in egrp.attrs:
                errors.append(f"{elec_path} missing 'colnames' attribute")
            else:
                colnames = [_decode_h5_str(c) for c in np.asarray(egrp.attrs["colnames"]).flat]
                for col in colnames:
                    if col not in egrp:
                        errors.append(f"{elec_path} listed column '{col}' in colnames but dataset missing")
                    elif egrp[col].shape[0] != electrode_count:
                        errors.append(
                            f"{elec_path}/{col} length {egrp[col].shape[0]} != id length {electrode_count}"
                        )
        else:
            errors.append(f"missing '{elec_path}' group")

        # 5. /units (optional, validate structure if present)
        if "units" in f and isinstance(f["units"], h5py.Group):
            has_units = True
            ugrp = f["units"]
            if "spike_times" not in ugrp or "spike_times_index" not in ugrp:
                errors.append("'/units' present but missing 'spike_times' or 'spike_times_index'")
            else:
                n_spikes = int(ugrp["spike_times"].shape[0])
                idx = np.asarray(ugrp["spike_times_index"][()], dtype=np.int64)
                if idx.ndim != 1:
                    errors.append("'/units/spike_times_index' must be 1D")
                else:
                    unit_count = int(idx.shape[0])
                    if idx.size > 0:
                        if idx[0] < 0 or np.any(idx > n_spikes):
                            errors.append("'/units/spike_times_index' out of bounds for 'spike_times'")
                        if idx.size >= 2 and np.any(np.diff(idx) < 0):
                            errors.append("'/units/spike_times_index' must be monotonic non-decreasing")

        # 6. /stimulus/presentation
        if "stimulus" not in f or "presentation" not in f["stimulus"]:
            errors.append("missing '/stimulus/presentation' group")
        elif not isinstance(f["stimulus/presentation"], h5py.Group):
            errors.append("'/stimulus/presentation' is not an HDF5 group")
        else:
            stimulus_presentations = sorted(list(f["stimulus/presentation"].keys()))

    # 7. Conditional pynwb validation
    # Guard against sys.modules["pynwb"] = None (or spec-less fakes) before find_spec("pynwb")
    pynwb_mod = sys.modules.get("pynwb", _SENTINEL)
    if pynwb_mod is not None:
        spec_ok = True if pynwb_mod is not _SENTINEL else (importlib.util.find_spec("pynwb") is not None)
        if spec_ok:
            import pynwb  # lazy optional import

            try:
                with pynwb.NWBHDF5IO(str(nwb_path), "r") as io:
                    nwbfile = io.read()
                    if not getattr(nwbfile, "identifier", None):
                        errors.append("pynwb.NWBHDF5IO: missing identifier")
                pynwb_validated = True
            except Exception as exc:  # pragma: no cover - depends on optional pynwb install
                errors.append(f"pynwb.NWBHDF5IO validation error: {exc}")

    return {
        "valid": len(errors) == 0,
        "nwb_version": nwb_version,
        "identifier": identifier,
        "root_metadata": root_metadata,
        "acquisition_series": acquisition_series,
        "has_electrodes": has_electrodes,
        "electrode_count": electrode_count,
        "has_units": has_units,
        "unit_count": unit_count,
        "stimulus_presentations": stimulus_presentations,
        "pynwb_validated": pynwb_validated,
        "errors": errors,
    }


# ---------------------------------------------------------------------------
# C99 Compiler Discovery & Standalone Compile/Run Helper
# ---------------------------------------------------------------------------


def _find_executable(name: str, extra_paths: Sequence[str] | None = None) -> str | None:
    found = shutil.which(name)
    if found:
        return found
    if extra_paths:
        suffix = ".exe" if sys.platform == "win32" else ""
        for p in extra_paths:
            candidate = Path(p) / f"{name}{suffix}"
            if candidate.is_file() and os.access(candidate, os.X_OK):
                return str(candidate)
    return None


def find_c99_compiler() -> tuple[str, str]:
    """Discover a working C99 compiler matching ``native/build.py`` priority."""
    cl_exe = _find_executable("cl")
    if cl_exe:
        return ("cl", cl_exe)

    clang_exe = _find_executable(
        "clang",
        [
            r"C:\Program Files\LLVM\bin",
            r"C:\LLVM\bin",
            r"C:\msys64\mingw64\bin",
            r"C:\msys64\ucrt64\bin",
        ],
    )
    if clang_exe:
        return ("clang", clang_exe)

    gcc_exe = _find_executable(
        "gcc",
        [
            r"C:\msys64\mingw64\bin",
            r"C:\msys64\ucrt64\bin",
            r"C:\mingw64\bin",
            r"C:\TDM-GCC-64\bin",
        ],
    )
    if gcc_exe:
        return ("gcc", gcc_exe)

    raise RuntimeError("No suitable C99 compiler found (cl, clang, or gcc).")


def compile_and_run_c99(
    c_source: str,
    tmp_dir: Path,
    link_wetvm: bool = True,
    extra_c_files: list[Path] | None = None,
    extra_libs: list[str] | None = None,
    timeout: int = 30,
) -> subprocess.CompletedProcess[str]:
    """Compile a standalone C99 test binary strictly inside ``tmp_dir`` and run it."""
    work_dir = Path(tmp_dir)
    work_dir.mkdir(parents=True, exist_ok=True)

    main_c = work_dir / "test_main.c"
    main_c.write_text(c_source, encoding="utf-8")
    sources = [main_c, *(Path(p) for p in (extra_c_files or []))]

    include_dir = PROJECT_ROOT / "native" / "include"
    bin_dir = PROJECT_ROOT / "native" / "bin"
    exe_path = work_dir / ("test_bin.exe" if sys.platform == "win32" else "test_bin")

    kind, compiler_exe = find_c99_compiler()
    cmd: list[str]

    if kind == "clang" and sys.platform == "win32":
        msvcrt_lib = bin_dir / "msvcrt.lib"
        kernel32_lib = bin_dir / "kernel32.lib"
        sync_lib = bin_dir / "synchronization.lib"
        sdkless = msvcrt_lib.is_file() and kernel32_lib.is_file()

        cmd = [
            compiler_exe,
            "-std=c99",
            "-Wall",
            "-Wextra",
            *(["-mno-stack-arg-probe"] if sdkless else []),
            f"-I{include_dir}",
            *[str(s) for s in sources],
        ]
        if link_wetvm:
            wetvm_lib = bin_dir / "wetvm.lib"
            if not wetvm_lib.is_file():
                raise FileNotFoundError(f"Expected import library not found: {wetvm_lib}")
            cmd.append(str(wetvm_lib))

        for lib in extra_libs or []:
            lib_name = lib if lib.endswith(".lib") else f"{lib}.lib"
            candidate = bin_dir / lib_name
            if candidate.is_file():
                cmd.append(str(candidate))
            elif sdkless:
                cmd.append(lib_name)
            else:
                cmd.append(f"-l{lib}")

        if sdkless:
            # Build a tmp_dir-local _fltused static archive so float code links under
            # -nostdlib without colliding when a test source defines _fltused itself.
            flt_c = work_dir / "_wet_fltused.c"
            flt_o = work_dir / "_wet_fltused.o"
            flt_lib = work_dir / "fltused.lib"
            flt_c.write_text("int _fltused = 0x9875;\n", encoding="utf-8")
            obj_res = subprocess.run(
                [compiler_exe, "-c", "-std=c99", "-mno-stack-arg-probe", str(flt_c), "-o", str(flt_o)],
                cwd=str(work_dir),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
            )
            if obj_res.returncode != 0:
                raise RuntimeError(f"Failed compiling _fltused stub: {obj_res.stderr}")

            llvm_ar = _find_executable("llvm-ar", [str(Path(compiler_exe).parent)])
            flt_link_arg: str | None = None
            if llvm_ar:
                if flt_lib.exists():
                    flt_lib.unlink()
                ar_res = subprocess.run(
                    [llvm_ar, "rcs", str(flt_lib), str(flt_o)],
                    cwd=str(work_dir),
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=timeout,
                )
                if ar_res.returncode == 0 and flt_lib.is_file():
                    flt_link_arg = str(flt_lib)
            if flt_link_arg is None:
                all_src_text = "\n".join(s.read_text(encoding="utf-8", errors="replace") for s in sources)
                if "_fltused" not in all_src_text:
                    flt_link_arg = str(flt_o)

            cmd.extend([str(msvcrt_lib), str(kernel32_lib)])
            if sync_lib.is_file():
                cmd.append(str(sync_lib))
            if flt_link_arg is not None:
                cmd.append(flt_link_arg)
            cmd.extend(["-nostdlib", "-Xlinker", "/entry:main"])

        cmd.extend(["-o", str(exe_path)])

    elif kind in ("clang", "gcc"):
        cmd = [
            compiler_exe,
            "-std=c99",
            "-Wall",
            "-Wextra",
            f"-I{include_dir}",
            *[str(s) for s in sources],
        ]
        if link_wetvm:
            if sys.platform == "win32":
                wetvm_lib = bin_dir / "wetvm.lib"
                wetvm_dll = bin_dir / "wetvm.dll"
                if wetvm_lib.is_file():
                    cmd.append(str(wetvm_lib))
                elif wetvm_dll.is_file():
                    cmd.append(str(wetvm_dll))
                else:
                    raise FileNotFoundError(f"wetvm library not found in {bin_dir}")
            else:
                ext = ".dylib" if sys.platform == "darwin" else ".so"
                wetvm_shared = bin_dir / f"wetvm{ext}"
                if not wetvm_shared.is_file():
                    alt_shared = PROJECT_ROOT / "native" / f"wetvm{ext}"
                    if alt_shared.is_file():
                        wetvm_shared = alt_shared
                    else:
                        raise FileNotFoundError(f"wetvm shared library not found: {wetvm_shared}")
                cmd.extend([str(wetvm_shared), f"-Wl,-rpath,{wetvm_shared.parent}"])

        extra = list(extra_libs or [])
        for lib in extra:
            cmd.append(f"-l{lib}")
        if sys.platform != "win32":
            if "m" not in extra:
                cmd.append("-lm")
            if "pthread" not in extra:
                cmd.append("-lpthread")
        cmd.extend(["-o", str(exe_path)])

    else:  # MSVC cl.exe
        cmd = [
            compiler_exe,
            "/nologo",
            "/TC",
            "/W3",
            f"/I{include_dir}",
            *[str(s) for s in sources],
        ]
        if link_wetvm:
            wetvm_lib = bin_dir / "wetvm.lib"
            if not wetvm_lib.is_file():
                raise FileNotFoundError(f"Expected import library not found: {wetvm_lib}")
            cmd.append(str(wetvm_lib))
        for lib in extra_libs or []:
            cmd.append(lib if lib.endswith(".lib") else f"{lib}.lib")
        cmd.extend([f"/Fo{work_dir}{os.sep}", f"/Fe:{exe_path}"])

    comp_res = subprocess.run(
        cmd,
        cwd=str(work_dir),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    if comp_res.returncode != 0:
        raise RuntimeError(
            f"C99 compilation failed (rc={comp_res.returncode})\n"
            f"CMD: {' '.join(cmd)}\n"
            f"STDOUT:\n{comp_res.stdout}\n"
            f"STDERR:\n{comp_res.stderr}"
        )

    run_env = os.environ.copy()
    bin_str = str(bin_dir)
    if sys.platform == "win32":
        run_env["PATH"] = f"{bin_str}{os.pathsep}{run_env.get('PATH', '')}"
    elif sys.platform == "darwin":
        run_env["DYLD_LIBRARY_PATH"] = f"{bin_str}{os.pathsep}{run_env.get('DYLD_LIBRARY_PATH', '')}"
    else:
        run_env["LD_LIBRARY_PATH"] = f"{bin_str}{os.pathsep}{run_env.get('LD_LIBRARY_PATH', '')}"

    return subprocess.run(
        [str(exe_path)],
        cwd=str(work_dir),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        env=run_env,
    )


# ---------------------------------------------------------------------------
# Fake pylsl Module Factory
# ---------------------------------------------------------------------------


def make_fake_pylsl_module(raise_on_init: Exception | None = None) -> types.ModuleType:
    """Create a deterministic in-memory ``pylsl`` test double module."""
    mod = types.ModuleType("pylsl")

    mod.cf_undefined = 0
    mod.cf_float32 = 1
    mod.cf_double64 = 2
    mod.cf_string = 3
    mod.cf_int32 = 4
    mod.cf_int16 = 5
    mod.cf_int8 = 6
    mod.cf_int64 = 7
    mod.FOREVER = 32000000.0
    mod.IRREGULAR_RATE = 0.0

    lock = threading.Lock()
    buffers: dict[tuple[str, str, str], deque[tuple[list[Any], float]]] = {}
    registered_infos: list[Any] = []

    def _stream_key(info: Any) -> tuple[str, str, str]:
        return (info.name(), info.type(), info.source_id())

    class _FakeDesc:
        def __init__(self) -> None:
            self._children: dict[str, Any] = {}

        def append_child(self, name: str) -> "_FakeDesc":
            child = _FakeDesc()
            self._children[name] = child
            return child

        def append_child_value(self, name: str, value: str) -> "_FakeDesc":
            self._children[name] = str(value)
            return self

    class StreamInfo:
        def __init__(
            self,
            name: str = "WetLang",
            type: str = "EEG",  # noqa: A002 - matches pylsl signature
            channel_count: int = 1,
            nominal_srate: float = 0.0,
            channel_format: int = 1,
            source_id: str = "",
        ) -> None:
            if raise_on_init is not None:
                raise raise_on_init
            self._name = str(name)
            self._type = str(type)
            self._channel_count = int(channel_count)
            self._nominal_srate = float(nominal_srate)
            self._channel_format = int(channel_format)
            self._source_id = str(source_id)
            self._desc = _FakeDesc()

        def name(self) -> str:
            return self._name

        def type(self) -> str:
            return self._type

        def channel_count(self) -> int:
            return self._channel_count

        def nominal_srate(self) -> float:
            return self._nominal_srate

        def channel_format(self) -> int:
            return self._channel_format

        def source_id(self) -> str:
            return self._source_id

        def desc(self) -> _FakeDesc:
            return self._desc

        def as_xml(self) -> str:
            return (
                f"<info><name>{self._name}</name><type>{self._type}</type>"
                f"<channel_count>{self._channel_count}</channel_count></info>"
            )

    class StreamOutlet:
        def __init__(
            self,
            info: StreamInfo,
            chunk_size: int = 0,
            max_buffered: int = 360,
        ) -> None:
            if raise_on_init is not None:
                raise raise_on_init
            self._info = info
            self._chunk_size = int(chunk_size)
            self._max_buffered = int(max_buffered)
            key = _stream_key(info)
            with lock:
                buffers.setdefault(key, deque())
                if info not in registered_infos:
                    registered_infos.append(info)

        def info(self) -> StreamInfo:
            return self._info

        def push_sample(self, x: Sequence[Any], timestamp: float = 0.0, pushthrough: bool = True) -> None:
            del pushthrough
            ts = float(timestamp) if timestamp else time.monotonic()
            sample = list(x) if isinstance(x, (list, tuple, np.ndarray)) else [x]
            key = _stream_key(self._info)
            with lock:
                buffers.setdefault(key, deque()).append((sample, ts))

        def push_chunk(
            self,
            x: Sequence[Any],
            timestamp: Union[float, Sequence[float]] = 0.0,
            pushthrough: bool = True,
        ) -> None:
            del pushthrough
            key = _stream_key(self._info)
            rows: list[list[Any]] = []
            if isinstance(x, np.ndarray):
                arr = np.atleast_2d(x) if x.ndim <= 1 else x
                if x.ndim == 1 and self._info.channel_count() == 1:
                    rows = [[val] for val in x.tolist()]
                else:
                    rows = [row.tolist() for row in arr]
            else:
                for item in x:
                    if isinstance(item, (list, tuple, np.ndarray)):
                        rows.append(list(item))
                    else:
                        rows.append([item])
            if isinstance(timestamp, (list, tuple, np.ndarray)):
                ts_seq = [float(t) for t in timestamp]
            else:
                base_ts = float(timestamp) if timestamp else time.monotonic()
                ts_seq = [base_ts] * len(rows)
            with lock:
                q = buffers.setdefault(key, deque())
                for idx, row in enumerate(rows):
                    ts_val = ts_seq[idx] if idx < len(ts_seq) else (ts_seq[-1] if ts_seq else time.monotonic())
                    q.append((row, ts_val))

        def have_consumers(self) -> bool:
            return True

        def wait_for_consumers(self, timeout: float) -> bool:
            del timeout
            return True

    class StreamInlet:
        def __init__(
            self,
            info: StreamInfo,
            max_buflen: int = 360,
            max_chunklen: int = 0,
            recover: bool = True,
        ) -> None:
            if raise_on_init is not None:
                raise raise_on_init
            self._info = info
            self._max_buflen = int(max_buflen)
            self._max_chunklen = int(max_chunklen)
            self._recover = bool(recover)
            self._opened = True

        def info(self, timeout: float = 32000000.0) -> StreamInfo:
            del timeout
            return self._info

        def open_stream(self, timeout: float = 32000000.0) -> None:
            del timeout
            self._opened = True

        def close_stream(self) -> None:
            self._opened = False

        def time_correction(self, timeout: float = 32000000.0) -> float:
            del timeout
            return 0.0

        def samples_available(self) -> int:
            key = _stream_key(self._info)
            with lock:
                return len(buffers.get(key, ()))

        def flush(self) -> int:
            key = _stream_key(self._info)
            with lock:
                q = buffers.get(key)
                if not q:
                    return 0
                count = len(q)
                q.clear()
                return count

        def pull_sample(
            self,
            timeout: float = 32000000.0,
            dest_obj: Any = None,
        ) -> tuple[list[Any] | None, float | None]:
            del timeout, dest_obj
            key = _stream_key(self._info)
            with lock:
                q = buffers.get(key)
                if not q:
                    return (None, None)
                sample, ts = q.popleft()
                return (list(sample), float(ts))

        def pull_chunk(
            self,
            timeout: float = 0.0,
            max_samples: int = 1024,
            dest_obj: Any = None,
        ) -> tuple[list[list[Any]], list[float]]:
            del timeout, dest_obj
            key = _stream_key(self._info)
            samples: list[list[Any]] = []
            timestamps: list[float] = []
            with lock:
                q = buffers.get(key)
                if not q:
                    return (samples, timestamps)
                while q and len(samples) < max_samples:
                    sample, ts = q.popleft()
                    samples.append(list(sample))
                    timestamps.append(float(ts))
            return (samples, timestamps)

    def resolve_byprop(
        prop: str,
        value: str,
        minimum: int = 1,
        timeout: float = 32000000.0,
    ) -> list[StreamInfo]:
        del minimum, timeout
        if raise_on_init is not None:
            raise raise_on_init
        with lock:
            matches: list[StreamInfo] = []
            for info in registered_infos:
                attr = getattr(info, prop, None)
                actual = attr() if callable(attr) else attr
                if actual == value:
                    matches.append(info)
            return matches

    def resolve_streams(wait_time: float = 1.0) -> list[StreamInfo]:
        del wait_time
        if raise_on_init is not None:
            raise raise_on_init
        with lock:
            return list(registered_infos)

    def resolve_stream(*args: Any, **kwargs: Any) -> list[StreamInfo]:
        if raise_on_init is not None:
            raise raise_on_init
        if len(args) >= 2:
            return resolve_byprop(str(args[0]), str(args[1]))
        if "prop" in kwargs and "value" in kwargs:
            return resolve_byprop(str(kwargs["prop"]), str(kwargs["value"]))
        return resolve_streams()

    def local_clock() -> float:
        return time.monotonic()

    mod.StreamInfo = StreamInfo
    mod.StreamOutlet = StreamOutlet
    mod.StreamInlet = StreamInlet
    mod.resolve_byprop = resolve_byprop
    mod.resolve_streams = resolve_streams
    mod.resolve_stream = resolve_stream
    mod.local_clock = local_clock
    mod._buffers = buffers
    mod._registered_infos = registered_infos
    return mod


# ---------------------------------------------------------------------------
# Ephemeral Local HTTP Server for NWB Download / SHA-256 Tests
# ---------------------------------------------------------------------------


@contextmanager
def serve_nwb_over_http(file_path: Union[str, Path]) -> Iterator[tuple[str, ThreadingHTTPServer]]:
    """Serve ``file_path`` over ``127.0.0.1:0`` and yield ``(url, server)``."""
    target = Path(file_path)
    payload = target.read_bytes()
    sha256_hex = hashlib.sha256(payload).hexdigest()
    count_lock = threading.Lock()

    class _Handler(BaseHTTPRequestHandler):
        def _send_common_headers(self) -> None:
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("X-SHA256", sha256_hex)
            self.end_headers()

        def do_HEAD(self) -> None:  # noqa: N802
            with count_lock:
                self.server.request_count += 1  # type: ignore[attr-defined]
            self._send_common_headers()

        def do_GET(self) -> None:  # noqa: N802
            with count_lock:
                self.server.request_count += 1  # type: ignore[attr-defined]
            self._send_common_headers()
            self.wfile.write(payload)

        def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    server.sha256 = sha256_hex  # type: ignore[attr-defined]
    server.file_path = target  # type: ignore[attr-defined]
    server.request_count = 0  # type: ignore[attr-defined]

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        port = server.server_address[1]
        url = f"http://127.0.0.1:{port}/{target.name}"
        yield (url, server)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


# ---------------------------------------------------------------------------
# WetLang (.wet) Source Generator Helpers
# ---------------------------------------------------------------------------


def make_wet_source(
    *,
    grid_rows: int = 8,
    grid_cols: int = 8,
    organoid_name: str | None = None,
    organoid_radius: str | None = "150um",
    organoid_perfusion: str | None = "1.0uL/min",
    organoid_area: str | None = None,
    organoid_area_key: str = "area",
    channel_name: str = "ch0",
    channel_coords: tuple[int, int] = (0, 0),
    channel_mode: str | None = "BiphasicStim",
    channel_area: str | None = None,
    channel_area_key: str = "area",
    blanking_ms: str | None = None,
    blanking_args: str | None = None,
    stim_fn: str = "stim_biphasic",
    stim_amp: str = "0.5V",
    stim_p1: str = "200us",
    stim_p2: str = "200us",
    stim_interphase: str | None = None,
    include_stim: bool = True,
    include_sync_tick: bool = True,
    extra_decls: Sequence[str] | None = None,
    extra_body_lines: Sequence[str] | None = None,
) -> str:
    """Generate a parameterized ``.wet`` program for v2.2 E2E tests."""
    lines: list[str] = [f"grid mea[{grid_rows}, {grid_cols}];"]

    if organoid_name:
        lines.append(f"organoid {organoid_name} {{")
        if organoid_radius is not None:
            lines.append(f"    radius: {organoid_radius};")
        if organoid_perfusion is not None:
            lines.append(f"    perfusion: {organoid_perfusion};")
        if organoid_area is not None:
            lines.append(f"    {organoid_area_key}: {organoid_area};")
        lines.append("}")

    r, c = channel_coords
    ch_parts = [f"channel {channel_name} = mea[{r}, {c}]"]
    if channel_mode is not None:
        ch_parts.append(f"mode: {channel_mode}")
    if channel_area is not None:
        ch_parts.append(f"{channel_area_key}: {channel_area}")
    lines.append(" ".join(ch_parts) + ";")

    if extra_decls:
        lines.extend(extra_decls)

    lines.append("")
    lines.append("fn main() -> int {")

    if blanking_args is not None:
        lines.append(f"    set_blanking({blanking_args});")
    elif blanking_ms is not None:
        lines.append(f"    set_blanking({blanking_ms});")

    if include_stim:
        stim_args = [channel_name, stim_amp, stim_p1, stim_p2]
        if stim_interphase is not None:
            stim_args.append(stim_interphase)
        lines.append(f"    {stim_fn}({', '.join(stim_args)});")

    if extra_body_lines:
        for body_line in extra_body_lines:
            lines.append(f"    {body_line}")

    if include_sync_tick:
        lines.append("    sync_tick();")

    lines.append("    return 0;")
    lines.append("}")
    return "\n".join(lines) + "\n"
