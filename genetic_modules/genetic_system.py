from genetic_modules.genetic_config import GeneticConfig
from genetic_modules.fitness_function import FitnessFunction


# need a way to 'pipe' things in. i.e DataPipe (preprocess data etc), FitnessFunction, SelectionStrategy, GeneticAlgorithms
class GeneticSystem:
    def __init__(self, config: GeneticConfig, fitness_function: FitnessFunction):
        self.population = []
        self.fitness_cache = []