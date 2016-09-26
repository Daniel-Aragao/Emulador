import unittest
from Codigo import Codigo


class TestCodigo(unittest.TestCase):

    @unittest.expectedFailure
    def test_solve_value_registrador_errors(self):
            registrador = Codigo.solve_value("E")  # -65
            self.assertEqual(-65, registrador)

    def test_solve_value(self):
        memoria = Codigo.solve_value("0x0010")  # -16
        registrador = Codigo.solve_value("A")  # -65
        valor = Codigo.solve_value("20")  # 20

        self.assertEqual(-16, memoria)
        self.assertEqual(-65, registrador)
        self.assertEqual(20, valor)

if __name__ == '__main__':
    unittest.main()