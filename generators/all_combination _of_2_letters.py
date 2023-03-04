# Используя символы малых букв латинского алфавита (строка ascii_lowercase):
#
# from string import ascii_lowercase
#
# запишите генератор, который бы возвращал все сочетания из двух букв латинского алфавита.
# Выведите первые 50 сочетаний на экран в строку через пробел.
#
# Например, первые семь начальных сочетаний имеют вид:
#
# aa ab ac ad ae af ag

from string import ascii_lowercase

gen = (i + j for i in ascii_lowercase for j in ascii_lowercase)

print(*(next(gen) for _ in range(50)))
