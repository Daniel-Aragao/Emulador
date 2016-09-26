import unittest
from Codigo import Codigo


class TestCodigo(unittest.TestCase):
    @unittest.expectedFailure
    def test_solve_value_valor_errors(self):
        registrador = Codigo.solve_value("256")  # -65

    @unittest.expectedFailure
    def test_solve_value_memory_errors(self):
        registrador = Codigo.solve_value("0x17")  # -65

    @unittest.expectedFailure
    def test_solve_value_registrador_errors(self):
        registrador = Codigo.solve_value("E")  # -65

    def test_solve_memoria(self):
        memoria = Codigo.solve_value("0x0010")  # -16
        self.assertEqual(-16, memoria)

    def test_solve_registrador(self):
        registrador = Codigo.solve_value("A")  # -65
        self.assertEqual(-65, registrador)

    def test_solve_value(self):
        valor = Codigo.solve_value("20")  # 20
        self.assertEqual(20, valor)

    def test_to_byte_array_add_memoria(self):
        codigo = Codigo(["add", "0x10", "2"])

        self.assertItemsEqual([2, -16, 2, -1], codigo.byteArray)

    def test_to_byte_array_mov_registrador(self):
        codigo = Codigo(["mov", "A", "2"])

        self.assertItemsEqual([3, -65, 2, -1], codigo.byteArray)

    def test_to_byte_array_imul(self):
        codigo = Codigo(["imul", "C", "0x0001", "4"])

        self.assertItemsEqual([4, -67, -1, 4], codigo.byteArray)

    def test_to_byte_array_inc(self):
        codigo = Codigo(["inc", "0x0001"])

        self.assertItemsEqual([1, -1, -1, -1], codigo.byteArray)


if __name__ == '__main__':
    unittest.main()
