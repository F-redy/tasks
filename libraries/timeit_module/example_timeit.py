import sys
from timeit import timeit

code = """
words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 'drop', 'produce', 'acquisition',
         'cheap', 'strength', 'master', 'perception', 'noise', 'strange', 'am'] * 1000000

lens = map(len, words)

for i in lens:
    a = i
"""

time_result_list = tuple()
for _ in range(10):
    time_result_list += timeit(code, number=1),

print(f"Время выполнения: {sum(time_result_list) / len(time_result_list)} сек.")
print(f"Размер всех элементов кортежа: {sys.getsizeof(time_result_list)} байт.")
# execution_time = timeit(code, number=1)
# print(f"Время выполнения: {execution_time} сек.")
