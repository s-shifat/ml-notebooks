import pandas as pd
from sklearn.datasets import fetch_california_housing


def get_classification_X_y(data_path="data/heart-disease.csv", target_var="target"):
    df = pd.read_csv(data_path)
    X = df.drop(target_var, axis=1)
    y = df[target_var]
    return X, y


def get_regression_X_y(data_path=None, target_var=None):
    if not data_path:
        return fetch_california_housing(as_frame=True, return_X_y=True)
    elif data_path and target_var:
        return get_classification_X_y(data_path=data_path, target_var=target_var)