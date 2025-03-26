import numpy as np

def roulette_wheel_selection(population, fitness_scores, allow_cloning=True):
    """Selects two parents using roulette wheel selection (fitness-proportionate), ensuring uniqueness if required."""
      
    total_fitness = sum(fitness_scores)
    selection_probs = [fitness / total_fitness for fitness in fitness_scores]

    # Select two parents
    parent_indices =  np.random.choice(len(population), size=2, p=selection_probs, replace=allow_cloning)
    
    return population[parent_indices[0]], population[parent_indices[1]]

def tournament_selection(population, fitness_scores, k=5, allow_cloning=True):
    """Selects two parents using two tournaments to find the fittest individual from 'k' tournament size."""
    
    def tournament_round():
        competitors = np.random.choice(len(population), size=k, replace=allow_cloning)
        best = max(competitors, key = lambda x: fitness_scores[x])
        return population[best]
        
    return tournament_round(), tournament_round()

def truncation_selection(population, fitness_scores, proportion=0.5, allow_cloning=True):
    """Randomly selects an individual from the top `proportion` of the population."""
    
    # Requires sorting population.
    # TODO
    pass

def sus_selection(population, fitness_scores, n=1, allow_cloning=True):
    """Selects `n` individuals using evenly spaced selection points across the fitness distribution."""
    
    # TODO
    pass