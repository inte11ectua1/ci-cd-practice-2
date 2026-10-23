import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(calculator.add(-2, -3), -5)

    def test_add_mixed(self):
        self.assertEqual(calculator.add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(calculator.add(0, 0), 0)
