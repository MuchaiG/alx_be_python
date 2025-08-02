# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(5, 3), 8)
        self.assertEqual(self.calc.addition(-2, 2), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(10, 4), 6)
        self.assertEqual(self.calc.subtraction(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 4), -4)

    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(9, 3), 3)

    def test_divide_by_zero(self):
        result = self.calc.division(10, 0)
        self.assertEqual(result, "Error: Cannot divide by zero.")

if __name__ == "__main__":
    unittest.main()
