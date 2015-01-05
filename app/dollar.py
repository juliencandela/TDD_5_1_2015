__author__ = 'marie-helene'
from money import Money


class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)


