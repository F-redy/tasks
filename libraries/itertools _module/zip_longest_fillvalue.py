from itertools import zip_longest

# В zip_longest можно передать аргумент fillvalue, который помогает заполнить недостающие значения.
# Если не передать значения будут заполняться None


ids = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
countries = ('Australia', 'USA')
records = zip_longest(ids, leaders, countries)

print(list(records))

records_2 = zip_longest(ids, leaders, countries, fillvalue='Unknown')
print(list(records_2))