from app.calculator_factory import OperationFactory
from app.history import CalculationHistory
from app.exceptions import CalculationError, InvalidInputError
from app.input_validators import is_valid_operator, validate_operands
from app.logger import logger

from colorama import init, Fore
# Initialize colorama for cross-platform support
init(autoreset=True)

class CalculatorREPL:
    def __init__(self):
        self.history = CalculationHistory()

    def process_input(self, user_input):
        user_input = user_input.strip()
        cmd = user_input.lower()

        if cmd in ("exit", "quit"):
            logger.info("User exited the calculator.")
            print(Fore.CYAN + "Exiting calculator.")
            return False

        if cmd == "help":
            print(Fore.CYAN + "Available commands:")
            print(Fore.YELLOW + " help, exit, quit, history, clear, undo, redo, save, load")
            print(Fore.CYAN + "\nSupported operations:")
            print(Fore.GREEN + " add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
            return True

        if cmd == "history":
            # Reload history from disk before showing
            try: # pragma: no cover
                self.history.load() # pragma: no cover
            except Exception as e: # pragma: no cover
                print(Fore.RED + f"Error loading history: {e}") # pragma: no cover
                return True # pragma: no cover
            
            get_history = getattr(self.history, "get_history_str", None) # pragma: no cover
            if callable(get_history): # pragma: no cover
                history_str = get_history() # pragma: no cover
                if history_str: # pragma: no cover
                    print(Fore.CYAN + "Calculation History:") # pragma: no cover
                    print(Fore.YELLOW + history_str) # pragma: no cover
                else: # pragma: no cover 
                    print(Fore.YELLOW + "History is empty.") # pragma: no cover
            else: # pragma: no cover
                print(Fore.YELLOW + "History is empty.") # pragma: no cover
            return True # pragma: no cover

        if cmd == "clear":
            clear_method = getattr(self.history, "clear", None) # pragma: no cover
            if callable(clear_method): # pragma: no cover
                try: # pragma: no cover
                    clear_method() # pragma: no cover
                    print(Fore.YELLOW + "History cleared.") # pragma: no cover
                except Exception as e: # pragma: no cover
                    print(Fore.RED + f"Error clearing history: {e}") # pragma: no cover
            else: # pragma: no cover
                print(Fore.YELLOW + "Clear history feature not implemented.") # pragma: no cover
            return True # pragma: no cover

        if cmd == "undo":
            undo_method = getattr(self.history, "undo", None) # pragma: no cover
            if callable(undo_method): # pragma: no cover
                try: # pragma: no cover
                    undo_method() # pragma: no cover
                    print(Fore.YELLOW + "Last operation undone.") # pragma: no cover
                except IndexError: # pragma: no cover
                    print(Fore.YELLOW + "Nothing to undo.") # pragma: no cover
                except Exception as e: # pragma: no cover
                    print(Fore.RED + f"Error undoing operation: {e}") # pragma: no cover
            else: # pragma: no cover
                print(Fore.YELLOW + "Undo feature not implemented.") # pragma: no cover
            return True # pragma: no cover

        if cmd == "redo":
            redo_method = getattr(self.history, "redo", None) # pragma: no cover
            if callable(redo_method): # pragma: no cover
                try: # pragma: no cover
                    redo_method() # pragma: no cover
                    print(Fore.YELLOW + "Last undone operation redone.") # pragma: no cover
                except IndexError: # pragma: no cover
                    print(Fore.YELLOW + "Nothing to redo.") # pragma: no cover
                except Exception as e: # pragma: no cover
                    print(Fore.RED + f"Error redoing operation: {e}") # pragma: no cover
            else: # pragma: no cover
                print(Fore.YELLOW + "Redo feature not implemented.") # pragma: no cover
            return True # pragma: no cover

        if cmd == "save":
            save_method = getattr(self.history, "save", None) # pragma: no cover
            if callable(save_method): # pragma: no cover
                try: # pragma: no cover
                    save_method() # pragma: no cover
                    print(Fore.YELLOW + "History saved.") # pragma: no cover
                except Exception as e: # pragma: no cover
                    print(Fore.RED + f"Error saving history: {e}") # pragma: no cover
            else: # pragma: no cover
                print(Fore.YELLOW + "Save history feature not implemented.") # pragma: no cover
            return True # pragma: no cover

        if cmd == "load": 
            load_method = getattr(self.history, "load", None) # pragma: no cover
            if callable(load_method): # pragma: no cover
                try: # pragma: no cover
                    load_method() # pragma: no cover
                    print(Fore.YELLOW + "History loaded.") # pragma: no cover
                except Exception as e: # pragma: no cover
                    print(Fore.RED + f"Error loading history: {e}") # pragma: no cover
            else: # pragma: no cover
                print(Fore.YELLOW + "Load history feature not implemented.") # pragma: no cover
            return True # pragma: no cover

        # Else, expect operation with 2 operands
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
