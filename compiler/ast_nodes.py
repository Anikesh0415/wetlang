"""
WetLang Compiler - Typed Abstract Syntax Tree (AST) Hierarchy
Hand-crafted from first principles. Complete visitor pattern interfaces.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict
from compiler.token import Dimension


@dataclass
class ASTNode:
    """Base class for all Abstract Syntax Tree nodes."""
    line: int = 0
    column: int = 0

    def accept(self, visitor: "ASTVisitor") -> Any:
        method_name = f"visit_{self.__class__.__name__}"
        visitor_fn = getattr(visitor, method_name, visitor.generic_visit)
        return visitor_fn(self)


# =========================================================================
# Top-Level & Declarations
# =========================================================================

@dataclass
class ProgramNode(ASTNode):
    declarations: List[ASTNode] = field(default_factory=list)


@dataclass
class OrganoidDeclNode(ASTNode):
    name: str = ""
    count: Optional[Any] = None  # None for single organoid, or int/expr for organoid array [N]
    cells: Optional[Any] = None
    radius: Optional[Any] = None
    perfusion: Optional[Any] = None
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ConnectDeclNode(ASTNode):
    source: ASTNode = None       # e.g. organoid_A or organoid_A.port
    target: ASTNode = None       # e.g. organoid_B or organoid_B.port
    delay_ms: Optional[Any] = None
    weight: Optional[Any] = None
    plasticity: Optional[str] = None


@dataclass
class PortDeclNode(ASTNode):
    name: str = ""
    channels: Any = None
    mode: Optional[str] = None


@dataclass
class GridDeclNode(ASTNode):
    name: str = ""
    rows: Any = None
    cols: Any = None
    pitch: Optional[Any] = None
    base_voltage: Optional[Any] = None


@dataclass
class ChannelDeclNode(ASTNode):
    name: str = ""
    target: ASTNode = None       # IndexNode, IdentifierNode, or RangeNode
    mode: Optional[str] = None   # "BiphasicStim", "SpikeReadout", etc.


@dataclass
class ParamNode(ASTNode):
    name: str = ""
    type_name: str = ""


@dataclass
class FnDeclNode(ASTNode):
    name: str = ""
    params: List[ParamNode] = field(default_factory=list)
    return_type: Optional[str] = None
    body: "BlockNode" = None


@dataclass
class StreamItemNode(ASTNode):
    kind: str = ""               # "bind_in", "bind_out", "cycle"
    left: Optional[str] = None
    right: Optional[str] = None
    cycle_block: Optional["BlockNode"] = None


@dataclass
class StreamDeclNode(ASTNode):
    name: str = ""
    items: List[StreamItemNode] = field(default_factory=list)


# =========================================================================
# Statements
# =========================================================================

@dataclass
class BlockNode(ASTNode):
    statements: List[ASTNode] = field(default_factory=list)


@dataclass
class LetStmtNode(ASTNode):
    name: str = ""
    is_mut: bool = False
    type_name: Optional[str] = None
    initializer: ASTNode = None


@dataclass
class AssignStmtNode(ASTNode):
    target: ASTNode = None       # IdentifierNode or IndexNode
    value: ASTNode = None


@dataclass
class StimStmtNode(ASTNode):
    channel: ASTNode = None
    voltage: ASTNode = None
    phase1: ASTNode = None
    phase2: ASTNode = None
    interphase: Optional[ASTNode] = None


@dataclass
class ModulateStmtNode(ASTNode):
    args: List[ASTNode] = field(default_factory=list)


@dataclass
class SyncTickStmtNode(ASTNode):
    count: Optional[ASTNode] = None


@dataclass
class IfStmtNode(ASTNode):
    condition: ASTNode = None
    then_block: BlockNode = None
    else_block: Optional[ASTNode] = None  # BlockNode or IfStmtNode


@dataclass
class WhileStmtNode(ASTNode):
    condition: ASTNode = None
    body: BlockNode = None


@dataclass
class ForStmtNode(ASTNode):
    var_name: str = ""
    range_start: ASTNode = None
    range_end: ASTNode = None
    body: BlockNode = None


@dataclass
class ReturnStmtNode(ASTNode):
    value: Optional[ASTNode] = None


@dataclass
class ExprStmtNode(ASTNode):
    expr: ASTNode = None


# =========================================================================
# Expressions
# =========================================================================

@dataclass
class BinaryOpNode(ASTNode):
    left: ASTNode = None
    op: str = ""
    right: ASTNode = None


@dataclass
class UnaryOpNode(ASTNode):
    op: str = ""
    operand: ASTNode = None


@dataclass
class LiteralNode(ASTNode):
    value: Any = None
    type_name: str = ""          # "int", "float", "bool", "string"


@dataclass
class PhysicalLiteralNode(ASTNode):
    magnitude: float = 0.0
    dimension: Dimension = Dimension.NONE
    si_value: float = 0.0
    unit_suffix: str = ""


@dataclass
class IdentifierNode(ASTNode):
    name: str = ""


@dataclass
class CallNode(ASTNode):
    callee: ASTNode = None
    args: List[ASTNode] = field(default_factory=list)


@dataclass
class IndexNode(ASTNode):
    target: ASTNode = None
    indices: List[ASTNode] = field(default_factory=list)


@dataclass
class RangeNode(ASTNode):
    start: ASTNode = None
    end: ASTNode = None


@dataclass
class DomainCallNode(ASTNode):
    func_name: str = ""          # "read_spikes", "read_voltage", "pop_firing_rate", "read_population_rate"
    args: List[ASTNode] = field(default_factory=list)


# =========================================================================
# AST Visitor Base Class
# =========================================================================

class ASTVisitor:
    """Base class for AST visitors with double-dispatch."""
    def visit(self, node: ASTNode) -> Any:
        if node is None:
            return None
        return node.accept(self)

    def generic_visit(self, node: ASTNode) -> Any:
        for attr, value in node.__dict__.items():
            if isinstance(value, ASTNode):
                self.visit(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, ASTNode):
                        self.visit(item)
        return None
