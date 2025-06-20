from app.calculation import Calculation
from app.history import CalculationHistory

class CalculatorREPL:
    def __init__(self):
        self.history = CalculationHistory()

    def process_input(self, user_input):
        user_input = user_input.strip()
        if user_input == "":
            print("Invalid input format. Use: <number> <operator> <number>")
            return True

        if user_input.lower() in ['exit', 'quit']:
            print("Exiting calculator.")
            return False

        if user_input.lower() == 'help':
            print("Available commands: help, exit, quit")
            print("Commands: help, exit, quit")
            print("Supported operations: +, -, *, /, ^, root")
            return True

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input format. Use: <number> <operator> <number>")
            return True

        operand1_str, operator, operand2_str = parts
        try:
            operand1 = float(operand1_str)
            operand2 = float(operand2_str)
        except ValueError:
            print("Operands must be numbers.")
            return True

        try:
            calc = Calculation(operand1, operand2, operator)
            result = calc.compute()
            print(f"Result: {result}")
            self.history.add_entry(user_input, result)
            return result
        except Exception as e:
            print(f"Error: {e}")
            return True
