# crossover.py DEBUGGER
# from random import randint, choice
# from crossover import *
#
# rand_size = randint(5, 10)  # Ensure at least one element
# fake_parent1 = [choice([0, 1]) for _ in range(rand_size)]
# fake_parent2 = [choice([0, 1]) for _ in range(rand_size)]
# print(f'parent1 = {fake_parent1}')
# print(f'parent2 = {fake_parent2}')
# -----------------------------------------------------------------------------------------
# splice_crossover
# to see the information for index, splice size, etc... : need to change function to return what you need


# children = splice_crossover(fake_parent1, fake_parent2)
# print(f'children = {children}')

# -----------------------------------------------------------------------------------------
# average_crossover

# child = average_crossover(fake_parent1, fake_parent2)
# print(child)

# -----------------------------------------------------------------------------------------
# dataset format verification
from load_a_dataset import load_breast_cancer, load_indian_pines, load_german_credit
from sklearn.datasets import load_breast_cancer as sk_breast_cancer
import numpy as np

custom = load_breast_cancer()
sklearn_ver = sk_breast_cancer()


def compare_datasets(d1, d2, label):
    print(f"\n--- Checking: {label} ---")
    assert isinstance(d1, type(d2)), f"Type mismatch: {type(d1)} vs {type(d2)}"
    assert hasattr(d1, "data") and hasattr(d1, "target"), "Missing 'data' or 'target'"
    assert isinstance(d1.data, np.ndarray), "'data' is not a NumPy array"
    assert d1.data.shape[0] == d1.target.shape[0], "Mismatch in number of samples"

    print(f"✅ Passed for {label} | Samples: {d1.data.shape[0]}, Features: {d1.data.shape[1]}")

    print(f"🧠 Feature names ({len(d1.feature_names)}):")
    for i, name in enumerate(d1.feature_names):
        print(f"  {i + 1:2d}. {name}")

    print(f"\n🎯 Target classes ({len(d1.target_names)}): {d1.target_names}")

compare_datasets(custom, sklearn_ver, "breast_cancer")
compare_datasets(load_indian_pines(), custom, "indian_pines")
compare_datasets(load_german_credit(), custom, "german_credit")

# -----------------------------------------------------------------------------------------



