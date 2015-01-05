__author__ = 'marie-helene'


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)
