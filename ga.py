from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import StratifiedKFold
import numpy as np
import random

from functools import cache

from sklearn import datasets
iris = datasets.load_iris()
breast_cancer = datasets.load_breast_cancer()

from config import *

# Custom Decorator function
def list_to_tuple(function):
    def wrapper(*args):
        args = [tuple(x) if isinstance(x, list) else x for x in args]
        result = function(*args)
        result = tuple(result) if isinstance(result, list) else result
        return result
    return wrapper

class GeneticAlgorithm():
    def __init__(self, data, gen, pop, rep, fold, elite_rate, padding_rate, mutation_rate):
        """Initializes the genetic algorithm with population-based feature selection."""
        self.data = data
        self.gen = gen
        self.pop = pop
        self.rep = rep
        self.fold = fold
        self.elite_rate = elite_rate
        self.padding_rate = padding_rate
        self.mutation_rate = mutation_rate
        
        # Preprocess dataset
        self.X, self.y = data.data, data.target
        self.attributes = self.X.shape[1]
        self.rep_folds = self.generateNFolds(self.X, self.y, self.rep, self.fold)
        
        # Generate initial population
        self.population = self.generateIndividuals(self.pop, self.attributes)
        
        for g in range(gen):
            print(f"\n--- Generation {g} ---")
            self.step()
        
    def step(self):
        self.pad_population()
        
        self.fitness_scores = self.evaluate_population()

        for i, (individual, fitness) in enumerate(zip(self.population, self.fitness_scores)):
            print(f"Position {i}: {individual}    Fitness: {fitness}")
    
    def pad_population(self):
        """Ensures the population remains at self.pop by adding new individuals if necessary."""
        difference = self.pop - len(self.population)
        if difference > 0:
            self.population += self.generateIndividuals(difference, self.attributes)

    def evaluate_population(self):
        """Evaluates fitness for each individual in the population."""
        fitness_scores = np.zeros(self.pop)
        
        # Individual loop
        for i, individual in enumerate(self.population):
            fitness_scores[i] = self.rep_individual(individual)
        
        return fitness_scores
    
    @list_to_tuple
    @cache
    def rep_individual(self, individual):
        rep_fitness = []
            
        # Attribute mask
        selected_attributes = np.array(individual, dtype=bool)
        
        # Rep loop
        for r in self.rep_folds:
            # Fold loop
            fold_fitness = [
                self.evaluate_individual(selected_attributes, train_idx, test_idx)
                for train_idx, test_idx in self.rep_folds[r]
            ]
                
            # Calculate average fitness across all folds
            rep_fitness.append(np.mean(fold_fitness))

        # Calculate average fitness across all reps
        return np.mean(rep_fitness)
    
    @cache
    def evaluate_individual(self, selected_attributes, train_idx, test_idx):
        """Trains and evaluates an individual using GaussianNB."""
        # Apply attribute mask
        X_train, X_test = self.X[train_idx][:, selected_attributes], self.X[test_idx][:, selected_attributes]
        y_train, y_test = self.y[train_idx], self.y[test_idx]
                    
        # Train
        return PARAMS["FITNESS"](X_train, y_train, X_test, y_test)
    
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
            
#ga = GeneticAlgorithm(data=iris, 
#                      gen=1, 
#                      pop=10, 
#                      rep=5, 
#                      fold=5, 
#                      elite_rate=0.05, 
#                      padding_rate=0.05, 
#                      mutation_rate=0.01)

print(PARAMS)
