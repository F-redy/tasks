#  Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой.
#  При реализации программы используйте функции zip и map. Выведите на экран первые три значения,
#  используя функцию next. Значения выводятся в строчку через пробел.
#  (Полагается, что три выходных значения всегда будут присутствовать).
#
# Sample Input:
# -7 8 11 -1 3
# 1 2 3 4 5 6 7 8 9 10
# Sample Output:
# -7 16 33

first, second = [map(int, input().split()) for _ in range(2)]
result = map(lambda x: x[0] * x[1], zip(first, second))
print(*(next(result) for _ in range(3)))

# v2
# lst = map(lambda x, y: x * y, first, second)
# print(*(next(lst) for _ in range(3)))
