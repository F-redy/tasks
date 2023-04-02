from time import time
from typing import Any, Callable


def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result

    return wrapper
