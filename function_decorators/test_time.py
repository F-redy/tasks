from time import time
from typing import Callable, Any

__all__ = ('test_time',)


# for import func: from function_decorators.test_time import test_time

def test_time(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time()
        for _ in range(100000):
            _ = func(*args, **kwargs)
        finish = time() - start
        print(f'Результат работы функции {func.__name__}: {finish:.2f} сек')
        return func

    return wrapper
