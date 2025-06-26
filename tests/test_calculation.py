import pytest
from app.calculation import Calculation
from app.exceptions import CalculatorError, InvalidInputError

@pytest.mark.parametrize(
    "a, operator, b",
    [
        (5, "divide", 0),      # Division by zero should raise CalculatorError during compute()
        (5, "unknown", 2)      # Unsupported operator should raise InvalidInputError during Calculation creation
    ]
)
def test_calculation_errors(a, operator, b):
    if operator == "unknown":
        with pytest.raises(InvalidInputError):  # Invalid operator raises error on construction
            Calculation(a, b, operator)
    else:
        calc = Calculation(a, b, operator)
        with pytest.raises(CalculatorError):  # Division by zero raises error during compute
            calc.compute()
