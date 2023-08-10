# Чередование
# Условие:
# На вход программе подается строка текста с разными словами на английском языке. Найдите такие слова,
# в которых постоянно чередуются гласные и согласные. Так как y может быть как и гласной, так и согласной,
# то добавим её сразу во все строчки.

import re

test_case = [(
    'cite election data chemistry point future tale employment wave rice '
    'expert fun food hi role discount initiative',
    'cite data future tale wave rice fun hi role'),
    ('age art item eye it is', 'age item eye it is'),

]

vowels = '[aeiouy]'
consonants = '[bcdfghjklmnpqrstvwxyz]'

pattern = re.compile(fr"(?ix)"
                     fr"\b(?:{consonants}{vowels})+{consonants}?\b"
                     fr"|"
                     fr"\b(?:{vowels}{consonants})+{vowels}?\b")

for i, (test, answer) in enumerate(test_case, 1):
    result = ' '.join(pattern.findall(test))
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
