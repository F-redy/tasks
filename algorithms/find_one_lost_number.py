# Есть массив натуральных чисел от 1 до n, в любой последовательности.
# Из этого массива удалили 1 случайное число.
# Напишите функцию, которая находит и возвращает это число.
# Если массив пустой функция должна вернуть 1.

def find_lost_number(lst: list[int]) -> int:
    n = len(lst) + 1
    total_sum = (n * (n + 1)) // 2
    return total_sum - sum(lst)


test_case = [
    (2, [1, 3, 4]),  # массив отсортирован по возрастанию, удалено число 2
    (1, [2, 3]),  # массив отсортирован по возрастанию, удалено число 1
    (2, [8, 7, 6, 5, 4, 3, 1]),  # массив отсортирован по убыванию, удалено число 2
    (3, [1, 2, 4]),  # массив отсортирован по возрастанию, удалено число 3
    (8, [5, 9, 1, 6, 7, 2, 3, 4]),  # случайный порядок чисел, удалено число 8
    (4, [1, 2, 3, 5, 6, 7, 8]),  # массив отсортирован по возрастанию, удалено число 4
    (3, [1, 2, 4, 5]),  # массив отсортирован по возрастанию, удалено число 3
    (1, []),  # Пустой массив. Вернуть 1
    (5, [1, 2, 3, 4]),  # массив отсортирован по возрастанию, удалено число 5
    (3, [1, 2, 4, 5, 6, 7, 8]),  # массив отсортирован по возрастанию, удалено число 3
    (10, [1, 5, 7, 8, 6, 2, 3, 9, 4]),  # случайный порядок чисел, удалено число 10
]


def tests():
    for i, case in enumerate(test_case, 1):
        answer, test_arr = case
        res = find_lost_number(test_arr)
        assert res == answer, AssertionError(f'Ожидали: {answer}, получили: {res}')
        print(f'Test_{i} - OK')


tests()