# На вход программы поступает строка в формате:
#
# предмет_1=вес_1
# ...
# предмет_N=вес_N
#
# Веса предметов заданы целыми числами. Необходимо на основе этих данных сформировать словарь и, затем,
# на основе этого словаря сформировать список предметов по убыванию их веса.
# (В списке должны находиться только наименования предметов без их весов).
#
# Отобразить полученный результат в виде строки с названиями через пробел.
#
# Sample Input:
# ножницы=100
# котелок=500
# спички=20
# зажигалка=40
# зеркальце=50

# Sample Output:
# котелок ножницы зеркальце зажигалка спички

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

items_dict = {item: int(weight) for item, weight in [row.split('=') for row in lst_in]}

print(*sorted(items_dict, key=lambda weight: -items_dict[weight]))

# v2
items_dct = dict(line.split("=") for line in lst_in)

print(*sorted(items_dct, key=lambda x: -int(items_dct.get(x))))

# v3
items_d = {item: int(weight) for item, weight in [row.split('=') for row in lst_in]}

print(*sorted(items_dct, key=items_d.get, reverse=True))
