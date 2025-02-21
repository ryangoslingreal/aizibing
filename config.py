import selection
import crossover

PARAMS = {
    # GA methods
    "SELECTION": selection.roulette_wheel_selection,
    "CROSSOVER": crossover.splice_crossover,

    # GA properties
    "ELITE_RATE": 0.2,
    "PADDING_RATE": 0.2,
    "MUTATION_RATE": 0.01, # maybe implement 'variable mutation' via hamming distance?


    # Tournament Rounds
    "TOURNAMENT_ROUNDS": 5
}

