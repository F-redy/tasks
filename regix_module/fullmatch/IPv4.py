# IPv4
# Условие
# Проверьте валидность IPv4 адресов (от 0.0.0.0 до 255.255.255.255) с помощью регулярных выражений.
#
# Если валидный - выведите True, иначе - False.


import re

test_case = [('0.0.0.0', True), ('31.19.95.7', True), ('255.19.90.7', True), ('00.34.90.7', False),
             ('124.257.123.3', False), ('1.2.3.b', False), ('1..23.4', False), ('1234', False),
             ('....', False), ('255.941.31.49', False), ('801.41.63.1', False), ('1000.100.10.1', False),
             ('12.-3.4.1', False)]

part = r"(0|[1-9][0-9]?|[1-2][0-5]{2})"
pattern = re.compile(fr"{part}\.{part}\.{part}\.{part}")

for i, (test, answer) in enumerate(test_case, 1):
    result = bool(pattern.fullmatch(test))
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')


