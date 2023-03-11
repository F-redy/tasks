# Вводится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу,
# приведя ее к прямоугольному виду, отбросив выходящие элементы.
# Вывести результат на экран в виде такой же таблицы чисел.

# Sample Input:
# 1 2 3 4 5 6
# 3 4 5 6
# 7 8 9
# 9 7 5 3 2
# Sample Output:
# 1 2 3
# 3 4 5
# 7 8 9
# 9 7 5

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

t = zip(*[map(int, lst.split()) for lst in lst_in])
for k in zip(*t):
    print(*k)
