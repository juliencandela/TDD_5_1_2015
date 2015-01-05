__author__ = 'marie-helene'


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier
