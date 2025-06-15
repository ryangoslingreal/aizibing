def bitwise_hamming_distance(individual, population):
    """Computes the normalised Hamming distance between an individual and the mean genome of the population."""
        
    pop_size = len(population)
    gene_len = len(individual.gene)
        
    # Count bits at each position
    bit_counts = [0] * gene_len
    for member in [ind.gene for ind in population]:
        for i, bit in enumerate(member):
            bit_counts[i] += bit
          
    # Build average genome using majority      
    avg_genome = [count >= (pop_size / 2) for count in bit_counts]
        
    differences = sum(ind_bit != avg_bit for ind_bit, avg_bit in zip(individual.gene, avg_genome))
    return differences / gene_len # Normalise

def pairwise_hamming_distance(individual, population):
    """Computes the average normalized Hamming distance between an individual and every other genome in the population."""
    
    gene_len = len(individual.gene)
    total_distance = 0
    comparisons = 0

    for other in population:
        if other is individual:
            continue  # Skip self
        differences = sum(bit1 != bit2 for bit1, bit2 in zip(individual.gene, other))
        total_distance += differences / gene_len
        comparisons += 1

    return total_distance / comparisons