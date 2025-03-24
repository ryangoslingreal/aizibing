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


from sklearn.neural_network import MLPClassifier

def mlp_classifier(X_train, y_train, X_test, y_test):
    # Multi-Layer Perceptron (MLP) - its like perceptron but deep learning
    model = MLPClassifier(hidden_layer_sizes=(100, ), max_iter=500) # change this ?
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)