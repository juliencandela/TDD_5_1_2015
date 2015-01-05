import unittest

from franc import Franc
from money import Money

__author__ = 'marie-helene'


class TestMoney(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(42))
        self.assertEqual(Money.franc(5), Money.franc(5))
        self.assertNotEqual(Money.franc(5), Money.franc(42))
        self.assertNotEqual(Money.franc(5), Money.dollar(5))