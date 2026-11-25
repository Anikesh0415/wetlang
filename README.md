# WetLang

WetLang is a domain-specific language, static biophysical safety analyzer, and freestanding C99 simulation runtime for closed-loop microelectrode array (MEA) stimulation, microfluidic life-support control, and neuromorphic silicon lowering.

## Overview

WetLang combines a static dimensional and electrochemical safety frontend with a zero-`malloc` C99 runtime (`wetvm.dll`) wrapped in Python and Farama Gymnasium (`WetworldGymEnv`). Rather than treating living neural tissue as a deterministic microprocessor, WetLang uses `.wet` programs and Python/PyTorch closed-loop policies to coordinate stimulation, readout, life-support limits, and hardware safety interlocks against either an in-silico COBA-LIF dynamical plant or neuromorphic silicon targets.

### Architecture & Scope

- **Static Compiler & Single-Source Linter (`compiler/`, `wetlang/cli.py`):**
  - Enforces physical SI units (`V`, `mV`, `uA`, `nC`, `ms`, `us`, `uL/min`, `um`, `kOhm`, `Hz`) and forbids incompatible dimensional arithmetic.
  - Enforces compile-time electrochemical water-window bounds (`[-1.2 V, +1.2 V]`), dynamic EIS current-density clamps (`30 uA/cm^2`), per-phase biphasic charge balance (`<= 0.5 nC`), Krogh-Thiele oxygen diffusion limits (`200 um` unperfused / `250 um` avascular), hydrodynamic channel wall-shear limits (`<= 0.05 Pa`), and control-flow graph (`CFG`) loop yield checks (`sync_tick`).
  - Exposes `wetlang check --format=json` as the canonical diagnostic backend for the VS Code extension.
- **Freestanding C99 Simulation Runtime (`native/`):**
  - Exact Exponential Euler COBA-LIF neuron dynamics, 4-class Tsodyks-Markram short-term plasticity (STP), pairwise spike-timing-dependent plasticity (STDP), slow afterhyperpolarization (AHP), and 2D spatial pickup across 64 MEA channels (`biophysics.c`).
  - Deterministic static arena VM (`wet_create_vm_arena`) and real-time scheduler (`wet_scheduler.c`) verified with zero heap allocations (`malloc`/`calloc`/`realloc`/`free`) in all stepping paths.
  - IEEE-754 finite-guarded safety interlocks (`interlocks.c`), 64-bit integer attoCoulomb DC drift tracking, and bounded AER spike ring buffers (`wet_aer.c`).
- **Neuromorphic Silicon Lowering (`compiler/emitter.py`):**
  - `--target=sim`: Emits signed `.wbc` bytecode for the native C99 VM.
  - `--target=loihi2`: Lowers AST declarations and stimulation primitives to Intel Lava processes (`AbstractProcess` + `PyLoihiProcessModel`) with a pure-Python behavioral reference simulator (`compiler/loihi2_ref_sim.py`).
  - `--target=spinnaker`: Lowers AST declarations to PyNN scripts (`pyNN.spiNNaker`) with a pure-Python behavioral reference simulator (`compiler/spinnaker_ref_sim.py`).
  - Wetware-only operations (microfluidic perfusion, pump/valve control) emit `W_SUBSTRATE_UNSUPPORTED_OP` warnings and lower to safe no-ops on silicon targets.
- **Closed-Loop AI & Empirical Validation (`wetlang/gym.py`, `sandbox/`, `benchmarks/`):**
  - `WetworldGymEnv(gymnasium.Env)` binds pre-allocated C99 arena buffers and multi-tick spike window accumulators to Python/PyTorch workflows with zero runtime heap allocations during `step()`.
  - Includes DishBrain Pong and CartPole closed-loop benchmarks using both PyTorch reward-modulated STDP (R-STDP) and Active Inference / Free Energy Principle (FEP) variational entropy controllers.
  - Validates baseline organoid firing rates (`3.55 Hz` simulated vs `3.87 Hz` empirical), ISI CV, and burst fractions against FinalSpark `fs369` HDF5 MEA recordings (`benchmarks/finalspark_validation.py`).
- **Hardware Abstraction Layer Scope (`native/src/wet_hal*.c`):**
  - `wet_hal_intan.c`, `wet_hal_maxwell.c`, `wet_hal_pump_valve.c`, and `wet_hal_sensirion.c` implement C99 command/frame encoders (Intan RHS2116 SPI commands, MaxOne channel routing matrices, pump/valve interlocks, and artifact blanking) paired with deterministic hardware-in-the-loop (HIL) state models.
  - Physical lab deployment requires linking external vendor transport drivers (such as Intan RHX, MaxLab C++ SDK, or FinalSpark Neuroplatform transport) behind the `wet_hal_ops_t` vtable.

## Installation

Build prerequisites: Python 3.10+ and Clang/LLVM (`clang`) for compiling the C99 runtime library.

```bash
git clone https://github.com/Anikesh0415/wetlang.git
cd wetlang
pip install -r requirements.txt
pip install -e .
python native/build.py
```

## Quickstart

### 1. Write a WetLang Program (`brain.wet`)

```wetlang
organoid CorticalUnit {
    radius: 180um;
    perfusion: 1.5uL/min;
}

fn main() {
    pump_set_rate(0, 1.5uL/min);
    valve_open(0);

    stim_biphasic(0, 0.4V, 0.2ms, 0.2ms);
    sync_tick();
}
```

### 2. CLI Commands

```bash
# Static safety & dimensional lint (JSON output supported for editors)
wetlang check brain.wet --format=json

# Compile to C99 VM bytecode (.wbc), Intel Loihi-2 (Lava), or SpiNNaker (PyNN)
wetlang compile brain.wet --target=sim -o brain.wbc
wetlang compile brain.wet --target=loihi2 -o brain_lava.py
wetlang compile brain.wet --target=spinnaker -o brain_pynn.py

# Execute on the native C99 VM
wetlang run brain.wet --ticks 20

# Disassemble compiled bytecode
wetlang disasm brain.wbc
```

### 3. Python API & Closed-Loop Gymnasium

```python
import wetlang as wl

# Canonical Gymnasium environment backed by C99 pre-allocated arena memory
env = wl.WetworldGymEnv(steps_per_action=10)
obs, info = env.reset()

for _ in range(50):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break

env.close()
```

### 4. Closed-Loop Benchmarks

```bash
python benchmarks/run_pong_rl.py --episodes 10 --max-steps 200
python benchmarks/run_pong_fep.py --episodes 10 --max-steps 200
python benchmarks/run_cartpole_rl.py --episodes 10 --max-steps 300
python benchmarks/run_cartpole_fep.py --episodes 10 --max-steps 300
python benchmarks/finalspark_validation.py --strict
```

## VS Code Extension

The official editor extension lives in `vscode-wetlang/` and provides:

- TextMate syntax highlighting (`syntaxes/wet.tmLanguage.json`) covering all 73 language keywords and operators plus SI physical unit suffixes.
- Single-source real-time linting invoking `wetlang check --format=json --stdin` on open/unsaved editor buffers via `execFile` without shell interpolation.

## Repository Structure

```text
wetlang/
├── .github/workflows/   # CI workflows
├── benchmarks/          # Pong/CartPole RL & FEP scripts, FinalSpark fs369 validator, .wet benchmarks
├── bin/                 # CLI wrapper scripts (wetlang, wetlang.cmd)
├── bindings/            # ctypes ABI definitions, VM runtime wrapper, AER & scheduler bindings
├── biophysics/          # Reference Python/NumPy COBA-LIF, STP, STDP, and MEA models
├── compiler/            # Lexer, Pratt parser, AST, semantic safety analyzer, emitters, ref simulators
├── examples/            # Example .wet programs and Python closed-loop scripts
├── native/              # Freestanding C99 engine, headers, HAL protocol framers, build.py
├── sandbox/             # Multi-organoid sandbox and shared DishBrain/CartPole encoders
├── tests/               # E2E, compiler, C99 zero-malloc, interlock, scheduler, and regression tests
├── vscode-wetlang/      # Official VS Code language extension & linter integration
├── wetlang/             # Public Python package (CLI, Gymnasium wrapper, PyTorch tensor interop, VM)
├── demo.py              # End-to-end compilation, execution, and safety interlock walkthrough
├── pyproject.toml       # Package metadata and entry points (wetlang, wetc)
├── setup.py             # Setuptools build configuration
├── requirements.txt     # Runtime dependencies
└── LICENSE              # Apache-2.0 License
```

## Testing & Verification

Run the verification suites from the repository root:

```bash
# C99 strict pedantic build (-std=c99 -Wall -Wextra -Werror -pedantic) + llvm-nm zero-malloc audit
pytest tests/test_c99_zero_malloc.py -v

# End-to-end unittest suite (313 tests)
python -m unittest discover -s tests/e2e -p "test_*.py"

# Full pytest suite (677 tests)
pytest -q
```

## License

Developed by **Anikesh Tiwari**. Licensed under the [Apache License, Version 2.0](LICENSE).
