# Project: WetLang Neural Organoid Computing Platform

## Architecture
WetLang is a domain-specific programming language, compiler pipeline, native virtual machine runtime, in-silico biophysical digital twin, and biocybersecurity interlock system designed for neural organoid computing on Microelectrode Arrays (MEA).

### System Data Flow
```
+-----------------------------------------------------------------------------------+
| 1. WetLang Source Code (.wet)                                                     |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| 2. Compiler Pipeline (Lexer -> Pratt Parser -> Semantic Analyzer -> Emitter)      |
|    - EBNF Grammar & Tokenizer with physical unit dimensions                       |
|    - AST & Pratt Expression Climber                                               |
|    - Static Safety Verifier: CFG loop-yield post-dominance & coordinate bounds    |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| 3. WBC Bytecode Binary (.wbc)                                                     |
|    - 32-byte header (Magic 'WETB', Version, Capability Flags, CRC32)              |
|    - Section table (Constants, Topology, Code, Manifest, Debug)                  |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| 4. Native Runtime Engine (wetvm shared library / C-ABI)                           |
|    - Stack Machine Dispatcher (30+ Opcodes)                                       |
|    - Cycle-accurate VM Tick Scheduler (dt = 0.1 ms synchronization via sync_tick) |
+-----------------------------------------------------------------------------------+
                                         |
                       +-----------------+-----------------+
                       v                                   v
+---------------------------------------+ +---------------------------------------+
| 5. Cycle-Accurate Hardware Watchdog   | | 6. Biophysical Digital Twin (8x8 MEA)  |
|    - Voltage Clamp (+/- 1.2 V)        | |    - 64 Neurons (80% Exc, 20% Inh)     |
|    - 10 ms Charge Ring Buffer (<0.5nC)| |    - Exponential Euler COBA-LIF & AHP  |
|    - 50 ms Runaway Breaker (>150 Hz   | |    - Absolute (2.0 ms) & Relative Refr |
|      across > 35% channels)           | |    - Tsodyks-Markram STP & Bounded STDP|
+---------------------------------------+ +---------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| 7. Telemetry & FFI Streaming (JSONL / CSV / NumPy Zero-Copy Views via ctypes)     |
+-----------------------------------------------------------------------------------+
```

---

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Formal EBNF Grammar | Grammar with domain primitives (`grid`, `channel`, `stim_biphasic`, `read_spikes`, `modulate_stdp`, `sync_tick`, units) | M1 | Survey 1 |
| 2 | Lexer with Physical Units | DFA scanner tagging dimensions (`ms`, `us`, `V`, `mV`, `uA`, `nC`, `Hz`) and SI scaling | M1 | Survey 1 |
| 3 | Pratt Recursive-Descent Parser | Hand-crafted parser building typed AST without external parser tools | M1 | Survey 1 |
| 4 | Semantic & Scope Analyzer | 3-pass analyzer verifying variable scopes, types, MEA coordinate bounds | M1 | Survey 1 |
| 5 | Static Loop-Yield Verifier | CFG post-dominance check enforcing `sync_tick` yield in every stimulation loop | M1 | Survey 1, 3 |
| 6 | Custom Bytecode ISA | Stack machine ISA, opcode table, 32-byte header, capability bitmask | M1 | Survey 1 |
| 7 | Bytecode Binary Emitter | Serialization into `.wbc` with section table, fixup backpatching, CRC32 | M1 | Survey 1 |
| 8 | Native C-ABI VM Engine | C99/C++17 portable shared library execution engine (`wetvm`) | M2 | Survey 1 |
| 9 | VM Tick Scheduler | Cycle-accurate tick stepping at fixed $dt = 0.1\text{ ms}$ with deterministic synchronization | M2 | Survey 1 |
| 10 | Python ctypes FFI Bindings | Clean C-ABI header (`wetvm_api.h`), caller-allocates pattern, zero memory leaks | M2 | Survey 1 |
| 11 | Zero-Copy NumPy Telemetry | Pinned buffer memory mapping for high-throughput raster and voltage inspection | M2 | Survey 1 |
| 12 | 8x8 MEA Grid Topology | 64 electrodes (200 µm pitch), 3D volume conduction forward pickup, cross-talk matrix | M3 | Survey 2 |
| 13 | Numerical ODE Solver | Exact Exponential Euler integration for COBA-LIF, conductances, and traces at $dt = 0.1\text{ ms}$ | M3 | Survey 2 |
| 14 | Absolute & Relative Refractory | 2.0 ms hard clamp (20 ticks, max 500 Hz), dynamic threshold (+15 mV), slow AHP | M3 | Survey 2 |
| 15 | Tsodyks-Markram STP | 4 cortical synapse classes (E->E, E->I, I->E, I->I) with vesicle depletion & facilitation | M3 | Survey 2 |
| 16 | Pairwise Trace STDP | Online exponential trace STDP, 1.05x depression bias, hard bounds $[0, 40\text{ nS}]$, Dale's principle | M3 | Survey 2 |
| 17 | Telemetry Streaming Engine | Structured per-tick JSONL and high-throughput CSV logging ($V_m$, spikes, rates, $\Delta w$, charge) | M3 | Survey 2 |
| 18 | Static Capability Verifier | Header validation, capability bitmasks, coordinate literal checks, privilege tiers | M4 | Survey 3 |
| 19 | Water-Window Voltage Clamp | Hard clamp saturating all requested stimulation within $[-1.2\text{ V}, +1.2\text{ V}]$ | M4 | Survey 3 |
| 20 | Sliding Charge Balance Watchdog | 100-tick (10.0 ms) circular ring buffer tripping if residual charge $\ge 0.5\text{ nC}$ | M4 | Survey 3 |
| 21 | Epileptiform Runaway Breaker | 500-tick (50.0 ms) accumulator tripping `ERR_EPILEPTIFORM_RUNAWAY` if $>150\text{ Hz}$ on $>35\%$ channels | M4 | Survey 3 |
| 22 | Fail-Safe Interlock Clamp | Zeroes all stimulation DACs ($0.0\text{ V}$, $0.0\text{ A}$) and locks VM upon any safety trip | M4 | Survey 3 |
| 23 | Benchmark 01 Active Inference | Sensory-motor closed-loop tracking with reward/punishment STDP feedback | M5 | Survey 3 |
| 24 | Benchmark 02 Polychronous Reservoir | Spatio-temporal trajectory discrimination with short-term synaptic dynamics | M5 | Survey 3 |
| 25 | Benchmark 03 Homeostatic Control | Adaptive population rate regulation ($15-25\text{ Hz}$) under acute perturbation stress | M5 | Survey 3 |
| 26 | Adversarial Debate Documentation | 4 multi-round technical debates recorded in `docs/adversarial_debate.md` with formal resolutions | M5 | Survey 3 |
| 27 | Synthetic Test Suite | Diagnostics, numerical stability, fault injection, and benchmark execution in `tests/` | M5 | Survey 3 |
| 28 | Full E2E Dual-Track Verification | 100% pass of independent opaque-box E2E test suite published in `TEST_READY.md` | M6 | Survey 3 |

---

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Language Compiler Pipeline | EBNF grammar, lexer, Pratt parser, semantic analyzer, static loop verifier, WBC emitter | None | DONE |
| M2 | Native Runtime & FFI Bindings | Native shared library (`wetvm`), stack VM, cycle-accurate scheduler, Python ctypes wrapper | M1 (Bytecode Spec) | DONE |
| M3 | Biophysical Digital Twin Sandbox | 8x8 MEA, 64-neuron COBA-LIF ODE solver, 2.0 ms refractory, STP, STDP, telemetry stream | M2 (VM hooks) | DONE |
| M4 | Biocybersecurity Hardware Interlocks | Water-window clamp (+/-1.2V), 10ms charge ring buffer (<0.5nC), 50ms epileptiform breaker | M2, M3 | DONE |
| M5 | Benchmarks, Debates & Test Suite | Benchmarks 01, 02, 03; `docs/language_spec.md`, `docs/adversarial_debate.md`, `tests/` | M1, M2, M3, M4 | DONE |
| M6 | Final E2E Integration & Hardening | Pass 100% of E2E tests from E2E Testing Track (`TEST_READY.md`) + adversarial hardening | M5, TEST_READY | DONE |

---

## Interface Contracts

### 1. Compiler (M1) ↔ Native VM Loader (M2)
- **Binary Format**: `.wbc` (WetLang Bytecode)
- **Header Structure**:
  ```c
  typedef struct {
      uint8_t  magic[4];       // "WETB" (0x57, 0x45, 0x54, 0x42)
      uint16_t version_major;  // 1
      uint16_t version_minor;  // 0
      uint16_t capabilities;   // Bitmask: STIM(0x1), PLAST(0x2), LOOP(0x4), HIGH_V(0x8)
      uint32_t file_size;      // Total bytes
      uint32_t checksum_crc32; // Header + code checksum
      uint32_t num_sections;   // Count of sections
      uint32_t channel_count;  // Required MEA channels (e.g. 64)
      float    max_charge_nc;  // Static charge upper bound
      uint32_t reserved;
  } wet_bytecode_header_t;
  ```
- **Error Codes**: `ERR_INVALID_MAGIC`, `ERR_UNSUPPORTED_VERSION`, `ERR_UNBOUNDED_STIM_LOOP`, `ERR_ELECTRODE_OUT_OF_BOUNDS`.

### 2. Native VM (M2) ↔ Biophysical Sandbox (M3)
- **Simulation Time Step**: Fixed $dt = 0.1\text{ ms}$ ($100\ \mu\text{s}$).
- **Synchronization Hook**:
  - `SYNC_TICK` opcode triggers `biophysics_step_tick(biophys_state, dt)`.
  - Stimulation dispatch: `biophysics_inject_stim(biophys_state, channel, voltage_v, phase1_ms, phase2_ms)`.
  - Spike readout: `biophysics_get_spikes_window(biophys_state, channel, window_ms) -> count`.
  - STDP modulation: `biophysics_modulate_stdp(biophys_state, pre, post, delta_w)`.

### 3. Biophysical Sandbox (M3) ↔ Hardware Interlocks (M4)
- **Voltage Clamp**: Clamps $V_{stim}(e, t) = \text{clamp}(V_{req}(e, t), -1.2\text{ V}, +1.2\text{ V})$.
- **Charge Accumulator**:
  - Circular buffer per electrode: `q_ring[64][100]`.
  - Running sum: $Q_{accum}[e] = Q_{accum}[e] - q_{ring}[e][head] + q_{tick}[e]$.
  - Trip condition: If $|Q_{accum}[e]| \ge 0.5\text{ nC}$, return `ERR_CHARGE_IMBALANCE`.
- **Epileptiform Runaway Breaker**:
  - Sustained counter for hyperactive channels ($f_e \ge 150\text{ Hz}$).
  - Trip condition: If $N_{hyper} \ge 23$ ($>35\%$ of 64) for $500\text{ consecutive ticks}$ ($50.0\text{ ms}$), return `ERR_EPILEPTIFORM_RUNAWAY`.
  - Immediate action: Zero all stimulation DACs, set fail-safe state, lock VM.

### 4. Native Engine (M2) ↔ Python FFI (`wetvm_ffi.py`)
- **C-ABI Header**: `wetvm_api.h`
- **Functions**:
  - `wet_vm_t* wet_create_vm(const wet_vm_config_t* config)`
  - `wet_status_t wet_load_bytecode(wet_vm_t* vm, const uint8_t* code, size_t len, char* err, size_t err_len)`
  - `wet_status_t wet_step_tick(wet_vm_t* vm, wet_telemetry_t* out_telem)`
  - `wet_status_t wet_run_ticks(wet_vm_t* vm, uint32_t ticks, uint32_t* executed, wet_telemetry_t* out_telem)`
  - `void wet_free_vm(wet_vm_t* vm)`
- **Memory Convention**: Caller-allocates `wet_telemetry_t`, callee-populates; zero-copy NumPy views for channel voltages and spike rasters.

---

## Code Layout
```
d:\New research\wetworld_language\
├── compiler/                     # M1: WetLang Compiler from Scratch
│   ├── __init__.py
│   ├── token.py                  # Token types & physical unit tags
│   ├── lexer.py                  # DFA lexical scanner
│   ├── ast_nodes.py              # AST hierarchy & visitor interfaces
│   ├── parser.py                 # Recursive-descent Pratt parser
│   ├── semantic.py               # Scope analysis, type checking & loop-yield verifier
│   ├── isa.py                    # Opcode definitions & WBC binary header format
│   ├── emitter.py                # WBC bytecode binary serializer
│   └── compiler_cli.py           # CLI entry point for compiling .wet to .wbc
├── native/                       # M2 & M3 & M4: Native C99/C++17 Engine
│   ├── include/
│   │   ├── wetvm_api.h           # Public C-ABI exports & telemetry structs
│   │   ├── wetvm_types.h         # Bytecode definitions, opcodes, error codes
│   │   ├── wetvm_vm.h            # Stack machine, local frames, tick scheduler
│   │   ├── biophysics.h          # 64-neuron COBA-LIF, 8x8 MEA, STP, STDP
│   │   └── interlocks.h          # Voltage clamp, charge ring buffer, runaway breaker
│   ├── src/
│   │   ├── wetvm_api.c           # C-ABI implementation
│   │   ├── wetvm_vm.c            # Stack machine dispatcher & scheduler
│   │   ├── biophysics.c          # Numerical ODE solver, STP, STDP, volume conduction
│   │   └── interlocks.c          # Cycle-accurate hardware watchdog & fail-safe clamps
│   ├── build.py                  # Portable C compiler builder (MSVC / GCC / Clang / TinyCC)
│   └── Makefile                  # Standard POSIX / MinGW build script
├── bindings/                     # M2: Python ctypes FFI Wrapper
│   ├── __init__.py
│   ├── ffi.py                    # ctypes bindings to wetvm shared library
│   └── runtime.py                # High-level Python execution & stepping API
├── biophysics/                   # M3: Telemetry, Geometry & Reference Engine
│   ├── __init__.py
│   ├── mea_grid.py               # 8x8 MEA spatial mapping & volume conduction kernel
│   └── telemetry.py              # Structured JSONL / CSV streaming & parser
├── benchmarks/                   # M5: Complex Closed-Loop WetLang Benchmark Programs
│   ├── 01_active_inference_closed_loop.wet
│   ├── 02_polychronous_reservoir_classifier.wet
│   └── 03_homeostatic_stabilization_and_stress.wet
├── docs/                         # M5: Technical Documentation & Multi-Agent Debates
│   ├── language_spec.md          # EBNF grammar, ISA table, timing model, primitives
│   └── adversarial_debate.md     # 4 multi-round technical debates with resolutions
└── tests/                        # M5 & Dual Track: Comprehensive Test Suites
    ├── test_parser_diagnostics.py# Syntax, invalid bytecode, opcode tiers
    ├── test_static_verifier.py   # Bounds check, un-yielded loop rejection
    ├── test_ode_stability.py     # Extreme current injection, 2.0 ms refractory, STDP clamp
    ├── test_interlocks.py        # Voltage clamp, 10ms charge balance trip, runaway breaker
    └── test_benchmarks.py        # End-to-end execution of benchmarks 01, 02, 03
```
