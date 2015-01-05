__author__ = 'marie-helene'


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __ne__(self, other):
        return not self == other

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def __repr__(self):
        return str(self.amount)+self.currency

    def __str__(self):
        return repr(self)

    @classmethod
    def dollar(cls, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Money(amount, "CHF")

    @property
    def currency(self):
        return self._currency

