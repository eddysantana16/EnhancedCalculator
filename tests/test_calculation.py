import pytest
from app.calculation import Calculation
from app.exceptions import CalculatorError

@pytest.mark.parametrize(
    "a, operator, b",
    [
        (5, "/", 0),      # Division by zero should raise CalculatorError during compute()
        (5, "unknown", 2) # Unsupported operator should raise ValueError during Calculation creation
    ]
)
def test_calculation_errors(a, operator, b):
    if operator == "unknown":
        with pytest.raises(ValueError):  # Expect ValueError on constructor
            Calculation(a, b, operator)
    else:
        calc = Calculation(a, b, operator)
        with pytest.raises(CalculatorError):  # Expect CalculatorError on division by zero
            calc.compute()
