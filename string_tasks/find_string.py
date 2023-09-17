# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
#
# NOTE: String letters are case-sensitive.
#
# Input Format
#
# The first line of input contains the original string. The next line contains the substring.

# Output Format
#
# Output the integer number indicating the total number of occurrences of the substring in the original string.
#
# Sample Input
#
# ABCDCDC
# CDC
#
# Sample Output
#
# 2

def count_substring(string, sub_string):
    count = 0
    substring_length = len(sub_string)

    for i in range(len(string) - substring_length + 1):
        count += string[i:i + substring_length] == sub_string

    return count
