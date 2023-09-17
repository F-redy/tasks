# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
#
# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

# Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.
#
# Input Format
#
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.
#
# Both lists have no duplicate integer elements.
#
# Output Format
#
# Output the space separated tuples of the cartesian product.
#
# Sample Input
#
#  1 2
#  3 4
# Sample Output
#
# (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product

a = map(int, input().split())
b = map(int, input().split())
print(list(product(a, b)))
