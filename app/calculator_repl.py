# calculator_repl.py

from app.calculator_factory import OperationFactory
from app.history import CalculationHistory
from app.exceptions import CalculationError, InvalidInputError
from app.input_validators import is_valid_operator, validate_operands
from app.logger import logger  

class CalculatorREPL:
    def __init__(self):
        self.history = CalculationHistory()

    def process_input(self, user_input):
        user_input = user_input.strip()

        if user_input.lower() in ("exit", "quit"):
            logger.info("User exited the calculator.")
            print("Exiting calculator.")
            return False

        if user_input.lower() == "help":
            print("Available commands: help, exit, quit, history, clear, undo, redo, save, load")
            print("Supported operations:")
            print(" add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
            return True

        if not user_input:
            print("Invalid input format. Use: <operation> <number> <number>")
            return True

        parts = user_input.split()

        if len(parts) != 3:
            print("Invalid input format. Use: <operation> <number> <number>")
            return True

        operator, operand1_str, operand2_str = parts

        if not is_valid_operator(operator):
            logger.warning(f"Invalid operator entered: {operator}")
            print(f"Invalid operator '{operator}'. Use 'help' to see supported operations.")
            return True

        if not validate_operands(operand1_str, operand2_str):
            logger.warning(f"Invalid operands: {operand1_str}, {operand2_str}")
            print("Invalid operands. Please enter numeric values within allowed range.")
            return True

        operand1 = float(operand1_str)
        operand2 = float(operand2_str)

        try:
            operation = OperationFactory.get_operation(operator)
            result = operation.execute(operand1, operand2)
            logger.info(f"Calculation performed: {operator} {operand1} {operand2} = {result}")
            print(f"Result: {result}")
            self.history.add_entry(user_input, result)
            return True
        except CalculationError as e:
            logger.error(f"Calculation error: {e}")
            print(f"Calculation error: {e}")
            return True
        except Exception as e:
            logger.exception("Unexpected error during calculation:")
            print(f"Unexpected error: {e}")
            return True
