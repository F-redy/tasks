# Функция `permutations` из модуля `itertools` в Python создает итератор, который генерирует все возможные
# перестановки элементов из входной последовательности (с повторениями или без, в зависимости от параметров)
# в определенной длине.
#
# Синтаксис функции `permutations` следующий:
#
# itertools.permutations(iterable, r)
#
# - `iterable`: Это исходная последовательность (например, строка, список или кортеж),
# из которой будут генерироваться перестановки.
#
# - `r` (необязательный): Этот параметр определяет длину перестановок. Если он не указан,
# то по умолчанию используется длина исходной последовательности.
# Если `r` указан, то будут сгенерированы только перестановки заданной длины.
#
# Функция возвращает итератор, который вы можете пройти в цикле `for` или передать в другие функции,
# такие как `list()` для получения списка всех перестановок.
#
# Примеры:
#
# 1. Генерация всех перестановок из трех элементов:
# from itertools import permutations
#
# elements = [1, 2, 3]
# permutations_result = permutations(elements)
#
# for perm in permutations_result:
#     print(perm)
#
# Вывод:
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
#
# 2. Генерация всех перестановок из двух элементов:
# from itertools import permutations
#
# elements = [1, 2]
# permutations_result = permutations(elements, 2)
#
# for perm in permutations_result:
#     print(perm)
#
# Вывод:
# (1, 2)
# (2, 1)
#
# Функция `permutations` полезна, когда вам нужно исследовать все возможные комбинации
# элементов в заданной последовательности.

# Task
#
# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
#
# Input Format
#
# A single line containing the space separated string S and the integer value k.

# Output Format
#
# Print the permutations of the string  on separate lines.


from itertools import permutations

string, n = input().split()
for pair in sorted(permutations(string, int(n))):
    print(''.join(pair))
