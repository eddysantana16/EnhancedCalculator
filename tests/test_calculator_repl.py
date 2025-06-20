import pytest
from unittest.mock import patch
from app.calculator_repl import CalculatorREPL
from app.history import CalculationHistory

def test_repl_add_calculation_to_history(tmp_path):
    history_file = tmp_path / "test_history.csv"
    history = CalculationHistory(str(history_file))

    repl = CalculatorREPL()
    repl.history = history

    result = repl.process_input("2 + 3")
    assert result == 5.0

    entries = repl.history.get_history()
    assert any("2 + 3" == e["Input"] for _, e in entries.iterrows())

def test_repl_help_and_exit():
    repl = CalculatorREPL()

    with patch('builtins.print') as mock_print:
        repl.process_input("help")
        mock_print.assert_called()

    assert repl.process_input("exit") is False

def test_repl_invalid_input():
    repl = CalculatorREPL()
    with patch('builtins.print') as mock_print:
        repl.process_input("invalid command")
        mock_print.assert_any_call("Invalid input format. Use: <number> <operator> <number>")

@pytest.mark.parametrize("expr, expected", [
    ("10 - 5", 5),
    ("4 * 3", 12),
    ("8 / 2", 4),
    ("2 ^ 3", 8),
])
def test_repl_various_operations(expr, expected):
    repl = CalculatorREPL()
    result = repl.process_input(expr)
    assert result == expected
