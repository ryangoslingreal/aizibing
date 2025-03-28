from types import SimpleNamespace

import selection
import crossover
import mutation

params = SimpleNamespace(
    FEATURE_COST=0.05,  # adjust this to control how strongly you penalize large feature sets

    # GA Methods
    SELECTION=selection.roulette_wheel_selection,
    CROSSOVER=crossover.random_crossover,
    MUTATION=mutation.random_mutate,
    FITNESS=None,

    # GA Properties
    GENERATIONS=20,
    POPULATION=20,
    REPETITIONS=3,
    FOLDS=2,
    ELITE_RATE=0.25,
    PADDING_RATE=0.05,
    MUTATION_RATE=0.05,  # maybe implement 'variable mutation' via hamming distance?

    # Selection Properties
    TOURNAMENT_ROUNDS=5,

    # Mutation Properties
    ALLOW_CLONING=True,
    MUTATE_ON_CLONE=True
)
