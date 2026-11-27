#!/usr/bin/env python3
"""
WetLang Native Runtime Build System
Builds wetvm shared library (DLL on Windows, .so on Linux, .dylib on macOS).
Supports MSVC cl.exe, GCC, Clang, and setuptools fallback.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def get_project_root() -> Path:
    script_dir = Path(__file__).resolve().parent
    if (script_dir / "include").exists() and (script_dir / "src").exists():
        return script_dir.parent
    return Path.cwd()


def find_executable(name: str, extra_paths=None) -> str | None:
    found = shutil.which(name)
    if found:
        return found
    if extra_paths:
        for p in extra_paths:
            candidate = Path(p) / (name + (".exe" if sys.platform == "win32" else ""))
            if candidate.is_file() and os.access(candidate, os.X_OK):
                return str(candidate)
    return None


def generate_msvcrt_import_lib(dlltool_path: str, output_lib: Path, output_def: Path) -> bool:
    """Generates an import library for Windows msvcrt.dll using llvm-dlltool."""
    def_content = """LIBRARY msvcrt.dll
EXPORTS
malloc
free
calloc
realloc
memcpy
memset
memmove
memcmp
strlen
strncpy
strcpy
strcat
strcmp
strncmp
sprintf
_snprintf
_vsnprintf
vsnprintf
strchr
strtol
strtod
atoi
log10
log10f
_finite
_finitef
printf
puts
abort
qsort
"""
    output_def.write_text(def_content, encoding="utf-8")
    cmd = [
        dlltool_path,
        "-d", str(output_def),
        "-l", str(output_lib),
        "-m", "i386:x86-64"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode == 0 and output_lib.exists()


def generate_kernel32_import_lib(dlltool_path: str, output_lib: Path, output_def: Path) -> bool:
    """Generates an import library for Windows kernel32.dll using llvm-dlltool."""
    def_content = """LIBRARY kernel32.dll
EXPORTS
QueryPerformanceCounter
QueryPerformanceFrequency
CreateThread
WaitForSingleObject
CloseHandle
GetCurrentThread
GetCurrentProcess
SetThreadAffinityMask
SetPriorityClass
SetThreadPriority
Sleep
VirtualLock
VirtualUnlock
ExitProcess
CreateFileA
CreateNamedPipeA
ConnectNamedPipe
DisconnectNamedPipe
GetFileType
GetCommState
SetCommState
GetCommTimeouts
SetCommTimeouts
PurgeComm
ClearCommError
ReadFile
WriteFile
PeekNamedPipe
WaitNamedPipeA
FlushFileBuffers
GetLastError
"""
    output_def.write_text(def_content, encoding="utf-8")
    cmd = [
        dlltool_path,
        "-d", str(output_def),
        "-l", str(output_lib),
        "-m", "i386:x86-64"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode == 0 and output_lib.exists()


def generate_ws2_32_import_lib(dlltool_path: str, output_lib: Path, output_def: Path) -> bool:
    """Generates an import library for Windows ws2_32.dll using llvm-dlltool."""
    def_content = """LIBRARY ws2_32.dll
EXPORTS
WSAStartup
WSACleanup
WSAGetLastError
socket
closesocket
connect
send
recv
ioctlsocket
select
setsockopt
getsockopt
htons
ntohs
htonl
ntohl
inet_addr
inet_pton
getaddrinfo
freeaddrinfo
__WSAFDIsSet
"""
    output_def.write_text(def_content, encoding="utf-8")
    cmd = [
        dlltool_path,
        "-d", str(output_def),
        "-l", str(output_lib),
        "-m", "i386:x86-64"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode == 0 and output_lib.exists()


def build_with_clang(clang_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
    print(f"Building with Clang: {clang_path}")
    bin_dir = out_dll.parent
    bin_dir.mkdir(parents=True, exist_ok=True)

    # Check if we need standalone msvcrt / kernel32 / ws2_32 import libraries on Windows
    extra_link_args = []
    if sys.platform == "win32":
        # Look for llvm-dlltool next to clang
        clang_dir = Path(clang_path).parent
        dlltool_path = find_executable("llvm-dlltool", [clang_dir])
        msvcrt_lib = bin_dir / "msvcrt.lib"
        msvcrt_def = bin_dir / "msvcrt.def"
        kernel32_lib = bin_dir / "kernel32.lib"
        kernel32_def = bin_dir / "kernel32.def"
        ws2_32_lib = bin_dir / "ws2_32.lib"
        ws2_32_def = bin_dir / "ws2_32.def"

        if dlltool_path:
            if (
                not msvcrt_lib.exists()
                or msvcrt_lib.stat().st_size == 0
                or not msvcrt_def.exists()
                or "log10f" not in msvcrt_def.read_text(encoding="utf-8")
                or msvcrt_def.stat().st_mtime > msvcrt_lib.stat().st_mtime
            ):
                generate_msvcrt_import_lib(dlltool_path, msvcrt_lib, msvcrt_def)
            if (
                not kernel32_lib.exists()
                or kernel32_lib.stat().st_size == 0
                or not kernel32_def.exists()
                or "PeekNamedPipe" not in kernel32_def.read_text(encoding="utf-8")
                or "ExitProcess" not in kernel32_def.read_text(encoding="utf-8")
                or kernel32_def.stat().st_mtime > kernel32_lib.stat().st_mtime
            ):
                generate_kernel32_import_lib(dlltool_path, kernel32_lib, kernel32_def)
            if (
                not ws2_32_lib.exists()
                or ws2_32_lib.stat().st_size == 0
                or not ws2_32_def.exists()
                or "freeaddrinfo" not in ws2_32_def.read_text(encoding="utf-8")
                or ws2_32_def.stat().st_mtime > ws2_32_lib.stat().st_mtime
            ):
                generate_ws2_32_import_lib(dlltool_path, ws2_32_lib, ws2_32_def)

            if msvcrt_lib.exists() and kernel32_lib.exists() and ws2_32_lib.exists():
                extra_link_args = [
                    "-nostdlib",
                    "-Xlinker",
                    "/noentry",
                    str(msvcrt_lib),
                    str(kernel32_lib),
                    str(ws2_32_lib),
                ]
            elif msvcrt_lib.exists() and kernel32_lib.exists():
                extra_link_args = ["-nostdlib", "-Xlinker", "/noentry", str(msvcrt_lib), str(kernel32_lib)]
            elif msvcrt_lib.exists():
                extra_link_args = ["-nostdlib", "-Xlinker", "/noentry", str(msvcrt_lib)]

    cmd = [
        clang_path,
        "-O3",
        "-shared",
        "-DWET_BUILDING_DLL",
        *(["-mno-stack-arg-probe"] if sys.platform == "win32" else ["-fPIC"]),
        f"-I{include_dir}",
        "-o", str(out_dll),
        *[str(f) for f in src_files],
        *(extra_link_args if sys.platform == "win32" else ["-lm", "-lpthread"]),
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Clang build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
        return False
    return out_dll.exists()


def build_with_gcc(gcc_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
    print(f"Building with GCC: {gcc_path}")
    bin_dir = out_dll.parent
    bin_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        gcc_path,
        "-O3",
        "-shared",
        *(["-fPIC"] if sys.platform != "win32" else []),
        "-DWET_BUILDING_DLL",
        f"-I{include_dir}",
        "-o", str(out_dll),
        *[str(f) for f in src_files],
        *(["-lm", "-lpthread"] if sys.platform != "win32" else ["-lws2_32"]),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"GCC build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
        return False
    return out_dll.exists()


def build_with_msvc(cl_path: str, src_files: list[Path], include_dir: Path, out_dll: Path) -> bool:
    print(f"Building with MSVC: {cl_path}")
    bin_dir = out_dll.parent
    bin_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        cl_path,
        "/LD",
        "/DWET_BUILDING_DLL",
        f"/I{include_dir}",
        *[str(f) for f in src_files],
        f"/Fe:{out_dll}",
        "/link",
        "ws2_32.lib",
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"MSVC build failed:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}")
        return False
    return out_dll.exists()


def build_native_runtime() -> Path:
    proj_root = get_project_root()
    native_dir = proj_root / "native"
    include_dir = native_dir / "include"
    src_dir = native_dir / "src"
    bin_dir = native_dir / "bin"
    bin_dir.mkdir(parents=True, exist_ok=True)

    src_files = [
        src_dir / "wetvm_api.c",
        src_dir / "wetvm_vm.c",
        src_dir / "biophysics.c",
        src_dir / "interlocks.c",
        src_dir / "wet_hal.c",
        src_dir / "wet_hal_intan.c",
        src_dir / "wet_hal_maxwell.c",
        src_dir / "wet_hal_pump_valve.c",
        src_dir / "wet_hal_sensirion.c",
        src_dir / "wet_hal_transport.c",
        src_dir / "wet_scheduler.c",
        src_dir / "wet_aer.c",
        src_dir / "wet_distributed.c",
        src_dir / "wet_verification.c",
    ]
    for sf in src_files:
        if not sf.exists():
            raise FileNotFoundError(f"Source file not found: {sf}")

    ext = ".dll" if sys.platform == "win32" else (".dylib" if sys.platform == "darwin" else ".so")
    out_dll = bin_dir / f"wetvm{ext}"
    fallback_dll = native_dir / f"wetvm{ext}"

    # Search for compilers in order of preference
    # 1. MSVC cl.exe
    cl_exe = find_executable("cl")
    if cl_exe and build_with_msvc(cl_exe, src_files, include_dir, out_dll):
        shutil.copy2(out_dll, fallback_dll)
        print(f"Successfully compiled shared library: {out_dll}")
        return out_dll

    # 2. Clang
    extra_clang_paths = [
        r"C:\Program Files\LLVM\bin",
        r"C:\LLVM\bin",
        r"C:\msys64\mingw64\bin",
        r"C:\msys64\ucrt64\bin"
    ]
    clang_exe = find_executable("clang", extra_clang_paths)
    if clang_exe and build_with_clang(clang_exe, src_files, include_dir, out_dll):
        shutil.copy2(out_dll, fallback_dll)
        print(f"Successfully compiled shared library: {out_dll}")
        return out_dll

    # 3. GCC
    extra_gcc_paths = [
        r"C:\msys64\mingw64\bin",
        r"C:\msys64\ucrt64\bin",
        r"C:\mingw64\bin",
        r"C:\TDM-GCC-64\bin"
    ]
    gcc_exe = find_executable("gcc", extra_gcc_paths)
    if gcc_exe and build_with_gcc(gcc_exe, src_files, include_dir, out_dll):
        shutil.copy2(out_dll, fallback_dll)
        print(f"Successfully compiled shared library: {out_dll}")
        return out_dll

    raise RuntimeError("No suitable C compiler found (MSVC cl.exe, Clang, or GCC).")


if __name__ == "__main__":
    try:
        path = build_native_runtime()
        print(f"BUILD SUCCESS: {path}")
        sys.exit(0)
    except Exception as e:
        print(f"BUILD ERROR: {e}", file=sys.stderr)
        sys.exit(1)
