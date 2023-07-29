# YT ID
# Условие:
# Получите все идентификаторы видеороликов на YouTube, используя регулярные выражения.
#
# Что нужно найти:
# Нужно найти последовательности, подходящие по следующим условиям:
#
# Cостоит из символов латинского алфавита обоих регистров, цифр, а также _
# Перед последовательностью стоит v=


import re

test_case = [
    ('https://youtu.be/watch?v=dQw4w9WgXcQ&list=PLi9drqWffJ9FWBo7ZVOiaVy0UQQEm4IbP', 'dQw4w9WgXcQ'),
    ('https://www.youtube.com/watch?v=jNQXAC9IVRw', 'jNQXAC9IVRw'),
    ('https://m.youtube.com/watch?v=pXRviuL6vMY&list=PLrhpb4TQr-uKzxOB1C_9x-Ysrj2WRMZN_&index=16&t=535s',
     'pXRviuL6vMY'),
    ('https://www.youtube.com/watch?app=desktop&v=WUEVJ0N6I1A&t=1s', 'WUEVJ0N6I1A'),
]

pattern = r"(?<=v=)[A-z\d_]+"

for i, (example, answer) in enumerate(test_case, 1):
    result = ' '.join(re.findall(pattern, example))
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}'
    print(f'TEST №{i} - OK!')