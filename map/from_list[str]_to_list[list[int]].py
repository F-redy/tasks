# Вводится таблица целых чисел. Используя функцию map и генератор списков,
# преобразуйте список строк lst_in (см. листинг) в двумерный список с именем lst2D, содержащий целые числа.

# Sample Input:
# 8 11 -5
# 3 4 10
# -1 -2 3
# 4 5 6
# Sample Output:
# True


import sys


def check_integers_only(lst: list[list]) -> bool:
    return all(all(isinstance(x, int) for x in row) for row in lst)


lst_in = list(map(str.strip, sys.stdin.readlines()))  # остановка ввода ctrl + D

lst2D_1 = [list(map(int, line.split())) for line in lst_in]
lst2D_2 = list(map(lambda x: list(map(int, x.split())), lst_in))

print(*[check_integers_only(lst_x) for lst_x in [lst2D_1, lst2D_2]])

[print(row1, row2) for row1, row2 in zip(lst2D_1, lst2D_2)]
