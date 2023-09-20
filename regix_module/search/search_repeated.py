# В регулярных выражениях \1 является обратной ссылкой на первую захваченную группу.
# В конкретном регулярном выражении r"([A-Za-z0-9])\1", оно используется для поиска последовательностей символов,
# которые состоят из одного и того же символа повторяющегося дважды подряд.

# \1 - Это обратная ссылка на первую (и единственную) группу захвата.
# Она требует, чтобы символ, найденный в группе захвата, повторялся сразу после первого символа.
# Таким образом, она ищет последовательности, в которых один и тот же символ повторяется дважды подряд.

# Task
#
# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character in  S(read from left to right)
# that has consecutive repetitions.
#
# Input Format
#
# A single line of input containing the string S.
#
# Output Format
#
# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
#
# Sample Input
# ..12345678910111213141516171820212223
#
# Sample Output
# 1


import re

pattern = re.compile(r"([A-Za-z0-9])\1")
m = re.search(pattern, input())
if m:
    print(m.group(1))
else:
    print(-1)
