# На вход программы поступает список товаров в формате:

# название_1:цена_1
# ...
# название_N:цена_N

# Необходимо преобразовать этот список в словарь, ключами которого выступают цены (целые числа),
# а значениями - соответствующие названия товаров. Необходимо написать функцию,
# которая бы принимала на входе словарь и возвращала список из наименований трех наиболее дешевых товаров.

# Вызовите эту функцию и отобразите на экране полученный список в порядке возрастания
# цены в одну строчку через пробел.

# Sample Input:
# смартфон:120000
# яблоко:2
# сумка:560
# брюки:2500
# линейка:10
# бумага:500

# Sample Output:
# яблоко линейка бумага

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


def find_three_cheapest_products(products_dict: dict) -> list:
    return [item for _, item in sorted(products_dict.items())[:3]]


products = dict([(int(key), value) for value, key in [string.split(':') for string in lst_in]])

print(*find_three_cheapest_products(products))
