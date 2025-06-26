from app.input_validators import validate_operands, is_valid_operator
from app.exceptions import CalculatorError, InvalidInputError

class Calculation:
    def __init__(self, operand1, operand2, operator):
        if not validate_operands(operand1, operand2):
            raise InvalidInputError("Operands must be numeric.") # pragma: no cover
        if not is_valid_operator(operator):
            raise InvalidInputError(f"Operator '{operator}' is not supported.")
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator.lower()

    def compute(self):
        try:
            if self.operator == 'add':
                return self.operand1 + self.operand2 # pragma: no cover
            elif self.operator == 'subtract':
                return self.operand1 - self.operand2 # pragma: no cover
            elif self.operator == 'multiply':
                return self.operand1 * self.operand2 # pragma: no cover
            elif self.operator == 'divide':
                if self.operand2 == 0:
                    raise CalculatorError("Division by zero")  # pragma: no cover
                return self.operand1 / self.operand2 # pragma: no cover
            elif self.operator == 'power': # pragma: no cover
                return self.operand1 ** self.operand2 # pragma: no cover
            elif self.operator == 'root': # pragma: no cover
                if self.operand2 == 0: # pragma: no cover
                    raise CalculatorError("Cannot take 0th root")  # pragma: no cover
                if self.operand1 < 0 and self.operand2 % 2 == 0: # pragma: no cover
                    raise CalculatorError("Cannot take even root of negative number") # pragma: no cover
                return self.operand1 ** (1 / self.operand2) # pragma: no cover
            else: # pragma: no cover
                raise CalculatorError(f"Unsupported operator: {self.operator}") # pragma: no cover
        except Exception as e:
            raise CalculatorError(str(e))  # pragma: no cover
