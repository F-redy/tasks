# Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:
#
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса
# с доменом mail.ru и длиной в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru
#
# Для формирования случайного индекса для строки chars используйте функцию randint модуля random:
#
# import random
# random.seed(1)
# indx = random.randint(0, len(chars)-1)
# Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно.
# Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
#
# Sample Input:
# 8
# Sample Output:
# iKZWeqhF@mail.ru
# WCEPyYng@mail.ru
# FbyBMWXa@mail.ru
# SCrUZoLg@mail.ru
# ubbbPIay@mail.ru

from random import choice, seed
from string import ascii_lowercase, ascii_uppercase
from typing import Generator

seed(1)
chars = ascii_lowercase + ascii_uppercase


def generator_email(length: int, domen: str = '@gmail.com') -> Generator[str, None, None]:
    while True:
        yield ''.join(choice(chars) for _ in range(length)) + domen


n = int(input())
email = generator_email(n, domen='@mail.ru')
[print(next(email)) for _ in range(5)]
