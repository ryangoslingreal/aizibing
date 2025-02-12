from genetic_modules.genetic_config import GeneticConfig
from genetic_modules.fitness_function import FitnessFunction
from genetic_modules.population_stream import PopulationStream

import random

# need a way to 'pipe' things in. i.e DataPipe (preprocess data etc), FitnessFunction, SelectionStrategy, GeneticAlgorithms (crossover, mutation, etc. elitism & padding too?)
class GeneticSystem:
    def __init__(self, config: GeneticConfig, population_stream: PopulationStream, fitness_function: FitnessFunction):
        self.config = config
        self.fitness_function = fitness_function
        self.population_stream = population_stream

        self.rand = random.Random(config.seed) # either pass rand thru or initialise here ? surely here is better - but just means things can't be passed thru that use rand... maybe can pass rand as a param there

        population_stream.initialise(config, fitness_function, self.rand)

        self.elite_threshold = int(config.population_size * config.elite_percent)
        self.padding_threshold = config.population_size - int(config.population_size * config.padding_percent)

        # pipe data in , preprocess ? turn into genes for pop


    def step(self):
        new_population = self.population[:self.elite_threshold] # copies elite genes over

    

# ignore false entries (i.e all attrs selected = 0)




# its 1am way past my bed time soo
# tomorrow, find nice way to plug in selection strategy
# ^ prob just follow similar to fitness_func
# add random select, tournament (with num tournies per selection as arg)
# roulette wheel the best yeah yeah


# this gonna be pretty cool codebase once everything can get plugged in and messed around with separately



# use mypy to check types
# btw, reason im 'typing' is cuz george recommended 'cpython' which is typed python... this might help implementation in future
# also typing is good practice for error checking and documentation etc