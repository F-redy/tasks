# Функция `product` из модуля `itertools` в Python создает итератор, который возвращает декартово произведение
# одной или нескольких последовательностей. Декартово произведение представляет собой все возможные комбинации
# элементов из этих последовательностей.
#
# Синтаксис функции `product` следующий:

# itertools.product(*iterables, repeat=1)
#
# - `*iterables`: Это последовательности (например, списки, кортежи и т. д.), для которых вы хотите получить
# декартово произведение. Вы можете передать любое количество последовательностей, разделяя их запятыми.
#
# - `repeat` (необязательный): Этот параметр определяет, сколько раз каждая последовательность должна быть
# использована в произведении. По умолчанию `repeat` равен 1.
#
# Функция возвращает итератор, который можно пройти в цикле `for` или преобразовать в другие структуры данных,
# такие как список или кортеж, для получения всех комбинаций.
#
# Примеры:
#
# 1. Получение декартова произведения двух списков:

# from itertools import product
#
# list1 = [1, 2]
# list2 = ['a', 'b']
#
# result = product(list1, list2)
#
# for item in result:
#     print(item)

# Вывод:
# (1, 'a')
# (1, 'b')
# (2, 'a')
# (2, 'b')
#
# 2. Получение декартова произведения трех кортежей с повторением:
# from itertools import product
#
# tuple1 = ('x', 'y')
# tuple2 = ('1', '2')
# tuple3 = ('A', 'B')
#
# result = product(tuple1, tuple2, tuple3, repeat=2)
#
# for item in result:
#     print(item)

# Вывод:
# ('x', '1', 'A', 'x', '1', 'A')
# ('x', '1', 'A', 'x', '1', 'B')
# ('x', '1', 'A', 'x', '2', 'A')
# ('x', '1', 'A', 'x', '2', 'B')
# ('x', '1', 'A', 'y', '1', 'A')
# ('x', '1', 'A', 'y', '1', 'B')
# ('x', '1', 'A', 'y', '2', 'A')
# ('x', '1', 'A', 'y', '2', 'B')
# ('x', '1', 'B', 'x', '1', 'A')
# ('x', '1', 'B', 'x', '1', 'B')

#
# Функция `product` полезна, когда вам нужно создать все возможные комбинации элементов из нескольких
# последовательностей, и эта функция позволяет контролировать повторение каждой последовательности в комбинациях
# с помощью параметра `repeat`.

#
# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

# Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.
#
# Input Format
#
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.
#
# Both lists have no duplicate integer elements.
#
# Output Format
#
# Output the space separated tuples of the cartesian product.
#
# Sample Input
#
#  1 2
#  3 4
# Sample Output
#
# (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product

a = map(int, input().split())
b = map(int, input().split())
print(list(product(a, b)))
