import pytest
from app.input_validators import is_number, is_valid_operator

def test_is_number_valid():
    assert is_number("5")
    assert is_number("3.14")
    assert is_number("-2")
    assert is_number("0")

def test_is_number_invalid():
    assert not is_number("abc")
    assert not is_number("")
    assert not is_number(None)
    assert not is_number("5+5")

def test_is_valid_operator_valid():
    for op in ['+', '-', '*', '/', '^', 'root']:
        assert is_valid_operator(op)

def test_is_valid_operator_invalid():
    for op in ['%', '**', 'log', '', None]:
        assert not is_valid_operator(op)
