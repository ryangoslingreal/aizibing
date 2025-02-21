from sklearn.model_selection import StratifiedKFold
import numpy as np
import random

from sklearn import datasets
iris = datasets.load_iris()
breast_cancer = datasets.load_breast_cancer()

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
            fitness_scores[i] = np.mean(rep_fitness)
            #print(f"Individual {i}: {individual}    Fitness: {fitness_scores[i]}")
        
        return fitness_scores
    
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
            
ga = GeneticAlgorithm(data=iris, 
                      gen=1, 
                      pop=10, 
                      rep=5, 
                      fold=5, 
                      elite_rate=0.05, 
                      padding_rate=0.05, 
                      mutation_rate=0.01)