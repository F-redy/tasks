# Функция `groupby` из модуля `itertools` в Python используется для группировки элементов последовательности
# на основе ключа. Она создает итератор, который генерирует пары, состоящие из ключа и соответствующей
# ему группы элементов из исходной последовательности. Каждая группа представляет собой последовательность элементов,
# которые имеют одинаковые значения ключа.
#
# Синтаксис функции `groupby` следующий:

# itertools.groupby(iterable, key=None)
#
# - `iterable`: Это исходная последовательность, элементы которой будут группироваться.
#
# - `key` (необязательный): Это функция, которая определяет ключ для группировки элементов. Если `key` не указан, то
# элементы будут группироваться на основе самих себя(т.е., одинаковые элементы будут считаться ключами для группировки).
#
# Функция `groupby` возвращает итератор, который генерирует пары
# `(key, group)`, где `key` - ключ для группы, и `group` - итератор, содержащий элементы из исходной последовательности,
# отнесенные к этой группе.
#
# Примеры:
#
# 1. Группировка списка слов по их первой букве:
# from itertools import groupby
#
# words = ['apple', 'banana', 'cherry', 'avocado', 'blueberry', 'date']
#
# # Определение ключа для группировки - первая буква слова
# key_func = lambda x: x[0]
#
# # Группировка слов по первой букве
# groups = groupby(sorted(words), key=key_func)
#
# for key, group in groups:
#     print(key, list(group))
#
# Вывод:
# a ['apple', 'avocado']
# b ['banana', 'blueberry']
# c ['cherry']
# d ['date']
#
# 2. Группировка списка чисел по четности/нечетности:
#
# from itertools import groupby
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# # Определение ключа для группировки - четность/нечетность числа
# key_func = lambda x: "Even" if x % 2 == 0 else "Odd"
#
# # Группировка чисел по четности/нечетности
# groups = groupby(numbers, key=key_func)
#
# for key, group in groups:
#     print(key, list(group))
#
# Вывод:
# Odd [1]
# Even [2]
# Odd [3]
# Even [4]
# Odd [5]
# Even [6]
# Odd [7]
# Even [8]
#
# Функция `groupby` полезна, когда вам нужно разбить последовательность элементов на группы на основе какого-либо
# критерия или ключа, и обрабатывать каждую группу отдельно.


# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
# Replace these consecutive occurrences of the character 'c' with (X, c) in the string.
#
# For a better understanding of the problem, check the explanation.
#
# Input Format
# A single line of input consisting of the string S.
#
# Output Format
# A single line of output consisting of the modified string.
#
# Constraints
# All the characters of S denote integers between 0 and 9.
#
# Sample Input
# 1222311
#
# Sample Output
# (1, 1) (3, 2) (1, 3) (2, 1)


from itertools import groupby

print(*((len(list(group)), key) for key, group in groupby(map(int, input()))))
