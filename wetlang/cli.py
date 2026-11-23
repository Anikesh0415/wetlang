"""
WetLang Command-Line Interface (CLI)
====================================
Standard CLI for compiling, running, disassembling, and verifying WetLang programs.
Usage:
  wetlang compile <file.wet> [-o <file.wbc>] [--sign <secret_key>]
  wetlang run <file.wbc | file.wet> [--ticks N] [--dt MS] [--jsonl]
  wetlang disasm <file.wbc>
  wetlang verify <file.wbc> [--key <secret_key>]
  wetlang version
"""

import sys
import argparse
from pathlib import Path

from .compiler.lexer import Lexer
from .compiler.parser import Parser
from .compiler.semantic import SemanticAnalyzer
from .compiler.emitter import BytecodeEmitter, disassemble
from .compiler.crypto_signer import sign_bytecode, verify_bytecode_signature
from .runtime.runtime import WetRuntime, WetVMError


def cmd_compile(args) -> int:
    src_path = Path(args.source)
    if not src_path.is_file():
        print(f"Error: Source file '{args.source}' not found.", file=sys.stderr)
        return 1

    try:
        source_text = src_path.read_text(encoding="utf-8")
        tokens = Lexer(source_text).tokenize()
        ast = Parser(tokens).parse()
        SemanticAnalyzer(ast).analyze()
        wbc = BytecodeEmitter().compile(ast)

        if args.sign:
            key = args.sign.encode("utf-8")
            wbc = sign_bytecode(wbc, key)
            print(f"[Crypto] Authenticated WBC signed with HMAC-SHA256")

        out_path = Path(args.output) if args.output else src_path.with_suffix(".wbc")
        out_path.write_bytes(wbc)
        print(f"Successfully compiled '{src_path.name}' -> '{out_path.name}' ({len(wbc)} bytes)")
        return 0
    except Exception as ex:
        print(f"Compilation Error: {ex}", file=sys.stderr)
        return 1


def cmd_run(args) -> int:
    file_path = Path(args.file)
    if not file_path.is_file():
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
        return 1

    try:
        if file_path.suffix.lower() == ".wet":
            # Auto-compile source first
            source_text = file_path.read_text(encoding="utf-8")
            tokens = Lexer(source_text).tokenize()
            ast = Parser(tokens).parse()
            SemanticAnalyzer(ast).analyze()
            wbc = BytecodeEmitter().compile(ast)
        else:
            wbc = file_path.read_bytes()

        rt = WetRuntime()
        rt.load(wbc)
        print(f"Running '{file_path.name}' on WetVM (ticks={args.ticks}, dt={args.dt}ms)...")

        for tick in range(1, args.ticks + 1):
            telem = rt.step(1)
            if args.jsonl:
                print(f'{{"tick": {telem.current_tick}, "time_ms": {telem.sim_time_ms:.1f}, "pop_rate_hz": {telem.population_rate_hz:.2f}, "spikes": {int(telem.spike_raster.sum())}}}')
            elif tick % 10 == 0 or tick == args.ticks:
                print(f"Tick {telem.current_tick:4d} | Sim Time: {telem.sim_time_ms:6.1f} ms | Population Rate: {telem.population_rate_hz:5.1f} Hz | Active Spikes: {int(telem.spike_raster.sum())}")

        act = rt.get_actuator_telemetry()
        if any(act.pump_rates > 0) or any(act.valves > 0) or any(act.motors != 0):
            print("\nActuator Final Status:")
            for p in range(8):
                if act.pump_rates[p] > 0 or act.pump_dispensed[p] > 0:
                    print(f"  Pump {p}: Rate={act.pump_rates[p]:.2f} uL/min, Dispensed={act.pump_dispensed[p]:.2f} uL")
                if act.valves[p] > 0:
                    print(f"  Valve {p}: OPEN")
            for m in range(4):
                if act.motors[m] != 0:
                    print(f"  Motor {m}: Position={act.motors[m]} steps")

        rt.close()
        print("\nSimulation execution completed successfully.")
        return 0
    except WetVMError as ex:
        print(f"WetVM Runtime Trip: {ex}", file=sys.stderr)
        return 2
    except Exception as ex:
        print(f"Execution Error: {ex}", file=sys.stderr)
        return 1


def cmd_disasm(args) -> int:
    wbc_path = Path(args.file)
    if not wbc_path.is_file():
        print(f"Error: Binary '{args.file}' not found.", file=sys.stderr)
        return 1

    try:
        wbc = wbc_path.read_bytes()
        print(disassemble(wbc))
        return 0
    except Exception as ex:
        print(f"Disassembly Error: {ex}", file=sys.stderr)
        return 1


def cmd_verify(args) -> int:
    wbc_path = Path(args.file)
    if not wbc_path.is_file():
        print(f"Error: Binary '{args.file}' not found.", file=sys.stderr)
        return 1

    try:
        wbc = wbc_path.read_bytes()
        key = args.key.encode("utf-8") if args.key else b""
        ok, reason = verify_bytecode_signature(wbc, key)
        if ok:
            print(f"[PASS] Cryptographic verification passed: {reason}")
            return 0
        else:
            print(f"[FAIL] Cryptographic verification failed: {reason}", file=sys.stderr)
            return 1
    except Exception as ex:
        print(f"Verification Error: {ex}", file=sys.stderr)
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="wetlang",
        description="WetLang: Programming Language for Neural Organoid Computing & Microfluidics"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # compile
    p_comp = subparsers.add_parser("compile", help="Compile WetLang source (.wet) into WBC bytecode (.wbc)")
    p_comp.add_argument("source", help="Path to .wet source file")
    p_comp.add_argument("-o", "--output", help="Path to output .wbc binary")
    p_comp.add_argument("--sign", help="Optional secret key to cryptographically sign binary")

    # run
    p_run = subparsers.add_parser("run", help="Execute WBC binary or .wet source on native WetVM")
    p_run.add_argument("file", help="Path to .wbc binary or .wet source file")
    p_run.add_argument("--ticks", type=int, default=50, help="Number of ticks to execute (default: 50)")
    p_run.add_argument("--dt", type=float, default=0.1, help="Simulation timestep dt in ms (default: 0.1)")
    p_run.add_argument("--jsonl", action="store_true", help="Stream telemetry in JSONL format")

    # disasm
    p_dis = subparsers.add_parser("disasm", help="Disassemble WBC bytecode binary into human-readable assembly")
    p_dis.add_argument("file", help="Path to .wbc binary")

    # verify
    p_ver = subparsers.add_parser("verify", help="Verify cryptographic signature of WBC binary")
    p_ver.add_argument("file", help="Path to .wbc binary")
    p_ver.add_argument("--key", required=True, help="HMAC secret key")

    # version
    subparsers.add_parser("version", help="Print WetLang platform version")

    args = parser.parse_args()

    if args.command == "compile":
        return cmd_compile(args)
    elif args.command == "run":
        return cmd_run(args)
    elif args.command == "disasm":
        return cmd_disasm(args)
    elif args.command == "verify":
        return cmd_verify(args)
    elif args.command == "version":
        print("WetLang Platform v2.1.0 (Production Wetware Engine & Runtime)")
        print("Developed by Anikesh Tiwari (Surat, Gujarat, India) / Wetworld")
        return 0
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
