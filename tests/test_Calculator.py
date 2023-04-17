from unittest import TestCase

from utils.Calculator import Calculator


class TestCalculator(TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator(1, 2)
        super().setUp()

    def test_add(self):
        self.assertEqual(self.calculator.add(), 3)

    def test_sub(self):
        self.assertEqual(self.calculator.sub(), -1)

    def test_mul(self):
        self.assertEqual(self.calculator.mul(), 2)
