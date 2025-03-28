from sklearn.model_selection import StratifiedKFold
import numpy as np

from functools import cache
import concurrent.futures  # multi-threading

# for feature names and outputting result
from utils import *
from load_a_dataset import *


class GeneticAlgorithm:
    def __init__(self, data):
        """Initializes the genetic algorithm with population-based feature selection."""

        self.data = data
        self.population = []
        self.fitness_scores = []
        self.best_per_gen = []

        # Define crossover thresholds
        self.elite_size = int(params.ELITE_RATE * params.POPULATION)
        self.padding_size = int(params.PADDING_RATE * params.POPULATION)
        self.breeding_size = params.POPULATION - self.padding_size - self.elite_size

        # Preprocess dataset
        self.X, self.y = data.data, data.target
        self.attributes = self.X.shape[1]
        self.rep_folds = self.generateNFolds(self.X, self.y, params.REPETITIONS, params.FOLDS)

        # Compute baseline fitness
        baseline_fitness = self.rep_individual_parallel(tuple([True for _ in range(self.attributes)]))
        print(f"Baseline fitness: {baseline_fitness}")

        for g in range(params.GENERATIONS):
            print(f"\n--- Generation {g} ---")
            self.step()

        self.sort_population()

    # returns top 'n' unique individuals of population, so you can see what columns they use - FIX THIS
    def unique_head(self, n=5):
        unique_individuals = []
        seen_individuals = set()  # track unique individuals

        for i, (individual, fitness) in enumerate(zip(self.population, self.fitness_scores)):
            individual_tuple = tuple(individual)  # make individual hashable

            # if unique
            if individual_tuple not in seen_individuals:
                seen_individuals.add(individual_tuple)
                unique_individuals.append(individual)

            if len(unique_individuals) >= n:
                break

        return unique_individuals

    def step(self):
        self.pad_population()

        self.fitness_scores = self.evaluate_population_parallel()

        self.sort_population()
        self.best_per_gen.append(self.population[0])  # storing top individual to list for resulting feature name

        for i, (individual, fitness) in enumerate(zip(self.population, self.fitness_scores)):
            print(f"Position {i}: {individual}    Fitness: {fitness}")
            break  # just output best individual

        # Extract breeding population
        breeding_pool = self.population[:self.breeding_size + self.elite_size]
        breeding_pool_fitness = self.fitness_scores[:self.breeding_size + self.elite_size]

        next_population = []

        # Until breeding threshold reached
        while len(next_population) < self.breeding_size:
            # Choose two unique parents if ALLOW_CLONING = False
            parent1, parent2 = params.SELECTION(breeding_pool, breeding_pool_fitness, params.ALLOW_CLONING)

            # If ALLOW_CLONING = True and MUTATE_ON_CLONE = True, mutate
            # Else, crossover
            if parent1 == parent2 and params.MUTATE_ON_CLONE:
                offspring = params.MUTATION(parent1)
            else:
                offspring = params.CROSSOVER(parent1, parent2)

            next_population.append(offspring)

        # Apply basic mutation rate
        for i, individual in enumerate(next_population):
            if random.random() < params.MUTATION_RATE:
                next_population[i] = params.MUTATION(individual)

        # Elite carry over
        next_population.extend(self.population[:self.elite_size])

        # Reset population for next generation cycle        
        self.population = next_population
        self.fitness_scores = []

    def sort_population(self):
        """Sorts population by fitness scores."""

        sorted_indices = np.argsort(self.fitness_scores)[::-1]
        self.population = [self.population[i] for i in sorted_indices]
        self.fitness_scores = [self.fitness_scores[i] for i in sorted_indices]

    def pad_population(self):
        """Ensures the population remains at POPULATION by adding new individuals if necessary."""

        difference = params.POPULATION - len(self.population)
        if difference > 0:
            self.population += self.generateIndividuals(difference, self.attributes)

    def evaluate_population(self):
        """Evaluates the fitness of all individuals in the population and stores their scores."""

        fitness_scores = np.zeros(params.POPULATION)

        # Individual loop
        for i, individual in enumerate(self.population):
            # Convert to tuple for caching
            fitness_scores[i] = self.rep_individual(tuple(individual))

        return fitness_scores

    def evaluate_population_parallel(self):
        """Evaluates fitness of all individuals using multi-threading."""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            fitness_scores = list(executor.map(self.rep_individual_parallel, [tuple(ind) for ind in self.population]))

        return fitness_scores

    @cache
    def rep_individual_parallel(self, individual):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            rep_fitness = list(
                executor.map(self.evaluate_rep, [individual] * params.REPETITIONS, range(params.REPETITIONS)))

        return np.mean(rep_fitness)

    # this function and above basically does rep_individual
    def evaluate_rep(self, individual, r):
        return np.mean(
            [self.evaluate_individual(individual, train_idx, test_idx) for train_idx, test_idx in self.rep_folds[r]])

    @cache
    def rep_individual(self, individual):
        """Computes the average fitness of an individual across multiple repetitions and caches result."""

        rep_fitness = []

        # Rep loop
        for r in range(params.REPETITIONS):
            # Fold loop
            fold_fitness = [
                self.evaluate_individual(individual, train_idx, test_idx)
                for train_idx, test_idx in self.rep_folds[r]
            ]

            # Calculate average fitness across all folds
            rep_fitness.append(np.mean(fold_fitness))

        # Calculate average fitness across all reps
        return np.mean(rep_fitness)

    def evaluate_individual(self, individual, train_idx, test_idx):
        """Applies individual attribute mask and evaluates an individual using the specified fitness function."""

        # Apply attribute mask
        X_train, X_test = self.X[train_idx][:, individual], self.X[test_idx][:, individual]
        y_train, y_test = self.y[train_idx], self.y[test_idx]

        # Train
        return params.FITNESS(X_train, y_train, X_test, y_test)

    @staticmethod
    def generateIndividuals(count, attributes):
        """Generates a specified number of random individuals."""

        population = []
        for _ in range(count):
            # Generate random individual
            # Ensure individual is valid
            # If so, regenerate
            while True:
                individual = [random.choice([True, False]) for _ in range(attributes)]
                if any(individual):
                    break

            population.append(individual)

        return population

    @staticmethod
    def generateNFolds(X, y, rep, fold):
        """Generates stratified k-fold splits for cross-validation."""

        rep_folds = {}
        for r in range(rep):
            skf = StratifiedKFold(n_splits=fold, shuffle=True, random_state=(42 + r))
            rep_folds[r] = list(skf.split(X, y))

        return rep_folds


if __name__ == "__main__":
    iris = load_iris()
    breast = load_breast_cancer()
    indian_pine = load_indian_pines()
    german_credit = load_german_credit()

    # Set seed for reproducibility
    # seed = 42
    # np.random.seed(seed)
    # num_samples = 1000
    # random_indices = np.random.choice(indian_pine.data.shape[0], num_samples, replace=False)
    # indian_pine.data = indian_pine.data[random_indices]
    # indian_pine.target = indian_pine.target[random_indices]

from fitness import (
    gaussian_nb,
    bernoulli_nb,
    multinomial_nb,
    xgboost_classifier,
    knn_classifier,
    hinge_loss,
    svm_classifier,
    decision_tree,
    random_forest,
    gradient_boosting_classifier,
    adaboost_classifier,
    mlp_classifier
)
from config import params
from utils import output_result  # if this is your visualization/logging function

ds_data = german_credit
ds_name = 'german_credit'

fitness_functions = [
    gaussian_nb,
    bernoulli_nb,
    multinomial_nb,
    xgboost_classifier,
    knn_classifier,
    hinge_loss,
    svm_classifier,
    decision_tree,
    random_forest,
    gradient_boosting_classifier,
    adaboost_classifier,
    mlp_classifier
]
fitness_function_names = [func.__name__ for func in fitness_functions]

import time

for func in fitness_functions:
    params.FITNESS = func
    fitness_function_name = func.__name__
    print(f"\n--- Running GA with fitness function: {fitness_function_name} ---")

    # Start timer BEFORE GA begins
    start_time = time.time()

    ga = GeneticAlgorithm(data=ds_data)

    elapsed_time = time.time() - start_time  # Time taken for GA to run

    output_result(
        best_individuals=ga.best_per_gen,
        feature_names=ga.data.feature_names,
        dataset_name=ds_name,
        fitness_function_name=fitness_function_name,
        elapsed_time=elapsed_time

    )
