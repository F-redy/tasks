#  На вход программы поступают два списка целых чисел (каждый в отдельной строке),
#  записанных в одну строчку через пробел. Длины списков могут быть разными.
#  Необходимо первый список отсортировать по возрастанию, а второй - по убыванию.
#  Полученные пары из обоих списков сложить друг с другом и получить новый список чисел.
#  Результат вывести на экран в виде строки чисел через пробел.
#
# P. S. Подсказка: не забываем про функцию zip.
#
# Sample Input:
# 7 6 4 2 6 7 9 10 4
# -4 5 10 4 5 65
# Sample Output:
# 67 14 9 11 10 3

lst1 = sorted(map(int, input().split()))
lst2 = sorted(map(int, input().split()), reverse=True)
print(*map(sum, zip(lst1, lst2)))