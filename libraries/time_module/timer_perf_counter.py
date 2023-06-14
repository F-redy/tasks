from time import perf_counter
from memory_profiler import profile
from typing import Any, Callable
from sys import getsizeof


def timer(repeat: int = 10, profile_enabled: bool = False) -> Callable[[Callable[..., Any]], Callable[..., str]]:
    """
    Декоратор для измерения времени выполнения функции.

    Параметры:
        repeat (int): Количество повторений измерений для получения среднего значения.
        profile_enabled (bool): Флаг, указывающий, нужно ли выполнять профилировку памяти.
                               По умолчанию установлено значение False.

    Зависимости:
        - memory-profiler: pip install memory-profiler
        - sys.getsizeof

    Возвращает:
        Callable[..., float]: Декорированную функцию, которая возвращает среднее время выполнения в секундах.

    Пример использования:
        @timer(repeat=5, profile_enabled=True)
        def my_function():
            # код функции

        average_time = my_function()  # Среднее время выполнения функции, Средний размер объекта
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., str]:
        def wrapper(*args, **kwargs) -> str:
            measurements = []
            sizes = []
            for _ in range(repeat):
                start = perf_counter()
                sizes.append(getsizeof(func(*args, **kwargs)))
                measurements.append(perf_counter() - start)

            average_time = sum(measurements) / len(measurements)
            average_size = sum(sizes) / len(sizes)
            return f'Среднее время выполнения функции: {average_time}\nСредний размер объекта: {average_size} байт'

        if profile_enabled:
            return profile(wrapper)
        else:
            return wrapper

    return decorator
