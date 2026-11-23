# WetLang Language Specification & Custom Bytecode ISA

**Version:** 1.0.0  
**Status:** Stable / Normative  
**Target Architecture:** Neural Organoid Computing & Microelectrode Array (MEA) Interfacing  

---

## 1. Overview & Architectural Scope

WetLang is a domain-specific programming language, compiler pipeline, and native virtual machine architecture designed specifically for in-vitro neural organoid computing, closed-loop electrophysiology, and biocybersecurity interlock enforcement on Microelectrode Arrays (MEA).

In wetware computing systems, standard general-purpose computing paradigms fail due to three core realities:
1. **Electrochemical Fragility**: Continuous direct-current injection causes irreversible electrode degradation and electrochemical water hydrolysis (water-window lysis outside $[-1.2\text{ V}, +1.2\text{ V}]$).
2. **Biological Non-Determinism & Plasticity**: Neural tissue adapts to stimuli via complex activity-dependent plasticity mechanisms (Tsodyks-Markram short-term plasticity and Spike-Timing-Dependent Plasticity).
3. **Hard Real-Time Biophysical Deadlines**: Organoid neural dynamics unfold on microsecond timescales; simulation and stimulation loops must synchronize deterministically with a fixed integration timestep ($dt = 0.1\text{ ms} = 100\ \mu\text{s}$).

WetLang addresses these challenges through a language design combining:
- First-class physical dimensional types (`ms`, `us`, `V`, `mV`, `uA`, `nC`, `Hz`).
- Explicit MEA topology declarations (`grid`, `channel`).
- Native biophysical primitives (`stim_biphasic`, `read_spikes`, `modulate_stdp`, `sync_tick`).
- Static loop-yield verification (enforcing cycle synchronization in all stimulation loops).
- A 32-byte hardened bytecode binary header (WBC) with CRC-32 checksums and capability bitmask validation.

---

## 2. Formal EBNF Grammar

The grammar of WetLang is defined below in standard ISO/IEC 14977 Extended Backus-Naur Form (EBNF).

### 2.1 Lexical Grammar

```ebnf
(* Whitespace and Comments *)
Whitespace          = { " " | "\t" | "\r" | "\n" } ;
SingleLineComment   = "//" , { all_characters - "\n" } , [ "\n" ] ;
MultiLineComment    = "/*" , { all_characters - "*/" } , "*/" ;

(* Identifiers and Literals *)
Letter              = "A" .. "Z" | "a" .. "z" | "_" ;
Digit               = "0" .. "9" ;
NonZeroDigit        = "1" .. "9" ;
Identifier          = Letter , { Letter | Digit } ;

IntegerLiteral      = "0" | NonZeroDigit , { Digit } ;
FloatLiteral        = Digit , { Digit } , "." , Digit , { Digit } , [ ( "e" | "E" ) , [ "+" | "-" ] , Digit , { Digit } ] ;
BooleanLiteral      = "true" | "false" ;
StringLiteral       = '"' , { all_characters - ( '"' | "\\" ) | ( "\\" , all_characters ) } , '"' ;

(* Physical Units and Dimensions *)
TimeUnit            = "s" | "ms" | "us" ;
VoltageUnit         = "V" | "mV" | "uV" ;
CurrentUnit         = "A" | "uA" | "nA" | "pA" ;
ChargeUnit          = "C" | "nC" | "pC" ;
FrequencyUnit       = "Hz" ;
LengthUnit          = "mm" | "um" ;

PhysicalUnit        = TimeUnit | VoltageUnit | CurrentUnit | ChargeUnit | FrequencyUnit | LengthUnit ;
PhysicalLiteral     = ( IntegerLiteral | FloatLiteral ) , PhysicalUnit ;
```

### 2.2 Physical Units & SI Dimension Scaling

WetLang natively resolves physical literals at compile time into their corresponding SI base units while maintaining dimensional type tags:

| Dimension | Suffix | SI Base Unit | Scale Factor to SI Base | Example Token | Internal SI Value |
|-----------|--------|--------------|-------------------------|---------------|-------------------|
| `TIME` | `s` | Second ($\text{s}$) | $1.0$ | `1s` | $1.0\text{ s}$ |
| `TIME` | `ms` | Second ($\text{s}$) | $10^{-3}$ | `0.1ms` | $0.0001\text{ s}$ |
| `TIME` | `us` | Second ($\text{s}$) | $10^{-6}$ | `200us` | $0.0002\text{ s}$ |
| `VOLTAGE` | `V` | Volt ($\text{V}$) | $1.0$ | `0.8V` | $0.8\text{ V}$ |
| `VOLTAGE` | `mV` | Volt ($\text{V}$) | $10^{-3}$ | `-70mV` | $-0.07\text{ V}$ |
| `VOLTAGE` | `uV` | Volt ($\text{V}$) | $10^{-6}$ | `50uV` | $0.00005\text{ V}$ |
| `CURRENT` | `A` | Ampere ($\text{A}$) | $1.0$ | `1A` | $1.0\text{ A}$ |
| `CURRENT` | `uA` | Ampere ($\text{A}$) | $10^{-6}$ | `10uA` | $10^{-5}\text{ A}$ |
| `CURRENT` | `nA` | Ampere ($\text{A}$) | $10^{-9}$ | `5nA` | $5 \times 10^{-9}\text{ A}$ |
| `CURRENT` | `pA` | Ampere ($\text{A}$) | $10^{-12}$ | `200pA` | $2 \times 10^{-10}\text{ A}$ |
| `CHARGE` | `C` | Coulomb ($\text{C}$) | $1.0$ | `1C` | $1.0\text{ C}$ |
| `CHARGE` | `nC` | Coulomb ($\text{C}$) | $10^{-9}$ | `0.5nC` | $5 \times 10^{-10}\text{ C}$ |
| `CHARGE` | `pC` | Coulomb ($\text{C}$) | $10^{-12}$ | `100pC` | $10^{-10}\text{ C}$ |
| `FREQUENCY`| `Hz` | Hertz ($\text{s}^{-1}$) | $1.0$ | `150Hz` | $150.0\text{ Hz}$ |
| `LENGTH` | `mm` | Meter ($\text{m}$) | $10^{-3}$ | `1mm` | $0.001\text{ m}$ |
| `LENGTH` | `um` | Meter ($\text{m}$) | $10^{-6}$ | `200um` | $0.0002\text{ m}$ |

**Dimensional Typing Rules:**
- $A + B$ and $A - B$ require $\text{dim}(A) == \text{dim}(B)$.
- $A \times B$: $\text{CURRENT} \times \text{TIME} \rightarrow \text{CHARGE}$ ($I \cdot t = Q$).
- $A / B$: $\text{CHARGE} / \text{TIME} \rightarrow \text{CURRENT}$ ($Q / t = I$).
- Comparison ($<, \le, >, \ge, ==, !=$): Operands must share the identical dimension.

### 2.3 Syntactic Grammar

```ebnf
Program             = { TopLevelDeclaration } , EOF ;

TopLevelDeclaration = GridDeclaration
                    | ChannelDeclaration
                    | FunctionDeclaration
                    | StreamDeclaration
                    | Statement ;

(* MEA Grid & Channel Declarations *)
GridDeclaration     = "grid" , Identifier , ( GridDimensions | GridBlock ) ;
GridDimensions      = "[" , Expression , [ "," , Expression ] , "]" , ";" ;
GridBlock           = "{" , { GridProperty } , "}" ;
GridProperty        = Identifier , ":" , Expression , ";" ;

ChannelDeclaration  = "channel" , Identifier , "=" , Expression , [ ChannelModeClause ] , ";" ;
ChannelModeClause   = "mode" , ":" , ChannelMode ;
ChannelMode         = "BiphasicStim" | "SpikeReadout" | "VoltageSense" | "Bidirectional" | Identifier ;

(* Functions and Streams *)
FunctionDeclaration = "fn" , Identifier , "(" , [ ParameterList ] , ")" , [ "->" , TypeName ] , Block ;
ParameterList       = Parameter , { "," , Parameter } ;
Parameter           = Identifier , ":" , TypeName ;

StreamDeclaration   = "stream" , Identifier , "{" , { StreamItem } , "}" ;
StreamItem          = BindStatement | CycleStatement ;
BindStatement       = "bind" , Identifier , ( "->" | "<-" ) , Identifier , ";" ;
CycleStatement      = "cycle" , Block ;

(* Type System *)
TypeName            = PrimitiveType | PhysicalType | Identifier ;
PrimitiveType       = "int" | "float" | "bool" | "string" | "channel" | "grid" ;
PhysicalType        = "Voltage" | "Current" | "Time" | "Frequency" | "Length" | "Charge" ;

(* Statements *)
Statement           = Block
                    | LetStatement
                    | TypedVarDeclaration
                    | StimStatement
                    | ModulateStatement
                    | SyncTickStatement
                    | IfStatement
                    | WhileStatement
                    | ForStatement
                    | ReturnStatement
                    | AssignOrExprStatement ;

Block               = "{" , { Statement } , "}" ;

LetStatement        = "let" , [ "mut" ] , Identifier , [ ":" , TypeName ] , "=" , Expression , ";" ;
TypedVarDeclaration = ( PrimitiveType | PhysicalType ) , Identifier , [ "=" , Expression ] , ";" ;

StimStatement       = "stim_biphasic" , "(" , Expression , "," , Expression , "," , Expression , "," , Expression , ")" , ";" ;
ModulateStatement   = "modulate_stdp" , "(" , Expression , "," , Expression , "," , Expression , ")" , ";" ;
SyncTickStatement   = "sync_tick" , [ "(" , ")" ] , ";" ;

IfStatement         = "if" , "(" , Expression , ")" , Statement , [ "else" , Statement ] ;
WhileStatement      = "while" , "(" , Expression , ")" , Statement ;
ForStatement        = "for" , Identifier , "in" , Expression , ".." , Expression , Statement ;
ReturnStatement     = "return" , [ Expression ] , ";" ;
AssignOrExprStatement = Expression , [ "=" , Expression ] , ";" ;

(* Pratt Expression Precedence Hierarchy *)
Expression          = LogicalOrExpr ;
LogicalOrExpr       = LogicalAndExpr , { "||" , LogicalAndExpr } ;
LogicalAndExpr      = EqualityExpr , { "&&" , EqualityExpr } ;
EqualityExpr        = RelationalExpr , { ( "==" | "!=" ) , RelationalExpr } ;
RelationalExpr      = AdditiveExpr , { ( "<" | "<=" | ">" | ">=" ) , AdditiveExpr } ;
AdditiveExpr        = MultiplicativeExpr , { ( "+" | "-" ) , MultiplicativeExpr } ;
MultiplicativeExpr  = UnaryExpr , { ( "*" | "/" | "%" ) , UnaryExpr } ;
UnaryExpr           = ( "-" | "!" ) , UnaryExpr | PostfixExpr ;

PostfixExpr         = PrimaryExpr , { CallSuffix | IndexSuffix } ;
CallSuffix          = "(" , [ ArgumentList ] , ")" ;
IndexSuffix         = "[" , Expression , [ "," , Expression ] , "]" ;
ArgumentList        = Expression , { "," , Expression } ;

PrimaryExpr         = IntegerLiteral
                    | FloatLiteral
                    | BooleanLiteral
                    | StringLiteral
                    | PhysicalLiteral
                    | DomainCall
                    | Identifier
                    | "(" , Expression , ")" ;

DomainCall          = ReadSpikesCall
                    | ReadVoltageCall
                    | PopFiringRateCall ;

ReadSpikesCall      = "read_spikes" , "(" , Expression , [ "," , Expression ] , ")" ;
ReadVoltageCall     = "read_voltage" , "(" , Expression , ")" ;
PopFiringRateCall   = ( "pop_firing_rate" | "read_population_rate" ) , "(" , ")" ;
```

---

## 3. Custom Bytecode Instruction Set Architecture (ISA)

The WetLang Virtual Machine operates as a deterministic, stack-based bytecode execution engine. Compiled binaries use the `.wbc` (WetLang Bytecode) format.

### 3.1 32-Byte Binary Header (`wet_bytecode_header_t`)

Every valid `.wbc` binary begins with a fixed 32-byte header with little-endian encoding:

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Magic: "WETB"                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Version Major | Version Minor |       Capability Bitmask      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                          File Size                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Checksum CRC-32                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Num Sections                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Channel Count                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                         Max Charge nC                         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                           Reserved                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Field Name | Byte Offset | Type | Format | Semantics |
|------------|-------------|------|--------|-----------|
| `magic` | `0x00 - 0x03` | `uint8_t[4]` | ASCII | Magic string: `"WETB"` (`0x57, 0x45, 0x54, 0x42`) |
| `version_major`| `0x04` | `uint8_t` | unsigned | Bytecode major version (currently `1`) |
| `version_minor`| `0x05` | `uint8_t` | unsigned | Bytecode minor version (currently `0`) |
| `capabilities` | `0x06 - 0x07` | `uint16_t` | bitmask | Authorized hardware capability flags |
| `file_size` | `0x08 - 0x0B` | `uint32_t` | little-endian | Total binary file size in bytes |
| `checksum_crc32`| `0x0C - 0x0F`| `uint32_t` | little-endian | IEEE 802.3 CRC-32 over header (with CRC=0) and all sections |
| `num_sections` | `0x10 - 0x13` | `uint32_t` | little-endian | Total count of section table entries |
| `channel_count`| `0x14 - 0x17` | `uint32_t` | little-endian | Number of MEA channels required (e.g., 64) |
| `max_charge_nc`| `0x18 - 0x1B` | `float32` | IEEE 754 | Static maximum charge limit per electrode (default 0.5 nC) |
| `reserved` | `0x1C - 0x1F` | `uint32_t` | 0 | Reserved padding for 64-bit alignment |

### 3.2 Capability Bitmask Flags

Capability flags determine which instruction classes are authorized at load-time and runtime:

| Flag Name | Value | Bit | Description |
|-----------|-------|-----|-------------|
| `CAP_NONE` | `0x0000` | None | Pure compute only (no I/O or stimulation) |
| `CAP_STIMULATION` | `0x0001` | Bit 0 | Authorizes `STIM_BIPHASIC` opcodes $\le 0.8\text{ V}$ |
| `CAP_PLASTICITY` | `0x0002` | Bit 1 | Authorizes `MODULATE_STDP` synaptic updates |
| `CAP_CLOSED_LOOP` | `0x0004` | Bit 2 | Authorizes autonomous `STREAM` feedback cycles |
| `CAP_HIGH_VOLTAGE`| `0x0008` | Bit 3 | Permits stimulation in elevated range $(0.8\text{ V}, 1.2\text{ V}]$ |
| `CAP_MULTI_ELECTRODE`| `0x0010`| Bit 4 | Permits concurrent stimulation across $>16$ electrodes |

### 3.3 Section Table Format

Directly following the 32-byte header is the Section Table. Each entry occupies 12 bytes (`<HHII`):

```c
typedef struct {
    uint16_t section_type;  // 1: CONSTANT_POOL, 2: TOPOLOGY, 3: BYTECODE, 4: MANIFEST, 5: DEBUG
    uint16_t reserved;      // 0
    uint32_t offset;        // Absolute byte offset in .wbc file
    uint32_t size;          // Byte length of section payload
} wet_section_entry_t;
```

Sections:
1. `WET_SEC_CONSTANT_POOL` (`0x0001`): Deduplicated strings, physical scalars, double-precision constants.
2. `WET_SEC_TOPOLOGY_CONFIG` (`0x0002`): Grid row/col dimensions, electrode mode table, pitch metrics.
3. `WET_SEC_BYTECODE_STREAM` (`0x0003`): Serialized stack VM opcode stream.
4. `WET_SEC_SAFETY_MANIFEST` (`0x0004`): Static analysis bounds, coordinate literals, max voltage declarations.
5. `WET_SEC_DEBUG_LINE_MAP` (`0x0005`): Bytecode offset to source file line/column mappings.

### 3.4 Opcode Table (34 Core Instructions)

The instruction set contains 34 opcodes spanning Control, Stack Manipulation, Arithmetic, Comparison, Control Flow, and MEA Biophysical Primitives:

| Opcode (Hex) | Mnemonic | Operand Format | Stack Effect | Description |
|--------------|----------|----------------|--------------|-------------|
| **Control Operations** | | | | |
| `0x00` | `NOP` | (none) | `[] -> []` | No operation. |
| `0x01` | `HALT` | (none) | `[] -> []` | Terminates VM execution cleanly; sets halted status. |
| `0x02` | `SYNC_TICK` | (none) | `[] -> []` | Cycle synchronization barrier: yields VM to biophysical ODE solver. |
| `0x03` | `SLEEP_TICKS` | `<H` (uint16) | `[] -> []` | Yields execution for $N$ consecutive simulation ticks ($N \times dt$). |
| **Stack Operations** | | | | |
| `0x10` | `PUSH_CONST` | `<H` (uint16) | `[] -> [val]` | Pushes value from constant pool index onto stack. |
| `0x11` | `PUSH_INT` | `<i` (int32) | `[] -> [int]` | Pushes 32-bit signed integer immediate onto stack. |
| `0x12` | `PUSH_FLOAT` | `<f` (float32) | `[] -> [float]` | Pushes 32-bit IEEE-754 float immediate onto stack. |
| `0x13` | `POP` | (none) | `[a] -> []` | Discards top item from evaluation stack. |
| `0x14` | `DUP` | (none) | `[a] -> [a, a]` | Duplicates top element on evaluation stack. |
| `0x15` | `SWAP` | (none) | `[a, b] -> [b, a]` | Swaps top two elements on evaluation stack. |
| `0x16` | `LOAD_LOCAL` | `<H` (uint16) | `[] -> [val]` | Pushes value from local frame slot index onto stack. |
| `0x17` | `STORE_LOCAL` | `<H` (uint16) | `[val] -> []` | Pops value from stack and stores into local frame slot index. |
| **Arithmetic Operations** | | | | |
| `0x20` | `ADD_I` | (none) | `[a, b] -> [a + b]` | Integer addition. |
| `0x21` | `SUB_I` | (none) | `[a, b] -> [a - b]` | Integer subtraction. |
| `0x22` | `MUL_I` | (none) | `[a, b] -> [a * b]` | Integer multiplication. |
| `0x23` | `DIV_I` | (none) | `[a, b] -> [a / b]` | Integer division (aborts with `ERR_DIVISION_BY_ZERO` if $b=0$). |
| `0x24` | `ADD_F` | (none) | `[a, b] -> [a + b]` | Float addition. |
| `0x25` | `SUB_F` | (none) | `[a, b] -> [a - b]` | Float subtraction. |
| `0x26` | `MUL_F` | (none) | `[a, b] -> [a * b]` | Float multiplication. |
| `0x27` | `DIV_F` | (none) | `[a, b] -> [a / b]` | Float division (aborts with `ERR_DIVISION_BY_ZERO` if $b=0.0$). |
| `0x28` | `NEG` | (none) | `[a] -> [-a]` | Arithmetic negation. |
| **Relational & Comparison** | | | | |
| `0x30` | `CMP_EQ` | (none) | `[a, b] -> [a == b]`| Pushes `1` if $a == b$, else `0`. |
| `0x31` | `CMP_NE` | (none) | `[a, b] -> [a != b]`| Pushes `1` if $a \ne b$, else `0`. |
| `0x32` | `CMP_LT` | (none) | `[a, b] -> [a < b]` | Pushes `1` if $a < b$, else `0`. |
| `0x33` | `CMP_LE` | (none) | `[a, b] -> [a <= b]`| Pushes `1` if $a \le b$, else `0`. |
| `0x34` | `CMP_GT` | (none) | `[a, b] -> [a > b]` | Pushes `1` if $a > b$, else `0`. |
| `0x35` | `CMP_GE` | (none) | `[a, b] -> [a >= b]`| Pushes `1` if $a \ge b$, else `0`. |
| **Control Jumps & Functions** | | | | |
| `0x40` | `JMP` | `<h` (int16) | `[] -> []` | Unconditional relative branch offset in instruction stream. |
| `0x41` | `JMP_IF_TRUE` | `<h` (int16) | `[cond] -> []` | Pops `cond`; branches if `cond != 0`. |
| `0x42` | `JMP_IF_FALSE` | `<h` (int16) | `[cond] -> []` | Pops `cond`; branches if `cond == 0`. |
| `0x43` | `CALL` | `<HB` (uint16, uint8)| `[args...] -> []`| Calls function at index with $N$ arguments, creating call frame. |
| `0x44` | `RET` | (none) | `[] -> []` | Returns from current function call frame to caller. |
| **Biophysical & Domain Primitives** | | | | |
| `0x50` | `STIM_BIPHASIC`| `<B` (uint8) | `[v, p1, p2] -> []`| Schedules biphasic pulse on channel; clamped by hardware watchdog. |
| `0x51` | `READ_SPIKES` | `<B` (uint8) | `[win] -> [count]`| Reads spike count on channel over sliding window (ms). |
| `0x52` | `READ_VOLTAGE`| `<B` (uint8) | `[] -> [v]` | Reads instantaneous extracellular MEA potential on channel. |
| `0x53` | `MODULATE_STDP`| `<BB` (uint8, uint8) | `[dw] -> []` | Modulates synaptic weight between pre and post neurons in $[0, 40\text{ nS}]$. |
| `0x54` | `GET_POP_RATE` | (none) | `[] -> [rate_hz]` | Pushes current population firing rate (Hz) onto stack. |
| `0x55` | `MEA_CONFIG` | `<BB` (uint8, uint8) | `[] -> []` | Configures active MEA topology dimensions (rows, cols). |

---

## 4. Deterministic Timing & Execution Model

WetLang implements a dual-timescale execution model that bridges digital computation and continuous electrophysiology.

### 4.1 Fixed Integration Timestep ($dt = 0.1\text{ ms}$)

Continuous biophysical dynamics (neuron membrane potentials, Tsodyks-Markram vesicle pools, synaptic conductances, and electrode charge accumulations) are integrated using a fixed integration timestep:
$$\Delta t = 0.1\text{ ms} = 100\ \mu\text{s} = 10^{-4}\text{ s}$$

A fixed timestep is mandatory for four architectural reasons:
1. **Numerical Reproducibility**: Prevents floating-point drift and non-deterministic branch divergence across compiler passes and native architectures.
2. **Cycle-Accurate Hardware Watchdog**: The sliding 10.0 ms charge balance ring buffer maps exactly to $N_{ticks} = \frac{10.0\text{ ms}}{0.1\text{ ms}} = 100\text{ ticks}$.
3. **Epileptiform Breaker Counter**: The 50.0 ms runaway breaker maps exactly to $N_{runaway} = \frac{50.0\text{ ms}}{0.1\text{ ms}} = 500\text{ ticks}$.
4. **Absolute Refractory Clamping**: The 2.0 ms absolute refractory period maps to $N_{refract} = \frac{2.0\text{ ms}}{0.1\text{ ms}} = 20\text{ ticks}$, ensuring a theoretical upper bound of $500\text{ Hz}$ per neuron.

### 4.2 Zero-Time Compute Assumption

Within any given simulation tick $k$:
- All bytecode instructions (arithmetic, local variables, logic, control jumps, stimulation schedules) execute in **zero simulated time**.
- When the VM encounters a `SYNC_TICK` (`0x02`) instruction, digital execution suspends.
- The scheduler advances simulation time by $\Delta t$:
  $$t_{sim} \leftarrow t_{sim} + \Delta t$$
- The biophysical digital twin advances its numerical ODE solver by $\Delta t$, evaluating:
  1. Stimulation pulse active durations and electrode charge injection.
  2. Synaptic decay and Tsodyks-Markram vesicle recovery.
  3. COBA-LIF membrane integration and spike threshold crossing.
  4. Axonal spike propagation and online STDP eligibility trace updates.
  5. Hardware watchdog charge accumulation and epileptiform rate monitoring.
- Control returns to the VM bytecode engine to execute the next cycle.

### 4.3 Static Control Flow Graph (CFG) Loop-Yield Verification

To guarantee that a program cannot starve the biophysical simulation or trigger infinite zero-time loops with hardware stimulators engaged, the WetLang compiler enforces static loop-yield verification:
- For every loop construct (`while`, `for`, `stream cycle`), every valid execution path through the loop body must contain a post-dominating `SYNC_TICK` instruction before looping back to the header.
- If any conditional branch allows a loop iteration without yielding, compilation is aborted with `ERR_UNBOUNDED_STIM_LOOP`.

---

## 5. Domain Primitives & Biophysical Semantics

### 5.1 MEA Grid Topology (`grid`, `channel`)

WetLang maps code directly to physical or simulated Microelectrode Arrays:
- The standard layout is an $8 \times 8$ grid of 64 planar microelectrodes with a pitch of $200\ \mu\text{m}$.
- Electrodes can be addressed via 2D spatial coordinates `mea[row, col]` ($0 \le \text{row} < 8, 0 \le \text{col} < 8$) or linear channel identifiers `mea[ch]` ($0 \le ch < 64$).
- Physical coordinate validation is performed statically during compilation and dynamically enforced by the runtime.

### 5.2 Biphasic Stimulation (`stim_biphasic`)

Electrical stimulation of neural tissue must maintain charge neutrality to prevent toxic electrode polarization:
$$\text{stim\_biphasic}(channel,\ voltage,\ phase1,\ phase2)$$
- **Phase 1 (Cathodic / Depolarizing)**: Applies voltage $V_{applied} = \text{clamp}(V, -1.2\text{ V}, +1.2\text{ V})$ for duration $\text{phase1}$ (e.g. $0.2\text{ ms}$).
- **Phase 2 (Anodic / Charge Recovery)**: Applies voltage $V_{recovery} = -V_{applied}$ for duration $\text{phase2}$ (e.g. $0.2\text{ ms}$).
- Current and injected charge are computed via the electrode-electrolyte interface impedance ($Z \approx 1\text{ M}\Omega$):
  $$I(t) = \frac{V(t)}{Z}, \quad Q_{tick} = I(t) \cdot \Delta t$$

### 5.3 Spike Acquisition (`read_spikes`)

Neural activity is acquired through sliding temporal integration windows:
$$\text{count} = \text{read\_spikes}(channel,\ window\_ms)$$
- Queries the total number of action potentials recorded on the designated electrode within the preceding $window\_ms$ (up to $50.0\text{ ms}$).
- Uses an internal cycle-accurate rolling bitmask ring buffer (`uint8_t spike_history[64][500]`).

### 5.4 Plasticity Modulation (`modulate_stdp`)

Synaptic plasticity can be biased or directly steered by feedback algorithms:
$$\text{modulate\_stdp}(pre\_neuron,\ post\_neuron,\ \Delta w)$$
- Updates the conductance weight $w$ of the directed synapse from $pre$ to $post$.
- Enforces hard physical boundaries:
  $$w \leftarrow \text{clamp}(w + \Delta w,\ 0.0\text{ nS},\ 40.0\text{ nS})$$
- Strictly adheres to **Dale's Principle**: An excitatory neuron ($80\%$ of population) forms only excitatory synapses ($E_{rev} = 0\text{ mV}$); an inhibitory neuron ($20\%$ of population) forms only inhibitory synapses ($E_{rev} = -80\text{ mV}$). The weight scalar $w$ remains strictly non-negative.

---

## 6. Summary of Architectural Guarantees

1. **Zero Raw Memory Leaks**: Memory allocation occurs strictly via caller-allocated buffers with pinned lifetimes across the C/Python FFI boundary.
2. **Deterministic Reproducibility**: Exact Exponential Euler biophysical integration at $dt = 0.1\text{ ms}$ yields bit-exact simulation outcomes across identical RNG seeds.
3. **Electrochemical Safety Guarantee**: Hard hardware clamp saturation at $\pm 1.2\text{ V}$ and automated lockout upon residual charge exceeding $0.5\text{ nC}$ over $10.0\text{ ms}$.
4. **Epileptiform Breaker Guarantee**: Immediate zeroing of stimulation DACs and VM state lockout upon $>35\%$ channels exceeding $150\text{ Hz}$ for $50.0\text{ ms}$.
