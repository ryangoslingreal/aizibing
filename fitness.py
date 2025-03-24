from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB

def gaussian_nb(X_train, y_train, X_test, y_test):
    """Trains and evaluates an individual using GaussianNB."""
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    return nb.score(X_test, y_test)

def Bernoulli_nb(X_train, y_train, X_test, y_test):
    bnb = BernoulliNB()
    bnb.fit(X_train, y_train)
    return bnb.score(X_test, y_test)