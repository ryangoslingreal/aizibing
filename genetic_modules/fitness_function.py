from abc import ABC, abstractmethod
from typing import Tuple
from functools import cache

Gene = Tuple[bool, ...]

# basic super class, use for polymorphism, multiple methods of calculating fitness
class FitnessFunction(ABC):    
    # 'centralised' caching - abstracts subclass implementation
    @cache
    def calculate(self, gene: Gene) -> float:
        return self._calculate(gene)

    # this method will be implemented in subclass
    @abstractmethod 
    def _calculate(self, gene: Gene) -> float:
        pass


# inherit super, so this can be used instead
class DemoFitnessFunction(FitnessFunction):
    def _calculate(self, gene: Gene) -> float:
        return sum(gene)
    

# instead of making multiple different classes here,
# how about just one class, which, __init__ is given the fitness function from notebook, then calculate (being cached) just calls that

# could implement __call__, so itll look like fitness_function(gene) instead of fitness_function.calculate(gene) .. just future thing to think about
    

# https://docs.python.org/dev/library/functools.html#functools.cache