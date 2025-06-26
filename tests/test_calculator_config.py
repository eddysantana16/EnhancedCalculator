import os
import pytest
from app.calculator_config import CalculatorConfig

def test_env_var_auto_save(monkeypatch):
    # Patch CALCULATOR_AUTO_SAVE environment variable
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "True")
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "10")  # valid size for validation

    # Reload config to pick up monkeypatched env vars
    CalculatorConfig.load()

    assert CalculatorConfig.CALCULATOR_AUTO_SAVE is True
    assert CalculatorConfig.CALCULATOR_MAX_HISTORY_SIZE == 10

def test_invalid_max_history_size(monkeypatch):
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "-1")
    with pytest.raises(ValueError):
        CalculatorConfig.load()

def test_invalid_precision(monkeypatch):
    monkeypatch.setenv("CALCULATOR_PRECISION", "-5")
    with pytest.raises(ValueError):
        CalculatorConfig.load()
