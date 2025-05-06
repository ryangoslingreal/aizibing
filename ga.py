from sklearn.model_selection import StratifiedKFold
import numpy as np
import random

from functools import cache

from utils import *
from individual import Individual
from config import params


class GeneticAlgorithm:
    def __init__(self, data):
        """Initializes the genetic algorithm with population-based feature selection."""
        self.data = data
        self.population = []
        self.best_per_gen = []
        
        # Define crossover thresholds
        self.elite_size = int(params.ELITE_RATE * params.POPULATION)
        self.padding_size = int(params.PADDING_RATE * params.POPULATION)
        self.breeding_size = params.POPULATION - self.padding_size - self.elite_size
        
        # Preprocess dataset
        self.X, self.y = data.data, data.target
        self.attributes = self.X.shape[1]
        self.rep_folds = self.generate_n_folds(self.X, self.y, params.REPETITIONS, params.FOLDS)
        
        # Compute baseline fitness
        baseline_fitness = self.rep_individual(tuple([True for _ in range(self.attributes)]))
        print(f"Baseline fitness: {baseline_fitness}")
        
        for g in range(params.GENERATIONS):
            print(f"\n--- Generation {g} ---")
            self.step()

    # returns top 'n' unique individuals of population, so you can see what columns they use - FIX THIS
    def unique_head(self, n = 5):
        unique_individuals = []
        seen_individuals = set()  # track unique individuals

        for i, individual in enumerate(self.population):
            individual_tuple = tuple(individual) # make individual hashable

            # if unique
            if individual_tuple not in seen_individuals:
                seen_individuals.add(individual_tuple)
                unique_individuals.append(individual)

            if len(unique_individuals) >= n:
                break

        return unique_individuals
    
    def step(self):
        self.pad_population()
        
        self.evaluate_population()

        self.sort_population()
        
        #self.best_per_gen.append(self.population[0]) # storing top individual to list for resulting feature name

        for i, individual in enumerate(self.population):
            print(f"Position {i}: {individual.gene}    Fitness: {individual.fitness}")
            #break # Only output best individual
        
        # Extract breeding population
        breeding_pool = self.population[:self.breeding_size + self.elite_size]
        
        next_population = []
        
        # Until breeding threshold reached
        while len(next_population) < self.breeding_size:
            # Choose two unique parents if ALLOW_CLONING = False
            parent1, parent2 = params.SELECTION(breeding_pool, params.ALLOW_CLONING)
            
            # If ALLOW_CLONING = True and MUTATE_ON_CLONE = True, mutate
            # Else, crossover
            if parent1.gene == parent2.gene and params.MUTATE_ON_CLONE:
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

    def sort_population(self):
        """Sorts population by fitness."""
        for ind in self.population:
            assert ind.fitness is not None, f"Fitness not set for individual: {ind.gene}"
        self.population = sorted(self.population, key=lambda ind: ind.fitness, reverse=True)
    
    def pad_population(self):
        """Ensures the population remains at POPULATION by adding new individuals if necessary."""
        
        difference = params.POPULATION - len(self.population)
        if difference > 0:
            self.population += self.generate_individuals(difference, self.attributes)


    def evaluate_population(self):
        """Evaluates the fitness of all individuals in the population and stores their scores."""
        
        for individual in self.population:
            individual.fitness = self.rep_individual(individual.gene) # Extract gene for caching

    @cache
    def rep_individual(self, gene):
        """Computes the average fitness of an individual across multiple repetitions and caches result."""
        
        rep_fitness = []
        
        # Rep loop
        for r in range(params.REPETITIONS):
            # Fold loop
            fold_fitness = [
                self.evaluate_individual(gene, train_idx, test_idx)
                for train_idx, test_idx in self.rep_folds[r]
            ]
                
            # Calculate average fitness across all folds
            rep_fitness.append(np.mean(fold_fitness))

        # Calculate average fitness across all reps
        return np.mean(rep_fitness)
    
    def evaluate_individual(self, gene, train_idx, test_idx):
        """Applies individual attribute mask and evaluates an individual using the specified fitness function."""
        
        # Apply attribute mask
        X_train, X_test = self.X[train_idx][:, gene], self.X[test_idx][:, gene]
        y_train, y_test = self.y[train_idx], self.y[test_idx]
                    
        # Train
        return params.FITNESS(X_train, y_train, X_test, y_test)
    
    @staticmethod
    def generate_individuals(count, attributes):
        """Generates a specified number of random individuals."""
        
        population = []
        for _ in range(count):
            # Generate random gene
            # Ensure gene is valid
            # If valid, continue
            # Else, regenerate
            while True:
                gene = [random.choice([True, False]) for _ in range(attributes)]
                if any(gene):
                    break
            
            population.append(Individual(gene))
            
        return population
    
    @staticmethod
    def generate_n_folds(X, y, rep, fold):
        """Generates stratified k-fold splits for cross-validation."""
        
        rep_folds = {}
        for r in range(rep):
            skf = StratifiedKFold(n_splits=fold, shuffle=True)
            rep_folds[r] = list(skf.split(X, y))
            
        return rep_folds

if __name__ == "__main__":
    iris = load_iris()
    ga = GeneticAlgorithm(data=iris)