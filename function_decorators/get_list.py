# На вход программы поступает строка из целых чисел, записанных через пробел.
# Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел
# и возвращает его. Определите декоратор для этой функции,
# который сортирует список чисел по возрастанию.
# Результат сортировки должен возвращаться при вызове декоратора.
#
# Вызовите декорированную функцию get_list и
# отобразите полученный отсортированный список lst командой:
#
# print(*lst)
#
# Sample Input:
# 8 11 -5 4 3 10
# Sample Output:
# -5 3 4 8 10 11
def sorted_list(func):
    def wrapper(*args, **kwargs):
        lst_sorted = sorted(func(*args, **kwargs))
        return lst_sorted

    return wrapper


@sorted_list
def get_list(string: str) -> list[int]:
    return list(map(int, string.split()))


if __name__ == '__main__':
    s = input()
    lst = get_list(s)
    print(*lst)
