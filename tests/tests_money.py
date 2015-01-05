__author__ = 'marie-helene'

import unittest

from dollar import Dollar


class TestDollar(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount)