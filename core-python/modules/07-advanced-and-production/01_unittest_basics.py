"""
01 — unittest Basics

THEORY
------
What: unittest is Python's built-in testing framework using TestCase classes and
      assertion methods like assertEqual, assertRaises, setUp, and tearDown.
Why:  Verify code behavior automatically; no extra install required; industry standard.
Key rules:
  - Test methods must start with test_; TestCase subclasses group related tests.
  - setUp runs before each test; tearDown runs after (even on failure).
  - Use assertRaises as context manager for expected exceptions.
When to use: Unit testing any Python module; CI pipelines; regression prevention.
Common mistakes: Testing implementation not behavior; shared mutable state between tests;
                 missing edge cases (zero, empty, None).

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/01_unittest_basics.py
"""

import unittest  # standard library testing framework


def add(a, b):  # add two numbers
    return a + b


def divide(a, b):  # divide a by b with zero guard
    if b == 0:  # prevent division by zero
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:  # simple calculator with history tracking
    def __init__(self):  # initialize empty operation history
        self.history = []

    def multiply(self, a, b):  # multiply and record operation
        result = a * b  # compute product
        self.history.append(f"{a} * {b} = {result}")  # log operation string
        return result  # return product


class TestAdd(unittest.TestCase):  # test suite for add()
    def test_add_positive(self):  # verify positive integer addition
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):  # verify negative integer addition
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):  # verify zero edge case
        self.assertEqual(add(0, 0), 0)


class TestDivide(unittest.TestCase):  # test suite for divide()
    def test_divide_normal(self):  # verify floating-point division
        self.assertAlmostEqual(divide(10, 4), 2.5)

    def test_divide_by_zero(self):  # verify ValueError on zero divisor
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestCalculator(unittest.TestCase):  # test suite for Calculator class
    def setUp(self):  # create fresh calculator before each test
        self.calc = Calculator()

    def test_multiply(self):  # verify multiplication result
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_history(self):  # verify history records operations
        self.calc.multiply(2, 5)
        self.assertIn("2 * 5 = 10", self.calc.history)

    def tearDown(self):  # optional cleanup hook after each test
        pass


def main() -> None:  # entry point that runs the test suite
    print("=" * 50)  # print section divider
    print("PRACTICE — Running unittest suite")  # section header
    print("=" * 50)  # close header divider
    unittest.main(verbosity=2, exit=False)  # discover and run tests with verbose output


if __name__ == "__main__":  # run tests when executed directly
    main()  # start unittest discovery and execution
