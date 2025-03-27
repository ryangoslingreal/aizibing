import os
import openml
from sklearn.datasets import load_iris as sk_load_iris, load_breast_cancer as sk_load_breast_cancer
from sklearn.utils import Bunch

# Cache directory set to project folder
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
openml.config.cache_directory = os.path.join(PROJECT_DIR, "ds_cache")

# Built-in sklearn datasets
load_iris = sk_load_iris
load_breast_cancer = sk_load_breast_cancer


def load_indian_pines():
    dataset = openml.datasets.get_dataset(151)
    X, y, _, _ = dataset.get_data(
        dataset_format='dataframe',
        target=dataset.default_target_attribute
    )

    return Bunch(
        data=X.to_numpy(),
        target=y.to_numpy(),
        feature_names=X.columns.tolist(),
        target_names=sorted(y.unique().tolist()),
        DESCR=dataset.description
    )


def load_german_credit():
    dataset = openml.datasets.get_dataset(46421)
    X, y, _, _ = dataset.get_data(
        dataset_format='dataframe',
        target=dataset.default_target_attribute
    )

    return Bunch(
        data=X.to_numpy(),
        target=y.to_numpy(),
        feature_names=X.columns.tolist(),
        target_names=sorted(y.unique().tolist()),
        DESCR=dataset.description
    )


# Public interface
__all__ = [
    "load_iris",
    "load_breast_cancer",
    "load_indian_pines",
    "load_german_credit"
]
