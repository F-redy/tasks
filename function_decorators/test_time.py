from time import time


def test_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        for _ in range(100000):
            _ = func(*args, **kwargs)
        print(f'Результат работы функции {func.__name__}: {(time() - start):.2f} сек')
        return func

    return wrapper
