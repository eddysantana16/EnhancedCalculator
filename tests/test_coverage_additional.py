import pytest
from app.calculator_repl import CalculatorREPL
from unittest.mock import patch

def test_repl_empty_and_unknown_commands(monkeypatch):
    repl = CalculatorREPL()
    # Empty input returns True (allowed, but prints invalid message)
    assert repl.process_input("") is True
    # Unknown command returns True as well
    assert repl.process_input("unknowncommand") is True

def test_repl_help_output(capsys):
    repl = CalculatorREPL()
    repl.process_input("help")
    out, _ = capsys.readouterr()
    # Adjusted to match actual output
    assert "Supported operations" in out
    assert "Commands" in out

def test_repl_exit_command():
    repl = CalculatorREPL()
    # exit returns False to signal exit
    assert repl.process_input("exit") is False
    assert repl.process_input("quit") is False
