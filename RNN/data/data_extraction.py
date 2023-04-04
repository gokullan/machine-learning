import pandas as pd
import numpy as np
from tabulate_cell_merger import tabulate_cell_merger


def display_samples(X, y):
    n = len(X)
    T = len(X[0])
    print(f"n = {n}, T = {T}")
    rowspan = dict()
    colspan = dict()
    table = [
        ["Sample", "Inputs", None, "Outputs"],
        [None, "Day", "Price", "Price"],
    ]
    colspan[(0,1)] = 2
    rowspan[(0,0)] = 2
    for s in range(n):
        for t in range(T):
            row = []
            if t == 0:
                row.append(s + 1)
            else:
                row.append(None)
            row.append(f"Day_{t+1}")
            row.append(X[s][t][0])
            if t == 0:
                row.append(y[s][0])
            else:
                row.append(None)
            table.append(row)
        rowspan[(5*s+2,0)] = 5
        rowspan[(5*s+2,3)] = 5
    tabulate_cell_merger.tabulate(table, colspan, rowspan)


def make_samples(data, window=5):
    n = len(data)
    X = []
    y = []
    for s in range(n - window):
        X.append(data.iloc[s:s+5].to_numpy())
        y.append(data.iloc[s+5].to_numpy())
    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.float32)
    return X, y


def get_data(path):
    data = pd.read_csv(path)
    data = data[data['symbol'] == 'YHOO']
    return make_samples(data['high'].to_frame())
