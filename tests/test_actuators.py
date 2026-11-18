import unittest
from wetlang.compiler import Lexer, Parser, SemanticAnalyzer, BytecodeEmitter
from wetlang.runtime import WetRuntime


class TestWetLangActuators(unittest.TestCase):
    def test_cyber_physical_actuation(self):
        code = """
        organoid Brain {
            radius: 180um;
            perfusion: 1.5uL/min;
        }
        fn main() {
            pump_set_rate(0, 2.5uL/min);
            valve_open(0);
            motor_step(1, 200, 60.0rpm);
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
        self.assertAlmostEqual(act.pump_rates[0], 2.5, places=2)
        self.assertEqual(act.valves[0], 1)
        self.assertEqual(act.motors[1], 200)
        rt.close()


if __name__ == "__main__":
    unittest.main()
