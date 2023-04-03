import numpy as np


def find_diagonal_difference(nested_list):
    matrix = np.array(nested_list)
    return np.abs(np.diag(matrix).sum() - np.diag(np.fliplr(matrix)).sum())

