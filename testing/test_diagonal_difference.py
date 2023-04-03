from matrix.diagonal_difference import diagonal_difference

TESTS = (
    (3, [[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15),
    (3, [[1, 2, 3], [4, 5, 6], [9, 8, 9]], 2),
    (2, [[1, 2], [3, 4]], 0),
    (3, [[-1, 2, 3], [4, 5, -6], [7, 8, 9]], 2),
    (2, [[-10, 2], [3, 5]], 10),
)


def test_diagonal_difference(data: tuple, v: int):
    test = diagonal_difference(data[1], data[0])
    result = data[2]
    assert test == result, AssertionError('Error in test-{}, expected: "{}", received: "{}"'.format(v, result, test))
    return f'test-{v}\t\t{test}\t\tOK'


for i, test in enumerate(TESTS, 1):
    print(test_diagonal_difference(test, i))
