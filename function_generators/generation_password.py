#  Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор,
#  которая бы выдавала пароль длиной N символов из случайных букв, цифр и некоторых других знаков.
#  Для получения последовательности допустимых символов для генерации паролей в программе импортированы две строки:
#  ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:
#
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N
# и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз.
# Сгенерировать случайный индекс indx в диапазоне [a; b] для символа можно с помощью функции randint модуля random:
#
# import random
# random.seed(1)
# indx = random.randint(a, b)
# Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).
#
# Sample Input:
# 10
# Sample Output:
# riGp?58WAm
# !dX3a5IDnO
# dcdbWB2d*C
# 4?DSDC6Lc1
# mxLpQ@2@yM


from string import ascii_lowercase, ascii_uppercase
from random import randint, seed, choice
from typing import Generator

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
seed(1)


def generation_password(length: int) -> Generator[str, None, None]:
    while True:
        yield ''.join(choice(chars) for _ in range(length))
        # через randint:
        # yield ''.join(chars[randint(0, len(chars) - 1)] for _ in range(length))


n = int(input())
passwords = generation_password(n)

[print(next(passwords)) for _ in range(5)]
