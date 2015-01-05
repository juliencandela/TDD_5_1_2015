__author__ = 'marie-helene'
from money import Money


class Franc(Money):

    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)


