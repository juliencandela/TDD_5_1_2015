from money import Money

__author__ = 'marie-helene'

import unittest


class TestDollar(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five * 2)
        self.assertEqual(Money.dollar(15), five * 3)
