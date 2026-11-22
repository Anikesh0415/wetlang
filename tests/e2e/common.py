"""
WetLang E2E Test Suite Common Infrastructure & Utilities
Provides:
  - Feature availability probes (HAS_COMPILER, HAS_NATIVE_VM, HAS_BIOPHYSICS, etc.)
  - Conditional test skip decorators (@require_feature, @require_compiler, etc.)
  - Synthetic test data and code generators (valid WetLang programs, WBC headers, MEA coordinates)
  - Domain assertion utilities (voltage clamp, sliding charge balance, epileptiform trip, SI values)
  - Base test case class WetLangE2ETestCase with isolated temp directories and helpers
"""

import os
import sys
import math
import time
import struct
import shutil
import tempfile
import zlib
import unittest
from typing import Dict, List, Optional, Tuple, Union, Any

# Ensure project root is on sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

try:
    import numpy as np
except ImportError:
    np = None  # Handled gracefully if numpy is missing


# =============================================================================
# 1. Feature Availability Probes
# =============================================================================

def probe_compiler() -> bool:
    """Check if the WetLang compiler pipeline modules can be imported and initialized."""
    try:
        import compiler.token
        import compiler.lexer
        import compiler.ast_nodes
        import compiler.parser
        import compiler.semantic
        import compiler.isa
        import compiler.emitter
        return True
    except Exception:
        return False


def probe_native_vm() -> bool:
    """Check if the native C-ABI shared library and Python FFI bindings are available."""
    try:
        import bindings.ffi
        return True
    except Exception:
        return False


def probe_biophysics() -> bool:
    """Check if the biophysical digital twin sandbox modules are available."""
    try:
        import biophysics.mea_grid
        import biophysics.telemetry
        return True
    except Exception:
        return False


def probe_interlocks() -> bool:
    """Check if biocybersecurity interlock watchdog logic is available."""
    if probe_native_vm():
        return True
    interlocks_h = os.path.join(PROJECT_ROOT, "native", "include", "interlocks.h")
    return os.path.isfile(interlocks_h)


def probe_benchmarks() -> bool:
    """Check if all three standard benchmark programs exist in benchmarks/."""
    bm_dir = os.path.join(PROJECT_ROOT, "benchmarks")
    if not os.path.isdir(bm_dir):
        return False
    required_benchmarks = [
        "01_active_inference_closed_loop.wet",
        "02_polychronous_reservoir_classifier.wet",
        "03_homeostatic_stabilization_and_stress.wet",
    ]
    return all(os.path.isfile(os.path.join(bm_dir, f)) for f in required_benchmarks)


# Global feature availability flags
HAS_COMPILER: bool = probe_compiler()
HAS_NATIVE_VM: bool = probe_native_vm()
HAS_BIOPHYSICS: bool = probe_biophysics()
HAS_INTERLOCKS: bool = probe_interlocks()
HAS_BENCHMARKS: bool = probe_benchmarks()


# =============================================================================
# 2. Skip Decorators
# =============================================================================

def require_feature(feature_name: str):
    """
    Decorator to conditionally skip a test if a required system component is unavailable.
    Supports feature names:
      'compiler', 'native_vm', 'biophysics', 'interlocks', 'benchmarks',
      or individual feature IDs ('F1'..'F28').
    """
    feat_lower = feature_name.lower().strip()
    available = True
    reason = f"Feature '{feature_name}' not yet available"

    if feat_lower in ("compiler", "m1") or feat_lower in (f"f{i}" for i in range(1, 8)):
        available = HAS_COMPILER
        reason = "Compiler pipeline (M1) not yet available"
    elif feat_lower in ("native_vm", "vm", "m2", "ffi") or feat_lower in (f"f{i}" for i in range(8, 12)):
        available = HAS_NATIVE_VM
        reason = "Native VM engine / ctypes FFI (M2) not yet available"
    elif feat_lower in ("biophysics", "sandbox", "m3") or feat_lower in (f"f{i}" for i in range(12, 18)):
        available = HAS_BIOPHYSICS
        reason = "Biophysical digital twin sandbox (M3) not yet available"
    elif feat_lower in ("interlocks", "security", "m4") or feat_lower in (f"f{i}" for i in range(18, 23)):
        available = HAS_INTERLOCKS
        reason = "Biocybersecurity hardware interlocks (M4) not yet available"
    elif feat_lower in ("benchmarks", "m5") or feat_lower in (f"f{i}" for i in range(23, 29)):
        available = HAS_BENCHMARKS
        reason = "Benchmark programs (M5) not yet available"

    return unittest.skipUnless(available, reason)


skip_if_unavailable = require_feature

# Convenience shortcuts
require_compiler = unittest.skipUnless(HAS_COMPILER, "Compiler pipeline (M1) not yet available")
require_native_vm = unittest.skipUnless(HAS_NATIVE_VM, "Native VM / ctypes FFI (M2) not yet available")
require_biophysics = unittest.skipUnless(HAS_BIOPHYSICS, "Biophysical digital twin sandbox (M3) not yet available")
require_interlocks = unittest.skipUnless(HAS_INTERLOCKS, "Hardware interlocks (M4) not yet available")
require_benchmarks = unittest.skipUnless(HAS_BENCHMARKS, "Benchmark programs (M5) not yet available")


# =============================================================================
# 3. Synthetic Test Generators
# =============================================================================

def make_minimal_wet_program(
    channel_id: int = 0,
    voltage_str: str = "0.8V",
    p1_str: str = "200us",
    p2_str: str = "200us",
) -> str:
    """Generate a minimal syntactically valid WetLang program with grid, channel, stimulation, and sync_tick."""
    row = channel_id // 8
    col = channel_id % 8
    return f"""grid mea {{
    rows: 8;
    cols: 8;
    pitch: 200um;
}}
channel ch0 = mea[{row}, {col}] mode: BiphasicStim;

fn main() -> int {{
    stim_biphasic(ch0, {voltage_str}, {p1_str}, {p2_str});
    sync_tick();
    return 0;
}}
"""


def generate_valid_wet_source(
    num_channels: int = 1,
    with_loop: bool = True,
    loop_count: int = 10,
    stim_voltage: str = "0.5V",
    stim_duration: str = "100us",
) -> str:
    """Generate a valid WetLang program with configurable channels and optional synchronized loop."""
    channels_decl = []
    stims = []
    for i in range(min(num_channels, 64)):
        r, c = i // 8, i % 8
        channels_decl.append(f"channel ch{i} = mea[{r}, {c}] mode: BiphasicStim;")
        stims.append(f"        stim_biphasic(ch{i}, {stim_voltage}, {stim_duration}, {stim_duration});")

    decl_str = "\n".join(channels_decl)
    stim_str = "\n".join(stims)

    if with_loop:
        body = f"""    let count: int = 0;
    while (count < {loop_count}) {{
{stim_str}
        sync_tick();
        count = count + 1;
    }}"""
    else:
        body = f"""{stim_str}
    sync_tick();"""

    return f"""grid mea {{
    rows: 8;
    cols: 8;
    pitch: 200um;
}}
{decl_str}

fn main() -> int {{
{body}
    return 0;
}}
"""


def make_unyielded_loop_code() -> str:
    """Generate adversarial WetLang code with an infinite stimulation loop lacking sync_tick."""
    return """grid mea {
    rows: 8;
    cols: 8;
    pitch: 200um;
}
channel ch0 = mea[0, 0] mode: BiphasicStim;

fn main() -> int {
    while (true) {
        stim_biphasic(ch0, 0.5V, 100us, 100us);
        // Violation: No sync_tick() inside cyclic stimulation loop
    }
    return 0;
}
"""


def make_overvoltage_code(voltage_v: float = 2.5) -> str:
    """Generate adversarial WetLang code requesting stimulus voltage exceeding +/- 1.2V water window."""
    return f"""grid mea {{
    rows: 8;
    cols: 8;
    pitch: 200um;
}}
channel ch0 = mea[0, 0] mode: BiphasicStim;

fn main() -> int {{
    stim_biphasic(ch0, {voltage_v}V, 200us, 200us);
    sync_tick();
    return 0;
}}
"""


def make_oob_coordinate_code(row: int = 8, col: int = 0) -> str:
    """Generate adversarial WetLang code with out-of-bounds MEA coordinates."""
    return f"""grid mea {{
    rows: 8;
    cols: 8;
    pitch: 200um;
}}
channel bad_ch = mea[{row}, {col}] mode: BiphasicStim;

fn main() -> int {{
    sync_tick();
    return 0;
}}
"""


def make_syntax_error_code() -> str:
    """Generate code with intentional syntax errors."""
    return """grid mea {
    rows = 8  // Missing colon, missing semicolon
}
fn main( -> {  // Malformed signature
"""


def make_wbc_header(
    magic: bytes = b"WETB",
    major: int = 1,
    minor: int = 0,
    caps: int = 0x0001,
    file_size: int = 32,
    checksum_crc32: Optional[int] = None,
    num_sections: int = 0,
    channel_count: int = 64,
    max_charge_nc: float = 0.5,
    reserved: int = 0,
    *,
    channels: Optional[int] = None,
    max_charge: Optional[float] = None,
) -> bytes:
    """
    Generate a 32-byte WBC binary header with Little-Endian fields and CRC32.
    Header layout (exactly 32 bytes):
      00-03: magic (4s)
      04:    version_major (uint8)
      05:    version_minor (uint8)
      06-07: capabilities (uint16)
      08-11: file_size (uint32)
      12-15: checksum_crc32 (uint32)
      16-19: num_sections (uint32)
      20-23: channel_count (uint32)
      24-27: max_charge_nc (float32)
      28-31: reserved (uint32)
    """
    if channels is not None:
        channel_count = channels
    if max_charge is not None:
        max_charge_nc = max_charge

    # Determine candidate formats to try, prioritizing compiler.isa.HEADER_STRUCT_FORMAT
    format_candidates: List[str] = []
    try:
        from compiler.isa import HEADER_STRUCT_FORMAT
        format_candidates.append(HEADER_STRUCT_FORMAT)
    except Exception:
        pass
    for fmt in ("<4sBBHIIIIfI", "<4sHHHIIIIfH"):
        if fmt not in format_candidates:
            format_candidates.append(fmt)

    # Truncate or pad magic to 4 bytes
    if len(magic) < 4:
        magic = magic.ljust(4, b"\x00")
    elif len(magic) > 4:
        magic = magic[:4]

    for format_str in format_candidates:
        assert struct.calcsize(format_str) == 32, "Header struct format must be exactly 32 bytes"
        try:
            if checksum_crc32 is None:
                # Compute CRC32 with checksum field set to 0
                header_zero_crc = struct.pack(
                    format_str,
                    magic, major, minor, caps, file_size, 0, num_sections, channel_count, max_charge_nc, reserved
                )
                computed_crc = zlib.crc32(header_zero_crc) & 0xFFFFFFFF
            else:
                computed_crc = checksum_crc32

            return struct.pack(
                format_str,
                magic, major, minor, caps, file_size, computed_crc, num_sections, channel_count, max_charge_nc, reserved
            )
        except struct.error:
            continue

    # Final fallback if all candidates failed struct.pack
    format_str = format_candidates[0]
    if checksum_crc32 is None:
        header_zero_crc = struct.pack(
            format_str,
            magic, major, minor, caps, file_size, 0, num_sections, channel_count, max_charge_nc, reserved
        )
        checksum_crc32 = zlib.crc32(header_zero_crc) & 0xFFFFFFFF
    return struct.pack(
        format_str,
        magic, major, minor, caps, file_size, checksum_crc32, num_sections, channel_count, max_charge_nc, reserved
    )


def generate_mea_coordinates(valid: bool = True, count: int = 64) -> List[Tuple[int, int]]:
    """
    Generate MEA electrode coordinates.
    If valid=True: yields (row, col) within 8x8 grid: 0 <= row < 8 and 0 <= col < 8.
    If valid=False: includes out-of-bounds coordinates (e.g. (-1, 0), (8, 0), (10, 10)).
    """
    if valid:
        coords = [(r, c) for r in range(8) for c in range(8)]
        return coords[:count]
    else:
        invalid_coords = [(-1, 0), (0, -1), (8, 0), (0, 8), (8, 8), (10, 15), (-5, -5), (100, 200)]
        return invalid_coords[:count]


def make_biphasic_stim_trace(
    amp_v: float = 0.8,
    p1_ms: float = 0.2,
    p2_ms: float = 0.2,
    total_ticks: int = 100,
    dt_ms: float = 0.1,
) -> Any:
    """Generate a time series of stimulation voltages for a single biphasic pulse."""
    p1_ticks = int(round(p1_ms / dt_ms))
    p2_ticks = int(round(p2_ms / dt_ms))

    if np is not None:
        trace = np.zeros(total_ticks, dtype=np.float64)
        trace[:p1_ticks] = amp_v
        trace[p1_ticks:p1_ticks + p2_ticks] = -amp_v
        return trace
    else:
        trace = [0.0] * total_ticks
        for t in range(min(p1_ticks, total_ticks)):
            trace[t] = amp_v
        for t in range(p1_ticks, min(p1_ticks + p2_ticks, total_ticks)):
            trace[t] = -amp_v
        return trace


def make_spike_raster_matrix(
    ticks: int = 500,
    channels: int = 64,
    firing_channels: int = 25,
    rate_hz: float = 200.0,
    dt_ms: float = 0.1,
    seed: int = 42,
) -> Any:
    """
    Generate synthetic spike raster matrix of shape (ticks, channels).
    Used for verifying epileptiform runaway breaker logic.
    """
    spike_prob_per_tick = rate_hz * (dt_ms / 1000.0)

    if np is not None:
        rng = np.random.default_rng(seed)
        raster = np.zeros((ticks, channels), dtype=np.uint8)
        active_ch = rng.choice(channels, size=min(firing_channels, channels), replace=False)
        for ch in active_ch:
            spikes = (rng.random(ticks) < spike_prob_per_tick).astype(np.uint8)
            raster[:, ch] = spikes
        return raster
    else:
        import random
        rnd = random.Random(seed)
        raster = [[0] * channels for _ in range(ticks)]
        active_channels = list(range(min(firing_channels, channels)))
        for t in range(ticks):
            for ch in active_channels:
                if rnd.random() < spike_prob_per_tick:
                    raster[t][ch] = 1
        return raster


# =============================================================================
# 4. Domain Assertion Utilities
# =============================================================================

def assert_si_value_close(
    actual: float,
    expected: float,
    tol: float = 1e-6,
    msg: str = "",
) -> None:
    """Assert that a physical unit scaled value matches the expected SI value within tolerance."""
    diff = abs(actual - expected)
    if diff > tol:
        error_msg = f"SI value mismatch: actual={actual}, expected={expected}, |diff|={diff} > tol={tol}"
        if msg:
            error_msg += f" ({msg})"
        raise AssertionError(error_msg)


def assert_voltage_clamped(
    *args,
    min_v: Optional[float] = None,
    max_v: Optional[float] = None,
    clamp_limit: Optional[float] = None,
    requested_v: Optional[float] = None,
    actual_v: Optional[float] = None,
    msg: str = "",
) -> None:
    """
    Verify water-window voltage clamp compliance.
    Supports both forms:
      1. Boundary check: assert_voltage_clamped(v, min_v=-1.2, max_v=1.2)
         Asserts that every element in v (or scalar v) is within [min_v, max_v].
      2. Transfer function check: assert_voltage_clamped(requested_v, actual_v, clamp_limit=1.2)
         Asserts that actual_v == clamp(requested_v, -clamp_limit, clamp_limit).
    """
    # Explicit transfer check via keyword arguments
    if requested_v is not None or actual_v is not None or clamp_limit is not None:
        limit = float(clamp_limit if clamp_limit is not None else (1.2 if max_v is None else max_v))
        req = float(requested_v if requested_v is not None else args[0])
        act = float(actual_v if actual_v is not None else (args[1] if len(args) > 1 else min_v))
        expected = max(-limit, min(limit, req))
        if abs(act - expected) > 1e-5:
            error_msg = f"Voltage clamp failure: requested={req}V, expected clamped={expected}V, got={act}V"
            if msg:
                error_msg += f" ({msg})"
            raise AssertionError(error_msg)
        return

    # If called with 3 positional arguments: (requested, actual, clamp_limit)
    if len(args) == 3 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float)):
        req = float(args[0])
        act = float(args[1])
        limit = float(args[2])
        expected = max(-limit, min(limit, req))
        if abs(act - expected) <= 1e-5:
            return  # Transfer function match
        else:
            raise AssertionError(f"Voltage clamp failure: requested={req}V, expected clamped={expected}V, got={act}V. {msg}")

    # Otherwise, boundary check:
    v = args[0] if len(args) >= 1 else requested_v
    low = min_v if min_v is not None else (args[1] if len(args) >= 2 else -1.2)
    high = max_v if max_v is not None else (args[2] if len(args) >= 3 else 1.2)

    if np is not None and isinstance(v, np.ndarray):
        if np.any(v < low) or np.any(v > high):
            violating_min = float(np.min(v))
            violating_max = float(np.max(v))
            raise AssertionError(
                f"Voltage out of water-window clamp range [{low}V, {high}V]: "
                f"min={violating_min}V, max={violating_max}V. {msg}"
            )
    elif isinstance(v, (list, tuple)):
        for idx, val in enumerate(v):
            if val < low or val > high:
                raise AssertionError(
                    f"Voltage element at index {idx} ({val}V) exceeds clamp range [{low}V, {high}V]. {msg}"
                )
    else:
        val = float(v)
        if val < low or val > high:
            raise AssertionError(f"Voltage {val}V exceeds clamp range [{low}V, {high}V]. {msg}")


class ChargeBalanceResult(tuple):
    """Named tuple-like result for sliding charge balance checks."""
    def __new__(cls, is_balanced: bool, trip_tick: int, max_residual_nc: float):
        return super().__new__(cls, (is_balanced, trip_tick, max_residual_nc))

    @property
    def is_balanced(self) -> bool:
        return self[0]

    @property
    def balanced(self) -> bool:
        return self[0]

    @property
    def trip_tick(self) -> int:
        return self[1]

    @property
    def tick(self) -> int:
        return self[1]

    @property
    def max_residual_nc(self) -> float:
        return self[2]

    @property
    def max_residual(self) -> float:
        return self[2]


def assert_sliding_charge_balance(
    charges: Any,
    max_charge_nc: float = 0.5,
    window_ticks: int = 100,
    *,
    limit_nc: Optional[float] = None,
    expect_balanced: Optional[bool] = None,
    msg: str = "",
) -> ChargeBalanceResult:
    """
    Simulate a 10.0 ms (100-tick at dt=0.1ms) sliding ring buffer charge balance watchdog.
    Calculates running net charge across the sliding window.
    Trips if |running_charge| >= max_charge_nc.

    Returns: ChargeBalanceResult(is_balanced, trip_tick, max_residual_nc)
    If expect_balanced is True, asserts that no trip occurred.
    If expect_balanced is False, asserts that a trip DID occur.
    """
    if limit_nc is not None:
        max_charge_nc = limit_nc

    # Handle parameter order (charges, window_ticks, limit_nc)
    if isinstance(max_charge_nc, int) and max_charge_nc > 10:
        window_ticks = max_charge_nc
        max_charge_nc = limit_nc if limit_nc is not None else 0.5

    charge_list = list(charges) if not hasattr(charges, "__len__") else charges
    ring = [0.0] * window_ticks
    running_sum = 0.0
    max_residual = 0.0
    trip_tick = -1
    is_balanced = True

    for tick, q in enumerate(charge_list):
        idx = tick % window_ticks
        running_sum += float(q) - ring[idx]
        ring[idx] = float(q)
        current_abs = abs(running_sum)
        if current_abs > max_residual:
            max_residual = current_abs

        if tick >= window_ticks and current_abs >= max_charge_nc:
            if is_balanced:
                is_balanced = False
                trip_tick = tick
                if expect_balanced is True:
                    raise AssertionError(
                        f"Charge balance tripped at tick {tick}: residual={running_sum:.4f}nC >= limit={max_charge_nc}nC. {msg}"
                    )

    if expect_balanced is False and is_balanced:
        raise AssertionError(
            f"Expected charge balance trip, but none occurred. Max residual charge: {max_residual:.4f}nC < limit={max_charge_nc}nC. {msg}"
        )

    return ChargeBalanceResult(is_balanced, trip_tick, max_residual)


class EpileptiformResult(tuple):
    """Named tuple-like result for epileptiform trip checks."""
    def __new__(cls, tripped: bool, trip_tick: int):
        return super().__new__(cls, (tripped, trip_tick))

    @property
    def tripped(self) -> bool:
        return self[0]

    @property
    def is_tripped(self) -> bool:
        return self[0]

    @property
    def trip_tick(self) -> int:
        return self[1]

    @property
    def tick(self) -> int:
        return self[1]


def assert_epileptiform_trip(
    firing_rates_or_raster: Any,
    channels: int = 64,
    duration_ms: float = 50.0,
    *,
    dt_ms: float = 0.1,
    threshold_hz: float = 150.0,
    channel_ratio: float = 0.35,
    window_ticks: Optional[int] = None,
    sustained_ticks_required: Optional[int] = None,
    expect_trip: Optional[bool] = None,
    msg: str = "",
) -> EpileptiformResult:
    """
    Simulate the 50.0 ms (500 ticks at dt=0.1ms) epileptiform runaway breaker.
    Breaker trips if population firing rate > 150 Hz across > 35% of electrodes (>= 23 of 64)
    sustained for 50.0 ms.

    Accepts:
      - 2D spike raster matrix of shape (num_ticks, num_channels) with binary 0/1 entries
      - 2D firing rate array (ticks, channels) in Hz

    Returns: EpileptiformResult(tripped: bool, trip_tick: int)
    """
    if window_ticks is None:
        window_ticks = int(round(duration_ms / dt_ms))

    if sustained_ticks_required is None:
        sustained_ticks_required = window_ticks

    required_hyper_channels = int(math.ceil(channels * channel_ratio))
    if required_hyper_channels <= channels * channel_ratio:
        required_hyper_channels += 1  # Strictly greater than 35% (e.g. >22.4 -> 23)

    spikes_per_window_threshold = (threshold_hz * (window_ticks * dt_ms)) / 1000.0

    if np is not None and isinstance(firing_rates_or_raster, np.ndarray):
        arr = firing_rates_or_raster
        num_ticks, num_ch = arr.shape
        is_binary = np.all((arr == 0) | (arr == 1))

        sustained_ticks = 0
        tripped = False
        trip_tick = -1

        for t in range(window_ticks, num_ticks):
            window = arr[t - window_ticks:t, :]
            if is_binary:
                spike_counts = np.sum(window, axis=0)
                hyper_count = np.sum(spike_counts >= spikes_per_window_threshold)
            else:
                mean_rates = np.mean(window, axis=0)
                hyper_count = np.sum(mean_rates >= threshold_hz)

            if hyper_count >= required_hyper_channels:
                sustained_ticks += 1
                if sustained_ticks >= sustained_ticks_required:
                    tripped = True
                    trip_tick = t
                    break
            else:
                sustained_ticks = 0
    else:
        # Pure Python fallback
        matrix = list(firing_rates_or_raster)
        num_ticks = len(matrix)
        num_ch = len(matrix[0]) if num_ticks > 0 else 0
        sustained_ticks = 0
        tripped = False
        trip_tick = -1

        for t in range(window_ticks, num_ticks):
            hyper_count = 0
            for ch in range(num_ch):
                total_spikes = sum(matrix[tick][ch] for tick in range(t - window_ticks, t))
                if total_spikes >= spikes_per_window_threshold:
                    hyper_count += 1
            if hyper_count >= required_hyper_channels:
                sustained_ticks += 1
                if sustained_ticks >= sustained_ticks_required:
                    tripped = True
                    trip_tick = t
                    break
            else:
                sustained_ticks = 0

    if expect_trip is True and not tripped:
        raise AssertionError(
            f"Expected epileptiform runaway trip (> {threshold_hz} Hz across > {channel_ratio*100}% channels for {duration_ms} ms), "
            f"but breaker did NOT trip. {msg}"
        )
    elif expect_trip is False and tripped:
        raise AssertionError(f"Epileptiform trip occurred unexpectedly at tick {trip_tick}. {msg}")

    return EpileptiformResult(tripped, trip_tick)


def assert_wbc_header_valid(
    header_bytes: bytes,
    expected_magic: bytes = b"WETB",
    expected_major: int = 1,
    expected_minor: int = 0,
    msg: str = "",
) -> Dict[str, Any]:
    """
    Validate that raw 32-byte WBC binary header conforms to the specification.
    Verifies:
      - Total length is at least 32 bytes
      - Magic matches 'WETB'
      - Major and minor version match expected
      - CRC32 checksum is valid (supports standalone header or full binary)
    """
    if len(header_bytes) < 32:
        raise AssertionError(f"Bytecode header too short: {len(header_bytes)} bytes < 32 bytes. {msg}")

    format_candidates: List[str] = []
    try:
        from compiler.isa import HEADER_STRUCT_FORMAT
        format_candidates.append(HEADER_STRUCT_FORMAT)
    except Exception:
        pass
    for fmt in ("<4sBBHIIIIfI", "<4sHHHIIIIfH"):
        if fmt not in format_candidates:
            format_candidates.append(fmt)

    primary_format = format_candidates[0]
    primary_error: Optional[Exception] = None
    last_error: Optional[Exception] = None
    matched_dict: Optional[Dict[str, Any]] = None

    for fmt in format_candidates:
        try:
            unpacked = struct.unpack(fmt, header_bytes[:32])
            magic, major, minor, caps, file_size, stored_crc, num_sections, channel_count, max_charge, reserved = unpacked

            if magic != expected_magic:
                raise AssertionError(f"Invalid WBC header magic: got {magic!r}, expected {expected_magic!r}. {msg}")
            if major != expected_major:
                raise AssertionError(f"Unsupported major version: got {major}, expected {expected_major}. {msg}")
            if minor != expected_minor:
                raise AssertionError(f"Unsupported minor version: got {minor}, expected {expected_minor}. {msg}")

            # Recompute CRC32 with stored_crc field zeroed
            zero_crc_header = struct.pack(
                fmt,
                magic, major, minor, caps, file_size, 0, num_sections, channel_count, max_charge, reserved
            )
            crc_header_only = zlib.crc32(zero_crc_header) & 0xFFFFFFFF

            valid_crc = (stored_crc == crc_header_only)
            if not valid_crc and len(header_bytes) > 32:
                # Emitter computes CRC over entire file with CRC field zeroed
                full_zero = zero_crc_header + header_bytes[32:]
                if stored_crc == (zlib.crc32(full_zero) & 0xFFFFFFFF):
                    valid_crc = True
                elif file_size > 32 and len(header_bytes) >= file_size:
                    if stored_crc == (zlib.crc32(zero_crc_header + header_bytes[32:file_size]) & 0xFFFFFFFF):
                        valid_crc = True

            if not valid_crc:
                raise AssertionError(
                    f"WBC header CRC32 mismatch: stored=0x{stored_crc:08X}, computed=0x{crc_header_only:08X}. {msg}"
                )

            matched_dict = {
                "magic": magic,
                "major": major,
                "minor": minor,
                "version_major": major,
                "version_minor": minor,
                "capabilities": caps,
                "file_size": file_size,
                "checksum_crc32": stored_crc,
                "num_sections": num_sections,
                "channel_count": channel_count,
                "max_charge_nc": max_charge,
                "reserved": reserved,
            }
            break
        except AssertionError as ae:
            if fmt == primary_format:
                primary_error = ae
            last_error = ae
            continue
        except struct.error as se:
            if fmt == primary_format:
                primary_error = se
            last_error = se
            continue

    if matched_dict is not None:
        return matched_dict
    elif primary_error is not None:
        raise primary_error
    elif last_error is not None:
        raise last_error
    else:
        raise AssertionError(f"Failed to validate WBC header. {msg}")


# =============================================================================
# 5. Base E2E Test Case Class
# =============================================================================

class WetLangE2ETestCase(unittest.TestCase):
    """
    Base test case for all WetLang E2E test suites.
    Provides:
      - Isolated temporary directory creation and cleanup per test
      - Helper methods for writing source files and invoking compiler/runtime
      - Execution timing and performance warnings (> 1.0s)
    """

    def setUp(self):
        super().setUp()
        self.test_start_time = time.time()
        self.temp_dir = tempfile.mkdtemp(prefix="wetlang_e2e_")

    def tearDown(self):
        super().tearDown()
        if os.path.isdir(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass
        duration = time.time() - self.test_start_time
        if duration > 1.0:
            print(f"  [PERF WARNING] {self.id()} took {duration:.2f}s")

    def write_source(self, code: str, filename: str = "test.wet") -> str:
        """Write source code snippet to a file in the isolated temp directory."""
        path = os.path.join(self.temp_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(code)
        return path

    def create_temp_file(self, content: Union[str, bytes], filename: str = "temp.bin") -> str:
        """Create a temporary file in the isolated temp directory with string or byte content."""
        path = os.path.join(self.temp_dir, filename)
        mode = "wb" if isinstance(content, bytes) else "w"
        encoding = None if isinstance(content, bytes) else "utf-8"
        with open(path, mode, encoding=encoding) as f:
            f.write(content)
        return path

    def compile_source(self, code: str, output_wbc: Optional[str] = None) -> Tuple[bool, str, Optional[bytes]]:
        """
        Compile WetLang source code using the compiler pipeline if available.
        Returns: (success: bool, error_message: str, wbc_bytes: Optional[bytes])
        """
        if not HAS_COMPILER:
            return False, "Compiler pipeline (M1) not available", None

        try:
            from compiler.lexer import Lexer
            from compiler.parser import Parser
            from compiler.semantic import SemanticAnalyzer
            from compiler.emitter import BytecodeEmitter

            lexer = Lexer(code)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            try:
                analyzer = SemanticAnalyzer(ast)
                if hasattr(analyzer, "analyze") and getattr(analyzer.analyze, "__code__", None) and analyzer.analyze.__code__.co_argcount > 1:
                    analyzer.analyze(ast)
                else:
                    analyzer.analyze()
            except TypeError:
                analyzer = SemanticAnalyzer()
                analyzer.analyze(ast)
            emitter = BytecodeEmitter()
            if hasattr(emitter, "compile"):
                wbc_bytes = emitter.compile(ast)
            else:
                wbc_bytes = emitter.emit(ast)

            if output_wbc:
                with open(output_wbc, "wb") as f:
                    f.write(wbc_bytes)

            return True, "", wbc_bytes
        except Exception as e:
            return False, str(e), None

    def run_program(
        self,
        wbc_path_or_bytes: Union[str, bytes],
        ticks: int = 100,
    ) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
        """
        Execute compiled WBC bytecode using Python bindings if available.
        Returns: (success: bool, error_message: str, telemetry: Optional[dict])
        """
        if not HAS_NATIVE_VM:
            return False, "Native VM / ctypes FFI (M2) not available", None

        try:
            from bindings.runtime import WetRuntime
            runtime = WetRuntime()
            if isinstance(wbc_path_or_bytes, bytes):
                wbc_path = os.path.join(self.temp_dir, "program.wbc")
                with open(wbc_path, "wb") as f:
                    f.write(wbc_path_or_bytes)
            else:
                wbc_path = wbc_path_or_bytes

            runtime.load(wbc_path)
            telemetry = runtime.step(ticks=ticks)
            return True, "", telemetry
        except Exception as e:
            return False, str(e), None


# =============================================================================
# 6. Infrastructure Self-Test Suite
# =============================================================================

class TestInfraCommon(WetLangE2ETestCase):
    """
    Self-test test case verifying that all generators, probes, and domain assertions
    in common.py execute correctly.
    """

    def test_probes_execute_without_crashing(self):
        """Verify availability probe flags return boolean values."""
        self.assertIsInstance(HAS_COMPILER, bool)
        self.assertIsInstance(HAS_NATIVE_VM, bool)
        self.assertIsInstance(HAS_BIOPHYSICS, bool)
        self.assertIsInstance(HAS_INTERLOCKS, bool)
        self.assertIsInstance(HAS_BENCHMARKS, bool)

    def test_make_minimal_wet_program(self):
        """Verify minimal valid WetLang source generator."""
        code = make_minimal_wet_program(channel_id=0, voltage_str="0.8V", p1_str="200us", p2_str="200us")
        self.assertIn("grid mea", code)
        self.assertIn("channel ch0", code)
        self.assertIn("stim_biphasic", code)
        self.assertIn("sync_tick();", code)

    def test_make_wbc_header_valid(self):
        """Verify 32-byte WBC header generation and validation."""
        header = make_wbc_header(magic=b"WETB", major=1, minor=0, caps=0x01, file_size=64, channels=64)
        self.assertEqual(len(header), 32)
        parsed = assert_wbc_header_valid(header)
        self.assertEqual(parsed["magic"], b"WETB")
        self.assertEqual(parsed["major"], 1)
        self.assertEqual(parsed["minor"], 0)
        self.assertEqual(parsed["file_size"], 64)

    def test_make_wbc_header_invalid_magic_raises(self):
        """Verify assert_wbc_header_valid rejects corrupt magic."""
        bad_header = make_wbc_header(magic=b"DEAD")
        with self.assertRaises(AssertionError):
            assert_wbc_header_valid(bad_header)

    def test_generate_mea_coordinates(self):
        """Verify MEA coordinate generators for valid and invalid sets."""
        valid_coords = generate_mea_coordinates(valid=True, count=64)
        self.assertEqual(len(valid_coords), 64)
        for r, c in valid_coords:
            self.assertTrue(0 <= r < 8 and 0 <= c < 8)

        invalid_coords = generate_mea_coordinates(valid=False, count=8)
        self.assertTrue(any(r < 0 or r >= 8 or c < 0 or c >= 8 for r, c in invalid_coords))

    def test_si_value_close_assertion(self):
        """Verify SI unit conversion assertion helper."""
        assert_si_value_close(0.0002, 200e-6, tol=1e-9)
        with self.assertRaises(AssertionError):
            assert_si_value_close(0.0002, 0.0005, tol=1e-6)

    def test_voltage_clamp_assertion(self):
        """Verify voltage clamp domain assertion."""
        # Transfer function check: clamp(requested, -limit, limit) == actual
        assert_voltage_clamped(2.5, 1.2, 1.2)
        assert_voltage_clamped(-2.5, -1.2, 1.2)
        assert_voltage_clamped(0.8, 0.8, 1.2)
        # Boundary check
        assert_voltage_clamped(1.1, min_v=-1.2, max_v=1.2)
        with self.assertRaises(AssertionError):
            assert_voltage_clamped(1.5, min_v=-1.2, max_v=1.2)

    def test_sliding_charge_balance_assertion(self):
        """Verify 10.0 ms circular ring buffer charge balance watchdog simulation."""
        # Balanced biphasic pulses: sum across window is ~0
        balanced_trace = [0.001, -0.001] * 100
        res = assert_sliding_charge_balance(balanced_trace, max_charge_nc=0.5, window_ticks=100)
        self.assertTrue(res.balanced)

        # Unbalanced trace: persistent charge accumulation > 0.5 nC
        unbalanced_trace = [0.01] * 200  # 100 ticks * 0.01 = 1.0 nC > 0.5 nC
        res = assert_sliding_charge_balance(unbalanced_trace, max_charge_nc=0.5, window_ticks=100)
        self.assertFalse(res.balanced)
        self.assertGreaterEqual(res.tick, 100)

    def test_epileptiform_trip_assertion(self):
        """Verify 50.0 ms epileptiform runaway breaker logic."""
        if np is not None:
            # Low firing rate (5 Hz) on 64 channels: should NOT trip
            safe_raster = make_spike_raster_matrix(ticks=600, channels=64, firing_channels=64, rate_hz=5.0)
            res = assert_epileptiform_trip(safe_raster, channels=64, duration_ms=50.0, dt_ms=0.1)
            self.assertFalse(res.tripped)

            # High firing rate (250 Hz) on 35 channels (>35% of 64): MUST trip
            runaway_raster = make_spike_raster_matrix(ticks=1500, channels=64, firing_channels=35, rate_hz=250.0)
            res = assert_epileptiform_trip(runaway_raster, channels=64, duration_ms=50.0, dt_ms=0.1)
            self.assertTrue(res.tripped)
            self.assertGreater(res.tick, 0)

    def test_temp_dir_lifecycle(self):
        """Verify temporary directory management and helpers."""
        self.assertTrue(os.path.isdir(self.temp_dir))
        src_path = self.write_source("test content", filename="example.wet")
        self.assertTrue(os.path.isfile(src_path))
        with open(src_path, "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "test content")

    def test_compile_source_valid(self):
        """Verify compile_source helper with SemanticAnalyzer and BytecodeEmitter."""
        if not HAS_COMPILER:
            self.skipTest("Compiler pipeline (M1) not available")
        code = make_minimal_wet_program(channel_id=0, voltage_str="0.8V", p1_str="200us", p2_str="200us")
        ok, err, wbc = self.compile_source(code)
        self.assertTrue(ok, f"Compilation failed: {err}")
        self.assertIsNotNone(wbc)
        parsed = assert_wbc_header_valid(wbc)
        self.assertEqual(parsed["magic"], b"WETB")
        self.assertEqual(parsed["major"], 1)


if __name__ == "__main__":
    unittest.main()
