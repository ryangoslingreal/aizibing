import selection
import crossover
import mutation

PARAMS = {
    # GA methods
    "SELECTION": selection.roulette_wheel_selection,
    "CROSSOVER": crossover.splice_crossover,
    "MUTATION": mutation.random_mutate,


    # Tournament Rounds
    "TOURNAMENT_ROUNDS": 5
}

