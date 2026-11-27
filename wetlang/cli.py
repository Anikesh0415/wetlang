"""
WetLang Command-Line Interface (CLI)
====================================
Standard CLI for compiling, running, disassembling, verifying, and checking WetLang programs.
Project Janus: Dual-Substrate Execution for Biological Wetware & Neuromorphic Silicon.

Usage:
  wetlang compile <file.wet> [-o <output>] [--target <sim|finalspark|spinnaker|embedded|loihi2>] [--sign <key>]
  wetlang run <file.wbc | file.wet> [--ticks N] [--dt MS] [--jsonl]
  wetlang disasm <file.wbc>
  wetlang verify <file.wbc> [--key <key>]
  wetlang version
"""

import sys
import argparse
import json
from pathlib import Path

# Ensure root repository directory is on sys.path
_root_dir = str(Path(__file__).resolve().parent.parent)
if _root_dir not in sys.path:
    sys.path.insert(0, _root_dir)

from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.semantic import SemanticAnalyzer, check_source, Diagnostic
from compiler.emitter import BytecodeEmitter, disassemble, compile_source, Target
from compiler.crypto_signer import sign_bytecode, verify_bytecode_signature
from bindings.runtime import WetRuntime, WetVMError


def cmd_compile(args) -> int:
    src_path = Path(args.source)
    if not src_path.is_file():
        print(f"Error: Source file '{args.source}' not found.", file=sys.stderr)
        return 1

    try:
        source_text = src_path.read_text(encoding="utf-8")
        target = getattr(args, "target", "sim")
        compiled = compile_source(source_text, filename=str(src_path), target=target)

        if target in ("loihi2", "spinnaker", "cl_sdk", "neuroplatform"):
            if getattr(args, "sign", None):
                print("Error: --sign is only supported for binary WBC targets, not Python scripts.", file=sys.stderr)
                return 1
            out_path = Path(args.output) if args.output else src_path.with_suffix(".py")
            out_path.write_text(compiled, encoding="utf-8")
            labels = {
                "loihi2": "Intel Lava script",
                "spinnaker": "SpiNNaker PyNN script",
                "cl_sdk": "Cortical Labs cl-sdk script",
                "neuroplatform": "FinalSpark Neuroplatform protocol script",
            }
            label = labels.get(target, "Python script")
            print(f"Successfully compiled '{src_path.name}' -> '{out_path.name}' ({label}, target={target})")
            return 0
        elif target == "embedded":
            from compiler.emitter import emit_c_embedded_header
            if getattr(args, "sign", None):
                compiled = sign_bytecode(compiled, args.sign.encode("utf-8"))
                print(f"[Crypto] Authenticated WBC signed with HMAC-SHA256")
            header = emit_c_embedded_header(compiled, model_name=src_path.stem, target=target)
            out_path = Path(args.output) if args.output else src_path.with_suffix(".h")
            out_path.write_text(header, encoding="utf-8")
            print(f"Successfully compiled '{src_path.name}' -> '{out_path.name}' (C header, target={target}, {len(compiled)} bytes bytecode)")
            return 0
        else:
            if getattr(args, "sign", None):
                key = args.sign.encode("utf-8")
                compiled = sign_bytecode(compiled, key)
                print(f"[Crypto] Authenticated WBC signed with HMAC-SHA256")

            out_path = Path(args.output) if args.output else src_path.with_suffix(".wbc")
            out_path.write_bytes(compiled)
            print(f"Successfully compiled '{src_path.name}' -> '{out_path.name}' ({len(compiled)} bytes, target={target})")
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
            source_text = file_path.read_text(encoding="utf-8")
            wbc = compile_source(source_text, target="sim")
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



def cmd_check(args) -> int:
    use_stdin = bool(getattr(args, "stdin", False)) or (args.file == "-")
    display_file = getattr(args, "filename", None) or args.file or "<stdin>"
    fmt = getattr(args, "format", "text")

    if not use_stdin:
        if not args.file:
            if fmt == "json":
                err = [{
                    "file": display_file,
                    "line": 1,
                    "column": 1,
                    "severity": "error",
                    "code": "ERR_FILE_NOT_FOUND",
                    "message": "No source file or --stdin specified."
                }]
                print(json.dumps(err, indent=2))
            else:
                print("Error: No source file or --stdin specified.", file=sys.stderr)
            return 1

        src_path = Path(args.file)
        if not src_path.is_file():
            if fmt == "json":
                err = [{
                    "file": display_file,
                    "line": 1,
                    "column": 1,
                    "severity": "error",
                    "code": "ERR_FILE_NOT_FOUND",
                    "message": f"Source file '{args.file}' not found."
                }]
                print(json.dumps(err, indent=2))
            else:
                print(f"Error: Source file '{args.file}' not found.", file=sys.stderr)
            return 1

    try:
        if use_stdin:
            if hasattr(sys.stdin, "buffer"):
                source_text = sys.stdin.buffer.read().decode("utf-8-sig")
            else:
                source_text = sys.stdin.read()
                if source_text.startswith("\ufeff"):
                    source_text = source_text[1:]
        else:
            source_text = Path(args.file).read_text(encoding="utf-8-sig")

        max_ticks = getattr(args, "max_unsynced_ticks", 1000) or 1000
        diagnostics = check_source(source_text, filename=str(display_file), max_unsynced_ticks=max_ticks)

        if fmt == "json":
            diag_dicts = [d.to_dict() for d in diagnostics]
            print(json.dumps(diag_dicts, indent=2))
        else:
            if not diagnostics:
                print(f"[PASS] No diagnostics found in '{Path(str(display_file)).name}'.")
            else:
                for d in diagnostics:
                    print(f"{d.file}:{d.line}:{d.column}: {d.severity.upper()}: [{d.code}] {d.message}")

        has_errors = any(d.severity == "error" for d in diagnostics)
        return 1 if has_errors else 0
    except Exception as ex:
        if fmt == "json":
            err = [{
                "file": str(display_file),
                "line": 1,
                "column": 1,
                "severity": "error",
                "code": "ERR_INTERNAL",
                "message": str(ex)
            }]
            print(json.dumps(err, indent=2))
        else:
            print(f"Linter Error: {ex}", file=sys.stderr)
        return 1


def cmd_nwb(args) -> int:
    try:
        from wetlang.nwb import read_nwb_recording, iter_nwb_chunks, export_to_nwb
    except ImportError as e:
        print(f"NWB Error: {e}", file=sys.stderr)
        return 1

    if getattr(args, "nwb_cmd", None) == "inspect":
        file_path = Path(args.file)
        if not file_path.is_file():
            print(f"Error: NWB file '{args.file}' not found.", file=sys.stderr)
            return 1
        try:
            series_name = getattr(args, "series", None)
            rec = read_nwb_recording(str(file_path), series_name=series_name)
            data = rec["data"]
            ts = rec["timestamps"]
            sr = rec.get("sample_rate")
            sr_str = f"{sr:.1f} Hz" if sr else "N/A"
            t_min = float(ts[0]) if len(ts) > 0 else 0.0
            t_max = float(ts[-1]) if len(ts) > 0 else 0.0
            duration_s = t_max - t_min
            print(f"--- NWB Recording Info: {file_path.name} ---")
            print(f"  Series Name    : {rec['series_name']}")
            print(f"  Sample Rate    : {sr_str}")
            print(f"  Data Shape     : {data.shape} ({data.dtype})")
            print(f"  Channels       : {data.shape[1] if data.ndim > 1 else 1}")
            print(f"  Total Samples  : {data.shape[0]}")
            print(f"  Duration       : {duration_s:.3f} s (timestamps: [{t_min:.3f}, {t_max:.3f}])")
            if rec.get("electrodes"):
                print(f"  Electrodes Meta: {list(rec['electrodes'].keys())}")
            if rec.get("units"):
                print(f"  Units Table    : {list(rec['units'].keys())}")
            return 0
        except Exception as ex:
            print(f"NWB Inspect Error: {ex}", file=sys.stderr)
            return 1

    elif getattr(args, "nwb_cmd", None) == "replay":
        file_path = Path(args.file)
        if not file_path.is_file():
            print(f"Error: NWB file '{args.file}' not found.", file=sys.stderr)
            return 1
        try:
            chunk_size = getattr(args, "chunk_size", 1024) or 1024
            max_seconds = getattr(args, "max_seconds", None)
            series_name = getattr(args, "series", None)
            total_samples = 0
            total_chunks = 0
            collected_chunks = []
            collected_ts = []

            for chunk, ts in iter_nwb_chunks(str(file_path), chunk_size=chunk_size, series_name=series_name):
                total_samples += len(chunk)
                total_chunks += 1
                if getattr(args, "export_nwb", None):
                    collected_chunks.append(chunk)
                    collected_ts.append(ts)
                if max_seconds is not None and len(ts) > 0 and (ts[-1] - ts[0]) >= max_seconds:
                    break

            print(f"Replay complete: {total_chunks} chunks ({total_samples} samples) processed.")
            if getattr(args, "export_nwb", None):
                import numpy as np
                all_data = np.concatenate(collected_chunks, axis=0) if collected_chunks else np.empty((0, 1))
                all_ts = np.concatenate(collected_ts, axis=0) if collected_ts else np.empty(0)
                export_to_nwb(
                    args.export_nwb,
                    {"voltages": all_data, "timestamps": all_ts},
                    session_description=f"Replay export of {file_path.name}"
                )
                print(f"Exported replay data to '{args.export_nwb}'.")
            return 0
        except Exception as ex:
            print(f"NWB Replay Error: {ex}", file=sys.stderr)
            return 1

    else:
        print("Usage: wetlang nwb [inspect|replay] <file.nwb>", file=sys.stderr)
        return 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="wetlang",
        description="WetLang: Programming Language for Neural Organoid Computing & Microfluidics"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # compile
    p_comp = subparsers.add_parser("compile", help="Compile WetLang source (.wet) for a target substrate (.wbc, .py, or .h)")
    p_comp.add_argument("source", help="Path to .wet source file")
    p_comp.add_argument("-o", "--output", help="Path to output file (.wbc, .py, or .h)")
    p_comp.add_argument("--target", choices=["sim", "finalspark", "spinnaker", "embedded", "loihi2", "cl_sdk", "neuroplatform"], default="sim", help="Target architecture (default: sim)")
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

    # check
    p_check = subparsers.add_parser("check", help="Run static linter and safety verification on .wet source")
    p_check.add_argument("file", nargs="?", default=None, help="Path to .wet source file (or '-' for stdin)")
    p_check.add_argument("--stdin", action="store_true", help="Read .wet source from standard input")
    p_check.add_argument("--filename", default=None, help="Display filename for diagnostics when using --stdin")
    p_check.add_argument("--format", choices=["text", "json"], default="text", help="Output format (default: text)")
    p_check.add_argument("--max-unsynced-ticks", type=int, default=1000, help="Maximum allowed ticks in loop without sync_tick (default: 1000)")

    # version
    subparsers.add_parser("version", help="Print WetLang platform version")

    # nwb
    p_nwb = subparsers.add_parser("nwb", help="Neurodata Without Borders (NWB) utilities")
    nwb_subs = p_nwb.add_subparsers(dest="nwb_cmd", help="NWB subcommands")

    p_nwb_insp = nwb_subs.add_parser("inspect", help="Inspect an NWB file metadata, series, and channels")
    p_nwb_insp.add_argument("file", help="Path to .nwb file")
    p_nwb_insp.add_argument("--series", default=None, help="Optional ElectricalSeries / TimeSeries name")

    p_nwb_rep = nwb_subs.add_parser("replay", help="Stream / replay an NWB file in chunks")
    p_nwb_rep.add_argument("file", help="Path to .nwb file")
    p_nwb_rep.add_argument("--series", default=None, help="Optional ElectricalSeries / TimeSeries name")
    p_nwb_rep.add_argument("--chunk-size", type=int, default=1024, help="Samples per chunk (default: 1024)")
    p_nwb_rep.add_argument("--max-seconds", type=float, default=None, help="Stop replay after N seconds")
    p_nwb_rep.add_argument("--export-nwb", default=None, help="Export replayed data to an output .nwb file")

    args = parser.parse_args(argv)

    if args.command == "compile":
        return cmd_compile(args)
    elif args.command == "run":
        return cmd_run(args)
    elif args.command == "disasm":
        return cmd_disasm(args)
    elif args.command == "verify":
        return cmd_verify(args)
    elif args.command == "check":
        return cmd_check(args)
    elif args.command == "nwb":
        return cmd_nwb(args)
    elif args.command == "version":
        print("WetLang Platform v2.2.0 (Production Wetware Engine & Project Janus)")
        print("Developed by Anikesh Tiwari (Surat, Gujarat, India) / Wetworld")
        return 0
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
