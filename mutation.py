import numpy as np
import random

def shuffle_mutate(individual):
    """Randomly shuffles the order of features in the individual."""
    from individual import Individual
    original_gene = list(individual.gene)
    mutated_gene = original_gene.copy()
    
    while(mutated_gene == original_gene):
        random.shuffle(mutated_gene)
    
    individual.gene = tuple(mutated_gene)
    individual._fitness = None
    return Individual.verify_individual(individual)


def random_mutate(individual, n=1):
    """Randomly changes `n` random features in the individual."""
    from individual import Individual
    original_gene = list(individual.gene)
    mutated_gene = original_gene.copy()
    
    while(mutated_gene == original_gene):
        gene_indices =  np.random.choice(len(mutated_gene), size=n, replace=False)

        for gene_index in gene_indices:
            mutated_gene[gene_index] = not(mutated_gene[gene_index])
            
    individual.gene = tuple(mutated_gene)
    individual._fitness = None
    return Individual.verify_individual(individual)

def flip_mutate(individual, n=1):
    """Selects two random features and swaps their states `n` times."""
    from individual import Individual
    original_gene = list(individual.gene)
    mutated_gene = original_gene.copy()

    while (mutated_gene == original_gene):
        for _ in range(n):
            gene1, gene2 =  np.random.choice(len(mutated_gene), size=2, replace=False)
            mutated_gene[gene1], mutated_gene[gene2] = mutated_gene[gene2], mutated_gene[gene1]
            
    individual.gene = tuple(mutated_gene)
    individual._fitness = None
    return Individual.verify_individual(individual)