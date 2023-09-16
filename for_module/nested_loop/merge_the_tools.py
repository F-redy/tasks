# Merge the Tools!
# Consider the following:
# A string, S, of length where s = C0C1...Cn-1.
# An integer, k, where k is a factor of n.
#
# We can split S into n/k substrings where each subtring, t, consists of a contiguous block of k characters in s.
# Then, use each Ti to create string Ui such that:
#
# The characters in Ui are a subsequence of the characters in Ti.
# Any repeat occurrence of a character is removed from the string such that each character in Ui occurs exactly once.
# In other words, if the character at some index j in Ti occurs at a previous index < j in Ti,
# then do not include the character in string Ui.
#
# Given s and k, print n/k lines where each line i denotes string Ui.
#
# Example
# s =’AAABCADDE’
# k = 3
#
# There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'.
# The first substring is all 'A' characters, so u1 = 'A'.
# The second substring has all distinct characters, so U2 = 'BCA'.
# The third substring has 2 different characters, so U3 = 'DE'.
#
# Note that a subsequence maintains the original order of characters encountered.
# The order of characters in each subsequence shown is important.
#
# Function Description
#
# Complete the merge_the_tools function in the editor below.
#
# merge_the_tools has the following parameters:
#
# - string s: the string to analyze
# - int k: the size of substrings to analyze
#
# Prints
#
# Print each subsequence on a new line. There will be n/k of them. No return value is expected.
#
# Input Format
#
# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.


def merge_the_tools(string: str, k: int) -> None:
    """
       Разбивает строку на подстроки длиной k и выводит уникальные символы в каждой подстроке.

       :param string: Входная строка, которую необходимо разбить и обработать.
       :param k: Длина подстроки для разбиения строки.

       Пример использования:
       >>> merge_the_tools("AABCAAADA", 3)
       AB
       CA
       AD
    """
    for i in range(0, len(string), k):
        substring = string[i:i + k]  # Получаем подстроку длиной k
        unique_chars = []

        # Убираем повторяющиеся символы и сохраняем порядок
        for char in substring:
            if char not in unique_chars:
                unique_chars.append(char)

        # Выводим уникальную подстроку
        print("".join(unique_chars))


if __name__ == "__main__":
    s = input("Введите строку: ")
    k = int(input("Введите длину подстроки: "))
    merge_the_tools(s, k)
