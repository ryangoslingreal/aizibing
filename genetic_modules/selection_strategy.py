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
        self.fitness = stream.fitness_function

    @abstractmethod
    def select(self) -> Gene:
        pass


class RandomSelection(SelectionStrategy):
    def select(self) -> Gene:
        return self.rand.choice(self.population.get())



class TournamentSelection(SelectionStrategy):
    def select(self) -> Gene:
        genes = self.population.get()

        champ = self.rand.choice(genes)

        for _ in range(self.config.tournament_rounds):
            contender = self.rand.choice(genes)

            if self.fitness(contender) > self.fitness(champ):
                champ = contender

        return champ



class RouletteSelection(SelectionStrategy):
    def select(self) -> Gene:
        genes = self.population.get()

        total_score = sum(self.fitness(gene) for gene in genes)

        threshold = self.rand.uniform(0, total_score)

        fitness = 0
        for gene in genes:
            fitness += self.fitness(gene)
            if fitness >= threshold:
                return gene
            
        return None # shouldn't ever happen



class StochasticUniversalSampling(SelectionStrategy):
    def select(self) -> Gene:
        pass


# implement: 
# https://en.wikipedia.org/wiki/Selection_(evolutionary_algorithm)
# https://en.wikipedia.org/wiki/Reward-based_selection
    

# here defining specific selection methods is okay
# you wouldnt want the user to write roulette wheel implementation in their main.py - they can just select a working preset
# however, maybe we should accommodate for this? (can just implement 'CustomSelection' class)