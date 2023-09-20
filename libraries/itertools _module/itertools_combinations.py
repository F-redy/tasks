# Функция `combinations` из модуля `itertools` в Python создает итератор, который генерирует все возможные комбинации
# элементов из входной последовательности без повторений, заданной длины.
#
# Синтаксис функции `combinations` следующий:

# itertools.combinations(iterable, r)

# - `iterable`: Это исходная последовательность (например, строка, список или кортеж),
# из которой будут генерироваться комбинации.
#
# - `r` (необязательный): Этот параметр определяет длину комбинаций.
# Если он не указан, то по умолчанию используется длина исходной последовательности.
# Если `r` указан, то будут сгенерированы только комбинации заданной длины.
#
# Функция возвращает итератор, который вы можете пройти в цикле `for` или передать в другие функции,
# такие как `list()` для получения списка всех комбинаций.
#
# Примеры:
# 1. Генерация всех комбинаций из трех элементов:
# from itertools import combinations
#
# elements = [1, 2, 3]
# combinations_result = combinations(elements, 2)
#
# for comb in combinations_result:
#     print(comb)
#
# Вывод:
# (1, 2)
# (1, 3)
# (2, 3)
#
# 2. Генерация всех комбинаций из четырех элементов:
# from itertools import combinations
#
# elements = [1, 2, 3, 4]
# combinations_result = combinations(elements, 3)
#
# for comb in combinations_result:
#     print(comb)

# Вывод:
# (1, 2, 3)
# (1, 2, 4)
# (1, 3, 4)
# (2, 3, 4)
#
# Функция `combinations` полезна, когда вам нужно создать комбинации элементов для решения задач,
# связанных с выбором наборов элементов из некоторого множества.

# Task
#
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
#
# Input Format
#
# A single line containing the string S and integer value k separated by a space.

# Output Format
#
# Print the different combinations of string S on separate lines.

# Sample Input
#
# HACK 2
# Sample Output
#
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK


from itertools import combinations

string, size = input().split()
combination_list = []
for i in range(int(size)):
    combination_list += list(combinations(sorted(string), i + 1))
print("\n".join(list(map(''.join, combination_list))))
