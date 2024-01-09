class Calcul:
    def additionner(self, a, b):
        return a + b

    def soustraire(self, a, b):
        return a - b

    def multiplier(self, a, b):
        return a * b

    def diviser(self, a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            return "Division par zéro impossible"

