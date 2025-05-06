from individual import Individual

import numpy as np
import math

def roulette_wheel_selection(population, allow_cloning=True):
    """Selects two parents using roulette wheel selection (fitness-proportionate), ensuring uniqueness if required."""
      
    total_fitness = sum(ind.fitness for ind in population)
    selection_probs = [ind.fitness / total_fitness for ind in population]

    # Select two parents
    parent_indices =  np.random.choice(len(population), size=2, p=selection_probs, replace=allow_cloning)
    
    return population[parent_indices[0]], population[parent_indices[1]]

def tournament_selection(population, k=5, allow_cloning=True):
    """Selects two parents using two tournaments to find the fittest individual from 'k' tournament size."""
    
    def tournament_round():
        competitors = np.random.choice(len(population), size=k, replace=allow_cloning)
        best = max(competitors, key = lambda x: population[x].fitness)
        return population[best]
        
    return tournament_round(), tournament_round()

def truncation_selection(population, proportion=0.5, allow_cloning=True):
    """Randomly selects an individual from the top `proportion` of the population."""
    
    min_pop = math.ceil(len(population) * proportion)

    def select_individual():
        return np.random.choice(population[:min_pop], replace = allow_cloning)
    
    return select_individual(), select_individual()

def sus_selection(population, n=1, allow_cloning=True):
    """Selects `n` individuals using evenly spaced selection points across the fitness distribution."""
    
    # TODO
    pass