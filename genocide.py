from config import *

def elitism(sorted_population, elite_rate):
    pre_kill = sorted_population
    elite_ratio = round(len(pre_kill) * elite_rate)
    after_kill = pre_kill[:elite_ratio]

    return after_kill