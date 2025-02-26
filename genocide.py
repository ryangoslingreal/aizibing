from config import *

def elitism(sorted_population, elite_rate):
    pre_kill = sorted_population
    elite_ratio = max(2,round(len(pre_kill) * elite_rate))
    print(f"elite_ratio = {elite_ratio}")
    after_kill = pre_kill[:elite_ratio]

    return after_kill