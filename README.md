# Enhanced Calculator

A professional command-line calculator built in Python.

## Features

- Comprehensive Operations: Supports addition, subtraction, multiplication, division, power, root modulus, integer division, percentage, and absolute difference.
- REPL Interface: Interactive command-line interface with support for calculation and utility commands (undo, redo, history, save, load, clear, help, exit).
- Undo/Redo Support: Implements the Memento Pattern to revert or reapply calculations.
- Logging & Auto-Save: Observer Pattern used to log calculations and auto-save history to CSV files.
- Configuration Management: Uses a .env file to manage settings like history size, precision, max input, and file paths.
- Robust Error Handling: Custom exceptions and input validation ensure stability and user guidance.
- History Persistence: Saves and loads calculation history using pandas.
- Unit Testing: 90%+ test coverage with pytest; includes edge cases and REPL behavior.
- Design Patterns: Includes Factory, Memento, and Observer patterns.
- CI/CD: GitHub Actions workflow runs tests, enforces coverage, and uploads coverage reports.

## Installation

git clone https://github.com/eddysantana16/EnhancedCalculator.git

cd EnhancedCalculator

pip install -r requirements.txt

## Create a Virtual environment

python -m venv venv

venv\Scripts\activate (# On Windows)

source venv/bin/activate  (# On Mac/Linux)

## Install dependencies

pip install -r requirements.txt

## Run the calculator REPL from the terminal

python main.py

## Example Command Inputs

- add 2 3 - addition
- subtract 5 1 – Subtraction
- multiply 4 6 – Multiplication
- divide 10 2 – Division
- power 2 3 – Exponentiation
- root 27 3 – nth Root
- modulus 10 3 – Modulo operation
- int_divide 9 2 – Integer division
- percent 50 200 – Percentage calculation
- abs_diff 10 6 – Absolute difference

- undo – Undo the last operation
- redo – Redo the last undone operation
- history – View calculation history
- save – Save history to file
- load – Load history from file
- clear – Clear history
- help – Show help menu
- exit or quit – Exit the calculator

## Running tests

- pytest 
- pytest --cov=app tests/

## Project Structure

EnhancedCalculator/
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator_config.py
|   ├── calculator_factory.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
|   ├── logger.py
|   ├── logging_observer.py
│   ├── observer.py
│   ├── operations.py
├── history/
├── logs/
├── tests/
|   ├── __init__.py
│   ├── test_calculation.py
│   ├── test_calculator_config.py
│   ├── test_calculator_memento.py
│   ├── test_calculator_repl.py
│   ├── test_coverage_additional.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_input_validators.py
│   ├── test_observer.py
│   ├── test_operations.py
├── .coverage
├── .env
├── .gitignore
├── config.json
├── main.py
├── README.md
├── requirements.txt

## License 

This project is licensed under MIT License

## Author

Eddy Santana