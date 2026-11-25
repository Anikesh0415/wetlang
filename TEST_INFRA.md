# E2E Test Infra: WetLang Neural Organoid Platform & Project Janus

## Test Philosophy
- **Opaque-box & Requirement-driven**: All tests are derived directly from `ORIGINAL_REQUEST.md` and user-facing specifications in `PROJECT.md`. Tests do not inspect or depend on internal private data structures or unexported symbols.
- **Progressive Testability**: Verification does not require features more complex than the tested feature. Tier 1 unit and compiler tests pass on early compiler builds; biophysical ODE tests run on numerical solver routines; full closed-loop benchmarks run on the integrated runtime. As new milestone components are created, tests automatically activate and assert specifications.
- **Methodology**: 4-tier systematic testing architecture:
  - **Tier 1 - Feature Coverage**: Category-Partition methodology. Isolated happy-path equivalence class tests across all features in `PROJECT.md`.
  - **Tier 2 - Boundary & Corner Cases**: Boundary Value Analysis (BVA). Tests for zero/negative, max bounds, extreme conductances, +/-1.2V voltage clamps, 0.5 nC charge limits, dynamic EIS current density clamps, substrate lowering warnings, and linter error codes.
  - **Tier 3 - Cross-Feature Combinations**: Pairwise Combinatorial Testing across compiler, VM, biophysics, interlocks, neuromorphic silicon backends, and IDE extension diagnostic pipelines.
  - **Tier 4 - Real-World Application Scenarios**: Closed-loop benchmarks and realistic operational workloads in neural organoid computation (DishBrain Pong, CartPole, FinalSpark calibration adapter, dual neuromorphic hardware lowering).

---

## Feature Inventory & Test Matrix

### Core Platform Features (Features 1–28)
| # | Feature | Source (Requirement) | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---------|---------------------|:------:|:------:|:------:|:------:|
| 1 | Formal EBNF Grammar | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | ✓ |
| 2 | Lexer with Physical Units | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | ✓ |
| 3 | Pratt Recursive-Descent Parser | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | ✓ |
| 4 | Semantic & Scope Analyzer | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | ✓ |
| 5 | Static Loop-Yield Verifier | ORIGINAL_REQUEST §R1, §R3 | 5 | 5 | ✓ | ✓ |
| 6 | Custom Bytecode ISA | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | ✓ |
| 7 | Bytecode Binary Emitter | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | ✓ |
| 8 | Native C-ABI VM Engine | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | ✓ |
| 9 | VM Tick Scheduler | ORIGINAL_REQUEST §R1, §R2 | 5 | 5 | ✓ | ✓ |
| 10 | Python ctypes FFI Bindings | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | ✓ |
| 11 | Zero-Copy NumPy Telemetry | ORIGINAL_REQUEST §R1, §R2 | 5 | 5 | ✓ | ✓ |
| 12 | 8x8 MEA Grid Topology | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | ✓ |
| 13 | Numerical ODE Solver | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | ✓ |
| 14 | Absolute & Relative Refractory | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | ✓ |
| 15 | Tsodyks-Markram STP | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | ✓ |
| 16 | Pairwise Trace STDP | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | ✓ |
| 17 | Telemetry Streaming Engine | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | ✓ |
| 18 | Static Capability Verifier | ORIGINAL_REQUEST §R3 | 5 | 5 | ✓ | ✓ |
| 19 | Water-Window Voltage Clamp | ORIGINAL_REQUEST §R3 | 5 | 5 | ✓ | ✓ |
| 20 | Sliding Charge Balance Watchdog | ORIGINAL_REQUEST §R3 | 5 | 5 | ✓ | ✓ |
| 21 | Epileptiform Runaway Breaker | ORIGINAL_REQUEST §R3 | 5 | 5 | ✓ | ✓ |
| 22 | Fail-Safe Interlock Clamp | ORIGINAL_REQUEST §R3 | 5 | 5 | ✓ | ✓ |
| 23 | Benchmark 01 Active Inference | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ | ✓ |
| 24 | Benchmark 02 Polychronous Reservoir | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ | ✓ |
| 25 | Benchmark 03 Homeostatic Control | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ | ✓ |
| 26 | Adversarial Debate Documentation | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ | - |
| 27 | Synthetic Test Suite | ORIGINAL_REQUEST Acceptance | 5 | 5 | ✓ | ✓ |
| 28 | Full E2E Dual-Track Verification | ORIGINAL_REQUEST Acceptance | 5 | 5 | ✓ | ✓ |

### Project Janus Extension Features (Options 1, 3, 4 & C99 Safety)
| # | Feature | Subsystem | Scope | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---------|-----------|-------|:------:|:------:|:------:|:------:|
| 29 | Canonical `WetworldGymEnv` | Option 1 (AI Benchmarks) | `wetlang.gym`: Box(128) obs, Box(4) action, C99 pre-allocated arena wrapping, zero heap allocations in `step()` | ✓ | ✓ | ✓ | ✓ |
| 30 | Shared State Encoders & Decoders | Option 1 (AI Benchmarks) | `sandbox/gym_env.py`: `PongStateEncoder`, `CartPoleStateEncoder`, `MotorSpikeDecoder` with +/-1.2V clamp & dynamic EIS clamp | ✓ | ✓ | ✓ | ✓ |
| 31 | Dual Learning Paradigms (RL & FEP) | Option 1 (AI Benchmarks) | `benchmarks/run_*`: PyTorch policy net with R-STDP and Karl Friston Active Inference entropy minimization baselines | ✓ | ✓ | ✓ | ✓ |
| 32 | FinalSpark Empirical Calibration Adapter | Option 1 (AI Benchmarks) | `benchmarks/finalspark_validation.py`: Ingests `E:\data\fs369\fs369data` (or graceful CI fallback) to validate firing rates, ISI CV, burst fraction | ✓ | ✓ | ✓ | ✓ |
| 33 | Intel Loihi-2 Lava Emitter | Option 3 (Neuromorphic) | `compiler/emitter.py` (`--target=loihi2`): Emits valid Intel Lava `AbstractProcess` and `PyLoihiProcessModel`, passes `ast.parse` | ✓ | ✓ | ✓ | ✓ |
| 34 | SpiNNaker PyNN Emitter | Option 3 (Neuromorphic) | `compiler/emitter.py` (`--target=spinnaker`): Emits executable `pyNN.spiNNaker` scripts, passes `ast.parse` | ✓ | ✓ | ✓ | ✓ |
| 35 | Substrate Lowering Contract | Option 3 (Neuromorphic) | Emits structured compiler warning `W_SUBSTRATE_UNSUPPORTED_OP` and safe comments/no-ops for wetware-only primitives without crashing | ✓ | ✓ | ✓ | ✓ |
| 36 | In-Repo Deterministic Reference Simulators | Option 3 (Neuromorphic) | `compiler/loihi2_ref_sim.py` and `compiler/spinnaker_ref_sim.py`: pure-Python reference execution engines | ✓ | ✓ | ✓ | ✓ |
| 37 | VS Code Extension Scaffolding | Option 4 (VS Code & Linter) | `vscode-wetlang/`: `package.json`, `language-configuration.json`, `syntaxes/wet.tmLanguage.json`, `src/extension.ts` | ✓ | ✓ | ✓ | ✓ |
| 38 | 73-Token TextMate Grammar Parity | Option 4 (VS Code & Linter) | `vscode-wetlang/syntaxes/wet.tmLanguage.json` covers all 73 canonical lexer token types from `compiler.token.TokenType` | ✓ | ✓ | ✓ | ✓ |
| 39 | Single-Source Diagnostic Linter CLI | Option 4 (VS Code & Linter) | `wetlang check --format=json <file>`: Flags compile-time overvoltage, SI dimensional mismatches, and unbounded stim loops | ✓ | ✓ | ✓ | ✓ |
| 40 | C99 Deterministic Stepping & Arena Gate | C99 & Safety Invariants | MISRA-C arena allocation (`wet_create_vm_arena`), bit-identical tick stepping, zero runtime `malloc`/`free` | ✓ | ✓ | ✓ | ✓ |

---

## Test Architecture

### Test Suites Layout
- Core Platform Suites:
  - `tests/e2e/test_tier1_features.py`: >=140 feature coverage tests.
  - `tests/e2e/test_tier2_boundaries.py`: >=140 boundary and safety corner tests.
  - `tests/e2e/test_tier3_pairwise.py`: >=28 pairwise combination tests.
  - `tests/e2e/test_tier4_benchmarks.py`: >=5 realistic workload / benchmark tests.
- Project Janus E2E Suite:
  - `tests/e2e/test_janus_options_e2e.py`: Complete opaque-box, requirement-driven 4-tier verification suite covering Options 1, 3, 4, and C99 Safety Invariants.

### Project Janus 4-Tier Test Breakdown (`test_janus_options_e2e.py`)
1. **Tier 1 - Feature Coverage (Happy Path & Conformance)**:
   - `WetworldGymEnv` canonical export, `make()` factory, Box(128) observation space, Box(4) action space, reset and sequential stepping.
   - `PongStateEncoder`, `CartPoleStateEncoder`, and `MotorSpikeDecoder` instantiation and state encoding.
   - `finalspark_validation.py` execution with empirical dataset or graceful CI fallback.
   - Intel Loihi-2 `--target=loihi2` codegen, `ast.parse` validation, Lava class emissions (`AbstractProcess`, `PyLoihiProcessModel`), and reference simulator execution.
   - SpiNNaker `--target=spinnaker` codegen, `ast.parse` validation, `pyNN.spiNNaker` emission, and reference simulator execution.
   - VS Code extension manifests (`package.json`, `language-configuration.json`, `syntaxes/wet.tmLanguage.json`, `src/extension.ts`).
   - 73-token parity validation between `compiler.token.TokenType` and `syntaxes/wet.tmLanguage.json`.
   - Single-source linter CLI JSON interface (`wetlang check --format=json`).
   - C99 deterministic tick stepping and pre-allocated arena VM creation.

2. **Tier 2 - Boundary Value Analysis & Safety Invariants**:
   - Biophysical voltage clamp upper rail (+1.2 V water window ceiling) on encoders.
   - Biophysical voltage clamp lower rail (-1.2 V water window floor) on encoders.
   - Dynamic EIS current density clamp ($I_{\text{safe}} = J_{\text{limit}} \times \text{Area}$, $V_{\text{safe}} = I_{\text{safe}} \times Z$).
   - Gymnasium action clipping with extreme out-of-bounds action vectors.
   - Substrate Lowering Contract: `W_SUBSTRATE_UNSUPPORTED_OP` warnings emitted for wetware-only primitives (microfluidics, EIS, water window) on Loihi-2 and SpiNNaker targets without compiler crash.
   - Safe comment and no-op emission for lowered wetware primitives.
   - Static linter overvoltage detection (`ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED`).
   - Static linter dimensional algebra mismatch detection (`ERR_DIMENSIONAL_MISMATCH`).
   - Static linter CFG unbounded stim loop detection (`ERR_UNBOUNDED_STIM_LOOP`).
   - Native C99 hardware rail clamping verification via C-ABI (`wet_clamp_voltage_vm` and `wet_clamp_voltage_dynamic_vm`).

3. **Tier 3 - Pairwise Cross-Feature Combinations**:
   - Closed-loop Gym encoder-to-arena pipeline: game state encoded -> action stepped -> observation streamed.
   - Neuromorphic dual-target AST equivalence: single circuit lowered to both Lava and PyNN with consistent topology.
   - Linter CLI file roundtrip: valid `.wet` yields 0 diagnostics, invalid `.wet` yields structured JSON diagnostics.
   - C99 arena stepping under rapid stimulation pulse trains without memory growth.

4. **Tier 4 - Real-World Application Scenarios**:
   - Scenario 1: Closed-loop DishBrain sensory-motor game loop (multi-step closed-loop episode with sensory stimulation, motor spike decoding, and reward calculation).
   - Scenario 2: FinalSpark empirical recording calibration pipeline (baseline firing rate, ISI CV, burst fraction verification against empirical organoid bounds).
   - Scenario 3: Multi-target dual-substrate workflow (compiling a single biophysical model to WBC bytecode, Loihi-2 Lava, and SpiNNaker PyNN).

---

## Test Execution Commands

```bash
# Run the Project Janus Options 1, 3, 4 E2E test suite
pytest tests/e2e/test_janus_options_e2e.py -v

# Run the complete test suite across all subsystems
pytest tests/ -v

# Run standalone E2E runner
python tests/run_e2e_tests.py
```

## Pass/Fail Semantics
- Deterministic assertions on return codes, error codes, structured JSON diagnostics, telemetry records, and safety clamp values.
- Infallible test execution: no unhandled exceptions, syntax errors, or segmentation faults.
- 100% pass rate requirement across all existing 878 tests plus new test suites.
