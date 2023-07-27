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
