import random

def shuffle_mutate(individual):
    """Randomly shuffles the order of features in the individual."""
    ind = individual 
    random.shuffle(ind)
    return ind


def random_mutate(individual, n=1):
    #When mutation is called do we always want it to mutate or just have a chance to mutate?
    """Randomly changes `n` random features in the individual."""
    mutationRate = 1/len(individual)
    ind = individual
    for attribute in individual:
        chance_of_mutation = random.random()
        if (chance_of_mutation < mutationRate):
            ind[attribute] = not(attribute)
        
    return ind

def flip_mutate(individual, n=1):
    """Selects two random features and swaps their states `n` times."""
    attribute_1 = round(random.random()*(len(individual)-1))
    attribute_2 = round(random.random()*(len(individual)-1))
    while(attribute_2==attribute_1):
        attribute_2 = round(random.random()*(len(individual)-1))

    for i in range(n):
        one = individual[attribute_1]
        two = individual[attribute_2]
        individual[attribute_1] = two
        individual[attribute_2] = one
        
    return individual
