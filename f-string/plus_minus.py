# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with places after the decimal.
#
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
# though answers with absolute error of up to are acceptable.
#
# For example, given the array there are elements, two positive, two negative and one zero.
# Their ratios would be , and . It should be printed as:
# arr = [1, 1, 0, -1, -1]
# 0.400000
# 0.400000
# 0.200000

#
# Output Format
# Print the following  lines, each to  decimals:
# proportion of positive values
# proportion of negative values
# proportion of zeros

def plus_minus(arr: list[int]) -> None:
    n = len(arr)
    positive = negative = zeros = 0

    for num in arr:
        positive += num > 0
        negative += num < 0
        zeros += not num

    for elem in [positive, negative, zeros]:
        print("{:.6f}".format(elem / n))


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    plus_minus(lst)
