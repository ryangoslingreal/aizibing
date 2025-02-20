from dataclasses import dataclass

# hyperparameters ?

@dataclass(frozen=True) #frozen = True meaning, once the object has been initialised, it can't be changed
class GeneticConfig:
    population_size: int = 10
    gene_length: int = 10

    elite_percent: float = 0.2   # 20%
    padding_percent: float = 0.2

    mutation_rate: float = 0.01
    
    maximize_fitness: bool = True

    seed: int = None

    # TournamentSelection rounds
    tournament_rounds: int = 5 # number of tournaments in selection