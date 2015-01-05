__author__ = 'marie-helene'

import unittest

from dollar import Dollar


class TestDollar(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five * 2
        self.assertEqual(10, product.amount)
        product = five * 3
        self.assertEqual(15, product.amount)