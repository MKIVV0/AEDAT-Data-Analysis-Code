from datetime import date
from .assignment import Assignment
from typing import Optional


class NoiseCharacterization(Assignment):
    _instance: Optional['NoiseCharacterization'] = None

    def __new__(cls, assignment_date: date) -> 'NoiseCharacterization':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, assignment_date: date) -> None:
        if not hasattr(self, 'initialized'):
            super().__init__(assignment_date)
            self.initialized = True
