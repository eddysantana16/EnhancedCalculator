from app.calculator_factory import OperationFactory
from app.history import CalculationHistory
from app.exceptions import CalculationError, InvalidInputError
from app.input_validators import is_valid_operator, validate_operands
from app.logger import logger

from colorama import init, Fore, Style
# Initialize colorama for cross-platform support
init(autoreset=True)

class CalculatorREPL:
    def __init__(self):
        self.history = CalculationHistory()

    def process_input(self, user_input):
        user_input = user_input.strip()

        if user_input.lower() in ("exit", "quit"):
            logger.info("User exited the calculator.")
            print(Fore.CYAN + "Exiting calculator.")
            return False

        if user_input.lower() == "help":
            print(Fore.CYAN + "Available commands:")
            print(Fore.YELLOW + " help, exit, quit, history, clear, undo, redo, save, load")
            print(Fore.CYAN + "\nSupported operations:")
            print(Fore.GREEN + " add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
            return True

        if not user_input:
            print(Fore.RED + "Invalid input format. Use: <operation> <number> <number>")
            return True

        parts = user_input.split()

        if len(parts) != 3:
            print(Fore.RED + "Invalid input format. Use: <operation> <number> <number>")
            return True

        operator, operand1_str, operand2_str = parts

        if not is_valid_operator(operator):
            logger.warning(f"Invalid operator entered: {operator}")  # pragma: no cover
            print(Fore.RED + f"Invalid operator '{operator}'. Use 'help' to see supported operations.")  # pragma: no cover
            return True  # pragma: no cover

        if not validate_operands(operand1_str, operand2_str):
            logger.warning(f"Invalid operands: {operand1_str}, {operand2_str}")  # pragma: no cover
            print(Fore.RED + "Invalid operands. Please enter numeric values within allowed range.")  # pragma: no cover
            return True  # pragma: no cover

        operand1 = float(operand1_str)
        operand2 = float(operand2_str)

        try:
            operation = OperationFactory.get_operation(operator)
            result = operation.execute(operand1, operand2)
            logger.info(f"Calculation performed: {operator} {operand1} {operand2} = {result}")
            print(Fore.GREEN + f"Result: {result}")
            self.history.add_entry(user_input, result)
            return True
        except CalculationError as e:  # pragma: no cover
            logger.error(f"Calculation error: {e}")  # pragma: no cover
            print(Fore.RED + f"Calculation error: {e}")  # pragma: no cover
            return True  # pragma: no cover
        except Exception as e:  # pragma: no cover
            logger.exception("Unexpected error during calculation:")  # pragma: no cover
            print(Fore.RED + f"Unexpected error: {e}")  # pragma: no cover
            return True  # pragma: no cover

