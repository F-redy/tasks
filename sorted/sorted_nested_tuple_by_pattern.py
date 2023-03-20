# Имеется таблица с данными, представленная в формате:

# Номер;Имя;Оценка;Зачет
# 1;Иванов;3;Да
# 2;Петров;2;Нет
# ...
# N;Балакирев;4;Да

# Эти данные необходимо представить в виде двумерного (вложенного) кортежа.
# Все числа должны быть представлены как целые числа. Затем, отсортировать данные так,
# чтобы столбцы шли в порядке:

# Имя;Зачет;Оценка;Номер

# Реализовать эту операцию с помощью сортировки.
# Результат должен быть представлен также в виде двумерного кортежа и присвоен переменной с именем t_sorted.

# Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.


# Sample Input:
# Номер;Имя;Оценка;Зачет
# 1;Портос;5;Да
# 2;Арамис;3;Да
# 3;Атос;4;Да
# 4;д'Артаньян;2;Нет
# 5;Балакирев;1;Нет

# Sample Output:
# True

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

# version for lesson
headers = tuple('Имя;Зачет;Оценка;Номер'.split(';'))
t = tuple(tuple(int(e) if e.isdigit() else e for e in s.split(';')) for s in lst_in)
t_sorted = tuple(zip(*sorted(zip(*t), key=lambda x: headers.index(x[0]))))


# version with output

def nice_way_out():
    """function outputs the data beautiful"""
    length = 39
    print(f" {'—' * length}")

    for obj in student_progress_log:
        name, record, mark, number = obj
        print(f"| {name:<12s} | {record:<5s} | {str(mark):>6s} |{str(number):>6s} |")

    print(f" {'—' * length}")


def change_to_nested_tuple(lst: list[str]) -> tuple[tuple[str | int]]:
    """
    Function changes a list into a nested tuple.
    :param lst: list of strings;
    :return: nested tuple of strings and numbers.
    """
    result = tuple()

    for row in lst:
        tmp = tuple()
        for obj in row.split(';'):
            tmp += int(obj) if obj.isdigit() else obj,
        result += tmp,

    return result
    # return tuple(tuple(int(obj) if obj.isdigit() else obj for obj in row.split(';')) for row in lst)


def sort_by_pattern(tpl_: tuple[tuple[str | int]], pattern: tuple[str]) -> tuple[tuple[str | int]]:
    """
    Function sorts a tuple by pattern.
    :param tpl_: nested tuple of strings and numbers;
    :param pattern: sample for sorting;
    :return: sorted nested tuple of strings and numbers.
    """
    transpose = zip(*tpl_)
    sort_matrix = sorted(transpose, key=lambda x: pattern.index(x[0]))

    return tuple(zip(*sort_matrix))
    # return tuple(zip(*sorted(zip(*tpl_order), key=lambda x: pattern.index(x[0]))))


pat = ('Имя', 'Зачет', 'Оценка', 'Номер')

tpl = change_to_nested_tuple(lst_in)
student_progress_log = sort_by_pattern(tpl, pat)

nice_way_out()
