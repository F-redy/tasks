# Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum,
# которая бы возвращала текущую сумму чисел последовательности длины N в диапазоне целых чисел [1; N]. Например:
#
# - для первого числа 1 сумма равна 1;
# - для второго числа 2 сумма равна 1+2 = 3
# ....
# - для N-го числа сумма равна 1+2+...+(N-1)+N
#
# Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только определить.
#
# Sample Input:
# 5
# Sample Output:
# 1 3 6 10 15
from typing import Generator


def get_sum(num: int) -> Generator[int, None, None]:
    current_sum = 0
    for i in range(1, num + 1):
        current_sum += i
        yield current_sum


n = int(input("Введите натуральное число: "))
print(*list(get_sum(n)))
