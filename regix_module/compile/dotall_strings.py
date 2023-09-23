# Через строки
# Условие:
# Дан большой текст, который состоит из нескольких строк, он находится в переменной text.
#
# Найдите в нём текст от start до end.
#
# Что нужно сделать:
# Нужно найти весь текст от start до end, текст может быть растянут на несколько строк.
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Найденный текст.

import re
import sys

test_case = [
    ("""start
Каждое
Слово
На
Новой
Строке
end""", ['\nКаждое\nСлово\nНа\nНовой\nСтроке\n']),
    ("""spamstartЭТОТ
ТЕКСТ
НАХОДИТСЯ
НА
НЕСКОЛЬКИХ
СТРОКАХ
endspam""", ['ЭТОТ\nТЕКСТ\nНАХОДИТСЯ\nНА\nНЕСКОЛЬКИХ\nСТРОКАХ\n']),
    ("""['ЭТОТ\nТЕКСТ\nНАХОДИТСЯ\nНА\nНЕСКОЛЬКИХ\nСТРОКАХ\n']""", [])
]

# text = ''.join(sys.stdin.readlines())
pattern = re.compile(r"(?<=start).+(?=end)", flags=re.DOTALL)
# print(pattern.findall(text)
for i, (test, answer) in enumerate(test_case):
    result = pattern.findall(test)
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
