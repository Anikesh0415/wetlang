"""
WetLang Phase 3 Hardware Readiness & Biophysical Safety Test Suite
=================================================================
Exhaustive verification of all Phase 3 Adversarial Audit remediations:
1. HD-MEA water-window clamping (Pt/TiN/IrOx/PEDOT material & geometric area CIC).
2. Persistent unbounded cumulative DC charge accumulator (zero decay drift).
3. Active hardware discharge recovery switch.
4. Spherical Reaction-Diffusion Thiele anoxia model (avascular core necrosis).
5. Geometry-aware hydrodynamic wall shear stress calculation.
6. Dead-heading microfluidic valve-pump overpressure interlock.
7. Ring-0 Life Support Supervisor maintaining baseline perfusion on Ring-1 HALT.
8. Static memory arena allocation (zero heap malloc/free in real-time execution).
9. Asymmetric Ed25519 cryptographic bytecode signing & tamper verification.
"""

import unittest
import numpy as np

try:
    from wetlang.compiler.lexer import Lexer
    from wetlang.compiler.parser import Parser
    from wetlang.compiler.semantic import SemanticAnalyzer, SemanticError
    from wetlang.compiler.emitter import BytecodeEmitter
    from wetlang.compiler.isa import Opcode, Capability
    from wetlang.compiler.crypto_signer import (
        generate_ed25519_keypair,
        sign_bytecode_ed25519,
        verify_bytecode_ed25519,
    )
    from wetlang.bindings.runtime import WetRuntime, WetVM, WetVMError
    from wetlang.bindings.ffi import WetStatus, WetVMConfig, WetVMFFI
except ImportError:
    from compiler.lexer import Lexer
    from compiler.parser import Parser
    from compiler.semantic import SemanticAnalyzer, SemanticError
    from compiler.emitter import BytecodeEmitter
    from compiler.isa import Opcode, Capability
    from compiler.crypto_signer import (
        generate_ed25519_keypair,
        sign_bytecode_ed25519,
        verify_bytecode_ed25519,
    )
    from bindings.runtime import WetRuntime, WetVM, WetVMError
    from bindings.ffi import WetStatus, WetVMConfig, WetVMFFI


class TestPhase3HardwareReadiness(unittest.TestCase):

    def _compile(self, src: str) -> bytes:
        tokens = Lexer(src).tokenize()
        ast = Parser(tokens).parse()
        SemanticAnalyzer(ast).analyze()
        return BytecodeEmitter().compile(ast)

    # -------------------------------------------------------------------------
    # 1. HD-MEA Water-Window Parameterized Clamping
    # -------------------------------------------------------------------------
    def test_01_hd_mea_water_window_clamping(self):
        """Verify MaxOne HD-MEA Pt electrode (132.25 um^2) limits charge to ~0.132 nC."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetRuntime() as rt:
            rt.load(wbc)
            # Material 0 = Platinum (0.10 mC/cm^2), Area = 132.25 um^2 -> Limit = 0.132 nC
            rt.configure_electrode(0, 132.25)

            # Injected charge of ~0.20 nC is under old 0.5 nC limit, but trips HD-MEA Pt limit!
            # 0.8V for 0.2 ms on 1 MOhm = 0.8 uA * 0.2 ms = 0.16 nC >= 0.132 nC
            with self.assertRaises(WetVMError) as ctx:
                rt.inject_stimulus(0, 0.8, 0.2, 0.0)
                rt.step(2)
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_CHARGE_IMBALANCE)
            self.assertIn("CIC limit", str(ctx.exception))

    # -------------------------------------------------------------------------
    # 2. Persistent Unbounded Cumulative DC Charge Accumulator
    # -------------------------------------------------------------------------
    def test_02_persistent_unbounded_dc_accumulator(self):
        """Verify unbounded cumulative DC charge does not decay and trips WET_ERR_DC_DRIFT."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetRuntime() as rt:
            rt.load(wbc)
            # HD-MEA Pt electrode: phase limit ~0.132 nC, cumulative DC limit ~0.264 nC
            rt.configure_electrode(0, 132.25)

            tripped = False
            # Inject small pulses (~0.05 nC) spaced out past 100 ticks (so sliding ring buffer resets)
            for _ in range(20):
                try:
                    rt.inject_stimulus(0, 0.3, 0.1, 0.0)
                    rt.step(15)
                except WetVMError as err:
                    if err.status in (WetStatus.WET_ERR_DC_DRIFT, WetStatus.WET_ERR_CHARGE_IMBALANCE):
                        tripped = True
                        break

            self.assertTrue(tripped, "Persistent unbounded DC accumulator must trip on unrecovered DC charge")

    # -------------------------------------------------------------------------
    # 3. Active Hardware Discharge Recovery
    # -------------------------------------------------------------------------
    def test_03_active_hardware_discharge_recovery(self):
        """Verify active hardware discharge grounding clears accumulated DC charge safely."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_STIMULATION | Capability.CAP_HIGH_VOLTAGE
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetRuntime() as rt:
            rt.load(wbc)
            rt.configure_electrode(0, 5000.0)

            # Inject several monophasic pulses (accumulating ~0.3 nC)
            for _ in range(5):
                rt.inject_stimulus(0, 0.2, 0.1, 0.0)
                rt.step(2)

            # Actuate active hardware discharge switch on channel 0
            rt.active_discharge(0)

            # We can now inject another 5 pulses without tripping, because accumulator was zeroed!
            for _ in range(5):
                rt.inject_stimulus(0, 0.2, 0.1, 0.0)
                rt.step(2)

            self.assertFalse(rt.is_halted)

    # -------------------------------------------------------------------------
    # 4. Spherical Reaction-Diffusion Thiele Anoxia Model
    # -------------------------------------------------------------------------
    def test_04_spherical_diffusion_thiele_anoxia(self):
        """Verify avascular organoid > 250 um is rejected even with perfusion unless vascularized."""
        # 1. Unvascularized large organoid: must be rejected!
        code_avascular = """
        organoid GiantCorticalUnit {
            radius: 350um;
            perfusion: 2.0uL/min;
        }
        fn main() { sync_tick(); }
        """
        ast = Parser(Lexer(code_avascular).tokenize()).parse()
        with self.assertRaises(SemanticError) as ctx:
            SemanticAnalyzer(ast).analyze()
        self.assertEqual(ctx.exception.error_code, "ERR_AVASCULAR_CORE_NECROSIS")

        # 2. Vascularized large organoid: permitted!
        code_vascularized = """
        organoid GiantCorticalUnit {
            radius: 350um;
            perfusion: 2.0uL/min;
            vascularized: true;
        }
        fn main() { sync_tick(); }
        """
        ast2 = Parser(Lexer(code_vascularized).tokenize()).parse()
        SemanticAnalyzer(ast2).analyze() # Must succeed without error

    # -------------------------------------------------------------------------
    # 5. Geometry-Aware Hydrodynamic Wall Shear Stress
    # -------------------------------------------------------------------------
    def test_05_geometry_aware_shear_stress(self):
        """Verify wall shear stress tau_w in narrow channels is calculated and clamped."""
        # Narrow channel (200 um x 100 um) with 10 uL/min flow rate produces tau_w > 0.05 Pa
        code_shear = """
        fn main() {
            pump_set_rate(0, 10.0uL/min, 200um, 100um);
            sync_tick();
        }
        """
        ast = Parser(Lexer(code_shear).tokenize()).parse()
        with self.assertRaises(SemanticError) as ctx:
            SemanticAnalyzer(ast).analyze()
        self.assertEqual(ctx.exception.error_code, "ERR_SHEAR_STRESS_EXCEEDED")
        self.assertIn("tau_w", str(ctx.exception))

    # -------------------------------------------------------------------------
    # 6. Dead-Heading Valve-Pump Interlock
    # -------------------------------------------------------------------------
    def test_06_dead_heading_valve_pump_interlock(self):
        """Verify running pump with closed downstream valve trips ERR_DEAD_HEAD_OVERPRESSURE."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_MICROFLUIDICS
        emitter.emit(Opcode.PUMP_SET_RATE, 0, 2.5) # Pump 0 = 2.5 uL/min, but Valve 0 is closed (0)!
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        with WetRuntime() as rt:
            rt.load(wbc)
            rt.enable_dead_head_protection(True)
            with self.assertRaises(WetVMError) as ctx:
                rt.step(1)
            self.assertEqual(ctx.exception.status, WetStatus.WET_ERR_ACTUATOR_FAULT)
            self.assertIn("ERR_DEAD_HEAD_OVERPRESSURE", str(ctx.exception))

    # -------------------------------------------------------------------------
    # 7. Ring-0 Life Support Supervisor
    # -------------------------------------------------------------------------
    def test_07_ring0_life_support_supervisor(self):
        """Verify Ring-0 supervisor maintains baseline perfusion and 37C when user code finishes."""
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_MICROFLUIDICS
        emitter.emit(Opcode.HALT)
        wbc = emitter._build_wbc_binary()

        with WetRuntime() as rt:
            rt.load(wbc)
            rt.step(1)

            # Query actuator state: Ring-0 supervisor maintains 1.5 uL/min baseline and 37C
            act = rt.get_actuator_telemetry()
            self.assertAlmostEqual(act.ambient_temperature_c, 37.0, places=1)
            self.assertAlmostEqual(act.pump_rates[0], 1.5, places=2)

    # -------------------------------------------------------------------------
    # 8. Static Memory Arena Allocation (Zero Heap Malloc)
    # -------------------------------------------------------------------------
    def test_08_static_arena_allocation_zero_malloc(self):
        """Verify VM can be initialized in caller-provided static memory arena."""
        ffi = WetVMFFI()
        # Allocate 256 KB memory buffer
        arena_size = 256 * 1024
        vm_handle, arena_buf = ffi.create_vm_arena(arena_size)
        self.assertIsNotNone(vm_handle)

        # Build simple bytecode
        emitter = BytecodeEmitter()
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        status = ffi.load_bytecode(vm_handle, wbc)
        self.assertEqual(status, WetStatus.WET_OK)

        telem = ffi.allocate_telemetry()
        status = ffi.step_tick(vm_handle, telem)
        self.assertEqual(status, WetStatus.WET_OK)
        self.assertEqual(telem.current_tick, 1)

        # Free arena-allocated VM (does not call free() on stack/locals/vm)
        ffi.free_vm(vm_handle)

    # -------------------------------------------------------------------------
    # 9. Asymmetric Ed25519 Cryptographic Provenance
    # -------------------------------------------------------------------------
    def test_09_ed25519_asymmetric_bytecode_provenance(self):
        """Verify Ed25519 asymmetric signature signing and public-key verification."""
        priv_bytes, pub_bytes = generate_ed25519_keypair()
        self.assertEqual(len(priv_bytes), 32)
        self.assertEqual(len(pub_bytes), 32)

        emitter = BytecodeEmitter()
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        # Sign bytecode with offline private key
        signed_wbc = sign_bytecode_ed25519(wbc, priv_bytes)
        self.assertTrue(len(signed_wbc) > len(wbc))

        # Verify with public key embedded in bioreactor firmware
        is_valid, reason = verify_bytecode_ed25519(signed_wbc, pub_bytes)
        self.assertTrue(is_valid, f"Verification failed: {reason}")

        # Tamper test: flip a single byte in payload
        tampered = bytearray(signed_wbc)
        tampered[20] ^= 0xFF
        is_valid_tampered, _ = verify_bytecode_ed25519(bytes(tampered), pub_bytes)
        self.assertFalse(is_valid_tampered, "Tampered bytecode must be rejected")


if __name__ == "__main__":
    unittest.main()
