import logging
import os
from app.calculator_config import CalculatorConfig

# Ensure log directory exists
os.makedirs(CalculatorConfig.CALCULATOR_LOG_DIR, exist_ok=True)

log_file_path = os.path.join(CalculatorConfig.CALCULATOR_LOG_DIR, "calculator.log")

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("calculator_logger")
