# input_validators.py

from app.calculator_config import CalculatorConfig

def is_number(value):
    """
    Check if the input value can be converted to a float and is within allowed range.
    """
    try:
        num = float(value)
        if abs(num) > CalculatorConfig.CALCULATOR_MAX_INPUT_VALUE:
            return False
        return True
    except (ValueError, TypeError):
        return False

def is_valid_operator(operator):
    """
    Check if the operator is valid.
    Handles None or non-string gracefully.
    Also supports symbolic operators like +, -, *, /, ^.
    """
    valid_operators = {
        "add", "subtract", "multiply", "divide", "power", "root",
        "modulus", "int_divide", "percent", "abs_diff",
        "+", "-", "*", "/", "^"
    }
    if not isinstance(operator, str):
        return False
    return operator.lower() in valid_operators

def validate_operands(operand1, operand2):
    """
    Validate both operands are numbers and within allowed range.
    """
    return is_number(operand1) and is_number(operand2)
