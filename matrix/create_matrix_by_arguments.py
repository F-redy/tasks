# Ваша задача создать функцию create_matrix, которая принимает
#
# необязательный числовой параметр size - размер квадратной матрицы, по умолчанию принимает значение 3;
# необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше главной диагонали.
# По умолчанию равен 0;
# необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся ниже главной диагонали.
# По умолчанию равен 0;
# Функция create_matrix должна возвращать квадратную матрицу размером size х size,
# на диагонали которой располагаются числа от 1 до size.
# Все остальные элементы заполнены согласно параметрам up_fill и down_fill.
#
# create_matrix() => [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
# create_matrix(4) => [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
#
# create_matrix(up_fill=7) => [[1, 7, 7],
#                              [0, 2, 7],
#                              [0, 0, 3]]
#
# create_matrix(up_fill=7, down_fill=9) => [[1, 7, 7],
#                                           [9, 2, 7],
#                                           [9, 9, 3]]
#
#
# create_matrix(size=4, up_fill=7, down_fill=9) => [[1, 7, 7, 7],
#                                                   [9, 2, 7, 7],
#                                                   [9, 9, 3, 7],
#                                                   [9, 9, 9, 4]]


# v1
def create_matrix_v1(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list[list[int]]:
    matrix = []
    for i in range(size):
        tmp_lst = []
        for j in range(size):
            if i == j:
                tmp_lst.append(i + 1)
            elif i > j:
                tmp_lst.append(down_fill)
            else:
                tmp_lst.append(up_fill)
        matrix.append(tmp_lst)
    return matrix


# v2
def create_matrix_v2(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list[list[int]]:
    return [[down_fill] * i + [i + 1] + [up_fill] * (size - i - 1) for i in range(size)]
