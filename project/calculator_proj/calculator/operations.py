class CalculatorOperations:
    def evaluate(self, expression):
        try:
            return str(eval(expression))
        except Exception as e:
            return "Error"
