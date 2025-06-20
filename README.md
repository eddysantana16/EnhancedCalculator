# Enhanced Calculator

A professional command-line calculator built in Python.

## Features

- Basic operations: +, -, *, /, ^, root
- Command-line REPL interface
- Calculation history saved to CSV
- Undo/Redo functionality
- Configurable settings
- Input validation and error handling
- Full test coverage with "pytest"

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

## Example Inputes

> 2 + 3, 
> 4 * 5,
> undo,
> help,
> exit

## Running tests

pytest --cov=app tests/

## Project Structure

EnhancedCalculator/
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── observer.py
│   ├── operations.py
├── tests/
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