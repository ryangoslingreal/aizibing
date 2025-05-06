import random

class Individual:
    def __init__(self, gene):
        self.gene = tuple(gene)
        self.fitness = None
    
    @staticmethod
    def verify_individual(individual):
        """Ensures individual has at least one True value. If all False, randomly set one to True."""
        
        gene = list(individual.gene)
        if not any(gene):
            random_index = random.randint(0, len(gene) - 1)
            gene[random_index] = True

        return Individual(gene)