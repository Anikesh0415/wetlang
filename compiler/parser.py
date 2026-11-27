"""
WetLang Compiler - Recursive-Descent Pratt Parser
Hand-crafted from first principles. Precedence climbing for expressions.
Zero external parser generator dependencies.
"""

from typing import List, Optional, Tuple, Any
from compiler.token import (
    Token,
    TokenType,
    Dimension,
    UNIT_SUFFIXES,
)
from compiler.ast_nodes import (
    ASTNode,
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
    SetBlankingStmtNode,
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


class ParseError(Exception):
    """Rich parser diagnostic error with line and column reporting."""
    def __init__(self, message: str, line: int, column: int, expected: Optional[str] = None, found: Optional[str] = None):
        detail = message
        if expected and found:
            detail = f"{message} (expected {expected}, found {found})"
        super().__init__(f"ParseError at line {line}, column {column}: {detail}")
        self.message = message
        self.line = line
        self.column = column
        self.expected = expected
        self.found = found


# Precedence Binding Powers: (left_bp, right_bp)
INFIX_BINDING_POWERS = {
    TokenType.OR_OR: (10, 11),
    TokenType.AND_AND: (20, 21),
    TokenType.EQ_EQ: (30, 31),
    TokenType.NOT_EQ: (30, 31),
    TokenType.LT: (40, 41),
    TokenType.LT_EQ: (40, 41),
    TokenType.GT: (40, 41),
    TokenType.GT_EQ: (40, 41),
    TokenType.PLUS: (50, 51),
    TokenType.MINUS: (50, 51),
    TokenType.STAR: (60, 61),
    TokenType.SLASH: (60, 61),
    TokenType.PERCENT: (60, 61),
}

PREFIX_BINDING_POWER = 70
POSTFIX_BINDING_POWER = 80


class Parser:
    """
    Recursive-descent Pratt parser.
    Parses top-level declarations, statements, domain blocks, and expressions.
    """
    def __init__(self, tokens: List[Token], source_text: str = ""):
        self.tokens: List[Token] = tokens
        self.source_text: str = source_text
        self.cursor: int = 0

    def _current(self) -> Token:
        if self.cursor < len(self.tokens):
            return self.tokens[self.cursor]
        return self.tokens[-1]

    def _peek(self, offset: int = 0) -> Token:
        idx = self.cursor + offset
        if idx < len(self.tokens):
            return self.tokens[idx]
        return self.tokens[-1]

    def _advance(self) -> Token:
        tok = self._current()
        if self.cursor < len(self.tokens):
            self.cursor += 1
        return tok

    def _match(self, expected_type: TokenType) -> bool:
        if self._current().type == expected_type:
            self._advance()
            return True
        return False

    def _is_identifier_token(self, tok: Token) -> bool:
        return tok.type in (
            TokenType.IDENTIFIER,
            TokenType.CYCLE,
            TokenType.STREAM,
            TokenType.MODE,
            TokenType.SENSOR,
            TokenType.MOTOR,
            TokenType.PUMP,
            TokenType.VALVE,
            TokenType.PORT,
            TokenType.ACTUATOR,
        )

    def _expect_identifier(self, context: str = "") -> Token:
        curr = self._current()
        if self._is_identifier_token(curr):
            return self._advance()
        msg = f"Unexpected token '{curr.raw_text or curr.type.name}'"
        if context:
            msg += f" while parsing {context}"
        raise ParseError(
            msg,
            curr.line,
            curr.column,
            expected="IDENTIFIER",
            found=curr.type.name
        )

    def _expect(self, expected_type: TokenType, context: str = "") -> Token:
        curr = self._current()
        if curr.type == expected_type:
            return self._advance()
        msg = f"Unexpected token '{curr.raw_text or curr.type.name}'"
        if context:
            msg += f" while parsing {context}"
        raise ParseError(
            msg,
            curr.line,
            curr.column,
            expected=expected_type.name,
            found=curr.type.name
        )

    # =========================================================================
    # Program & Top-Level Declarations
    # =========================================================================

    def parse(self) -> ProgramNode:
        """Parse full compilation unit into a ProgramNode."""
        program = ProgramNode(declarations=[], line=1, column=1)
        while self._current().type != TokenType.EOF:
            decl = self._parse_top_level_decl()
            if decl is not None:
                program.declarations.append(decl)
        return program

    def _parse_top_level_decl(self) -> Optional[ASTNode]:
        curr = self._current()

        # MEA Grid declaration
        if curr.type == TokenType.GRID:
            return self._parse_grid_decl()

        # Multi-Organoid Universal Architecture Declarations
        if curr.type in (TokenType.ORGANOID, TokenType.TISSUE):
            return self._parse_organoid_decl()

        if curr.type == TokenType.CONNECT:
            return self._parse_connect_decl()

        if curr.type == TokenType.PORT:
            return self._parse_port_decl()

        # Channel declaration
        if curr.type == TokenType.CHANNEL:
            return self._parse_channel_decl()

        # Function declaration
        if curr.type == TokenType.FN:
            return self._parse_fn_decl()

        # Stream declaration
        if curr.type == TokenType.STREAM:
            return self._parse_stream_decl()

        # Top-level statements (e.g. scripts, variable declarations, control loops)
        return self._parse_statement()

    # =========================================================================
    # Universal Multi-Organoid, Connectome, and Grid Declarations
    # =========================================================================

    def _parse_organoid_decl(self) -> OrganoidDeclNode:
        tok = self._advance()  # 'organoid' or 'tissue'
        name_tok = self._expect_identifier("organoid name")
        node = OrganoidDeclNode(name=name_tok.value, line=tok.line, column=tok.column)

        curr = self._current()
        if curr.type == TokenType.LBRACKET:
            # Parametric array: organoid Cluster[1024]; or organoid Hive[N];
            self._advance()
            node.count = self.parse_expression()
            self._expect(TokenType.RBRACKET, "organoid array closing ']'")
            if self._match(TokenType.SEMICOLON):
                return node

        if self._match(TokenType.LBRACE):
            while not self._match(TokenType.RBRACE):
                prop_tok = self._expect(TokenType.IDENTIFIER, "organoid property name")
                self._expect(TokenType.COLON, "organoid property colon")
                prop_val = self.parse_expression()
                self._match(TokenType.SEMICOLON)

                pname = prop_tok.value
                node.properties[pname] = prop_val
                if pname in ("cells", "density"):
                    node.cells = prop_val
                elif pname in ("radius", "geometry"):
                    node.radius = prop_val
                elif pname == "perfusion":
                    node.perfusion = prop_val
            return node
        elif self._match(TokenType.SEMICOLON):
            return node
        else:
            raise ParseError("Expected '{' or ';' after organoid declaration", tok.line, tok.column)

    def _parse_connect_decl(self) -> ConnectDeclNode:
        tok = self._expect(TokenType.CONNECT, "connect declaration")
        src = self.parse_expression()
        self._expect(TokenType.ARROW_RIGHT, "connect arrow '->'")
        tgt = self.parse_expression()
        node = ConnectDeclNode(source=src, target=tgt, line=tok.line, column=tok.column)

        if self._current().raw_text == "with" or self._current().type == TokenType.LBRACE:
            if self._current().raw_text == "with":
                self._advance()
            self._expect(TokenType.LBRACE, "connect properties opening '{'")
            while not self._match(TokenType.RBRACE):
                prop_tok = self._expect(TokenType.IDENTIFIER, "connect property name")
                self._expect(TokenType.COLON, "connect property colon")
                prop_val = self.parse_expression()
                self._match(TokenType.SEMICOLON)
                pname = prop_tok.value
                if "delay" in pname:
                    node.delay_ms = prop_val
                elif "weight" in pname:
                    node.weight = prop_val
                elif "plasticity" in pname:
                    node.plasticity = str(prop_val)
        self._match(TokenType.SEMICOLON)
        return node

    def _parse_port_decl(self) -> PortDeclNode:
        tok = self._expect(TokenType.PORT, "port declaration")
        name_tok = self._expect_identifier("port name")
        node = PortDeclNode(name=name_tok.value, line=tok.line, column=tok.column)
        if self._match(TokenType.LBRACE):
            while not self._match(TokenType.RBRACE):
                if self._current().type in (TokenType.IDENTIFIER, TokenType.MODE):
                    prop_tok = self._advance()
                else:
                    prop_tok = self._expect(TokenType.IDENTIFIER, "port property name")
                self._expect(TokenType.COLON, "port property colon")
                pname = prop_tok.value if isinstance(prop_tok.value, str) else prop_tok.raw_text
                if pname == "mode":
                    mode_tok = self._current()
                    if mode_tok.type in (
                        TokenType.BIPHASIC_STIM,
                        TokenType.SPIKE_READOUT,
                        TokenType.VOLTAGE_SENSE,
                        TokenType.BIDIRECTIONAL,
                        TokenType.IDENTIFIER,
                    ):
                        node.mode = mode_tok.value or mode_tok.raw_text
                        self._advance()
                    else:
                        node.mode = str(self.parse_expression())
                else:
                    prop_val = self.parse_expression()
                    if pname == "channels":
                        node.channels = prop_val
                self._match(TokenType.SEMICOLON)
        return node

    def _parse_grid_decl(self) -> GridDeclNode:
        tok = self._expect(TokenType.GRID, "grid declaration")
        name_tok = self._expect_identifier("grid name")
        node = GridDeclNode(name=name_tok.value, line=tok.line, column=tok.column)

        curr = self._current()
        if curr.type == TokenType.LBRACKET:
            # Array syntax: grid mea[8, 8]; or grid mea[64];
            self._advance() # [
            first_dim = self.parse_expression()
            second_dim = None
            if self._match(TokenType.COMMA):
                second_dim = self.parse_expression()
            self._expect(TokenType.RBRACKET, "grid dimensions")
            self._expect(TokenType.SEMICOLON, "grid declaration end")

            if second_dim is not None:
                node.rows = first_dim
                node.cols = second_dim
            else:
                node.rows = first_dim
                node.cols = None
            return node

        elif curr.type == TokenType.LBRACE:
            # Block property syntax: grid mea { rows: 8; cols: 8; pitch: 200um; }
            self._advance() # {
            while not self._match(TokenType.RBRACE):
                prop_name_tok = self._expect(TokenType.IDENTIFIER, "grid property name")
                self._expect(TokenType.COLON, "grid property colon")
                prop_val = self.parse_expression()
                self._expect(TokenType.SEMICOLON, "grid property semicolon")

                pname = prop_name_tok.value
                if pname == "rows":
                    node.rows = prop_val
                elif pname == "cols":
                    node.cols = prop_val
                elif pname == "pitch":
                    node.pitch = prop_val
                elif pname == "base_voltage":
                    node.base_voltage = prop_val
            return node
        else:
            raise ParseError(
                f"Expected '[' or '{{' after grid identifier '{name_tok.value}'",
                curr.line,
                curr.column,
                expected="[ or {",
                found=curr.type.name
            )

    def _parse_channel_decl(self) -> ChannelDeclNode:
        tok = self._expect(TokenType.CHANNEL, "channel declaration")
        name_tok = self._expect_identifier("channel name")
        self._expect(TokenType.ASSIGN, "channel assignment '='")

        # Target can be: mea[0, 2], mea[0], or [0 .. 15]
        target = self.parse_expression()

        mode_val: Optional[str] = None
        if self._match(TokenType.MODE):
            self._expect(TokenType.COLON, "channel mode colon")
            mode_tok = self._current()
            if mode_tok.type in (
                TokenType.BIPHASIC_STIM,
                TokenType.SPIKE_READOUT,
                TokenType.VOLTAGE_SENSE,
                TokenType.BIDIRECTIONAL,
                TokenType.IDENTIFIER,
            ):
                mode_val = mode_tok.value or mode_tok.raw_text
                self._advance()
            else:
                raise ParseError(
                    f"Invalid channel mode '{mode_tok.raw_text}'",
                    mode_tok.line,
                    mode_tok.column
                )

        self._expect(TokenType.SEMICOLON, "channel declaration semicolon")
        return ChannelDeclNode(name=name_tok.value, target=target, mode=mode_val, line=tok.line, column=tok.column)

    # =========================================================================
    # Function & Stream Declarations
    # =========================================================================

    def _parse_fn_decl(self) -> FnDeclNode:
        tok = self._expect(TokenType.FN, "function declaration")
        name_tok = self._expect_identifier("function name")
        self._expect(TokenType.LPAREN, "function parameter list")

        params: List[ParamNode] = []
        if self._current().type != TokenType.RPAREN:
            while True:
                p_name_tok = self._expect_identifier("parameter name")
                self._expect(TokenType.COLON, "parameter colon")
                p_type = self._parse_type_name()
                params.append(ParamNode(name=p_name_tok.value, type_name=p_type, line=p_name_tok.line, column=p_name_tok.column))
                if not self._match(TokenType.COMMA):
                    break

        self._expect(TokenType.RPAREN, "function parameter list end")

        return_type: Optional[str] = None
        if self._match(TokenType.ARROW_RIGHT):
            return_type = self._parse_type_name()

        body = self._parse_block()
        return FnDeclNode(
            name=name_tok.value,
            params=params,
            return_type=return_type,
            body=body,
            line=tok.line,
            column=tok.column
        )

    def _parse_stream_decl(self) -> StreamDeclNode:
        tok = self._expect(TokenType.STREAM, "stream declaration")
        name_tok = self._expect(TokenType.IDENTIFIER, "stream name")
        self._expect(TokenType.LBRACE, "stream block opening")

        items: List[StreamItemNode] = []
        while not self._match(TokenType.RBRACE):
            item_tok = self._current()
            if self._match(TokenType.BIND):
                left_tok = self._expect_identifier("bind source")
                if self._match(TokenType.ARROW_RIGHT):
                    right_tok = self._expect_identifier("bind target")
                    self._expect(TokenType.SEMICOLON, "bind statement semicolon")
                    items.append(StreamItemNode(
                        kind="bind_out",
                        left=left_tok.value,
                        right=right_tok.value,
                        line=item_tok.line,
                        column=item_tok.column
                    ))
                elif self._match(TokenType.ARROW_LEFT):
                    right_tok = self._expect_identifier("bind source")
                    self._expect(TokenType.SEMICOLON, "bind statement semicolon")
                    items.append(StreamItemNode(
                        kind="bind_in",
                        left=left_tok.value,
                        right=right_tok.value,
                        line=item_tok.line,
                        column=item_tok.column
                    ))
                else:
                    raise ParseError("Expected '->' or '<-' in bind statement", self._current().line, self._current().column)
            elif self._match(TokenType.CYCLE):
                cycle_block = self._parse_block()
                items.append(StreamItemNode(
                    kind="cycle",
                    cycle_block=cycle_block,
                    line=item_tok.line,
                    column=item_tok.column
                ))
            else:
                raise ParseError(
                    f"Unexpected token '{self._current().raw_text}' in stream declaration",
                    self._current().line,
                    self._current().column
                )

        return StreamDeclNode(name=name_tok.value, items=items, line=tok.line, column=tok.column)

    def _parse_type_name(self) -> str:
        curr = self._current()
        type_tokens = (
            TokenType.INT, TokenType.FLOAT, TokenType.BOOL, TokenType.STRING,
            TokenType.CHANNEL, TokenType.GRID,
            TokenType.TYPE_VOLTAGE, TokenType.TYPE_CURRENT, TokenType.TYPE_TIME,
            TokenType.TYPE_FREQUENCY, TokenType.TYPE_LENGTH, TokenType.TYPE_CHARGE,
            TokenType.IDENTIFIER
        )
        if curr.type in type_tokens:
            self._advance()
            return curr.raw_text or curr.value
        raise ParseError(f"Expected type name, found '{curr.raw_text}'", curr.line, curr.column)

    # =========================================================================
    # Statements
    # =========================================================================

    def _parse_statement(self) -> ASTNode:
        curr = self._current()

        # Block statement
        if curr.type == TokenType.LBRACE:
            return self._parse_block()

        # let [mut] x [: type] = expr;
        if curr.type == TokenType.LET:
            return self._parse_let_statement()

        # C/Rust-style typed declaration: int x = 0; float y = 1.0;
        if curr.type in (
            TokenType.INT, TokenType.FLOAT, TokenType.BOOL, TokenType.STRING,
            TokenType.TYPE_VOLTAGE, TokenType.TYPE_CURRENT, TokenType.TYPE_TIME,
            TokenType.TYPE_FREQUENCY, TokenType.TYPE_LENGTH, TokenType.TYPE_CHARGE
        ) and self._is_identifier_token(self._peek(1)) and self._peek(2).type in (TokenType.ASSIGN, TokenType.SEMICOLON):
            return self._parse_typed_var_decl()

        # stim_biphasic(...)
        if curr.type == TokenType.STIM_BIPHASIC:
            return self._parse_stim_statement()

        # set_blanking(duration_ms) or set_blanking(channel, duration_ms)
        if curr.type == TokenType.SET_BLANKING:
            return self._parse_set_blanking_statement()

        # modulate_stdp(...)
        if curr.type == TokenType.MODULATE_STDP:
            return self._parse_modulate_statement()

        # sync_tick [()];
        if curr.type == TokenType.SYNC_TICK:
            return self._parse_sync_tick_statement()

        # if (...) ... [else ...]
        if curr.type == TokenType.IF:
            return self._parse_if_statement()

        # while (...) ...
        if curr.type == TokenType.WHILE:
            return self._parse_while_statement()

        # for identifier in start .. end ...
        if curr.type == TokenType.FOR:
            return self._parse_for_statement()

        # return [expr];
        if curr.type == TokenType.RETURN:
            return self._parse_return_statement()

        # Assignment or Expression Statement
        return self._parse_assign_or_expr_statement()

    def _parse_block(self) -> BlockNode:
        tok = self._expect(TokenType.LBRACE, "block opening '{'")
        stmts: List[ASTNode] = []
        while not self._match(TokenType.RBRACE):
            if self._current().type == TokenType.EOF:
                raise ParseError("Unterminated block statement, missing '}'", tok.line, tok.column)
            stmt = self._parse_statement()
            if stmt is not None:
                stmts.append(stmt)
        return BlockNode(statements=stmts, line=tok.line, column=tok.column)

    def _parse_let_statement(self) -> LetStmtNode:
        tok = self._expect(TokenType.LET, "let statement")
        is_mut = self._match(TokenType.MUT)
        name_tok = self._expect_identifier("variable name")

        type_name: Optional[str] = None
        if self._match(TokenType.COLON):
            type_name = self._parse_type_name()

        self._expect(TokenType.ASSIGN, "assignment '='")
        init_expr = self.parse_expression()
        self._expect(TokenType.SEMICOLON, "let statement semicolon")
        return LetStmtNode(
            name=name_tok.value,
            is_mut=is_mut,
            type_name=type_name,
            initializer=init_expr,
            line=tok.line,
            column=tok.column
        )

    def _parse_typed_var_decl(self) -> LetStmtNode:
        type_tok = self._advance()
        type_name = type_tok.raw_text or type_tok.value
        name_tok = self._expect_identifier("variable name")
        init_expr = None
        if self._match(TokenType.ASSIGN):
            init_expr = self.parse_expression()
        self._expect(TokenType.SEMICOLON, "variable declaration semicolon")
        return LetStmtNode(
            name=name_tok.value,
            is_mut=True,
            type_name=type_name,
            initializer=init_expr,
            line=type_tok.line,
            column=type_tok.column
        )

    def _parse_stim_statement(self) -> StimStmtNode:
        tok = self._expect(TokenType.STIM_BIPHASIC, "stim_biphasic call")
        self._expect(TokenType.LPAREN, "stim_biphasic arguments '('")

        channel = self.parse_expression()
        self._expect(TokenType.COMMA, "after channel argument")
        voltage = self.parse_expression()
        self._expect(TokenType.COMMA, "after voltage argument")
        phase1 = self.parse_expression()
        self._expect(TokenType.COMMA, "after phase1 argument")
        phase2 = self.parse_expression()

        interphase = None
        if self._match(TokenType.COMMA):
            interphase = self.parse_expression()

        self._expect(TokenType.RPAREN, "stim_biphasic closing ')'")
        self._expect(TokenType.SEMICOLON, "stim_biphasic semicolon")

        return StimStmtNode(
            channel=channel,
            voltage=voltage,
            phase1=phase1,
            phase2=phase2,
            interphase=interphase,
            line=tok.line,
            column=tok.column
        )

    def _parse_set_blanking_statement(self) -> SetBlankingStmtNode:
        """Parse: set_blanking(duration_ms) or set_blanking(channel, duration_ms)"""
        tok = self._expect(TokenType.SET_BLANKING, "set_blanking call")
        self._expect(TokenType.LPAREN, "set_blanking arguments '('")
        first_arg = self.parse_expression()
        channel_node = None
        duration_node = first_arg
        if self._match(TokenType.COMMA):
            channel_node = first_arg
            duration_node = self.parse_expression()
        self._expect(TokenType.RPAREN, "set_blanking closing ')'")
        self._expect(TokenType.SEMICOLON, "set_blanking semicolon")
        return SetBlankingStmtNode(
            channel=channel_node,
            duration=duration_node,
            line=tok.line,
            column=tok.column
        )

    def _parse_modulate_statement(self) -> ModulateStmtNode:
        tok = self._expect(TokenType.MODULATE_STDP, "modulate_stdp call")
        self._expect(TokenType.LPAREN, "modulate_stdp arguments '('")

        args: List[ASTNode] = []
        if self._current().type != TokenType.RPAREN:
            while True:
                args.append(self.parse_expression())
                if not self._match(TokenType.COMMA):
                    break

        self._expect(TokenType.RPAREN, "modulate_stdp closing ')'")
        self._expect(TokenType.SEMICOLON, "modulate_stdp semicolon")
        return ModulateStmtNode(args=args, line=tok.line, column=tok.column)

    def _parse_sync_tick_statement(self) -> SyncTickStmtNode:
        tok = self._expect(TokenType.SYNC_TICK, "sync_tick statement")
        count: Optional[ASTNode] = None
        if self._match(TokenType.LPAREN):
            if self._current().type != TokenType.RPAREN:
                count = self.parse_expression()
            self._expect(TokenType.RPAREN, "sync_tick closing ')'")
        self._expect(TokenType.SEMICOLON, "sync_tick semicolon")
        return SyncTickStmtNode(count=count, line=tok.line, column=tok.column)

    def _parse_if_statement(self) -> IfStmtNode:
        tok = self._expect(TokenType.IF, "if statement")
        self._expect(TokenType.LPAREN, "if condition opening '('")
        cond = self.parse_expression()
        self._expect(TokenType.RPAREN, "if condition closing ')'")

        then_block = self._parse_block()
        else_block: Optional[ASTNode] = None

        if self._match(TokenType.ELSE):
            if self._current().type == TokenType.IF:
                else_block = self._parse_if_statement()
            else:
                else_block = self._parse_block()

        return IfStmtNode(
            condition=cond,
            then_block=then_block,
            else_block=else_block,
            line=tok.line,
            column=tok.column
        )

    def _parse_while_statement(self) -> WhileStmtNode:
        tok = self._expect(TokenType.WHILE, "while statement")
        self._expect(TokenType.LPAREN, "while condition opening '('")
        cond = self.parse_expression()
        self._expect(TokenType.RPAREN, "while condition closing ')'")
        body = self._parse_block()
        return WhileStmtNode(condition=cond, body=body, line=tok.line, column=tok.column)

    def _parse_for_statement(self) -> ForStmtNode:
        tok = self._expect(TokenType.FOR, "for statement")
        var_tok = self._expect_identifier("for loop variable")
        self._expect(TokenType.IN, "for loop 'in'")
        range_start = self.parse_expression()
        self._expect(TokenType.DOT_DOT, "range '..'")
        range_end = self.parse_expression()
        body = self._parse_block()
        return ForStmtNode(
            var_name=var_tok.value,
            range_start=range_start,
            range_end=range_end,
            body=body,
            line=tok.line,
            column=tok.column
        )

    def _parse_return_statement(self) -> ReturnStmtNode:
        tok = self._expect(TokenType.RETURN, "return statement")
        val: Optional[ASTNode] = None
        if self._current().type != TokenType.SEMICOLON:
            val = self.parse_expression()
        self._expect(TokenType.SEMICOLON, "return statement semicolon")
        return ReturnStmtNode(value=val, line=tok.line, column=tok.column)

    def _parse_assign_or_expr_statement(self) -> ASTNode:
        start_tok = self._current()
        expr = self.parse_expression()

        # Check if this expression is followed by '='
        if self._match(TokenType.ASSIGN):
            if not isinstance(expr, (IdentifierNode, IndexNode)):
                raise ParseError(
                    f"Invalid assignment target at line {start_tok.line}, column {start_tok.column}",
                    start_tok.line,
                    start_tok.column
                )
            val = self.parse_expression()
            self._expect(TokenType.SEMICOLON, "assignment semicolon")
            return AssignStmtNode(target=expr, value=val, line=start_tok.line, column=start_tok.column)

        self._expect(TokenType.SEMICOLON, "expression statement semicolon")
        return ExprStmtNode(expr=expr, line=start_tok.line, column=start_tok.column)

    # =========================================================================
    # Pratt Expression Parser
    # =========================================================================

    def parse_expression(self, min_bp: int = 0) -> ASTNode:
        """Pratt precedence climbing expression parser."""
        token = self._advance()
        left = self._parse_prefix(token)

        while True:
            curr = self._current()
            if curr.type == TokenType.EOF or curr.type in (
                TokenType.SEMICOLON, TokenType.RPAREN, TokenType.RBRACKET,
                TokenType.RBRACE, TokenType.COMMA, TokenType.COLON, TokenType.DOT_DOT
            ):
                break

            # Handle immediate unit suffix following a numeric literal (e.g. 1.0 V or 200 us)
            if isinstance(left, LiteralNode) and left.type_name in ("int", "float"):
                unit_text = curr.raw_text or curr.value
                if unit_text in UNIT_SUFFIXES:
                    self._advance()
                    dim, scale = UNIT_SUFFIXES[unit_text]
                    mag = float(left.value)
                    left = PhysicalLiteralNode(
                        magnitude=mag,
                        dimension=dim,
                        si_value=mag * scale,
                        unit_suffix=unit_text,
                        line=left.line,
                        column=left.column
                    )
                    continue

            # Infix Function Call: left(...)
            if curr.type == TokenType.LPAREN:
                if POSTFIX_BINDING_POWER < min_bp:
                    break
                self._advance() # (
                args: List[ASTNode] = []
                if self._current().type != TokenType.RPAREN:
                    while True:
                        args.append(self.parse_expression(0))
                        if not self._match(TokenType.COMMA):
                            break
                self._expect(TokenType.RPAREN, "call argument closing ')'")
                left = CallNode(callee=left, args=args, line=left.line, column=left.column)
                continue

            # Infix Indexing: left[...] or left[r, c]
            if curr.type == TokenType.LBRACKET:
                if POSTFIX_BINDING_POWER < min_bp:
                    break
                self._advance() # [
                indices: List[ASTNode] = []
                while True:
                    indices.append(self.parse_expression(0))
                    if not self._match(TokenType.COMMA):
                        break
                self._expect(TokenType.RBRACKET, "indexing closing ']'")
                left = IndexNode(target=left, indices=indices, line=left.line, column=left.column)
                continue

            # Standard Binary Infix Operators
            if curr.type in INFIX_BINDING_POWERS:
                l_bp, r_bp = INFIX_BINDING_POWERS[curr.type]
                if l_bp < min_bp:
                    break
                op_tok = self._advance()
                right = self.parse_expression(r_bp)
                left = BinaryOpNode(
                    left=left,
                    op=op_tok.raw_text,
                    right=right,
                    line=op_tok.line,
                    column=op_tok.column
                )
                continue

            break

        return left

    def _parse_prefix(self, token: Token) -> ASTNode:
        """Parses prefix expressions: literals, unary operators, grouping, identifiers."""
        # Unary operators: -, !
        if token.type in (TokenType.MINUS, TokenType.NOT):
            operand = self.parse_expression(PREFIX_BINDING_POWER)
            return UnaryOpNode(op=token.raw_text, operand=operand, line=token.line, column=token.column)

        # Parenthesized expression: (expr)
        if token.type == TokenType.LPAREN:
            expr = self.parse_expression(0)
            self._expect(TokenType.RPAREN, "closing ')'")
            return expr

        # Range literal or array slice: [start .. end]
        if token.type == TokenType.LBRACKET:
            start_expr = self.parse_expression(0)
            if self._match(TokenType.DOT_DOT):
                end_expr = self.parse_expression(0)
                self._expect(TokenType.RBRACKET, "range closing ']'")
                return RangeNode(start=start_expr, end=end_expr, line=token.line, column=token.column)
            self._expect(TokenType.RBRACKET, "closing ']'")
            return start_expr

        # Integer literal
        if token.type == TokenType.INT_LIT:
            return LiteralNode(value=token.value, type_name="int", line=token.line, column=token.column)

        # Float literal
        if token.type == TokenType.FLOAT_LIT:
            return LiteralNode(value=token.value, type_name="float", line=token.line, column=token.column)

        # Boolean literal
        if token.type == TokenType.BOOL_LIT:
            return LiteralNode(value=token.value, type_name="bool", line=token.line, column=token.column)

        # String literal
        if token.type == TokenType.STRING_LIT:
            return LiteralNode(value=token.value, type_name="string", line=token.line, column=token.column)

        # Physical literal with immediate suffix (e.g. 10ms, 0.5V)
        if token.type == TokenType.PHYSICAL_LIT:
            # Extract suffix from raw text
            suffix = ""
            for s in UNIT_SUFFIXES:
                if token.raw_text.endswith(s):
                    suffix = s
                    break
            return PhysicalLiteralNode(
                magnitude=float(token.value),
                dimension=token.dimension,
                si_value=float(token.si_value) if token.si_value is not None else float(token.value),
                unit_suffix=suffix,
                line=token.line,
                column=token.column
            )

        # Built-in Domain Expression Calls
        if token.type in (
            TokenType.READ_SPIKES,
            TokenType.READ_VOLTAGE,
            TokenType.POP_FIRING_RATE,
            TokenType.READ_POPULATION_RATE,
            TokenType.PUMP_SET_RATE,
            TokenType.PUMP_DISPENSE,
            TokenType.VALVE_SET,
            TokenType.VALVE_OPEN,
            TokenType.VALVE_CLOSE,
            TokenType.MOTOR_STEP,
            TokenType.READ_PRESSURE,
            TokenType.READ_TEMPERATURE,
        ):
            func_name = token.raw_text
            self._expect(TokenType.LPAREN, f"{func_name} arguments '('")
            args: List[ASTNode] = []
            if self._current().type != TokenType.RPAREN:
                while True:
                    args.append(self.parse_expression(0))
                    if not self._match(TokenType.COMMA):
                        break
            self._expect(TokenType.RPAREN, f"{func_name} closing ')'")
            return DomainCallNode(func_name=func_name, args=args, line=token.line, column=token.column)

        # Standard Identifier or contextual keyword used as expression
        if token.type == TokenType.IDENTIFIER or token.type in (TokenType.CYCLE, TokenType.STREAM, TokenType.MODE):
            name = token.raw_text or token.value
            return IdentifierNode(name=name, line=token.line, column=token.column)

        # Type conversion calls: int(expr), float(expr)
        if token.type in (TokenType.INT, TokenType.FLOAT, TokenType.BOOL, TokenType.STRING):
            if self._current().type == TokenType.LPAREN:
                # Type cast expression: float(spikes)
                self._advance() # (
                arg = self.parse_expression(0)
                self._expect(TokenType.RPAREN, "cast closing ')'")
                return CallNode(
                    callee=IdentifierNode(name=token.raw_text, line=token.line, column=token.column),
                    args=[arg],
                    line=token.line,
                    column=token.column
                )
            return IdentifierNode(name=token.raw_text, line=token.line, column=token.column)

        raise ParseError(
            f"Expected expression, found '{token.raw_text or token.type.name}'",
            token.line,
            token.column
        )
