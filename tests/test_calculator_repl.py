import pytest
from unittest.mock import patch
from app.calculator_repl import CalculatorREPL
from app.history import CalculationHistory

def test_repl_add_calculation_to_history(tmp_path):
    history_file = tmp_path / "test_history.csv"
    history = CalculationHistory(str(history_file))

    repl = CalculatorREPL()
    repl.history = history

    # Use operation-style input to match REPL expectation
    result = repl.process_input("add 2 3")
    # process_input returns True on success, so check print output instead
    assert result is True

    entries = repl.history.get_history()
    assert any("add 2 3" == e["Input"] for _, e in entries.iterrows())

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
        mock_print.assert_any_call("Invalid input format. Use: <operation> <number> <number>")

@pytest.mark.parametrize("expr, expected", [
    ("add 10 5", 15),
    ("subtract 4 3", 1),
    ("multiply 8 2", 16),
    ("divide 12 4", 3),
    ("power 2 3", 8),
])
def test_repl_various_operations(expr, expected):
    repl = CalculatorREPL()
    with patch('builtins.print') as mock_print:
        repl.process_input(expr)
        # The actual result is printed, so check if the print call includes the expected result
        assert any(str(expected) in str(call.args[0]) for call in mock_print.call_args_list)
