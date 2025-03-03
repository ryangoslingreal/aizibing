import random

def shuffle_mutate(individual):
    """Randomly shuffles the order of features in the individual."""
    ind = list(individual) 
    random.shuffle(ind)
    return [ind]


def random_mutate(individual, n=1):
    #When mutation is called do we always want it to mutate or just have a chance to mutate?
    """Randomly changes `n` random features in the individual."""
    mutationRate = 1/len(individual)
    ind = list(individual)
    for attribute in individual:
        chance_of_mutation = random.random()
        if (chance_of_mutation < mutationRate):
            ind[attribute] = not(attribute)
        
    return [ind]

def flip_mutate(individual, n=1):
    """Selects two random features and swaps their states `n` times."""
    ind = list(individual)
    
    attribute_1 = round(random.random()*(len(ind)-1))
    attribute_2 = round(random.random()*(len(ind)-1))
    while(attribute_2==attribute_1):
        attribute_2 = round(random.random()*(len(ind)-1))

    for i in range(n):
        one = ind[attribute_1]
        two = ind[attribute_2]
        ind[attribute_1] = two
        ind[attribute_2] = one
        
    return [ind]
