# Volume III: Biophysical Digital Twin & Empirical Scientific Grounding

**Platform:** Wetworld — WetLang Neural Organoid Computing Platform (v2.1.0)  
**Founder & Lead Architect:** Anikesh Tiwari (Surat, Gujarat, India)  
**Source Scope:** `native/include/biophysics.h`, `native/src/biophysics.c`, `biophysics/ode_solver.py`, `biophysics/stp.py`, `biophysics/stdp.py`, `biophysics/mea_grid.py`, `biophysics/telemetry.py`, `all_10_zenodo_papers.txt`, FinalSpark `fs369` dataset (`E:\data\fs369\fs369data`)

---

## 1. COBA-LIF + Slow AHP Membrane Dynamics & Exact Exponential Euler

### 1.1 Continuous-Time Governing Equations

Each of the $N = 64$ neurons in `native/src/biophysics.c` is modeled as a Conductance-Based Leaky Integrate-and-Fire (COBA-LIF) unit augmented with a slow potassium after-hyperpolarization (AHP) conductance and an adaptive firing threshold:

$$C_m \frac{dV_i}{dt} = g_L (E_L - V_i) + g_{e,i}(t)(E_e - V_i) + g_{i,i}(t)(E_i - V_i) + g_{\text{ahp},i}(t)(E_K - V_i) + I_{\text{stim},i}(t) + I_{\text{bg},i}(t)$$

with exponential relaxation dynamics for all synaptic conductances, adaptation, and dynamic threshold:

$$\frac{dg_{e,i}}{dt} = -\frac{g_{e,i}}{\tau_e}, \qquad \frac{dg_{i,i}}{dt} = -\frac{g_{i,i}}{\tau_i}, \qquad \frac{dg_{\text{ahp},i}}{dt} = -\frac{g_{\text{ahp},i}}{\tau_{\text{ahp}}}, \qquad \frac{dV_{\theta,i}}{dt} = -\frac{V_{\theta,i} - E_{\theta,\text{base}}}{\tau_\theta}$$

### 1.2 Exact Parameter Table (Verified from `native/src/biophysics.c` & `biophysics/*.py`)

| Symbol | C Field (`bio_state_t`) | Value | Units | Physiological Meaning |
|---|---|---:|---|---|
| $\Delta t$ | `dt_ms` | `0.1` | ms | Fixed integration timestep ($100\ \mu\text{s}$) |
| $C_m$ | `c_m_pf` | `200.0` | pF | Membrane capacitance ($\tau_m = C_m / g_L = 20.0\text{ ms}$) |
| $g_L$ | `g_leak_ns` | `10.0` | nS | Passive leak conductance |
| $E_L$ | `e_leak_mv` | `-70.0` | mV | Leak reversal / resting potential (init jitter $\pm 2\text{ mV}$) |
| $E_{\text{reset}}$ | `e_reset_mv` | `-75.0` | mV | Post-spike reset & refractory clamp potential |
| $E_{\theta,\text{base}}$ | `e_thresh_base_mv` | `-50.0` | mV | Baseline action-potential threshold |
| $E_e$ | `e_exc_mv` | `0.0` | mV | AMPA excitatory reversal potential |
| $E_i$ | `e_inh_mv` | `-80.0` | mV | $\text{GABA}_A$ inhibitory reversal potential |
| $E_K$ | `e_k_mv` | `-90.0` | mV | Slow $K^+$ AHP reversal potential |
| $\tau_e$ | `tau_exc_ms` | `5.0` | ms | AMPA synaptic conductance decay constant |
| $\tau_i$ | `tau_inh_ms` | `10.0` | ms | $\text{GABA}_A$ synaptic conductance decay constant |
| $\tau_{\text{ahp}}$ | `tau_ahp_ms` | `80.0` | ms | Slow potassium AHP conductance decay constant |
| $\tau_\theta$ | `tau_thresh_ms` | `10.0` | ms | Relative refractory threshold relaxation constant |
| $\Delta V_\theta$ | *(inline line 306)* | `+15.0` | mV | Threshold jump on spike emission |
| $\Delta g_{\text{ahp}}$ | *(inline line 307)* | `+2.0` | nS | Slow AHP conductance increment on spike emission |
| $t_{\text{abs}}$ | `BIO_ABS_REFRACT_MS` | `2.0` | ms | Hard absolute refractory clamp (`20` ticks) |
| $I_{\text{bg}}$ | *(inline line 280)* | $215 + 140\,\mathcal{N}(0,1)$ | pA | Tonic + Irwin-Hall cortical background synaptic drive |
| $k_{\text{stim}}$ | *(inline line 277)* | `1500.0` | pA/V | Extracellular field to somatic depolarization gain |
| $Z_{\text{elec}}$ | `electrode_impedance_kohm` | `1000.0` | $\text{k}\Omega$ | Electrode-electrolyte impedance ($1.0\text{ M}\Omega$) *(see note below)* |

> **Implementation Audit Notes (100% Ground Truth):**
> 1. **Electrode Impedance**: `native/include/biophysics.h` line 137 has a legacy comment `(50 kOhm)`, whereas `native/src/biophysics.c` line 62 initializes `bio->electrode_impedance_kohm = 1000.0f` ($1.0\text{ M}\Omega$), matching `docs/language_spec.md` §5.2. Charge per tick is computed from this runtime value: $I_{\mu\text{A}} = (V / 1000)\times 1000 = V\ [\mu\text{A}]$, so $Q_{\text{tick}} = I_{\mu\text{A}}\cdot \Delta t_{\text{ms}} = 0.1\cdot V\ [\text{nC}]$.
> 2. **Excitatory / Inhibitory Population Split**: `biophysics.c` line 70 assigns `bio->is_excitatory[i] = ((i % 5) != 4) ? 1 : 0` across $i \in \{0,\dots,63\}$. This deterministic modulo rule places inhibitory interneurons at indices $\{4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59\}$ — exactly **52 excitatory neurons (81.25%)** and **12 inhibitory neurons (18.75%)**, approximating the canonical 80%/20% cortical ratio.

### 1.3 Exact Exponential Euler Derivation & Unconditional Stability Proof

Group all conductances at tick $t_k$:
$$g_{\text{tot}} = g_L + g_e + g_i + g_{\text{ahp}} \ge g_L = 10\text{ nS}$$
Define the instantaneous steady-state target potential $V_\infty$ and effective membrane time constant $\tau_{\text{eff}}$:
$$V_\infty = \frac{g_L E_L + g_e E_e + g_i E_i + g_{\text{ahp}} E_K + I_{\text{stim}} + I_{\text{bg}}}{g_{\text{tot}}}, \qquad \tau_{\text{eff}} = \frac{C_m}{g_{\text{tot}}}$$
Then the linear first-order ODE over $[t_k, t_k + \Delta t]$ with frozen coefficients is:
$$\frac{dV}{dt} = -\frac{V - V_\infty}{\tau_{\text{eff}}}$$
whose **exact analytical solution** over step $\Delta t$ is:
$$V(t_k + \Delta t) = V_\infty + \left(V(t_k) - V_\infty\right)\exp\!\left(-\frac{\Delta t}{\tau_{\text{eff}}}\right)$$

**Unconditional Numerical Stability Proof (vs. Forward Euler and Explicit RK4):**
- Let $\alpha = \exp(-\Delta t / \tau_{\text{eff}})$. Because $C_m = 200\text{ pF} > 0$, $\Delta t = 0.1\text{ ms} > 0$, and $g_{\text{tot}} \ge g_L > 0$, we strictly have $\Delta t / \tau_{\text{eff}} > 0 \implies \alpha \in (0, 1)$.
- Consequently, $V(t_k + \Delta t) = (1 - \alpha) V_\infty + \alpha V(t_k)$ is a **strict convex combination** of $V(t_k)$ and $V_\infty$.
- **Theorem**: For any arbitrarily large excitatory or inhibitory conductance shock ($g_{\text{tot}} \to +\infty$, causing $\tau_{\text{eff}} \to 0^+$ and stiffness ratio $\Delta t / \tau_{\text{eff}} \to +\infty$), $\alpha \to 0^+$ smoothly and $V(t_k + \Delta t) \to V_\infty$ monotonically with **zero overshoot, zero sign oscillation, and zero divergence**.
- By contrast, explicit Forward Euler requires $\Delta t / \tau_{\text{eff}} < 2$ (diverging as soon as $g_{\text{tot}} > 4000\text{ nS}$), and explicit RK4 requires $\Delta t / \tau_{\text{eff}} < 2.785$ (diverging as soon as $g_{\text{tot}} > 5570\text{ nS}$). Under adversarial high-conductance or high-current bursts, Forward Euler and RK4 blow up to $\pm\infty$/NaN, whereas Exact Exponential Euler (plus the defensive `wet_clampf(v_next, -120.0f, 50.0f)` clamp) is provably A-stable and L-stable for all positive conductances.

---

## 2. Refractory Dynamics (Absolute & Relative)

When $V_i(t_k + \Delta t) \ge V_{\theta,i}(t_k)$:
1. **Spike Emission**: `spikes_now[i] = 1`.
2. **Absolute Refractory Clamp**: `v_m_mv[i] = -75.0f` ($E_{\text{reset}}$) and `refract_ticks[i] = 20` ($2.0\text{ ms}$ at $\Delta t = 0.1\text{ ms}$). On the next 20 ticks, `biophysics_step_tick()` decrements `refract_ticks[i]` and holds $V_i = -75.0\text{ mV}$ unconditionally, ignoring all synaptic and stimulation currents. This enforces a strict physical single-neuron firing ceiling:
   $$f_{\max} = \frac{1}{t_{\text{abs}}} = \frac{1}{2.0\text{ ms}} = 500\text{ Hz}$$
3. **Relative Refractory Adaptation**:
   - Instantaneous threshold jump: $V_{\theta,i} \leftarrow V_{\theta,i} + 15.0\text{ mV}$ (e.g., $-50 \to -35\text{ mV}$), decaying back to $-50\text{ mV}$ with $\tau_\theta = 10.0\text{ ms}$.
   - Slow potassium AHP recruitment: $g_{\text{ahp},i} \leftarrow g_{\text{ahp},i} + 2.0\text{ nS}$ pulling toward $E_K = -90\text{ mV}$ with $\tau_{\text{ahp}} = 80.0\text{ ms}$, providing spike-frequency adaptation and autonomous burst termination.

---

## 3. Tsodyks-Markram Short-Term Synaptic Plasticity (STP)

### 3.1 Sparse Spatial Connectivity & Equations

`biophysics_init()` creates directed recurrent synapses ($i \ne j$) with distance-dependent probability:
$$P_{\text{conn}}(i \to j) = 0.35 \exp\!\left(-\frac{\|\mathbf{r}_j - \mathbf{r}_i\|_2}{350\ \mu\text{m}}\right)$$
Initial weights are drawn uniformly: $w_0 \in [4, 10]\text{ nS}$ for excitatory presynaptic neurons and $w_0 \in [10, 20]\text{ nS}$ for inhibitory presynaptic neurons.

Each directed synapse tracks two dynamic state variables: utilization $u \in [U_{\text{base}}, 1]$ (calcium-dependent release probability) and available vesicle pool $x \in [0, 1]$:
- **Continuous Relaxation (Exact Exponential Euler every tick)**:
  $$x(t + \Delta t) = 1 + \left(x(t) - 1\right)\exp\!\left(-\frac{\Delta t}{\tau_{\text{rec}}}\right), \qquad u(t + \Delta t) = U_{\text{base}} + \left(u(t) - U_{\text{base}}\right)\exp\!\left(-\frac{\Delta t}{\tau_{\text{fac}}}\right)$$
- **Presynaptic Spike Arrival Update**:
  $$u^+ = u^- + U_{\text{base}}(1 - u^-), \qquad \Delta g = w \cdot (u^+ x^-), \qquad x^+ = \text{clamp}(x^- - u^+ x^-,\ 0,\ 1)$$
  where $\Delta g$ adds to `g_exc_ns[post]` if presynaptic neuron $i$ is excitatory, or to `g_inh_ns[post]` if inhibitory.

### 3.2 Parameter Table Across All 4 Cortical Synapse Classes

| Class | Enum (`bio_syn_class_t`) | Regime | $U_{\text{base}}$ | $\tau_{\text{rec}}$ (`biophysics.c`) | $\tau_{\text{rec}}$ (`biophysics/stp.py`) | $\tau_{\text{fac}}$ (ms) |
|---|---|---|---:|---:|---:|---:|
| **E $\to$ E** | `SYN_CLASS_EE` (`0`) | Strongly Depressing | `0.50` | `800.0` ms | `800.0` ms | `20.0` ms |
| **E $\to$ I** | `SYN_CLASS_EI` (`1`) | Strongly Facilitating | `0.15` | `200.0` ms | `200.0` ms | `600.0` ms |
| **I $\to$ E** | `SYN_CLASS_IE` (`2`) | Depressing | `0.25` | `500.0` ms | `700.0` ms | `50.0` ms |
| **I $\to$ I** | `SYN_CLASS_II` (`3`) | Moderately Depressing | `0.30` | `400.0` ms | `400.0` ms | `50.0` ms |

*(Note: The `500.0 ms` vs `700.0 ms` difference in $\tau_{\text{rec}}$ for `I->E` between the C runtime `biophysics.c` and the Python reference helper `biophysics/stp.py` is documented verbatim from source; unifying both to a single shared JSON/header constant table is recommended for v1.1.)*

---

## 4. Online Pairwise Exponential-Trace STDP & Dale's Principle

Each neuron maintains local presynaptic and postsynaptic eligibility traces $z_{\text{pre},i}(t)$ and $z_{\text{post},i}(t)$ decaying every tick with $\tau_+ = \tau_- = 20.0\text{ ms}$:
$$z_{\text{pre},i}(t + \Delta t) = z_{\text{pre},i}(t) e^{-\Delta t / \tau_+}, \qquad z_{\text{post},i}(t + \Delta t) = z_{\text{post},i}(t) e^{-\Delta t / \tau_-}$$
On every spike of neuron $i$:
1. Both traces increment: $z_{\text{pre},i} \leftarrow z_{\text{pre},i} + 1$, $z_{\text{post},i} \leftarrow z_{\text{post},i} + 1$.
2. **LTD (Outgoing Excitatory Synapses $i \to j$, post-before-pre)**:
   $$\Delta w_{ij} = -\eta_{\text{stdp}} A_- z_{\text{post},j}, \qquad A_- = 0.21\text{ nS}$$
3. **LTP (Incoming Excitatory Synapses $k \to i$, pre-before-post)**:
   $$\Delta w_{ki} = +\eta_{\text{stdp}} A_+ z_{\text{pre},k}, \qquad A_+ = 0.20\text{ nS}$$
4. **Hard Bounds & Stability Invariants**:
   - **1.05x Depression Bias**: $A_- / A_+ = 0.21 / 0.20 = 1.05$, ensuring uncorrelated Poisson firing produces net synaptic depression rather than runaway potentiation.
   - **Conductance Clamping**: $w \leftarrow \text{clamp}(w + \Delta w,\ 0.0\text{ nS},\ 40.0\text{ nS})$.
   - **Dale's Principle**: Inhibitory presynaptic neurons (`is_excitatory[pre] == 0`) never undergo autonomous STDP weight updates and never flip synaptic sign; conductance magnitude $w \ge 0$ always remains non-negative while excitatory/inhibitory polarity is fixed solely by $E_e = 0\text{ mV}$ vs $E_i = -80\text{ mV}$.
   - **Closed-Loop Neuromodulation**: `MODULATE_STDP(0, 0, scale)` modulates global $\eta_{\text{stdp}} = \texttt{stdp\_lr\_scale}$ (reward/punishment gating), while `MODULATE_STDP(pre, post, dw)` directly perturbs $w_{\text{pre},\text{post}}$ within $[0, 40]\text{ nS}$.

### 4.1 Live Synaptic Matrix Introspection (`wet_vm_get_synapse_matrix`)

To support continuous non-invasive connectome introspection and dynamic plasticity monitoring, WetLang v1.1 exposes live synapse matrix introspection directly across the C-ABI:
- **Exported C-ABI Function**:
  ```c
  WET_EXPORT wet_status_t wet_vm_get_synapse_matrix(
      const wet_vm_instance_t* vm,
      float* out_weights,
      size_t max_count
  );
  ```
- **Zero-Copy Python Binding**: Wrapped in `WetVM.get_synapse_matrix()`, returning a contiguous $(64, 64)$ float32 NumPy array containing the exact active synaptic conductance values $w_{ij} \in [0.0, 40.0]\text{ nS}$ in biological real time.
- **Dale's Principle Decomposition & Verification**: Enables direct online verification of Dale's principle decomposition ($W = W_+ - W_-$), synaptic drift tracking, and real-time connectivity matrix extraction without interrupting the $10\text{ kHz}$ hard real-time scheduler loop.

---

## 5. 8x8 MEA Spatial Geometry & 3D Volume Conduction

The array consists of 64 planar microelectrodes arranged in an $8 \times 8$ Cartesian grid at pitch $d_{\text{pitch}} = 200.0\ \mu\text{m}$ with bijective index mapping $\text{ch} = 8r + c \iff (r, c) = (\lfloor \text{ch}/8 \rfloor, \text{ch} \bmod 8)$.

### 5.1 Native C Forward Pickup & Stimulation Coupling (`biophysics.c`)

Neurons are placed over each grid site with bounded 3D spatial jitter:
$$x_i = 200 c + U(-15, +15)\ \mu\text{m}, \qquad y_i = 200 r + U(-15, +15)\ \mu\text{m}, \qquad z_i = U(20, 35)\ \mu\text{m}$$
Electrode centers lie in the substrate plane $z_e = 0$. The $64 \times 64$ normalized Lorentzian volume-conduction matrix (`lambda_um = 120.0`) is:
$$G_{c,i} = \frac{1}{1 + \|\mathbf{r}_i - \mathbf{e}_c\|_2^2 / \lambda^2}, \qquad P_{c,i} = \frac{G_{c,i}}{\sum_{j=0}^{63} G_{c,j}}$$
- **Cathodic-First Stimulation Polarity**: In real neurophysiology ($V_m = \phi_{\text{intra}} - \phi_{\text{extra}}$), a negative (cathodic) extracellular potential ($\phi_{\text{extra}} < 0$) depolarizes the soma and elicits action potentials. WetLang enforces cathodic-first biphasic pulses:
  $$I_{\text{stim},i}(t) = -k_{\text{stim}} \sum_{c=0}^{63} P_{c,i} V_{\text{ext},c}(t)$$
  where Phase 1 delivers cathodic negative potential (depolarization), Phase 2 delivers anodic positive potential (active charge recovery), and total net charge integrates to $<0.5\text{ nC}$.
- **Extracellular LFP Dipole Pickup & Artifact Blanking**: Instantaneous extracellular potential is modeled via the point-source transmembrane dipole equation:
  $$V_{\text{MEA},c}(t) = \sum_{i=0}^{63} \frac{I_{m,i}(t)}{4\pi\sigma \|\mathbf{e}_c - \mathbf{r}_i\|_2} + V_{\text{stim},c}(t)$$
  To prevent amplifier saturation, `read_spikes` enforces a $1.5\text{ ms}$ post-stimulus artifact blanking refractory window, distinguishing true biological action potentials from stimulation transients.
- **Axonal Conduction Delays**: Unmyelinated cortical axons conduct at biological velocity $v_c \approx 0.2\text{ m/s}$ ($5.0\text{ ms/mm}$). Synaptic connections between neuron $i$ and $j$ route through circular delay queues with physical latency $\tau_{ij} = \|\mathbf{r}_i - \mathbf{r}_j\|_2 / v_c \in [1, 150]\text{ ticks}$, enabling biological polychronous wavefront synchrony.

### 5.2 Krogh Cylinder Life-Support Diffusion & Microfluidic Coupling

Cortical organoids lack native blood vasculature. Unlike cylindrical capillary blood vessels described by the classic August Krogh model, brain organoids in perfusion chambers are avascular spheres where oxygen diffuses inward following the spherical steady-state reaction-diffusion (Thiele modulus) equation:
$$\frac{1}{r^2} \frac{d}{dr} \left( r^2 D_{\text{eff}} \frac{dC}{dr} \right) = \frac{d^2 C}{dr^2} + \frac{2}{r} \frac{dC}{dr} = M_0 \frac{C}{C + K_m}$$
where $D_{\text{eff}} = 2.0 \times 10^{-5}\text{ cm}^2/\text{s}$ (or $\approx 1.07 \times 10^{-9}\text{ m}^2/\text{s}$ effective in dense extracellular matrix) is the tissue diffusion coefficient, $M_0 = 0.03\text{ mM/s}$ is the volumetric consumption rate, and $K_m = 0.005\text{ mM}$ is the Michaelis-Menten affinity constant.
- **Critical Anoxia Radius**: When organoid radius $r > 200\,\mu\text{m}$, unperfused core oxygen drops below the hypoxic threshold ($C < 0.02\text{ mM}$), inducing central necrosis. The compiler statically enforces active laminar microfluidic perfusion (`ERR_KROGH_ANOXIA_VIOLATION`).
- **Avascular Spherical Diffusion Limit**: At $R > 250\,\mu\text{m}$, internal tissue diffusion resistance physically prevents oxygen penetration to the core even with 100% saturated external perfusion. The compiler rejects avascular organoids $> 250\,\mu\text{m}$ (`ERR_AVASCULAR_CORE_NECROSIS`) unless declared with structural vascularization, internal microfluidic channels, or air-liquid interface (ALI) slicing.
- **Hydrodynamic Shear Stress**: Microfluidic perfusion $Q$ maintains bath surface oxygen while strictly limiting wall shear stress:
  $$\tau_w = 1.2 \times \frac{6 \mu Q}{w h^2} \le 0.05\text{ Pa}$$
  tripping `ERR_SHEAR_STRESS_EXCEEDED` if excessive flow rates strip neurites.

### 5.3 Universal Multi-Organoid Connectome Scaling ($1$ to $10^3+$ Clusters)

WetLang scales from a single standalone organoid to large multi-organoid neural architectures (`UniversalOrganoidSandbox`), benchmarked from 1 to 1,024 discrete organoid nodes interconnected via 4,096 dynamic synaptic projections with sub-50 µs tick latency:
- Each organoid instance maintains its own independent C99 `wetvm` state, local 8x8 MEA electrophysiology, and microfluidic life-support telemetry.
- Inter-organoid axonal tracts (`connect OrganoidA[ch] -> OrganoidB[ch] with { delay: 5.0ms; weight: 1.2; };`) are simulated with sub-millisecond ring-buffered conduction delay lines.
- Inter-organoid graph routing operates with zero-copy shared memory, allowing computational biological networks of arbitrary scale.

### 5.2 Python Analytical Reference Kernel (`biophysics/mea_grid.py`)

`MEAGrid` provides the physical electrostatic point-source volume conduction forward model and resistive electrode cross-talk kernel for offline validation:
- Electrode centers: $(x_c, y_c) = ((c + 0.5)\cdot 200,\ (r + 0.5)\cdot 200)\ \mu\text{m}$ (ch `0` at `(100, 100)`, ch `63` at `(1500, 1500)`).
- Point-source potential in conductive medium ($\sigma = 0.3\text{ S/m}$, regularization radius $r_0 = 15.0\ \mu\text{m}$):
  $$V_c = \frac{I_{\text{nA}} \times 10^{-9}}{4\pi \sigma \sqrt{(x_s - x_c)^2 + (y_s - y_c)^2 + z_s^2 + r_0^2}\times 10^{-6}}\ [\text{V}]$$
- $64 \times 64$ resistive cross-talk matrix $C_{ij}$: $C_{ii} = 1.0$; 4-way adjacent ($|r_1-r_2|+|c_1-c_2|=1$) $C_{ij} = 0.04$; non-adjacent $C_{ij} = 0.04 / d_{\text{Euclid}}^2$.

---

## 6. Structured Telemetry Streaming (`biophysics/telemetry.py`)

`TelemetryStream` standardizes machine-readable logging across JSONL and CSV pipelines:
- **Per-Tick JSONL (`format_tick_json`)**: Emits one JSON object per line with keys:
  `{"tick": int, "time_ms": float (5 decimals), "v_m": float[], "spikes": int[], "population_rate_hz": float, "charges_nc": float[], ...kwargs}`.
- **Summary CSV Header (`get_csv_header`)**: `tick,time_ms,spike_count,r_inst_hz\n`.
- **Sparse Spike Event CSV (`format_spike_event`)**: `tick,time_ms,neuron_id,neuron_type` (1 decimal place on `time_ms`).
- **Instantaneous Rate Estimator (`compute_firing_rate`)**: $r_{\text{inst}} = N_{\text{spikes}} / (N_{\text{neurons}} \cdot \Delta t_{\text{ms}} / 1000)$.

---

## 7. Direct Mapping to Published Research & Empirical FinalSpark `fs369` Data

WetLang v1.0 is the operational software/runtime instantiation of the theoretical and empirical research program authored by Anikesh Tiwari across 9 standalone Zenodo papers and 1 unified master compendium (`all_10_zenodo_papers.txt`), grounded in the live 30 kHz human brain organoid recordings from the FinalSpark Neuroplatform (`E:\data\fs369\fs369data`):

- **Empirical Ground-Truth Dataset on Disk (`E:\data\fs369\fs369data`)**:
  - `fs369_raw.hdf5`: **270,677,927,049 bytes (252.09 GiB)** continuous uncompressed 30 kHz MEA recording (33,247,914 spikes, sampling period $T_s = 33.33\ \mu\text{s}$).
  - `fs369_package.hdf5`: **3,039,707,528 bytes (2.83 GiB)** packaged spike/feature dataset.
  - `fs369_segment_index.parquet`: **4,298,634 bytes (4.10 MiB)** segment metadata index.

| Zenodo Paper & DOI | Core Quantitative Finding | Direct Mapping into WetLang v1.0 / v2.0 |
|---|---|---|
| **1. Memory-Nonlinearity Trade-off in Critical Neural Substrates** (`10.5281/zenodo.22089249`) | Tsodyks-Markram STP boosted Linear Fading Memory Capacity `0.12 -> 0.22` (+83%) while worsening NARMA-10 NRMSE `0.90 -> 1.07`. | Directly motivated embedding all 4 Tsodyks-Markram STP classes (`E->E`, `E->I`, `I->E`, `I->I`) natively inside `biophysics.c` and testing spatio-temporal fading memory in **Benchmark 02**. |
| **2. Thermodynamics of Wetware: MaxEnt & SOC** (`10.5281/zenodo.22137998`) | Inverse Ising PCD MAE = `0.0077`; specific heat $C_v$ peaked at $T = 1.05$; avalanche exponent $\tau = 1.954$. | Justifies homeostatic criticality targeting (`15-25 Hz` window in **Benchmark 03**) and defines the v2.0 real-time Inverse Ising criticality monitor. |
| **3. Geometry of Chaos: Topological Memory & Fractals** (`10.5281/zenodo.22139454`) | Persistent $H_1$ homology loop lifetime = `1.3382`; DFA Hurst $H = 0.5242$; positive LLE $\lambda_1 = 0.0010$. | Motivates high-dimensional recurrent reservoir readouts (Benchmark 02) and v2.0 Vietoris-Rips $H_1$ topological state decoders. |
| **4. Scale Invariance: Renormalization Group Flow** (`10.5281/zenodo.22139748`) | Kadanoff $b=2$ coarse-graining invariant: $\tau_{\text{micro}} = 4.4798$, $\tau_{\text{macro}} = 4.4381$, $\Delta\tau = 0.0417 < 0.05$. | Justifies scaling WetLang's 8x8 (`64`-neuron) digital twin via hierarchical RG multi-scale tiling in v2.0 without losing critical statistics. |
| **5. Causal Computation: Directed Information Routing** (`10.5281/zenodo.22089208`) | Bivariate Transfer Entropy $\text{TE}_{\text{Inh}\to\text{Sum}} = 0.0305\text{ bits}$ proved active GABAergic suppression executes XOR logic. | Directly drove explicit GABAergic inhibitory subpopulation modeling (`E_inh = -80 mV`, `I->E`/`I->I` STP, Dale's Principle) in `biophysics.c`. |
| **6. Noise-Tolerant Biological Boolean Logic via Critical Avalanches** (`10.5281/zenodo.22084092`) | AND/OR/XOR/SR-Latch via STDP + SOC ($\tau \approx 1.67$) without brute-force electrical pacing. | Directly motivated low-amplitude biphasic stimulation + STDP modulation (`modulate_stdp`) over brute-force DC pacing. |
| **7. Detection Limits & Sub-Millisecond Dynamics** (`10.5281/zenodo.20968200`) | 30 kHz MEA physical Nyquist temporal floor = `33.3 us` ($T_s = 1/30000\text{ s}$). | Calibrated WetLang's fixed `dt = 0.1 ms = 100 us` (3x physical 30 kHz sample period) so stimulation pulses (`100-200 us`) and refractory clamps (`2.0 ms`) remain physically realizable on real 30 kHz MEAs. |
| **8. Physical & Computational Boundaries of Organoid Intelligence** (`10.5281/zenodo.21909482`) | Full-lifecycle `fs369`/`fs437` analysis discovered Beta (13–30 Hz) / Gamma (30–100 Hz) complexity phase inversion and power-law post-stimulus relaxation. | Grounds WetLang strictly in non-teleological physical electrophysiology (avoiding anthropomorphic metaphors) and informs stimulation recovery windows. |
| **9. Non-Equilibrium Dynamics, Higher-Order Info Physics & Wave Mechanics** (`10.5281/zenodo.21967013`) | 252 GB `fs369` recording (`33,247,914` spikes): positive entropy production $dS/dt > 0$, strange attractor, Complex Ginzburg-Landau wave dynamics. | Establishes the macro-scale wave-physics target for v2.0 multi-scale organoid simulation and live FinalSpark Neuroplatform backend integration. |
| **10. Organoid Intelligence Master Compendium** (`10.5281/zenodo.22664729`) | 125-page 2-volume open-access textbook synthesizing all 5 phases + `fs369`/`fs437` empirical findings. | Serves as the theoretical foundation paired with this WetLang systems engineering compendium. |
