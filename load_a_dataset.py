import openml
from sklearn.datasets import load_iris as sk_load_iris, load_breast_cancer as sk_load_breast_cancer
from sklearn.utils import Bunch
from sklearn.preprocessing import LabelEncoder

def load_openml(dataset_id, as_frame=False):
    dataset = openml.datasets.get_dataset(dataset_id)
    X, y, _, _ = dataset.get_data(
        dataset_format='dataframe',
        target=dataset.default_target_attribute
    )

    # Encode string labels to integers
    if y.dtype == 'O' or y.dtype.name == 'category':
        y = LabelEncoder().fit_transform(y)

    df = X.copy()
    df["target"] = y

    # Drop columns with too many nulls and rows with any nulls
    COLUMN_NA_THRESHOLD = 0.2
    df = df.loc[:, df.isnull().mean() < COLUMN_NA_THRESHOLD]
    df = df.dropna()

    X_cleaned = df.drop(columns='target')
    y_cleaned = df['target']

    if as_frame:
        return Bunch(
            data=X_cleaned,
            target=y_cleaned,
            frame=df,
            feature_names=X_cleaned.columns.tolist(),
            target_names=sorted(set(y_cleaned)),
            DESCR=dataset.description
        )
    else:
        return Bunch(
            data=X_cleaned.to_numpy(),
            target=y_cleaned.to_numpy(),
            feature_names=X_cleaned.columns.tolist(),
            target_names=sorted(set(y_cleaned)),
            DESCR=dataset.description
        )


load_iris = sk_load_iris
load_breast_cancer = sk_load_breast_cancer
load_indian_pines = lambda: load_openml(41972)
load_german_credit = lambda: load_openml(46416)
load_arrythmia = lambda: load_openml(5)

# Public interface
__all__ = [
    "load_iris",
    "load_breast_cancer",
    "load_indian_pines",
    "load_german_credit"
]
