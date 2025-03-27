from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB  
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score

import xgboost as xgb

def gaussian_nb(X_train, y_train, X_test, y_test):
    """Trains and evaluates using GaussianNB."""
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)

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

def xgboost_classifier(X_train, y_train, X_test, y_test):
    """Trains and evaluates using XGBoost Classifier."""
    xc = xgb.XGBClassifier()
    xc.fit(X_train, y_train)
    return xc.score(X_test, y_test)

def knn_classifier(X_train, y_train, X_test, y_test):
    """simple algorithm that classifies based on majority class of the nearest neighbors"""
    clf = KNeighborsClassifier()
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)

def hinge_loss(X_train, y_train, X_test, y_test):
    """Trains and evaluates using SGDClassifier with hinge loss (SVM).
    
    Can handle continuous numerical features well, but typically requires feature scaling."""
    
    clf = SGDClassifier(loss='hinge', random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

def svm_classifier(X_train, y_train, X_test, y_test):
    """support vector machine - better suited to higher-dimension datasets"""
    clf = SVC()
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)

# creates a warning / error when called
#def maximum_entropy(X_train, y_train, X_test, y_test):
#    """Trains and evaluates using Logistic Regression (Maximum Entropy).
#    
#    General-purpose classifier suitable for both continuous and discrete numerical features. 
#    Feature scaling often improves performance."""
#    
#    clf = LogisticRegression(max_iter=1000, random_state=42)
#    clf.fit(X_train, y_train)
#    y_pred = clf.predict(X_test)
#    return accuracy_score(y_test, y_pred)

def decision_tree(X_train, y_train, X_test, y_test):
    """Trains and evaluates using DecisionTreeClassifier.
    
    Highly general, robust to varying types of features (categorical, numerical) without requiring extensive preprocessing."""
    
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

def random_forest(X_train, y_train, X_test, y_test):
    """'ensemble' of decision trees"""
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)

def gradient_boosting_classifier(X_train, y_train, X_test, y_test):
    """trains and evaluates gradient boosting classifier"""
    clf = GradientBoostingClassifier()
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)

# all of these are based off of decision trees
def adaboost_classifier(X_train, y_train, X_test, y_test):
    """trains & envaluates adaboost"""
    clf = AdaBoostClassifier()
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)

def mlp_classifier(X_train, y_train, X_test, y_test):
    # Multi-Layer Perceptron (MLP) - its like perceptron but deep learning
    clf = MLPClassifier(hidden_layer_sizes=(100, ), max_iter=500) # change this ?
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)