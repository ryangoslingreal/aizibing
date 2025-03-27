import openml
from sklearn.datasets import load_iris as sk_load_iris, load_breast_cancer as sk_load_breast_cancer
from sklearn.utils import Bunch

# Built-in sklearn datasets


def load_openml(dataset_id):
    """
    Loads any OpenML dataset by ID and returns a sklearn-style Bunch object.
    """
    dataset = openml.datasets.get_dataset(dataset_id)
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

load_iris = sk_load_iris
load_breast_cancer = sk_load_breast_cancer
load_indian_pines = lambda: load_openml(41972)
load_german_credit = lambda: load_openml(46416)

# Public interface
__all__ = [
    "load_iris",
    "load_breast_cancer",
    "load_indian_pines",
    "load_german_credit"
]
