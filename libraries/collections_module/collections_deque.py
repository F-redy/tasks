# # A deque is a double-ended queue. It can be used to add or remove elements from both ends.
# #
# # Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately
# #     the same O(1) performance in either direction.
# #
# # deque() methods: https://docs.python.org/2/library/collections.html#deque-objects
# # Deque Recipes: https://docs.python.org/2.7/library/collections.html#deque-recipes
#
# Task
#
# Perform append, pop, popleft and appendleft methods on an empty deque d.
#
# Input Format
#
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.
#
# Output Format
#
# Print the space separated elements of deque d.
#
# Sample Input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output
# 1 2

from collections import deque

d = deque()
for _ in range(int(input())):
    line = input()
    try:
        method, value = line.split()
        eval(f'd.{method}(value)')
    except ValueError:
        eval(f'd.{line}()')
print(*d)
