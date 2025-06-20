import pandas as pd

class Caretaker:
    def __init__(self):
        self.states = []
        self.current_index = -1

    def save_state(self, state: pd.DataFrame):
        # Remove any states ahead of current index for proper redo behavior
        self.states = self.states[:self.current_index + 1]
        self.states.append(state.copy())
        self.current_index += 1

    def undo(self, current_state: pd.DataFrame):
        if self.current_index <= 0:
            return current_state
        self.current_index -= 1
        return self.states[self.current_index].copy()

    def redo(self, current_state: pd.DataFrame):
        if self.current_index + 1 >= len(self.states):
            return current_state
        self.current_index += 1
        return self.states[self.current_index].copy()
