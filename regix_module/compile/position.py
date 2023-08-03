# position
# Условие:
# Найдите первое слово, которое содержится в определённом диапазоне.
#
# Что нужно сделать:
# Найти первое слово, состоящее из a-z в определённом диапазоне. Слово не может являться подпоследовательностью.
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 3 строки:
#
# Текст
# Начальная позиция для поиска
# Конечная позиция для поиска
# Выходные данные:
# Если в полученном диапазоне есть слово, то нужно его вывести.

import re

test_case = [('soda senior tuition library task tone few torch vacuum', 2, 29, 'senior'),
             ('access patient artist annual space mother color plunge unusual', 200, 10, ''),
             ('truly reform mosquito host slim dinner palm crisp glory tattoo cable popular motion toilet laugh egg '
              'coast exhaust planet never found', 39, 44, 'palm')
             ]

pattern = re.compile(r"(?i)\b[a-z]+\b")
# text, start, end = input(), int(input()), int(input())
for i, (text, start, end, answer) in enumerate(test_case, 1):
    match = pattern.search(text, start, end)
    result = match[0] if match else ''
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {text}'
    print(f'TEST №{i} - OK\n{result}\n')
