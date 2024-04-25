import unittest

def calcular_media(a, b):
    return (a + b) / 2

class TestMedia(unittest.TestCase):

    def test_media_de_dois_numeros(self):
        self.assertEqual(calcular_media(3, 5), 4)

if __name__ == '__main__':
    unittest.main()
