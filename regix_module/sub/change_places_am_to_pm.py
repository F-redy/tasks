# Замена
# Условие:
# Напишите программу, которая найдёт все am и pm в тексте и заменит их друг на друга.
#
# Что нужно сделать:
# Нужно заменить все am на pm, а pm на am.
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Строка с am, заменённым на pm, и pm, заменённым на am.

import re

test_case = [
    ("It's already 12:00am and I still don't want to sleep.", "It's already 12:00pm and I still don't want to sleep."),
    (
        '2:00 am 3:00 pm 10:00 pm 3:00 am 1:00 am  5:00 am 8:00 am 7:00 am 5:00 pm 8:00 pm 7:00 pm 6:00 pm 11:00 '
        'am 4:00 am 9:00 pm 6:00 am 12:00 am 12:00 pm 9:00 am 1:00 pm 11:00 pm 4:00 pm 2:00 pm 10:00 am',
        '2:00 pm 3:00 am 10:00 am 3:00 pm 1:00 pm  5:00 pm 8:00 pm 7:00 pm 5:00 am 8:00 am 7:00 am 6:00 am 11:00 '
        'pm 4:00 pm 9:00 am 6:00 pm 12:00 pm 12:00 am 9:00 pm 1:00 am 11:00 am 4:00 am 2:00 am 10:00 pm'),
    ('pm am pm', 'am pm am')]


def func(match: re.Match):
    d = {'am': 'pm', 'pm': 'am'}
    if match[1]:
        return f'{str(d[match[1]])}'


pattern = r"(am|pm)*"

# for i, (test, answer) in enumerate(test_case, 1):
#     result = re.sub(pattern, func, test)
#     assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
#     print(f'TEST №{i} - OK\n{result}\n')
from regix_module.test_regex import test_regex

test_regex(test_case, pattern, 'sub', func)