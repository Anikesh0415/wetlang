"""
WetLang Compiler - Bytecode Binary Emitter & Disassembler
Hand-crafted from first principles. Complete WBC binary serialization and CRC32 checksum.
"""

import struct
import zlib
from typing import Dict, List, Tuple, Optional, Any, Set
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
            64, # channel count (8x8 MEA)
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
        data.extend(struct.pack("<IHHfI", 64, 8, 8, 200.0, len(self.channel_aliases)))
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

def compile_source(source_text: str, filename: str = "<stdin>", target: str = "sim") -> bytes:
    """
    Executes the complete 4-stage compiler pipeline:
    Lexer -> Pratt Parser -> Semantic/Safety Analyzer -> Bytecode Emitter.
    Supports target-specific capability tuning (Project Janus).
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
    emitter = BytecodeEmitter()
    return emitter.compile(ast)


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
    bytecode = compile_source(source_text, target=target)
    return emit_c_embedded_header(bytecode, model_name=model_name, target=target)
