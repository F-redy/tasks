# Напишите функцию find_repeated, принимающую строку, состоящую из слов, разделённых пробелом.
# Функция должна вернуть первое слово, у которого существуют повторения в строке.
# Если такого слова нет - функция возвращает None.

import re

test_case = [('ap fl hk ap hk fl', 'ap'), ('yes no eyes no maybe', 'no'), ('abc def apc def', 'def'),
             ('three different words', 'None')]


def find_repeated(text):
    match = re.search(r"\b(\w+)\b(?=.*\b\1\b)", text)
    if match:
        return match[0]


for i, (test, answer) in enumerate(test_case, 1):
    print(find_repeated(test))


# похожая задача
# https://stepik.org/lesson/611485/step/12?unit=606807
def first_repeated_word(text):
    """Находит первый дубль в строке"""
    pattern = re.compile(r"\b(\w+)\b(.*\b)?\1\b")
    result = pattern.search(text)
    return first_repeated_word(result[2]) or result[1] if result else result
