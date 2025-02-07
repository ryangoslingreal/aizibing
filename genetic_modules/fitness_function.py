from abc import ABC, abstractmethod
from typing import List

# basic super class, use for polymorphism, multiple methods of calculating fitness
class FitnessFunction(ABC):
    @abstractmethod
    def calculate(self, gene: List[bool]) -> float:
        pass


# inherit super, so this can be used instead
class DemoFitnessFunction(FitnessFunction):
    def calculate(self, gene: List[bool]) -> float:
        return sum(gene)