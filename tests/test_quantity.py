import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_positive_quantity(self):
        self.assertEqual(parse_quantity("12"), 12)
        self.assertEqual(parse_quantity(" 12 \n"), 12)

    def test_zero_quantity(self):
        for value in ("0", " 0 \n"):
            with self.subTest(value=value):
                self.assertEqual(parse_quantity(value), 0)

    def test_negative_quantity(self):
        for value in ("-1", "-12", " -12 \n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_quantity(value)

    def test_invalid_quantity(self):
        for value in ("", " ", "abc", "1.5"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_quantity(value)
