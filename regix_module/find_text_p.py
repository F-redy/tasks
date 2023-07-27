# Параграфы
# Условие:
# Напишите регулярное выражение, которое найдёт всё содержимое тегов p.
#
# Что нужно найти:
# Нужно найти теги, подходящие по следующим условиям:
#
# В начале тега стоит:
#
# <p
# Тут может быть последовательность символов минимально возможной длины
# >
# Внутри тега последовательность из любых символов минимально возможной длины
#
# В конце тега стоит </p>
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка с html-разметкой.
#
# Выходные данные:
# Выведите в консоль содержимое тегов p. Каждое совпадение на новой строке.


import re

test_case = [
    '<p Неправильный параграф</p></p>1</p><p>2</p><p3/p>',
    '<noscript class="noscript"><p class="l-header">Сайт не работает<br>без JavaScript 😕</p></noscript>',
    '<main><section class="faq__section content"><h2 class="h-header">Частозадаваемые вопросы</h2><div class="faq__megawrapper"><div class="faq__wrapper"><details><summary class="l-header">Какой-то вопрос?</summary><p class="details__paragraph p-paragraph">Какой-то ответ</p></details><details><summary class="l-header">Какой-то вопрос?</summary><p class="details__paragraph p-paragraph">Какой-то ответ</p></details><details><summary class="l-header">Какой-то вопрос?</summary><p class="details__paragraph p-paragraph">Какой-то'
]

pattern = r'<p[^><]*?>(.+?)</p>'

matches = [re.findall(pattern, text) for text in test_case]

for idx, match_list in enumerate(matches, start=1):
    print(f"Совпадения для test_case {idx}:")
    for match in match_list:
        print(f"Содержимое: {match}")
    print()
