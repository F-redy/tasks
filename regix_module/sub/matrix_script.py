# Neo has a complex matrix script. The matrix script is a N X N grid of strings.
# It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
#
# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them.
# Neo reads the column from top to bottom and starts reading from the leftmost column.
#
# If there are symbols or spaces between two alphanumeric characters of the decoded script,
# then Neo replaces them with a single space '' for better readability.
#
# Neo feels that there is no need to use 'if' conditions for decoding.
#
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
#
# Input Format
#
# The first line contains space-separated integers N (rows) and M (columns) respectively.
# The next N lines contain the row elements of the matrix script.

# Output Format
# Print the decoded matrix script.
#
# Sample Input 0
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!

# Sample Output 0
# This is Matrix#  %!


import re

n, m = map(int, input().strip().split())
matrix = [input() for _ in range(n)]

print(re.sub(r"(?<=\w)(\W+)(?=\w)", " ", "".join(matrix[row][item] for item in range(m) for row in range(n))))
