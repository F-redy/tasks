# Длинные строки
# Условие:
# Дан большой текст, который состоит из нескольких строк, он находится в переменной text.
#
# Найдите все строки в этой переменной, которые состоят только из символов ^ и $.
#
# Что нужно сделать:
# Из всех строк в переменной text найти только те, которые полностью состоят из символов ^$
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Список строк, которые получилось найти.

import re
import sys

test_case = [
    ("""$$^^$^$$4^^$^^$$$
^$^$
^$$^$^^^$^^$$^$$$$
^^^^$$S^$^$^$^$^^$$
    """, ['^$^$', '^$$^$^^^$^^$$^$$$$']),
    ("""^^^^^$$$$$^$^$$^$^d
$$$$^$^$$$$^^^$^^^
        """, ['$$$$^$^$$$$^^^$^^^'])
]

pattern = re.compile(r"^[\^\$]+$", flags=re.M)

# text = ''.join(sys.stdin.readlines())
# print(re.findall(r"(?m)привет", text))  # v1
# print(re.findall(r"привет", text, flags=re.M))  # v2
# print(re.findall(r"привет", text, flags=re.MULTILINE))  # v3
# print(re.findall(r"привет", text, flags=8))  # v4
# print(re.compile(r"привет", flags=8).findall(text))  # v5
for i, (test, answer) in enumerate(test_case):
    result = pattern.findall(test)
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
