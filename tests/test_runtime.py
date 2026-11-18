import unittest
from wetlang.runtime import WetRuntime, WetStatus
from wetlang.compiler import BytecodeEmitter, Opcode, Capability


class TestWetLangRuntime(unittest.TestCase):
    def test_vm_stepping(self):
        emitter = BytecodeEmitter()
        emitter.capabilities = Capability.CAP_CLOSED_LOOP
        emitter.emit(Opcode.SYNC_TICK)
        wbc = emitter._build_wbc_binary()

        rt = WetRuntime()
        rt.load(wbc)
        telem = rt.step(10)
        self.assertEqual(telem.current_tick, 10)
        self.assertAlmostEqual(telem.sim_time_ms, 1.0, places=2)
        rt.close()


if __name__ == "__main__":
    unittest.main()
