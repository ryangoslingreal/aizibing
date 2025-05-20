from types import SimpleNamespace

import selection
import crossover
import mutation
import fitness

params = SimpleNamespace(
    # GA Methods
    SELECTION=selection.roulette_wheel_selection,
    CROSSOVER=crossover.random_crossover,
    MUTATION=mutation.random_mutate,
    FITNESS=fitness.gaussian_nb,

    # GA Properties
    GENERATIONS=10,
    POPULATION=5,
    REPETITIONS=5,
    FOLDS=5,
    ELITE_RATE=0.2,
    PADDING_RATE=0.2,
    MUTATION_RATE=0.1,  # maybe implement 'variable mutation' via hamming distance?
    
    # Fitness Properties
    FEATURE_PENALTY=True,
    ALPHA=1,
    BETA=0.01,

    # Selection Properties
    TOURNAMENT_ROUNDS=5,

    # Mutation Properties
    ALLOW_CLONING=True,
    MUTATE_ON_CLONE=True
)