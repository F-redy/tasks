# Используя замыкания функций, объявите внутреннюю функцию,
# которая преобразует строку из списка целых чисел, записанных через пробел,
# либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
#
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp;
# вторая - список целых чисел, записанных через пробел.
# С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.

# Sample Input:
# list
# -5 6 8 11 0 111 -456 3
# Sample Output:
# [-5, 6, 8, 11, 0, 111, -456, 3]

def parse(tp: str = 'list'):
    def inner(s: str) -> tuple[int] | list[int]:
        return (tuple, list)[tp == 'list'](map(int, s.split()))

    return inner


pr = parse(input())
print(pr(input()))
