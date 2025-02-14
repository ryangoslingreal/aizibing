from abc import ABC, abstractmethod
from typing import Tuple, List # List[Gene] is population
import random

from genetic_modules.genetic_config import GeneticConfig
from genetic_modules.population_stream import PopulationStream

Gene = Tuple[bool, ...]

# pass datapipe in from init ?, so can get population piped in without having to pass it every call

class SelectionStrategy(ABC):
    def __init__(self, config: GeneticConfig, rng: random.Random): # pass PopStream thru here
        self.rng = rng

    @abstractmethod
    def select(self, population: List[Gene]) -> Gene:
        pass


# p1, p2 = self.rand.choices(genes, k=2) ... also population shouldnt be passed thru these funcs, maybe implement k=1 default val
class RandomSelection(SelectionStrategy):
    def select(self, population: List[Gene]) -> Gene:
        return self.rng.choice(population)


class TournamentSelection(SelectionStrategy):
    def select(self, population: List[Gene]) -> Gene:
        return self.rng.choice(population)


class RouletteSelection(SelectionStrategy):
    def select(self, population: List[Gene]) -> Gene:
        pass

    

# here defining specific selection methods is okay
# you wouldnt want the user to write roulette wheel implementation in their main.py - they can just select a working preset
# however, maybe we should accommodate for this? (can just implement 'CustomSelection' class)