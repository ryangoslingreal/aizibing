from sklearn.naive_bayes import GaussianNB
from functools import cache

def evaluate_individual(self, selected_attributes, train_idx, test_idx):
    """Trains and evaluates an individual using GaussianNB."""
    # Apply attribute mask
    X_train, X_test = self.X[train_idx][:, selected_attributes], self.X[test_idx][:, selected_attributes]
    y_train, y_test = self.y[train_idx], self.y[test_idx]
                
    # Train
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    return nb.score(X_test, y_test)