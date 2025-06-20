def is_number(value):
    """
    Check if the input value can be converted to a float.
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def is_valid_operator(operator):
    """
    Check if the operator is valid.
    """
    valid_operators = {"+", "-", "*", "/", "^", "root"}
    return operator in valid_operators


def validate_operands(operand1, operand2):
    """
    Validate both operands are numbers.
    """
    return is_number(operand1) and is_number(operand2)
