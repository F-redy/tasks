# Разделяем найденные ссылки
# Условие:
# Напишите программу, которая будет находить ссылки и разделять их на части: протокол, адрес, параметры, якорь.
# Протокол и адрес у ссылок есть всегда.
#
# Что нужно найти:
# Нужно найти ссылки, подходящие по следующим условиям:
#
# Протокол https или http
# После протокола идёт ://
# Домен состоит из символов a-z, .
# Путь состоит из символов a-z, 0-9, -, _, /
# Параметры начинаются с ? и состоят из a-z, =, &, 0-9
# Якорь начинается с # и состоит из a-z
# Протокол и адрес у ссылок есть всегда, остальных частей может не быть
# Ссылка не может быть подпоследовательностью
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка текста.
#
# Выходные данные:
# Выведите в консоль ссылку, протокол, домен, параметры, якорь найденных совпадений в следующем виде:
#
# Полная ссылка: https://example.com/test/42523/step/2?q=query&s=search#test
# Протокол: https | Домен: example.com | Параметры: ?q=query&s=search | Якорь: #test
# Если группа ничего не нашла, то вместо совпадения нужно вывести None.


import re

test_case = [
    'В этом https://stepik.org/lesson/704265/step/2?unit=704697#test тексте https://example.com/ очень много https://keep.google.com/#home разных http://oldastoundingrelaxedlaugh.neverssl.com/online ссылок. ',
    'Наступаешь на одни и те же грабли: https://vk.com/video-460389_160321403 https://pikabu.ru/story/vse_schitayut_sebya_unikalnyimi_poka_ne_prikhoditsya_pokupat_domen_dlya_svoego_startapa_9132005#comments https://www.google.com/search?q=query https://yandex.ru/search/?lr=16&text=query',
    'https://www.google+com/ https://www.google?com/ https://www.google#com/',
    'https://quizlet.com/810646817/edit#addRow',
    'https://chat.openai.com/?model=text-davinci-002-render-sha',
    'https://www.youtube.com/playlist?list=PLF4MWzDJPFSYeUtNQGDsS-XZDriJjFRL8'
]

pattern = re.compile("""(?x)(?i)
                (?P<protocol>http[s]?)://
                (?P<domen>(?:[a-z\d_]+\.)+[a-z]+)/
                (?:[a-z\d\-_/]*) # path
                (?P<param>\?[a-z=&\d]+)?
                (?P<anchor>\#[a-z]+)?
""")

for test in test_case:
    for current_match in re.finditer(pattern, test):
        print(f'Полная ссылка: {current_match[0]}')

        # если pattern path сделать не включающейся группой
        print('Протокол: {} | Домен: {} | Параметры: {} | Якорь: {}\n'.format(*current_match.groups()))

        # Если нужен еще и path и сделать path сделать именованной группой
        # if match['current_match']:
        #     print(f'Путь: {match["current_match"]}')
        # print(f'Протокол: {current_match["protocol"]} | '
        #       f'Домен: {current_match["domen"]} | '
        #       f'Параметры: {current_match["param"]} | '
        #       f'Якорь: {current_match["anchor"]}\n')
