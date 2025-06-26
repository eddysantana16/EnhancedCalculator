import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file contents into environment variables

class CalculatorConfig:
    CALCULATOR_LOG_DIR = None
    CALCULATOR_HISTORY_DIR = None
    CALCULATOR_MAX_HISTORY_SIZE = None
    CALCULATOR_AUTO_SAVE = None
    CALCULATOR_PRECISION = None
    CALCULATOR_MAX_INPUT_VALUE = None
    CALCULATOR_DEFAULT_ENCODING = None
    CALCULATOR_HISTORY_FILE = None
    CALCULATOR_LOG_FILE = None

    @classmethod
    def load(cls):
        cls.CALCULATOR_LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
        cls.CALCULATOR_HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "history")
        cls.CALCULATOR_MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))
        cls.CALCULATOR_AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
        cls.CALCULATOR_PRECISION = int(os.getenv("CALCULATOR_PRECISION", 4))
        cls.CALCULATOR_MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1e6))
        cls.CALCULATOR_DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
        cls.CALCULATOR_HISTORY_FILE = os.getenv("CALCULATOR_HISTORY_FILE", "calc_history.csv")
        cls.CALCULATOR_LOG_FILE = os.getenv("CALCULATOR_LOG_FILE", "calc.log")

        cls.validate()

    @classmethod
    def validate(cls):
        if cls.CALCULATOR_MAX_HISTORY_SIZE <= 0:
            raise ValueError("CALCULATOR_MAX_HISTORY_SIZE must be positive")
        if cls.CALCULATOR_PRECISION < 0:
            raise ValueError("CALCULATOR_PRECISION must be non-negative")
        if cls.CALCULATOR_MAX_INPUT_VALUE <= 0:
            raise ValueError("CALCULATOR_MAX_INPUT_VALUE must be positive")

# Load configuration once at import
CalculatorConfig.load()
