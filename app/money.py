__author__ = 'marie-helene'


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount and self.__class__ == other.__class__

    def __ne__(self, other):
        return not self == other

    @classmethod
    def dollar(cls, amount):
        from dollar import Dollar
        return Dollar(amount)

    @classmethod
    def franc(cls, amount):
        from franc import Franc
        return Franc(amount)