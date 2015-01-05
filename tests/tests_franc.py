from money import Money

__author__ = 'marie-helene'

import unittest


class TestFranc(unittest.TestCase):
    def test_multiplication(self):
        five = Money.franc(5)
        self.assertEqual(Money.franc(10), five * 2)
        self.assertEqual(Money.franc(15), five * 3)
