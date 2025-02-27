from config import *

def elitism(sorted_population):
    pre_kill = sorted_population
    elite_ratio = round(len(pre_kill) / params.ELITE_RATE)
    after_kill = pre_kill[:elite_ratio]

    return after_kill