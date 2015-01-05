__author__ = 'marie-helene'


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return not self == other