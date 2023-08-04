# ПрИвЕт
# Условие:
# Найдите все слова привет. Регистр учитывать не нужно.
#
# Что нужно сделать:
# Нужно найти слова привет в разном регистре.
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Все слова привет в тексте.


import re

test_case = [(
    'ПРИВЕТспампрИвЕТspamпРИвет123ПРИвЕт456ПРиВет789ПРиВет10пРиВЕТПокаПРиВеТHiпРИВетHelloПРиветTestприветStringПривЕт',
    ['ПРИВЕТ', 'прИвЕТ', 'пРИвет', 'ПРИвЕт', 'ПРиВет', 'ПРиВет', 'пРиВЕТ', 'ПРиВеТ', 'пРИВет', 'ПРивет', 'привет',
     'ПривЕт']),
    ('привет ПРИВЕТ пРиВеТ', ['привет', 'ПРИВЕТ', 'пРиВеТ'])]

pattern = re.compile(r"привет", flags=re.IGNORECASE)
# print(re.findall(r"(?i)привет", input()))  # v1
# print(re.findall(r"привет", input(), flags=re.I))  # v2
# print(re.findall(r"привет", input(), flags=re.IGNORECASE))  # v3
# print(re.findall(r"привет", input(), flags=2))  # v4
# print(re.compile(r"привет", flags=2).findall(input()))  # v5

for i, (test, answer) in enumerate(test_case):
    result = pattern.findall(test)
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
