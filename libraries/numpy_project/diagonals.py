import numpy as np


def main_diagonal(nested_list: list[list[int]]) -> list[int]:
    matrix = np.array(nested_list)
    return np.diagonal(matrix).tolist()


def secondary_diagonal(nested_list: list[list[int]]) -> list[int]:
    matrix = np.array(nested_list)
    return np.diagonal(np.fliplr(matrix)).tolist()
