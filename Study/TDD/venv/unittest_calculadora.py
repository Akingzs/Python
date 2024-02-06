import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def fala_oi(self):
        print('oi')
        
    def test_sum_5_5_return_10(self):
        self.assertEqual(soma(5,5), 10)
        
    def 

unittest.main(verbosity=2)