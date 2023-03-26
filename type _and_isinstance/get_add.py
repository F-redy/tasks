# Определите функцию с именем get_add,
# которая складывает или два числа, или две строки (но не число со строкой) и возвращает полученный результат.
# Если сложение не может быть выполнено, то функция возвращает значение None. Сигнатура функции должна быть, следующей:
#
# def get_add(a, b): ...
#
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.


# v1
def get_add(a, b):
    d = (int, float)
    if type(a) in d and type(b) in d:
        return a + b
    if type(a) == str and type(b) == str:
        return a + b


# v2
def get_add_1(a, b):
    tset = {type(a), type(b)}
    if tset <= {int, float} or tset == {str}:
        return a + b
