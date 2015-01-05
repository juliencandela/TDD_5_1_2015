__author__ = 'marie-helene'


class Expression:
    def __init__(self, addend, augend):
        self.addend = addend
        self.augend = augend
        #TODO Apprendre le mot augend à cet ordinateur de type pas intelligent

    def reduce(self, bank, currency_to):
        from money import Money
        amount = bank.reduce(self.addend, currency_to).amount + bank.reduce(self.augend, currency_to).amount
        return Money(amount, currency_to)

    def __add__(self, other):
        return Expression(self, other)

    def __mul__(self, multiplier):
        return Expression(self.addend * multiplier, self.augend * multiplier)