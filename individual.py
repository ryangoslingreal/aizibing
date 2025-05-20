from functools import cache
import numpy as np
import traceback
import random

from config import params

class Individual:
    X = None
    y = None
    rep_folds = None
    attributes = None
    
    def __init__(self, gene):
        self.gene = tuple(gene)
        self._fitness = None
    
    @property
    def fitness(self):
        if self._fitness is None:
            # If FEATURE_PENALTY = True, use parameters
            # Else, use defaults 
            self._fitness = (
                (params.ALPHA if params.FEATURE_PENALTY else 1) * self.rep_individual(self.gene) - 
                (params.BETA if params.FEATURE_PENALTY else 0) * sum(self.gene)
            )
        return self._fitness
            
    @fitness.setter
    def fitness(self, value):
        self._fitness = value
    
    @classmethod
    @cache
    def rep_individual(cls, gene):
        """Computes the average fitness of an individual across multiple repetitions and caches result."""
        
        if not any(gene):
            Individual.log_bad_gene(gene)
            return 0
        
        rep_fitness = []
        
        # Rep loop
        for r in range(params.REPETITIONS):
            # Fold loop
            fold_fitness = [
                Individual.evaluate_individual(gene, train_idx, test_idx)
                for train_idx, test_idx in Individual.rep_folds[r]
            ]
                
            # Calculate average fitness across all folds
            rep_fitness.append(np.mean(fold_fitness))

        # Calculate average fitness across all reps
        return np.mean(rep_fitness)
    
    @classmethod
    def evaluate_individual(cls, gene, train_idx, test_idx):
        """Applies individual attribute mask and evaluates an individual using the specified fitness function."""
        
        # Apply attribute mask
        X_train, X_test = Individual.X[train_idx][:, gene], Individual.X[test_idx][:, gene]
        y_train, y_test = Individual.y[train_idx], Individual.y[test_idx]
                    
        # Train
        return params.FITNESS(X_train, y_train, X_test, y_test)
    
    @staticmethod
    def generate_individuals(count):
        """Generates a specified number of random individuals."""
        
        population = []
        for _ in range(count):
            # Generate random gene
            # Ensure gene is valid
            # If valid, continue
            # Else, regenerate
            while True:
                gene = [random.choice([True, False]) for _ in range(Individual.attributes)]
                if any(gene):
                    break
            
            population.append(Individual(gene))
            
        return population
    
    @staticmethod
    def verify_individual(individual):
        """Ensures individual has at least one True value. If all False, randomly set one to True."""
        
        gene = list(individual.gene)
        if not any(gene):
            random_index = random.randint(0, len(gene) - 1)
            gene[random_index] = True

        return Individual(gene)
    
    @staticmethod
    def log_bad_gene(gene):
        print("\n[⚠️ BAD GENE DETECTED ⚠️]")
        print("Gene:", gene)
        print("Length:", len(gene))
        print("Sum:", sum(gene))
        traceback.print_stack()