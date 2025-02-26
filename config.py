from types import SimpleNamespace

import selection
import crossover
import mutation
import fitness
import genocide

params = SimpleNamespace(
    # GA Methods
    SELECTION=selection.roulette_wheel_selection,
    CROSSOVER=crossover.splice_crossover,
    MUTATION=mutation.random_mutate,
    FITNESS=fitness.gaussian_nb,

    # GA Properties
    GENERATIONS=10,
    POPULATION=10,
    REPETITIONS=30,
    FOLDS=5,
    ELITE_RATE=0.10,
    PADDING_RATE=0.2,
    MUTATION_RATE=0.01,  # maybe implement 'variable mutation' via hamming distance?

    # Selection Properties
    TOURNAMENT_ROUNDS=5,

    # Genocide Methods
    KILL_METHOD=genocide.elitism,

    # Mutation Properties
    ALLOW_CLONING=True,
    MUTATE_ON_CLONE=True
)