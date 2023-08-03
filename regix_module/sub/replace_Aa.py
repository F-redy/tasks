# Условие:
# Замените все слова, которые начинаются на букву А в любом регистре, на удалено(n), где n - длина удалённого слова.
#
# Что нужно сделать:
# Нужно найти все слова, которые начинаются на букву А или а и заменить их на удалено(n), где n - длина удалённого слова
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Строка с удалёнными словами.

import re

test_case = [(
    'Акционер, акцентируя внимание на актуальность аналога данного продукта, прикупил несколько акций '
    'компании-производителя этого товара.',
    'удалено(8), удалено(10) внимание на удалено(12) удалено(7) данного продукта, прикупил несколько удалено(5) '
    'компании-производителя этого товара.'),
    ('А роза упала на лапу Азора.', 'удалено(1) роза упала на лапу удалено(5).'),
    ('Абажур Аббревиатура Абзац абитуриент абонемент абонент',
        'удалено(6) удалено(12) удалено(5) удалено(10) удалено(9) удалено(7)')]

pattern = r"(?i)\b(а[а-я]*)\b"

for i, (test, answer) in enumerate(test_case, 1):
    result = re.sub(pattern, lambda x: f"удалено({str(len(x[0]))})", test)
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
