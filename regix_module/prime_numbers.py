# Найдите все последовательности, состоящие из символов x, длина которых простое число.


import re

test_case = [(
    'x xx xxx xxxx xxxxx xxxxxx xxxxxxx xxxxxxxx xxxxxxxxx xxxxxxxxxx xxxxxxxxxxx xxxxxxxxxxxx xxxxxxxxxxxxx '
    'xxxxxxxxxxxxxx',
    'xx xxx xxxxx xxxxxxx xxxxxxxxxxx xxxxxxxxxxxxx'),
    ('xxxxxxxxxxxxxxx xxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxx '
     'xxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxx',
     'xxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxx')]


def is_prime(match: re.Match):
    x = len(match[0])
    if x < 2:
        return
    for num in range(2, (x // 2) + 1):
        if x % num == 0:
            return
    return match[0]


for i, (test, answer) in enumerate(test_case, 1):
    result = re.sub(r"\s{2,}", ' ', re.sub(r'\bx+\b', is_prime, test)).strip()
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
