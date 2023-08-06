# CamelCase & snake_case
# Условие:
# Преобразуйте CamelCase «Верблюжий регистр» в snake_case «Змеиный регистр».


import re

test_case = [('MySendMessage', 'my_send_message'), ('RegularExpression', 'regular_expression'),
             ('VUpperCase', 'v_upper_case'), ('ThisFunctionIsEmpty', 'this_function_is_empty'),
             ('Case', 'case'), ('SomeNumbers123', 'some_numbers_123'),
             ('VeryVeryBigVariable123', 'very_very_big_variable_123'),
             ]


for i, (test, answer) in enumerate(test_case, 1):
    result = re.sub(r"([A-Z]|\d+)", r"_\1", test).strip('_').lower()
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
