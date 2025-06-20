class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass

class InvalidInputError(CalculatorError):
    """Exception raised for invalid user inputs."""
    pass

class ConfigurationError(CalculatorError):
    """Exception raised for configuration related errors."""
    pass

class DivisionByZeroError(CalculatorError):
    """Exception raised when division by zero occurs."""
    pass
class CalculationError(Exception):
    """Custom exception for calculation errors."""
    pass
