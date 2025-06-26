import pandas as pd
from app.calculator_config import CalculatorConfig
import os

class CalculationHistory:
    def __init__(self, filename=None):
        # Use given filename or default path from config and env var
        if filename:
            self.history_file = filename
        else:
            self.history_file = os.path.join(
                CalculatorConfig.CALCULATOR_HISTORY_DIR,
                os.getenv("HISTORY_FILE", "calc_history.csv")
            )
        self.entries = []  # list of (input, result)
        self.undo_stack = []
        self.redo_stack = []

        # Load existing history
        self.load()

    def add_entry(self, calc_input, result):
        self.entries.append((calc_input, result))
        self.undo_stack.append((calc_input, result))
        self.redo_stack.clear()  # reset redo stack

    def get_history(self):
        # Return pandas DataFrame for tests expecting it
        return pd.DataFrame(self.entries, columns=["Input", "Result"])

    def clear(self):
        self.entries.clear()
        self.undo_stack.clear()
        self.redo_stack.clear()
        self.save()

    def undo(self):
        if not self.undo_stack:
            raise IndexError("Nothing to undo.")
        last = self.undo_stack.pop()
        self.redo_stack.append(last)
        self.entries.remove(last)

    def redo(self):
        if not self.redo_stack:
            raise IndexError("Nothing to redo.")
        entry = self.redo_stack.pop()
        self.entries.append(entry)
        self.undo_stack.append(entry)

    def save(self):
        df = pd.DataFrame(self.entries, columns=["Input", "Result"])
        dir_path = os.path.dirname(self.history_file)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        df.to_csv(self.history_file, index=False)

    def load(self):
        try:
            df = pd.read_csv(self.history_file)
            self.entries = list(df.itertuples(index=False, name=None))
            self.undo_stack = self.entries.copy()
            self.redo_stack.clear()
        except FileNotFoundError:
            self.entries = []
            self.undo_stack = []
            self.redo_stack = []
