import os
import pytest
from app.calculator_config import load_config
from app.exceptions import ConfigurationError

def test_load_valid_config(monkeypatch):
    # Set environment variable for testing
    monkeypatch.setenv("HISTORY_FILE", "test_history.csv")
    config = load_config()
    assert config["HISTORY_FILE"] == "test_history.csv"

def test_missing_config(monkeypatch):
    # Ensure variable is not set
    monkeypatch.delenv("HISTORY_FILE", raising=False)
    with pytest.raises(ConfigurationError):
        load_config()
