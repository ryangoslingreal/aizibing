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
    GENERATIONS=20,
    POPULATION=200,
    REPETITIONS=1,
    FOLDS=5,
    ELITE_RATE=0.25,
    PADDING_RATE=0.05,
    MUTATION_RATE=0.05,  # maybe implement 'variable mutation' via hamming distance?

    # Selection Properties
    TOURNAMENT_ROUNDS=5,


    # Mutation Properties
    ALLOW_CLONING=True,
    MUTATE_ON_CLONE=True
)