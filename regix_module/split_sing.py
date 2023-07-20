# На слова
# Условие:
# Разделите текст на слова.
#
# Что нужно сделать:
# Нужно разделить текст на слова по следующим символам: .?!, .
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Список после разделения текста на слова.

import re

test_case = [
    ("Привет, как твои дела? Привет, нормально, учу регулярные выражения.",
     ['Привет', '', 'как', 'твои', 'дела', '', 'Привет', '', 'нормально', '', 'учу', 'регулярные', 'выражения', '']),
    ("The first one is heavy!This actually goes really well with Chris's workout he's doing.",
     ['The', 'first', 'one', 'is', 'heavy', 'This', 'actually', 'goes', 'really', 'well', 'with', "Chris's", 'workout',
      "he's", 'doing', ''])
]

for i, (test, answer) in enumerate(test_case, 1):
    result = re.split(r"[.?!, ]", test)
    assert result == answer, f'TEST №{i}\nError in {test}\n{result} != {answer}'
    print(f'TEST №{i} - OK')
