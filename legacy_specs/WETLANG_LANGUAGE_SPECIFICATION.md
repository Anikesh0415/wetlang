# WetLang: The Native Programming Language for Biological Wetware Computing
## Language Specification & Reference Manual (v1.0.0)

**Language Architect & Designer:** Anikesh Tiwari  
**Target Architecture:** Wetworld Biological Neural Appliances & In-Silico Organoid Twins  
**File Extension:** `.wet`  
**Official Compiler:** `wetc`  
**Virtual Machine / Runtime:** `WetVM`  
**Date of Ratification:** November 2026  

---

## 1. Philosophical & Biophysical Foundation

Classical programming languages (C, Python, Rust) are strictly **Von Neumann abstractions**: they assume deterministic CPU clocks, static 64-bit addressable memory cells, and sequential instruction execution.

Living neural wetware is non-Von Neumann:
1. **Asynchronous & Continuous-Time:** Neurons fire on electro-chemical event dynamics, not clock ticks.
2. **Dynamic Plastic Memory:** Synaptic weights self-wire in response to millisecond spike timing differences (Spike-Timing-Dependent Plasticity - STDP).
3. **Variational Free Energy Minimization:** Biological tissue computes by minimizing thermodynamic and sensory surprise (Karl Friston's Free Energy Principle).
4. **Physical & Dimensional Safety:** Commands sent to wetware are physical electrical currents ($\mu\text{A}$) and fluid flows ($\mu\text{L/min}$). Passing incorrect values will permanently kill the tissue via necrosis or lysis.

**WetLang** is designed from first principles as the first native programming language that treats biological neural tissue as a primary computational primitive with compile-time physical dimension checking.

---

## 2. Core Language Grammar & Primitives

### 2.1 The `tissue` Declaration
Specifies the biological substrate, cytoarchitecture, and microfluidic life support:
```wetlang
tissue CortexAlpha {
    density: 1024;
    ratio: 80% excitatory, 20% inhibitory;
    perfusion: 2.5 uL/min;
    geometry: sphere(radius = 250 um);
    plasticity: STDP(tau_plus = 20 ms, tau_minus = 20 ms, ltp_rate = 0.05);
}
```

### 2.2 The `port` Declaration
Defines physical or virtual Multi-Electrode Array (MEA) pinouts:
```wetlang
port SensoryArray {
    channels: [0..7];
    mode: BiphasicCurrent;
    max_current: 45 uA;
    pulse_width: 200 us;
}

port MotorArray {
    channels: [56..63];
    mode: SpikeReadout;
    window: 10 ms;
}
```

### 2.3 The `objective` Declaration (Active Inference)
Defines sensory priors and entropic feedback driving biological learning:
```wetlang
objective BalanceInvertedPendulum {
    observe: SensoryArray;
    prior: angle in [-0.05 rad, 0.05 rad];
    
    // Punish deviations with unpredictable high-entropy electrical bursts
    on error > 0.20 rad: {
        burst(SensoryArray, current = 40 uA, duration = 10 ms);
    }
    
    // Reward alignment with predictable resonant pulses
    on success: {
        pulse(SensoryArray, frequency = 25 Hz, current = 15 uA);
    }
}
```

### 2.4 The `stream` & `cycle` Declaration
Defines physical signal routing and real-time execution loops:
```wetlang
stream ClosedLoopEngine {
    bind CortexAlpha.SensoryArray -> InvertedPendulum.Angle;
    bind InvertedPendulum.MotorForce <- CortexAlpha.MotorArray;
    
    cycle {
        evolve CortexAlpha for 10 ms;
        audit viability(min_po2 = 85 mmHg, max_shear = 0.08 Pa);
    };
}
```

---

## 3. Compile-Time Biophysical Type Safety

`wetc` enforces strict physical biophysical laws at compile time:

| Hazard Class | Failure Condition | Compiler Action |
| :--- | :--- | :--- |
| **Krogh Necrosis** | `radius > 200 um` AND `perfusion < 0.8 uL/min` | **Fatal Compile Error:** Core anoxic necrosis mathematically guaranteed. |
| **Cellular Lysis** | `max_current > 100 uA` | **Fatal Compile Error:** Electrical current exceeds membrane electroporation limit. |
| **Electrolysis Hazard** | `pulse_width > 1000 us` | **Fatal Compile Error:** Charge injection limit violated (causes electrode oxidation). |
| **Electrode Collision** | Same MEA channel allocated to multiple ports | **Fatal Compile Error:** Short-circuit hardware collision. |

---

## 4. Compiler CLI Usage

```powershell
# Type-check and verify biophysical safety:
wetc check program.wet

# Compile and execute on WetVM:
wetc run program.wet --cycles 30 --backend in_silico
```

---
*Authored by Anikesh Tiwari | Wetworld Engineering Systems*
