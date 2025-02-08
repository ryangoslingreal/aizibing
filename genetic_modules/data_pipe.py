from typing import Tuple

Gene = Tuple[bool, ...]

# need to define Gene type

# define get_population, update population etc... 
# basically, this class handles dataset input, preprocess (folding)
# need to pass in dataset

# DataHandler? PopulationHandler? ... need a proper name here guys...
class DataPipe:
    def __init__(self, config, create_gene):
        self.population = self.Population(config)

    #def    # function that 'adds' multiple preprocessing functions into 'queue'? 

    class Population:
        def __init__(self, config):
            self.config = config
            self.genes = []

        def add_gene(self, gene):
            # add config checks here? 
            self.genes.append(gene)

        def sort(self):
            self.genes.sort

        def get(self):
            return self.genes

    def load_data(data):
        # sequential pass data thru preprocess functions then load_function then 
        pass

    
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