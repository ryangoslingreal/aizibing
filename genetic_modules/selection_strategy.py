from abc import ABC, abstractmethod
from typing import Tuple, List # List[Gene] is population
import random

from genetic_modules.genetic_config import GeneticConfig
from genetic_modules.population_stream import PopulationStream

Gene = Tuple[bool, ...]

# pass datapipe in from init ?, so can get population piped in without having to pass it every call

class SelectionStrategy(ABC):
    def __init__(self):
        pass

    def initialise(self, stream):
        self.stream = stream
        self.population = stream.get()
        self.config = stream.config
        self.rand = stream.rand

    @abstractmethod
    def select(self) -> Gene:
        pass


class RandomSelection(SelectionStrategy):
    def select(self) -> Gene:
        return self.rand.choice(self.population.get())


class TournamentSelection(SelectionStrategy):
    def select(self, population: List[Gene]) -> Gene:
        return self.rand.choice(population)


class RouletteSelection(SelectionStrategy):
    def select(self, population: List[Gene]) -> Gene:
        pass

    

# here defining specific selection methods is okay
# you wouldnt want the user to write roulette wheel implementation in their main.py - they can just select a working preset
# however, maybe we should accommodate for this? (can just implement 'CustomSelection' class)