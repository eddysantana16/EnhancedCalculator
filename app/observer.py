from abc import ABC, abstractmethod
from app.logger import logger
from app.history import CalculationHistory
from app.calculator_config import CalculatorConfig

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class LoggingObserver(Observer):
    def update(self, message):
        logger.info(f"Calculation performed: {message}")

class AutoSaveObserver(Observer):
    def __init__(self, history: CalculationHistory):
        self.history = history

    def update(self, message):
        if CalculatorConfig.CALCULATOR_AUTO_SAVE:
            self.history.save()
            logger.info("History auto-saved after operation.")
