import pandas as pd

class CalculationHistory:
    def __init__(self, filename="history.csv"):
        self.filename = filename
        try:
            self.history = pd.read_csv(self.filename)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=["Input", "Result"])

    def add_entry(self, calculation_input, result):
        new_entry = {"Input": calculation_input, "Result": result}
        new_df = pd.DataFrame([new_entry])
        # Filter out empty or all-NA columns before concatenation to avoid FutureWarning
        dfs_to_concat = [df for df in [self.history, new_df] if not df.empty and df.dropna(axis=1, how='all').shape[1] > 0]
        self.history = pd.concat(dfs_to_concat, ignore_index=True)

    def get_history(self):
        return self.history

    def save(self):
        self.history.to_csv(self.filename, index=False)

    def load(self):
        """Reload history from file (used in tests)."""
        self.history = pd.read_csv(self.filename)

    def clear(self):
        self.history = pd.DataFrame(columns=["Input", "Result"])
        self.save()
