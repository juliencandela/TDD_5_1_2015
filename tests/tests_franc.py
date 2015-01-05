__author__ = 'marie-helene'

import unittest

from franc import Franc


class TestFranc(unittest.TestCase):
    def test_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five * 2)
        self.assertEqual(Franc(15), five * 3)

    def test_equality(self):
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(5), Franc(42))