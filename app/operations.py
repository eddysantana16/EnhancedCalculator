class AddOperation:
    def execute(self, a, b):
        return a + b

class SubtractOperation:
    def execute(self, a, b):
        return a - b

class MultiplyOperation:
    def execute(self, a, b):
        return a * b

class DivideOperation:
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

class PowerOperation:
    def execute(self, a, b):
        return a ** b

class RootOperation:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Root degree cannot be zero")
        if a < 0 and b % 2 == 0:
            raise ValueError("Cannot take even root of negative number")
        # Handle negative odd roots properly:
        if a < 0 and b % 2 == 1:
            return -((-a) ** (1 / b))
        return a ** (1 / b)
