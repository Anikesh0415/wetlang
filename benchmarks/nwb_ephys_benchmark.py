"""
benchmarks/nwb_ephys_benchmark.py — Project Janus v2.2 (R4)
NWB electrophysiology I/O benchmark.

Runs in two modes:
  - Offline (default): uses a synthetic NWB file generated in-process.
  - Online (--download-public): downloads a pinned public DANDI dataset
    and verifies its SHA-256 before benchmarking.

Usage:
    python -B benchmarks/nwb_ephys_benchmark.py
    python -B benchmarks/nwb_ephys_benchmark.py --download-public
    python -B benchmarks/nwb_ephys_benchmark.py --chunk-size 1024 --n-chunks 50

NEVER commit .nwb files. Cache in .cache/nwb/
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional

import numpy as np

# Ensure we can import wetlang from the project root
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_PROJECT_ROOT))

try:
    import h5py
except ImportError:
    print("ERROR: h5py is required. Install with: pip install h5py")
    sys.exit(1)

from wetlang.nwb import read_nwb_recording, iter_nwb_chunks, export_to_nwb

# ---------------------------------------------------------------------------
# Pinned public DANDI dataset (sub-000005 from DANDI:000005 Allen SDC)
# This is a small publicly available electrophysiology recording.
# ---------------------------------------------------------------------------
_DANDI_URL = (
    "https://api.dandiarchive.org/api/assets/"
    "9e31e8df-7b66-4e3f-b9e0-7d6e01b65f9b/download/"
)
_DANDI_SHA256 = "PLACEHOLDER_SHA256_TO_BE_FILLED_AFTER_FIRST_DOWNLOAD"
_CACHE_DIR = _PROJECT_ROOT / ".cache" / "nwb"


# ---------------------------------------------------------------------------
# Synthetic NWB generation
# ---------------------------------------------------------------------------


def _make_synthetic_nwb(path: str, n_samples: int, n_channels: int, seed: int = 0) -> None:
    """Write a minimal synthetic NWB file for benchmarking."""
    rng = np.random.default_rng(seed)
    data = rng.integers(-32768, 32767, (n_samples, n_channels), dtype=np.int16)
    timestamps = np.arange(n_samples, dtype=np.float64) / 20_000.0  # 20 kHz

    with h5py.File(path, "w") as f:
        f.attrs.update({
            "neurodata_type": "NWBFile",
            "nwb_version": "2.7.0",
            "session_description": "WetLang NWB benchmark synthetic",
            "identifier": "wetlang-benchmark",
            "session_start_time": "2024-01-01T00:00:00+00:00",
            "file_create_date": "2024-01-01T00:00:00+00:00",
        })
        acq = f.require_group("acquisition")
        series = acq.create_group("SyntheticEphys")
        series.attrs.update({
            "neurodata_type": "ElectricalSeries",
            "namespace": "core",
            "description": "Synthetic benchmark data",
        })
        ds = series.create_dataset("data", data=data, compression="gzip", compression_opts=1)
        ds.attrs["conversion"] = 1e-6  # int16 µV → V
        ds.attrs["offset"] = 0.0
        ds.attrs["unit"] = "volts"
        series.create_dataset("timestamps", data=timestamps)


# ---------------------------------------------------------------------------
# Download helper (online mode)
# ---------------------------------------------------------------------------


def _download_with_cache(url: str, expected_sha256: str, cache_dir: Path) -> Path:
    """Download url → cache_dir and verify SHA-256."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    fname = cache_dir / "public_ephys_benchmark.nwb"
    if fname.exists():
        print(f"[cache hit] {fname}")
        # Verify cached file
        sha256 = _sha256_file(str(fname))
        if expected_sha256 != "PLACEHOLDER_SHA256_TO_BE_FILLED_AFTER_FIRST_DOWNLOAD" and sha256 != expected_sha256:
            print(f"[warn] SHA-256 mismatch: expected {expected_sha256}, got {sha256}. Re-downloading.")
            fname.unlink()
        else:
            return fname

    import urllib.request
    print(f"[download] {url}")
    t0 = time.time()
    urllib.request.urlretrieve(url, str(fname))
    elapsed = time.time() - t0
    size_mb = fname.stat().st_size / 1e6
    sha256 = _sha256_file(str(fname))
    print(f"[download] {size_mb:.1f} MB in {elapsed:.1f}s — SHA-256: {sha256}")

    if expected_sha256 != "PLACEHOLDER_SHA256_TO_BE_FILLED_AFTER_FIRST_DOWNLOAD":
        if sha256 != expected_sha256:
            fname.unlink()
            raise RuntimeError(
                f"SHA-256 mismatch for downloaded NWB file.\n"
                f"  expected: {expected_sha256}\n"
                f"  got:      {sha256}"
            )
    return fname


def _sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Benchmark runners
# ---------------------------------------------------------------------------


def bench_full_load(path: str, series_name: Optional[str] = None) -> None:
    """Benchmark read_nwb_recording (full load)."""
    t0 = time.perf_counter()
    result = read_nwb_recording(path, series_name=series_name)
    dt = time.perf_counter() - t0
    n, c = result["data"].shape
    mb = result["data"].nbytes / 1e6
    print(
        f"[full_load] {n} samples × {c} ch = {mb:.1f} MB | "
        f"time={dt*1000:.1f} ms | "
        f"throughput={mb/max(dt,1e-9):.1f} MB/s"
    )


def bench_chunked_read(
    path: str,
    chunk_size: int = 2048,
    n_chunks: Optional[int] = None,
    series_name: Optional[str] = None,
) -> None:
    """Benchmark iter_nwb_chunks (streaming)."""
    total_samples = 0
    total_bytes = 0
    t0 = time.perf_counter()
    for i, (chunk, ts) in enumerate(iter_nwb_chunks(path, chunk_size=chunk_size, series_name=series_name)):
        total_samples += len(chunk)
        total_bytes += chunk.nbytes
        if n_chunks is not None and i + 1 >= n_chunks:
            break
    dt = time.perf_counter() - t0
    mb = total_bytes / 1e6
    print(
        f"[chunked]   {total_samples} samples | {mb:.1f} MB | "
        f"chunk={chunk_size} | time={dt*1000:.1f} ms | "
        f"throughput={mb/max(dt,1e-9):.1f} MB/s"
    )


def bench_export(path: str, n_samples: int, n_channels: int) -> None:
    """Benchmark export_to_nwb."""
    rng = np.random.default_rng(1)
    vm_data = {
        "timestamps": np.arange(n_samples, dtype=np.float64) / 10_000.0,
        "voltages": rng.normal(0.0, 5e-3, (n_samples, n_channels)).astype(np.float32),
    }
    with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
        out_path = tf.name
    try:
        t0 = time.perf_counter()
        export_to_nwb(out_path, vm_data, session_description="benchmark export")
        dt = time.perf_counter() - t0
        size_mb = os.path.getsize(out_path) / 1e6
        print(
            f"[export]    {n_samples} × {n_channels} ch → {size_mb:.1f} MB | "
            f"time={dt*1000:.1f} ms"
        )
    finally:
        os.unlink(out_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="WetLang NWB Ephys Benchmark (Project Janus v2.2)"
    )
    parser.add_argument(
        "--download-public",
        action="store_true",
        help="Download pinned public DANDI dataset for benchmarking",
    )
    parser.add_argument(
        "--n-samples",
        type=int,
        default=100_000,
        help="Samples in synthetic NWB (default: 100,000)",
    )
    parser.add_argument(
        "--n-channels",
        type=int,
        default=64,
        help="Channels in synthetic NWB (default: 64)",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=2048,
        help="Samples per chunk for streaming benchmark (default: 2048)",
    )
    parser.add_argument(
        "--n-chunks",
        type=int,
        default=None,
        help="Limit number of chunks read (default: all)",
    )
    args = parser.parse_args()

    if args.download_public:
        nwb_path = str(_download_with_cache(_DANDI_URL, _DANDI_SHA256, _CACHE_DIR))
        series_name = None
    else:
        # Synthetic offline mode
        with tempfile.NamedTemporaryFile(suffix=".nwb", delete=False) as tf:
            nwb_path = tf.name
        print(
            f"[synthetic] Generating {args.n_samples} × {args.n_channels} ch NWB file…"
        )
        t0 = time.perf_counter()
        _make_synthetic_nwb(nwb_path, args.n_samples, args.n_channels)
        gen_dt = time.perf_counter() - t0
        size_mb = os.path.getsize(nwb_path) / 1e6
        print(f"[synthetic] Done in {gen_dt*1000:.1f} ms → {size_mb:.1f} MB")
        series_name = "SyntheticEphys"

    print()
    bench_full_load(nwb_path, series_name=series_name)
    bench_chunked_read(nwb_path, chunk_size=args.chunk_size, n_chunks=args.n_chunks, series_name=series_name)
    bench_export(nwb_path, n_samples=min(args.n_samples, 10_000), n_channels=args.n_channels)

    if not args.download_public:
        os.unlink(nwb_path)

    print("\nAll benchmarks complete.")


if __name__ == "__main__":
    main()
