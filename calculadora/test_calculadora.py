import unittest
from fractions import Fraction
from calculadora import calcular_expressao

class TestLogicaCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calcular_expressao("2+3"), 5)

    def test_subtracao(self):
        self.assertEqual(calcular_expressao("10-4"), 6)

    def test_multiplicacao(self):
        self.assertEqual(calcular_expressao("4*5"), 20)

    def test_divisao(self):
        self.assertEqual(calcular_expressao("10/2"), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calcular_expressao("5/0")

    def test_expressao_invalida(self):
        with self.assertRaises(ValueError):
            calcular_expressao("2++")

    # 🔥 novos testes
    def test_fracao_soma(self):
        self.assertEqual(calcular_expressao("1/2+1/3"), Fraction(5, 6))

    def test_fracao_multiplicacao(self):
        self.assertEqual(calcular_expressao("2/3*3/4"), Fraction(1, 2))

if __name__ == "__main__":
    unittest.main()
