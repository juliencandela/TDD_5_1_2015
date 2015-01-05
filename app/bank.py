from money import Money

__author__ = 'marie-helene'


class Bank:
    def __init__(self):
        self._rate = {}

    def reduce(self, expression, currency_to):
        return expression.reduce(self, currency_to)

    def add_rate(self, currency_from, currency_to, rate):
        self._rate[(currency_from, currency_to)] = rate

    def rate(self, currency_from, currency_to):
        if currency_from == currency_to:
            return 1
        return self._rate[(currency_from, currency_to)]