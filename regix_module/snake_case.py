# Условие:
# Напишите регулярное выражение, которое найдёт все переменные, записанные в стиле snake_case.

# Что нужно найти:
# Как вы уже поняли - snake_case это тоже стиль наименования переменных.
# В Python переменные принято называть, используя этот стиль. Вот что он из себя представляет:

# Всегда используется нижний регистр;
# Слова разделяются нижним подчёркиванием;
# Используются буквы латинского алфавита;
# Цифры в переменных из тестовых данных находятся только в конце.

# Примеры использования:
# variable
# quite_long_variable
# two_words


import re

test_case = [
    ('get_id sendMessage echo_all canvas wrapper RegularExpression upperCAse nice_Flick_SHOT that_was_bad',
     'get_id echo_all canvas wrapper that_was_bad'),
    ('project_one project_1 test_2 test_3 test_4 variable_5 var_6 var_7 var_8 var_9 var_42342354325',
     'project_one project_1 test_2 test_3 test_4 variable_5 var_6 var_7 var_8 var_9 var_42342354325'),
    ('just_a_variable Wrong_Variable SendNudes doubleShibaInu', 'just_a_variable'),
    ('dfgh_', '')
]

pattern = r"\b[a-z]+(?:_\d+)?(?:_[a-z]+\d*)*\b"

for i, (example, answer) in enumerate(test_case, 1):
    result = ' '.join(re.findall(pattern, example))
    assert result == answer, f"TEST №{i} - ERROR!\n'{result}' != '{answer}'"
    print(f'TEST №{i} - OK')
