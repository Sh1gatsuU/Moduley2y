import unittest
from factorial import calculate_factorial

class TestFactorialFunction(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(calculate_factorial(0), 1)

    def test_factorial_of_one(self):
        self.assertEqual(calculate_factorial(1), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(calculate_factorial(5), 120)

    def test_factorial_raises_value_error_for_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-2)

if __name__ == '__main__':
    unittest.main()