# На вход поступает список целых чисел, записанных в одну строчку через пробел.
# Преобразуйте сначала эту строку в список из целых чисел, а затем список в кортеж из целых чисел.
# То есть, в программе будет две разные коллекции: список и кортеж.
# Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно,
# а иначе - примените функцию sorted.
#
# На экран ничего выводить не нужно, только сформировать две отсортированные коллекции:
# lst (список) - результат сортировки списка; tp_lst (кортеж) - результат сортировки кортежа.
#
# P. S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
#
# Sample Input:
# -2 -1 8 11 4 5
# Sample Output:
# -2 -1 4 5 8 11

from typing import Union

s = input()

lst = list(map(int, s.split()))
lst.sort()
tp_lst = tuple(lst)
print(lst)
print(tp_lst)

# v2
def sorted_anyway(array: Union[list[int], tuple[int], set[int]], rev: bool = False) -> Union[list[int], tuple[int]]:
    """
    Function sorts the input collection
    :param array: list, tuple, or set of integers.
    :param rev: sorting False - ascending, True - descending
    :return: sorted collection.
    """
    try:
        array.sort(reverse=rev)
    except AttributeError:
        array = tuple(sorted(array, reverse=rev))

    return array


def data_type_change(data_type, string: str) -> Union[list[int], tuple[int], set[int]]:
    """
    Function converts a string of space-separated integers to the specified collection type.
    :param data_type: the type of the collection to convert the string to.
    :param string: string with integers separated by spaces.
    :return: collection of integers.
    """
    return data_type(map(int, string.split()))



print(sorted_anyway(data_type_change(list, s)))
print(sorted_anyway(data_type_change(tuple, s)))
print(sorted_anyway(data_type_change(set, s), rev=True))
