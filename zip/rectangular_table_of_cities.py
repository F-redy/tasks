#  Вводится строка из слов, записанных через пробел.
#  Необходимо на их основе составить прямоугольную таблицу из трех столбцов и N строк
#  (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
#  Реализовать эту программу с использованием функции zip.
#  Результат отобразить на экране в виде прямоугольной таблицы из слов, записанных через пробел (в каждой строчке).
#
# Sample Input:
# Львів Київ Одеса Харків Дніпро Луцьк Чернівці Житомир Тернопіль Рівне
# Sample Output:
# Львів Київ Одеса
# Харків Дніпро Луцьк
# Чернівці Житомир Тернопіль

for row in zip(*[iter(input().split())] * 3):
    print(*row)

# v2
# words = input().split()
# num_rows = len(words) // 3
# table = list(zip(words[:num_rows], words[num_rows:num_rows*2], words[num_rows*2:num_rows*3]))
#
# for row in table:
#     print(" ".join(row))
