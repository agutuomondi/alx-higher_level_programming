#!/usr/bin/python3
from abc import ABC, abstractmethod
class BaseGeometry(ABC):
    @abstractmethod
    def area(self):
        """Abstract method for calculating area."""
        pass
