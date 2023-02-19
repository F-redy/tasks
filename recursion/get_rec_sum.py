# Вводится список целых чисел в одну строчку через пробел.
# Необходимо вычислить сумму этих введенных значений,
# используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum.
# Функция должна возвращать значение суммы. (Выводить на экран она ничего не должна).

# Sample Input:
# 8 11 -5 4 3
# Sample Output:
# 21

numbers = list(map(int, input().split()))


def get_rec_sum(lst):
    if lst:
        return lst.pop() + get_rec_sum(lst)
    return 0


print(get_rec_sum(numbers))
