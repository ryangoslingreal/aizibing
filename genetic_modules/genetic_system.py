from genetic_modules.genetic_config import GeneticConfig
from genetic_modules.fitness_function import FitnessFunction
from genetic_modules.population_stream import PopulationStream
from genetic_modules.selection_strategy import SelectionStrategy

import random

# need a way to 'pipe' things in. i.e DataPipe (preprocess data etc), FitnessFunction, SelectionStrategy, GeneticAlgorithms (crossover, mutation, etc. elitism & padding too?)
class GeneticSystem:
    def __init__(self, config: GeneticConfig, fitness_function: FitnessFunction, selection_strategy: SelectionStrategy, population_stream: PopulationStream = PopulationStream()):
        self.config = config
        self.fitness_function = fitness_function.calculate
        self.stream = population_stream

        self.rand = random.Random(config.seed)

        # initialise population
        self.population = population_stream.initialise(config, fitness_function.calculate, self.rand)

        # initialise chosen selection strategy
        selection_strategy.initialise(population_stream)
        self.select = selection_strategy.select
        self.nselect = lambda n: [self.select() for _ in range(n)]

        # config inferences
        self.elite_threshold = int(config.population_size * config.elite_percent)
        self.padding_threshold = config.population_size - int(config.population_size * config.padding_percent)


    def step(self):
        genes = self.population.get()
        new_genes = genes[:self.elite_threshold] # copies elite genes over
        
        for _ in range(self.elite_threshold, self.padding_threshold):
            # perform selection
            p1, p2 = self.nselect(2)

            # perform crossover
            crossover_point = self.rand.randint(0,self.config.gene_length)
            child = p1[:crossover_point] + p2[crossover_point:] # okay python is pretty cool


            new_genes.append(child)

        # pad genes
        new_genes[self.padding_threshold:self.config.population_size] = [self.stream.random_gene()]

        self.population.set_genes(new_genes)
        self.population.sort() # sorting at end confirms fitness is cached (and at end of train, pop is sorted.)


    def train(self, n_generations):
        for i in range(n_generations):
            # add 'verbose' ? output avg fitness per gen ? debugging stuff
            self.step()
    


# create info() function? output stored data 

# vvv Output Gene
# print(''.join(['1' if g else '0' for g in gene]), gs.fitness_function.calculate(gene))

# to-do , plug in selection_strategy , crososver etc... 
# GeneticSystem initialisation is getting kinda ugly so think of better way maybe..
# create CustomFitnessFunction ! and sort out that entire module

# i need to delete all these ugly comments!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# implement reps & folds tho

# ignore edge case where gene = only 0s

# mypy typing?