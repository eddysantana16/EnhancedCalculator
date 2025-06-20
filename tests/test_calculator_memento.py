import copy
import pandas as pd
import pytest
from app.calculator_memento import Caretaker

def test_caretaker_save_and_undo_redo():
    caretaker = Caretaker()

    state = pd.DataFrame(columns=["Input", "Result"])

    # Save initial empty state
    caretaker.save_state(state)

    # Add first calculation and save state AFTER
    state = pd.concat([state, pd.DataFrame([{"Input": "1 + 1", "Result": 2}])], ignore_index=True)
    caretaker.save_state(state)

    # Add second calculation and save
    state = pd.concat([state, pd.DataFrame([{"Input": "2 * 2", "Result": 4}])], ignore_index=True)
    caretaker.save_state(state)

    # Add third calculation and save
    state = pd.concat([state, pd.DataFrame([{"Input": "3 ^ 2", "Result": 9}])], ignore_index=True)
    caretaker.save_state(state)

    # Undo should remove last calc
    state_undo = caretaker.undo(state)
    assert "3 ^ 2" not in state_undo["Input"].values
    assert "2 * 2" in state_undo["Input"].values

    # Undo again removes second calc
    state_undo2 = caretaker.undo(state_undo)
    assert "2 * 2" not in state_undo2["Input"].values
    assert "1 + 1" in state_undo2["Input"].values

    # Redo brings back second calc
    state_redo = caretaker.redo(state_undo2)
    assert "2 * 2" in state_redo["Input"].values

    # Redo again brings back third calc
    state_redo2 = caretaker.redo(state_redo)
    assert "3 ^ 2" in state_redo2["Input"].values

def test_undo_redo_edges():
    caretaker = Caretaker()
    state = pd.DataFrame(columns=["Input", "Result"])

    # No states saved, undo returns same state
    assert caretaker.undo(state).equals(state)
    assert caretaker.redo(state).equals(state)

    caretaker.save_state(state)
    # Undo at first state returns same state
    assert caretaker.undo(state).equals(state)
    # Redo at last state returns same state
    assert caretaker.redo(state).equals(state)
