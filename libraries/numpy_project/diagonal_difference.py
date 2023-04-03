import numpy as np


def get_diagonal_difference(nested_list: list[list[int]]) -> int:
    matrix = np.array(nested_list)
    return np.abs(np.diag(matrix).sum() - np.diag(np.fliplr(matrix)).sum()).item()
