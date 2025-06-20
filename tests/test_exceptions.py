import pytest
from app.exceptions import CalculatorError, ConfigurationError

def test_calculator_error():
    with pytest.raises(CalculatorError) as excinfo:
        raise CalculatorError("Test calculator error")
    assert "Test calculator error" in str(excinfo.value)

def test_configuration_error():
    with pytest.raises(ConfigurationError) as excinfo:
        raise ConfigurationError("Test config error")
    assert "Test config error" in str(excinfo.value)
