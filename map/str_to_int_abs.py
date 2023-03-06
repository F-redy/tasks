#  На вход поступает строка из целых чисел, записанных через пробел.
#  С помощью функции map преобразовать эту строку в список целых чисел, взятых по модулю.
#  Сформируйте именно список lst из таких чисел. Отобразите его на экране в виде набора чисел, идущих через пробел.
#
# Sample Input:
# -5 6 8 11 -10 0
# Sample Output:
# 5 6 8 11 10 0

s = input().split()

# v1 - print(*map(lambda x: abs(int(x)), input().split()))
lst = list(map(lambda x: abs(int(x)), s))
print(*lst)

# v2 - print(*map(abs, map(int, input().split())))
lst1 = list(map(abs, map(int, s)))
print(*lst1)
