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





file = "german_credit_gaussian_nb_results.txt"
plot_all(file)
