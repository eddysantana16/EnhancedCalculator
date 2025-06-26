from app.exceptions import DivisionByZeroError, CalculationError

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
            raise DivisionByZeroError("Division by zero is not allowed.")
        return a / b

class PowerOperation:
    def execute(self, a, b):
        return a ** b

class RootOperation:
    def execute(self, a, b):
        if b == 0:
            raise CalculationError("Root degree cannot be zero.")
        if a < 0 and b % 2 == 0:
            raise CalculationError("Cannot take even root of negative number.")
        if a < 0 and b % 2 == 1:
            return -((-a) ** (1 / b))
        return a ** (1 / b)

class ModulusOperation:
    def execute(self, a, b):
        if b == 0:
            raise CalculationError("Division by zero in modulus operation.")
        return a % b

class IntDivideOperation:
    def execute(self, a, b):
        if b == 0:
            raise CalculationError("Division by zero in integer division.")
        return a // b

class PercentOperation:
    def execute(self, a, b):
        if b == 0:
            raise CalculationError("Division by zero in percentage calculation.")
        return (a / b) * 100

class AbsDiffOperation:
    def execute(self, a, b):
        return abs(a - b)
