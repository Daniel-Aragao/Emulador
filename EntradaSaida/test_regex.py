import unittest
from Regex import Regex


class TestRegex(unittest.TestCase):

    def test_Numero_de_linhas_enviadas_4_retorno_length_deve_ser_4(self):
        linhas = ["add A,3", "mov A, 5", "imul C, 2, 3", "inc A"]
        regex = Regex(linhas)
        self.assertEqual(len(linhas), len(regex.traducao))

    def test_deve_receber_byte_array_com_addA3_e_retornar_26531(self):
        linhas = ["add A,3", "mov A, 5", "imul C, 2, 3", "inc A"]
        regex = Regex(linhas)
        self.assertItemsEqual([2, -65, 3, -1], regex.traducao[0].byteArray)

    def test_deve_receber_byte_array_com_movA5_e_retornar_36551(self):
        linhas = ["add A,3", "mov A, 5", "imul C, 2, 3", "inc A"]
        regex = Regex(linhas)
        self.assertItemsEqual([3, -65, 5, -1], regex.traducao[1].byteArray)

    def test_deve_receber_byte_array_com_imulC23_e_retornar_46723(self):
        linhas = ["add A,3", "mov A, 5", "imul C, 2, 3", "inc A"]
        regex = Regex(linhas)
        self.assertItemsEqual([4, -67, 2, 3], regex.traducao[2].byteArray)

    def test_deve_receber_byte_array_com_incA_e_retornar_165(self):
        linhas = ["add A,3", "mov A, 5", "imul C, 2, 3", "inc A"]
        regex = Regex(linhas)
        self.assertItemsEqual([1, -65, -1, -1], regex.traducao[3].byteArray)

    def test_deve_receber_byte_array_com_inc0x002_e_retornar_12(self):
        linhas = ["add A,3", "mov A, 5", "imul C, 2, 3", "inc 0x002"]
        regex = Regex(linhas)
        self.assertItemsEqual([1, -2, -1, -1], regex.traducao[3].byteArray)

if __name__ == '__main__':
    unittest.main()
