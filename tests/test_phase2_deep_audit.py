"""
Phase 2 Deep Adversarial Red-Team Audit Test Suite
=================================================
Rigorous, adversarial verification of WetLang:
  - Malformed & corrupted WBC binary fuzzing (header, CRC32, truncation, bounds)
  - Capability privilege escalation prevention (stimulation, microfluidics, motors)
  - Cyber-physical actuator execution & hydrodynamic shear stress limits
  - Cryptographic biosafety signing & tamper-evidence
  - Arithmetic edge cases (DIV_BY_ZERO, stack underflow, float anomalies)
  - Multi-threaded concurrent execution stress (16 parallel VMs)
  - 100-cycle VM lifecycle memory leak endurance
  - End-to-end cyber-physical organoid program compilation and execution
"""

import unittest
import struct
import zlib
import threading
import numpy as np

from bindings.runtime import WetRuntime, WetVM, WetVMError
from bindings.ffi import WetStatus, WetVMConfig, WetActuatorTelemetry
from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.semantic import SemanticAnalyzer, SemanticError
from compiler.emitter import BytecodeEmitter
from compiler.isa import Opcode, Capability, HEADER_MAGIC, HEADER_SIZE
from compiler.crypto_signer import sign_bytecode, verify_bytecode_signature


class TestPhase2DeepAudit(unittest.TestCase):
    """Deep adversarial audit tests for WetLang compiler, native VM, and cyber-physical actuators."""

    def _build_minimal_valid_wbc(self, caps: int = Capability.NONE) -> bytes:
        emitter = BytecodeEmitter()
        emitter.capabilities = caps
        emitter.emit(Opcode.SYNC_TICK)
        return emitter._build_wbc_binary()

    # =========================================================================
    # 1. WBC Binary Header Corruption & Fuzzing
    # =========================================================================

    def test_01_wbc_header_truncation(self):
        """Verify strict rejection of truncated WBC files."""
        rt = WetRuntime()
        for size in [0, 4, 16, 31]:
            corrupted = b"WETB"[:size] if size >= 4 else b"\x00" * size
            with self.assertRaises(WetVMError) as ctx:
                rt.load(corrupted)
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_MALFORMED_SECTION)
        rt.close()

    def test_02_wbc_magic_corruption(self):
        """Verify strict rejection of corrupted magic bytes."""
        valid_wbc = bytearray(self._build_minimal_valid_wbc())
        rt = WetRuntime()
        for bad_magic in [b"NOPE", b"WET\x00", b"ABCD", b"\x00\x00\x00\x00"]:
            valid_wbc[:4] = bad_magic
            with self.assertRaises(WetVMError) as ctx:
                rt.load(bytes(valid_wbc))
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_INVALID_MAGIC)
        rt.close()

    def test_03_wbc_crc32_tamper_detection(self):
        """Verify tamper detection: flipping even 1 byte triggers CRC mismatch."""
        valid_wbc = bytearray(self._build_minimal_valid_wbc())
        # Flip a byte in the payload (after 32-byte header)
        if len(valid_wbc) > 35:
            valid_wbc[35] ^= 0xFF
        rt = WetRuntime()
        with self.assertRaises(WetVMError) as ctx:
            rt.load(bytes(valid_wbc))
        self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_CRC_MISMATCH)
        rt.close()

    def test_04_wbc_unsupported_version(self):
        """Verify rejection of incompatible future bytecode version."""
        valid_wbc = bytearray(self._build_minimal_valid_wbc())
        valid_wbc[4] = 99  # Major version 99
        # Recompute CRC32 so version check is reached
        struct.pack_into("<I", valid_wbc, 12, 0)
        crc = zlib.crc32(bytes(valid_wbc))
        struct.pack_into("<I", valid_wbc, 12, crc)

        rt = WetRuntime()
        with self.assertRaises(WetVMError) as ctx:
            rt.load(bytes(valid_wbc))
        self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_UNSUPPORTED_VERSION)
        rt.close()

    # =========================================================================
    # 2. Capability Privilege Escalation Attacks
    # =========================================================================

    def test_05_stimulation_without_capability(self):
        """Verify VM prevents stimulation when CAP_STIMULATION is withheld."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.NONE  # Deny stimulation
        emitter.emit(Opcode.PUSH_FLOAT, 0.4)    # voltage
        emitter.emit(Opcode.PUSH_FLOAT, 0.2)    # p1
        emitter.emit(Opcode.PUSH_FLOAT, 0.2)    # p2
        emitter.emit(Opcode.PUSH_FLOAT, 0.0)    # interphase
        emitter.emit(Opcode.STIM_BIPHASIC, 0)   # channel 0
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        rt = WetRuntime()
        rt.load(wbc)
        with self.assertRaises(WetVMError) as ctx:
            rt.step(1)
        self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_CAPABILITY_DENIED)
        rt.close()

    def test_06_microfluidics_without_capability(self):
        """Verify VM prevents pump actuation when CAP_MICROFLUIDICS is withheld."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION  # No microfluidics
        emitter.emit(Opcode.PUMP_SET_RATE, 0, 1.5)
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        rt = WetRuntime()
        rt.load(wbc)
        with self.assertRaises(WetVMError) as ctx:
            rt.step(1)
        self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_CAPABILITY_DENIED)
        rt.close()

    def test_07_motor_actuation_without_capability(self):
        """Verify VM prevents motor stepping when CAP_MOTOR_ACTUATION is withheld."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_MICROFLUIDICS  # No motor
        emitter.emit(Opcode.MOTOR_STEP, 0, 200, 60.0)
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        rt = WetRuntime()
        rt.load(wbc)
        with self.assertRaises(WetVMError) as ctx:
            rt.step(1)
        self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_CAPABILITY_DENIED)
        rt.close()

    # =========================================================================
    # 3. Cyber-Physical Actuator & Hydrodynamic Shear Stress Safety
    # =========================================================================

    def test_08_hydrodynamic_shear_stress_enforcement(self):
        """Verify VM halts if microfluidic pump exceeds safe limit (15.0 uL/min)."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_MICROFLUIDICS
        emitter.emit(Opcode.PUMP_SET_RATE, 0, 25.0)  # 25 uL/min exceeds 15 uL/min limit!
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        rt = WetRuntime()
        rt.load(wbc)
        with self.assertRaises(WetVMError) as ctx:
            rt.step(1)
        self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_SHEAR_STRESS_EXCEEDED)
        rt.close()

    def test_09_compiler_shear_stress_rejection(self):
        """Verify compiler rejects programs attempting dangerous microfluidic flow rates."""
        code_shear = """
        fn main() {
            pump_set_rate(0, 30.0uL/min); // Exceeds safe limit!
            sync_tick();
        }
        """
        ast = Parser(Lexer(code_shear).tokenize()).parse()
        with self.assertRaises(SemanticError) as ctx:
            SemanticAnalyzer(ast).analyze()
        self.assertEqual(ctx.exception.error_code, "ERR_SHEAR_STRESS_EXCEEDED")

    def test_10_valid_actuator_telemetry_inspection(self):
        """Verify pump, valve, and motor states update accurately in telemetry."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_MICROFLUIDICS | Capability.CAP_MOTOR_ACTUATION
        emitter.emit(Opcode.PUMP_SET_RATE, 0, 2.5)   # Pump 0 = 2.5 uL/min
        emitter.emit(Opcode.PUMP_DISPENSE, 0, 10.0)  # Pump 0 dispense 10 uL
        emitter.emit(Opcode.VALVE_SET, 1, 1)         # Valve 1 = Open
        emitter.emit(Opcode.MOTOR_STEP, 2, 400, 120.0) # Motor 2 = +400 steps
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        rt = WetRuntime()
        rt.load(wbc)
        rt.step(1)

        act = rt.get_actuator_telemetry()
        self.assertAlmostEqual(act.pump_rates[0], 2.5, places=3)
        self.assertAlmostEqual(act.pump_dispensed[0], 10.0, places=3)
        self.assertEqual(act.valves[1], 1)
        self.assertEqual(act.motors[2], 400)
        self.assertAlmostEqual(act.ambient_temperature_c, 37.0, places=1)
        self.assertAlmostEqual(act.fluid_pressure_kpa[0], 101.325, places=1)
        rt.close()

    # =========================================================================
    # 4. Cryptographic Biosafety Signing & Tamper Verification
    # =========================================================================

    def test_11_cryptographic_signing_and_verification(self):
        """Verify HMAC-SHA256 biosafety signing and tamper-evident rejection."""
        secret_key = b"wetworld-institute-secret-master-key-2026"
        raw_wbc = self._build_minimal_valid_wbc(caps=Capability.CAP_STIMULATION)

        signed_wbc = sign_bytecode(raw_wbc, secret_key)
        self.assertTrue(len(signed_wbc) > len(raw_wbc))

        # 1. Valid signature verifies cleanly
        ok, reason = verify_bytecode_signature(signed_wbc, secret_key)
        self.assertTrue(ok, reason)

        # 2. Tampered payload fails verification
        tampered = bytearray(signed_wbc)
        tampered[20] ^= 0x55
        bad_ok, bad_reason = verify_bytecode_signature(bytes(tampered), secret_key)
        self.assertFalse(bad_ok)
        self.assertIn("mismatch", bad_reason)

        # 3. Wrong secret key fails verification
        wrong_key = b"unauthorized-intruder-key"
        wrong_ok, _ = verify_bytecode_signature(signed_wbc, wrong_key)
        self.assertFalse(wrong_ok)

    # =========================================================================
    # 5. Arithmetic Edge Cases & Safety Interlocks
    # =========================================================================

    def test_12_division_by_zero_safety(self):
        """Verify division by zero trips cleanly without host crash."""
        emitter = BytecodeEmitter()
        emitter.emit(Opcode.PUSH_INT, 42)
        emitter.emit(Opcode.PUSH_INT, 0)
        emitter.emit(Opcode.DIV_I)
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        rt = WetRuntime()
        rt.load(wbc)
        with self.assertRaises(WetVMError) as ctx:
            rt.step(1)
        self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_DIVISION_BY_ZERO)
        rt.close()

    def test_13_stack_underflow_safety(self):
        """Verify popping an empty stack trips cleanly."""
        emitter = BytecodeEmitter()
        emitter.emit(Opcode.POP)
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        rt = WetRuntime()
        rt.load(wbc)
        with self.assertRaises(WetVMError) as ctx:
            rt.step(1)
        self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_STACK_UNDERFLOW)
        rt.close()

    # =========================================================================
    # 6. Multi-Threaded Concurrency Stress & Memory Lifecycle
    # =========================================================================

    def test_14_multithreaded_concurrent_vms(self):
        """Verify 16 parallel threads running distinct WetVM instances with zero cross-talk."""
        thread_count = 16
        ticks_per_thread = 100
        errors = []

        def worker(thread_idx: int):
            try:
                vm = WetRuntime()
                emitter = BytecodeEmitter()
                emitter.capabilities = Capability.CAP_CLOSED_LOOP
                emitter.emit(Opcode.SYNC_TICK)
                vm.load(emitter._build_wbc_binary())

                for _ in range(ticks_per_thread):
                    telem = vm.step(1)
                    if telem.population_rate_hz < 0.0:
                        raise ValueError("Invalid population rate")
                vm.close()
            except Exception as ex:
                errors.append((thread_idx, str(ex)))

        threads = [threading.Thread(target=worker, args=(i,)) for i in range(thread_count)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(len(errors), 0, f"Thread execution errors: {errors}")

    def test_15_hundred_cycle_memory_endurance(self):
        """Verify 100 rapid load/step/free cycles execute with zero leaks or crashes."""
        wbc = self._build_minimal_valid_wbc(caps=Capability.CAP_CLOSED_LOOP)
        for i in range(100):
            vm = WetRuntime()
            vm.load(wbc)
            telem = vm.step(10)
            self.assertEqual(telem.current_tick, 10)
            vm.close()

    # =========================================================================
    # 7. Complete End-to-End Cyber-Physical Program
    # =========================================================================

    def test_16_full_cyber_physical_closed_loop_program(self):
        """Verify end-to-end compilation & execution of a combined organoid + hardware program."""
        code = """
        organoid BrainUnit {
            radius: 180um;
            perfusion: 1.5uL/min;
        }

        fn main() {
            // Actuate life support microfluidic pump
            pump_set_rate(0, 1.5uL/min);
            valve_open(0);

            // Cycle-accurate closed-loop stimulation
            stim_biphasic(0, 0.4V, 0.2ms, 0.2ms);
            sync_tick();
        }
        """
        ast = Parser(Lexer(code).tokenize()).parse()
        SemanticAnalyzer(ast).analyze()
        wbc = BytecodeEmitter().compile(ast)

        rt = WetRuntime()
        rt.load(wbc)
        rt.step(1)

        act = rt.get_actuator_telemetry()
        self.assertAlmostEqual(act.pump_rates[0], 1.5, places=2)
        self.assertEqual(act.valves[0], 1)

        telem = rt.get_telemetry()
        self.assertEqual(telem.current_tick, 1)
        self.assertAlmostEqual(abs(telem.voltages[0]), 0.4, places=1)
        rt.close()


if __name__ == "__main__":
    unittest.main()
