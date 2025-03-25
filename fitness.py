from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def gaussian_nb(X_train, y_train, X_test, y_test):
    """Trains and evaluates using GaussianNB."""
    
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

def hinge_loss(X_train, y_train, X_test, y_test):
    """Trains and evaluates using SGDClassifier with hinge loss (SVM).
    
    Can handle continuous numerical features well, but typically requires feature scaling."""
    
    clf = SGDClassifier(loss='hinge', random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

def maximum_entropy(X_train, y_train, X_test, y_test):
    """Trains and evaluates using Logistic Regression (Maximum Entropy).
    
    General-purpose classifier suitable for both continuous and discrete numerical features. 
    Feature scaling often improves performance."""
    
    clf = LogisticRegression(max_iter=1000, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

def decision_tree(X_train, y_train, X_test, y_test):
    """Trains and evaluates using DecisionTreeClassifier.
    
    Highly general, robust to varying types of features (categorical, numerical) without requiring extensive preprocessing."""
    
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

def mlp_classifier(X_train, y_train, X_test, y_test):
    # Multi-Layer Perceptron (MLP) - its like perceptron but deep learning
    clf = MLPClassifier(hidden_layer_sizes=(100, ), max_iter=500) # change this ?
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)