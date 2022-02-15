import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 2
        num_2 = 3
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 5)


    def test_suma_dos_negativos(self):
        num_1 = -2
        num_2 = -3
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -5)


if __name__ == '__main__':
    unittest.main()