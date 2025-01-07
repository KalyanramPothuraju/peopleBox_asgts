import unittest
from services import calculate_discount, final_price

class TestCalculateDiscount(unittest.TestCase):
    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 10), 10)
        self.assertEqual(calculate_discount(200, 15), 30)
        self.assertEqual(calculate_discount(0, 50), 0)
        self.assertEqual(calculate_discount(100, 0), 0)
        self.assertEqual(calculate_discount(100, 100), 100)

class TestFinalPrice(unittest.TestCase):
    def test_final_price(self):
        self.assertEqual(final_price(100, 10), 90)
        self.assertEqual(final_price(200, 15), 170)
        self.assertEqual(final_price(0, 50), 0)
        self.assertEqual(final_price(100, 0), 100)
        self.assertEqual(final_price(100, 100), 0)