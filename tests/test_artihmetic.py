from bank import Bank
from money import Money

__author__ = 'marie-helene'
import unittest


class TestArithmetic(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five * 2)
        self.assertEqual(Money.dollar(15), five * 3)

    def test_simple_addition(self):
        five = Money.dollar(5)
        sum = five + five
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_expression(self):
        five = Money.dollar(5)
        sum = five + five
        self.assertEqual(five, sum.addend)
        self.assertEqual(five, sum.augend)

    def test_reduce_sum(self):
        expression = Money.dollar(3) + Money.dollar(4)
        bank = Bank()
        reduced = bank.reduce(expression, "USD")
        self.assertEqual(Money.dollar(7), reduced)

    def test_reduce_money(self):
        bank = Bank()
        reduce = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), reduce)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_rate_same_currency(self):
        self.assertEqual(1, Bank().rate("USD", "USD"))

    def test_mixed_currency_addition(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        sum = Money.dollar(5) + Money.franc(10)
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(10), result)

    def test_big_sum(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        sum = (Money.dollar(5) + Money.franc(10) + Money.dollar(4)) * 2
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(28), result)