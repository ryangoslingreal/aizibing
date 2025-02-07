from abc import ABC, abstractmethod
from typing import Tuple

# basic super class, use for polymorphism, multiple methods of calculating fitness
class FitnessFunction(ABC):
    @abstractmethod
    def calculate(self, gene: Tuple[bool]) -> float:
        pass


# inherit super, so this can be used instead
class DemoFitnessFunction(FitnessFunction):
    def calculate(self, gene: Tuple[bool]) -> float:
        return sum(gene)
    

# need to find way to cache here
# https://docs.python.org/dev/library/functools.html#functools.cache