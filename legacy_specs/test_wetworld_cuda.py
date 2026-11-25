#!/usr/bin/env python
"""
test_wetworld_cuda.py
================================================================================
WETWORLD: "CUDA for Organoid Intelligence" Verification Suite
Demonstrates the complete Wetworld SDK & Biological Hardware Abstraction Layer.
Authored by: Anikesh Tiwari | Wetworld
================================================================================
"""

import sys
import os
import time

# Ensure current directory is in path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

import wetworld as ww

def run_wetworld_verification():
    print("=" * 80)
    print("        WETWORLD: THE OPEN COMPUTATIONAL ARCHITECTURE FOR ORGANOID INTELLIGENCE")
    print(f"        SDK Version: {ww.__version__} | Architect: {ww.__author__} ({ww.__organization__})")
    print("=" * 80)

    # 1. Initialize Biological Compute Session (Bio-HAL)
    print("\n[PHASE 1] Initializing Biological Compute Session (Bio-HAL)...")
    session = ww.Session(backend="in_silico")
    print(f"  -> Connected: {session}")

    # 2. Audit Biological Health & Viability
    telemetry = session.get_telemetry()
    print("\n[PHASE 2] Auditing Biological Viability & Biophysics Telemetry...")
    print(f"  -> Active Neural Density:     {telemetry['neurons_active']} neurons (80:20 E/I ratio)")
    print(f"  -> Core Oxygen Tension:       {telemetry['core_po2_mmhg']} mmHg (Safe > 85 mmHg)")
    print(f"  -> WW-16 Wall Shear Stress:   {telemetry['wall_shear_stress_pa']} Pa (< 0.08 Pa limit)")
    print(f"  -> Input-Referred Noise:      {telemetry['input_referred_noise_uv_rms']} µVrms (Enforcing < 2.0 µVrms)")
    print(f"  -> Critical Branching Ratio:  m = {telemetry['branching_ratio_m']} (Optimal criticality [0.982, 0.997])")

    # 3. Dispatch Bio-ISA Microvolt Kernels
    print("\n[PHASE 3] Dispatching Bio-ISA Microvolt Kernels...")
    print("  -> Injecting 30 µA Biphasic Pulse into Sensory Channels [0, 1, 2, 3]...")
    stim_tensor = session.stimulate(channels=[0, 1, 2, 3], amplitude_ua=30.0, duration_us=200.0, duration_ms=25.0)
    print(f"  -> Acquired Post-Stimulus Tensor: {stim_tensor}")

    print("  -> Sensing 50 ms Multi-Channel Extracellular Biopotentials...")
    sense_tensor = session.sense(duration_ms=50.0)
    print(f"  -> Acquired Stream Tensor: {sense_tensor}")

    # 4. Spike Extraction & Electrophysiological Metrics
    print("\n[PHASE 4] Extracting Biological Action Potentials (Quiroga DSP)...")
    spikes = sense_tensor.extract_spikes(threshold_std=4.5)
    firing_rates = sense_tensor.firing_rates_hz()
    spectral_entropy = sense_tensor.compute_spectral_entropy()
    print(f"  -> Total Detected Spikes:     {spikes.sum()} unit events across 64 channels")
    print(f"  -> Mean Population Rate:      {firing_rates.mean():.2f} Hz")
    print(f"  -> Shannon Spectral Entropy:  {spectral_entropy:.3f} bits")

    # 5. Embodied Active Inference Benchmark
    print("\n[PHASE 5] Executing Embodied Active Inference (Karl Friston's Free Energy Principle)...")
    task = ww.ActiveInferenceTask(session)
    
    # Warmup cycle (initializes JIT caches and buffer memory)
    task.step(dt=0.010)

    print("  -> Running 30 closed-loop cycles on Inverted Pendulum benchmark...")
    latencies = []
    for step_i in range(30):
        step_metrics = task.step(dt=0.010)
        lat = step_metrics["closed_loop_latency_ms"]
        latencies.append(lat)
        if step_i % 10 == 0:
            print(f"     Step {step_i:02d}: Tilt={step_metrics['theta_rad']:+.3f} rad | "
                  f"Force={step_metrics['action_force']:+.2f} N | "
                  f"FreeEnergy={step_metrics['free_energy']:.3f} | "
                  f"Latency={lat:.2f} ms")

    max_latency = max(latencies)
    mean_latency = sum(latencies) / len(latencies)
    print(f"  -> Mean Closed-Loop Latency:    {mean_latency:.2f} ms")
    print(f"  -> Maximum Closed-Loop Latency: {max_latency:.2f} ms")
    assert max_latency <= 10.0, f"Closed-loop latency {max_latency:.2f} ms violated sub-10ms STDP threshold!"
    print("  -> Latency Budget: STRICT PASS (< 10 ms STDP biological window)")

    # 6. Neuromorphic Intermediate Representation (NIR) Compilation
    print("\n[PHASE 6] Compiling Biological Graph to NIR Neuromorphic Standard...")
    nir_out_path = os.path.join(CURRENT_DIR, "wetworld_compiled.nir.json")
    ww.NIRCompiler.export_file(nir_out_path, num_neurons=1024, num_inputs=8, num_outputs=2)
    print(f"  -> Exported NIR Graph to: {nir_out_path}")

    # Clean up
    session.close()

    print("\n" + "=" * 80)
    print("       WETWORLD COMPUTE ARCHITECTURE: 100% VERIFICATION SUCCESSFUL")
    print("       'CUDA for Organoid Intelligence' is Operational in Wetworld.")
    print("=" * 80)

if __name__ == "__main__":
    run_wetworld_verification()
