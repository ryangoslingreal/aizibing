from sklearn.datasets import load_iris
from sklearn.utils import Bunch
import numpy as np
import random
import os

        
def verifyIndividual(individual):
    """Ensuress individual has at least one True value. If all False, randomly set one to True."""
        
    if not any(individual):
        random_index = random.randint(0, len(individual) - 1)
        individual[random_index] = True

    return individual

def get_selected_feature_names(individual, feature_names):
    return [name for name, selected in zip(feature_names, individual) if selected]

def print_name_from_best(best_per_gen, feature_names):
    for i, individual in enumerate(best_per_gen):
        selected = get_selected_feature_names(individual, feature_names)
        print(f"\nGeneration {i} ({len(selected)} features):")
        for name in selected:
            print(" -", name)



def output_result(best_individuals, feature_names, dataset_name):
    """
    Saves best individual features from each generation to a file in the project root.
    """
    safe_name = dataset_name.lower().replace(" ", "_")
    filename = f"{safe_name}_results.txt"
    file_path = os.path.join(os.getcwd(), filename)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"📊 Best features per generation for '{dataset_name}'\n\n")
        for i, individual in enumerate(best_individuals):
            selected = get_selected_feature_names(individual, feature_names)
            f.write(f"Generation {i} ({len(selected)} features):\n")
            for name in selected:
                f.write(f" - {name}\n")
            f.write("\n")

    print(f"\n✅ Feature log saved to: {file_path}")
    
def load_iris_with_noise(n):
    """Load iris dataset and adds `n` columns of noise to features."""
    iris = load_iris()
    X = iris.data
    y = iris.target

    noise = np.random.randn(X.shape[0], n)
    X_noisy = np.hstack((X, noise))

    return Bunch(data=X_noisy, target=y, feature_names=iris.feature_names + [f"noise_{i+1}" for i in range(n)])