import os
import joblib
from ucimlrepo import fetch_ucirepo
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd

class HeartDiseaseClassifier:
    def __init__(self, cache_dir, dataset_id=45):
        self.cache_dir = cache_dir
        self.cache_file = os.path.join(cache_dir, 'heart_disease.pkl')
        self.dataset_id = dataset_id
        self.data = None
        self.model = GaussianNB()

    def ensure_cache_dir(self):
        """Ensure the cache directory exists."""
        os.makedirs(self.cache_dir, exist_ok=True)

    def fetch_data(self):
        """Fetch or load the heart disease dataset."""
        self.ensure_cache_dir()
        if os.path.exists(self.cache_file):
            print("Loading data from cache...")
            self.data = joblib.load(self.cache_file)
        else:
            print("Fetching data from UCI repository...")
            self.data = fetch_ucirepo(id=self.dataset_id)
            joblib.dump(self.data, self.cache_file)
            print(f"Data cached successfully at: {self.cache_file}")

    def preprocess_data(self):
        """Preprocess the dataset to extract features and targets."""
        X = pd.DataFrame(self.data.data.features, columns=self.data.data.feature_names)
        y = pd.Series(np.ravel(self.data.data.targets))
        data_cleaned = pd.concat([X, y], axis=1).dropna()
        X_cleaned = data_cleaned.iloc[:, :-1]
        y_cleaned = data_cleaned.iloc[:, -1]
        return X_cleaned, y_cleaned

    def train_model(self, X, y):
        """Train the Gaussian Naive Bayes model."""
        self.model.fit(X, y)
        accuracy = self.model.score(X, y)
        print(f"Model accuracy: {accuracy:.4f}")

    def run(self):
        """Main method to run the entire process."""
        self.fetch_data()
        X_cleaned, y_cleaned = self.preprocess_data()
        self.train_model(X_cleaned, y_cleaned)
        print("Sample data:")
        print(X_cleaned.head())
        print(y_cleaned.head())

