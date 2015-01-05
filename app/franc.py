__author__ = 'marie-helene'


class Franc:
    def __init__(self, amount):
        self.amount = amount

    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return not self == other

