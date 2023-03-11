#  Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map,
#  которая бы возвращала названия городов только длиной более 5 символов.
#  Вместо остальных названий - строку с дефисом ("-").
#  Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.
#
# Sample Input:
# Харьков Львов Бахмут Одесса Луцк Мариуполь
# Sample Output:
# Харьков - Бахмут Одесса - Мариуполь

# v1
def map_cities(cities_string: str) -> list[str]:
    return [('-', city)[len(city) > 5] for city in cities_string.split()]


print(*map_cities(input()))

# v2
cities = map(lambda x: ('-', x)[len(x) > 5], input().split())
print(*cities)