import unittest
from ArrayTools import ArrayTools


class MyTestCase(unittest.TestCase):
    def test_sub_array_without_steps(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        resultado = ArrayTools.sub_array(lista, 1, 4)

        self.assertItemsEqual([2, 3, 4, 5], resultado)

    def test_sub_array_with_steps(self):
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        resultado = ArrayTools.sub_array(lista, 1, 5, 2)

        self.assertItemsEqual([2, 4, 6], resultado)

    def test_append123On456off3(self):
        lista = [4, 5, 6, 0, 0, 0]
        src = [1, 2, 3]
        ArrayTools.append_array(src, lista, 3, 3)
        self.assertItemsEqual([4, 5, 6, 1, 2, 3], lista)

    def test_append123On456off2(self):
        lista = [4, 5, 6, 0, 0, 0]
        src = [1, 2, 3]
        ArrayTools.append_array(src, lista, 2, 3)
        self.assertItemsEqual([4, 5, 1, 2, 3, 0], lista)

    def test_append123On456off2(self):
        lista = [4, 5, 6, 0, 0, 0]
        src = [1, 2, 3]
        ArrayTools.append_array(src, lista, 2, 2)
        self.assertItemsEqual([4, 5, 1, 2, 0, 0], lista)


if __name__ == '__main__':
    unittest.main()
