# Вводится список из целых чисел в одну строчку через пробел.
# Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием.
# Функция должна возвращать новый отсортированный список.
# Вызовите результирующую функцию сортировки для введенного списка и
# отобразите результат на экран в виде последовательности чисел, записанных через пробел.
#
# Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.

# Sample Input:
# 8 11 -6 3 0 1 1
# Sample Output:
# -6 0 1 1 3 8 11


def merge_two_lists(a, b):
    res = []
    while a and b:
        res += [a.pop(0) if a[0] < b[0] else b.pop(0)]
    return res + a + b


def merge_sort(l):
    if len(l) == 1:
        return l
    mid = len(l) // 2
    a, b = l[:mid], l[mid:]
    return merge_two_lists(merge_sort(a), merge_sort(b))


l = [int(i) for i in input().split()]
print(*merge_sort(l))
