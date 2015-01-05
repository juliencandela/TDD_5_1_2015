import unittest
from dollar import Dollar
from franc import Franc

__author__ = 'marie-helene'


class TestMoney(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(42))
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(5), Franc(42))
        self.assertNotEqual(Franc(5), Dollar(5))