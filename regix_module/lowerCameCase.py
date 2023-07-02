# Условие:
# Напишите регулярное выражение, которое найдёт все переменные, записанные в стиле lowerCamelCase.
#
# Что нужно найти:
# Нужно найти переменные, записанные в стиле lowerCamelCase, который включает в себя следующее:
#
# Первое слово начинается всегда с буквы нижнего регистра
# Последующие слова начинаются с букв в верхнем регистре
# Больше верхний регистр нигде не используется
# Используются буквы латинского алфавита
# Цифры в переменных из тестовых данных находятся только в конце
# Примеры использования:
#
# variable
# quiteLongVariable
# twoWords

from test_regex import test_regex

test_case = [
    ('get_id sendMessage echo_all canvas wrapper RegularExpression vUpperCase nice_Flick_SHOT that_was_bad getLink',
     'sendMessage canvas wrapper vUpperCase getLink'),
    ('variableWithNumbers3134 anotherOne1 another1', 'variableWithNumbers3134 anotherOne1 another1'),
    ('just_a_variable Wrong_Variable SendNudes doubleShibaInu', 'doubleShibaInu'),
    ('doubleS1', ''), ('heloEveryOne1 heloEveryO1 helo_Every_One_1 ', 'heloEveryOne1')
]

pattern = r"\b[a-z]+(?:[A-Z][a-z]+\d*)*\d*\b"

test_regex(test_case, pattern)
