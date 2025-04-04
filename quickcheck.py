import time
import fitness
import inspect
import multiprocessing

from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from load_a_dataset import load_openml

#iris = load_iris()
#breast_cancer = load_breast_cancer()

def run_function(func):
    if (func.__name__ == "accuracy_score"): return # skip this function
    try:
        dataset = load_openml(5)
        X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=42)

        start_time = time.time()
        result = func(X_train, y_train, X_test, y_test)
        time_taken = time.time() - start_time

        #print(f"{func.__name__}\n    result: {result}\n")
        return (func.__name__, result, time_taken)
    except Exception as e:
        print(f"Error occurred while running {func.__name__}: {e}\n")
        return

functions = [func for _, func in inspect.getmembers(fitness, inspect.isfunction)]

if __name__ == "__main__":
    #dataset = load_openml(5)
    #print(dataset.data.shape)

    # need to do .astype(int) cuz xgboost dont like string target
    #X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=42)


    #openml_id = input("enter the openml dataset id: ")
    

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(run_function, functions)

    # remove None results
    results = [result for result in results if result is not None]

    # Convert the results into a pandas DataFrame
    df_results = pd.DataFrame(results, columns=["Model", "Accuracy", "Time Taken (s)"])

        # Display the results as a table
    print("\nResults Summary:")
    print(df_results)

    # Plot results using matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(df_results["Model"], df_results["Accuracy"], color='skyblue')
    plt.yticks(np.arange(0, 1.05, 0.05))
    plt.ylabel("Accuracy")
    plt.xlabel("Model")
    plt.title("Model Performance Comparison")

    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()