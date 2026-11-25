# WETWORLD: Autonomous Organoid Intelligence & Neuromorphic Wetware Computing Architecture

**Founder & Lead Systems Architect:** Anikesh Tiwari  
**Classification:** Open-Source Biocomputing & Bio-Hybrid Neuromorphic Architecture  
**Primary Deliverable:** `wetworld_oi_studio.html`  
**Launch Command:** `python run_wetworld_studio.py`  

---

## 1. Executive Mission & Identity

**Wetworld** is an autonomous, open-source biocomputing engineering initiative developing self-sustaining biological artificial intelligence running at **<20W edge power**.

By interfacing 3D human cerebral organoids with high-density microelectrode arrays (MEA) and neuromorphic spiking silicon, Wetworld transforms living neural tissue from an in-vitro cell culture into a fault-tolerant, continuous, energy-efficient computational processor.

---

## 2. The 4-Tier Wetworld Physical Architecture

```
===================================================================================================
                                  WETWORLD 4-TIER HARDWARE TOPOLOGY
===================================================================================================

  [Tier 4: Host Orchestration & NIR Standard]
  • High-performance Python server interfacing local testbenches, FinalSpark cloud, or edge nodes
  • Exports spiking neural network graphs to the Neuromorphic Intermediate Representation (NIR)
        │
        ▼
  [Tier 3: Real-Time Edge Processing & Closed-Loop Control]
  • Real-time spike sorting (<10 ms closed-loop budget for Spike-Timing-Dependent Plasticity)
  • SynSense Xylo (<500 µW) / AMD Kria edge co-processors
  • Karl Friston's Free Energy Principle: embodied active inference via sensory entropy minimization
        │
        ▼
  [Tier 2: Analog Front-End (AFE) & Biopotential Sensing]
  • 6-layer custom KiCad PCB hosting an 8x8 (64-channel) Multi-Electrode Array (MEA)
  • Capacitive-Coupled Instrumentation Amplifiers (CCIA) with sub-threshold pseudo-resistors (R_eq >= 1.0–1.6 TΩ)
  • Solid L2 AGND ground plane enforcing input-referred noise < 2.0 µVrms in 37°C saline
        │
        ▼
  [Tier 1: Living Wetware & WW-16 Perfusion Manifold]
  • Negative-space microfluidic manifold sustaining 3D cortical organoids
  • Laminar delivery (Re ≈ 1.2 in 100 µm feed channels) -> Creeping Stokes flow (Re < 0.1) in culture well
  • Wall shear stress strictly maintained at τ ≈ 0.05 dyn/cm² (safely below 0.1–0.5 dyn/cm² cell damage limit)
  • Solves the Krogh cylinder diffusion limit (r_crit ≈ 200–300 µm), preventing core anoxic necrosis
===================================================================================================
```

---

## 3. Wetworld OI Studio (In-Silico Interactive Laboratory)

To enable researchers, students, and engineers worldwide to test, simulate, and understand Organoid Intelligence from first principles, Wetworld provides the **Wetworld OI Studio** (`wetworld_oi_studio.html`):

### Core Interactive Features:
1. **3D Cortical Organoid Engine (Three.js WebGL):**
   - 1,024 interactive neurons with realistic biological heterogeneity (80% Excitatory Pyramidal cells, 20% Inhibitory Interneurons).
   - Real-time action potential wave propagation (somatic depolarization glowing at +30 mV).
   - Toggleable **Fickian Oxygen Diffusion Gradient**: visualizes the necrotic core boundary ($r_{\text{crit}} \approx 250\,\mu\text{m}$) if microfluidic perfusion is halted.
2. **64-Channel MEA & Intan AFE Oscilloscope:**
   - Interactive 8x8 electrode grid: click any electrode to inject constant-current stimulation pulses.
   - Real-time oscilloscope tracking extracellular microvolt potential ($20\text{--}100\,\mu\text{V}$) with Johnson-Nyquist thermal noise and $1/f$ pink noise injection.
   - Multi-channel spike raster plot recording all unit firing events across the last 2.0 seconds.
3. **Interactive Spike-Timing-Dependent Plasticity (STDP) Lab:**
   - Real-time synaptic weight rewiring based on millisecond spike intervals:
     $$\Delta w = \begin{cases} A_+ e^{-\Delta t / \tau_+} & \text{for } \Delta t > 0 \text{ (causal LTP)} \\ -A_- e^{\Delta t / \tau_-} & \text{for } \Delta t < 0 \text{ (anti-causal LTD)} \end{cases}$$
4. **Embodied Active Inference Benchmark (Inverted Pendulum):**
   - The virtual organoid is embodied in a physical closed-loop task: balancing an inverted pendulum.
   - Sensory channels (Ch 0–7) encode tilt angle; motor channels (Ch 56–63) decode corrective push forces.
   - Follows Karl Friston’s Free Energy Principle: predictable pulses on balance, chaotic bursts on error, forcing the living network to self-stabilize.
5. **Neuromorphic Intermediate Representation (NIR) Export:**
   - One-click export of the learned spiking neural graph into the standard `NIR-1.0` JSON format, ready for deployment to silicon neuromorphic processors.

---

## 4. How to Launch and Test

### Method 1: Automated Local Server Runner
Run the launcher in your terminal:
```bash
python run_wetworld_studio.py
```
This serves the application on `http://localhost:8080/wetworld_oi_studio.html` and automatically opens your default browser.

### Method 2: Direct File Open
You can also directly open `<WORKSPACE_ROOT>\wetworld_oi_studio.html` in any modern web browser (Chrome, Edge, Firefox, Brave). No build tools, Node.js, or complex dependencies required.

---

## 5. First-Principles Equations Summary

| Domain | Governing Equation | Wetworld Implementation |
| :--- | :--- | :--- |
| **Microfluidics** | $\nabla^2 P_{O2} = \frac{R_{\text{metabolic}}}{D \cdot \alpha}$ (Fick's Second Law) | Creeping Stokes flow ($Re < 0.1$, $\tau \approx 0.05\,\text{dyn/cm}^2$) prevents necrotic core formation. |
| **Electrophysiology** | $V_{\text{rms}} = \sqrt{4 k_B T R \Delta f}$ (Thermal Noise) | CCIA front-end with sub-threshold pseudo-resistors ($R_{\text{eq}} \ge 1.0\,\text{T}\Omega$) keeps noise $<2.0\,\mu\text{V}_{\text{rms}}$. |
| **Plasticity** | $\Delta w = A_+ e^{-\Delta t / \tau_+}$ (Hebbian STDP) | Closed-loop round-trip latency strictly enforced at $<10\,\text{ms}$ to stay inside biological STDP plasticity windows. |
| **Active Inference** | $F = \mathbb{E}_q[\ln q(s) - \ln p(s, o)]$ (Free Energy) | Sensory feedback drives organoid to minimize entropy and stabilize control tasks. |

---

*Authored by Anikesh Tiwari | Wetworld Engineering Systems (Surat, Gujarat, India)*
