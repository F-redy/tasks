# название.расширение
# Условие:
# Найдите в тексте все названия файлов и их расширения.
#
# Что нужно найти:
# Нужно найти последовательности, подходящие по следующим условиям:
#
# Название файла состоит из: букв латинского алфавита верхнего и нижнего регистров, _, цифр, -
# Между названием и расширением файла стоит .
# Расширение файла состоит из букв латинского алфавита верхнего и нижнего регистров, цифр
# Минимальная длина названия и расширения - один символ
# Найденная последовательность может являться подпоследовательностью,
# только если стоит в абсолютном или относительном пути: C:\Users\test.txt, ../Users/test.txt,
# т.е. перед ней стоят символы / или \

import re

test_case = [
    ('Untitled-1.psd Untitled-1.jpg video.mp4', 'Untitled-1.psd Untitled-1.jpg video.mp4'),
    (r'C:\Users\matv3\Desktop\script.js index.html @/assets/images/logo.svg', 'script.js index.html logo.svg'),
    ('bot.py sad.gif', 'bot.py sad.gif'),
    ('.mp4 some-text .py', ''),
    ('test... te..st', ''),
    ('файл.file файл.файл file.файл фfile.фfile fфile.fфile', ''),
    ('c#logs.txt query.$exe', ''),
    (' :a.json  ?s.csv', ''),
    ('video-_a.mp4 logs_1.txt', 'video-_a.mp4 logs_1.txt')
]
pattern = r"(?<![^\s\\/])[a-zA-Z\d\-_]+[a-zA-Z\d]+\.[a-zA-Z\d]+"

for i, (example, answer) in enumerate(test_case, 1):
    result = ' '.join(re.findall(pattern, example))
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}'
    print(f'TEST №{i} - OK!')
