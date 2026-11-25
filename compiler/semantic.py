"""
WetLang Compiler - Multi-Pass Semantic Analyzer & Safety Verifier
Hand-crafted from first principles.

Pass 1: Scope & Symbol Resolution, MEA Electrode Coordinate Bounds Checking.
Pass 2: Type Checking, Dimensional Homogeneity, and Static Voltage Clamp Check.
Pass 3: Control Flow Graph (CFG) Construction & Loop-Yield Verification.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Set, Tuple, Any
from compiler.lexer import Lexer
from compiler.parser import Parser

from compiler.token import Dimension
from compiler.ast_nodes import (
    ASTNode,
    ASTVisitor,
    ProgramNode,
    OrganoidDeclNode,
    ConnectDeclNode,
    PortDeclNode,
    GridDeclNode,
    ChannelDeclNode,
    FnDeclNode,
    ParamNode,
    StreamDeclNode,
    StreamItemNode,
    BlockNode,
    LetStmtNode,
    AssignStmtNode,
    StimStmtNode,
    ModulateStmtNode,
    SyncTickStmtNode,
    IfStmtNode,
    WhileStmtNode,
    ForStmtNode,
    ReturnStmtNode,
    ExprStmtNode,
    BinaryOpNode,
    UnaryOpNode,
    LiteralNode,
    PhysicalLiteralNode,
    IdentifierNode,
    CallNode,
    IndexNode,
    RangeNode,
    DomainCallNode,
)


@dataclass
class Diagnostic:
    file: str
    line: int
    column: int
    severity: str  # "error" or "warning"
    code: str
    message: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file": self.file,
            "line": self.line,
            "column": self.column,
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
        }


class SemanticError(Exception):
    """Raised when static semantics or safety invariants are violated."""
    def __init__(self, message: str, line: int = 0, column: int = 0, error_code: str = ""):
        self.error_code = error_code
        self.line = line
        self.column = column
        prefix = f"{error_code}: " if error_code else ""
        super().__init__(f"SemanticError at line {line}, column {column}: {prefix}{message}")


class Symbol:
    def __init__(self, name: str, type_name: str, dimension: Dimension = Dimension.NONE, is_mut: bool = False, node: Optional[ASTNode] = None):
        self.name: str = name
        self.type_name: str = type_name
        self.dimension: Dimension = dimension
        self.is_mut: bool = is_mut
        self.node: Optional[ASTNode] = node


class Scope:
    def __init__(self, parent: Optional["Scope"] = None, name: str = "block"):
        self.parent: Optional["Scope"] = parent
        self.name: str = name
        self.symbols: Dict[str, Symbol] = {}

    def define(self, symbol: Symbol) -> None:
        self.symbols[symbol.name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        if name in self.symbols:
            return self.symbols[name]
        if self.parent is not None:
            return self.parent.resolve(name)
        return None

    def is_local(self, name: str) -> bool:
        return name in self.symbols


class SemanticAnalyzer:
    """
    Orchestrates the 3-pass semantic analysis and safety verification.
    """
    def __init__(
        self,
        program: ProgramNode,
        collect_diagnostics: bool = False,
        filename: str = "<stdin>",
        max_unsynced_ticks: int = 1000
    ):
        self.program: ProgramNode = program
        self.collect_diagnostics: bool = collect_diagnostics
        self.filename: str = filename
        self.max_unsynced_ticks: int = max_unsynced_ticks
        self.diagnostics: List[Diagnostic] = []
        self.global_scope: Scope = Scope(parent=None, name="global")
        self.current_scope: Scope = self.global_scope
        self.mea_grids: Dict[str, Tuple[int, int]] = {} # grid_name -> (rows, cols)
        self.node_dimensions: Dict[int, Dimension] = {}
        self.const_int_values: Dict[str, int] = {}
        self.electrode_area_um2: float = 5000.0
        self.j_limit_ua_cm2: float = 30.0
        self.z_magnitude_ohms: float = 100000.0
        self.dynamic_eis_clamp_enabled: bool = False

    def report_error(self, message: str, line: int = 0, column: int = 0, error_code: str = "ERR_SEMANTIC", severity: str = "error") -> None:
        diag = Diagnostic(
            file=self.filename,
            line=line,
            column=column,
            severity=severity,
            code=error_code,
            message=message
        )
        self.diagnostics.append(diag)
        if not self.collect_diagnostics and severity == "error":
            raise SemanticError(message, line, column, error_code)

    def analyze(self) -> None:
        """Run all verification passes in sequence."""
        # Pre-populate global built-ins
        self._init_builtins()

        # Pass 1: Symbol resolution and coordinate bounds checking
        self._pass1_symbols_and_bounds()

        # Pass 2: Type checking, dimensional arithmetic, and static voltage clamp check
        self._pass2_types_and_dimensions()

        # Pass 3: Static loop-yield verification (CFG analysis)
        self._pass3_loop_yield_verifier()

    def _init_builtins(self) -> None:
        builtins = [
            ("read_spikes", "fn", Dimension.NONE),
            ("read_voltage", "fn", Dimension.VOLTAGE),
            ("pop_firing_rate", "fn", Dimension.FREQUENCY),
            ("read_population_rate", "fn", Dimension.FREQUENCY),
            ("abs", "fn", Dimension.NONE),
            ("float", "fn", Dimension.NONE),
            ("int", "fn", Dimension.NONE),
            ("exp", "fn", Dimension.NONE),
            ("log", "fn", Dimension.NONE),
            ("ln", "fn", Dimension.NONE),
            ("sqrt", "fn", Dimension.NONE),
            ("pow", "fn", Dimension.NONE),
            ("sin", "fn", Dimension.NONE),
            ("cos", "fn", Dimension.NONE),
            ("tanh", "fn", Dimension.NONE),
        ]
        for name, tname, dim in builtins:
            self.global_scope.define(Symbol(name, tname, dimension=dim))

    # =========================================================================
    # PASS 1: Scope, Symbol Resolution & MEA Coordinate Bounds
    # =========================================================================

    def _pass1_symbols_and_bounds(self) -> None:
        visitor = _Pass1Visitor(self)
        visitor.visit(self.program)

    # =========================================================================
    # PASS 2: Types, Dimensional Checking & Voltage Clamp
    # =========================================================================

    def _pass2_types_and_dimensions(self) -> None:
        visitor = _Pass2Visitor(self)
        visitor.visit(self.program)
        self.node_dimensions = visitor.node_dimensions

    # =========================================================================
    # PASS 3: Static Loop-Yield Verifier (CFG Post-Dominance)
    # =========================================================================

    def _pass3_loop_yield_verifier(self) -> None:
        visitor = _Pass3LoopYieldVisitor(self)
        visitor.visit(self.program)


# =========================================================================
# Pass 1 Visitor
# =========================================================================

class _Pass1Visitor(ASTVisitor):
    def __init__(self, analyzer: SemanticAnalyzer):
        self.analyzer: SemanticAnalyzer = analyzer
        self.const_int_values: Dict[str, int] = {}
        self.ref_channels: set = set()
        self.rec_only_channels: set = set()
        self.ref_channel_indices: set = set()
        self.rec_only_channel_indices: set = set()

    def visit_ProgramNode(self, node: ProgramNode) -> None:
        for decl in node.declarations:
            self.visit(decl)

    def visit_GridDeclNode(self, node: GridDeclNode) -> None:
        if self.analyzer.current_scope.is_local(node.name):
            self.analyzer.report_error(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")

        rows = 8
        cols = 8
        if isinstance(node.rows, LiteralNode) and node.rows.type_name == "int":
            rows = int(node.rows.value)
        if isinstance(node.cols, LiteralNode) and node.cols.type_name == "int":
            cols = int(node.cols.value)

        if rows < 1 or rows > 255 or cols < 1 or cols > 255:
            self.analyzer.report_error(
                f"Grid dimensions must be in range 1..255 (got {rows}x{cols}). For high-density connectomes exceeding 255x255, partition into subgrids or route via the AER event engine.",
                node.line, node.column, "ERR_INVALID_GRID_DIMENSIONS"
            )
            self.analyzer.current_scope.define(Symbol(node.name, "grid", Dimension.NONE, False, node))
            return

        self.analyzer.mea_grids[node.name] = (rows, cols)
        self.analyzer.current_scope.define(Symbol(node.name, "grid", Dimension.NONE, False, node))

    def visit_ChannelDeclNode(self, node: ChannelDeclNode) -> None:
        if self.analyzer.current_scope.is_local(node.name):
            self.analyzer.report_error(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")

        # Verify target coordinate literal bounds
        self._check_coordinate_bounds(node.target)
        mode_str = str(node.mode) if node.mode else ""
        ch_idx = self._extract_channel_index(node.target)
        if mode_str in ("Reference", "ref", "Ref", "reference"):
            self.ref_channels.add(node.name)
            if ch_idx is not None:
                self.ref_channel_indices.add(ch_idx)
        elif mode_str in ("RecordingOnly", "record", "Rec", "SpikeReadout", "rec"):
            self.rec_only_channels.add(node.name)
            if ch_idx is not None:
                self.rec_only_channel_indices.add(ch_idx)
        self.analyzer.current_scope.define(Symbol(node.name, "channel", Dimension.NONE, False, node))

    def _extract_channel_index(self, node: ASTNode) -> Optional[int]:
        if isinstance(node, IndexNode):
            if len(node.indices) == 2:
                r = self._extract_int_constant(node.indices[0])
                c = self._extract_int_constant(node.indices[1])
                if r is not None and c is not None:
                    return r * 8 + c
            elif len(node.indices) == 1:
                return self._extract_int_constant(node.indices[0])
        elif isinstance(node, (LiteralNode, IdentifierNode)):
            return self._extract_int_constant(node)
        return None

    def visit_OrganoidDeclNode(self, node: OrganoidDeclNode) -> None:
        if self.analyzer.current_scope.is_local(node.name):
            self.analyzer.report_error(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
        self.analyzer.current_scope.define(Symbol(node.name, "organoid", Dimension.NONE, False, node))
        if node.properties:
            for k, v in node.properties.items():
                k_lower = str(k).lower()
                if "impedance" in k_lower or "z_mag" in k_lower:
                    val = self._extract_float_from_node(v)
                    if val is not None:
                        self.analyzer.z_magnitude_ohms = val
                        self.analyzer.dynamic_eis_clamp_enabled = True
                elif "area" in k_lower:
                    val = self._extract_float_from_node(v)
                    if val is not None:
                        self.analyzer.electrode_area_um2 = val
                elif "eis" in k_lower or "clamp" in k_lower:
                    self.analyzer.dynamic_eis_clamp_enabled = True

    def _extract_float_from_node(self, node: Any) -> Optional[float]:
        if isinstance(node, PhysicalLiteralNode):
            return float(node.si_value)
        if isinstance(node, LiteralNode) and node.type_name in ("int", "float"):
            return float(node.value)
        if isinstance(node, (int, float)):
            return float(node)
        return None

    def visit_ConnectDeclNode(self, node: ConnectDeclNode) -> None:
        pass

    def visit_PortDeclNode(self, node: PortDeclNode) -> None:
        if self.analyzer.current_scope.is_local(node.name):
            self.analyzer.report_error(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
        self.analyzer.current_scope.define(Symbol(node.name, "port", Dimension.NONE, False, node))

    def visit_FnDeclNode(self, node: FnDeclNode) -> None:
        if self.analyzer.current_scope.is_local(node.name):
            self.analyzer.report_error(f"Redeclared function '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")

        self.analyzer.current_scope.define(Symbol(node.name, "fn", Dimension.NONE, False, node))

        # Enter function scope
        fn_scope = Scope(parent=self.analyzer.current_scope, name=f"fn_{node.name}")
        prev_scope = self.analyzer.current_scope
        self.analyzer.current_scope = fn_scope

        for param in node.params:
            if fn_scope.is_local(param.name):
                self.analyzer.report_error(f"Duplicate parameter '{param.name}' in function '{node.name}'", param.line, param.column, "ERR_REDECLARED_IDENTIFIER")
            fn_scope.define(Symbol(param.name, param.type_name, self._type_to_dimension(param.type_name), False, param))

        self.visit(node.body)
        self.analyzer.current_scope = prev_scope

    def visit_StreamDeclNode(self, node: StreamDeclNode) -> None:
        if self.analyzer.current_scope.is_local(node.name):
            self.analyzer.report_error(f"Redeclared stream '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")
        self.analyzer.current_scope.define(Symbol(node.name, "stream", Dimension.NONE, False, node))

        stream_scope = Scope(parent=self.analyzer.current_scope, name=f"stream_{node.name}")
        prev_scope = self.analyzer.current_scope
        self.analyzer.current_scope = stream_scope

        for item in node.items:
            if item.kind == "cycle" and item.cycle_block is not None:
                self.visit(item.cycle_block)

        self.analyzer.current_scope = prev_scope

    def visit_BlockNode(self, node: BlockNode) -> None:
        block_scope = Scope(parent=self.analyzer.current_scope, name="block")
        prev_scope = self.analyzer.current_scope
        self.analyzer.current_scope = block_scope

        for stmt in node.statements:
            self.visit(stmt)

        self.analyzer.current_scope = prev_scope

    def visit_LetStmtNode(self, node: LetStmtNode) -> None:
        if self.analyzer.current_scope.is_local(node.name):
            self.analyzer.report_error(f"Redeclared identifier '{node.name}'", node.line, node.column, "ERR_REDECLARED_IDENTIFIER")

        dim = self._type_to_dimension(node.type_name) if node.type_name else Dimension.NONE
        self.analyzer.current_scope.define(Symbol(node.name, node.type_name or "inferred", dim, node.is_mut, node))
        if node.initializer is not None:
            self.visit(node.initializer)
            val = self._extract_int_constant(node.initializer)
            if val is not None and not node.is_mut:
                self.const_int_values[node.name] = val
                self.analyzer.const_int_values[node.name] = val

    def visit_AssignStmtNode(self, node: AssignStmtNode) -> None:
        self.visit(node.target)
        self.visit(node.value)

    def visit_StimStmtNode(self, node: StimStmtNode) -> None:
        self._check_coordinate_bounds(node.channel)
        ch_idx = self._extract_channel_index(node.channel)
        if ch_idx is not None:
            if ch_idx in self.ref_channel_indices:
                self.analyzer.report_error(
                    f"Electrode channel index {ch_idx} is declared as a reference channel and cannot be stimulated",
                    node.line, node.column, "ERR_STIM_ON_REFERENCE_CHANNEL"
                )
            if ch_idx in self.rec_only_channel_indices:
                self.analyzer.report_error(
                    f"Electrode channel index {ch_idx} is declared in a recording-only channel bank and cannot be stimulated",
                    node.line, node.column, "ERR_STIM_ON_RECORDING_CHANNEL"
                )
        if isinstance(node.channel, IdentifierNode):
            if node.channel.name in self.ref_channels:
                self.analyzer.report_error(
                    f"Electrode channel '{node.channel.name}' is declared as a reference channel and cannot be stimulated",
                    node.line, node.column, "ERR_STIM_ON_REFERENCE_CHANNEL"
                )
            if node.channel.name in self.rec_only_channels:
                self.analyzer.report_error(
                    f"Electrode channel '{node.channel.name}' is declared in a recording-only channel bank and cannot be stimulated",
                    node.line, node.column, "ERR_STIM_ON_RECORDING_CHANNEL"
                )
        self.visit(node.channel)
        self.visit(node.voltage)
        self.visit(node.phase1)
        self.visit(node.phase2)
        if node.interphase is not None:
            self.visit(node.interphase)

    def visit_ModulateStmtNode(self, node: ModulateStmtNode) -> None:
        for arg in node.args:
            self.visit(arg)

    def visit_SyncTickStmtNode(self, node: SyncTickStmtNode) -> None:
        if node.count is not None:
            self.visit(node.count)

    def visit_IfStmtNode(self, node: IfStmtNode) -> None:
        self.visit(node.condition)
        self.visit(node.then_block)
        if node.else_block is not None:
            self.visit(node.else_block)

    def visit_WhileStmtNode(self, node: WhileStmtNode) -> None:
        self.visit(node.condition)
        self.visit(node.body)

    def visit_ForStmtNode(self, node: ForStmtNode) -> None:
        for_scope = Scope(parent=self.analyzer.current_scope, name="for")
        prev_scope = self.analyzer.current_scope
        self.analyzer.current_scope = for_scope

        for_scope.define(Symbol(node.var_name, "int", Dimension.NONE, False, node))
        self.visit(node.range_start)
        self.visit(node.range_end)
        self.visit(node.body)

        self.analyzer.current_scope = prev_scope

    def visit_ReturnStmtNode(self, node: ReturnStmtNode) -> None:
        if node.value is not None:
            self.visit(node.value)

    def visit_ExprStmtNode(self, node: ExprStmtNode) -> None:
        self.visit(node.expr)

    def visit_BinaryOpNode(self, node: BinaryOpNode) -> None:
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOpNode(self, node: UnaryOpNode) -> None:
        self.visit(node.operand)

    def visit_CallNode(self, node: CallNode) -> None:
        self.visit(node.callee)
        for arg in node.args:
            self.visit(arg)

    def visit_IndexNode(self, node: IndexNode) -> None:
        self._check_coordinate_bounds(node)
        self.visit(node.target)
        for idx in node.indices:
            self.visit(idx)

    def visit_DomainCallNode(self, node: DomainCallNode) -> None:
        if node.func_name in ("read_spikes", "read_voltage") and len(node.args) > 0:
            self._check_coordinate_bounds(node.args[0])
        elif node.func_name == "pump_set_rate" and len(node.args) >= 2:
            rate_node = node.args[1]
            if isinstance(rate_node, PhysicalLiteralNode):
                val = float(rate_node.magnitude)
                if rate_node.unit_suffix == "mL/min":
                    val *= 1000.0
                if val < 0.0 or val > 15.0:
                    self.analyzer.report_error(
                        f"Requested pump rate {val:.2f} uL/min exceeds safe hydrodynamic shear limit (0..15.0 uL/min)",
                        node.line, node.column, "ERR_SHEAR_STRESS_EXCEEDED"
                    )

                # Geometry-Aware Shear Stress Check:
                # Uses Shah-London rectangular duct friction factor with aspect ratio alpha = min(h/w, w/h)
                # If optional channel dimensions are passed as args: pump_set_rate(ch, rate, width, height)
                if len(node.args) >= 4:
                    w_node, h_node = node.args[2], node.args[3]
                    w_um = getattr(w_node, "magnitude", 1000.0) if isinstance(w_node, PhysicalLiteralNode) else 1000.0
                    h_um = getattr(h_node, "magnitude", 200.0) if isinstance(h_node, PhysicalLiteralNode) else 200.0
                    # Convert Q to m^3/s: val uL/min * 1e-9 m^3/uL / 60 s/min
                    q_m3_s = (val * 1e-9) / 60.0
                    w_m = float(w_um) * 1e-6
                    h_m = float(h_um) * 1e-6
                    # Physiological dynamic viscosity of protein-supplemented neural media at 37°C:
                    mu = 0.00078  # Pa*s (0.78 mPa*s / 0.78 cP)

                    # Shah-London aspect-ratio correction for rectangular microchannels:
                    # Peak wall shear stress scales from 1.0x (alpha -> 0) to 1.43x (alpha = 1, square duct).
                    alpha = min(h_m / w_m, w_m / h_m) if w_m > 0 and h_m > 0 else 0.2
                    geom_factor = 1.0 + 0.43 * alpha
                    tau_w = geom_factor * (6.0 * mu * q_m3_s) / (w_m * (h_m ** 2))
                    if tau_w > 0.05: # 0.05 Pa maximum safe shear stress for neurites
                        self.analyzer.report_error(
                            f"Hydrodynamic Shear Stress Exceeded: Wall shear stress tau_w = {tau_w:.3f} Pa "
                            f"exceeds physiological threshold (0.05 Pa) in {w_um:.0f}x{h_um:.0f} um channel at {val:.2f} uL/min",
                            node.line, node.column, "ERR_SHEAR_STRESS_EXCEEDED"
                        )
        for arg in node.args:
            self.visit(arg)

    def visit_IdentifierNode(self, node: IdentifierNode) -> None:
        sym = self.analyzer.current_scope.resolve(node.name)
        if sym is None:
            # Check if it's a known grid
            if node.name not in self.analyzer.mea_grids:
                self.analyzer.report_error(f"Undeclared identifier '{node.name}'", node.line, node.column, "ERR_UNDECLARED_IDENTIFIER")

    def _check_coordinate_bounds(self, node: ASTNode) -> None:
        """Verifies literal MEA coordinate bounds: (r, c) in [0..rows-1]x[0..cols-1], linear in [0..total-1]."""
        # Determine active grid bounds from declared grids, defaulting to 8x8 (64 channels)
        max_r, max_c, max_total = 8, 8, 64
        if self.analyzer.mea_grids:
            first_grid = next(iter(self.analyzer.mea_grids.values()))
            max_r, max_c = first_grid
            max_total = max_r * max_c

        if isinstance(node, IndexNode):
            # Check 2D indexing: mea[r, c]
            if len(node.indices) == 2:
                r_node = node.indices[0]
                c_node = node.indices[1]
                r_val = self._extract_int_constant(r_node)
                c_val = self._extract_int_constant(c_node)

                if r_val is not None:
                    if r_val < 0 or r_val >= max_r:
                        self.analyzer.report_error(
                            f"Electrode row coordinate {r_val} is out of bounds [0..{max_r - 1}]",
                            node.line,
                            node.column,
                            "ERR_ELECTRODE_OUT_OF_BOUNDS"
                        )
                if c_val is not None:
                    if c_val < 0 or c_val >= max_c:
                        self.analyzer.report_error(
                            f"Electrode col coordinate {c_val} is out of bounds [0..{max_c - 1}]",
                            node.line,
                            node.column,
                            "ERR_ELECTRODE_OUT_OF_BOUNDS"
                        )

            # Check 1D indexing: mea[k]
            elif len(node.indices) == 1:
                k_node = node.indices[0]
                k_val = self._extract_int_constant(k_node)
                if k_val is not None:
                    if k_val < 0 or k_val >= max_total:
                        self.analyzer.report_error(
                            f"Electrode linear channel {k_val} is out of bounds [0..{max_total - 1}]",
                            node.line,
                            node.column,
                            "ERR_ELECTRODE_OUT_OF_BOUNDS"
                        )
        elif isinstance(node, (LiteralNode, UnaryOpNode, BinaryOpNode)):
            k_val = self._extract_int_constant(node)
            if k_val is not None:
                if k_val < 0 or k_val >= max_total:
                    self.analyzer.report_error(
                        f"Electrode channel coordinate {k_val} is out of bounds [0..{max_total - 1}]",
                        node.line,
                        node.column,
                        "ERR_ELECTRODE_OUT_OF_BOUNDS"
                    )

    def _extract_int_constant(self, node: ASTNode) -> Optional[int]:
        if isinstance(node, LiteralNode) and node.type_name == "int":
            return int(node.value)
        if isinstance(node, UnaryOpNode):
            inner = self._extract_int_constant(node.operand)
            if inner is None:
                return None
            if node.op == "-":
                return -inner
            if node.op == "+":
                return inner
            return None
        if isinstance(node, BinaryOpNode):
            left = self._extract_int_constant(node.left)
            right = self._extract_int_constant(node.right)
            if left is None or right is None:
                return None
            if node.op == "+":
                return left + right
            if node.op == "-":
                return left - right
            if node.op == "*":
                return left * right
            if node.op == "/":
                if right == 0:
                    return None
                return left // right
            if node.op == "%":
                if right == 0:
                    return None
                return left % right
            return None
        if isinstance(node, IdentifierNode):
            if hasattr(self, "const_int_values") and node.name in self.const_int_values:
                return self.const_int_values[node.name]
        return None

    def _type_to_dimension(self, tname: Optional[str]) -> Dimension:
        if not tname:
            return Dimension.NONE
        mapping = {
            "Voltage": Dimension.VOLTAGE,
            "Current": Dimension.CURRENT,
            "Time": Dimension.TIME,
            "Frequency": Dimension.FREQUENCY,
            "Length": Dimension.LENGTH,
            "Charge": Dimension.CHARGE,
            "Resistance": Dimension.RESISTANCE,
            "Conductance": Dimension.CONDUCTANCE,
        }
        return mapping.get(tname, Dimension.NONE)


# =========================================================================
# Pass 2 Visitor
# =========================================================================

class _Pass2Visitor(ASTVisitor):
    def __init__(self, analyzer: SemanticAnalyzer):
        self.analyzer: SemanticAnalyzer = analyzer
        self.current_scope: Scope = analyzer.global_scope
        self.node_dimensions: Dict[int, Dimension] = {}
        self.const_values: Dict[str, float] = {}
        self.known_values: Dict[str, Optional[float]] = {}

    def visit_ProgramNode(self, node: ProgramNode) -> None:
        for decl in node.declarations:
            self.visit(decl)

    def visit_OrganoidDeclNode(self, node: OrganoidDeclNode) -> None:
        # Phase 3 & v2.1 Biophysics: Spherical Reaction-Diffusion (Thiele Modulus & Sherwood Scaling) Anoxia Model.
        # Living neural organoids in culture baths are avascular spheres.
        # Steady-state spherical diffusion equation with metabolic oxygen consumption R_met:
        #   (1/r^2) d/dr (r^2 dC/dr) = R_met / D_eff
        # In quiescent fluid (unperfused, Re -> 0, Sh = 2), the Robin boundary condition couples
        # internal mass transport to external boundary layer diffusion:
        #   -D_eff (dC/dr)|_R = k_c * (C_bulk - C_surface), where k_c = Sh * D_media / (2 * R_org)
        # Yielding surface concentration depression:
        #   C_surface = C_bulk - (R_met * R_org^2) / (3 * D_media)
        # Critical penetration depth before core anoxia C(0) <= 0:
        #   R_crit = sqrt(6 * D_eff * C_surface / R_met) ~= 200 um under quiescent conditions.
        # Under active laminar perfusion (Re > 0, Sc ~ 350), Sherwood number scales via
        # Acrivos-Taylor / Froessling relation: Sh = 2 + 0.6 * Re^(1/2) * Sc^(1/3), restoring C_surface -> C_bulk.
        if node.radius is not None:
            r_val = getattr(node.radius, "si_value", 0.0)
            r_um = r_val * 1e6

            # 1. Unperfused threshold: R > 200 um without perfusion causes core necrosis
            # (Quiescent Nernst boundary layer starvation: Sh = 2 causes C_surface << C_bulk)
            if r_val > 0.000200 and node.perfusion is None:
                self.analyzer.report_error(
                    f"Spherical Diffusion Anoxia Violation: organoid '{node.name}' has radius > 200 um "
                    f"({r_um:.1f} um) requiring active microfluidic perfusion (Sherwood boundary layer starvation)",
                    node.line, node.column, "ERR_KROGH_ANOXIA_VIOLATION"
                )

            # 2. Avascular physical diffusion limit: R > 250 um causes central necrosis
            # even with 100% saturated external perfusion, due to internal diffusion limits
            # unless structural micro-channels, air-liquid interface slicing, or vascularization exist.
            if r_val > 0.000250 and node.perfusion is not None:
                props = getattr(node, "properties", {})
                is_vascularized = False
                for key in ("vascularized", "sliced_ali", "internal_channel", "slice"):
                    if key in props:
                        val = props[key]
                        val_str = str(getattr(val, "value", getattr(val, "name", str(val)))).lower()
                        if val_str in ("true", "1"):
                            is_vascularized = True
                            break

                if not is_vascularized:
                    self.analyzer.report_error(
                        f"Avascular Core Necrosis Violation: organoid '{node.name}' radius {r_um:.1f} um "
                        f"exceeds the avascular spherical diffusion limit (250 um). External perfusion cannot "
                        f"prevent central anoxia due to internal tissue diffusion limits (D_eff = 1.07e-9 m^2/s). "
                        f"Requires 'vascularized: true', 'sliced_ali: true', or 'internal_channel: true'.",
                        node.line, node.column, "ERR_AVASCULAR_CORE_NECROSIS"
                    )

    def visit_ConnectDeclNode(self, node: ConnectDeclNode) -> None:
        src_name = getattr(node.source, "name", None)
        tgt_name = getattr(node.target, "name", None)
        if src_name and not self.current_scope.resolve(src_name):
            self.analyzer.report_error(f"Undefined connect source '{src_name}'", node.line, node.column, "ERR_UNDEFINED_IDENTIFIER")
        if tgt_name and not self.current_scope.resolve(tgt_name):
            self.analyzer.report_error(f"Undefined connect target '{tgt_name}'", node.line, node.column, "ERR_UNDEFINED_IDENTIFIER")

    def visit_PortDeclNode(self, node: PortDeclNode) -> None:
        pass

    def visit_FnDeclNode(self, node: FnDeclNode) -> None:
        fn_scope = Scope(parent=self.current_scope, name=f"fn_{node.name}")
        for param in node.params:
            dim = self._type_to_dimension(param.type_name)
            fn_scope.define(Symbol(param.name, param.type_name, dim))
        prev = self.current_scope
        self.current_scope = fn_scope
        self.visit(node.body)
        self.current_scope = prev

    def visit_BlockNode(self, node: BlockNode) -> None:
        block_scope = Scope(parent=self.current_scope, name="block")
        prev = self.current_scope
        self.current_scope = block_scope
        for stmt in node.statements:
            self.visit(stmt)
        self.current_scope = prev

    def visit_LetStmtNode(self, node: LetStmtNode) -> None:
        init_dim = Dimension.NONE
        if node.initializer is not None:
            self.visit(node.initializer)
            init_dim = self.get_dimension(node.initializer)
            val = self._extract_float_si_value(node.initializer)
            if val is not None:
                self.known_values[node.name] = val
                if not node.is_mut:
                    self.const_values[node.name] = val
            else:
                self.known_values[node.name] = None
        else:
            self.known_values[node.name] = None

        declared_dim = self._type_to_dimension(node.type_name) if node.type_name else Dimension.NONE
        if declared_dim != Dimension.NONE and init_dim != Dimension.NONE and declared_dim != init_dim:
            self.analyzer.report_error(
                f"Cannot assign dimension {init_dim.value} to variable '{node.name}' declared with dimension {declared_dim.value}",
                node.line,
                node.column,
                "ERR_DIMENSIONAL_MISMATCH"
            )

        final_dim = declared_dim if declared_dim != Dimension.NONE else init_dim
        self.current_scope.define(Symbol(node.name, node.type_name or "inferred", final_dim))

    def visit_AssignStmtNode(self, node: AssignStmtNode) -> None:
        self.visit(node.value)
        val_dim = self.get_dimension(node.value)
        if isinstance(node.target, IdentifierNode):
            val = self._extract_float_si_value(node.value)
            self.known_values[node.target.name] = val
            sym = self.current_scope.resolve(node.target.name)
            if sym is not None and sym.dimension != Dimension.NONE and val_dim != Dimension.NONE and sym.dimension != val_dim:
                self.analyzer.report_error(
                    f"Cannot assign dimension {val_dim.value} to variable '{node.target.name}' with dimension {sym.dimension.value}",
                    node.line,
                    node.column,
                    "ERR_DIMENSIONAL_MISMATCH"
                )

    def _collect_assigned_names(self, node: Optional[ASTNode], out: Set[str]) -> None:
        if node is None:
            return
        if isinstance(node, AssignStmtNode) and isinstance(node.target, IdentifierNode):
            out.add(node.target.name)
        elif isinstance(node, BlockNode):
            for s in node.statements:
                self._collect_assigned_names(s, out)
        elif isinstance(node, IfStmtNode):
            self._collect_assigned_names(node.then_block, out)
            self._collect_assigned_names(node.else_block, out)
        elif isinstance(node, (WhileStmtNode, ForStmtNode)):
            self._collect_assigned_names(node.body, out)

    def visit_IfStmtNode(self, node: IfStmtNode) -> None:
        self.visit(node.condition)
        saved = dict(self.known_values)
        self.visit(node.then_block)
        self.known_values = dict(saved)
        if node.else_block is not None:
            self.visit(node.else_block)
        self.known_values = saved
        assigned: Set[str] = set()
        self._collect_assigned_names(node, assigned)
        for name in assigned:
            self.known_values[name] = None

    def visit_WhileStmtNode(self, node: WhileStmtNode) -> None:
        assigned: Set[str] = set()
        self._collect_assigned_names(node.body, assigned)
        for name in assigned:
            self.known_values[name] = None
        self.visit(node.condition)
        self.visit(node.body)
        for name in assigned:
            self.known_values[name] = None

    def visit_ForStmtNode(self, node: ForStmtNode) -> None:
        assigned: Set[str] = set()
        self._collect_assigned_names(node.body, assigned)
        for name in assigned:
            self.known_values[name] = None
        for_scope = Scope(parent=self.current_scope, name="for")
        for_scope.define(Symbol(node.var_name, "int", Dimension.NONE))
        prev = self.current_scope
        self.current_scope = for_scope
        self.visit(node.range_start)
        self.visit(node.range_end)
        self.known_values[node.var_name] = None
        self.visit(node.body)
        self.current_scope = prev
        for name in assigned:
            self.known_values[name] = None

    def visit_StimStmtNode(self, node: StimStmtNode) -> None:
        self.visit(node.channel)
        self.visit(node.voltage)
        self.visit(node.phase1)
        self.visit(node.phase2)
        if node.interphase is not None:
            self.visit(node.interphase)

        v_val = self._extract_float_si_value(node.voltage)
        dim_val = self.get_dimension(node.voltage)

        # 0. Check non-negative pulse durations
        tau1 = self._extract_float_si_value(node.phase1)
        tau2 = self._extract_float_si_value(node.phase2)
        tau_ip = self._extract_float_si_value(node.interphase) if node.interphase is not None else None

        if tau1 is not None and tau1 < 0:
            self.analyzer.report_error(
                f"Stimulation phase1 duration cannot be negative ({tau1 * 1000.0:.3f} ms)",
                node.phase1.line, node.phase1.column, "ERR_INVALID_STIM_DURATION"
            )
        if tau2 is not None and tau2 < 0:
            self.analyzer.report_error(
                f"Stimulation phase2 duration cannot be negative ({tau2 * 1000.0:.3f} ms)",
                node.phase2.line, node.phase2.column, "ERR_INVALID_STIM_DURATION"
            )
        if tau_ip is not None and tau_ip < 0:
            self.analyzer.report_error(
                f"Stimulation interphase duration cannot be negative ({tau_ip * 1000.0:.3f} ms)",
                node.interphase.line, node.interphase.column, "ERR_INVALID_STIM_DURATION"
            )

        # 1. Compile-time overvoltage clamp check: |V| > 1.2 V
        if v_val is None:
            self.analyzer.report_error(
                "Stimulation amplitude cannot be statically verified within [+/- 1.2 V] safety bounds",
                node.voltage.line,
                node.voltage.column,
                "W_UNVERIFIED_STIM_BOUNDS",
                severity="warning"
            )
        elif dim_val in (Dimension.VOLTAGE, Dimension.NONE):
            if abs(v_val) > 1.2 + 1e-9:
                self.analyzer.report_error(
                    f"Requested stimulation voltage {v_val:.3f} V exceeds hard safety clamp [+/- 1.2 V]",
                    node.voltage.line,
                    node.voltage.column,
                    "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED"
                )

        # 2. Dynamic EIS current density clamp check:
        # Faradaic current density limit J = 30 uA/cm^2, default Area = 5000 um^2 = 5e-5 cm^2
        # I_safe = J * Area = 30e-6 A/cm^2 * 5e-5 cm^2 = 1.5e-9 A (1.5 nA = 0.0015 uA)
        area_cm2 = self.analyzer.electrode_area_um2 * 1e-8
        j_limit_a_cm2 = self.analyzer.j_limit_ua_cm2 * 1e-6
        i_safe_a = j_limit_a_cm2 * area_cm2

        if v_val is not None:
            if dim_val == Dimension.CURRENT:
                i_actual_a = abs(v_val)
                if i_actual_a > i_safe_a + 1e-15:
                    self.analyzer.report_error(
                        f"Stimulation current {i_actual_a * 1e6:.4f} uA exceeds safe Faradaic current density limit of {self.analyzer.j_limit_ua_cm2:.1f} uA/cm^2 (I_safe = {i_safe_a * 1e6:.4f} uA)",
                        node.voltage.line,
                        node.voltage.column,
                        "ERR_DYNAMIC_EIS_CLAMP_VIOLATION"
                    )
            elif dim_val == Dimension.VOLTAGE:
                if self.analyzer.dynamic_eis_clamp_enabled:
                    v_safe_mag = i_safe_a * self.analyzer.z_magnitude_ohms
                    if abs(v_val) > v_safe_mag + 1e-9:
                        self.analyzer.report_error(
                            f"Stimulation voltage {abs(v_val):.4f} V exceeds dynamic EIS impedance clamp {v_safe_mag:.4f} V (J_limit = {self.analyzer.j_limit_ua_cm2:.1f} uA/cm^2, Z = {self.analyzer.z_magnitude_ohms:.0f} Ohm)",
                            node.voltage.line,
                            node.voltage.column,
                            "ERR_DYNAMIC_EIS_CLAMP_VIOLATION"
                        )

        # 3. Charge limit check per phase (Phase 1, Phase 2) and biphasic net charge balance: Q <= 0.5 nC
        p1_dim = self.get_dimension(node.phase1)
        p2_dim = self.get_dimension(node.phase2)
        if v_val is not None and tau1 is not None and tau2 is not None:
            if dim_val == Dimension.CURRENT:
                q1_c = abs(v_val) * tau1
                q2_c = abs(v_val) * tau2
                if q1_c > 0.5e-9 + 1e-15:
                    self.analyzer.report_error(
                        f"Stimulation phase1 charge {q1_c * 1e9:.3f} nC exceeds maximum safe charge limit (0.500 nC)",
                        node.line,
                        node.column,
                        "ERR_CHARGE_LIMIT_VIOLATION"
                    )
                if q2_c > 0.5e-9 + 1e-15:
                    self.analyzer.report_error(
                        f"Stimulation phase2 charge {q2_c * 1e9:.3f} nC exceeds maximum safe charge limit (0.500 nC)",
                        node.line,
                        node.column,
                        "ERR_CHARGE_LIMIT_VIOLATION"
                    )
                if abs(q1_c - q2_c) > 0.5e-9 + 1e-15:
                    self.analyzer.report_error(
                        f"Biphasic net charge imbalance {abs(q1_c - q2_c) * 1e9:.3f} nC exceeds maximum safe limit (0.500 nC)",
                        node.line,
                        node.column,
                        "ERR_CHARGE_LIMIT_VIOLATION"
                    )
            elif (
                dim_val == Dimension.VOLTAGE
                and self.analyzer.dynamic_eis_clamp_enabled
                and self.analyzer.z_magnitude_ohms > 0.0
                and p1_dim == Dimension.TIME
                and p2_dim == Dimension.TIME
            ):
                i_est_a = abs(v_val) / self.analyzer.z_magnitude_ohms
                q1_c = i_est_a * tau1
                q2_c = i_est_a * tau2
                if q1_c > 0.5e-9 + 1e-15 or q2_c > 0.5e-9 + 1e-15:
                    max_q_nc = max(q1_c, q2_c) * 1e9
                    self.analyzer.report_error(
                        f"Voltage-mode stimulation charge per phase {max_q_nc:.3f} nC exceeds maximum safe limit (0.500 nC at Z={self.analyzer.z_magnitude_ohms:.0f} Ohm)",
                        node.line,
                        node.column,
                        "ERR_CHARGE_LIMIT_VIOLATION"
                    )
                if abs(q1_c - q2_c) > 0.5e-9 + 1e-15:
                    self.analyzer.report_error(
                        f"Voltage-mode biphasic net charge imbalance {abs(q1_c - q2_c) * 1e9:.3f} nC exceeds maximum safe limit (0.500 nC)",
                        node.line,
                        node.column,
                        "ERR_CHARGE_LIMIT_VIOLATION"
                    )

        # Also check duration symmetry even if voltage amplitude is only known as matching phases
        if tau1 is not None and tau2 is not None and p1_dim == Dimension.TIME and p2_dim == Dimension.TIME:
            if tau1 > 0.0 and tau2 > 0.0 and abs(tau1 - tau2) > max(tau1, tau2) * 0.5 and dim_val == Dimension.CURRENT and v_val is not None:
                pass  # already covered by |q1 - q2| above

    def visit_BinaryOpNode(self, node: BinaryOpNode) -> None:
        self.visit(node.left)
        self.visit(node.right)
        left_dim = self.get_dimension(node.left)
        right_dim = self.get_dimension(node.right)

        # Addition and Subtraction require dimensional homogeneity (including Dimension vs NONE)
        if node.op in ("+", "-"):
            if left_dim != right_dim:
                self.analyzer.report_error(
                    f"Cannot perform '{node.op}' between incompatible dimensions {left_dim.value} and {right_dim.value}",
                    node.line,
                    node.column,
                    "ERR_DIMENSIONAL_MISMATCH"
                )
            res_dim = left_dim if left_dim != Dimension.NONE else right_dim
            self.node_dimensions[id(node)] = res_dim

        # Multiplication
        elif node.op == "*":
            if (left_dim == Dimension.CURRENT and right_dim == Dimension.TIME) or \
               (left_dim == Dimension.TIME and right_dim == Dimension.CURRENT):
                self.node_dimensions[id(node)] = Dimension.CHARGE
            elif (left_dim == Dimension.CURRENT and right_dim == Dimension.RESISTANCE) or \
                 (left_dim == Dimension.RESISTANCE and right_dim == Dimension.CURRENT):
                # Ohm's Law: V = I * R
                self.node_dimensions[id(node)] = Dimension.VOLTAGE
            elif (left_dim == Dimension.VOLTAGE and right_dim == Dimension.CONDUCTANCE) or \
                 (left_dim == Dimension.CONDUCTANCE and right_dim == Dimension.VOLTAGE):
                # Ohm's Law: I = V * G
                self.node_dimensions[id(node)] = Dimension.CURRENT
            elif left_dim == Dimension.NONE:
                self.node_dimensions[id(node)] = right_dim
            elif right_dim == Dimension.NONE:
                self.node_dimensions[id(node)] = left_dim
            else:
                self.node_dimensions[id(node)] = Dimension.NONE

        # Division
        elif node.op == "/":
            if left_dim == right_dim and left_dim != Dimension.NONE:
                self.node_dimensions[id(node)] = Dimension.NONE
            elif left_dim == Dimension.CHARGE and right_dim == Dimension.TIME:
                self.node_dimensions[id(node)] = Dimension.CURRENT
            elif left_dim == Dimension.CHARGE and right_dim == Dimension.CURRENT:
                self.node_dimensions[id(node)] = Dimension.TIME
            elif left_dim == Dimension.VOLTAGE and right_dim == Dimension.CURRENT:
                # Ohm's Law: V / I = R (Resistance, Ohms)
                self.node_dimensions[id(node)] = Dimension.RESISTANCE
            elif left_dim == Dimension.CURRENT and right_dim == Dimension.VOLTAGE:
                # Ohm's Law: I / V = G (Conductance, Siemens)
                self.node_dimensions[id(node)] = Dimension.CONDUCTANCE
            elif left_dim == Dimension.VOLTAGE and right_dim == Dimension.RESISTANCE:
                # Ohm's Law: V / R = I (Current, Amperes)
                self.node_dimensions[id(node)] = Dimension.CURRENT
            elif left_dim == Dimension.CURRENT and right_dim == Dimension.CONDUCTANCE:
                # Ohm's Law: I / G = V (Voltage, Volts)
                self.node_dimensions[id(node)] = Dimension.VOLTAGE
            elif left_dim == Dimension.NONE and right_dim == Dimension.RESISTANCE:
                # 1 / R = G (Conductance, Siemens)
                self.node_dimensions[id(node)] = Dimension.CONDUCTANCE
            elif left_dim == Dimension.NONE and right_dim == Dimension.CONDUCTANCE:
                # 1 / G = R (Resistance, Ohms)
                self.node_dimensions[id(node)] = Dimension.RESISTANCE
            elif right_dim == Dimension.NONE:
                self.node_dimensions[id(node)] = left_dim
            else:
                self.node_dimensions[id(node)] = Dimension.NONE

        # Relational and Equality
        elif node.op in ("==", "!=", "<", "<=", ">", ">="):
            if left_dim != right_dim:
                self.analyzer.report_error(
                    f"Cannot compare incompatible dimensions {left_dim.value} and {right_dim.value}",
                    node.line,
                    node.column,
                    "ERR_DIMENSIONAL_MISMATCH"
                )
            self.node_dimensions[id(node)] = Dimension.NONE

        else:
            self.node_dimensions[id(node)] = Dimension.NONE

    def visit_UnaryOpNode(self, node: UnaryOpNode) -> None:
        self.visit(node.operand)
        operand_dim = self.get_dimension(node.operand)
        self.node_dimensions[id(node)] = operand_dim

    def visit_PhysicalLiteralNode(self, node: PhysicalLiteralNode) -> None:
        self.node_dimensions[id(node)] = node.dimension
        try:
            val = float(getattr(node, "si_value", getattr(node, "magnitude", 0.0)))
            if abs(val) > 3.402823466e38:
                self.analyzer.report_error(
                    f"Physical literal {getattr(node, 'magnitude', val)} exceeds 32-bit single-precision floating point limits (+/- 3.4028235e+38)",
                    node.line, node.column, "ERR_FLOAT_OVERFLOW"
                )
        except (ValueError, OverflowError):
            self.analyzer.report_error(
                f"Physical literal overflowed IEEE 754 limits",
                node.line, node.column, "ERR_FLOAT_OVERFLOW"
            )

    def visit_LiteralNode(self, node: LiteralNode) -> None:
        self.node_dimensions[id(node)] = Dimension.NONE
        if node.type_name == "float":
            try:
                val = float(node.value)
                if abs(val) > 3.402823466e38:
                    self.analyzer.report_error(
                        f"Float literal {node.value} exceeds 32-bit single-precision floating point limits (+/- 3.4028235e+38)",
                        node.line, node.column, "ERR_FLOAT_OVERFLOW"
                    )
            except (ValueError, OverflowError):
                self.analyzer.report_error(
                    f"Float literal {node.value} overflowed IEEE 754 limits",
                    node.line, node.column, "ERR_FLOAT_OVERFLOW"
                )

    def visit_IdentifierNode(self, node: IdentifierNode) -> None:
        sym = self.current_scope.resolve(node.name)
        if sym is not None:
            self.node_dimensions[id(node)] = sym.dimension
        else:
            self.node_dimensions[id(node)] = Dimension.NONE

    def visit_CallNode(self, node: CallNode) -> None:
        self.visit(node.callee)
        for arg in node.args:
            self.visit(arg)

        callee_name = None
        if isinstance(node.callee, IdentifierNode):
            callee_name = node.callee.name

        # Enforce dimensionless operands for transcendental functions
        transcendental_fns = {"exp", "log", "ln", "sin", "cos", "tanh"}
        if callee_name in transcendental_fns:
            for idx, arg in enumerate(node.args):
                arg_dim = self.get_dimension(arg)
                if arg_dim != Dimension.NONE:
                    self.analyzer.report_error(
                        f"Transcendental function '{callee_name}' requires dimensionless arguments, but argument {idx+1} has physical dimension '{arg_dim.value}'",
                        node.line, node.column, "ERR_DIMENSIONAL_MISMATCH"
                    )
            self.node_dimensions[id(node)] = Dimension.NONE
            return

        if callee_name == "sqrt":
            if node.args:
                arg_dim = self.get_dimension(node.args[0])
                if arg_dim != Dimension.NONE:
                    self.analyzer.report_error(
                        f"Square root function 'sqrt' requires dimensionless argument, got dimension '{arg_dim.value}'",
                        node.line, node.column, "ERR_DIMENSIONAL_MISMATCH"
                    )
            self.node_dimensions[id(node)] = Dimension.NONE
            return

        if callee_name == "pow":
            if len(node.args) >= 2:
                base_dim = self.get_dimension(node.args[0])
                exp_dim = self.get_dimension(node.args[1])
                if exp_dim != Dimension.NONE:
                    self.analyzer.report_error(
                        f"Exponent in 'pow' must be dimensionless, got '{exp_dim.value}'",
                        node.line, node.column, "ERR_DIMENSIONAL_MISMATCH"
                    )
                self.node_dimensions[id(node)] = base_dim if base_dim == Dimension.NONE else Dimension.NONE
            return

        if callee_name == "abs":
            if node.args:
                self.node_dimensions[id(node)] = self.get_dimension(node.args[0])
            else:
                self.node_dimensions[id(node)] = Dimension.NONE
            return

        # Lookup function in current scope for return dimension
        if callee_name:
            sym = self.current_scope.resolve(callee_name)
            if sym is not None:
                self.node_dimensions[id(node)] = sym.dimension
            else:
                self.node_dimensions[id(node)] = Dimension.NONE
        else:
            self.node_dimensions[id(node)] = Dimension.NONE

    def _type_to_dimension(self, tname: Optional[str]) -> Dimension:
        if not tname:
            return Dimension.NONE
        mapping = {
            "Voltage": Dimension.VOLTAGE,
            "Current": Dimension.CURRENT,
            "Time": Dimension.TIME,
            "Frequency": Dimension.FREQUENCY,
            "Length": Dimension.LENGTH,
            "Charge": Dimension.CHARGE,
            "Resistance": Dimension.RESISTANCE,
            "Conductance": Dimension.CONDUCTANCE,
        }
        return mapping.get(tname, Dimension.NONE)

    def get_dimension(self, node: ASTNode) -> Dimension:
        return self.node_dimensions.get(id(node), Dimension.NONE)

    def _extract_float_si_value(self, node: ASTNode) -> Optional[float]:
        if isinstance(node, PhysicalLiteralNode):
            return float(node.si_value)
        if isinstance(node, LiteralNode) and node.type_name in ("int", "float"):
            return float(node.value)
        if isinstance(node, UnaryOpNode):
            sub = self._extract_float_si_value(node.operand)
            if sub is None:
                return None
            if node.op == "-":
                return -sub
            if node.op == "+":
                return sub
            return None
        if isinstance(node, BinaryOpNode):
            left = self._extract_float_si_value(node.left)
            right = self._extract_float_si_value(node.right)
            if left is None or right is None:
                return None
            if node.op == "+":
                return left + right
            if node.op == "-":
                return left - right
            if node.op == "*":
                return left * right
            if node.op == "/":
                if abs(right) < 1e-15:
                    return None
                return left / right
            return None
        if isinstance(node, IdentifierNode):
            if hasattr(self, "known_values") and node.name in self.known_values:
                return self.known_values[node.name]
            if hasattr(self, "const_values") and node.name in self.const_values:
                return self.const_values[node.name]
        return None


# =========================================================================
# Pass 3 Visitor: Loop-Yield Verification (CFG Post-Dominance)
# =========================================================================

class _Pass3LoopYieldVisitor(ASTVisitor):
    def __init__(self, analyzer: SemanticAnalyzer):
        self.analyzer: SemanticAnalyzer = analyzer
        self.var_init_values: Dict[str, Optional[int]] = {}
        self.fn_decls: Dict[str, FnDeclNode] = {}
        self.fn_all_paths_yield: Dict[str, bool] = {}
        self.fn_exits_unyielded_stim: Dict[str, Optional[ASTNode]] = {}

    def _collect_fn_decls(self, program: ProgramNode) -> None:
        self.fn_decls.clear()
        for decl in program.declarations:
            if isinstance(decl, FnDeclNode):
                self.fn_decls[decl.name] = decl
        self._compute_fn_summaries()

    def _collect_calls(self, node: Optional[ASTNode], out: List[CallNode]) -> None:
        if node is None:
            return
        if isinstance(node, CallNode):
            out.append(node)
            self._collect_calls(node.callee, out)
            for a in node.args:
                self._collect_calls(a, out)
        elif isinstance(node, ExprStmtNode):
            self._collect_calls(node.expr, out)
        elif isinstance(node, LetStmtNode):
            self._collect_calls(node.initializer, out)
        elif isinstance(node, AssignStmtNode):
            self._collect_calls(node.value, out)
        elif isinstance(node, ReturnStmtNode):
            self._collect_calls(node.value, out)
        elif isinstance(node, BinaryOpNode):
            self._collect_calls(node.left, out)
            self._collect_calls(node.right, out)
        elif isinstance(node, UnaryOpNode):
            self._collect_calls(node.operand, out)
        elif isinstance(node, BlockNode):
            for s in node.statements:
                self._collect_calls(s, out)
        elif isinstance(node, IfStmtNode):
            self._collect_calls(node.condition, out)
            self._collect_calls(node.then_block, out)
            self._collect_calls(node.else_block, out)

    def _compute_fn_summaries(self) -> None:
        self.fn_all_paths_yield = {name: False for name in self.fn_decls}
        self.fn_exits_unyielded_stim = {name: None for name in self.fn_decls}

        # Fixed-point iteration over function call graph
        changed = True
        while changed:
            changed = False
            for name, fn in self.fn_decls.items():
                new_yield = self._all_paths_yield_sync_tick(fn.body)
                if new_yield != self.fn_all_paths_yield[name]:
                    self.fn_all_paths_yield[name] = new_yield
                    changed = True

                new_stim = self._check_unyielded_stim_path(fn.body, unyielded_stim=None)
                if (new_stim is not None) != (self.fn_exits_unyielded_stim[name] is not None):
                    self.fn_exits_unyielded_stim[name] = new_stim
                    changed = True

    def visit_ProgramNode(self, node: ProgramNode) -> None:
        self._collect_fn_decls(node)
        for decl in node.declarations:
            self.visit(decl)

    def visit_FnDeclNode(self, node: FnDeclNode) -> None:
        saved = dict(self.var_init_values)
        for p in node.params:
            self.var_init_values[p.name] = None
        self.visit(node.body)
        self.var_init_values = saved

    def visit_BlockNode(self, node: BlockNode) -> None:
        saved = dict(self.var_init_values)
        for stmt in node.statements:
            self.visit(stmt)
        # Propagate assignments to variables declared in outer scope
        for k in list(saved.keys()):
            if k in self.var_init_values:
                saved[k] = self.var_init_values[k]
        self.var_init_values = saved

    def visit_LetStmtNode(self, node: LetStmtNode) -> None:
        if node.initializer is not None:
            self.var_init_values[node.name] = self._extract_int_constant(node.initializer)
        else:
            self.var_init_values[node.name] = None

    def visit_AssignStmtNode(self, node: AssignStmtNode) -> None:
        if isinstance(node.target, IdentifierNode):
            self.var_init_values[node.target.name] = self._extract_int_constant(node.value)

    def _collect_assigned_var_names(self, node: Optional[ASTNode], out: Set[str]) -> None:
        if node is None:
            return
        if isinstance(node, AssignStmtNode) and isinstance(node.target, IdentifierNode):
            out.add(node.target.name)
        elif isinstance(node, BlockNode):
            for s in node.statements:
                self._collect_assigned_var_names(s, out)
        elif isinstance(node, IfStmtNode):
            self._collect_assigned_var_names(node.then_block, out)
            self._collect_assigned_var_names(node.else_block, out)
        elif isinstance(node, (WhileStmtNode, ForStmtNode)):
            self._collect_assigned_var_names(node.body, out)

    def visit_IfStmtNode(self, node: IfStmtNode) -> None:
        saved = dict(self.var_init_values)
        self.visit(node.then_block)
        self.var_init_values = dict(saved)
        if node.else_block is not None:
            self.visit(node.else_block)
        self.var_init_values = saved
        assigned: Set[str] = set()
        self._collect_assigned_var_names(node, assigned)
        for name in assigned:
            self.var_init_values[name] = None

    def visit_WhileStmtNode(self, node: WhileStmtNode) -> None:
        self._verify_loop_yield(node.body, loop_node=node, loop_name="while", line=node.line, column=node.column)
        assigned: Set[str] = set()
        self._collect_assigned_var_names(node.body, assigned)
        saved = dict(self.var_init_values)
        for name in assigned:
            self.var_init_values[name] = None
        self.visit(node.body)
        self.var_init_values = saved
        for name in assigned:
            self.var_init_values[name] = None

    def visit_ForStmtNode(self, node: ForStmtNode) -> None:
        self._verify_loop_yield(node.body, loop_node=node, loop_name="for", line=node.line, column=node.column)
        assigned: Set[str] = set()
        self._collect_assigned_var_names(node.body, assigned)
        saved = dict(self.var_init_values)
        self.var_init_values[node.var_name] = None
        for name in assigned:
            self.var_init_values[name] = None
        self.visit(node.body)
        self.var_init_values = saved
        for name in assigned:
            self.var_init_values[name] = None

    def visit_StreamDeclNode(self, node: StreamDeclNode) -> None:
        for item in node.items:
            if item.kind == "cycle" and item.cycle_block is not None:
                self._verify_loop_yield(item.cycle_block, loop_node=None, loop_name="cycle", line=item.line, column=item.column)
                self.visit(item.cycle_block)

    def _verify_loop_yield(self, body: BlockNode, loop_node: Optional[ASTNode], loop_name: str, line: int, column: int) -> None:
        """
        Linear-time O(V + E) Control-Flow Graph (CFG) Reachability Analysis.
        Verifies that:
        1. Every cyclic path containing a stim_biphasic statement is post-dominated by a mandatory sync_tick (ERR_UNBOUNDED_STIM_LOOP).
        2. Loops lacking guaranteed sync_tick on all acyclic paths are statically bounded below MAX_UNSYNCED_TICKS (ERR_UNSYNCED_LOOP).
        """
        violating_stim = self._check_unyielded_stim_path(body, unyielded_stim=None)
        if violating_stim is not None:
            self.analyzer.report_error(
                f"Stimulation loop without mandatory 'sync_tick' yield. "
                f"Unbounded stimulation loop detected in '{loop_name}' block at line {line}",
                violating_stim.line,
                violating_stim.column,
                "ERR_UNBOUNDED_STIM_LOOP"
            )
            return

        all_paths_yield = self._all_paths_yield_sync_tick(body)
        if not all_paths_yield:
            bound = self._estimate_loop_bound(loop_node)
            max_ticks = getattr(self.analyzer, "max_unsynced_ticks", 1000)
            if bound is None or bound >= max_ticks:
                self.analyzer.report_error(
                    f"Loop lacking guaranteed 'sync_tick' on all paths is not statically bounded below {max_ticks} ticks (bound={bound}) in '{loop_name}' block at line {line}",
                    line,
                    column,
                    "ERR_UNSYNCED_LOOP"
                )

    def _min_loop_step(self, node: ASTNode, var_name: str, direction: int) -> Optional[int]:
        """
        Returns the guaranteed net progress of 'var_name' in 'direction' (+1 or -1)
        across all acyclic paths through 'node', or None if unknown/non-monotonic.
        """
        if isinstance(node, BlockNode):
            total = 0
            for stmt in node.statements:
                delta = self._min_loop_step(stmt, var_name, direction)
                if delta is None:
                    return None
                total += delta
            return total
        if isinstance(node, IfStmtNode):
            if node.else_block is None:
                then_d = self._min_loop_step(node.then_block, var_name, direction)
                if then_d is None or then_d < 0:
                    return None
                return 0
            then_d = self._min_loop_step(node.then_block, var_name, direction)
            else_d = self._min_loop_step(node.else_block, var_name, direction)
            if then_d is None or else_d is None:
                return None
            return min(then_d, else_d)
        if isinstance(node, AssignStmtNode) and isinstance(node.target, IdentifierNode):
            if node.target.name != var_name:
                return 0
            val = node.value
            if isinstance(val, BinaryOpNode) and isinstance(val.left, IdentifierNode) and val.left.name == var_name:
                step = self._extract_int_constant(val.right)
                if step is None:
                    return None
                if val.op == "+":
                    signed_step = step * direction
                    return signed_step if signed_step >= 0 else None
                if val.op == "-":
                    signed_step = (-step) * direction
                    return signed_step if signed_step >= 0 else None
            return None
        if isinstance(node, (WhileStmtNode, ForStmtNode)):
            assigned: Set[str] = set()
            self._collect_assigned_var_names(node.body, assigned)
            if var_name in assigned:
                return None
            return 0
        return 0

    def _estimate_loop_bound(self, node: Optional[ASTNode]) -> Optional[int]:
        if node is None:
            return None
        if isinstance(node, ForStmtNode):
            start = self._extract_int_constant(node.range_start)
            end = self._extract_int_constant(node.range_end)
            if start is not None and end is not None:
                return max(0, end - start)
            return None
        elif isinstance(node, WhileStmtNode):
            cond = node.condition
            if isinstance(cond, BinaryOpNode):
                if cond.op in ("<", "<=") and isinstance(cond.left, IdentifierNode):
                    var_name = cond.left.name
                    limit = self._extract_int_constant(cond.right)
                    init_val = self.var_init_values.get(var_name)
                    if init_val is None and hasattr(self.analyzer, "const_int_values"):
                        init_val = self.analyzer.const_int_values.get(var_name)
                    if limit is not None and init_val is not None:
                        step = self._min_loop_step(node.body, var_name, direction=+1)
                        if step is None or step <= 0:
                            return None
                        diff = (limit - init_val) if cond.op == "<" else (limit - init_val + 1)
                        if diff <= 0:
                            return 0
                        return (diff + step - 1) // step
                elif cond.op in (">", ">="):
                    if isinstance(cond.right, IdentifierNode):
                        # e.g. limit > var  <=>  var < limit
                        var_name = cond.right.name
                        limit = self._extract_int_constant(cond.left)
                        init_val = self.var_init_values.get(var_name)
                        if init_val is None and hasattr(self.analyzer, "const_int_values"):
                            init_val = self.analyzer.const_int_values.get(var_name)
                        if limit is not None and init_val is not None:
                            step = self._min_loop_step(node.body, var_name, direction=+1)
                            if step is None or step <= 0:
                                return None
                            diff = (limit - init_val) if cond.op == ">" else (limit - init_val + 1)
                            if diff <= 0:
                                return 0
                            return (diff + step - 1) // step
                    elif isinstance(cond.left, IdentifierNode):
                        # e.g. var > limit (counting down)
                        var_name = cond.left.name
                        limit = self._extract_int_constant(cond.right)
                        init_val = self.var_init_values.get(var_name)
                        if init_val is None and hasattr(self.analyzer, "const_int_values"):
                            init_val = self.analyzer.const_int_values.get(var_name)
                        if limit is not None and init_val is not None:
                            step = self._min_loop_step(node.body, var_name, direction=-1)
                            if step is None or step <= 0:
                                return None
                            diff = (init_val - limit) if cond.op == ">" else (init_val - limit + 1)
                            if diff <= 0:
                                return 0
                            return (diff + step - 1) // step
            return None
        return None

    def _extract_int_constant(self, node: ASTNode) -> Optional[int]:
        if isinstance(node, LiteralNode) and node.type_name == "int":
            return int(node.value)
        if isinstance(node, UnaryOpNode):
            inner = self._extract_int_constant(node.operand)
            if inner is None:
                return None
            if node.op == "-":
                return -inner
            if node.op == "+":
                return inner
            return None
        if isinstance(node, BinaryOpNode):
            left = self._extract_int_constant(node.left)
            right = self._extract_int_constant(node.right)
            if left is None or right is None:
                return None
            if node.op == "+":
                return left + right
            if node.op == "-":
                return left - right
            if node.op == "*":
                return left * right
            return None
        if isinstance(node, IdentifierNode):
            if node.name in self.var_init_values:
                return self.var_init_values[node.name]
            if hasattr(self.analyzer, "const_int_values") and node.name in self.analyzer.const_int_values:
                return self.analyzer.const_int_values[node.name]
        return None

    def _all_paths_yield_sync_tick(self, node: ASTNode) -> bool:
        if isinstance(node, SyncTickStmtNode):
            return True
        if isinstance(node, ExprStmtNode) and isinstance(node.expr, CallNode):
            return self._all_paths_yield_sync_tick(node.expr)
        if isinstance(node, CallNode) and isinstance(node.callee, IdentifierNode):
            return self.fn_all_paths_yield.get(node.callee.name, False)
        if isinstance(node, BlockNode):
            for stmt in node.statements:
                if self._all_paths_yield_sync_tick(stmt):
                    return True
            return False
        if isinstance(node, IfStmtNode):
            if node.else_block is None:
                return False
            then_yields = self._all_paths_yield_sync_tick(node.then_block)
            else_yields = self._all_paths_yield_sync_tick(node.else_block)
            return then_yields and else_yields
        if isinstance(node, (WhileStmtNode, ForStmtNode)):
            return False
        return False

    def _check_unyielded_stim_path(self, node: ASTNode, unyielded_stim: Optional[ASTNode]) -> Optional[ASTNode]:
        """
        Recursively checks if there exists a control-flow path from 'node' to the exit of the block
        carrying an active unyielded stimulation statement without a post-dominating sync_tick.
        Returns the first violating ASTNode if an unyielded path exists, or None if all paths safely yield.
        """
        if isinstance(node, StimStmtNode):
            return node

        elif isinstance(node, SyncTickStmtNode):
            return None

        elif isinstance(node, ExprStmtNode):
            calls: List[CallNode] = []
            self._collect_calls(node.expr, calls)
            curr = unyielded_stim
            for c in calls:
                curr = self._check_unyielded_stim_path(c, curr)
            return curr

        elif isinstance(node, CallNode):
            curr = unyielded_stim
            for arg in node.args:
                arg_calls: List[CallNode] = []
                self._collect_calls(arg, arg_calls)
                for c in arg_calls:
                    curr = self._check_unyielded_stim_path(c, curr)
            if isinstance(node.callee, IdentifierNode):
                fname = node.callee.name
                if self.fn_exits_unyielded_stim.get(fname) is not None:
                    return node
                if self.fn_all_paths_yield.get(fname, False):
                    return None
            return curr

        elif isinstance(node, (LetStmtNode, AssignStmtNode, ReturnStmtNode)):
            expr = node.initializer if isinstance(node, LetStmtNode) else node.value
            calls = []
            self._collect_calls(expr, calls)
            curr = unyielded_stim
            for c in calls:
                curr = self._check_unyielded_stim_path(c, curr)
            return curr

        elif isinstance(node, BlockNode):
            curr_stim = unyielded_stim
            for stmt in node.statements:
                if isinstance(stmt, SyncTickStmtNode):
                    curr_stim = None
                elif isinstance(stmt, StimStmtNode):
                    curr_stim = stmt
                elif isinstance(stmt, IfStmtNode):
                    then_stim = self._check_unyielded_stim_path(stmt.then_block, curr_stim)
                    if stmt.else_block is not None:
                        else_stim = self._check_unyielded_stim_path(stmt.else_block, curr_stim)
                    else:
                        else_stim = curr_stim  # Fall-through branch inherits incoming stim!

                    # Out of the if/else construct, if either branch carries unyielded stim:
                    curr_stim = then_stim if then_stim is not None else else_stim
                elif isinstance(stmt, BlockNode):
                    curr_stim = self._check_unyielded_stim_path(stmt, curr_stim)
                elif isinstance(stmt, (WhileStmtNode, ForStmtNode)):
                    # Inner loops cannot guarantee yield for an outer loop's path
                    pass
                else:
                    curr_stim = self._check_unyielded_stim_path(stmt, curr_stim)
            return curr_stim

        elif isinstance(node, IfStmtNode):
            then_stim = self._check_unyielded_stim_path(node.then_block, unyielded_stim)
            if node.else_block is not None:
                else_stim = self._check_unyielded_stim_path(node.else_block, unyielded_stim)
            else:
                else_stim = unyielded_stim
            return then_stim if then_stim is not None else else_stim

        return unyielded_stim

    def _contains_sync_tick(self, node: ASTNode) -> bool:
        if isinstance(node, SyncTickStmtNode):
            return True
        if isinstance(node, BlockNode):
            return any(self._contains_sync_tick(s) for s in node.statements)
        if isinstance(node, (WhileStmtNode, ForStmtNode)):
            # Inner loops cannot guarantee yield for an outer loop's path
            return False
        if isinstance(node, IfStmtNode):
            if node.else_block is None:
                return False
            then_has = self._contains_sync_tick(node.then_block)
            else_has = self._contains_sync_tick(node.else_block)
            return then_has and else_has
        return False


def check_source(source: str, filename: str = "<stdin>", max_unsynced_ticks: int = 1000) -> List[Diagnostic]:
    """
    Analyzes WetLang source code and returns a list of non-fatal diagnostics.
    Collects syntax, type, dimensional, biophysical, and CFG errors without crashing.
    """
    diagnostics: List[Diagnostic] = []

    # Step 1: Lexical Analysis
    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()
    except Exception as ex:
        line = getattr(ex, "line", 1)
        col = getattr(ex, "column", 1)
        code = getattr(ex, "error_code", "ERR_SYNTAX_LEXER")
        diagnostics.append(Diagnostic(file=filename, line=line, column=col, severity="error", code=code, message=str(ex)))
        return diagnostics

    # Step 2: Parsing
    try:
        parser = Parser(tokens, source_text=source)
        ast = parser.parse()
    except Exception as ex:
        line = getattr(ex, "line", 1)
        col = getattr(ex, "column", 1)
        code = getattr(ex, "error_code", "ERR_SYNTAX_PARSE")
        diagnostics.append(Diagnostic(file=filename, line=line, column=col, severity="error", code=code, message=str(ex)))
        return diagnostics

    # Step 3: Multi-Pass Semantic Analysis (Diagnostic Collection Mode)
    analyzer = SemanticAnalyzer(
        ast,
        collect_diagnostics=True,
        filename=filename,
        max_unsynced_ticks=max_unsynced_ticks
    )
    try:
        analyzer.analyze()
    except Exception as ex:
        line = getattr(ex, "line", 1)
        col = getattr(ex, "column", 1)
        code = getattr(ex, "error_code", "ERR_INTERNAL")
        analyzer.diagnostics.append(Diagnostic(file=filename, line=line, column=col, severity="error", code=code, message=str(ex)))

    return analyzer.diagnostics
