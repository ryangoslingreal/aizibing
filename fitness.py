from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

def gaussian_nb(X_train, y_train, X_test, y_test):
    """Trains and evaluates an individual using GaussianNB."""
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    return gnb.score(X_test, y_test)

def bernoulli_nb(X_train, y_train, X_test, y_test):
    """Trains and evaluates an individual using BernoulliNB."""
    bnb = BernoulliNB()
    bnb.fit(X_train, y_train)
    return bnb.score(X_test, y_test)

def multinomial_nb(X_train, y_train, X_test, y_test):
    """Trains and evaluates an individual using MultinomialNB."""
    mnb = MultinomialNB()
    mnb.fit(X_train, y_train)
    return mnb.score(X_test, y_test)

def hinge_loss(X_train, y_train, X_test, y_test):
    pass

def maximum_entropy(X_train, y_train, X_test, y_test):
    pass

def hmm(X_train, y_train, X_test, y_test):
    pass