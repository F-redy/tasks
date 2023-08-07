# `Gaius Julius Caesar
# Условие:
# Найдите все арабские числа и замените их на римские с помощью функции SPQR.
#
# В римских числах не существует числа 0, его нужно игнорировать.

import re

test_case = [('2022 11.09.2001', 'MMXXII XI.0IX.MMI'),
             ('404 1259 2848 8 86 25 917 0 007', 'CDIV MCCLIX MMDCCCXLVIII VIII LXXXVI XXV CMXVII 0 00VII')]

pattern = re.compile(r"[1-9][0-9]*")


def SPQR(match):
    num = int(match[0])
    res = ''
    lst = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
           (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    for arabic, roman in lst:
        res += num // arabic * roman
        num %= arabic
    return res


for i, (test, answer) in enumerate(test_case, 1):
    result = pattern.sub(SPQR, test)
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
