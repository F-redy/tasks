# Разделяем параметры
# Условие:
# Разделите строку по символам ? и &.
#
# Что нужно сделать:
# Нужно разделить строку по символвам ? и &, оставив эти символы в полученном списке.
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Список, с частями исходной строки.

import re

test_case = [
    ('https://stackoverflow.com/questions/tagged/regex?tab=votes&page=11&pagesize=15',
     ['https://stackoverflow.com/questions/tagged/regex', '?', 'tab=votes', '&', 'page=11', '&', 'pagesize=15']),
    ('https://www.youtube.com/results?search_query=random+stream&sp=EggIARABGAFAAQ%253D%253D',
     ['https://www.youtube.com/results', '?', 'search_query=random+stream', '&', 'sp=EggIARABGAFAAQ%253D%253D'])
]

pattern = r"([&?])"

for i, (test, answer) in enumerate(test_case, 1):
    result = re.split(pattern, test)
    assert result == answer, f'TEST №{i}\nError in {test}\n{result} != {answer}'
    print(f'TEST №{i} - OK\n{result}')
