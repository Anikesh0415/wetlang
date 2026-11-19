# Volume I: WetLang Language Specification & Compiler Internals

**Platform:** Wetworld — WetLang Neural Organoid Computing Platform (v1.0.0)  
**Founder & Lead Architect:** Anikesh Tiwari (Surat, Gujarat, India)  
**Source Scope:** `compiler/token.py`, `compiler/lexer.py`, `compiler/ast_nodes.py`, `compiler/parser.py`, `compiler/semantic.py`, `compiler/isa.py`, `compiler/emitter.py`, `compiler/compiler_cli.py`, `docs/language_spec.md`

---

## 1. Compiler Pipeline Architecture

The WetLang compiler (`wetc`, entry point `compiler/compiler_cli.py`) translates `.wet` source programs into standalone `.wbc` (WetLang Bytecode) binaries without external parser generators, regular-expression engines, or third-party compiler frameworks. Every stage is hand-crafted in pure Python 3.12+ standard library modules:

```
  Source (.wet)
       │
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Stage 1: Deterministic DFA Lexer (compiler/lexer.py, compiler/token.py) │
│   - Zero-regex character scanner with 1-based line/column tracking      │
│   - Longest-match physical unit suffix binding -> SI base scaling       │
└─────────────────────────────────────────────────────────────────────────┘
       │  List[Token]
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Stage 2: Pratt Recursive-Descent Parser (compiler/parser.py)            │
│   - Top-level declarations (grid, channel, fn, stream, statements)      │
│   - Precedence-climbing expression parser -> 27 typed AST node classes  │
└─────────────────────────────────────────────────────────────────────────┘
       │  ProgramNode (AST)
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Stage 3: 3-Pass Semantic & Safety Verifier (compiler/semantic.py)       │
│   - Pass 1: Lexical scope resolution + constant-folded MEA bounds check │
│   - Pass 2: Dimensional homogeneity + static +/-1.2 V voltage clamp     │
│   - Pass 3: Static CFG loop-yield post-dominance verifier (sync_tick)   │
└─────────────────────────────────────────────────────────────────────────┘
       │  Verified ProgramNode
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ Stage 4: WBC Bytecode Emitter & Cryptographic Signer                    │
│   - 45-opcode stack machine codegen + int16 relative jump backpatching  │
│   - 32-byte header, 5 sections, 8 capability flags, IEEE 802.3 CRC-32   │
│   - HMAC-SHA256 biosafety trailer signature for tamper-evident provenance│
└─────────────────────────────────────────────────────────────────────────┘
       │
       ▼
  Verified Binary (.wbc)
```

---

## 2. Formal ISO/IEC 14977 EBNF Grammar

The grammar below is verified directly against `docs/language_spec.md` and the recursive-descent implementation in `compiler/parser.py` (including implementation extensions such as optional 5th `interphase` parameter on `stim_biphasic`, optional tick count / duration argument on `sync_tick`, range literals `[start .. end]`, C-style typed declarations, and contextual identifier reuse for `cycle`, `stream`, and `mode`).

### 2.1 Lexical Grammar

```ebnf
Whitespace          = { " " | "\t" | "\r" | "\n" } ;
SingleLineComment   = "//" , { all_characters - "\n" } , [ "\n" ] ;
MultiLineComment    = "/*" , { all_characters - "*/" } , "*/" ;

Letter              = "A" .. "Z" | "a" .. "z" | "_" ;
Digit               = "0" .. "9" ;
Identifier          = Letter , { Letter | Digit } ;

IntegerLiteral      = Digit , { Digit } ;
FloatLiteral        = Digit , { Digit } , [ "." , Digit , { Digit } ] ,
                      [ ( "e" | "E" ) , [ "+" | "-" ] , Digit , { Digit } ] ;
BooleanLiteral      = "true" | "false" ;
StringLiteral       = '"' , { ( all_characters - ( '"' | "\\" ) )
                            | ( "\\" , ( "n" | "t" | "r" | '"' | "\\" | all_characters ) ) } , '"' ;

TimeUnit            = "s" | "ms" | "us" ;
VoltageUnit         = "V" | "mV" | "uV" ;
CurrentUnit         = "A" | "uA" | "nA" | "pA" ;
ChargeUnit          = "C" | "nC" | "pC" ;
FrequencyUnit       = "Hz" ;
LengthUnit          = "mm" | "um" ;
FlowRateUnit        = "uL/min" | "uL_per_min" | "mL/min" ;
VolumeUnit          = "uL" | "nL" | "mL" ;
PressureUnit        = "kPa" | "Pa" ;
TemperatureUnit     = "degC" ;
PhysicalUnit        = TimeUnit | VoltageUnit | CurrentUnit | ChargeUnit | FrequencyUnit | LengthUnit
                    | FlowRateUnit | VolumeUnit | PressureUnit | TemperatureUnit ;
PhysicalLiteral     = ( IntegerLiteral | FloatLiteral ) , PhysicalUnit ;
```

### 2.2 Syntactic Grammar

```ebnf
Program             = { TopLevelDeclaration } , EOF ;

TopLevelDeclaration = GridDeclaration
                    | ChannelDeclaration
                    | OrganoidDeclaration
                    | ConnectDeclaration
                    | FunctionDeclaration
                    | StreamDeclaration
                    | Statement ;

(* Biological Organoid & Connectome Declarations *)
OrganoidDeclaration = "organoid" , ContextIdent , "{" , { OrganoidProperty } , "}" ;
OrganoidProperty    = Identifier , ":" , Expression , ";" ;

ConnectDeclaration  = "connect" , ContextIdent , "[" , Expression , "]" , "->" ,
                      ContextIdent , "[" , Expression , "]" , "with" , "{" ,
                      { ConnectProperty } , "}" , ";" ;
ConnectProperty     = Identifier , ":" , Expression , ";" ;

(* MEA Grid & Channel Declarations *)
GridDeclaration     = "grid" , ContextIdent , ( GridDimensions | GridBlock ) ;
GridDimensions      = "[" , Expression , [ "," , Expression ] , "]" , ";" ;
GridBlock           = "{" , { GridProperty } , "}" ;
GridProperty        = Identifier , ":" , Expression , ";" ;

ChannelDeclaration  = "channel" , ContextIdent , "=" , Expression , [ ChannelModeClause ] , ";" ;
ChannelModeClause   = "mode" , ":" , ChannelMode ;
ChannelMode         = "BiphasicStim" | "SpikeReadout" | "VoltageSense" | "Bidirectional" | Identifier ;

(* Functions and Closed-Loop Streams *)
FunctionDeclaration = "fn" , ContextIdent , "(" , [ ParameterList ] , ")" , [ "->" , TypeName ] , Block ;
ParameterList       = Parameter , { "," , Parameter } ;
Parameter           = ContextIdent , ":" , TypeName ;

StreamDeclaration   = "stream" , Identifier , "{" , { StreamItem } , "}" ;
StreamItem          = BindStatement | CycleStatement ;
BindStatement       = "bind" , Identifier , ( "->" | "<-" ) , Identifier , ";" ;
CycleStatement      = "cycle" , Block ;

(* Type System *)
TypeName            = PrimitiveType | PhysicalType | Identifier ;
PrimitiveType       = "int" | "float" | "bool" | "string" | "channel" | "grid" ;
PhysicalType        = "Voltage" | "Current" | "Time" | "Frequency" | "Length" | "Charge"
                    | "FlowRate" | "Volume" | "Pressure" | "Temperature" ;
ContextIdent        = Identifier | "cycle" | "stream" | "mode" ;

(* Statements *)
Statement           = Block
                    | LetStatement
                    | TypedVarDeclaration
                    | StimStatement
                    | ActuatorStatement
                    | ModulateStatement
                    | SyncTickStatement
                    | IfStatement
                    | WhileStatement
                    | ForStatement
                    | ReturnStatement
                    | AssignOrExprStatement ;

Block               = "{" , { Statement } , "}" ;

LetStatement        = "let" , [ "mut" ] , ContextIdent , [ ":" , TypeName ] , "=" , Expression , ";" ;
TypedVarDeclaration = ( "int" | "float" | "bool" | "string" | PhysicalType ) ,
                      ContextIdent , [ "=" , Expression ] , ";" ;

StimStatement       = "stim_biphasic" , "(" , Expression , "," , Expression , "," ,
                      Expression , "," , Expression , [ "," , Expression ] , ")" , ";" ;

ActuatorStatement   = "pump_set_rate" , "(" , Expression , "," , Expression , ")" , ";"
                    | "pump_dispense" , "(" , Expression , "," , Expression , ")" , ";"
                    | "valve_set" , "(" , Expression , "," , Expression , ")" , ";"
                    | "valve_open" , "(" , Expression , ")" , ";"
                    | "valve_close" , "(" , Expression , ")" , ";"
                    | "motor_step" , "(" , Expression , "," , Expression , [ "," , Expression ] , ")" , ";" ;
ModulateStatement   = "modulate_stdp" , "(" , [ ArgumentList ] , ")" , ";" ;
SyncTickStatement   = "sync_tick" , [ "(" , [ Expression ] , ")" ] , ";" ;

IfStatement         = "if" , "(" , Expression , ")" , Block , [ "else" , ( IfStatement | Block ) ] ;
WhileStatement      = "while" , "(" , Expression , ")" , Block ;
ForStatement        = "for" , ContextIdent , "in" , Expression , ".." , Expression , Block ;
ReturnStatement     = "return" , [ Expression ] , ";" ;
AssignOrExprStatement = Expression , [ "=" , Expression ] , ";" ;

(* Pratt Expression Hierarchy *)
Expression          = LogicalOrExpr ;
LogicalOrExpr       = LogicalAndExpr , { "||" , LogicalAndExpr } ;
LogicalAndExpr      = EqualityExpr , { "&&" , EqualityExpr } ;
EqualityExpr        = RelationalExpr , { ( "==" | "!=" ) , RelationalExpr } ;
RelationalExpr      = AdditiveExpr , { ( "<" | "<=" | ">" | ">=" ) , AdditiveExpr } ;
AdditiveExpr        = MultiplicativeExpr , { ( "+" | "-" ) , MultiplicativeExpr } ;
MultiplicativeExpr  = UnaryExpr , { ( "*" | "/" | "%" ) , UnaryExpr } ;
UnaryExpr           = ( "-" | "!" ) , UnaryExpr | PostfixExpr ;
PostfixExpr         = PrimaryExpr , { UnitSuffix | CallSuffix | IndexSuffix } ;
CallSuffix          = "(" , [ ArgumentList ] , ")" ;
IndexSuffix         = "[" , Expression , { "," , Expression } , "]" ;
ArgumentList        = Expression , { "," , Expression } ;

PrimaryExpr         = IntegerLiteral
                    | FloatLiteral
                    | BooleanLiteral
                    | StringLiteral
                    | PhysicalLiteral
                    | DomainCall
                    | CastCall
                    | RangeLiteral
                    | ContextIdent
                    | "(" , Expression , ")" ;

RangeLiteral        = "[" , Expression , ".." , Expression , "]" ;
CastCall            = ( "int" | "float" | "bool" | "string" ) , "(" , Expression , ")" ;
DomainCall          = ( "read_spikes" | "read_voltage" | "pop_firing_rate" | "read_population_rate"
                      | "read_pressure" | "read_temperature" ) ,
                      "(" , [ ArgumentList ] , ")" ;
```

---

## 3. Lexical Token Table & Physical Dimensional Units

### 3.1 Token Inventory (`compiler/token.py`)

`TokenType` defines enum variants organized across lexical categories. Each scanned `Token` dataclass carries `(type, value, line, column, dimension, si_value, raw_text)`.

| Category | Count | TokenType Members / Lexemes |
|---|---:|---|
| Sentinel | 1 | `EOF` |
| Literals & Identifiers | 6 | `INT_LIT`, `FLOAT_LIT`, `BOOL_LIT`, `STRING_LIT`, `PHYSICAL_LIT`, `IDENTIFIER` |
| Biological Topology & Connectome | 4 | `ORGANOID` (`organoid`), `CONNECT` (`connect`), `WITH` (`with`), `TO` (`to`) |
| MEA Topology & Modes | 7 | `GRID` (`grid`), `CHANNEL` (`channel`), `MODE` (`mode`), `BIPHASIC_STIM` (`BiphasicStim`), `SPIKE_READOUT` (`SpikeReadout`), `VOLTAGE_SENSE` (`VoltageSense`), `BIDIRECTIONAL` (`Bidirectional`) |
| Declarations & Primitive Types | 7 | `FN` (`fn`), `LET` (`let`), `MUT` (`mut`), `INT` (`int`), `FLOAT` (`float`), `BOOL` (`bool`), `STRING` (`string`) |
| Physical Type Keywords | 10 | `TYPE_VOLTAGE` (`Voltage`), `TYPE_CURRENT` (`Current`), `TYPE_TIME` (`Time`), `TYPE_FREQUENCY` (`Frequency`), `TYPE_LENGTH` (`Length`), `TYPE_CHARGE` (`Charge`), `TYPE_FLOW_RATE` (`FlowRate`), `TYPE_VOLUME` (`Volume`), `TYPE_PRESSURE` (`Pressure`), `TYPE_TEMPERATURE` (`Temperature`) |
| Closed-Loop & Control Flow | 11 | `STREAM` (`stream`), `BIND` (`bind`), `CYCLE` (`cycle`), `IF` (`if`), `ELSE` (`else`), `WHILE` (`while`), `FOR` (`for`), `IN` (`in`), `RETURN` (`return`), `TRUE` (`true`), `FALSE` (`false`) |
| Electrophysiology Primitives | 7 | `STIM_BIPHASIC` (`stim_biphasic`), `MODULATE_STDP` (`modulate_stdp`), `SYNC_TICK` (`sync_tick`), `READ_SPIKES` (`read_spikes`), `READ_VOLTAGE` (`read_voltage`), `POP_FIRING_RATE` (`pop_firing_rate`), `READ_POPULATION_RATE` (`read_population_rate`) |
| Cyber-Physical Actuators | 8 | `PUMP_SET_RATE` (`pump_set_rate`), `PUMP_DISPENSE` (`pump_dispense`), `VALVE_SET` (`valve_set`), `VALVE_OPEN` (`valve_open`), `VALVE_CLOSE` (`valve_close`), `MOTOR_STEP` (`motor_step`), `READ_PRESSURE` (`read_pressure`), `READ_TEMPERATURE` (`read_temperature`) |
| Operators & Delimiters | 28 | `+` `PLUS`, `-` `MINUS`, `*` `STAR`, `/` `SLASH`, `%` `PERCENT`, `==` `EQ_EQ`, `!=` `NOT_EQ`, `<` `LT`, `<=` `LT_EQ`, `>` `GT`, `>=` `GT_EQ`, `&&` `AND_AND`, `\|\|` `OR_OR`, `!` `NOT`, `=` `ASSIGN`, `->` `ARROW_RIGHT`, `<-` `ARROW_LEFT`, `..` `DOT_DOT`, `(` `LPAREN`, `)` `RPAREN`, `{` `LBRACE`, `}` `RBRACE`, `[` `LBRACKET`, `]` `RBRACKET`, `,` `COMMA`, `:` `COLON`, `;` `SEMICOLON`, `.` `DOT` |

> **Scanner Note:** The `KEYWORDS` lookup table maps reserved lexemes. `true` and `false` are converted directly into `TokenType.BOOL_LIT` with Python `bool` values (`True`/`False`) during `_scan_identifier_or_keyword()`. Contextual identifier handling permits reusing names like `sensor`, `motor`, `valve`, and `pump` as variable or stream identifiers when not appearing in command position.

### 3.2 Physical Dimensional Units & SI Conversion Table (`UNIT_SUFFIXES`)

`Lexer._scan_number()` evaluates candidate unit suffixes using `SORTED_UNIT_SUFFIXES` (sorted by descending string length so multi-character suffixes such as `"uL/min"`, `"uL_per_min"`, `"degC"`, `"kPa"`, `"ms"`, `"mV"` match before single-character `"s"`, `"V"`, `"A"`, `"C"`). A lookahead guard ensures the character immediately following a suffix is not alphanumeric or `_`, preventing false matches on identifiers.

| Dimension (`Dimension`) | Suffix | SI Base Unit | Scale Factor | Example Source | Internal `si_value` |
|---|---|---|---:|---|---:|
| `Dimension.TIME` | `s` | Second (s) | `1.0` | `1s` | `1.0` |
| `Dimension.TIME` | `ms` | Second (s) | `1e-3` | `0.1ms` | `1.0e-4` |
| `Dimension.TIME` | `us` | Second (s) | `1e-6` | `200us` | `2.0e-4` |
| `Dimension.VOLTAGE` | `V` | Volt (V) | `1.0` | `0.8V` | `0.8` |
| `Dimension.VOLTAGE` | `mV` | Volt (V) | `1e-3` | `-70mV` | `-0.07` |
| `Dimension.VOLTAGE` | `uV` | Volt (V) | `1e-6` | `50uV` | `5.0e-5` |
| `Dimension.CURRENT` | `A` | Ampere (A) | `1.0` | `1A` | `1.0` |
| `Dimension.CURRENT` | `uA` | Ampere (A) | `1e-6` | `10uA` | `1.0e-5` |
| `Dimension.CURRENT` | `nA` | Ampere (A) | `1e-9` | `5nA` | `5.0e-9` |
| `Dimension.CURRENT` | `pA` | Ampere (A) | `1e-12` | `200pA` | `2.0e-10` |
| `Dimension.CHARGE` | `C` | Coulomb (C) | `1.0` | `1C` | `1.0` |
| `Dimension.CHARGE` | `nC` | Coulomb (C) | `1e-9` | `0.5nC` | `5.0e-10` |
| `Dimension.CHARGE` | `pC` | Coulomb (C) | `1e-12` | `100pC` | `1.0e-10` |
| `Dimension.FREQUENCY` | `Hz` | Hertz (s^-1) | `1.0` | `150Hz` | `150.0` |
| `Dimension.LENGTH` | `mm` | Meter (m) | `1e-3` | `1mm` | `1.0e-3` |
| `Dimension.LENGTH` | `um` | Meter (m) | `1e-6` | `200um` | `2.0e-4` |
| `Dimension.FLOW_RATE` | `uL/min`, `uL_per_min` | m^3 / s | `1.666667e-11` | `1.5uL/min` | `2.5e-11` |
| `Dimension.FLOW_RATE` | `mL/min` | m^3 / s | `1.666667e-8` | `0.1mL/min` | `1.667e-9` |
| `Dimension.VOLUME` | `uL` | m^3 | `1e-9` | `50uL` | `5.0e-8` |
| `Dimension.VOLUME` | `nL` | m^3 | `1e-12` | `500nL` | `5.0e-10` |
| `Dimension.PRESSURE` | `kPa` | Pascal (Pa) | `1000.0` | `101.3kPa` | `101300.0` |
| `Dimension.PRESSURE` | `Pa` | Pascal (Pa) | `1.0` | `500Pa` | `500.0` |
| `Dimension.TEMPERATURE` | `degC` | Kelvin (K) offset | `1.0` | `37.0degC` | `37.0` |

Range disambiguation: In `_scan_number()`, a decimal point `.` is only consumed as a floating-point fraction if `self._peek(1)` is a digit (`!= '.'`), ensuring `0..10` tokenizes cleanly as `INT_LIT(0)`, `DOT_DOT(..)`, `INT_LIT(10)`.

---

## 4. Pratt Recursive-Descent Parser & AST Hierarchy

### 4.1 Precedence Binding Power Table (`compiler/parser.py`)

Statements and declarations use LL(k) recursive descent (with 2-token lookahead in `_parse_statement()` to distinguish C-style typed declarations like `float error = ...;` from cast expressions like `float(right_spikes)`). Expressions use Pratt precedence climbing via `parse_expression(min_bp=0)`:

| Precedence Tier | Operators / Constructs | Binding Power `(l_bp, r_bp)` | Associativity |
|---:|---|---:|---|
| 1 (Lowest) | `\|\|` (`OR_OR`) | `(10, 11)` | Left-associative |
| 2 | `&&` (`AND_AND`) | `(20, 21)` | Left-associative |
| 3 | `==` (`EQ_EQ`), `!=` (`NOT_EQ`) | `(30, 31)` | Left-associative |
| 4 | `<` (`LT`), `<=` (`LT_EQ`), `>` (`GT`), `>=` (`GT_EQ`) | `(40, 41)` | Left-associative |
| 5 | `+` (`PLUS`), `-` (`MINUS`) | `(50, 51)` | Left-associative |
| 6 | `*` (`STAR`), `/` (`SLASH`), `%` (`PERCENT`) | `(60, 61)` | Left-associative |
| 7 | Prefix unary `-`, `!` | `PREFIX_BINDING_POWER = 70` | Right-associative |
| 8 (Highest) | Postfix call `f(...)`, indexing `a[r, c]`, unit suffix | `POSTFIX_BINDING_POWER = 80` | Left-associative |

Every left-associative binary operator uses `r_bp = l_bp + 1`, so `a - b - c` parses as `(a - b) - c`. On syntax failure, `ParseError` reports exact `(line, column, expected, found)`. *(Codegen Note: The modulo operator `%` (`PERCENT`) is lexed, parsed at binding power `(60, 61)`, and integer-folded in Semantic Pass 1, but `BytecodeEmitter.visit_BinaryOpNode()` does not yet emit a runtime modulo opcode in v1.0.)*

### 4.2 Complete AST Node Hierarchy (`compiler/ast_nodes.py`)

All 30 concrete AST node dataclasses inherit from `ASTNode(line: int = 0, column: int = 0)` and implement double-dispatch via `accept(visitor: ASTVisitor)` invoking `visit_<ClassName>`.

| Category | AST Node Class | Fields |
|---|---|---|
| **Root & Declarations (10)** | `ProgramNode` | `declarations: List[ASTNode]` |
| | `GridDeclNode` | `name: str`, `rows: Any`, `cols: Any`, `pitch: Optional[Any]`, `base_voltage: Optional[Any]` |
| | `ChannelDeclNode` | `name: str`, `target: ASTNode`, `mode: Optional[str]` |
| | `OrganoidDeclNode` | `name: str`, `properties: Dict[str, ASTNode]` |
| | `ConnectDeclNode` | `source: str`, `source_ch: ASTNode`, `target: str`, `target_ch: ASTNode`, `properties: Dict[str, ASTNode]` |
| | `PortDeclNode` | `name: str`, `port_type: str`, `port_id: int` |
| | `ParamNode` | `name: str`, `type_name: str` |
| | `FnDeclNode` | `name: str`, `params: List[ParamNode]`, `return_type: Optional[str]`, `body: BlockNode` |
| | `StreamItemNode` | `kind: str` (`"bind_in"`, `"bind_out"`, `"cycle"`), `left: Optional[str]`, `right: Optional[str]`, `cycle_block: Optional[BlockNode]` |
| | `StreamDeclNode` | `name: str`, `items: List[StreamItemNode]` |
| **Statements (11)** | `BlockNode` | `statements: List[ASTNode]` |
| | `LetStmtNode` | `name: str`, `is_mut: bool`, `type_name: Optional[str]`, `initializer: ASTNode` |
| | `AssignStmtNode` | `target: ASTNode`, `value: ASTNode` |
| | `StimStmtNode` | `channel: ASTNode`, `voltage: ASTNode`, `phase1: ASTNode`, `phase2: ASTNode`, `interphase: Optional[ASTNode]` |
| | `ModulateStmtNode` | `args: List[ASTNode]` |
| | `SyncTickStmtNode` | `count: Optional[ASTNode]` |
| | `IfStmtNode` | `condition: ASTNode`, `then_block: BlockNode`, `else_block: Optional[ASTNode]` |
| | `WhileStmtNode` | `condition: ASTNode`, `body: BlockNode` |
| | `ForStmtNode` | `var_name: str`, `range_start: ASTNode`, `range_end: ASTNode`, `body: BlockNode` |
| | `ReturnStmtNode` | `value: Optional[ASTNode]` |
| | `ExprStmtNode` | `expr: ASTNode` |
| **Expressions (9)** | `BinaryOpNode` | `left: ASTNode`, `op: str`, `right: ASTNode` |
| | `UnaryOpNode` | `op: str`, `operand: ASTNode` |
| | `LiteralNode` | `value: Any`, `type_name: str` (`"int"`, `"float"`, `"bool"`, `"string"`) |
| | `PhysicalLiteralNode` | `magnitude: float`, `dimension: Dimension`, `si_value: float`, `unit_suffix: str` |
| | `IdentifierNode` | `name: str` |
| | `CallNode` | `callee: ASTNode`, `args: List[ASTNode]` |
| | `IndexNode` | `target: ASTNode`, `indices: List[ASTNode]` |
| | `RangeNode` | `start: ASTNode`, `end: ASTNode` |
| | `DomainCallNode` | `func_name: str`, `args: List[ASTNode]` |

*(Total: 1 base `ASTNode` + 30 concrete node classes including `ParamNode`, `StreamItemNode`, `OrganoidDeclNode`, and `ConnectDeclNode`.)*

---

## 5. Three-Pass Semantic & Static Safety Analyzer (`compiler/semantic.py`)

`SemanticAnalyzer.analyze()` pre-populates global built-in symbols (`read_spikes`, `read_voltage`, `pop_firing_rate`, `read_population_rate`, `abs`, `float`, `int`) and executes three sequential AST visitor passes. Any invariant violation aborts compilation with `SemanticError(message, line, column, error_code)`.

### 5.1 Pass 1: Scope Resolution & Constant-Folded MEA Bounds (`_Pass1Visitor`)

- **Lexical Scoping**: Maintains a linked parent-pointer `Scope` chain for global, function, stream, block, and `for`-loop scopes. Detects duplicate local declarations (`ERR_REDECLARED_IDENTIFIER`) and unresolved identifiers (`ERR_UNDECLARED_IDENTIFIER`).
- **Integer Constant Folding**: `_extract_int_constant()` evaluates immutable `let` bindings (`not node.is_mut`), unary `+`/`-`, and binary `+`, `-`, `*`, `//`, `%` over integer literals.
- **MEA Coordinate Verification**: `_check_coordinate_bounds()` inspects every `IndexNode` inside `ChannelDeclNode`, `StimStmtNode`, `IndexNode`, and `read_spikes`/`read_voltage` calls:
  - 2D indexing `mea[r, c]`: enforces $0 \le r \le 7$ and $0 \le c \le 7$.
  - 1D indexing `mea[k]`: enforces $0 \le k \le 63$.
  - Any static violation raises `ERR_ELECTRODE_OUT_OF_BOUNDS`.

### 5.2 Pass 2: Dimensional Type Checking & Static Water-Window Clamp (`_Pass2Visitor`)

- **Dimensional Algebra**: Tracks `Dimension` per AST node (`node_dimensions[id(node)]`) and propagates dimensions across `LetStmtNode`, `AssignStmtNode`, `UnaryOpNode`, and `BinaryOpNode`:
  - Addition/Subtraction (`+`, `-`): if both operands have non-`NONE` dimensions and $\text{dim}(L) \ne \text{dim}(R)$, raises `ERR_DIMENSIONAL_MISMATCH`.
  - Multiplication (`*`): $\text{CURRENT} \times \text{TIME} \rightarrow \text{CHARGE}$ (commutatively); scalar `NONE` preserves the other operand's dimension.
  - Division (`/`): $\text{CHARGE} / \text{TIME} \rightarrow \text{CURRENT}$; identical non-`NONE` dimensions cancel to `NONE`; dividing by `NONE` preserves numerator dimension.
  - Relational/Equality (`==`, `!=`, `<`, `<=`, `>`, `>=`): mismatched non-`NONE` dimensions raise `ERR_DIMENSIONAL_MISMATCH`; result dimension is `NONE`.
  - Variable Assignment: assigning incompatible non-`NONE` dimensions raises `ERR_DIMENSIONAL_MISMATCH`.
- **Static Water-Window Voltage Clamp**: `_extract_float_si_value()` constant-folds physical literals, numeric literals, unary `+`/`-`, binary `+`/`-`/`*`/`/`, and immutable `let` variables. In `visit_StimStmtNode()`, if the folded voltage satisfies $|V| > 1.2 + 10^{-9}\text{ V}$, compilation immediately fails with `ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED`.

### 5.3 Pass 3: Static CFG Loop-Yield Post-Dominance Verifier (`_Pass3LoopYieldVisitor`)

**Safety Invariant:** In WetLang's zero-time compute model, bytecode instructions between `sync_tick` barriers execute in zero simulated time. If a loop body can execute `stim_biphasic(...)` and return along the loop back-edge without executing `sync_tick`, the program can issue unbounded electrical stimulation commands without advancing the biophysical ODE solver or sliding charge watchdog.

**Formal Verification Algorithm:**
For every loop construct $L \in \{\texttt{while}, \texttt{for}, \texttt{stream cycle}\}$, `_verify_loop_yield(body)` enumerates the complete set of straight-line intraprocedural control-flow paths $\Pi(L)$ through `body` via `_enumerate_execution_paths(block)`:
1. Start with $\Pi = \{\langle\rangle\}$.
2. For each statement $s$ in `block.statements`:
   - If $s$ is a nested `BlockNode` $B$: take the Cartesian concatenation $\Pi \leftarrow \{p \cdot q \mid p \in \Pi,\ q \in \Pi(B)\}$.
   - If $s$ is an `IfStmtNode(cond, T, E)`: compute $\Pi(T)$ and $\Pi(E)$ (where absent `else` yields the empty fall-through path $\{\langle\rangle\}$, and chained `else if` recurses), then form $\Pi \leftarrow \{p \cdot t \mid p \in \Pi, t \in \Pi(T)\} \cup \{p \cdot e \mid p \in \Pi, e \in \Pi(E)\}$.
   - Otherwise (including `StimStmtNode`, `SyncTickStmtNode`, and inner loop statements `WhileStmtNode`/`ForStmtNode` treated as opaque non-yielding singletons at the outer level): append $s$ to every path in $\Pi$.
3. **Post-Dominance Check**: For every path $p \in \Pi(L)$:
   $$\exists\, s \in p : \text{isStim}(s) \implies \exists\, y \in p : \text{isSyncTick}(y)$$
   If any path $p$ contains a `StimStmtNode` without a `SyncTickStmtNode`, compilation aborts with `ERR_UNBOUNDED_STIM_LOOP`.

**Critical Soundness Properties (Verified by `tests/test_static_verifier.py`):**
- **Branch Bypass Rejection**: An `if (c) { sync_tick(); }` without an `else` generates the fall-through path bypassing `sync_tick()`, so any stimulation on that path is rejected.
- **Inner-Loop Evasion Immunity**: Because inner `while`/`for` nodes are appended as atomic statements rather than flattened into the outer loop's path list, a `sync_tick()` hidden inside an inner loop (which might execute 0 iterations at runtime) does **not** satisfy the outer loop's yield obligation.
- **Pure-Compute Exemption**: Loops with no `StimStmtNode` on any path (e.g., Benchmark 02's 16-channel readout summation loop) are accepted without spurious `sync_tick` requirements.
- **Known Scope Limitation (Honest Engineering Note)**: Pass 3 currently checks direct `StimStmtNode` statements intraprocedurally; it does not perform interprocedural call-graph traversal for user-defined `fn` helpers that wrap `stim_biphasic`, nor does it guard against exponential path blowup on deeply nested `if/else` chains (e.g., >20 sequential independent `if` blocks in one loop).

---

## 6. Custom `.wbc` Binary Bytecode Specification (`compiler/isa.py`, `compiler/emitter.py`)

### 6.1 32-Byte Header Layout (`<4sBBHIIIIfI`)

Every `.wbc` binary begins with an exact 32-byte packed little-endian header verified by `assert struct.calcsize("<4sBBHIIIIfI") == 32` in Python and `#pragma pack(push, 1)` in C (`wet_bytecode_header_t`):

| Offset | Size (B) | Struct Code | C Field | Type | Default / Normative Value |
|---:|---:|---|---|---|---|
| `0x00` | 4 | `4s` | `magic[4]` | `uint8_t[4]` | `"WETB"` (`0x57 0x45 0x54 0x42`, little-endian uint32 `0x42544557`) |
| `0x04` | 1 | `B` | `version_major` | `uint8_t` | `1` (`VERSION_MAJOR`) |
| `0x05` | 1 | `B` | `version_minor` | `uint8_t` | `0` (`VERSION_MINOR`) |
| `0x06` | 2 | `H` | `capabilities` | `uint16_t` | Bitwise OR of `Capability` flags |
| `0x08` | 4 | `I` | `file_size` | `uint32_t` | Total `.wbc` byte length (header + section table + payloads) |
| `0x0C` | 4 | `I` | `checksum_crc32` | `uint32_t` | IEEE 802.3 CRC-32 (`zlib.crc32` / polynomial `0xEDB88320`) over full file with bytes `0x0C..0x0F` zeroed |
| `0x10` | 4 | `I` | `num_sections` | `uint32_t` | `5` (all 5 standard sections emitted) |
| `0x14` | 4 | `I` | `channel_count` | `uint32_t` | `64` (8x8 MEA default) |
| `0x18` | 4 | `f` | `max_charge_nc` | `float` | `0.5f` (IEEE-754 float32, static charge bound in nC) |
| `0x1C` | 4 | `I` | `reserved` | `uint32_t` | `0` |

### 6.2 Capability Bitmask Flags (`Capability`)

| Constant | Hex | Bit | Trigger Condition in `BytecodeEmitter` |
|---|---:|---:|---|
| `NONE` | `0x0000` | — | Pure compute / readout-only program |
| `CAP_STIMULATION` | `0x0001` | 0 | Emitted whenever any `StimStmtNode` is compiled |
| `CAP_PLASTICITY` | `0x0002` | 1 | Emitted whenever any `ModulateStmtNode` is compiled |
| `CAP_CLOSED_LOOP` | `0x0004` | 2 | Emitted whenever any `StreamDeclNode` is compiled |
| `CAP_HIGH_VOLTAGE` | `0x0008` | 3 | Emitted whenever static stimulation voltage satisfies $\|V\| \ge 0.8 - 10^{-9}\text{ V}$ |
| `CAP_MULTI_ELECTRODE` | `0x0010` | 4 | Emitted whenever `len(used_electrodes) > 16` across stim/readout/STDP ops |
| `CAP_MICROFLUIDICS` | `0x0020` | 5 | Emitted whenever microfluidic pump or valve actuation builtins are called |
| `CAP_MOTOR_ACTUATION` | `0x0040` | 6 | Emitted whenever physical stepper motor positioning builtins are called |
| `CAP_SIGNATURE_VERIFIED` | `0x0080` | 7 | Cryptographically authenticated HMAC-SHA256 signature verified in WBC trailer |

### 6.3 Section Table & Binary Payloads

Immediately following offset `0x20` (byte 32) is the section table of `num_sections` 12-byte entries (`SECTION_ENTRY_FORMAT = "<HHII"`):

| Offset in Entry | Size | Field | Description |
|---:|---:|---|---|
| `+0` | 2 | `section_type` (`uint16`) | `1..5` (`SectionType`) |
| `+2` | 2 | `reserved` (`uint16`) | `0` |
| `+4` | 4 | `offset` (`uint32`) | Absolute byte offset from start of `.wbc` file (`payload_offset = 32 + 5 * 12 = 92`) |
| `+8` | 4 | `size` (`uint32`) | Section payload byte length |

**Payload Encodings for All 5 Sections:**
1. **`CONSTANT_POOL` (`1`)**: `<I` (`count`), followed by `count` tagged records:
   - Tag `1` (`WET_VAL_INT`): `uint8(1)` + `<i` (`int32`)
   - Tag `2` (`WET_VAL_FLOAT`): `uint8(2)` + `<f` (`float32`)
   - Tag `3` (`WET_VAL_STRING`): `uint8(3)` + `<H` (`byte_len`) + UTF-8 bytes
   Deduplicated via hash table lookup `(tag, val) -> index`.
2. **`TOPOLOGY_CONFIG` (`2`)**: Header `<IHHfI` (`channel_count=64`, `rows=8`, `cols=8`, `pitch_um=200.0f`, `num_aliases`), followed per alias by `<H` (`name_len`), UTF-8 `name`, `<BB` (`channel_id`, `mode_byte` where `0=Bidirectional`, `1=BiphasicStim`, `2=SpikeReadout`, `3=VoltageSense`).
3. **`BYTECODE_STREAM` (`3`)**: Tightly packed variable-length instruction stream (`1 byte opcode` + `0..4 bytes little-endian operands`), terminated by `0x01` (`HALT`).
4. **`SAFETY_MANIFEST` (`4`)**: Fixed 13-byte packed struct `<IBff` (`capabilities: uint32`, `verified_loop_yield: uint8 = 1`, `max_voltage_seen: float32`, `max_charge: float32 = 0.5f`).
5. **`DEBUG_LINE_MAP` (`5`)**: `<I` (`entry_count`), followed by `entry_count` triples `<III` (`bytecode_offset`, `source_line`, `source_column`).

**Cryptographic Signature Trailer:**
Optionally appended to the WBC binary is a 32-byte HMAC-SHA256 authenticated signature certificate generated by `compiler/crypto_signer.py`. The native runtime validates this signature against the authorized lab secret before granting `CAP_HIGH_VOLTAGE` or cyber-physical actuator control, returning `WET_ERR_SECURITY_UNTRUSTED` on any signature invalidity or payload modification.

### 6.4 Jump Fixup Backpatching & CRC-32 Integrity

- **Relative Branch Addressing**: `JMP`, `JMP_IF_TRUE`, and `JMP_IF_FALSE` take a signed 16-bit offset `<h` relative to the **start byte of the jump instruction itself**:
  $$\text{target\_pc} = \text{instr\_pc} + \text{rel\_offset}$$
  Forward branches (`if`/`else` skip, `while`/`for` exit) emit a placeholder `0` via `emit_jump()` and backpatch with `patch_jump(operand_offset, target_offset)` once the target offset is known. Backward loop edges compute `loop_start - current_offset()` directly.
- **CRC-32 Verification**: `BytecodeEmitter._build_wbc_binary()` packs the 32-byte header with `checksum_crc32 = 0`, appends the section table and all 5 payloads, computes `zlib.crc32(full_binary) & 0xFFFFFFFF`, and patches the 4-byte little-endian checksum at offset `0x0C` (12). The native loader (`wetvm_vm.c`) computes the identical bitwise IEEE 802.3 CRC-32 (`0xEDB88320`) in three chunks (`[0..11]`, four `0x00` bytes, `[16..size-1]`), rejecting any single-bit tamper with `WET_ERR_CRC_MISMATCH`.

### 6.5 Complete Opcode Reference Table (All 45 Instructions)

Verified directly against `compiler/isa.py`, `native/include/wetvm_types.h`, and `native/src/wetvm_vm.c`:

| Hex | Mnemonic | Operand Format | Bytes | Stack Effect (Before -> After) | Semantics & Runtime Error Conditions |
|---:|---|---|---:|---|---|
| `0x00` | `NOP` | *(none)* | 1 | `[] -> []` | Advances `pc += 1`. |
| `0x01` | `HALT` | *(none)* | 1 | `[] -> []` | Advances `pc += 1` and invokes `advance_simulation_tick` (yields final tick). |
| `0x02` | `SYNC_TICK` | *(none)* | 1 | `[] -> []` | Yields VM, advances biophysics + watchdogs by `dt = 0.1 ms`. |
| `0x03` | `SLEEP_TICKS` | `<H` (`ticks`) | 3 | `[] -> []` | Advances 1 tick immediately; if `ticks > 1`, sets `sleep_ticks_remaining = ticks - 1`. Errors: `WET_ERR_INVALID_OPCODE` if truncated. |
| `0x10` | `PUSH_CONST` | `<H` (`idx`) | 3 | `[] -> [val]` | Pushes `constants[idx]`. Errors: `WET_ERR_INVALID_OPCODE` (OOB index), `WET_ERR_STACK_OVERFLOW`. |
| `0x11` | `PUSH_INT` | `<i` (`int32`) | 5 | `[] -> [int]` | Pushes signed 32-bit integer (`WET_VAL_INT`). Errors: `WET_ERR_STACK_OVERFLOW`. |
| `0x12` | `PUSH_FLOAT` | `<f` (`float32`) | 5 | `[] -> [float]` | Pushes IEEE-754 float32 (`WET_VAL_FLOAT`). Errors: `WET_ERR_STACK_OVERFLOW`. |
| `0x13` | `POP` | *(none)* | 1 | `[a] -> []` | Discards top of stack. Errors: `WET_ERR_STACK_UNDERFLOW`. |
| `0x14` | `DUP` | *(none)* | 1 | `[a] -> [a, a]` | Duplicates top of stack. Errors: `WET_ERR_STACK_UNDERFLOW`, `WET_ERR_STACK_OVERFLOW`. |
| `0x15` | `SWAP` | *(none)* | 1 | `[a, b] -> [b, a]` | Swaps top two stack entries. Errors: `WET_ERR_STACK_UNDERFLOW` (`sp < 2`). |
| `0x16` | `LOAD_LOCAL` | `<H` (`slot`) | 3 | `[] -> [val]` | Pushes `locals[slot]`. Errors: `WET_ERR_INVALID_OPCODE` (`slot >= max_locals`), `WET_ERR_STACK_OVERFLOW`. |
| `0x17` | `STORE_LOCAL` | `<H` (`slot`) | 3 | `[val] -> []` | Pops value into `locals[slot]`. Errors: `WET_ERR_INVALID_OPCODE`, `WET_ERR_STACK_UNDERFLOW`. |
| `0x20` | `ADD_I` | *(none)* | 1 | `[a, b] -> [a + b]` | 32-bit integer addition (`to_int`). |
| `0x21` | `SUB_I` | *(none)* | 1 | `[a, b] -> [a - b]` | 32-bit integer subtraction. |
| `0x22` | `MUL_I` | *(none)* | 1 | `[a, b] -> [a * b]` | 32-bit integer multiplication (also emitted for logical `&&`). |
| `0x23` | `DIV_I` | *(none)* | 1 | `[a, b] -> [a / b]` | 32-bit integer division. Errors: `WET_ERR_DIVISION_BY_ZERO` if `b == 0`. |
| `0x24` | `ADD_F` | *(none)* | 1 | `[a, b] -> [a + b]` | Float32 addition (`to_float`). |
| `0x25` | `SUB_F` | *(none)* | 1 | `[a, b] -> [a - b]` | Float32 subtraction. |
| `0x26` | `MUL_F` | *(none)* | 1 | `[a, b] -> [a * b]` | Float32 multiplication. |
| `0x27` | `DIV_F` | *(none)* | 1 | `[a, b] -> [a / b]` | Float32 division. Errors: `WET_ERR_DIVISION_BY_ZERO` if `fabsf(b) < 1e-15f`. |
| `0x28` | `NEG` | *(none)* | 1 | `[a] -> [-a]` | Preserves `WET_VAL_FLOAT` or `WET_VAL_INT` tag and negates. |
| `0x29` | `MOD_I` | *(none)* | 1 | `[a, b] -> [a % b]` | 32-bit integer modulo remainder. Errors: `WET_ERR_DIVISION_BY_ZERO` if `b == 0`. |
| `0x30` | `CMP_EQ` | *(none)* | 1 | `[a, b] -> [0\|1]` | Equality test (promotes to float32 if either operand is float); pushes `WET_VAL_INT`. |
| `0x31` | `CMP_NE` | *(none)* | 1 | `[a, b] -> [0\|1]` | Inequality test; pushes `WET_VAL_INT`. |
| `0x32` | `CMP_LT` | *(none)* | 1 | `[a, b] -> [0\|1]` | Less-than test; pushes `WET_VAL_INT`. |
| `0x33` | `CMP_LE` | *(none)* | 1 | `[a, b] -> [0\|1]` | Less-or-equal test; pushes `WET_VAL_INT`. |
| `0x34` | `CMP_GT` | *(none)* | 1 | `[a, b] -> [0\|1]` | Greater-than test; pushes `WET_VAL_INT`. |
| `0x35` | `CMP_GE` | *(none)* | 1 | `[a, b] -> [0\|1]` | Greater-or-equal test; pushes `WET_VAL_INT`. |
| `0x40` | `JMP` | `<h` (`rel`) | 3 | `[] -> []` | Unconditional branch to `instr_pc + rel`. Errors: `WET_ERR_INVALID_OPCODE` if target out of `[0, code_size]`. |
| `0x41` | `JMP_IF_TRUE` | `<h` (`rel`) | 3 | `[cond] -> []` | Pops `cond`; branches if `is_truthy(cond)`. Errors: `WET_ERR_STACK_UNDERFLOW`, `WET_ERR_INVALID_OPCODE`. |
| `0x42` | `JMP_IF_FALSE` | `<h` (`rel`) | 3 | `[cond] -> []` | Pops `cond`; branches if `!is_truthy(cond)`. |
| `0x43` | `CALL` | `<HB` (`fn`, `argc`) | 4 | `[a1..aN] -> [0]` | Pops `argc` arguments and pushes `int(0)` (external/stub call dispatch in v1.0). |
| `0x44` | `RET` | *(none)* | 1 | `[] -> []` | Pops `call_stack` frame if `call_sp > 0`, else advances `pc += 1`. |
| `0x50` | `STIM_BIPHASIC` | `<B` (`ch`) | 2 | `[V, p1, p2, ip] -> []` | Pops 4 stack args (`interphase`, `p2`, `p1`, `voltage`), checks channel bounds, interlock lock, and capabilities (`CAP_STIMULATION`, `CAP_HIGH_VOLTAGE` if `\|V\| > 0.8 V`), discharges pending phase-2 counter-charge, clamps `V` to `[-1.2, +1.2] V`, schedules biphasic pulse. Errors: `WET_ERR_OUT_OF_BOUNDS_CH`, `WET_ERR_INTERLOCK_LOCKED`, `WET_ERR_CAPABILITY_DENIED`. |
| `0x51` | `READ_SPIKES` | `<B` (`ch`) | 2 | `[win_ms] -> [cnt]` | Pops `window_ms` (clamped to `[0.1, 50.0] ms`), pushes integer spike count from 500-tick rolling history. Errors: `WET_ERR_OUT_OF_BOUNDS_CH`. |
| `0x52` | `READ_VOLTAGE` | `<B` (`ch`) | 2 | `[] -> [V]` | Pushes `bio.mea_voltage_v[ch]` (`WET_VAL_FLOAT`, in Volts). Errors: `WET_ERR_OUT_OF_BOUNDS_CH`. |
| `0x53` | `MODULATE_STDP` | `<BB` (`pre`, `post`) | 3 | `[dw] -> []` | Checks `CAP_PLASTICITY` and bounds. If `pre == 0 && post == 0`, sets global `bio.stdp_lr_scale = dw`; if `pre != post`, updates `synapses[pre][post].weight_ns` clamped to `[0, 40] nS`. Errors: `WET_ERR_OUT_OF_BOUNDS_CH`, `WET_ERR_CAPABILITY_DENIED`, `WET_ERR_INTERLOCK_LOCKED`. |
| `0x54` | `GET_POP_RATE` | *(none)* | 1 | `[win_ms] -> [Hz]` | Pops window arg, pushes `bio.population_rate_hz` (`WET_VAL_FLOAT`). |
| `0x55` | `MEA_CONFIG` | `<BB` (`r`, `c`) | 3 | `[] -> []` | Sets `vm->grid_rows = r`, `vm->grid_cols = c`. |
| `0x56` | `PUMP_SET_RATE` | `<B` (`port`) | 2 | `[rate] -> []` | Sets volumetric flow rate on microfluidic pump port (`rate` in uL/min). Enforces `CAP_MICROFLUIDICS` and hydrodynamic shear stress limit ($Q \le 15.0\,\mu\text{L/min}$). Errors: `WET_ERR_SHEAR_STRESS_EXCEEDED`, `WET_ERR_CAPABILITY_DENIED`. |
| `0x57` | `PUMP_DISPENSE` | `<B` (`port`) | 2 | `[vol, rate] -> []` | Dispenses bolus volume at given flow rate. Errors: `WET_ERR_SHEAR_STRESS_EXCEEDED`, `WET_ERR_CAPABILITY_DENIED`. |
| `0x58` | `VALVE_SET` | `<B` (`port`) | 2 | `[state] -> []` | Actuates micro-pinch valve on port (`0 = closed`, `1 = open`). Updates hardware valve register. Errors: `WET_ERR_CAPABILITY_DENIED`. |
| `0x59` | `MOTOR_STEP` | `<BB` (`axis`, `dir`) | 3 | `[steps, speed] -> []` | Drives precision stepper motor along physical incubator axis. Enforces `CAP_MOTOR_ACTUATION`. Errors: `WET_ERR_CAPABILITY_DENIED`. |
| `0x5A` | `READ_PRESSURE` | `<B` (`sensor_id`) | 2 | `[] -> [kPa]` | Pushes microfluidic bioreactor chamber pressure (`WET_VAL_FLOAT`, in kPa). |
| `0x5B` | `READ_TEMPERATURE` | `<B` (`sensor_id`) | 2 | `[] -> [degC]` | Pushes chamber incubator temperature (`WET_VAL_FLOAT`, in degrees Celsius). |

> **Implementation Detail Note:** Notice that `STIM_BIPHASIC` (`0x50`) pops **four** values from the stack (`interphase`, `phase2`, `phase1`, `voltage` in LIFO order, matching `BytecodeEmitter.visit_StimStmtNode()`, which always pushes a `0.0f` default for `interphase` when omitted), and `GET_POP_RATE` (`0x54`) pops one window argument pushed by `read_population_rate(window_ms)`.
