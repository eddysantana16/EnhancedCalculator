import pytest
from app.calculator_repl import CalculatorREPL
from unittest.mock import patch
from colorama import Fore

def test_repl_empty_and_unknown_commands():
    repl = CalculatorREPL()
    with patch('builtins.print') as mock_print:
        assert repl.process_input("") is True
        mock_print.assert_any_call(Fore.RED + "Invalid input format. Use: <operation> <number> <number>")
    with patch('builtins.print') as mock_print:
        assert repl.process_input("unknowncommand") is True
        mock_print.assert_any_call(Fore.RED + "Invalid input format. Use: <operation> <number> <number>")

def test_repl_help_output(capsys):
    repl = CalculatorREPL()
    repl.process_input("help")
    out, _ = capsys.readouterr()
    assert "Supported operations" in out
    assert "Available commands" in out

def test_repl_exit_command():
    repl = CalculatorREPL()
    assert repl.process_input("exit") is False
    assert repl.process_input("quit") is False
