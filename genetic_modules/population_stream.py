from typing import Tuple, List

from genetic_modules.fitness_function import FitnessFunction

Gene = Tuple[bool, ...] # in future, create a Gene class (for more customisation)

# define get_population, update population etc... 
# basically, this class handles dataset input, preprocess (folding)
# need to pass in dataset

# preprocess data, generate genes (need processing), 
# implement n-fold cross validation (NFold from sklearn?)

class PopulationStream:
    def __init__(self, create_gene = None):
        self.population = self.Population(self)

    def random_gene(self):
        return tuple(self.rand.choice([True, False]) for _ in range(self.config.gene_length))

    def initialise(self, config, fitness_function, rand):
        self.config = config
        self.fitness_function = fitness_function
        self.rand = rand

        # generate genes randomly - may need to pass this as a param
        for _ in range (config.population_size):
            self.population.add_gene(self.random_gene())

        self.population.sort()
        return self.population


    #def    # function that 'adds' multiple preprocessing functions into 'queue'? 

    class Population:
        def __init__(self, stream): # can't give 'stream' type here. need to forward declare , pass genes through
            self.stream = stream
            self.genes: List[Gene] = []

        def set_genes(self, genes: List[Gene]):
            self.genes = genes

        def add_gene(self, gene: Gene):
            # add config checks here? 
            self.genes.append(gene)

        def sort(self): # check for fitness_function ? 
            self.genes.sort(key=lambda g: self.stream.fitness_function.calculate(g), reverse=self.stream.config.maximize_fitness)

        # find 'hamming distance' (diversity of population) --- basically exploration vs exploitation --- to reduce computation, 'sample' population to get rough estimate of diversity ... target a certain value of diversity
        # def diversity(self):

        def get(self) -> List[Gene]:
            return self.genes

    def load_data(data):
        # sequential pass data thru preprocess functions then load_function then 
        pass

    def get(self) -> Population:
        return self.population

    
# need to figure out how to do this module
# - load data into pipe


# i have an idea
'''
basically, DataPipe is main class,
inside has a nested Population class

Population is 'loaded' once preprocessing etc has been done in DataPipe
multiple DataPipe instances (to handle different datasets)
OR, just make it a 'manager' - i.e pass functions into DataPipe from notebook
which basically would do what the subclasses would do - i.e 'offload' the preprocessing to main notebook - so more easy to configure

and also means dont have to edit this file once its setup at all
'''