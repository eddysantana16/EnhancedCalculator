def is_valid_operator(op: str) -> bool:
    valid_ops = ['+', '-', '*', '/', '^', 'root']
    return op in valid_ops

def validate_operands(operand1, operand2) -> bool:
    try:
        float(operand1)
        float(operand2)
        return True
    except ValueError:
        return False

def is_number(value: str) -> bool:
    if value is None:
        return False
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
