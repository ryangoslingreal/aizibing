from sklearn.naive_bayes import GaussianNB

def gaussian_nb(X_train, y_train, X_test, y_test):
    """Trains and evaluates an individual using GaussianNB."""
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    return nb.score(X_test, y_test)
