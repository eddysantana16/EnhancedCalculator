import pytest
from app.operations import (
    AddOperation, SubtractOperation, MultiplyOperation,
    DivideOperation, PowerOperation, RootOperation,
)
from app.exceptions import DivisionByZeroError, CalculationError

def test_add_operation():
    op = AddOperation()
    assert op.execute(2, 3) == 5
    assert op.execute(-1, 1) == 0

def test_subtract_operation():
    op = SubtractOperation()
    assert op.execute(5, 3) == 2
    assert op.execute(3, 5) == -2

def test_multiply_operation():
    op = MultiplyOperation()
    assert op.execute(4, 3) == 12
    assert op.execute(-2, 3) == -6

def test_divide_operation():
    op = DivideOperation()
    assert op.execute(10, 2) == 5
    assert op.execute(-10, 2) == -5
    with pytest.raises(DivisionByZeroError):
        op.execute(5, 0)

def test_power_operation():
    op = PowerOperation()
    assert op.execute(2, 3) == 8
    assert op.execute(4, 0.5) == 2

def test_root_operation():
    op = RootOperation()
    assert op.execute(27, 3) == 3
    assert op.execute(16, 4) == 2
    with pytest.raises(CalculationError):
        op.execute(-16, 2)  # even root of negative number not allowed
    with pytest.raises(CalculationError):
        op.execute(16, 0)   # zero root undefined

def test_root_negative_odd():
    op = RootOperation()
    result = op.execute(-27, 3)
    assert abs(result + 3) < 1e-6
