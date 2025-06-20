import os
import pandas as pd
from app.history import CalculationHistory

def test_add_and_get_history():
    history = CalculationHistory(filename="test_history.csv")
    history.clear()
    history.add_entry("2 + 2", 4)
    df = history.get_history()
    assert df.iloc[0]["Input"] == "2 + 2"
    assert df.iloc[0]["Result"] == 4

def test_save_and_load_history():
    history = CalculationHistory(filename="test_history.csv")
    history.clear()
    history.add_entry("3 * 3", 9)
    history.save()

    new_history = CalculationHistory(filename="test_history.csv")
    new_history.load()
    df = new_history.get_history()
    assert df.iloc[0]["Input"] == "3 * 3"
    assert df.iloc[0]["Result"] == 9

    os.remove("test_history.csv")
