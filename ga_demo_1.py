from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score
import numpy as np
import random

from sklearn import datasets
iris = datasets.load_iris()
breast_cancer = datasets.load_breast_cancer()

class GeneticAlgorithm():
    def __init__(self, data, gen, pop, rep, fold, elite, padding, mutation_rate):
        self.data = data
        self.gen = gen
        self.pop = pop
        self.rep = rep
        self.fold = fold
        self.elite = elite
        self.padding = padding
        self.mutation_rate = mutation_rate
        
        # Preprocess dataset
        self.X, self.y, self.attributes = data.data, data.target, len(data.data[0])
        self.rep_folds = self.generateNFolds(self.X, self.y, self.rep, self.fold)
        
        # Generate initial population
        self.population = self.generateIndividuals(self.pop, self.attributes)
        
        for g in range(gen):
            print(f"Generation {g}:")
            # Pad generation with new random individuals 
            if len(self.population) != self.pop:
                difference = self.pop - len(self.population)
                self.population += self.generateIndividuals(difference, self.attributes)
            
            self.step()
        
    def step(self):
        """Performs one generation step on the current population."""
        final_fitness = []
        
        for i, individual in enumerate(self.population):
            rep_fitness = []
            
            selected_attributes = np.array(individual, dtype=bool)
            
            for r in self.rep_folds:
                fold_fitness = []
                
                for train_idx, test_idx in self.rep_folds[r]:  
                    X_train, X_test = self.X[train_idx][:, selected_attributes], self.X[test_idx][:, selected_attributes]
                    y_train, y_test = self.y[train_idx], self.y[test_idx]
                    
                    nb = GaussianNB()
                    nb.fit(X_train, y_train)
                    accuracy = nb.score(X_test, y_test)
                    fold_fitness.append(accuracy)
                    
                rep_fitness.append(np.mean(fold_fitness))
                
            fitness = np.mean(rep_fitness)
            final_fitness.append(fitness)
            print(f"Individual {i}: {individual}    Fitness: {fitness}")
            
        sorted_indices = np.argsort(final_fitness)[::-1]
        self.population = [self.population[i] for i in sorted_indices]
            
    def crossover(self, parent1, parent2):
        """Performs crossover between two parents and returns offspring."""
        pass
    
    def mutate(self, individual, mutation_rate):
        """Mutates an individual with a given mutation rate."""
        pass
    
    @staticmethod
    def generateIndividuals(count, attributes):
        """Generates a specified number of random individuals."""
        population = []
        for _ in range(count):
            while True:
                individual = [random.choice([True, False]) for _ in range(attributes)]
                if any(individual):
                    break
            
            population.append(individual)
            
        return population
    
    @staticmethod
    def generateNFolds(X, y, rep, fold):
        rep_folds = {}
        for r in range(rep):
            skf = StratifiedKFold(n_splits=fold, shuffle=True, random_state=(42 + r))
            rep_folds[r] = list(skf.split(X, y))
            
        return rep_folds
            
ga = GeneticAlgorithm(data=breast_cancer, 
                      gen=1, 
                      pop=10, 
                      rep=5, 
                      fold=5, 
                      elite=0.05, 
                      padding=0.05, 
                      mutation_rate=0.01)