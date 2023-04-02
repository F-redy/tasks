from for_module.nested_loop.electronics_shop import getMoneySpent

TESTS = (
    (([4], [5], 5), -1),
    (([3, 1], [5, 2, 8], 10), 9),
    (([10, 20, 30], [15, 25, 35], 30), 25),
    (([20, 30, 40, 50], [5, 10, 15, 20], 25), 25),
    (([40, 50, 60], [5, 8, 12], 100), 72),
    (([30, 50, 70], [20, 40, 60], 80), 70),
    (([25, 35, 45], [30, 40, 50], 60), 55),
)


def test_getMoneySpent(data: tuple, num: int):
    test = getMoneySpent(*data[0])
    res = data[1]
    assert test == res, AssertionError('wrong result, expected: "{}", received: "{}"'.format(res, test))
    return f'test_{num}\t\t{test} \t\t OK'


for i, tr in enumerate(TESTS, 1):
    print(test_getMoneySpent(tr, i))
