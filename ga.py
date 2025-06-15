from sklearn.model_selection import StratifiedKFold
import random

from utils import *
from preprocessing import preprocess_data
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
        preprocess_data(data)
        
        # Compute baseline fitness
        baseline_fitness = Individual.rep_individual(tuple([True for _ in range(Individual.attributes)]))
        print(f"Baseline fitness: {baseline_fitness}")
        
        for g in range(params.GENERATIONS):
            print(f"\n--- Generation {g} ---")
            self.step()

    # returns top 'n' unique individuals of population, so you can see what columns they use - FIX THIS
    def unique_head(self, n = 5):
        unique_individuals = []
        seen_individuals = set()  # track unique individuals

        for individual in self.population:
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
            if params.ADAPTIVE_MUTATION is not None:
                hamming_distance = params.HAMMING_DISTANCE(individual, next_population)
                mutation_rate = params.ADAPTIVE_MUTATION(hamming_distance)
            else:
                mutation_rate = params.BASIC_MUTATION_RATE
                
            if random.random() < mutation_rate:
                next_population[i] = params.MUTATION(individual)

        # Elite carry over
        next_population.extend(self.population[:self.elite_size])
        
        # Reset population for next generation cycle
        self.population = next_population

    def sort_population(self):
        """Sorts population by fitness."""
        self.population = sorted(self.population, key=lambda ind: ind.fitness, reverse=True)
    
    def pad_population(self):
        """Ensures the population remains at POPULATION by adding new individuals if necessary."""
        
        difference = params.POPULATION - len(self.population)
        if difference > 0:
            self.population += Individual.generate_individuals(difference)

if __name__ == "__main__":
    iris = load_iris()
    ga = GeneticAlgorithm(data=iris)