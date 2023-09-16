# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.
#
# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Your task is to determine the winner of the game and their score.
#
# Function Description
#
# Complete the minion_game in the editor below.
#
# minion_game has the following parameters:
#
# string string: the string to analyze
# Prints
# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

# Input Format
#
# A single line of input containing the string S.
# Note: The string  will contain only uppercase letters: [A-Z].

# Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.


def minion_game(string: str, stuart: int = 0, kevin: int = 0) -> None:
    """
    Игра "Миньон". Оценивает количество очков для Стюарта и Кевина в игре с заданной строкой.

    :args:
    string (str): Входная строка.

    :return:
    None. Функция выводит результат игры.

    :example:
    >>> minion_game("BANANA")
    Kevin 9
    """

    vowels = "AEIOU"
    stuart_score = stuart
    kevin_score = kevin

    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if kevin_score == stuart_score:
        print('Draw')
    else:
        print((f"Stuart {stuart_score}", f"Kevin {kevin_score}")[kevin_score > stuart_score])


input_string = input('Enter a string: ')
minion_game(input_string)
