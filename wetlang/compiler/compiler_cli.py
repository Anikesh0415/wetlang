"""
WetLang Compiler CLI (wetc)
Command-line compiler and disassembler for WetLang (.wet -> .wbc).
"""

import sys
import argparse
import os
from typing import Optional

from compiler.lexer import Lexer, LexerError
from compiler.parser import Parser, ParseError
from compiler.semantic import SemanticAnalyzer, SemanticError
from compiler.emitter import BytecodeEmitter, disassemble, compile_source
from compiler.ast_nodes import ProgramNode, ASTNode




def format_ast(node: ASTNode, indent: int = 0) -> str:
    """Recursively formats AST nodes for debugging."""
    sp = "  " * indent
    lines = [f"{sp}{node.__class__.__name__}"]
    for k, v in node.__dict__.items():
        if k in ("line", "column"):
            continue
        if isinstance(v, ASTNode):
            lines.append(f"{sp}  {k}:")
            lines.append(format_ast(v, indent + 2))
        elif isinstance(v, list):
            lines.append(f"{sp}  {k}: [")
            for item in v:
                if isinstance(item, ASTNode):
                    lines.append(format_ast(item, indent + 2))
                else:
                    lines.append(f"{sp}    {item!r}")
            lines.append(f"{sp}  ]")
        else:
            lines.append(f"{sp}  {k}: {v!r}")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="wetc",
        description="WetLang Compiler & Disassembler for Neural Organoid Computing."
    )
    parser.add_argument("source", help="Input .wet source file path")
    parser.add_argument("-o", "--output", help="Output .wbc binary file path")
    parser.add_argument("--disasm", action="store_true", help="Print disassembly of compiled bytecode")
    parser.add_argument("--dump-ast", action="store_true", help="Dump Abstract Syntax Tree to stdout")

    args = parser.parse_args(argv)

    if not os.path.exists(args.source):
        print(f"Error: Source file '{args.source}' not found.", file=sys.stderr)
        return 1

    try:
        with open(args.source, "r", encoding="utf-8") as f:
            source_text = f.read()

        # Step 1 & 2: Tokenize and Parse
        lexer = Lexer(source_text)
        tokens = lexer.tokenize()
        parser_inst = Parser(tokens, source_text=source_text)
        ast = parser_inst.parse()

        if args.dump_ast:
            print(format_ast(ast))

        # Step 3: Semantic Analysis
        analyzer = SemanticAnalyzer(ast)
        analyzer.analyze()

        # Step 4: Emit Bytecode
        emitter = BytecodeEmitter()
        bytecode = emitter.compile(ast)

        if args.disasm:
            print(disassemble(bytecode))

        # Write output file
        out_path = args.output
        if not out_path:
            base, _ = os.path.splitext(args.source)
            out_path = base + ".wbc"

        with open(out_path, "wb") as f:
            f.write(bytecode)

        print(f"Successfully compiled '{args.source}' -> '{out_path}' ({len(bytecode)} bytes).")
        return 0

    except (LexerError, ParseError, SemanticError) as err:
        print(f"Compilation Failed: {err}", file=sys.stderr)
        return 2
    except Exception as ex:
        print(f"Unexpected Compiler Error: {ex}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
