import selection
import crossover

PARAMS = {
    # GA methods
    "SELECTION": selection.roulette_wheel_selection,
    "CROSSOVER": crossover.splice_crossover,



    # Tournament Rounds
    "TOURNAMENT_ROUNDS": 5
}

