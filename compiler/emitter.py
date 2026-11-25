"""
WetLang Compiler - Bytecode Binary Emitter & Disassembler
Hand-crafted from first principles. Complete WBC binary serialization and CRC32 checksum.
"""

import struct
import zlib
import math
import warnings
from typing import Dict, List, Tuple, Optional, Any, Set, Union
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
from compiler.isa import (
    HEADER_MAGIC,
    HEADER_SIZE,
    VERSION_MAJOR,
    VERSION_MINOR,
    HEADER_STRUCT_FORMAT,
    Capability,
    SectionType,
    SECTION_ENTRY_FORMAT,
    SECTION_ENTRY_SIZE,
    Opcode,
    OPCODE_OPERAND_FORMATS,
    OPCODE_NAMES,
)
from enum import Enum


class Target(str, Enum):
    """Compilation target architectures (Project Janus)."""
    SIM = "sim"
    FINALSPARK = "finalspark"
    SPINNAKER = "spinnaker"
    EMBEDDED = "embedded"
    LOIHI2 = "loihi2"


class SubstrateWarning(UserWarning):
    """Structured compiler warning for neuromorphic substrate lowering."""
    pass


class SubstrateUnsupportedOpWarning(SubstrateWarning):
    """Specific warning for wetware operations unsupported on silicon substrates."""
    code = "W_SUBSTRATE_UNSUPPORTED_OP"


class ConstantPool:
    """Manages deduplicated constants (integers, floats, strings)."""
    def __init__(self):
        self.entries: List[Tuple[int, Any]] = []  # (type_tag, value) 1=int, 2=float, 3=string
        self.lookup: Dict[Tuple[int, Any], int] = {}

    def add_int(self, val: int) -> int:
        key = (1, int(val))
        if key in self.lookup:
            return self.lookup[key]
        idx = len(self.entries)
        self.entries.append(key)
        self.lookup[key] = idx
        return idx

    def add_float(self, val: float) -> int:
        key = (2, float(val))
        if key in self.lookup:
            return self.lookup[key]
        idx = len(self.entries)
        self.entries.append(key)
        self.lookup[key] = idx
        return idx

    def add_string(self, val: str) -> int:
        key = (3, str(val))
        if key in self.lookup:
            return self.lookup[key]
        idx = len(self.entries)
        self.entries.append(key)
        self.lookup[key] = idx
        return idx

    def serialize(self) -> bytes:
        data = bytearray()
        data.extend(struct.pack("<I", len(self.entries)))
        for tag, val in self.entries:
            data.append(tag)
            if tag == 1:
                data.extend(struct.pack("<i", val))
            elif tag == 2:
                data.extend(struct.pack("<f", val))
            elif tag == 3:
                s_bytes = val.encode('utf-8')
                data.extend(struct.pack("<H", len(s_bytes)))
                data.extend(s_bytes)
        return bytes(data)


class BytecodeEmitter(ASTVisitor):
    """
    Traverses the AST and emits stack machine bytecode with jump backpatching.
    """
    def __init__(self):
        self.code: bytearray = bytearray()
        self.constant_pool: ConstantPool = ConstantPool()
        self.locals_map: Dict[str, int] = {}
        self.next_local_slot: int = 0
        self.channel_aliases: Dict[str, int] = {} # alias_name -> linear channel 0..63
        self.channel_modes: Dict[str, str] = {}
        self.capabilities: int = Capability.NONE
        self.grid_rows: int = 8
        self.grid_cols: int = 8
        self.channel_count: int = 64
        self.line_map: List[Tuple[int, int, int]] = [] # (bytecode_offset, line, col)
        self.max_voltage_seen: float = 0.0
        self.const_float_values: Dict[str, float] = {}
        self.const_int_values: Dict[str, int] = {}
        self.used_electrodes: Set[int] = set()
        self.local_types: Dict[str, str] = {}
        self.function_entry_points: Dict[str, int] = {}

    def _emit_duration_ms(self, node: ASTNode) -> None:
        """Emits a duration/window argument scaled to milliseconds for the VM internal clock."""
        if isinstance(node, PhysicalLiteralNode) and node.dimension == Dimension.TIME:
            # Convert SI seconds to milliseconds (* 1000.0)
            self.emit(Opcode.PUSH_FLOAT, float(node.si_value * 1000.0), node=node)
        else:
            self.visit(node)

    def _is_int_expr(self, node: ASTNode) -> bool:
        """Determines if an expression evaluates to an integer type."""
        if isinstance(node, LiteralNode) and node.type_name == "int":
            return True
        if isinstance(node, IdentifierNode):
            if node.name in self.const_int_values:
                return True
            if getattr(node, "inferred_type", None) == "int":
                return True
            if self.local_types.get(node.name) == "int":
                return True
        if isinstance(node, DomainCallNode) and node.func_name == "read_spikes":
            return True
        if isinstance(node, BinaryOpNode) and node.op in ("+", "-", "*", "/", "%"):
            return self._is_int_expr(node.left) and self._is_int_expr(node.right)
        if isinstance(node, UnaryOpNode) and node.op in ("-", "+"):
            return self._is_int_expr(node.operand)
        if isinstance(node, CallNode) and isinstance(node.callee, IdentifierNode) and node.callee.name == "int":
            return True
        return False

    def _is_const_channel(self, node: ASTNode) -> bool:
        """Determines if a channel reference is known at compile time."""
        if isinstance(node, IdentifierNode):
            if node.name in self.channel_aliases or node.name in self.const_int_values:
                return True
            return False
        if isinstance(node, LiteralNode) and node.type_name == "int":
            return True
        if isinstance(node, IndexNode):
            for idx in node.indices:
                if self._extract_int_constant(idx) is None:
                    return False
            return True
        return self._extract_int_constant(node) is not None

    def emit(self, opcode: Opcode, *operands: Any, node: Optional[ASTNode] = None) -> int:
        """Emits an instruction byte and packed operands. Returns instruction start offset."""
        offset = len(self.code)
        if node is not None:
            self.line_map.append((offset, node.line, node.column))

        self.code.append(opcode.value)
        fmt = OPCODE_OPERAND_FORMATS.get(opcode, "")
        if fmt:
            self.code.extend(struct.pack(fmt, *operands))
        return offset

    def emit_jump(self, opcode: Opcode, target_placeholder: int = 0) -> int:
        """Emits a jump with placeholder offset for backpatching. Returns offset of the int16 operand."""
        self.code.append(opcode.value)
        operand_offset = len(self.code)
        self.code.extend(struct.pack("<h", target_placeholder))
        return operand_offset

    def patch_jump(self, operand_offset: int, target_instruction_offset: int) -> None:
        """Backpatches relative jump offset."""
        # Relative jump offset = target_instruction_offset - instruction_start_offset
        instr_start = operand_offset - 1
        rel_offset = target_instruction_offset - instr_start
        struct.pack_into("<h", self.code, operand_offset, rel_offset)

    def current_offset(self) -> int:
        return len(self.code)

    def get_or_create_local(self, name: str) -> int:
        if name not in self.locals_map:
            slot = self.next_local_slot
            self.locals_map[name] = slot
            self.next_local_slot += 1
            return slot
        return self.locals_map[name]

    # =========================================================================
    # AST Traversal & Code Generation
    # =========================================================================

    def compile(self, program: ProgramNode, sequence_counter: int = 1) -> bytes:
        """Compiles the AST ProgramNode into a complete WBC binary."""
        self.visit(program)

        # Set CAP_MULTI_ELECTRODE if more than 16 unique electrodes were used
        if len(self.used_electrodes) > 16:
            self.capabilities |= Capability.CAP_MULTI_ELECTRODE

        # Append final HALT instruction
        self.emit(Opcode.HALT)

        # Serialize WBC Sections and Binary
        return self._build_wbc_binary(sequence_counter=sequence_counter)

    def visit_ProgramNode(self, node: ProgramNode) -> None:
        for decl in node.declarations:
            self.visit(decl)

    def visit_OrganoidDeclNode(self, node: OrganoidDeclNode) -> None:
        pass

    def visit_ConnectDeclNode(self, node: ConnectDeclNode) -> None:
        pass

    def visit_PortDeclNode(self, node: PortDeclNode) -> None:
        pass

    def visit_GridDeclNode(self, node: GridDeclNode) -> None:
        rows = 8
        cols = 8
        if isinstance(node.rows, LiteralNode) and node.rows.type_name == "int":
            rows = int(node.rows.value)
        if isinstance(node.cols, LiteralNode) and node.cols.type_name == "int":
            cols = int(node.cols.value)
        self.grid_rows = rows
        self.grid_cols = cols
        self.channel_count = rows * cols
        if rows <= 255 and cols <= 255:
            self.emit(Opcode.MEA_CONFIG, rows, cols, node=node)

    def visit_ChannelDeclNode(self, node: ChannelDeclNode) -> None:
        ch_idx = self._resolve_channel_index(node.target)
        self.channel_aliases[node.name] = ch_idx
        if node.mode:
            self.channel_modes[node.name] = node.mode

    def visit_FnDeclNode(self, node: FnDeclNode) -> None:
        if node.name == "main":
            # main is the program entry point: emit body inline without skip jump or ret
            for param in reversed(node.params):
                slot = self.get_or_create_local(param.name)
                self.emit(Opcode.STORE_LOCAL, slot, node=node)
                if getattr(param, "type_name", None) == "int":
                    self.local_types[param.name] = "int"

            self.visit(node.body)
            return

        skip_jump = self.emit_jump(Opcode.JMP)
        fn_entry_pc = self.current_offset()
        self.function_entry_points[node.name] = fn_entry_pc

        for param in reversed(node.params):
            slot = self.get_or_create_local(param.name)
            self.emit(Opcode.STORE_LOCAL, slot, node=node)
            if getattr(param, "type_name", None) == "int":
                self.local_types[param.name] = "int"

        self.visit(node.body)
        self.emit(Opcode.PUSH_INT, 0, node=node)
        self.emit(Opcode.RET, node=node)

        self.patch_jump(skip_jump, self.current_offset())

    def visit_StreamDeclNode(self, node: StreamDeclNode) -> None:
        self.capabilities |= Capability.CAP_CLOSED_LOOP
        for item in node.items:
            if item.kind == "cycle" and item.cycle_block is not None:
                loop_start = self.current_offset()
                self.visit(item.cycle_block)
                self.emit_jump(Opcode.JMP, loop_start - self.current_offset())

    def visit_BlockNode(self, node: BlockNode) -> None:
        for stmt in node.statements:
            self.visit(stmt)

    def visit_LetStmtNode(self, node: LetStmtNode) -> None:
        slot = self.get_or_create_local(node.name)
        if getattr(node, "type_name", None) == "int":
            self.local_types[node.name] = "int"
        elif getattr(node, "type_name", None) == "float":
            self.local_types[node.name] = "float"

        if node.initializer is not None:
            if self._is_int_expr(node.initializer):
                self.local_types[node.name] = "int"
            self.visit(node.initializer)
            self.emit(Opcode.STORE_LOCAL, slot, node=node)
            if not node.is_mut:
                f_val = self._extract_float_si_value(node.initializer)
                if f_val is not None:
                    self.const_float_values[node.name] = f_val
                i_val = self._extract_int_constant(node.initializer)
                if i_val is not None:
                    self.const_int_values[node.name] = i_val
        else:
            # Default zero initialization
            self.emit(Opcode.PUSH_INT, 0, node=node)
            self.emit(Opcode.STORE_LOCAL, slot, node=node)

    def visit_AssignStmtNode(self, node: AssignStmtNode) -> None:
        self.visit(node.value)
        if isinstance(node.target, IdentifierNode):
            slot = self.get_or_create_local(node.target.name)
            self.emit(Opcode.STORE_LOCAL, slot, node=node)
            if self._is_int_expr(node.value):
                self.local_types[node.target.name] = "int"
        else:
            # Target is index, evaluate value then store
            self.emit(Opcode.POP, node=node)

    def visit_StimStmtNode(self, node: StimStmtNode) -> None:
        self.capabilities |= Capability.CAP_STIMULATION

        # Check if stimulation amplitude is specified in Current (uA/mA/A) -> Opcode.STIM_CURRENT
        curr_node = node.voltage
        while isinstance(curr_node, UnaryOpNode) and curr_node.op in ("-", "+"):
            curr_node = curr_node.operand
        is_current_stim = (
            (isinstance(curr_node, PhysicalLiteralNode) and curr_node.dimension == Dimension.CURRENT)
            or getattr(node.voltage, "inferred_dimension", None) == Dimension.CURRENT
        )
        if is_current_stim:
            si_curr = self._extract_float_si_value(node.voltage)
            current_ua = float(si_curr * 1e6) if si_curr is not None else 0.0
            if not self._is_const_channel(node.channel):
                self.visit(node.channel)
                self._emit_duration_ms(node.phase1)
                self._emit_duration_ms(node.phase2)
                if node.interphase is not None:
                    self._emit_duration_ms(node.interphase)
                else:
                    self.emit(Opcode.PUSH_FLOAT, 0.0)
                self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                self.emit(Opcode.STIM_CURRENT, 0xFF, current_ua, node=node)
            else:
                ch_idx = self._resolve_channel_index(node.channel)
                if ch_idx == 0xFF:
                    self.emit(Opcode.PUSH_INT, 0xFF, node=node)
                    self._emit_duration_ms(node.phase1)
                    self._emit_duration_ms(node.phase2)
                    if node.interphase is not None:
                        self._emit_duration_ms(node.interphase)
                    else:
                        self.emit(Opcode.PUSH_FLOAT, 0.0)
                    self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                    self.emit(Opcode.STIM_CURRENT, 0xFF, current_ua, node=node)
                else:
                    self.used_electrodes.add(ch_idx)
                    if len(self.used_electrodes) > 16:
                        self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                    self._emit_duration_ms(node.phase1)
                    self._emit_duration_ms(node.phase2)
                    if node.interphase is not None:
                        self._emit_duration_ms(node.interphase)
                    else:
                        self.emit(Opcode.PUSH_FLOAT, 0.0)
                    self.emit(Opcode.STIM_CURRENT, ch_idx, current_ua, node=node)
            return

        # Evaluate arguments onto stack: voltage, phase1, phase2, interphase
        self.visit(node.voltage)
        self._emit_duration_ms(node.phase1)
        self._emit_duration_ms(node.phase2)
        if node.interphase is not None:
            self._emit_duration_ms(node.interphase)
        else:
            self.emit(Opcode.PUSH_FLOAT, 0.0)

        # Check voltage capability and track max voltage seen
        v_val = self._extract_float_si_value(node.voltage)
        if v_val is not None:
            v_mag = abs(v_val)
            if v_mag > self.max_voltage_seen:
                self.max_voltage_seen = v_mag
            if v_mag >= 0.8 - 1e-9:
                self.capabilities |= Capability.CAP_HIGH_VOLTAGE
        else:
            # Fallback unwrap UnaryOpNode / Literals
            curr = node.voltage
            while isinstance(curr, UnaryOpNode) and curr.op in ("-", "+"):
                curr = curr.operand
            if isinstance(curr, PhysicalLiteralNode):
                v_mag = abs(curr.si_value)
                if v_mag > self.max_voltage_seen:
                    self.max_voltage_seen = v_mag
                if v_mag >= 0.8 - 1e-9:
                    self.capabilities |= Capability.CAP_HIGH_VOLTAGE
            elif isinstance(curr, LiteralNode) and curr.type_name in ("int", "float"):
                v_mag = abs(float(curr.value))
                if v_mag > self.max_voltage_seen:
                    self.max_voltage_seen = v_mag
                if v_mag >= 0.8 - 1e-9:
                    self.capabilities |= Capability.CAP_HIGH_VOLTAGE

        if not self._is_const_channel(node.channel):
            self.visit(node.channel)
            self.capabilities |= Capability.CAP_MULTI_ELECTRODE
            self.emit(Opcode.STIM_BIPHASIC, 0xFF, node=node)
        else:
            ch_idx = self._resolve_channel_index(node.channel)
            if ch_idx == 0xFF:
                # 0xFF is the dynamic channel sentinel in the VM; push explicitly
                self.emit(Opcode.PUSH_INT, 0xFF, node=node)
                self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                self.emit(Opcode.STIM_BIPHASIC, 0xFF, node=node)
            else:
                self.used_electrodes.add(ch_idx)
                if len(self.used_electrodes) > 16:
                    self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                self.emit(Opcode.STIM_BIPHASIC, ch_idx, node=node)

    def visit_ModulateStmtNode(self, node: ModulateStmtNode) -> None:
        self.capabilities |= Capability.CAP_PLASTICITY
        if len(node.args) == 3:
            if not self._is_const_channel(node.args[0]) or not self._is_const_channel(node.args[1]):
                self.visit(node.args[0])  # dynamic pre
                self.visit(node.args[1])  # dynamic post
                self.visit(node.args[2])  # weight delta
                self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                self.emit(Opcode.MODULATE_STDP, 0xFF, 0xFF, node=node)
            else:
                pre_ch = self._resolve_channel_index(node.args[0])
                post_ch = self._resolve_channel_index(node.args[1])
                self.used_electrodes.add(pre_ch)
                self.used_electrodes.add(post_ch)
                if len(self.used_electrodes) > 16:
                    self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                self.visit(node.args[2])  # weight delta
                self.emit(Opcode.MODULATE_STDP, pre_ch, post_ch, node=node)
        elif len(node.args) == 1:
            self.visit(node.args[0])  # weight delta / rate
            self.emit(Opcode.MODULATE_STDP, 0, 0, node=node)
        else:
            for arg in node.args:
                self.visit(arg)
            self.emit(Opcode.MODULATE_STDP, 0, 0, node=node)

    def visit_SyncTickStmtNode(self, node: SyncTickStmtNode) -> None:
        if node.count is not None:
            if isinstance(node.count, LiteralNode) and node.count.type_name == "int":
                cnt = int(node.count.value)
                if cnt > 1:
                    self.emit(Opcode.SLEEP_TICKS, cnt, node=node)
                    return
            elif isinstance(node.count, PhysicalLiteralNode) and node.count.dimension == Dimension.TIME:
                # e.g. sync_tick(2.0 ms) -> 20 ticks
                ticks = int(round(node.count.si_value / 1e-4))
                if ticks > 1:
                    self.emit(Opcode.SLEEP_TICKS, ticks, node=node)
                    return

        self.emit(Opcode.SYNC_TICK, node=node)

    def visit_IfStmtNode(self, node: IfStmtNode) -> None:
        self.visit(node.condition)
        false_jump = self.emit_jump(Opcode.JMP_IF_FALSE)
        self.visit(node.then_block)

        if node.else_block is not None:
            end_jump = self.emit_jump(Opcode.JMP)
            else_start = self.current_offset()
            self.patch_jump(false_jump, else_start)
            self.visit(node.else_block)
            end_offset = self.current_offset()
            self.patch_jump(end_jump, end_offset)
        else:
            then_end = self.current_offset()
            self.patch_jump(false_jump, then_end)

    def visit_WhileStmtNode(self, node: WhileStmtNode) -> None:
        loop_start = self.current_offset()
        self.visit(node.condition)
        exit_jump = self.emit_jump(Opcode.JMP_IF_FALSE)
        self.visit(node.body)
        self.emit_jump(Opcode.JMP, loop_start - (self.current_offset()))
        loop_end = self.current_offset()
        self.patch_jump(exit_jump, loop_end)

    def visit_ForStmtNode(self, node: ForStmtNode) -> None:
        slot = self.get_or_create_local(node.var_name)
        # Initialize var to range_start
        self.visit(node.range_start)
        self.emit(Opcode.STORE_LOCAL, slot, node=node)

        loop_start = self.current_offset()
        self.emit(Opcode.LOAD_LOCAL, slot)
        self.visit(node.range_end)
        self.emit(Opcode.CMP_LT)
        exit_jump = self.emit_jump(Opcode.JMP_IF_FALSE)

        self.visit(node.body)

        # Step: slot = slot + 1
        self.emit(Opcode.LOAD_LOCAL, slot)
        self.emit(Opcode.PUSH_INT, 1)
        self.emit(Opcode.ADD_I)
        self.emit(Opcode.STORE_LOCAL, slot)

        self.emit_jump(Opcode.JMP, loop_start - (self.current_offset()))
        loop_end = self.current_offset()
        self.patch_jump(exit_jump, loop_end)

    def visit_ReturnStmtNode(self, node: ReturnStmtNode) -> None:
        if node.value is not None:
            self.visit(node.value)
        else:
            self.emit(Opcode.PUSH_INT, 0)
        self.emit(Opcode.RET, node=node)

    def visit_ExprStmtNode(self, node: ExprStmtNode) -> None:
        self.visit(node.expr)
        # Void domain calls do not push a return value to the stack; do not emit POP
        if isinstance(node.expr, DomainCallNode) and node.expr.func_name in (
            "pump_set_rate", "pump_dispense", "valve_set", "valve_open", "valve_close", "motor_step"
        ):
            return
        self.emit(Opcode.POP, node=node)

    def visit_BinaryOpNode(self, node: BinaryOpNode) -> None:
        is_int = self._is_int_expr(node.left) and self._is_int_expr(node.right)
        self.visit(node.left)
        self.visit(node.right)

        if node.op == "+":
            self.emit(Opcode.ADD_I if is_int else Opcode.ADD_F, node=node)
        elif node.op == "-":
            self.emit(Opcode.SUB_I if is_int else Opcode.SUB_F, node=node)
        elif node.op == "*":
            self.emit(Opcode.MUL_I if is_int else Opcode.MUL_F, node=node)
        elif node.op == "/":
            self.emit(Opcode.DIV_I if is_int else Opcode.DIV_F, node=node)
        elif node.op == "%":
            self.emit(Opcode.MOD_I, node=node)
        elif node.op == "==":
            self.emit(Opcode.CMP_EQ, node=node)
        elif node.op == "!=":
            self.emit(Opcode.CMP_NE, node=node)
        elif node.op == "<":
            self.emit(Opcode.CMP_LT, node=node)
        elif node.op == "<=":
            self.emit(Opcode.CMP_LE, node=node)
        elif node.op == ">":
            self.emit(Opcode.CMP_GT, node=node)
        elif node.op == ">=":
            self.emit(Opcode.CMP_GE, node=node)
        elif node.op == "&&":
            self.emit(Opcode.MUL_I, node=node)
            self.emit(Opcode.PUSH_INT, 0)
            self.emit(Opcode.CMP_NE, node=node)
        elif node.op == "||":
            # Boolean normalization: (left != 0) + (right != 0) > 0
            self.emit(Opcode.ADD_I, node=node)
            self.emit(Opcode.PUSH_INT, 0)
            self.emit(Opcode.CMP_NE, node=node)

    def visit_UnaryOpNode(self, node: UnaryOpNode) -> None:
        self.visit(node.operand)
        if node.op == "-":
            self.emit(Opcode.NEG, node=node)
        elif node.op == "!":
            self.emit(Opcode.PUSH_INT, 0, node=node)
            self.emit(Opcode.CMP_EQ, node=node)

    def visit_LiteralNode(self, node: LiteralNode) -> None:
        if node.type_name == "int":
            self.emit(Opcode.PUSH_INT, int(node.value), node=node)
        elif node.type_name == "float":
            self.emit(Opcode.PUSH_FLOAT, float(node.value), node=node)
        elif node.type_name == "bool":
            self.emit(Opcode.PUSH_INT, 1 if node.value else 0, node=node)
        elif node.type_name == "string":
            idx = self.constant_pool.add_string(str(node.value))
            self.emit(Opcode.PUSH_CONST, idx, node=node)

    def visit_PhysicalLiteralNode(self, node: PhysicalLiteralNode) -> None:
        # All physical literals are loaded in SI base units on stack
        self.emit(Opcode.PUSH_FLOAT, float(node.si_value), node=node)

    def visit_IdentifierNode(self, node: IdentifierNode) -> None:
        if node.name in self.locals_map:
            slot = self.locals_map[node.name]
            self.emit(Opcode.LOAD_LOCAL, slot, node=node)
        elif node.name in self.channel_aliases:
            ch_idx = self.channel_aliases[node.name]
            self.emit(Opcode.PUSH_INT, ch_idx, node=node)
        else:
            slot = self.get_or_create_local(node.name)
            self.emit(Opcode.LOAD_LOCAL, slot, node=node)

    def visit_CallNode(self, node: CallNode) -> None:
        # Handle cast/math builtins
        if isinstance(node.callee, IdentifierNode):
            cname = node.callee.name
            if cname in ("int", "float") and len(node.args) == 1:
                self.visit(node.args[0])
                return
            if cname == "abs" and len(node.args) == 1:
                self.visit(node.args[0])
                self.emit(Opcode.DUP)
                self.emit(Opcode.PUSH_INT, 0)
                self.emit(Opcode.CMP_LT)
                skip = self.emit_jump(Opcode.JMP_IF_FALSE)
                self.emit(Opcode.NEG)
                self.patch_jump(skip, self.current_offset())
                return
            if cname in self.function_entry_points:
                for arg in node.args:
                    self.visit(arg)
                fn_pc = self.function_entry_points[cname]
                self.emit(Opcode.CALL, fn_pc, len(node.args), node=node)
                return

        for arg in node.args:
            self.visit(arg)
        fn_idx = self.constant_pool.add_string(getattr(node.callee, "name", "fn"))
        self.emit(Opcode.CALL, fn_idx, len(node.args), node=node)

    def visit_IndexNode(self, node: IndexNode) -> None:
        if self._is_const_channel(node):
            ch_idx = self._resolve_channel_index(node)
            self.emit(Opcode.PUSH_INT, ch_idx, node=node)
        else:
            # Dynamic grid/channel indexing
            if len(node.indices) == 2:
                self.visit(node.indices[0])
                self.emit(Opcode.PUSH_INT, 8)
                self.emit(Opcode.MUL_I)
                self.visit(node.indices[1])
                self.emit(Opcode.ADD_I)
            elif len(node.indices) == 1:
                self.visit(node.indices[0])

    def visit_DomainCallNode(self, node: DomainCallNode) -> None:
        if node.func_name == "read_spikes":
            if not self._is_const_channel(node.args[0]):
                self.visit(node.args[0])  # dynamic channel
                self._emit_duration_ms(node.args[1])  # window_ms
                self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                self.emit(Opcode.READ_SPIKES, 0xFF, node=node)
            else:
                ch_idx = self._resolve_channel_index(node.args[0])
                if ch_idx == 0xFF:
                    self.emit(Opcode.PUSH_INT, 0xFF, node=node)
                    self._emit_duration_ms(node.args[1])
                    self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                    self.emit(Opcode.READ_SPIKES, 0xFF, node=node)
                else:
                    self.used_electrodes.add(ch_idx)
                    if len(self.used_electrodes) > 16:
                        self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                    self._emit_duration_ms(node.args[1])  # window_ms
                    self.emit(Opcode.READ_SPIKES, ch_idx, node=node)
        elif node.func_name == "read_voltage":
            if not self._is_const_channel(node.args[0]):
                self.visit(node.args[0])  # dynamic channel
                self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                self.emit(Opcode.READ_VOLTAGE, 0xFF, node=node)
            else:
                ch_idx = self._resolve_channel_index(node.args[0])
                if ch_idx == 0xFF:
                    self.emit(Opcode.PUSH_INT, 0xFF, node=node)
                    self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                    self.emit(Opcode.READ_VOLTAGE, 0xFF, node=node)
                else:
                    self.used_electrodes.add(ch_idx)
                    if len(self.used_electrodes) > 16:
                        self.capabilities |= Capability.CAP_MULTI_ELECTRODE
                    self.emit(Opcode.READ_VOLTAGE, ch_idx, node=node)
        elif node.func_name in ("pop_firing_rate", "read_population_rate"):
            self._emit_duration_ms(node.args[0])  # window_ms
            self.emit(Opcode.GET_POP_RATE, node=node)
        elif node.func_name == "pump_set_rate":
            pump_id = self._eval_const_int(node.args[0])
            rate_val = 0.0
            if isinstance(node.args[1], PhysicalLiteralNode):
                rate_val = float(node.args[1].magnitude)
                if node.args[1].unit_suffix == "mL/min":
                    rate_val *= 1000.0
            elif isinstance(node.args[1], LiteralNode):
                rate_val = float(node.args[1].value)
            self.capabilities |= Capability.CAP_MICROFLUIDICS
            self.emit(Opcode.PUMP_SET_RATE, pump_id, rate_val, node=node)
        elif node.func_name == "pump_dispense":
            pump_id = self._eval_const_int(node.args[0])
            vol_val = 0.0
            if isinstance(node.args[1], PhysicalLiteralNode):
                vol_val = float(node.args[1].magnitude)
                if node.args[1].unit_suffix == "mL":
                    vol_val *= 1000.0
            elif isinstance(node.args[1], LiteralNode):
                vol_val = float(node.args[1].value)
            self.capabilities |= Capability.CAP_MICROFLUIDICS
            self.emit(Opcode.PUMP_DISPENSE, pump_id, vol_val, node=node)
        elif node.func_name in ("valve_set", "valve_open", "valve_close"):
            valve_id = self._eval_const_int(node.args[0])
            if node.func_name == "valve_open":
                state = 1
            elif node.func_name == "valve_close":
                state = 0
            else:
                state = 1 if self._eval_const_int(node.args[1]) else 0
            self.capabilities |= Capability.CAP_MICROFLUIDICS
            self.emit(Opcode.VALVE_SET, valve_id, state, node=node)
        elif node.func_name == "motor_step":
            motor_id = self._eval_const_int(node.args[0])
            steps = self._eval_const_int(node.args[1])
            speed = 60.0
            if len(node.args) > 2:
                if isinstance(node.args[2], PhysicalLiteralNode):
                    speed = float(node.args[2].magnitude)
                elif isinstance(node.args[2], LiteralNode):
                    speed = float(node.args[2].value)
            self.capabilities |= Capability.CAP_MOTOR_ACTUATION
            self.emit(Opcode.MOTOR_STEP, motor_id, steps, speed, node=node)
        elif node.func_name == "read_pressure":
            port_id = self._eval_const_int(node.args[0]) if node.args else 0
            self.emit(Opcode.READ_PRESSURE, port_id, node=node)
        elif node.func_name == "read_temperature":
            self.emit(Opcode.READ_TEMPERATURE, node=node)

    def _resolve_channel_index(self, node: ASTNode) -> int:
        """Resolves channel expression to linear channel index 0..63."""
        if isinstance(node, IdentifierNode):
            if node.name in self.channel_aliases:
                return self.channel_aliases[node.name]
            if node.name in self.const_int_values:
                return self.const_int_values[node.name]
            return 0
        if isinstance(node, LiteralNode) and node.type_name == "int":
            return int(node.value)
        if isinstance(node, IndexNode):
            if len(node.indices) == 2:
                r = self._eval_const_int(node.indices[0])
                c = self._eval_const_int(node.indices[1])
                return r * 8 + c
            elif len(node.indices) == 1:
                return self._eval_const_int(node.indices[0])
        const_int = self._extract_int_constant(node)
        if const_int is not None:
            return const_int
        return 0

    def _eval_const_int(self, node: ASTNode) -> int:
        val = self._extract_int_constant(node)
        return val if val is not None else 0

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
            if hasattr(self, "const_float_values") and node.name in self.const_float_values:
                return self.const_float_values[node.name]
        return None

    # =========================================================================
    # Section Packaging & WBC Serialization
    # =========================================================================

    def _build_wbc_binary(self, sequence_counter: int = 1) -> bytes:
        # 1. Section 1: CONSTANT_POOL
        sec1_data = self.constant_pool.serialize()

        # 2. Section 2: TOPOLOGY_CONFIG
        sec2_data = self._serialize_topology()

        # 3. Section 3: BYTECODE_STREAM
        sec3_data = bytes(self.code)

        # 4. Section 4: SAFETY_MANIFEST
        sec4_data = self._serialize_manifest()

        # 5. Section 5: DEBUG_LINE_MAP
        sec5_data = self._serialize_line_map()

        sections = [
            (SectionType.CONSTANT_POOL, sec1_data),
            (SectionType.TOPOLOGY_CONFIG, sec2_data),
            (SectionType.BYTECODE_STREAM, sec3_data),
            (SectionType.SAFETY_MANIFEST, sec4_data),
            (SectionType.DEBUG_LINE_MAP, sec5_data),
        ]

        num_sections = len(sections)
        section_table_size = num_sections * SECTION_ENTRY_SIZE
        payload_offset = HEADER_SIZE + section_table_size

        section_table_bytes = bytearray()
        payload_bytes = bytearray()

        curr_offset = payload_offset
        for sec_type, sec_data in sections:
            sec_len = len(sec_data)
            entry = struct.pack(SECTION_ENTRY_FORMAT, sec_type.value, 0, curr_offset, sec_len)
            section_table_bytes.extend(entry)
            payload_bytes.extend(sec_data)
            curr_offset += sec_len

        total_file_size = HEADER_SIZE + len(section_table_bytes) + len(payload_bytes)

        # Build Header with CRC32 = 0 placeholder
        header_placeholder = struct.pack(
            HEADER_STRUCT_FORMAT,
            HEADER_MAGIC,
            VERSION_MAJOR,
            VERSION_MINOR,
            int(self.capabilities),
            total_file_size,
            0, # CRC32 placeholder
            num_sections,
            self.channel_count, # dynamic channel count from grid declaration (e.g. rows * cols)
            0.5, # max charge limit 0.5 nC
            sequence_counter # Monotonic anti-rollback security sequence counter
        )

        full_binary = bytearray(header_placeholder)
        full_binary.extend(section_table_bytes)
        full_binary.extend(payload_bytes)

        # Calculate CRC32 over the entire file
        crc = zlib.crc32(bytes(full_binary)) & 0xFFFFFFFF
        # Backpatch CRC32 at offset 0x0C (12)
        struct.pack_into("<I", full_binary, 12, crc)

        return bytes(full_binary)

    def _serialize_topology(self) -> bytes:
        data = bytearray()
        data.extend(struct.pack("<IHHfI", self.channel_count, min(self.grid_rows, 65535), min(self.grid_cols, 65535), 200.0, len(self.channel_aliases)))
        for name, ch_id in self.channel_aliases.items():
            name_bytes = name.encode('utf-8')
            mode_str = self.channel_modes.get(name, "Bidirectional")
            mode_byte = 0
            if mode_str == "BiphasicStim":
                mode_byte = 1
            elif mode_str == "SpikeReadout":
                mode_byte = 2
            elif mode_str == "VoltageSense":
                mode_byte = 3
            data.extend(struct.pack("<H", len(name_bytes)))
            data.extend(name_bytes)
            data.extend(struct.pack("<BB", ch_id, mode_byte))
        return bytes(data)

    def _serialize_manifest(self) -> bytes:
        # Manifest format: capabilities (I), verified_loop_yield (B), max_voltage_seen (f), max_charge (f)
        return struct.pack("<IBff", int(self.capabilities), 1, self.max_voltage_seen, 0.5)

    def _serialize_line_map(self) -> bytes:
        data = bytearray()
        data.extend(struct.pack("<I", len(self.line_map)))
        for off, line, col in self.line_map:
            data.extend(struct.pack("<III", off, line, col))
        return bytes(data)


# =========================================================================
# High-Level Compiler Pipeline Helper
# =========================================================================

def compile_source(source_text: str, filename: str = "<stdin>", target: str = "sim") -> Union[bytes, str]:
    """
    Executes the complete 4-stage compiler pipeline:
    Lexer -> Pratt Parser -> Semantic/Safety Analyzer -> Target Emitter.
    Supports target-specific lowering (WBC bytecode for sim/finalspark/embedded,
    Intel Lava Python for loihi2, PyNN Python for spinnaker).
    """
    from compiler.lexer import Lexer
    from compiler.parser import Parser
    from compiler.semantic import SemanticAnalyzer

    lexer = Lexer(source_text)
    tokens = lexer.tokenize()
    parser = Parser(tokens, source_text=source_text)
    ast = parser.parse()
    analyzer = SemanticAnalyzer(ast)
    analyzer.analyze()

    target_norm = target.value if isinstance(target, Target) else str(target).lower()
    if target_norm == Target.LOIHI2.value:
        return emit_loihi2(ast)
    if target_norm == Target.SPINNAKER.value:
        return emit_spinnaker(ast)
    if target_norm in (Target.SIM.value, Target.FINALSPARK.value, Target.EMBEDDED.value):
        emitter = BytecodeEmitter()
        return emitter.compile(ast)
    raise ValueError(f"Unsupported compilation target: {target!r}")


def disassemble(bytecode_bytes: bytes) -> str:
    """Disassembles a raw WBC binary into human-readable assembly listing."""
    if len(bytecode_bytes) < HEADER_SIZE:
        raise ValueError(f"Binary too small ({len(bytecode_bytes)} bytes), expected at least {HEADER_SIZE}")

    magic, v_maj, v_min, caps, fsize, crc, n_secs, ch_cnt, max_q, seq_counter = struct.unpack_from(HEADER_STRUCT_FORMAT, bytecode_bytes, 0)
    if magic != HEADER_MAGIC:
        raise ValueError(f"Invalid WBC magic: {magic!r}, expected {HEADER_MAGIC!r}")

    lines: List[str] = []
    lines.append("=" * 70)
    lines.append(f"WBC Binary Disassembly (v{v_maj}.{v_min})")
    lines.append(f"File Size: {fsize} bytes | CRC32: 0x{crc:08X} | Capabilities: 0x{caps:04X} | Seq: {seq_counter}")
    lines.append(f"Sections: {n_secs} | Channels: {ch_cnt} | Max Charge Bound: {max_q:.2f} nC")
    lines.append("=" * 70)

    # Read Section Table
    sections_info: Dict[int, Tuple[int, int]] = {}
    sec_table_off = HEADER_SIZE
    for i in range(n_secs):
        stype, _, off, size = struct.unpack_from(SECTION_ENTRY_FORMAT, bytecode_bytes, sec_table_off + i * SECTION_ENTRY_SIZE)
        sections_info[stype] = (off, size)

    # Disassemble Bytecode Stream (Section 3)
    if SectionType.BYTECODE_STREAM.value in sections_info:
        code_off, code_size = sections_info[SectionType.BYTECODE_STREAM.value]
        code_bytes = bytecode_bytes[code_off:code_off + code_size]

        lines.append("\n[Section 3: BYTECODE_STREAM]")
        pc = 0
        while pc < len(code_bytes):
            op_byte = code_bytes[pc]
            op_name = OPCODE_NAMES.get(op_byte, f"UNKNOWN_0x{op_byte:02X}")
            op = Opcode(op_byte) if op_byte in OPCODE_NAMES else None

            fmt = OPCODE_OPERAND_FORMATS.get(op, "") if op else ""
            fmt_size = struct.calcsize(fmt) if fmt else 0

            raw_hex = [f"{op_byte:02X}"]
            for b in code_bytes[pc + 1:pc + 1 + fmt_size]:
                raw_hex.append(f"{b:02X}")
            raw_str = " ".join(raw_hex).ljust(16)

            operands_str = ""
            if fmt_size > 0 and pc + 1 + fmt_size <= len(code_bytes):
                operands = struct.unpack_from(fmt, code_bytes, pc + 1)
                operands_str = ", ".join(str(o) for o in operands)

            lines.append(f"{pc:04X}:  {raw_str} {op_name:<16} {operands_str}")
            pc += 1 + fmt_size

    lines.append("=" * 70)
    return "\n".join(lines)


# =========================================================================
# Project Janus: Neuromorphic Silicon Backend Emitter (Sprint Task 2)
# =========================================================================

def emit_c_embedded_header(bytecode_bytes: bytes, model_name: str = "wet_model", target: str = "embedded") -> str:
    """
    Generates a standalone, self-contained C header (model_compiled.h) for embedded systems
    (ARM Cortex-M4/M7, ESP32, STM32, and SpiNNaker ARM968 cores).
    Includes:
      - Bytecode binary array (const uint8_t wet_bytecode[])
      - Zero-malloc static arena memory allocation
      - Deterministic embedded lifecycle functions (init, step, get_bytecode)
    """
    clean_name = "".join(c if c.isalnum() else "_" for c in model_name)
    n_bytes = len(bytecode_bytes)

    # Format bytes in rows of 12
    byte_rows = []
    for i in range(0, n_bytes, 12):
        chunk = bytecode_bytes[i:i + 12]
        row_str = "    " + ", ".join(f"0x{b:02X}" for b in chunk)
        byte_rows.append(row_str)
    formatted_bytes = ",\n".join(byte_rows)

    is_spinnaker = (target.lower() == "spinnaker")
    spinnaker_headers = """#ifdef __SPINNAKER__
#include <sark.h>
#include <spin1_api.h>
#endif
""" if is_spinnaker else ""

    target_comment = "SpiNNaker Neuromorphic Core (ARM968)" if is_spinnaker else "Embedded Microcontroller (ARM Cortex-M / ESP32)"

    header_code = f"""/*
 * Auto-generated by WetLang Compiler (Project Janus - Silicon Target)
 * Model Name: {clean_name}
 * Target Architecture: {target_comment}
 * Bytecode Size: {n_bytes} bytes
 * Memory Model: MISRA-C:2012 Static Arena (Zero Dynamic Malloc)
 */

#ifndef WET_MODEL_{clean_name.upper()}_H
#define WET_MODEL_{clean_name.upper()}_H

#include <stdint.h>
#include <stddef.h>
#include <string.h>

{spinnaker_headers}
#ifdef __cplusplus
extern "C" {{
#endif

#define WET_BYTECODE_SIZE_{clean_name.upper()} {n_bytes}
#define WET_STATIC_ARENA_SIZE 65536

/* Compiled WetLang WBC Binary Array */
static const uint8_t wet_bytecode_{clean_name}[{n_bytes}] = {{
{formatted_bytes}
}};

/* Static Zero-Malloc Execution Arena */
static uint8_t g_wet_static_arena_{clean_name}[WET_STATIC_ARENA_SIZE];

/* Static Embedded VM State Scaffolding */
typedef struct {{
    uint8_t  initialized;
    uint8_t  target_id; /* 0=Sim, 1=FinalSpark, 2=SpiNNaker, 3=Embedded */
    uint64_t current_tick;
    float    last_voltages[64];
    uint8_t  last_spikes[64];
}} wet_embedded_state_{clean_name}_t;

static wet_embedded_state_{clean_name}_t g_wet_state_{clean_name};

/**
 * Initializes the embedded WetLang model.
 * Zero dynamic allocations.
 */
static inline int wet_embedded_init_{clean_name}(void) {{
    memset(&g_wet_state_{clean_name}, 0, sizeof(g_wet_state_{clean_name}));
    g_wet_state_{clean_name}.initialized = 1;
    g_wet_state_{clean_name}.target_id = {2 if is_spinnaker else 3};
    return 0; /* WET_OK */
}}

/**
 * Steps execution by 1 biological tick (0.1 ms).
 */
static inline int wet_embedded_step_{clean_name}(void) {{
    if (!g_wet_state_{clean_name}.initialized) {{
        wet_embedded_init_{clean_name}();
    }}
    g_wet_state_{clean_name}.current_tick++;
    return 0; /* WET_OK */
}}

/**
 * Returns a pointer to the compiled bytecode binary and its size.
 */
static inline const uint8_t* wet_get_compiled_bytecode_{clean_name}(size_t* out_size) {{
    if (out_size) {{
        *out_size = sizeof(wet_bytecode_{clean_name});
    }}
    return wet_bytecode_{clean_name};
}}

#ifdef __cplusplus
}}
#endif

#endif /* WET_MODEL_{clean_name.upper()}_H */
"""
    return header_code


def compile_to_embedded_header(source_text: str, target: str = "embedded", model_name: str = "wet_model") -> str:
    """Compiles .wet source directly to a standalone C header file (Project Janus - Sprint Task 2)."""
    bytecode = compile_source(source_text, target="sim")
    return emit_c_embedded_header(bytecode, model_name=model_name, target=target)


# =========================================================================
# Neuromorphic Silicon Backend Emitters (Intel Loihi-2 & SpiNNaker PyNN)
# =========================================================================

class NeuromorphicEmitterBase:
    """Base class for neuromorphic silicon code emitters."""
    def __init__(self, target_name: str):
        self.target_name = target_name
        self.warnings_list: List[str] = []
        self.organoids: Dict[str, OrganoidDeclNode] = {}
        self.connections: List[ConnectDeclNode] = []
        self.channels: Dict[str, ChannelDeclNode] = {}
        self.channel_indices: Dict[str, int] = {}
        self.grids: List[GridDeclNode] = []
        self.functions: Dict[str, FnDeclNode] = {}
        self.top_statements: List[ASTNode] = []

    def _warn_unsupported(self, op_name: str, detail: str = "") -> None:
        msg = f"W_SUBSTRATE_UNSUPPORTED_OP: Wetware primitive '{op_name}' is unsupported on neuromorphic target '{self.target_name}'."
        if detail:
            msg += f" {detail}"
        warnings.warn(msg, category=SubstrateUnsupportedOpWarning, stacklevel=3)
        self.warnings_list.append(msg)

    def _extract_voltage_val(self, node: Optional[ASTNode]) -> Optional[float]:
        if node is None:
            return None
        if isinstance(node, UnaryOpNode) and node.op in ("-", "+"):
            sub = self._extract_voltage_val(node.operand)
            if sub is None:
                return None
            return -sub if node.op == "-" else sub
        if isinstance(node, PhysicalLiteralNode):
            return float(node.si_value)
        if isinstance(node, LiteralNode) and node.type_name in ("int", "float"):
            return float(node.value)
        return None

    def _extract_time_ms(self, node: Optional[ASTNode], default: float = 0.2) -> float:
        if node is None:
            return default
        if isinstance(node, PhysicalLiteralNode):
            if node.dimension == Dimension.TIME:
                return max(0.0, float(node.si_value) * 1000.0)
            return max(0.0, float(node.magnitude))
        if isinstance(node, LiteralNode) and node.type_name in ("int", "float"):
            return max(0.0, float(node.value))
        return default

    def _extract_int_val(self, node: Optional[ASTNode], default: int = 1) -> int:
        if node is None:
            return default
        if isinstance(node, LiteralNode) and node.type_name == "int":
            return int(node.value)
        if isinstance(node, PhysicalLiteralNode):
            return int(node.magnitude)
        return default

    def _resolve_target_name(self, node: ASTNode) -> str:
        if isinstance(node, IdentifierNode):
            return node.name
        if isinstance(node, IndexNode):
            return self._resolve_target_name(node.target)
        return "defaultorganoid"

    def _resolve_target_index(self, node: ASTNode) -> Optional[int]:
        if isinstance(node, IndexNode):
            if len(node.indices) == 2:
                r = self._extract_int_val(node.indices[0], default=0)
                c = self._extract_int_val(node.indices[1], default=0)
                return r * 8 + c
            if len(node.indices) == 1:
                return self._extract_int_val(node.indices[0], default=0)
        return None

    def _extract_weight_val(self, node: Optional[ASTNode], default: float = 0.5) -> float:
        if node is None:
            return default
        if isinstance(node, LiteralNode) and node.type_name in ("int", "float"):
            return float(node.value)
        if isinstance(node, PhysicalLiteralNode):
            return float(node.magnitude)
        return default

    def _resolve_channel_index_static(self, node: Optional[ASTNode]) -> Optional[int]:
        if node is None:
            return None
        if isinstance(node, LiteralNode) and node.type_name == "int":
            return int(node.value)
        if isinstance(node, IdentifierNode) and node.name in self.channel_indices:
            return self.channel_indices[node.name]
        if isinstance(node, IndexNode):
            if len(node.indices) == 2:
                r = self._resolve_channel_index_static(node.indices[0])
                c = self._resolve_channel_index_static(node.indices[1])
                if r is not None and c is not None:
                    return r * 8 + c
            elif len(node.indices) == 1:
                return self._resolve_channel_index_static(node.indices[0])
        return None

    def _is_wetware_call(self, name: str) -> bool:
        return name in (
            "pump_set_rate", "pump_dispense",
            "valve_set", "valve_open", "valve_close",
            "motor_step", "read_pressure", "read_temperature", "read_voltage"
        )

    def _collect_declarations(self, ast_root: ProgramNode) -> None:
        for decl in ast_root.declarations:
            if isinstance(decl, OrganoidDeclNode):
                self.organoids[decl.name] = decl
                if decl.perfusion is not None:
                    perf_str = f"{decl.perfusion.magnitude} {decl.perfusion.unit_suffix}" if isinstance(decl.perfusion, PhysicalLiteralNode) else str(decl.perfusion)
                    self._warn_unsupported("perfusion", f"Perfusion flow rate '{perf_str}' lowered to safe no-op.")
            elif isinstance(decl, ConnectDeclNode):
                self.connections.append(decl)
            elif isinstance(decl, ChannelDeclNode):
                self.channels[decl.name] = decl
                idx = self._resolve_channel_index_static(decl.target)
                if idx is not None:
                    self.channel_indices[decl.name] = idx
            elif isinstance(decl, GridDeclNode):
                self.grids.append(decl)
            elif isinstance(decl, FnDeclNode):
                self.functions[decl.name] = decl
            elif isinstance(decl, PortDeclNode):
                if decl.mode and decl.mode.lower() in ("pump", "valve", "motor", "sensor", "actuator"):
                    self._warn_unsupported(f"port_{decl.mode}", "Fluidic/mechanical port lowered to safe no-op.")
            else:
                self.top_statements.append(decl)


class Loihi2Emitter(NeuromorphicEmitterBase):
    """
    Emits Intel Lava Python source code for execution on Intel Loihi-2 neuromorphic hardware
    or the in-repo deterministic reference simulator.
    """
    def __init__(self):
        super().__init__(target_name="loihi2")

    def emit(self, ast_root: ProgramNode) -> str:
        self._collect_declarations(ast_root)
        lines: List[str] = []

        lines.append('"""')
        lines.append("Auto-generated by WetLang Compiler (Target: Intel Loihi-2 Lava)")
        lines.append("Architecture: Intel Loihi-2 Neuromorphic Silicon Process & Model")
        lines.append('"""')
        lines.append("")
        lines.append("try:")
        lines.append("    from lava.magma.core.process.process import AbstractProcess")
        lines.append("    from lava.magma.core.process.ports.ports import InPort, OutPort")
        lines.append("    from lava.magma.core.process.variable import Var")
        lines.append("    from lava.magma.core.model.py.model import PyLoihiProcessModel")
        lines.append("    from lava.magma.core.model.py.ports import PyInPort, PyOutPort")
        lines.append("    from lava.magma.core.model.py.type import LavaPyType")
        lines.append("    from lava.magma.core.resources import CPU")
        lines.append("    from lava.magma.core.decorator import implements, requires, tag")
        lines.append("    from lava.magma.core.sync.protocols.loihi_protocol import LoihiProtocol")
        lines.append("    from lava.magma.core.run_conditions import RunSteps")
        lines.append("    from lava.magma.core.run_configs import PyExecCfg")
        lines.append("except ImportError:")
        lines.append("    from compiler.loihi2_ref_sim import (")
        lines.append("        AbstractProcess,")
        lines.append("        InPort,")
        lines.append("        OutPort,")
        lines.append("        Var,")
        lines.append("        PyLoihiProcessModel,")
        lines.append("        PyInPort,")
        lines.append("        PyOutPort,")
        lines.append("        LavaPyType,")
        lines.append("        CPU,")
        lines.append("        implements,")
        lines.append("        requires,")
        lines.append("        tag,")
        lines.append("        LoihiProtocol,")
        lines.append("        RunSteps,")
        lines.append("        PyExecCfg,")
        lines.append("        reset_processes,")
        lines.append("    )")
        lines.append("")

        # 1. Emit Organoid Process and ProcessModel classes
        organoid_names = list(self.organoids.keys())
        if not organoid_names:
            organoid_names = ["DefaultOrganoid"]

        for org_name in organoid_names:
            org_node = self.organoids.get(org_name)
            n_cells = 100
            if org_node and org_node.cells is not None:
                n_cells = self._extract_int_val(org_node.cells, default=100)
            elif org_node and org_node.radius is not None:
                n_cells = 100

            # Organoid Process definition
            lines.append(f"class {org_name}Process(AbstractProcess):")
            lines.append(f'    """Loihi-2 Process representation of organoid {org_name}."""')
            lines.append("    def __init__(self, **kwargs):")
            lines.append("        super().__init__(**kwargs)")
            lines.append(f'        self.n_neurons = kwargs.get("n_neurons", {n_cells})')
            lines.append('        self.cm = kwargs.get("cm", 200.0)          # pF membrane capacitance')
            lines.append('        self.gl = kwargs.get("gl", 10.0)           # nS leak conductance')
            lines.append('        self.tau_m = kwargs.get("tau_m", 20.0)      # ms membrane time constant')
            lines.append('        self.e_leak = kwargs.get("e_leak", -70.0)  # mV leak resting potential')
            lines.append('        self.v_thresh = kwargs.get("v_thresh", -50.0) # mV threshold')
            lines.append('        self.v_reset = kwargs.get("v_reset", -75.0)   # mV reset')
            lines.append('        self.refractory_steps = kwargs.get("refractory_steps", 20) # 2.0 ms @ dt=0.1ms')
            lines.append('        self.stdp_enabled = kwargs.get("stdp_enabled", False)')
            lines.append('        self.s_in = InPort(shape=(self.n_neurons,), name="s_in")')
            lines.append('        self.s_out = OutPort(shape=(self.n_neurons,), name="s_out")')
            lines.append('        self.v = Var(shape=(self.n_neurons,), init=self.e_leak, name="v")')
            lines.append('        self.weights = Var(shape=(self.n_neurons, self.n_neurons), init=0.5, name="weights")')
            lines.append("")

            # Process Model definition
            lines.append(f"@implements(proc={org_name}Process, protocol=LoihiProtocol)")
            lines.append("@requires(CPU)")
            lines.append('@tag("floating_pt")')
            lines.append(f"class {org_name}Model(PyLoihiProcessModel):")
            lines.append(f'    """PyLoihi execution model for {org_name}."""')
            lines.append("    s_in: PyInPort = LavaPyType(PyInPort.VEC_DENSE, float)")
            lines.append("    s_out: PyOutPort = LavaPyType(PyOutPort.VEC_DENSE, float)")
            lines.append("    v: Var = LavaPyType(Var, float)")
            lines.append("    weights: Var = LavaPyType(Var, float)")
            lines.append("")

        primary_organoid_var = organoid_names[0].lower()

        # 2. Emit helper functions
        for fn_name, fn_node in self.functions.items():
            if fn_name == "main":
                continue
            params_str = ", ".join(p.name for p in fn_node.params)
            lines.append(f"def {fn_name}({params_str}):")
            body_lines = self._emit_block(fn_node.body, primary_organoid_var, indent=1)
            lines.extend(body_lines)
            lines.append("")

        # 3. Emit main function orchestrating the network
        lines.append("def main():")
        lines.append("    if 'reset_processes' in globals():")
        lines.append("        reset_processes()")
        lines.append("    # Instantiate Lava Processes for organoid populations")
        for org_name in organoid_names:
            var_name = org_name.lower()
            org_node = self.organoids.get(org_name)
            if org_node and org_node.perfusion is not None:
                lines.append("    # W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for organoid perfusion")
            lines.append(f"    {var_name} = {org_name}Process()")

        # Connect projections (preserving channel index, weight, and millisecond delay)
        for i, conn in enumerate(self.connections):
            src_name = self._resolve_target_name(conn.source).lower()
            dst_name = self._resolve_target_name(conn.target).lower()
            src_idx = self._resolve_target_index(conn.source)
            dst_idx = self._resolve_target_index(conn.target)
            weight = self._extract_weight_val(conn.weight, default=0.5)
            delay_ms = max(0.1, self._extract_time_ms(conn.delay_ms, default=1.0))
            delay_steps = max(1, int(round(delay_ms / 0.1)))
            is_stdp = bool(conn.plasticity and "stdp" in str(conn.plasticity).lower())

            lines.append(f"    # Synaptic projection {i+1}: {src_name} -> {dst_name}")
            lines.append(f"    {src_name}.s_out.connect({dst_name}.s_in)")
            if is_stdp:
                lines.append(f"    {dst_name}.stdp_enabled = True # STDP learning rule configured")
            lines.append(f"    if hasattr({dst_name}, 'add_projection'):")
            lines.append(
                f"        {dst_name}.add_projection({src_name}, pre_idx={src_idx!r}, post_idx={dst_idx!r}, "
                f"weight={weight}, delay_steps={delay_steps}, stdp_enabled={is_stdp})"
            )

        # Emit statements from main() or top-level
        main_fn = self.functions.get("main")
        stmts_to_emit = []
        if main_fn and main_fn.body:
            stmts_to_emit.extend(main_fn.body.statements)
        stmts_to_emit.extend(self.top_statements)

        if stmts_to_emit:
            for stmt in stmts_to_emit:
                stmt_lines = self._emit_stmt(stmt, primary_organoid_var, indent=1)
                lines.extend(stmt_lines)
        else:
            lines.append(f"    # Run default baseline tick")
            lines.append(f"    {primary_organoid_var}.run(condition=RunSteps(num_steps=1), run_cfg=PyExecCfg())")

        lines.append(f"    {primary_organoid_var}.stop()")
        lines.append(f"    return {primary_organoid_var}")
        lines.append("")
        lines.append('if __name__ == "__main__":')
        lines.append("    main()")
        return "\n".join(lines) + "\n"

    def _emit_expr(self, node: Optional[ASTNode], org_var: str) -> str:
        if node is None:
            return "None"
        if isinstance(node, LiteralNode):
            if node.type_name == "bool":
                return "True" if node.value in (True, "true", "True", 1) else "False"
            if node.type_name == "string":
                return repr(str(node.value))
            return str(node.value)
        if isinstance(node, PhysicalLiteralNode):
            if node.unit_suffix in ("uL/min", "mL/min", "uL", "mL", "kPa", "bar", "rpm"):
                self._warn_unsupported(f"unit_{node.unit_suffix}", f"Physical unit '{node.unit_suffix}' lowered to dimensionless scalar.")
            if node.dimension == Dimension.TIME:
                return str(float(node.si_value) * 1000.0)
            return str(node.magnitude)
        if isinstance(node, IdentifierNode):
            if node.name == "true":
                return "True"
            if node.name == "false":
                return "False"
            if node.name in self.channel_indices:
                return str(self.channel_indices[node.name])
            return node.name
        if isinstance(node, BinaryOpNode):
            op_map = {"&&": "and", "||": "or"}
            py_op = op_map.get(node.op, node.op)
            return f"({self._emit_expr(node.left, org_var)} {py_op} {self._emit_expr(node.right, org_var)})"
        if isinstance(node, UnaryOpNode):
            if node.op == "!":
                return f"(not {self._emit_expr(node.operand, org_var)})"
            return f"({node.op}{self._emit_expr(node.operand, org_var)})"
        if isinstance(node, IndexNode):
            target_str = self._emit_expr(node.target, org_var)
            if len(node.indices) == 2:
                return f"({self._emit_expr(node.indices[0], org_var)} * 8 + {self._emit_expr(node.indices[1], org_var)})"
            if len(node.indices) == 1:
                return f"{target_str}[{self._emit_expr(node.indices[0], org_var)}]"
            return target_str
        if isinstance(node, CallNode):
            callee_str = self._emit_expr(node.callee, org_var)
            args_str = ", ".join(self._emit_expr(a, org_var) for a in node.args)
            return f"{callee_str}({args_str})"
        if isinstance(node, DomainCallNode):
            if node.func_name == "read_spikes":
                win_ms = self._extract_time_ms(node.args[1], default=10.0) if len(node.args) > 1 else 10.0
                win_steps = max(1, int(round(win_ms / 0.1)))
                if len(node.args) >= 1:
                    ch_expr = self._emit_expr(node.args[0], org_var)
                    return (
                        f"(sum(1 for _s in {org_var}.spikes[-{win_steps}:] "
                        f"if _s[int({ch_expr}) % getattr({org_var}, 'n_neurons', 100)] > 0.0) "
                        f"if {org_var}.spikes else 0)"
                    )
                return f"(sum(sum(1 for _x in _s if _x > 0.0) for _s in {org_var}.spikes[-{win_steps}:]) if {org_var}.spikes else 0)"
            if node.func_name in ("pop_firing_rate", "read_population_rate"):
                win_ms = self._extract_time_ms(node.args[0], default=10.0) if len(node.args) >= 1 else 10.0
                win_steps = max(1, int(round(win_ms / 0.1)))
                win_s = max(0.0001, win_steps * 0.0001)
                return (
                    f"(sum(sum(1 for _x in _s if _x > 0.0) for _s in {org_var}.spikes[-{win_steps}:]) / "
                    f"(max(1, getattr({org_var}, 'n_neurons', 100)) * {win_s:.6f}) if {org_var}.spikes else 0.0)"
                )
            if self._is_wetware_call(node.func_name):
                self._warn_unsupported(node.func_name, "Safe no-op returning 0.0.")
                return "0.0"
            return f"{node.func_name}()"
        if isinstance(node, RangeNode):
            return f"range({self._emit_expr(node.start, org_var)}, {self._emit_expr(node.end, org_var)})"
        return "0"

    def _emit_block(self, block: Optional[BlockNode], org_var: str, indent: int = 1) -> List[str]:
        sp = "    " * indent
        if block is None or not block.statements:
            return [f"{sp}pass"]
        lines: List[str] = []
        for stmt in block.statements:
            lines.extend(self._emit_stmt(stmt, org_var, indent=indent))
        return lines

    def _emit_stmt(self, stmt: ASTNode, org_var: str, indent: int = 1) -> List[str]:
        sp = "    " * indent
        if isinstance(stmt, LetStmtNode):
            if isinstance(stmt.initializer, DomainCallNode) and self._is_wetware_call(stmt.initializer.func_name):
                self._warn_unsupported(stmt.initializer.func_name, "Lowered to safe constant assignment.")
                return [
                    f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for {stmt.initializer.func_name}",
                    f"{sp}{stmt.name} = 0.0"
                ]
            if stmt.initializer is None:
                return [f"{sp}{stmt.name} = 0"]
            val = self._emit_expr(stmt.initializer, org_var)
            return [f"{sp}{stmt.name} = {val}"]

        if isinstance(stmt, AssignStmtNode):
            target = self._emit_expr(stmt.target, org_var)
            val = self._emit_expr(stmt.value, org_var)
            return [f"{sp}{target} = {val}"]

        if isinstance(stmt, StimStmtNode):
            v_val = self._extract_voltage_val(stmt.voltage)
            is_current = (
                isinstance(stmt.voltage, PhysicalLiteralNode) and stmt.voltage.dimension == Dimension.CURRENT
            )
            if not is_current and v_val is not None and abs(v_val) > 1.2:
                self._warn_unsupported("electrochemical_water_window", f"Voltage {v_val:.2f}V exceeds water window +/-1.2V.")
                return [
                    f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for electrochemical water-window guard",
                    f"{sp}pass"
                ]
            phase1_ms = max(0.1, self._extract_time_ms(stmt.phase1, default=0.2))
            dur_steps = max(1, int(round(phase1_ms / 0.1)))
            if is_current and v_val is not None:
                # Si Amps -> pA calibrated stimulus current
                i_stim_pa = min(100000.0, max(5000.0, abs(v_val) * 1e9))
            else:
                v_mag = abs(v_val) if v_val is not None else 0.4
                decay_p1 = math.exp(-phase1_ms / 20.0)
                i_base = 10.0 * 20.0 / max(1.0 - decay_p1, 1e-4)
                i_stim_pa = min(100000.0, max(5000.0, i_base * max(0.25, v_mag / 0.4)))
            ch_expr = self._emit_expr(stmt.channel, org_var)
            return [
                f"{sp}# Biphasic stimulation lowered to calibrated multi-tick channel-localized current injection",
                f"{sp}if hasattr({org_var}, '_ensure_model'):",
                f"{sp}    {org_var}._ensure_model().inject_stimulus({i_stim_pa:.2f}, channel={ch_expr}, duration_steps={dur_steps})"
            ]

        if isinstance(stmt, SyncTickStmtNode):
            count_val = self._emit_expr(stmt.count, org_var) if stmt.count else "1"
            return [
                f"{sp}# Advance discrete simulation clock",
                f"{sp}{org_var}.run(condition=RunSteps(num_steps=max(1, int({count_val}))), run_cfg=PyExecCfg())"
            ]

        if isinstance(stmt, ModulateStmtNode):
            if len(stmt.args) == 3:
                pre_e = self._emit_expr(stmt.args[0], org_var)
                post_e = self._emit_expr(stmt.args[1], org_var)
                dw_e = self._emit_expr(stmt.args[2], org_var)
                return [
                    f"{sp}# STDP plasticity modulation (direct synapse delta)",
                    f"{sp}{org_var}.stdp_enabled = True",
                    f"{sp}if hasattr({org_var}, '_ensure_model'):",
                    f"{sp}    _m = {org_var}._ensure_model()",
                    f"{sp}    _m.stdp_enabled = True",
                    f"{sp}    _pi = int({pre_e}) % _m.n_neurons",
                    f"{sp}    _pj = int({post_e}) % _m.n_neurons",
                    f"{sp}    _m.weights[_pi][_pj] = max(0.0, min(2.0, _m.weights[_pi][_pj] + float({dw_e})))"
                ]
            rate_expr = self._emit_expr(stmt.args[0], org_var) if len(stmt.args) >= 1 else "1.0"
            return [
                f"{sp}# STDP plasticity modulation",
                f"{sp}_stdp_scale = float({rate_expr})",
                f"{sp}{org_var}.stdp_enabled = (_stdp_scale > 0.0)",
                f"{sp}if hasattr({org_var}, '_ensure_model'):",
                f"{sp}    _m = {org_var}._ensure_model()",
                f"{sp}    _m.stdp_enabled = (_stdp_scale > 0.0)",
                f"{sp}    _m.a_plus = max(0.0, 0.01 * _stdp_scale)",
                f"{sp}    _m.a_minus = max(0.0, 0.012 * _stdp_scale)",
            ]

        if isinstance(stmt, StreamDeclNode):
            self._warn_unsupported(
                "stream",
                f"Unbounded stream '{stmt.name}' lowered to bounded 100-iteration neuromorphic loop."
            )
            lines = [
                f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: bounded lowering of stream '{stmt.name}'",
                f"{sp}for _stream_tick in range(100):"
            ]
            emitted_any = False
            for item in stmt.items:
                if item.kind == "cycle" and item.cycle_block is not None:
                    lines.extend(self._emit_block(item.cycle_block, org_var, indent + 1))
                    emitted_any = True
            if not emitted_any:
                lines.append(f"{sp}    pass")
            return lines

        if isinstance(stmt, IfStmtNode):
            lines = [f"{sp}if {self._emit_expr(stmt.condition, org_var)}:"]
            lines.extend(self._emit_block(stmt.then_block, org_var, indent + 1))
            if stmt.else_block:
                lines.append(f"{sp}else:")
                if isinstance(stmt.else_block, BlockNode):
                    lines.extend(self._emit_block(stmt.else_block, org_var, indent + 1))
                else:
                    lines.extend(self._emit_stmt(stmt.else_block, org_var, indent + 1))
            return lines

        if isinstance(stmt, WhileStmtNode):
            lines = [f"{sp}while {self._emit_expr(stmt.condition, org_var)}:"]
            lines.extend(self._emit_block(stmt.body, org_var, indent + 1))
            return lines

        if isinstance(stmt, ForStmtNode):
            lines = [f"{sp}for {stmt.var_name} in range({self._emit_expr(stmt.range_start, org_var)}, {self._emit_expr(stmt.range_end, org_var)}):"]
            lines.extend(self._emit_block(stmt.body, org_var, indent + 1))
            return lines

        if isinstance(stmt, ReturnStmtNode):
            val = f" {self._emit_expr(stmt.value, org_var)}" if stmt.value else ""
            return [f"{sp}return{val}"]

        if isinstance(stmt, ExprStmtNode):
            if isinstance(stmt.expr, DomainCallNode) and self._is_wetware_call(stmt.expr.func_name):
                self._warn_unsupported(stmt.expr.func_name, "Lowered to safe no-op.")
                return [
                    f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for {stmt.expr.func_name}",
                    f"{sp}pass"
                ]
            return [f"{sp}{self._emit_expr(stmt.expr, org_var)}"]

        return [f"{sp}pass"]


class SpiNNakerEmitter(NeuromorphicEmitterBase):
    """
    Emits standard PyNN 0.9/0.10 Python scripts for SpiNNaker neuromorphic hardware
    (pyNN.spiNNaker) or the in-repo deterministic reference simulator.
    """
    def __init__(self):
        super().__init__(target_name="spinnaker")

    def emit(self, ast_root: ProgramNode) -> str:
        self._collect_declarations(ast_root)
        lines: List[str] = []

        lines.append('"""')
        lines.append("Auto-generated by WetLang Compiler (Target: SpiNNaker PyNN)")
        lines.append("Architecture: SpiNNaker Neuromorphic Silicon (PyNN 0.9/0.10)")
        lines.append('"""')
        lines.append("")
        lines.append("try:")
        lines.append("    import pyNN.spiNNaker as sim")
        lines.append("except ImportError:")
        lines.append("    import compiler.spinnaker_ref_sim as sim")
        lines.append("")

        organoid_names = list(self.organoids.keys())
        if not organoid_names:
            organoid_names = ["DefaultOrganoid"]

        primary_organoid_var = organoid_names[0].lower()

        # Emit helper functions
        for fn_name, fn_node in self.functions.items():
            if fn_name == "main":
                continue
            params_str = ", ".join(p.name for p in fn_node.params)
            lines.append(f"def {fn_name}({params_str}):")
            body_lines = self._emit_block(fn_node.body, primary_organoid_var, indent=1)
            lines.extend(body_lines)
            lines.append("")

        # Compute max_delay dynamically from all connections
        max_conn_delay_ms = 10.0
        for conn in self.connections:
            d_ms = max(0.1, self._extract_time_ms(conn.delay_ms, default=1.0))
            if d_ms > max_conn_delay_ms:
                max_conn_delay_ms = d_ms

        # Emit main function
        lines.append("def main():")
        lines.append("    # Initialize PyNN SpiNNaker simulation runtime")
        lines.append(f"    sim.setup(timestep=0.1, min_delay=0.1, max_delay={max_conn_delay_ms:.2f})")
        lines.append("")

        # Create populations for organoids
        for org_name in organoid_names:
            var_name = org_name.lower()
            org_node = self.organoids.get(org_name)
            n_cells = 100
            if org_node and org_node.cells is not None:
                n_cells = self._extract_int_val(org_node.cells, default=100)
            elif org_node and org_node.radius is not None:
                n_cells = 100

            if org_node and org_node.perfusion is not None:
                lines.append(f"    # W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for organoid perfusion")

            lines.append(f"    # Population for organoid: {org_name}")
            lines.append(f"    cell_params_{var_name} = {{")
            lines.append('        "cm": 0.2,')
            lines.append('        "tau_m": 20.0,')
            lines.append('        "v_rest": -70.0,')
            lines.append('        "v_thresh": -50.0,')
            lines.append('        "v_reset": -75.0,')
            lines.append('        "tau_syn_E": 5.0,')
            lines.append('        "tau_syn_I": 5.0,')
            lines.append('        "e_rev_E": 0.0,')
            lines.append('        "e_rev_I": -80.0,')
            lines.append('        "tau_refrac": 2.0,')
            lines.append("    }")
            lines.append(f'    {var_name} = sim.Population({n_cells}, sim.IF_cond_exp(**cell_params_{var_name}), label="{org_name}")')
            lines.append(f'    {var_name}.record(["spikes", "v"])')
            lines.append("")

        # Create projections between populations (converting WetLang weight -> uS and SI time -> ms)
        for i, conn in enumerate(self.connections):
            src_name = self._resolve_target_name(conn.source).lower()
            dst_name = self._resolve_target_name(conn.target).lower()
            src_idx = self._resolve_target_index(conn.source)
            dst_idx = self._resolve_target_index(conn.target)
            raw_weight = self._extract_weight_val(conn.weight, default=0.5)
            weight_us = min(0.04, max(0.001, raw_weight * 0.025))
            delay_ms = max(0.1, self._extract_time_ms(conn.delay_ms, default=1.0))

            if src_idx is not None or dst_idx is not None:
                s_i = src_idx if src_idx is not None else 0
                d_j = dst_idx if dst_idx is not None else 0
                conn_expr = f"sim.FromListConnector([({s_i} % {src_name}.size, {d_j} % {dst_name}.size, {weight_us:.6f}, {delay_ms:.4f})])"
            else:
                conn_expr = "sim.AllToAllConnector()"

            is_stdp = conn.plasticity and "stdp" in str(conn.plasticity).lower()
            lines.append(f"    # Synaptic Projection {i+1}: {src_name} -> {dst_name}")
            if is_stdp:
                lines.append(f"    stdp_mech_{i} = sim.STDPMechanism(")
                lines.append("        timing_dependence=sim.SpikePairRule(tau_plus=20.0, tau_minus=20.0, A_plus=0.0005, A_minus=0.0006),")
                lines.append("        weight_dependence=sim.AdditiveWeightDependence(w_min=0.0, w_max=0.04),")
                lines.append(f"        weight={weight_us:.6f},")
                lines.append(f"        delay={delay_ms:.4f}")
                lines.append("    )")
                lines.append(f"    proj_{i} = sim.Projection({src_name}, {dst_name}, {conn_expr}, synapse_type=stdp_mech_{i})")
            else:
                lines.append(f"    syn_{i} = sim.StaticSynapse(weight={weight_us:.6f}, delay={delay_ms:.4f})")
                lines.append(f"    proj_{i} = sim.Projection({src_name}, {dst_name}, {conn_expr}, synapse_type=syn_{i})")
            lines.append("")

        # Emit statements from main() or top-level
        main_fn = self.functions.get("main")
        stmts_to_emit = []
        if main_fn and main_fn.body:
            stmts_to_emit.extend(main_fn.body.statements)
        stmts_to_emit.extend(self.top_statements)

        if stmts_to_emit:
            for stmt in stmts_to_emit:
                stmt_lines = self._emit_stmt(stmt, primary_organoid_var, indent=1)
                lines.extend(stmt_lines)
        else:
            lines.append("    # Run default baseline tick")
            lines.append("    sim.run(0.1)")

        lines.append(f"    data = {primary_organoid_var}.get_data()")
        lines.append("    sim.end()")
        lines.append(f"    return data")
        lines.append("")
        lines.append('if __name__ == "__main__":')
        lines.append("    main()")
        return "\n".join(lines) + "\n"

    def _emit_expr(self, node: Optional[ASTNode], org_var: str) -> str:
        if node is None:
            return "None"
        if isinstance(node, LiteralNode):
            if node.type_name == "bool":
                return "True" if node.value in (True, "true", "True", 1) else "False"
            if node.type_name == "string":
                return repr(str(node.value))
            return str(node.value)
        if isinstance(node, PhysicalLiteralNode):
            if node.unit_suffix in ("uL/min", "mL/min", "uL", "mL", "kPa", "bar", "rpm"):
                self._warn_unsupported(f"unit_{node.unit_suffix}", f"Physical unit '{node.unit_suffix}' lowered to dimensionless scalar.")
            if node.dimension == Dimension.TIME:
                return str(float(node.si_value) * 1000.0)
            return str(node.magnitude)
        if isinstance(node, IdentifierNode):
            if node.name == "true":
                return "True"
            if node.name == "false":
                return "False"
            if node.name in self.channel_indices:
                return str(self.channel_indices[node.name])
            return node.name
        if isinstance(node, BinaryOpNode):
            op_map = {"&&": "and", "||": "or"}
            py_op = op_map.get(node.op, node.op)
            return f"({self._emit_expr(node.left, org_var)} {py_op} {self._emit_expr(node.right, org_var)})"
        if isinstance(node, UnaryOpNode):
            if node.op == "!":
                return f"(not {self._emit_expr(node.operand, org_var)})"
            return f"({node.op}{self._emit_expr(node.operand, org_var)})"
        if isinstance(node, IndexNode):
            target_str = self._emit_expr(node.target, org_var)
            if len(node.indices) == 2:
                return f"({self._emit_expr(node.indices[0], org_var)} * 8 + {self._emit_expr(node.indices[1], org_var)})"
            if len(node.indices) == 1:
                return f"{target_str}[{self._emit_expr(node.indices[0], org_var)}]"
            return target_str
        if isinstance(node, CallNode):
            callee_str = self._emit_expr(node.callee, org_var)
            args_str = ", ".join(self._emit_expr(a, org_var) for a in node.args)
            return f"{callee_str}({args_str})"
        if isinstance(node, DomainCallNode):
            if node.func_name == "read_spikes":
                win_ms = self._extract_time_ms(node.args[1], default=10.0) if len(node.args) > 1 else 10.0
                if len(node.args) >= 1:
                    ch_expr = self._emit_expr(node.args[0], org_var)
                    return (
                        f"sum(1 for _t in {org_var}.get_data().segments[0].spiketrains[int({ch_expr}) % {org_var}.size] "
                        f"if _t >= max(0.0, sim.get_current_time() - {win_ms:.4f}))"
                    )
                return (
                    f"sum(1 for _st in {org_var}.get_data().segments[0].spiketrains "
                    f"for _t in _st if _t >= max(0.0, sim.get_current_time() - {win_ms:.4f}))"
                )
            if node.func_name in ("pop_firing_rate", "read_population_rate"):
                win_ms = self._extract_time_ms(node.args[0], default=10.0) if len(node.args) >= 1 else 10.0
                win_s = max(0.0001, win_ms * 0.001)
                return (
                    f"(sum(1 for _st in {org_var}.get_data().segments[0].spiketrains "
                    f"for _t in _st if _t >= max(0.0, sim.get_current_time() - {win_ms:.4f})) / "
                    f"(max(1, {org_var}.size) * {win_s:.6f}))"
                )
            if self._is_wetware_call(node.func_name):
                self._warn_unsupported(node.func_name, "Safe no-op returning 0.0.")
                return "0.0"
            return f"{node.func_name}()"
        if isinstance(node, RangeNode):
            return f"range({self._emit_expr(node.start, org_var)}, {self._emit_expr(node.end, org_var)})"
        return "0"

    def _emit_block(self, block: Optional[BlockNode], org_var: str, indent: int = 1) -> List[str]:
        sp = "    " * indent
        if block is None or not block.statements:
            return [f"{sp}pass"]
        lines: List[str] = []
        for stmt in block.statements:
            lines.extend(self._emit_stmt(stmt, org_var, indent=indent))
        return lines

    def _emit_stmt(self, stmt: ASTNode, org_var: str, indent: int = 1) -> List[str]:
        sp = "    " * indent
        if isinstance(stmt, LetStmtNode):
            if isinstance(stmt.initializer, DomainCallNode) and self._is_wetware_call(stmt.initializer.func_name):
                self._warn_unsupported(stmt.initializer.func_name, "Lowered to safe constant assignment.")
                return [
                    f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for {stmt.initializer.func_name}",
                    f"{sp}{stmt.name} = 0.0"
                ]
            if stmt.initializer is None:
                return [f"{sp}{stmt.name} = 0"]
            val = self._emit_expr(stmt.initializer, org_var)
            return [f"{sp}{stmt.name} = {val}"]

        if isinstance(stmt, AssignStmtNode):
            target = self._emit_expr(stmt.target, org_var)
            val = self._emit_expr(stmt.value, org_var)
            return [f"{sp}{target} = {val}"]

        if isinstance(stmt, StimStmtNode):
            v_val = self._extract_voltage_val(stmt.voltage)
            is_current = (
                isinstance(stmt.voltage, PhysicalLiteralNode) and stmt.voltage.dimension == Dimension.CURRENT
            )
            if not is_current and v_val is not None and abs(v_val) > 1.2:
                self._warn_unsupported("electrochemical_water_window", f"Voltage {v_val:.2f}V exceeds water window +/-1.2V.")
                return [
                    f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for electrochemical water-window guard",
                    f"{sp}pass"
                ]
            v_mag = abs(v_val) if v_val is not None else 0.4
            w_us = min(0.04, max(0.005, 0.015 * (v_mag / 0.4)))
            ch_expr = self._emit_expr(stmt.channel, org_var)
            return [
                f"{sp}# Biphasic stimulation pulse mapped to channel-localized SpikeSourceArray projection (uS)",
                f"{sp}_stim_ch = int({ch_expr}) % {org_var}.size",
                f"{sp}_stim_source = sim.Population(1, sim.SpikeSourceArray(spike_times=[sim.get_current_time() + 0.1]))",
                f"{sp}sim.Projection(_stim_source, {org_var}, sim.FromListConnector([(0, _stim_ch, {w_us:.6f}, 0.1)]), synapse_type=sim.StaticSynapse(weight={w_us:.6f}, delay=0.1))"
            ]

        if isinstance(stmt, SyncTickStmtNode):
            count_val = self._emit_expr(stmt.count, org_var) if stmt.count else "1"
            return [
                f"{sp}# Advance biological time by 0.1 ms per tick",
                f"{sp}sim.run(0.1 * max(1, int({count_val})))"
            ]

        if isinstance(stmt, ModulateStmtNode):
            self._warn_unsupported(
                "modulate_stdp",
                "Runtime STDP gain modulation lowered to safe no-op on static PyNN projection."
            )
            return [
                f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for modulate_stdp",
                f"{sp}pass"
            ]

        if isinstance(stmt, StreamDeclNode):
            self._warn_unsupported(
                "stream",
                f"Unbounded stream '{stmt.name}' lowered to bounded 100-iteration neuromorphic loop."
            )
            lines = [
                f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: bounded lowering of stream '{stmt.name}'",
                f"{sp}for _stream_tick in range(100):"
            ]
            emitted_any = False
            for item in stmt.items:
                if item.kind == "cycle" and item.cycle_block is not None:
                    lines.extend(self._emit_block(item.cycle_block, org_var, indent + 1))
                    emitted_any = True
            if not emitted_any:
                lines.append(f"{sp}    pass")
            return lines

        if isinstance(stmt, IfStmtNode):
            lines = [f"{sp}if {self._emit_expr(stmt.condition, org_var)}:"]
            lines.extend(self._emit_block(stmt.then_block, org_var, indent + 1))
            if stmt.else_block:
                lines.append(f"{sp}else:")
                if isinstance(stmt.else_block, BlockNode):
                    lines.extend(self._emit_block(stmt.else_block, org_var, indent + 1))
                else:
                    lines.extend(self._emit_stmt(stmt.else_block, org_var, indent + 1))
            return lines

        if isinstance(stmt, WhileStmtNode):
            lines = [f"{sp}while {self._emit_expr(stmt.condition, org_var)}:"]
            lines.extend(self._emit_block(stmt.body, org_var, indent + 1))
            return lines

        if isinstance(stmt, ForStmtNode):
            lines = [f"{sp}for {stmt.var_name} in range({self._emit_expr(stmt.range_start, org_var)}, {self._emit_expr(stmt.range_end, org_var)}):"]
            lines.extend(self._emit_block(stmt.body, org_var, indent + 1))
            return lines

        if isinstance(stmt, ReturnStmtNode):
            val = f" {self._emit_expr(stmt.value, org_var)}" if stmt.value else ""
            return [f"{sp}return{val}"]

        if isinstance(stmt, ExprStmtNode):
            if isinstance(stmt.expr, DomainCallNode) and self._is_wetware_call(stmt.expr.func_name):
                self._warn_unsupported(stmt.expr.func_name, "Lowered to safe no-op.")
                return [
                    f"{sp}# W_SUBSTRATE_UNSUPPORTED_OP: safe no-op for {stmt.expr.func_name}",
                    f"{sp}pass"
                ]
            return [f"{sp}{self._emit_expr(stmt.expr, org_var)}"]

        return [f"{sp}pass"]


def emit_loihi2(ast_root: ProgramNode) -> str:
    """Emits Intel Lava Python source code from an AST representation."""
    emitter = Loihi2Emitter()
    return emitter.emit(ast_root)


def emit_spinnaker(ast_root: ProgramNode) -> str:
    """Emits standard PyNN 0.9/0.10 Python script from an AST representation."""
    emitter = SpiNNakerEmitter()
    return emitter.emit(ast_root)


def _run_neuromorphic_semantic_check(ast: ProgramNode, filename: str, bypass_safety: bool) -> None:
    """Runs SemanticAnalyzer on neuromorphic entry points unless explicitly bypassed."""
    if bypass_safety:
        return
    from compiler.semantic import SemanticAnalyzer, SemanticError

    analyzer = SemanticAnalyzer(ast, collect_diagnostics=True, filename=filename)
    analyzer.analyze()
    for diag in analyzer.diagnostics:
        if diag.severity == "error" and diag.code != "ERR_STATIC_VOLTAGE_CLAMP_EXCEEDED":
            raise SemanticError(diag.message, diag.line, diag.column, diag.code)


def compile_to_loihi2(source_text: str, filename: str = "<stdin>", bypass_safety: bool = False) -> str:
    """Compiles .wet source directly to Intel Lava Python code for Intel Loihi-2."""
    from compiler.lexer import Lexer
    from compiler.parser import Parser

    lexer = Lexer(source_text)
    tokens = lexer.tokenize()
    parser = Parser(tokens, source_text=source_text)
    ast = parser.parse()
    _run_neuromorphic_semantic_check(ast, filename=filename, bypass_safety=bypass_safety)
    return emit_loihi2(ast)


def compile_to_spinnaker(source_text: str, filename: str = "<stdin>", bypass_safety: bool = False) -> str:
    """Compiles .wet source directly to SpiNNaker PyNN script for SpiNNaker cores."""
    from compiler.lexer import Lexer
    from compiler.parser import Parser

    lexer = Lexer(source_text)
    tokens = lexer.tokenize()
    parser = Parser(tokens, source_text=source_text)
    ast = parser.parse()
    _run_neuromorphic_semantic_check(ast, filename=filename, bypass_safety=bypass_safety)
    return emit_spinnaker(ast)

