# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.
#
# A valid UID must follow the rules below:
#
# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0 - 9).
# It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.
# Input Format
#
# The first line contains an integer T, the number of test cases.
# The next T lines contains an employee's UID.
#
# Output Format
#
# For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines.
# Do not print the quotation marks.
#
# Sample Input
#
# 2
# B1CD102354
# B1CDEF2354
# Sample Output
#
# Invalid
# Valid


import re

pattern = re.compile(r"(?x)"
                     r"^"
                     r"(?=(?:.*[A-Z]){2})"  # проверяет наличие как минимум 2 больших букв (A-Z)
                     r"(?=(?:.*[0-9]){3})"  # проверяет наличие как минимум 3 цифр (0-9)
                     r"[A-Za-z0-9]{10}$"  # общая длинна найденной строки должна быть 10 символов [A-Z0-9]
                     )

for _ in range(int(input())):
    uid = input()
    match = pattern.search(uid)
    if match and len(set(match.group(0))) == 10:
        print('Valid')
    else:
        print('Invalid')
