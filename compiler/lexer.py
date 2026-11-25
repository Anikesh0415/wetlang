"""
WetLang Compiler - Deterministic DFA Lexical Scanner
Hand-crafted from first principles. Zero regex library dependencies.
"""

from typing import List, Optional
from compiler.token import (
    Token,
    TokenType,
    Dimension,
    KEYWORDS,
    UNIT_SUFFIXES,
    SORTED_UNIT_SUFFIXES,
)


class LexerError(Exception):
    """Raised when a lexical scanning invariant is violated."""
    def __init__(self, message: str, line: int, column: int):
        super().__init__(f"LexerError at line {line}, column {column}: {message}")
        self.message = message
        self.line = line
        self.column = column


class Lexer:
    """
    Deterministic DFA lexical scanner.
    Maintains 1-based line and column counters, character offsets,
    and performs immediate physical unit suffix binding on numeric literals.
    """
    def __init__(self, source: str):
        if source.startswith("\ufeff"):
            source = source[1:]
        self.source: str = source
        self.length: int = len(source)
        self.cursor: int = 0
        self.line: int = 1
        self.column: int = 1

    def _peek(self, offset: int = 0) -> Optional[str]:
        idx = self.cursor + offset
        if idx < self.length:
            return self.source[idx]
        return None

    def _advance(self) -> Optional[str]:
        if self.cursor >= self.length:
            return None
        ch = self.source[self.cursor]
        self.cursor += 1
        if ch == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return ch

    def _match(self, expected: str) -> bool:
        if self.cursor >= self.length:
            return False
        if self.source[self.cursor] != expected:
            return False
        self._advance()
        return True

    def tokenize(self) -> List[Token]:
        tokens: List[Token] = []
        while self.cursor < self.length:
            # Skip whitespace
            ch = self._peek()
            if ch in (' ', '\t', '\r', '\n'):
                self._advance()
                continue

            # Skip comments: single-line // and block /* ... */
            if ch == '/' and self._peek(1) == '/':
                # Single-line comment
                self._advance() # /
                self._advance() # /
                while self._peek() is not None and self._peek() != '\n':
                    self._advance()
                continue

            if ch == '/' and self._peek(1) == '*':
                # Multi-line block comment
                start_line = self.line
                start_col = self.column
                self._advance() # /
                self._advance() # *
                closed = False
                while self._peek() is not None:
                    if self._peek() == '*' and self._peek(1) == '/':
                        self._advance() # *
                        self._advance() # /
                        closed = True
                        break
                    self._advance()
                if not closed:
                    raise LexerError("Unterminated block comment", start_line, start_col)
                continue

            # Record token start position
            tok_line = self.line
            tok_col = self.column
            tok_start_offset = self.cursor

            # Number literal (or physical literal)
            if ch.isdigit():
                tok = self._scan_number()
                tokens.append(tok)
                continue

            # String literal
            if ch == '"':
                tok = self._scan_string()
                tokens.append(tok)
                continue

            # Identifier or keyword
            if ch.isalpha() or ch == '_':
                tok = self._scan_identifier_or_keyword()
                tokens.append(tok)
                continue

            # Multi-character or single-character operators & delimiters
            tok = self._scan_operator_or_delimiter()
            tokens.append(tok)

        # Append EOF token
        tokens.append(Token(
            type=TokenType.EOF,
            value="",
            line=self.line,
            column=self.column,
            dimension=Dimension.NONE,
            si_value=None,
            raw_text=""
        ))
        return tokens

    def _scan_number(self) -> Token:
        start_line = self.line
        start_col = self.column
        start_offset = self.cursor

        # Consume integer part
        while self._peek() is not None and self._peek().isdigit():
            self._advance()

        # Check for fractional part
        is_float = False
        if self._peek() == '.' and self._peek(1) is not None and self._peek(1).isdigit():
            # Ensure it's not a range operator '..'
            if self._peek(1) != '.':
                is_float = True
                self._advance() # consume '.'
                while self._peek() is not None and self._peek().isdigit():
                    self._advance()

        # Check for scientific exponent (e.g. 1e-3, 2.5e4)
        if self._peek() in ('e', 'E'):
            next_ch = self._peek(1)
            if next_ch in ('+', '-') and self._peek(2) is not None and self._peek(2).isdigit():
                is_float = True
                self._advance() # e
                self._advance() # +/-
                while self._peek() is not None and self._peek().isdigit():
                    self._advance()
            elif next_ch is not None and next_ch.isdigit():
                is_float = True
                self._advance() # e
                while self._peek() is not None and self._peek().isdigit():
                    self._advance()

        num_str = self.source[start_offset:self.cursor]
        base_val = float(num_str) if is_float else int(num_str)

        # Check for immediate unit suffix (no intervening whitespace)
        # Match longest matching suffix
        matched_suffix: Optional[str] = None
        for suffix in SORTED_UNIT_SUFFIXES:
            s_len = len(suffix)
            candidate = self.source[self.cursor:self.cursor + s_len]
            if candidate == suffix:
                # Ensure the suffix is not just the prefix of a larger identifier
                next_after = self.source[self.cursor + s_len:self.cursor + s_len + 1]
                if next_after and (next_after.isalnum() or next_after == '_'):
                    continue
                matched_suffix = suffix
                break

        if matched_suffix is not None:
            # Advance through suffix characters
            for _ in range(len(matched_suffix)):
                self._advance()
            raw_full = self.source[start_offset:self.cursor]
            dim, scale = UNIT_SUFFIXES[matched_suffix]
            si_val = float(base_val) * scale
            return Token(
                type=TokenType.PHYSICAL_LIT,
                value=float(base_val),
                line=start_line,
                column=start_col,
                dimension=dim,
                si_value=si_val,
                raw_text=raw_full
            )

        # Normal numeric literal
        raw_full = self.source[start_offset:self.cursor]
        if is_float:
            return Token(
                type=TokenType.FLOAT_LIT,
                value=float(base_val),
                line=start_line,
                column=start_col,
                dimension=Dimension.NONE,
                si_value=None,
                raw_text=raw_full
            )
        else:
            return Token(
                type=TokenType.INT_LIT,
                value=int(base_val),
                line=start_line,
                column=start_col,
                dimension=Dimension.NONE,
                si_value=None,
                raw_text=raw_full
            )

    def _scan_string(self) -> Token:
        start_line = self.line
        start_col = self.column
        start_offset = self.cursor

        self._advance() # opening quote '"'
        chars: List[str] = []
        while True:
            ch = self._peek()
            if ch is None:
                raise LexerError("Unterminated string literal", start_line, start_col)
            if ch == '"':
                self._advance() # closing quote
                break
            if ch == '\\':
                self._advance() # escape char
                esc = self._advance()
                if esc == 'n':
                    chars.append('\n')
                elif esc == 't':
                    chars.append('\t')
                elif esc == 'r':
                    chars.append('\r')
                elif esc == '"':
                    chars.append('"')
                elif esc == '\\':
                    chars.append('\\')
                else:
                    chars.append(esc if esc is not None else '')
            else:
                chars.append(self._advance())

        val = "".join(chars)
        raw = self.source[start_offset:self.cursor]
        return Token(
            type=TokenType.STRING_LIT,
            value=val,
            line=start_line,
            column=start_col,
            dimension=Dimension.NONE,
            si_value=None,
            raw_text=raw
        )

    def _scan_identifier_or_keyword(self) -> Token:
        start_line = self.line
        start_col = self.column
        start_offset = self.cursor

        while self._peek() is not None and (self._peek().isalnum() or self._peek() == '_'):
            self._advance()

        text = self.source[start_offset:self.cursor]

        # Check keyword table
        if text in KEYWORDS:
            tok_type = KEYWORDS[text]
            if tok_type == TokenType.TRUE:
                return Token(
                    type=TokenType.BOOL_LIT,
                    value=True,
                    line=start_line,
                    column=start_col,
                    dimension=Dimension.NONE,
                    si_value=None,
                    raw_text=text
                )
            elif tok_type == TokenType.FALSE:
                return Token(
                    type=TokenType.BOOL_LIT,
                    value=False,
                    line=start_line,
                    column=start_col,
                    dimension=Dimension.NONE,
                    si_value=None,
                    raw_text=text
                )
            return Token(
                type=tok_type,
                value=text,
                line=start_line,
                column=start_col,
                dimension=Dimension.NONE,
                si_value=None,
                raw_text=text
            )

        # Regular identifier
        return Token(
            type=TokenType.IDENTIFIER,
            value=text,
            line=start_line,
            column=start_col,
            dimension=Dimension.NONE,
            si_value=None,
            raw_text=text
        )

    def _scan_operator_or_delimiter(self) -> Token:
        start_line = self.line
        start_col = self.column
        ch = self._advance()

        # Two-character operators
        if ch == '=':
            if self._peek() == '=':
                self._advance()
                return Token(TokenType.EQ_EQ, "==", start_line, start_col, raw_text="==")
            return Token(TokenType.ASSIGN, "=", start_line, start_col, raw_text="=")

        if ch == '!':
            if self._peek() == '=':
                self._advance()
                return Token(TokenType.NOT_EQ, "!=", start_line, start_col, raw_text="!=")
            return Token(TokenType.NOT, "!", start_line, start_col, raw_text="!")

        if ch == '<':
            if self._peek() == '=':
                self._advance()
                return Token(TokenType.LT_EQ, "<=", start_line, start_col, raw_text="<=")
            elif self._peek() == '-':
                self._advance()
                return Token(TokenType.ARROW_LEFT, "<-", start_line, start_col, raw_text="<-")
            return Token(TokenType.LT, "<", start_line, start_col, raw_text="<")

        if ch == '>':
            if self._peek() == '=':
                self._advance()
                return Token(TokenType.GT_EQ, ">=", start_line, start_col, raw_text=">=")
            return Token(TokenType.GT, ">", start_line, start_col, raw_text=">")

        if ch == '&':
            if self._peek() == '&':
                self._advance()
                return Token(TokenType.AND_AND, "&&", start_line, start_col, raw_text="&&")
            raise LexerError(f"Unexpected character '{ch}', expected '&&'", start_line, start_col)

        if ch == '|':
            if self._peek() == '|':
                self._advance()
                return Token(TokenType.OR_OR, "||", start_line, start_col, raw_text="||")
            raise LexerError(f"Unexpected character '{ch}', expected '||'", start_line, start_col)

        if ch == '-':
            if self._peek() == '>':
                self._advance()
                return Token(TokenType.ARROW_RIGHT, "->", start_line, start_col, raw_text="->")
            return Token(TokenType.MINUS, "-", start_line, start_col, raw_text="-")

        if ch == '.':
            if self._peek() == '.':
                self._advance()
                return Token(TokenType.DOT_DOT, "..", start_line, start_col, raw_text="..")
            return Token(TokenType.DOT, ".", start_line, start_col, raw_text=".")

        # Single-character operators & delimiters
        single_char_map = {
            '+': (TokenType.PLUS, "+"),
            '*': (TokenType.STAR, "*"),
            '/': (TokenType.SLASH, "/"),
            '%': (TokenType.PERCENT, "%"),
            '(': (TokenType.LPAREN, "("),
            ')': (TokenType.RPAREN, ")"),
            '{': (TokenType.LBRACE, "{"),
            '}': (TokenType.RBRACE, "}"),
            '[': (TokenType.LBRACKET, "["),
            ']': (TokenType.RBRACKET, "]"),
            ',': (TokenType.COMMA, ","),
            ':': (TokenType.COLON, ":"),
            ';': (TokenType.SEMICOLON, ";"),
        }

        if ch in single_char_map:
            tt, text = single_char_map[ch]
            return Token(tt, text, start_line, start_col, raw_text=text)

        raise LexerError(f"Unexpected character: {ch!r}", start_line, start_col)
