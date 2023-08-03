from time import perf_counter
from typing import Any, Callable

from memory_profiler import profile
from pympler import asizeof


def timer(repeat: int = 10, profile_enabled: bool = False) -> Callable[[Callable[..., Any]], Callable[..., str]]:
    """
    Декоратор для измерения времени выполнения функции и размера возвращаемого объекта.

    Параметры:
        repeat (int): Количество повторений измерений для получения среднего значения.
        profile_enabled (bool): Флаг, указывающий, нужно ли выполнять профилировку памяти.
                               По умолчанию установлено значение False.

    Зависимости:
        - memory-profiler: pip install memory-profiler
        - pympler: pip install pympler

    Возвращает:
        Callable[..., str]: Декорированную функцию, которая возвращает строку с информацией о среднем времени выполнения
                            и среднем размере объекта.

    Пример использования:
        @timer(repeat=5, profile_enabled=True)
        def my_function():
            # код функции

        result = my_function()  # Строка с информацией о среднем времени выполнения и среднем размере объекта
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., str]:

        def wrapper(*args, **kwargs) -> str:
            if profile_enabled:
                # Выполняем профилировку памяти только один раз перед циклом
                func_profiled = profile(func)
                func_profiled(*args, **kwargs)

            measurements = []
            sizes = []
            for _ in range(repeat):
                start = perf_counter()
                result = func(*args, **kwargs)
                measurements.append(perf_counter() - start)
                sizes.append(asizeof.asizeof(result))

            average_time = sum(measurements) / len(measurements)
            average_size = sum(sizes) / len(sizes)
            return f'Среднее время выполнения функции: {average_time}\nСредний размер объекта: {average_size} байт'

        return wrapper

    return decorator
