import os
import numpy as np
import matplotlib.pyplot as plt

def func(x, m, b):
    # Linear function
    return m * x + b

def get_data(train_split=0.7, N=150, m=0.71, b=0.2, std=1.0):
    '''Loads Training or Test data'''
    
    # create data
    x = np.linspace(-2, 2, N)
    y = func(x, m, b) + np.random.normal(size=x.shape[0], scale=std)

    # shuffle the data
    idx = np.random.choice(np.arange(N), size=N, replace=False)
    x_ = x[idx]
    y_ = y[idx]

    # split the data
    n_train = int(x_.shape[0] * train_split)
    X_train, X_test = x_[:n_train].reshape(-1, 1), x_[n_train:].reshape(-1, 1)
    y_train, y_test = y_[:n_train].reshape(-1, 1), y_[n_train:].reshape(-1, 1)

    return X_train, y_train, X_test, y_test