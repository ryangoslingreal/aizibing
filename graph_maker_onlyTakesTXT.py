import matplotlib.pyplot as plt
import re


def plot_accuracy_over_generations(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    generations = []
    accuracies = []

    for line in lines:
        match = re.match(r"Generation (\d+).*?\| Accuracy: ([0-9.]+)", line)
        if match:
            gen = int(match.group(1))
            acc = float(match.group(2))
            generations.append(gen)
            accuracies.append(acc)

    plt.figure(figsize=(10, 6))
    plt.plot(generations, accuracies, marker='o', linestyle='-', color='blue')
    plt.title("Best Individual Accuracy per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_feature_count_over_generations(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    generations = []
    feature_counts = []

    for line in lines:
        match = re.match(r"Generation (\d+) \((\d+) features\)", line)
        if match:
            gen = int(match.group(1))
            count = int(match.group(2))
            generations.append(gen)
            feature_counts.append(count)

    plt.figure(figsize=(10, 6))
    plt.plot(generations, feature_counts, marker='o', linestyle='-', color='green')
    plt.title("Number of Features per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Number of Features")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_duration_per_generation(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    avg_duration = None
    gen_count = 0

    for line in lines:
        match = re.match(r"Generation (\d+)", line)
        if match:
            gen_count = max(gen_count, int(match.group(1)) + 1)

        time_match = re.match(r"📈 Avg time per generation: ([0-9.]+)", line)
        if time_match:
            avg_duration = float(time_match.group(1))

    if avg_duration is None or gen_count == 0:
        print("⚠️ Duration data not found in file.")
        return

    durations = [avg_duration] * gen_count
    generations = list(range(gen_count))

    plt.figure(figsize=(10, 6))
    plt.plot(generations, durations, marker='o', linestyle='--', color='purple')
    plt.title("Average Time per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Seconds")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_all(file_path):
    plot_accuracy_over_generations(file_path)
    plot_feature_count_over_generations(file_path)
    plot_duration_per_generation(file_path)
import os
import matplotlib.pyplot as plt
import re

def parse_result_file(file_path):
    """Extracts generation-wise accuracy, feature count, and duration."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    generations = []
    accuracies = []
    feature_counts = []
    avg_time = None

    for line in lines:
        gen_match = re.match(r"Generation (\d+)", line)
        acc_match = re.match(r"Generation (\d+).*?\| Accuracy: ([0-9.]+)", line)
        feat_match = re.match(r"Generation (\d+) \((\d+) features\)", line)
        time_match = re.match(r"📈 Avg time per generation: ([0-9.]+)", line)

        if acc_match:
            generations.append(int(acc_match.group(1)))
            accuracies.append(float(acc_match.group(2)))
        if feat_match:
            feature_counts.append(int(feat_match.group(2)))
        if time_match:
            avg_time = float(time_match.group(1))

    durations = [avg_time] * len(generations) if avg_time else []

    return generations, accuracies, feature_counts, durations

def plot_multiple_metrics(file_list):
    all_accuracies = {}
    all_features = {}
    all_durations = {}

    for file in file_list:
        name = os.path.basename(file).replace(".txt", "")
        classifier_name = "_".join(name.split("_")[2:-1])  # extracts full classifier name between dataset and 'results'
        generations, acc, feats, times = parse_result_file(file)

        if acc:
            all_accuracies[classifier_name] = (generations, acc)
        if feats:
            all_features[classifier_name] = (generations, feats)
        if times:
            all_durations[classifier_name] = (generations, times)

    # Plot accuracy
    plt.figure(figsize=(10, 6))
    for clf, (gens, accs) in all_accuracies.items():
        plt.plot(gens, accs, label=clf)
    plt.title("Accuracy per Generation for Each Classifier")
    plt.xlabel("Generation")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot durations
    plt.figure(figsize=(10, 6))
    for clf, (gens, times) in all_durations.items():
        plt.plot(gens, times, label=clf)
    plt.title("Avg Duration per Generation for Each Classifier")
    plt.xlabel("Generation")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot feature counts
    plt.figure(figsize=(10, 6))
    for clf, (gens, feats) in all_features.items():
        plt.plot(gens, feats, label=clf)
    plt.title("Number of Features per Generation for Each Classifier")
    plt.xlabel("Generation")
    plt.ylabel("Number of Features")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()






files = [
    "iris_gaussian_nb_results.txt",
    "iris_bernoulli_nb_results.txt",
    "german_credit_gaussian_nb_results.txt",
    "german_credit_decision_tree_results.txt"
]

plot_multiple_metrics(files)
