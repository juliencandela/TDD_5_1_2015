import unittest

from money import Money

__author__ = 'marie-helene'


class TestMoney(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(42))
        self.assertEqual(Money.franc(5), Money.franc(5))
        self.assertNotEqual(Money.franc(5), Money.franc(42))
        self.assertNotEqual(Money.franc(5), Money.dollar(5))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency)
        self.assertEqual("CHF", Money.franc(1).currency)

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five * 2)
        self.assertEqual(Money.dollar(15), five * 3)