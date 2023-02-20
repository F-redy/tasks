# С помощью рекурсивной функции get_line_list
# создать на его основе одномерный список из значений элементов списка d.
# Функция должна возвращать новый созданный одномерный список.

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(lst: list, a: list = None) -> list:
    if a is None:
        a = list()

    for elem in lst:
        if isinstance(elem, list):
            get_line_list(elem, a)
        else:
            a.append(elem)

    return a


print(get_line_list(d))
