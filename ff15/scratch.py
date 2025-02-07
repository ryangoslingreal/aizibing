# import random
# import math
#
#
# class GeneticAlgorithm:
#     def __init__(self, number_of_features):
#         self.number_of_features = number_of_features
#         self.classifier = 'fitness function place holder(an executable class)'
#         self.fitness_score = 0.0
#         self.number_of_folds = 'number of folds place holder(int representing the number of folds)'
#
#
#     def individual(self):
#         self.genecode = [random.choice([0, 1]) for i in range(self.number_of_features)]
#         return self.genecode
#
#     # simply choose either 0 or 1 and fill the list up to the number of features
#     def populate(self, population_size):
#         self.population = []
#         for i in range(population_size):
#             self.population.append(self.individual())
#         return self.population
#
#     # at the moment the FF calculates the sum of 0s and 1s
#     # return the fitness of each individual in a list
#     def fitness_of_individuals(self):
#         gene_pool = {}
#         for individual in self.population:
#             score = 0
#             for feature in individual:
#                 score += feature
#             gene_pool[tuple(individual)] = score
#         return gene_pool
#
#     # determine the top 5%, bottom 5% then repopulate mid 90%
#     def evolve(self, gene_pool, number_of_evolutions):
#         gene_pool = sorted(gene_pool, reverse=True)
#
#         percentage = 0.05
#         cut_off = math.ceil(len(gene_pool) * percentage)
#
#         elites = gene_pool[:cut_off]
#         peseants = gene_pool[-cut_off:]
#         mutant_pop_size = len(gene_pool[cut_off:-cut_off])
#
#         for i in range(number_of_evolutions):
#             gene_pool.append(elites)
#
#
#         return gene_pool, elites, peseants, mutant_pop_size
#
#
#
# # define ga with 10 features
# ga = GeneticAlgorithm(10)
#
# #pop size of 10. RETURNS a list containing the population (self.population)
# population_list = ga.populate(10)
# print(population_list)
#
# #feed fit_of_indi into evovle


import random
gene_code = []
for i in range(10):
    gene_code = [random.choice([0, 1]) for i in range(10)]
return gene_code


def evaluate_individual(self, a_gene_code):
    gene_code = a_gene_code  # a_gene_code should be a list
    score = 0
    for gene in gene_code:
        if gene == 0:
            score += 1
    return score


























