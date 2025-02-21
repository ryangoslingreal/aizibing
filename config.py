import selection
import crossover
import mutation

PARAMS = {
    # GA methods
    "SELECTION": selection.roulette_wheel_selection,
    "CROSSOVER": crossover.splice_crossover,
    "MUTATION": mutation.random_mutate,


    # GA Properties
    "ELITE_RATE": 0.2,
    "PADDING_RATE": 0.2,
    "MUTATION_RATE": 0.01, # maybe implement 'variable mutation' via hamming distance?


    # Selection Properties
    "TOURNAMENT_ROUNDS": 5
}