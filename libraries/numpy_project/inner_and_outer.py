# Task
#
# You are given two arrays: A and B.
# Your task is to compute their inner and outer product.
#
# Input Format
#
# The first line contains the space separated elements of array A.
# The second line contains the space separated elements of array B.
#
# Output Format
#
# First, print the inner product.
# Second, print the outer product.

import numpy

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print(numpy.inner(A, B))
print(numpy.outer(A, B))
