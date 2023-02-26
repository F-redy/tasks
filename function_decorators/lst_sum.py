#  Вводится строка целых чисел через пробел.
#  Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.
#
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
#
# s = input()
#
# Результат отобразите на экране.
#
# Sample Input:
# 5 6 3 6 -4 6 -1
# Sample Output:
# 26


from functools import wraps


def start_value(start: int):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start

        return wrapper

    return real_decorator


@start_value(start=5)
def into_lst_sum(string: str) -> int:
    return sum(map(int, string.split()))


s = input()
print(into_lst_sum(s))
