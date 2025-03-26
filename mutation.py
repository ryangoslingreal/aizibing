from utils import *
import numpy as np
import random

def shuffle_mutate(individual):
    """Randomly shuffles the order of features in the individual."""

    non_mutated_individual = individual[:]

    while(non_mutated_individual == individual and not all(individual) and not any(individual)):
        random.shuffle(individual)

    return verifyIndividual(individual)


def random_mutate(individual, n=1):
    """Randomly changes `n` random features in the individual."""

    non_mutated_individual = individual[:]

    while(non_mutated_individual == individual):
        gene_indices =  np.random.choice(len(individual), size=n, replace=False)
    
        for gene_index in gene_indices:
            individual[gene_index] = not(individual[gene_index])
            
    return verifyIndividual(individual)

def flip_mutate(individual, n=1):
    """Selects two random features and swaps their states `n` times."""
    
    non_mutated_individual = individual[:]

    while (non_mutated_individual == individual and not all(individual) and any(individual)):
        for _ in range(n):
            gene1, gene2 =  np.random.choice(len(individual), size=2, replace=False)
            individual[gene1], individual[gene2] = individual[gene2], individual[gene1]
            
    return verifyIndividual(individual)