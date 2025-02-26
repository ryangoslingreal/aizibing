import random
def splice_crossover(parent1, parent2):
    """Performs splice crossover between two parents and returns offspring along with splicing details."""
    cut_length = round(len(parent1) * 0.3)  # Ensure at least 1 element is swapped
    start_index = random.randint(0, len(parent1) - cut_length)
    end_index = start_index + cut_length

    # Swap genetic material between parents
    child1 = parent1[:start_index] + parent2[start_index:end_index] + parent1[end_index:]
    child2 = parent2[:start_index] + parent1[start_index:end_index] + parent2[end_index:]


    return child1, child2

def proportional_crossover(parent1, parent2):
        """Performs proportional crossover between two parents and returns offspring."""
        # TODO
        pass