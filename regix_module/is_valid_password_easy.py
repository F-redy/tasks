# Проверка пароля
# Условие:
# Проверьте пароль на валидность.
#
# Что нужно сделать:
# Проверить пароль на валидность. Валидным будем считать пароль, который:
#
# Состоит из a-z, A-Z, 0-9, @#$%^&*()_-+!?
# Его длина минимум 8 символов
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Если это валидный пароль - выводите True, иначе - False.

import re

test_case = [
    ('d2D8dh8DA#!', True),
    ('g0JDQ0#(dka02b vp', False),
    ('Это не пароль', False),
    ('111111111$%^1111111111', True),
    ('@#$%^64&*()_-+!?', True),
]


def is_valid_password(password: str) -> bool:
    symbols = ''.join(map(re.escape, '@#$%^&*()_-+!?'))
    pattern = re.compile(fr"[A-Za-z\d{symbols}]{{8,}}")
    return bool(pattern.fullmatch(password))


for i, (test, result) in enumerate(test_case, 1):
    res = is_valid_password(test)
    assert res == result, f'TEST №{i}: ERROR!\n{res} != {result}'
    print(f'TEST №{i}: OK')
