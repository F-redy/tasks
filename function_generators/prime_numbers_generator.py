# Определите функцию-генератор, которая бы возвращала простые числа.
# (Простое число - это натуральное число, которое делится только на себя и на 1).
# Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.


from typing import Generator


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generator_natural_number() -> Generator[int, None, None]:
    start = 2
    while True:
        if is_prime(start):
            yield start
        start += 1


# version 2
def prime_gen() -> Generator[int, None, None]:
    for i in range(2, 10 ** 10):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            yield i


number = generator_natural_number()
g = prime_gen()

[print(next(number), end=' ') for _ in range(20)]
print()
[print(next(g), end=' ') for _ in range(20)]
