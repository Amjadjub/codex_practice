import unittest

from calculator import add, divide, modulo, multiply, power, subtract


class CalculatorTests(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(7, 4), 3)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(6, 5), 30)

    def test_divide(self) -> None:
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ValueError):
            divide(8, 0)

    def test_power(self) -> None:
        self.assertEqual(power(2, 3), 8)

    def test_modulo(self) -> None:
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_by_zero(self) -> None:
        with self.assertRaises(ValueError):
            modulo(10, 0)


if __name__ == "__main__":
    unittest.main()
