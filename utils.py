from sklearn.datasets import load_iris
from sklearn.utils import Bunch
import numpy as np

def get_selected_feature_names(individual, feature_names):
    return [name for name, selected in zip(feature_names, individual) if selected]
    
def load_iris_with_noise(n):
    """Load iris dataset and adds `n` columns of noise to features."""
    iris = load_iris()
    X = iris.data
    y = iris.target

    noise = np.random.randn(X.shape[0], n)
    X_noisy = np.hstack((X, noise))

    return Bunch(data=X_noisy, target=y, feature_names=iris.feature_names + [f"noise_{i+1}" for i in range(n)])