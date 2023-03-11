# Вводится таблица целых чисел. Необходимо сначала эту таблицу представить двумерным списком чисел,
# а затем, с помощью функции zip выполнить транспонирование этой таблицы
# (то есть, строки заменить на соответствующие столбцы).
# Результат вывести на экран в виде таблицы чисел (числа в строках следуют через пробел).
#

# Sample Input:
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# Sample Output:
# 1 5 9
# 2 6 8
# 3 7 7
# 4 8 6

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
two_dimensional_lst = [list(map(int, lst.split())) for lst in lst_in]
for row in zip(*two_dimensional_lst):
    print(*row)
