# E2E Test Infra: WetLang Neural Organoid Platform

## Test Philosophy
- **Opaque-box & Requirement-driven**: All tests are derived directly from `ORIGINAL_REQUEST.md` and user-facing specifications in `PROJECT.md`. Tests do not inspect or depend on internal private data structures or unexported symbols.
- **Progressive Testability**: Verification does not require features more complex than the tested feature. Tier 1 unit and compiler tests can pass on early compiler builds; biophysical ODE tests can run on numerical solver routines; full closed-loop benchmarks run on the integrated runtime.
- **Methodology**: 4-tier systematic testing architecture:
  - **Tier 1 - Feature Coverage**: Category-Partition methodology. >=5 isolated happy-path equivalence class tests per feature across all 28 features in `PROJECT.md` (Total >= 140 tests).
  - **Tier 2 - Boundary & Corner Cases**: Boundary Value Analysis (BVA). >=5 tests per feature for zero/negative, max bounds, extreme conductances, +/-1.2V voltage clamps, 0.5 nC charge limits, 150 Hz / 35% / 50ms epileptiform runaway, 2.0 ms refractory period (Total >= 140 tests).
  - **Tier 3 - Cross-Feature Combinations**: Pairwise Combinatorial Testing across compiler, VM, biophysics, and interlocks (Total >= 28 tests).
  - **Tier 4 - Real-World Application Scenarios**: Closed-loop benchmarks and realistic operational workloads in neural organoid computation (Total >= 5 scenarios).

## Feature Inventory & Test Matrix
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

## Test Architecture
- **Location**: All E2E test suites reside in `tests/e2e/`:
  - `tests/e2e/test_tier1_features.py`: >=140 feature coverage tests.
  - `tests/e2e/test_tier2_boundaries.py`: >=140 boundary and safety corner tests.
  - `tests/e2e/test_tier3_pairwise.py`: >=28 pairwise combination tests.
  - `tests/e2e/test_tier4_benchmarks.py`: >=5 realistic workload / benchmark tests.
- **Test Runner**:
  - Standalone script: `python tests/run_e2e_tests.py` (exits 0 on all passed, non-zero on failure).
  - Also compatible with standard pytest: `pytest tests/e2e/ -v`.
- **Pass/Fail Semantics**:
  - Deterministic assertions on return codes, error enum strings, telemetry records, and safety trips.
  - Infallible test execution: no unhandled exceptions or crashes.

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Complexity |
|---|----------|--------------------|------------|
| 1 | Active Inference Sensory-Motor Learning Loop | F1, F2, F3, F4, F5, F8, F9, F12, F13, F14, F15, F16, F17, F23 | High |
| 2 | Polychronous Wavefront Discrimination in Recurrent Reservoir | F1, F3, F6, F7, F8, F9, F12, F14, F15, F24 | High |
| 3 | Homeostatic Rate Stabilization under Acute Perturbation Bursts | F1, F4, F8, F9, F12, F13, F14, F19, F20, F21, F22, F25 | High |
| 4 | Adversarial Injection of High-Frequency Voltage Pulses | F5, F7, F8, F18, F19, F20, F21, F22 | High |
| 5 | Long-Horizon Deterministic Telemetry & FFI Stream Integrity | F8, F9, F10, F11, F17, F28 | Medium |

## Coverage Thresholds
- Tier 1: >=5 tests per feature (minimum 140 tests)
- Tier 2: >=5 boundary tests per feature (minimum 140 tests)
- Tier 3: >=28 pairwise interaction tests
- Tier 4: >=5 realistic closed-loop application scenarios
- **Total Minimum Test Count: >= 313 test cases**
