from individual import Individual
import random

def splice_crossover(parent1, parent2):
    """Performs splice crossover between two parents and returns a random of two offspring."""
    
    cut_length = round(len(parent1.gene) * 0.3)  # Ensure at least 1 element is swapped
    start_index = random.randint(0, len(parent1.gene) - cut_length)
    end_index = start_index + cut_length

    # Swap genetic material between parents
    child_gene_1 = parent1.gene[:start_index] + parent2.gene[start_index:end_index] + parent1.gene[end_index:]
    child_gene_2 = parent2.gene[:start_index] + parent1.gene[start_index:end_index] + parent2.gene[end_index:]
    child = Individual(random.choice([child_gene_1, child_gene_2]))
    
    return Individual.verify_individual(child)

def average_crossover(parent1, parent2):
    """Performs average crossover between two parents and returns offspring."""
    
    paired_genes = zip(parent1.gene, parent2.gene)
    child_gene = []
    for pair in paired_genes:
        child_gene.append(random.choice(pair))
        
    child = Individual(child_gene)

    return Individual.verify_individual(child)

def random_crossover(p1, p2):
    crossover_point = random.randint(0, len(p1.gene))
    child_gene = p1.gene[:crossover_point] + p2.gene[crossover_point:]
    child = Individual(child_gene)
    
    return Individual.verify_individual(child)