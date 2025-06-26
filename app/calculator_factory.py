from app.operations import (
    AddOperation, SubtractOperation, MultiplyOperation, DivideOperation,
    PowerOperation, RootOperation, ModulusOperation, IntDivideOperation,
    PercentOperation, AbsDiffOperation
)
from app.exceptions import CalculationError

class OperationFactory:
    _operations = {
        "add": AddOperation,
        "subtract": SubtractOperation,
        "multiply": MultiplyOperation,
        "divide": DivideOperation,
        "power": PowerOperation,
        "root": RootOperation,
        "modulus": ModulusOperation,
        "int_divide": IntDivideOperation,
        "percent": PercentOperation,
        "abs_diff": AbsDiffOperation,
    }

    @staticmethod
    def get_operation(op_name):
        op_class = OperationFactory._operations.get(op_name.lower())
        if not op_class:
            raise CalculationError(f"Operation '{op_name}' is not supported.")
        return op_class()
