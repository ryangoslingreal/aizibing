import fitness
import inspect
import multiprocessing

from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split

iris = load_iris()
breast_cancer = load_breast_cancer()

dataset = breast_cancer


# super basic preprocessing trash, just to drop null values:

#COLUMN_NA_THRESHOLD = 0.2 # if 20% of column is null, drop column.
#print(df.isnull().mean())
#df = df.loc[:, df.isnull().mean() < COLUMN_NA_THRESHOLD]
#df = df.dropna()



X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=42)

def run_function(func):
    try:
        result = func(X_train, y_train, X_test, y_test)

        print(f"{func.__name__}\n    result: {result}\n")
    except Exception as e:
        print(f"Error occurred while running {func.__name__}: {e}\n")

functions = [func for _, func in inspect.getmembers(fitness, inspect.isfunction)]

if __name__ == "__main__":
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(run_function, functions)
