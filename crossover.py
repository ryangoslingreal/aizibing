from random import random


def splice_crossover(parent1, parent2):
    """Performs splice crossover between two parents and returns offspring."""
    # cut length = to 30% of the parent
    # TODO
    cut_length = len(parent1) * .3
    start_index = random.randint(0, len(parent1) - cut_length)
    end_index = start_index + cut_length

    splt_1 = parent1[start_index:end_index]
    splt_2 = parent2[start_index:end_index]

    child1 = parent1[:start_index] + splt_1 + parent1[end_index:]
    child2 = parent2[:start_index] + splt_2 + parent2[end_index:]

    return child1, child2

    pass

def proportional_crossover(parent1, parent2):
    """Performs proportional crossover between two parents and returns offspring."""
    # TODO
    pass