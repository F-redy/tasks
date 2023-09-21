# Task
#
# You are given a text of N lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
#
# && → and
# || → or
#
# Both && and || should have a space " " on both sides.
#
# Input Format
#
# The first line contains the integer, N.
# The next N lines each contain a line of the text.
#
# Constraints
# 0 < N < 100
#
# Neither && nor || occur in the start or end of each line.
#
# Output Format
#
# Output the modified text.
#
#
# Sample Input
# 11
# a = 1;
# b = input();
#
# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.
#
# Sample Output
# a = 1;
# b = input();
#
# if a + b > 0 and a - b < 0:
#     start()
# elif a*b > 10 or a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.

import re

pattern = re.compile(r"(?<=\s)(&&|\|\|)(?=\s)")

for _ in range(int(input())):
    print(pattern.sub(lambda match: ("or", "and")[match.group(0) == '&&'], input()))
