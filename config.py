import selection
import crossover
import mutation
import fitness

PARAMS = {
    # GA methods
    "SELECTION": selection.roulette_wheel_selection,
    "CROSSOVER": crossover.splice_crossover,
    "MUTATION": mutation.random_mutate,
    "FITNESS": fitness.gaussian_nb,


    # GA Properties
    "ELITE_RATE": 0.2,
    "PADDING_RATE": 0.2,
    "MUTATION_RATE": 0.01, # maybe implement 'variable mutation' via hamming distance?


    # Selection Properties
    "TOURNAMENT_ROUNDS": 5,
}