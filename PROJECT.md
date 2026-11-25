# Project: WetLang Options 1, 3, 4 & 5-Bot Production Verification

## Architecture
WetLang is an open, biological and neuromorphic computing system comprising a C99 MISRA-compliant virtual machine runtime (`wetvm`), a from-scratch domain-specific compiler frontend, hardware biocybersecurity interlocks, and closed-loop sensory-motor interfaces for neural organoids and neuromorphic silicon processors.

### Extended System Data Flow
```
+-----------------------------------------------------------------------------------+
| 1. WetLang Source Code (.wet)                                                     |
+-----------------------------------------------------------------------------------+
                                    |
            +-----------------------+-----------------------+
            v                                               v
+---------------------------------------+ +---------------------------------------+
| 2A. Compiler Frontend & Linter        | | 2B. Official VS Code Extension        |
|    - 73 canonical lexer tokens        | |    - vscode-wetlang/ & TextMate JSON  |
|    - SI dimensional unit algebra      | |    - Calls 'wetlang check --format=   |
|    - Overvoltage & dynamic EIS clamp  | |      json' for single-source linting  |
|    - CFG loop sync_tick analysis      | |    - Zero duplicate TS linter logic   |
+---------------------------------------+ +---------------------------------------+
                    |
                    v
+-----------------------------------------------------------------------------------+
| 3. Multi-Target Substrate Lowering Emitter (`compiler/emitter.py`)                 |
|    - Target: WBC Bytecode (Native C99 runtime)                                    |
|    - Target: Intel Loihi-2 Lava (`AbstractProcess` + `PyLoihiProcessModel`)       |
|    - Target: SpiNNaker PyNN (`pyNN.spiNNaker` standard script)                    |
|    - Substrate Lowering Contract: W_SUBSTRATE_UNSUPPORTED_OP for wetware ops      |
|    - Pure-Python In-Repo Deterministic Reference Simulators                       |
+-----------------------------------------------------------------------------------+
                    |
                    v
+-----------------------------------------------------------------------------------+
| 4. Native Runtime & Closed-Loop Benchmark Suite                                   |
|    - `wetlang/gym.py`: WetworldGymEnv(gymnasium.Env) with C99 pre-allocated arena |
|    - `sandbox/gym_env.py`: State-to-stimulation encoders & motor decoders         |
|    - Dual Paradigms: PyTorch RL (R-STDP) & Active Inference (FEP)                 |
|    - Interlock Invariants: +/-1.2V water window, 64-bit attoCoulomb accumulator   |
|    - Empirical Calibration: Ingests FinalSpark fs369 recordings (94.15M spikes)   |
+-----------------------------------------------------------------------------------+
                    |
                    v
+-----------------------------------------------------------------------------------+
| 5. 5-Bot Adversarial Verification & Clean Release Synchronization                 |
|    - Clang C99 `-Wall -Wextra -Werror -pedantic` across all C files               |
|    - Symbol table audit (`llvm-nm`): 0 malloc/free in real-time execution paths   |
|    - `docs/JANUS_ADVERSARIAL_AUDIT.md`: 5-bot cross-domain challenge matrix       |
|    - Clean manifest mirror to `wetlang_github_release` passing all 878+ tests     |
+-----------------------------------------------------------------------------------+
```

---

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Canonical `WetworldGymEnv` | `wetlang/gym.py` wrapping C99 runtime via fixed-size pre-allocated arena struct (`create_vm_arena`), zero heap allocations in `step()` | M1 | Survey 1 (R1) |
| 2 | Reference Encoders & Sandbox | `sandbox/gym_env.py` providing shared observation/action encoders (`PongStateEncoder`, `CartPoleStateEncoder`, `MotorSpikeDecoder`) without duplicating step logic | M1 | Survey 1 (R1) |
| 3 | PyTorch RL with R-STDP | `benchmarks/run_pong_rl.py` & `benchmarks/run_cartpole_rl.py`: PyTorch policy net coupled with reward-modulated STDP eligibility traces | M1 | Survey 1 (R1) |
| 4 | Active Inference / FEP Agents | `benchmarks/run_pong_fep.py` & `benchmarks/run_cartpole_fep.py`: Free Energy Principle agents minimizing variational free energy via predictable vs. unpredictable stimulation | M1 | Survey 1 (R1) |
| 5 | Biophysical Safety Coupling | State-to-stimulation encoders enforce water window `±1.2 V`, zero net charge drift in 64-bit attoCoulomb accumulator, dynamic EIS current density clamp | M1 | Survey 1 (R1) |
| 6 | FinalSpark Empirical Adapter | `benchmarks/finalspark_validation.py` ingesting recordings from `E:\data\fs369\fs369data` to calibrate baseline firing rate, ISI CV, and burst fraction with CI fallback | M1 | Survey 1 (R1) |
| 7 | Intel Loihi-2 Lava Emitter | `compiler/emitter.py` `--target=loihi2` emitting Intel Lava `AbstractProcess` and `PyLoihiProcessModel` | M2 | Survey 2 (R2) |
| 8 | SpiNNaker PyNN Emitter | `compiler/emitter.py` `--target=spinnaker` emitting executable `pyNN.spiNNaker` scripts | M2 | Survey 2 (R2) |
| 9 | Substrate Lowering Contract | Maps stimulation/compartments; emits `W_SUBSTRATE_UNSUPPORTED_OP` warnings and safe no-op comments for wetware-only primitives | M2 | Survey 2 (R2) |
| 10 | In-Repo Reference Simulators | `compiler/loihi2_ref_sim.py` & `compiler/spinnaker_ref_sim.py` providing deterministic execution fallbacks without vendor hardware | M2 | Survey 2 (R2) |
| 11 | CLI Neuromorphic Driver | `--target` choices (`loihi2`, `spinnaker`) in `compiler/compiler_cli.py` and `wetlang/cli.py` | M2 | Survey 2 (R2) |
| 12 | VS Code Extension Scaffolding | `vscode-wetlang/` containing `package.json`, `language-configuration.json`, `tsconfig.json`, `src/extension.ts`, icons | M3 | Survey 2 (R3) |
| 13 | TextMate Syntax Grammar | `vscode-wetlang/syntaxes/wet.tmLanguage.json` covering all 73 canonical lexer token types | M3 | Survey 2 (R3) |
| 14 | Token Parity Verification | Pytest automated check verifying all 73 canonical tokens from `compiler/token.py` are mapped in `syntaxes/wet.tmLanguage.json` | M3 | Survey 2 (R3) |
| 15 | Single-Source Linter CLI | `wetlang check --format=json <file>` in `wetlang/cli.py` and `compiler/semantic.py` returning structured non-fatal diagnostics | M3 | Survey 2 (R3) |
| 16 | Comprehensive Static Checks | Compile-time overvoltage (`> ±1.2 V`), dynamic EIS current density clamp, SI dimensional unit algebra, CFG loop `sync_tick` reachability analysis | M3 | Survey 2 (R3) |
| 17 | C99 Strict Compiler Fixes | Fix `-Wpedantic` function pointer cast in `native/src/wet_scheduler.c:345`; compile all 13 C files with `clang -std=c99 -Wall -Wextra -Werror -pedantic` | M4 | Survey 2 (R4) |
| 18 | Mirror Sync Restoration | Restore missing `wetlang/cli.py` and `wetlang/runtime.py` in `<WETLANG_ROOT>\wetlang/` from release mirror | M4 | Survey 2 (R4) |
| 19 | Zero-`malloc` Symbol Audit | Automated `llvm-nm` symbol audit confirming 0 dynamic heap calls (`malloc`, `calloc`, `realloc`, `free`) in deterministic tick stepping | M4 | Survey 1, 2 (R4) |
| 20 | 5-Bot Adversarial Audit Log | `docs/JANUS_ADVERSARIAL_AUDIT.md` multi-agent debate (Biophysicist, Systems Architect, Cybersecurity, Neuroengineer, Formal Verification) with 0 unresolved defects | M4 | Survey 1, 2 (R4) |
| 21 | Clean Deterministic Release Sync | Manifest-based sync to `<WETLANG_RELEASE_ROOT>` strictly excluding build caches, `.pyc`, `.wbc`, and `node_modules` | M5 | Survey 2 (R4) |
| 22 | 100% Full Verification Gate | Complete test execution in `<WETLANG_ROOT>` and `wetlang_github_release` confirming 100% pass across all 878 existing tests + new test suites | M5 | Survey 1, 2 (R4) |

---

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Closed-Loop AI Benchmark Suite | Features 1–6: `wetlang/gym.py`, `sandbox/gym_env.py`, RL & FEP DishBrain Pong/CartPole, safety coupling, FinalSpark adapter | None | DONE |
| M2 | Neuromorphic Silicon Backends | Features 7–11: `--target=loihi2` & `--target=spinnaker`, Substrate Lowering Contract, reference simulators, CLI flags | None | DONE |
| M3 | VS Code Extension & Linter | Features 12–16: `vscode-wetlang/`, 73-token TextMate grammar, token parity test, `wetlang check --format=json` static checks | None | DONE |
| M4 | 5-Bot Adversarial Audit & C99 Gate | Features 17–20: C99 `-Werror -pedantic` fix in `wet_scheduler.c`, file restoration, `llvm-nm` zero-malloc audit, `docs/JANUS_ADVERSARIAL_AUDIT.md` | M1, M2, M3 | DONE |
| M5 | Clean Release Sync & Full Verification | Features 21–22: Manifest release mirroring to `wetlang_github_release`, full 878+ test suite pass, zero regressions sign-off | M4 | DONE |

---

## Interface Contracts

### 1. Gym Environment ↔ C99 Runtime Arena
- `WetworldGymEnv.__init__` allocates static byte buffer `self._arena_buf = (ctypes.c_uint8 * arena_bytes)()`.
- Invokes `wet_create_vm_arena(ctypes.byref(self._arena_buf), arena_bytes, config)`.
- Pre-allocates `WetTelemetry` ctypes struct.
- In `step(action)`: passes pre-allocated pointer to `wet_step_tick` / `wet_run_ticks`. Zero heap `malloc`/`free` calls during stepping.

### 2. State Encoders ↔ Biophysical Safety Clamp
- In `sandbox/gym_env.py`:
  - `PongStateEncoder` / `CartPoleStateEncoder` generates stimulation parameters $(V, \tau_1, \tau_2)$.
  - Enforces $|V| \le 1.2\,\text{V}$ (hardware rail ceiling) and dynamic EIS current clamp:
    $I_{\text{safe}} = J_{\text{limit}} \times \text{Area}$, $V_{\text{safe}} = I_{\text{safe}} \times Z$.
  - Interlocks in C99 runtime track charge in 64-bit attoCoulomb accumulator; trips `ERR_DC_DRIFT` if $|Q| \ge 1.0\,\text{nC}$.

### 3. Neuromorphic Lowering ↔ Reference Simulators
- `compiler/emitter.py` lowers AST to Python script using Intel Lava or PyNN syntax.
- Emitted script uses conditional import:
  ```python
  try:
      import lava.magma.core.process.process as lava_proc
  except ImportError:
      import compiler.loihi2_ref_sim as lava_proc
  ```
  ```python
  try:
      import pyNN.spiNNaker as sim
  except ImportError:
      import compiler.spinnaker_ref_sim as sim
  ```
- Guaranteed to parse cleanly with `ast.parse` and execute deterministically on Windows.

### 4. VS Code Extension ↔ Single-Source Linter CLI
- Single-source diagnostic command:
  `wetlang check --format=json <file>`
- JSON output format:
  ```json
  [
    {
      "file": "path/to/file.wet",
      "line": 12,
      "column": 5,
      "severity": "error",
      "code": "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED",
      "message": "Requested stimulation voltage 1.500 V exceeds water window clamp limit (+/-1.2 V)"
    }
  ]
  ```
- VS Code extension reads this array and populates `vscode.DiagnosticCollection`.

---

## Code Layout
```
<WETLANG_ROOT>\
├── wetlang/
│   ├── __init__.py
│   ├── cli.py                        # Single-source CLI entry point (restored & extended with 'check')
│   ├── gym.py                        # M1: Canonical WetworldGymEnv(gymnasium.Env) with C99 arena wrapping
│   ├── runtime.py                    # Restored Python runtime wrapper
│   ├── vm.py                         # High-level VirtualMachine class
│   └── tensors.py                    # Zero-copy tensor bridge
├── sandbox/
│   ├── gym_env.py                    # M1: Reference environment & shared encoders/decoders
│   └── ...
├── benchmarks/
│   ├── run_pong_rl.py                # M1: PyTorch RL + R-STDP DishBrain Pong
│   ├── run_cartpole_rl.py            # M1: PyTorch RL + R-STDP CartPole
│   ├── run_pong_fep.py               # M1: Active Inference / FEP DishBrain Pong
│   ├── run_cartpole_fep.py           # M1: Active Inference / FEP CartPole
│   ├── finalspark_validation.py      # M1: FinalSpark E:\ recordings calibration adapter
│   └── ...
├── compiler/
│   ├── token.py                      # 73 canonical lexer tokens
│   ├── lexer.py                      # DFA lexer
│   ├── ast_nodes.py                  # AST hierarchy
│   ├── parser.py                     # Pratt parser
│   ├── semantic.py                   # M3: Single-source static checks & diagnostic collection
│   ├── compiler_cli.py               # wetc compiler CLI driver
│   ├── emitter.py                    # M2: Emitter extended with --target=loihi2 & spinnaker
│   ├── loihi2_ref_sim.py             # M2: Intel Lava pure-Python reference simulator
│   └── spinnaker_ref_sim.py          # M2: SpiNNaker PyNN pure-Python reference simulator
├── vscode-wetlang/                   # M3: Official VS Code Extension
│   ├── package.json                  # Extension manifest
│   ├── language-configuration.json   # Brackets, comments, indentation
│   ├── tsconfig.json                 # TypeScript configuration
│   ├── syntaxes/
│   │   └── wet.tmLanguage.json       # 73-token TextMate grammar
│   ├── src/
│   │   └── extension.ts              # Extension activation & linter bridge
│   └── icons/
│       └── wetlang.png               # Extension icon
├── native/
│   ├── include/                      # C99 headers
│   ├── src/
│   │   ├── wet_scheduler.c           # M4: Fixed C99 -Wpedantic CreateThread signature
│   │   └── ...
│   └── build.py
├── docs/
│   ├── JANUS_ADVERSARIAL_AUDIT.md    # M4: 5-bot cross-domain review matrix (0 unresolved defects)
│   └── ...
├── tests/                            # 878 existing tests + new test suites
│   ├── test_gym_closed_loop.py       # New M1 test suite
│   ├── test_neuromorphic_emitter.py  # New M2 test suite
│   ├── test_vscode_token_parity.py   # New M3 test suite
│   └── test_c99_zero_malloc.py       # New M4 test suite
└── wetlang_github_release/           # M5: Clean mirrored release target
```
