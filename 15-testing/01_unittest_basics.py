"""01 — unittest Basics"""

import unittest

# Code under test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    def __init__(self):
        self.history = []

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

# Tests
class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

class TestDivide(unittest.TestCase):
    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 4), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_history(self):
        self.calc.multiply(2, 5)
        self.assertIn("2 * 5 = 10", self.calc.history)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
