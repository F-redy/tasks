# https://pypi.org/project/regex/
import regex

pattern = '''
(?x)^(?=[^\W_]{6,})  # длина пароля более 6 символов
(?=.*?\d)  # определяю наличие цифры
(?=.*?[[:upper:]])  # определяю наличие заглавной буквы
(?=.*?[[:lower:]])  # определяю наличие маленькой буквы
[^\W_]+$  # записываю пароль правильными символами
'''.strip()
pattern = regex.compile(pattern)

test_case = [('f4aD2g', True), ('ddddddd4ddddAs', True), ('pi44', False), ('22222', False),
             ('dddddddd4ddddas', False), ('dgah2_dd2g', False), ('بdFa3ав', True), ('الحH3ёدث', True),
             ('أل42Čö263ف', True), ('الأح2Äа5مر', True), ('ن', False), ('_______', False),
             ('dasda_adsadad', False), ('sööÖ42k', True), ('3123123_123_13131', False), ('____f______', False),
             ('____41__', False)]

for i, (test, answer) in enumerate(test_case, 1):
    result = bool(pattern.fullmatch(test))
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')


