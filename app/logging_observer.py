from app.logger import logger
from app.observer import Observer

class LoggingObserver(Observer):
    def update(self, message):
        logger.info(f"LoggingObserver received: {message}")
