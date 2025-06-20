from app.input_validators import validate_operands, is_valid_operator
from app.exceptions import CalculatorError

class Calculation:
    def __init__(self, operand1, operand2, operator):
        if not validate_operands(operand1, operand2):
            raise ValueError("Invalid operands")
        if not is_valid_operator(operator):
            raise ValueError("Invalid operator")
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    def compute(self):
        try:
            if self.operator == '+':
                return self.operand1 + self.operand2
            elif self.operator == '-':
                return self.operand1 - self.operand2
            elif self.operator == '*':
                return self.operand1 * self.operand2
            elif self.operator == '/':
                if self.operand2 == 0:
                    raise CalculatorError("Division by zero")
                return self.operand1 / self.operand2
            elif self.operator == '^':
                return self.operand1 ** self.operand2
            elif self.operator == 'root':
                if self.operand2 == 0:
                    raise CalculatorError("Cannot take 0th root")
                if self.operand1 < 0 and self.operand2 % 2 == 0:
                    raise CalculatorError("Cannot take even root of negative number")
                return self.operand1 ** (1 / self.operand2)
            else:
                raise CalculatorError(f"Unsupported operator: {self.operator}")
        except Exception as e:
            raise CalculatorError(str(e))
