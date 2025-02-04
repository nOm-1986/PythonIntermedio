import unittest
import src.calculator as c

class CalculatorTests(unittest.TestCase):
    
    def test_sum(self):
        assert c.sum(5,6) == 11

    def test_sub(self):
        assert c.substraction2(5, 5) == 0