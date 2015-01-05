__author__ = 'marie-helene'

import unittest

from dollar import Dollar


class TestDollar(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five * 2)
        self.assertEqual(Dollar(15), five * 3)
