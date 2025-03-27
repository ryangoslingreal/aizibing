import random
import os
import time

        
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


def output_result(best_individuals, feature_names, dataset_name, fitness_function_name, elapsed_time):
    import os

    safe_name = dataset_name.lower().replace(" ", "_")
    filename = f"{safe_name}_{fitness_function_name}_results.txt"
    file_path = os.path.join(os.getcwd(), filename)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"📊 Best features per generation for '{dataset_name}'\n")
        f.write(f"🔧 Classifier used: {fitness_function_name}\n")
        f.write(f"⏱️ Time taken: {elapsed_time:.2f} seconds\n")

        for i, individual in enumerate(best_individuals):
            selected = get_selected_feature_names(individual, feature_names)
            f.write(f"\nGeneration {i} ({len(selected)} features):\n")
            for name in selected:
                f.write(f" - {name}\n")

    print(f"\n✅ Feature log saved to: {file_path}")
    print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")

