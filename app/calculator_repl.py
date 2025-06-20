from app.calculation import Calculation
from app.history import CalculationHistory
from app.exceptions import CalculationError

class CalculatorREPL:
    def __init__(self):
        self.history = CalculationHistory()

    def process_input(self, user_input):
        user_input = user_input.strip()

        if user_input.lower() in ("exit", "quit"):
            print("Exiting calculator.")
            return False

        if user_input.lower() == "help":
            print("Available commands: help, exit, quit")
            print("Commands: help, exit, quit")
            print("Supported operations: +, -, *, /, ^, root")
            return True

        if not user_input:
            print("Invalid input format. Use: <number> <operator> <number>")  # pragma: no cover
            return True  # pragma: no cover

        parts = user_input.split()

        if len(parts) != 3:
            print("Invalid input format. Use: <number> <operator> <number>")  # pragma: no cover
            return True  # pragma: no cover

        operand1_str, operator, operand2_str = parts

        try:
            operand1 = float(operand1_str)
            operand2 = float(operand2_str)
        except ValueError:
            print("Invalid operands. Please enter numeric values.")  # pragma: no cover
            return True  # pragma: no cover

        try:
            # Note operand1, operand2, operator order
            calculation = Calculation(operand1, operand2, operator)
            result = calculation.compute()
            print(f"Result: {result}")
            self.history.add_entry(user_input, result)
            return result
        except CalculationError as e:
            print(f"Calculation error: {e}")  # pragma: no cover
            return True  # pragma: no cover
        except Exception as e:
            print(f"Error: {e}")  # pragma: no cover
            return True  # pragma: no cover
