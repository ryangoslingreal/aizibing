from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import StratifiedKFold
import numpy as np
import random

from functools import cache

from sklearn import datasets
iris = datasets.load_iris()
breast_cancer = datasets.load_breast_cancer()

from config import *

class GeneticAlgorithm():
    def __init__(self, data):
        """Initializes the genetic algorithm with population-based feature selection."""
        self.data = data
        
        # Preprocess dataset
        self.X, self.y = data.data, data.target
        self.attributes = self.X.shape[1]
        self.rep_folds = self.generateNFolds(self.X, self.y, params.REPETITIONS, params.FOLDS)
        
        # Generate initial population
        self.population = self.generateIndividuals(params.POPULATION, self.attributes)
        
        for g in range(params.GENERATIONS):
            print(f"\n--- Generation {g} ---")
            self.step()
        
    def step(self):
        self.pad_population()
        
        self.fitness_scores = self.evaluate_population()

        self.sort_population()

        for i, (individual, fitness) in enumerate(zip(self.population, self.fitness_scores)):
            print(f"Position {i}: {individual}    Fitness: {fitness}")

    def sort_population(self):
        """Sorts population by fitness scores."""
        sorted_indices = np.argsort(self.fitness_scores)[::-1]
        self.population = [self.population[i] for i in sorted_indices]
        self.fitness_scores = [self.fitness_scores[i] for i in sorted_indices]
    
    def pad_population(self):
        """Ensures the population remains at self.pop by adding new individuals if necessary."""
        difference = params.POPULATION - len(self.population)
        if difference > 0:
            self.population += self.generateIndividuals(difference, self.attributes)

    def evaluate_population(self):
        """Evaluates fitness for each individual in the population."""
        fitness_scores = np.zeros(params.POPULATION)
        
        # Individual loop
        for i, individual in enumerate(self.population):
            fitness_scores[i] = self.rep_individual(individual)
        
        return fitness_scores
    
    @cache
    def rep_individual(self, individual):
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
        """Trains and evaluates an individual using GaussianNB."""
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
                individual = tuple(random.choice([True, False]) for _ in range(attributes))
                if any(individual):
                    break
            
            population.append(individual)
            
        return population
    
    @staticmethod
    def generateNFolds(X, y, rep, fold):
        """Generates stratified k-fold splits for cross-validation."""
        rep_folds = {}
        for r in range(params.REPETITIONS):
            skf = StratifiedKFold(n_splits=fold, shuffle=True, random_state=(42 + r))
            rep_folds[r] = list(skf.split(X, y))
            
        return rep_folds
            
ga = GeneticAlgorithm(data=iris)