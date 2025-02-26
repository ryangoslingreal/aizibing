# crossover.py DEBUGGER
# splice_crossover
from random import randint, choice

rand_size = randint(5, 100)  # Ensure at least one element
fake_parent1 = [choice([0, 1]) for _ in range(rand_size)]
fake_parent2 = [choice([0, 1]) for _ in range(rand_size)]

print(f'parent1 = {fake_parent1}')
print(f'parent2 = {fake_parent2}')

from crossover import *
children = splice_crossover(fake_parent1, fake_parent2)
print(f'children = {children}')