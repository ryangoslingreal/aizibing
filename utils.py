import random
        
def verifyIndividual(individual):
    """Ensuress individual has at least one True value. If all False, randomly set one to True."""
        
    if not any(individual):
        random_index = random.randint(0, len(individual) - 1)
        individual[random_index] = True

    return individual
