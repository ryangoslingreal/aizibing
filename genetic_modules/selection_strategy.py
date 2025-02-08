from abc import ABC, abstractmethod
from typing import List # List[Gene] is population
import random

from data_pipe import Gene

# pass datapipe in from init ?, so can get population piped in without having to pass it every call


class SelectionStrategy(ABC):
    def __init__(self, rng: random.Random):
        self.rng = rng

    @abstractmethod
    def select(self, population: List[Gene]) -> Gene:
        pass


class RandomSelection(SelectionStrategy):
    def select(self, population: List[Gene]) -> Gene:
        return self.rng.choice(population)