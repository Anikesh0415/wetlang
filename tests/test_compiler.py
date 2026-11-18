import unittest
from wetlang.compiler import Lexer, Parser, SemanticAnalyzer, BytecodeEmitter, Dimension


class TestWetLangCompiler(unittest.TestCase):
    def test_lexer_physical_units(self):
        tokens = Lexer("stim_biphasic(0, 0.5V, 0.2ms, 0.2ms);").tokenize()
        self.assertEqual(tokens[0].type.name, "STIM_BIPHASIC")
        self.assertEqual(tokens[4].dimension, Dimension.VOLTAGE)
        self.assertAlmostEqual(tokens[4].si_value, 0.5)

    def test_parser_and_semantic_analysis(self):
        code = """
        organoid Brain {
            radius: 180um;
            perfusion: 1.5uL/min;
        }
        fn main() {
            stim_biphasic(0, 0.4V, 0.2ms, 0.2ms);
            sync_tick();
        }
        """
        ast = Parser(Lexer(code).tokenize()).parse()
        SemanticAnalyzer(ast).analyze()
        wbc = BytecodeEmitter().compile(ast)
        self.assertEqual(wbc[:4], b"WETB")


if __name__ == "__main__":
    unittest.main()
