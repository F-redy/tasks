# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# For example, the square matrix arr is shown below:
# Copy code
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17.
# Their absolute difference is |15 - 17| = 2.
#
# Function description:
# Complete the diagonalDifference function in the editor below.
# diagonalDifference takes the following parameter:
#
# arr: an array of integers .
# Return:
#
# integer: the absolute diagonal difference.
# Input Format:
# The first line contains a single integer, n, the number of rows and columns in the matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].
#
# Constraints:
#
# -100 <= arr[i][j] <= 100
# Output Format:
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.


# tests testing/test_diagonal_difference.py

def diagonal_difference(arr: list, x: int) -> int:
    primary = sum(arr[i][i] for i in range(x))
    secondary = sum(arr[i][x - i - 1] for i in range(x))
    return abs(primary - secondary)


if __name__ == '__main__':
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    print(diagonal_difference(lst, n))
