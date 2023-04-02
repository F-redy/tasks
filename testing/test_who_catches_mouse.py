from ternary_operator.cats_and_mouse import who_catches_mouse

TESTS = (
    ((1, 2, 3), 'Cat B'),
    ((1, 3, 2), 'Mouse C'),
    ((1, 2, 3), 'Cat B'),
    ((1, 3, 2), 'Mouse C'),
    ((1, 5, 2), 'Cat A'),
    ((1, 3, 4), 'Cat B'),
    ((1, 1, 1), 'Mouse C'),

)


def test_cat_and_mouse(data: tuple, v: int):
    test = who_catches_mouse(*data[0])
    result = data[1]
    assert test == result, AssertionError('Error in test-{}, expected: "{}", received: "{}"'.format(v, result, test))
    return f'test.{v}\t\t{test:<11}  OK'


for i, task in enumerate(TESTS, 1):
    print(test_cat_and_mouse(task, i))
