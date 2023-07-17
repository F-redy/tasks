# Валидация многочленов
# Условие:
# Проверьте, является ли строка многочленом или нет.
#
# Что нужно сделать:
# Найдите все последовательности, которые могут быть многочленами. Многочлен состоит из слагаемых.
# Каждое слагаемое это следующее произведение:
#
# Первым множителем может быть целое число (любая последовательность цифр)
# Числа могут быть отрицательными
# Вторым множителем может быть x
# x может быть возведён в любую степень (любая последовательность цифр)
# Между множителями ничего не стоит
# в произведении может не быть одного из множителей
# x не всегда возведен в какую-либо степень
# Между слагаемыми стоит - или +.
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Если это номер многочлен - выводите True, иначе - False.

import re


def validate_equation(equation: str) -> bool:
    pattern = r"(?:\-?(?![\-^])\d*(?!\^)x?(?![x\d])\^?[+-]?)*"
    return bool(re.fullmatch(pattern, equation))


test_case = [('x^3-11x^2+38x-40', True), ('6x^4+19x^3-7x^2-26x+12', True), ('15x^5-8x^4+46x^3+21x^2-21x+3', True),
             ('4x^6+9x^5-x^4+22x^3-x^2+9x-18', True), ('6x^4+x^3+2x^2-4x+1', True), ('x', True), ('5x+2', True),
             ('-x', True), ('x^2-x', True), ('-9', True), ('-x9', False), ('x792x', False), ('xx', False),
             ('--34', False), ('x^3+14^x', False), ('-^10', False)]

for i, (test, result) in enumerate(test_case, 1):
    is_valid = validate_equation(test)
    assert is_valid == result, f'TEST №{i} - Error in: "{test}"\n{is_valid} != {result}'
    print(f'TEST №{i:<5} -> OK')
