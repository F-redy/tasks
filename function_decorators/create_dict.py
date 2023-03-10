#  Вводятся две строки из слов (слова записаны через пробел).
#  Объявите функцию, которая преобразовывает эти две строки в два списка слов и возвращает эти списки.
#
# Определите декоратор для этой функции, который из двух списков формирует словарь,
# в котором ключами являются слова из первого списка,
# а значениями - соответствующие элементы из второго списка.
# Полученный словарь должен возвращаться при вызове декоратора.
#
# Примените декоратор к первой функции и вызовите ее для введенных строк.
# Результат (словарь d) отобразите на экране командой:
#
# print(*sorted(d.items()))
#
# Sample Input:
# house river tree car
# дом река дерево машина
# Sample Output:
# ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')

def create_dict(func):
    def wrapper(*args, **kwargs):
        return dict(zip(*func(*args, **kwargs)))

    return wrapper


@create_dict
def create_lst(*args):
    return [s.split() for s in args]


if __name__ == '__main__':
    first = input()
    second = input()

    d = create_lst(first, second)
    print(*sorted(d.items()))
