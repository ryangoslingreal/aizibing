from abc import ABC, abstractmethod
from typing import Tuple
from functools import cache

# basic super class, use for polymorphism, multiple methods of calculating fitness
class FitnessFunction(ABC):
    # 'centralised' caching - abstracts subclass implementation
    @cache
    def calculate(self, gene: Tuple[bool]) -> float:
        return self._calculate(gene)

    # this method will be implemented in subclass
    @abstractmethod 
    def _calculate(self, gene: Tuple[bool]) -> float:
        pass


# inherit super, so this can be used instead
class DemoFitnessFunction(FitnessFunction):
    def _calculate(self, gene: Tuple[bool]) -> float:
        return sum(gene)
    

# https://docs.python.org/dev/library/functools.html#functools.cache