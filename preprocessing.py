from individual import Individual

from config import params
from utils import *

def preprocess_data(data):
    Individual.X, Individual.y = data.data, data.target
    Individual.rep_folds = generate_n_folds(Individual.X, Individual.y, params.REPETITIONS, params.FOLDS)
    Individual.attributes = Individual.X.shape[1]