# Функция `combinations_with_replacement` из модуля `itertools` в Python создает итератор, который
# генерирует все возможные комбинации элементов из входной последовательности с повторениями, заданной длины.
#
# Синтаксис функции `combinations_with_replacement` следующий:

# itertools.combinations_with_replacement(iterable, r)

# - `iterable`: Это исходная последовательность (например, строка, список или кортеж),
# из которой будут генерироваться комбинации с повторениями.
#
# - `r` (необязательный): Этот параметр определяет длину комбинаций. Если он не указан,
# то по умолчанию используется длина исходной последовательности. Если `r` указан,
# то будут сгенерированы только комбинации заданной длины.
#
# Функция возвращает итератор, который вы можете пройти в цикле `for` или передать в другие функции,
# такие как `list()` для получения списка всех комбинаций.
#
# Примеры:
# 1. Генерация всех комбинаций с повторениями из трех элементов:
# from itertools import combinations_with_replacement
#
# elements = [1, 2, 3]
# combinations_result = combinations_with_replacement(elements, 2)
#
# for comb in combinations_result:
#     print(comb)

# Вывод:
# (1, 1)
# (1, 2)
# (1, 3)
# (2, 2)
# (2, 3)
# (3, 3)
#
# 2. Генерация всех комбинаций с повторениями из четырех элементов:
# from itertools import combinations_with_replacement
#
# elements = [1, 2, 3, 4]
# combinations_result = combinations_with_replacement(elements, 3)
#
# for comb in combinations_result:
#     print(comb)
#
# Вывод:
# (1, 1, 1)
# (1, 1, 2)
# (1, 1, 3)
# (1, 1, 4)
# (1, 2, 2)
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 3)
# (1, 3, 4)
# (1, 4, 4)
# (2, 2, 2)
# (2, 2, 3)
# (2, 2, 4)
# (2, 3, 3)
# (2, 3, 4)
# (2, 4, 4)
# (3, 3, 3)
# (3, 3, 4)
# (3, 4, 4)
# (4, 4, 4)
#
# Функция `combinations_with_replacement` полезна, когда вам нужно создать комбинации элементов
# с возможностью повторений, например, при генерации всех возможных наборов элементов для задач,
# связанных с выбором из множества с возвращением.

# Task
# You are given a string S.
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.
#
# Input Format
#
# A single line containing the string S and integer value k separated by a space.
#
# Output Format
#
# Print the combinations with their replacements of string  on separate lines.
#
# Sample Input
# HACK
# 2
#
# Sample Output
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

from itertools import combinations_with_replacement

string, k = input().split()
for combinations in combinations_with_replacement(sorted(string), int(k)):
    print(''.join(combinations))
