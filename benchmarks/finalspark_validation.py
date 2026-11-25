"""
FinalSpark fs369 Empirical Electrophysiological Validation Adapter
==================================================================
Ingests empirical biological recordings from FinalSpark neural organoid fs369:
Path: E:\\data\\fs369\\fs369data\\fs369_package.hdf5
Table: /fs369_wholelife_events/table (94.15M spike events)

Validates simulated WetLang organoid digital twin against empirical bounds:
1. Baseline spontaneous firing rate (0.5 - 25 Hz)
2. Inter-Spike Interval (ISI) distribution coefficient of variation (CV_ISI in [1.0, 8.0])
3. Burst fraction (percentage of spikes with ISI <= 50 ms in [0.20, 0.90])

CI / Cloud Fallback:
If drive E: is unmounted (in CI/Docker environments), gracefully falls back
to pre-computed empirical calibration constants without throwing exceptions.
"""

import sys
import os
import argparse
import time
from pathlib import Path
from typing import Dict, Any, Tuple, Optional

# Ensure root repository directory is in sys.path
_root = str(Path(__file__).resolve().parent.parent)
if _root not in sys.path:
    sys.path.insert(0, _root)

import numpy as np

# Cached empirical reference constants measured directly from fs369_package.hdf5 (94.15M spikes)
CACHED_EMPIRICAL_BOUNDS = {
    "dataset": "FinalSpark fs369 (Wholelife 94.15M Events)",
    "mean_firing_rate_hz": 3.87,
    "firing_rate_min_hz": 0.5,
    "firing_rate_max_hz": 25.0,
    "mean_cv_isi": 3.32,
    "cv_isi_min": 1.0,
    "cv_isi_max": 8.0,
    "mean_burst_fraction": 0.616,
    "burst_fraction_min": 0.20,
    "burst_fraction_max": 0.90,
}

DEFAULT_HDF5_PATH = Path(r"E:\data\fs369\fs369data\fs369_package.hdf5")


def load_empirical_metrics(
    hdf5_path: Path = DEFAULT_HDF5_PATH,
    sample_size: int = 50000,
) -> Tuple[Dict[str, float], bool]:
    """
    Ingests FinalSpark empirical recording from HDF5 file if available.
    Returns (metrics_dict, is_live_data).
    """
    if not hdf5_path.exists():
        return CACHED_EMPIRICAL_BOUNDS.copy(), False

    try:
        import h5py
        with h5py.File(hdf5_path, "r") as f:
            if "fs369_wholelife_events/table" not in f:
                return CACHED_EMPIRICAL_BOUNDS.copy(), False

            tbl = f["fs369_wholelife_events/table"]
            actual_sample = min(sample_size, len(tbl))
            data = tbl[:actual_sample]

        times_ns = data["time_of_event"]
        electrodes = data["electrode"]
        unique_elec = np.unique(electrodes)

        dur_s = (times_ns.max() - times_ns.min()) / 1e9
        if dur_s <= 0:
            dur_s = 1.0

        rates = []
        cv_isis = []
        burst_fractions = []

        for el in unique_elec:
            el_times = np.sort(times_ns[electrodes == el]) / 1e9
            if len(el_times) < 10:
                continue
            el_dur = el_times[-1] - el_times[0]
            if el_dur <= 0:
                continue

            rate = len(el_times) / el_dur
            isis = np.diff(el_times)
            if len(isis) > 0 and np.mean(isis) > 0:
                cv = np.std(isis) / np.mean(isis)
                # Burst criterion: inter-spike interval <= 50 ms
                bf = np.sum(isis <= 0.05) / len(isis)

                rates.append(rate)
                cv_isis.append(cv)
                burst_fractions.append(bf)

        metrics = {
            "dataset": f"Live FinalSpark fs369 ({actual_sample:,} events)",
            "mean_firing_rate_hz": float(np.mean(rates)) if rates else 3.87,
            "firing_rate_min_hz": 0.5,
            "firing_rate_max_hz": 25.0,
            "mean_cv_isi": float(np.mean(cv_isis)) if cv_isis else 3.32,
            "cv_isi_min": 1.0,
            "cv_isi_max": 8.0,
            "mean_burst_fraction": float(np.mean(burst_fractions)) if burst_fractions else 0.616,
            "burst_fraction_min": 0.20,
            "burst_fraction_max": 0.90,
            "active_electrodes": len(unique_elec),
            "duration_s": dur_s,
        }
        return metrics, True

    except Exception as e:
        print(f"[Notice] Failed to read HDF5 ({e}), falling back to cached reference.")
        return CACHED_EMPIRICAL_BOUNDS.copy(), False


def run_simulated_twin(
    steps: int = 30000,
    steps_per_action: int = 1,
    dt_ms: float = 0.1,
) -> Dict[str, float]:
    """Runs WetworldGymEnv tick-by-tick spontaneous activity to measure simulated electrophysiology."""
    from wetlang.gym import WetworldGymEnv

    total_ticks = int(steps) * int(steps_per_action)
    if total_ticks <= 0:
        raise ValueError(f"total_ticks must be positive, got {total_ticks}")

    dt_s = float(dt_ms) / 1000.0
    sim_duration_s = total_ticks * dt_s

    # Always step WetworldGymEnv with steps_per_action=1 so every tick's spike raster
    # in obs[64:128] is captured without discarding intermediate ticks.
    env = WetworldGymEnv(
        steps_per_action=1,
        dt_ms=dt_ms,
        max_episode_steps=total_ticks + 10,
    )
    obs, _ = env.reset(seed=42)

    n_ch = env.channel_count
    spike_mat = np.empty((total_ticks, n_ch), dtype=np.uint8)
    zero_action = np.zeros(4, dtype=np.float32)

    try:
        for tick_idx in range(total_ticks):
            obs, _, terminated, _, _ = env.step(zero_action)
            spike_mat[tick_idx] = (obs[n_ch:n_ch * 2] > 0.5).astype(np.uint8)
            if terminated:
                raise RuntimeError(f"WetworldGymEnv terminated prematurely at tick {tick_idx}")
    finally:
        env.close()

    # True per-channel firing rates across the simulated window
    total_spikes_per_ch = np.sum(spike_mat, axis=0, dtype=np.float64)
    ch_rates = total_spikes_per_ch / sim_duration_s
    sim_rate = float(np.mean(ch_rates))

    # True inter-spike interval (ISI) CV and burst fraction (ISI <= 50 ms) per active channel
    cv_isis = []
    burst_fractions = []
    for ch in range(n_ch):
        spike_ticks = np.nonzero(spike_mat[:, ch])[0]
        if len(spike_ticks) < 3:
            continue
        spike_times_s = spike_ticks.astype(np.float64) * dt_s
        isis = np.diff(spike_times_s)
        mean_isi = float(np.mean(isis))
        if len(isis) > 0 and mean_isi > 0.0:
            cv_isis.append(float(np.std(isis)) / mean_isi)
            burst_fractions.append(float(np.sum(isis <= 0.05)) / float(len(isis)))

    if not cv_isis:
        raise RuntimeError(
            f"Insufficient simulated spikes ({int(np.sum(total_spikes_per_ch))} total over "
            f"{sim_duration_s:.3f}s) to compute genuine ISI statistics."
        )

    sim_cv = float(np.mean(cv_isis))
    sim_burst = float(np.mean(burst_fractions))

    return {
        "mean_firing_rate_hz": sim_rate,
        "mean_cv_isi": sim_cv,
        "mean_burst_fraction": sim_burst,
        "sim_duration_s": sim_duration_s,
        "total_spikes": int(np.sum(total_spikes_per_ch)),
        "active_channels": len(cv_isis),
    }


def validate_against_finalspark(
    hdf5_path: Path = DEFAULT_HDF5_PATH,
    sample_size: int = 50000,
    sim_steps: int = 30000,
    strict: bool = False,
) -> bool:
    """Validates Wetworld digital twin against empirical biological bounds."""
    print("=" * 78)
    print(" FinalSpark fs369 Empirical Electrophysiological Validation")
    print("=" * 78)

    t0 = time.time()
    empirical, is_live = load_empirical_metrics(hdf5_path, sample_size)
    source_tag = "LIVE HDF5 RECORDING" if is_live else "CACHED EMPIRICAL REFERENCE"
    print(f" Empirical Source: {empirical['dataset']} [{source_tag}]")
    if is_live:
        print(f" Sample Window: {sample_size:,} events | Active Electrodes: {empirical.get('active_electrodes', 64)}")

    print("-" * 78)
    print(" Simulating WetLang digital twin baseline organoid dynamics...")
    simulated = run_simulated_twin(steps=sim_steps)
    t_elapsed = time.time() - t0

    # Validation Checks
    rate_ok = (
        empirical["firing_rate_min_hz"]
        <= simulated["mean_firing_rate_hz"]
        <= empirical["firing_rate_max_hz"]
    )
    cv_ok = (
        empirical["cv_isi_min"]
        <= simulated["mean_cv_isi"]
        <= empirical["cv_isi_max"]
    )
    burst_ok = (
        empirical["burst_fraction_min"]
        <= simulated["mean_burst_fraction"]
        <= empirical["burst_fraction_max"]
    )

    all_passed = rate_ok and cv_ok and burst_ok

    print("-" * 78)
    print(f" {'Metric':<25} | {'Empirical':<12} | {'Simulated':<12} | {'Allowable Bound':<16} | Status")
    print("-" * 78)

    rate_str = f"{empirical['mean_firing_rate_hz']:.2f} Hz"
    sim_rate_str = f"{simulated['mean_firing_rate_hz']:.2f} Hz"
    bound_rate_str = f"[{empirical['firing_rate_min_hz']:.1f}, {empirical['firing_rate_max_hz']:.1f}] Hz"
    status_rate = "PASS" if rate_ok else "FAIL"
    print(f" {'Firing Rate (mean)':<25} | {rate_str:<12} | {sim_rate_str:<12} | {bound_rate_str:<16} | {status_rate}")

    cv_str = f"{empirical['mean_cv_isi']:.2f}"
    sim_cv_str = f"{simulated['mean_cv_isi']:.2f}"
    bound_cv_str = f"[{empirical['cv_isi_min']:.1f}, {empirical['cv_isi_max']:.1f}]"
    status_cv = "PASS" if cv_ok else "FAIL"
    print(f" {'ISI CV (burstiness)':<25} | {cv_str:<12} | {sim_cv_str:<12} | {bound_cv_str:<16} | {status_cv}")

    bf_str = f"{empirical['mean_burst_fraction']*100:.1f}%"
    sim_bf_str = f"{simulated['mean_burst_fraction']*100:.1f}%"
    bound_bf_str = f"[{empirical['burst_fraction_min']*100:.0f}%, {empirical['burst_fraction_max']*100:.0f}%]"
    status_bf = "PASS" if burst_ok else "FAIL"
    print(f" {'Burst Fraction (<=50ms)':<25} | {bf_str:<12} | {sim_bf_str:<12} | {bound_bf_str:<16} | {status_bf}")

    print("-" * 78)
    print(f" Validation Duration: {t_elapsed:.2f}s | Result: {'PASSED (Biological Fidelity Confirmed)' if all_passed else 'FAILED'}")
    print("=" * 78)

    if strict and not all_passed:
        raise ValueError("Simulated digital twin electrophysiology diverged from FinalSpark empirical bounds")

    return all_passed


def main():
    parser = argparse.ArgumentParser(description="FinalSpark fs369 Empirical Electrophysiological Validation")
    parser.add_argument("--data-path", type=str, default=str(DEFAULT_HDF5_PATH), help="Path to fs369_package.hdf5")
    parser.add_argument("--sample-size", type=int, default=50000, help="Number of empirical events to sample")
    parser.add_argument("--sim-steps", type=int, default=30000, help="Simulation ticks (dt=0.1ms) for digital twin")
    parser.add_argument("--strict", action="store_true", help="Raise error if validation fails")
    args = parser.parse_args()

    passed = validate_against_finalspark(
        hdf5_path=Path(args.data_path),
        sample_size=args.sample_size,
        sim_steps=args.sim_steps,
        strict=args.strict,
    )
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
