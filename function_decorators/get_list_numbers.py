# Объявите функцию с именем get_list и следующим описанием в теле функции:
#
# '''Функция для формирования списка целых значений'''
#
# Сама функция должна формировать и возвращать список целых чисел,
# который поступает на ее вход в виде строки из целых чисел, записанных через пробел.
#
# Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
# Внутри декоратора декорируйте переданную функцию get_list
# с помощью команды @wraps (не забудьте сделать импорт: from functools import wraps).
# Такое декорирование необходимо, чтобы исходная функция get_list сохраняла свои локальные свойства:
# __name__ и __doc__.
# Примените декоратор к функции get_list.
# Sample Input:
# 8 11 -5 4 3 10
# Sample Output:
# 31
from functools import wraps


def lst_sum(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args, **kwargs))

    return wrapper


@lst_sum
def get_list(string: str) -> list[int]:
    """Функция для формирования списка целых значений"""
    return list(map(int, string.split()))


[print(obj) for obj in [get_list(input()), get_list.__name__, get_list.__doc__]]
