from genetic_modules.genetic_config import GeneticConfig
from genetic_modules.fitness_function import FitnessFunction


# need a way to 'pipe' things in. i.e DataPipe (preprocess data etc), FitnessFunction, SelectionStrategy, GeneticAlgorithms (crossover, mutation, etc. elitism & padding too?)
class GeneticSystem:
    def __init__(self, config: GeneticConfig, fitness_function: FitnessFunction):
        self.population = [] # genes must be Tuple[bool]

        self.config = config
        self.fitness_function = fitness_function


        self.elite_threshold = int(config.population_size * config.elite_percent)
        self.padding_threshold = config.population_size - int(config.population_size * config.padding_percent)

        # pipe data in , preprocess ? turn into genes for pop


    



    def sort_genes_by_fitness(self):
        self.population.sort(key=lambda g: self.fitness_function.calculate(g), reverse=self.config.maximize_fitness)


    def step(self):
        new_population = self.population[:self.elite_threshold] # copies elite genes over

        

# don't have to re-evaluate genes. fitness_cache must be stored and accessed from multiple places