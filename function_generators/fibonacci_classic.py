# Генератор последовательности Фибоначчи
# Ваша задача создать функцию-генератор gen_fibonacci_numbers,
# которая принимает аргумент n и генерирует n-ое количество чисел Фибоначчи.
#
# Будем считать, что последовательность Фибоначчи такая: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
#  Ниже несколько вариантов использования:
#
# for i in gen_fibonacci_numbers(5):
#     print(i)
#
# # Будет напечатано
# # 1
# # 1
# # 2
# # 3
# # 5
# for i in gen_fibonacci_numbers(10):
#     print(i)
#
# # Будет напечатано
# # 1
# # 1
# # 2
# # 3
# # 5
# # 8
# # 13
# # 21
# # 34
# # 55
from typing import Generator


def gen_fibonacci_numbers(n: int) -> Generator[int, None, None]:
    f1, f2 = 1, 1
    for _ in range(1, n + 1):
        yield f1
        f1, f2 = f2, f1 + f2


x = 10
for i in gen_fibonacci_numbers(x):
    print(i)
