import random


class GeneticAlgorithm:
    def __init__(self, num_genes, num_generations, population_size, elite_percentage):
        self.num_genes = num_genes
        self.num_generations = num_generations
        self.population_size = population_size
        self.elite_percentage = elite_percentage

    def create_individual(self):
        gene_code = []
        for i in range(self.num_genes):
            gene_code = [random.choice([0, 1]) for i in range(self.num_genes)]
        return gene_code

    def evaluate_individual(self, a_gene_code):
        gene_code = a_gene_code  # a_gene_code should be a list
        score = 0
        for gene in gene_code:
            if gene == 0:
                score += 1
        return score

    def rank_population(self, a_population):
        population = a_population
        ranked_population = sorted(population)  # ascending order, favoring lower score
        return ranked_population

    def darwin_population(self, a_ranked_population):   # return a list of survivors
        ranked_population = a_ranked_population
        num_elites = round(len(ranked_population) * self.elite_percentage)  # expecting a float
        alive = ranked_population[:num_elites + 1]
        return alive

    def start_generation(self):
        for generation in range(self.num_generations):
            population = {}
            for i in range(self.population_size):
                individual = self.create_individual()
                score = self.evaluate_individual(individual)
                population[tuple(individual)] = score  # adds the individual to population
            self.rank_population(population)


ga = GeneticAlgorithm(8, 20, 10, 0.3)

print(ga.start_generation())
