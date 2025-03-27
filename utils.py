import random
        
def verifyIndividual(individual):
    """Ensuress individual has at least one True value. If all False, randomly set one to True."""
        
    if not any(individual):
        random_index = random.randint(0, len(individual) - 1)
        individual[random_index] = True

    return individual

def get_selected_feature_names(individual, feature_names):
    """
    Given a boolean mask (individual) and feature_names,
    return the names of the selected features.
    """
    return [name for name, selected in zip(feature_names, individual) if selected]

def print_best_features_per_generation(best_individuals, feature_names):
    """
    Prints the selected feature names for each generation's best individual.
    """
    print("\nBest features per generation:")
    for i, individual in enumerate(best_individuals):
        selected = get_selected_feature_names(individual, feature_names)
        print(f"\nGeneration {i} ({len(selected)} features):")
        for name in selected:
            print(" -", name)
