import numpy as np

def roulette_wheel_selection(population, fitness_scores):
    """Selects an individual using roulette wheel selection (fitness-proportionate)."""         
    total_fitness = sum(fitness_scores)
    selection_probs = [fitness / total_fitness for fitness in fitness_scores]

    return population[np.random.choice(len(population), p=selection_probs)]

def tournament_selection(population, fitness_scores, k=5):
    """Selects an individual through 'k 'rounds where random individuals compete, with the fittest advancing each round."""
    # TODO
    pass

def truncation_selection(population, fitness_scores, proportion=0.5):
    """Randomly selects an individual from the top `proportion` of the population."""
    # Requires sorting population.
    # TODO
    pass

def sus_selection(population, fitness_scores, n=1):
    """Selects `n` individuals using evenly spaced selection points across the fitness distribution."""
    # TODO
    pass

def _sort_population(self):
        """Sorts population by fitness scores."""
        sorted_indices = np.argsort(self.fitness_scores)[::-1]
        self.population = [self.population[i] for i in sorted_indices]
        self.fitness_scores = [self.fitness_scores[i] for i in sorted_indices]