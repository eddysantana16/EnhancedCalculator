from app.logger import logger # pragma: no cover
from app.observer import Observer # pragma: no cover

class LoggingObserver(Observer): # pragma: no cover
    def update(self, message): # pragma: no cover
        logger.info(f"LoggingObserver received: {message}") # pragma: no cover
