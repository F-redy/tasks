import requests
from bs4 import BeautifulSoup as BS
from random import randint
import re

# Обманка для сайтов
headers = [{"User-Agent": "Mozzila/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Accept": "text/html,aplication/xhtml+xml,aplication/xml;q=0.9,*/*;q=0.8"
            },
           {
               "User-Agent": "Mozzila/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
               "Accept": "text/html,aplication/xhtml+xml,aplication/xml;q=0.9,*/*;q=0.8"
           },
           {"User-Agent": "Mozzila/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0",
            "Accept": "text/html,aplication/xhtml+xml,aplication/xml;q=0.9,*/*;q=0.8"
            },
           ]


def check_lang(word: str) -> str:
    en = 'abcdefghijklmnopqrstuvwxyz'
    return ('ru', 'en')[word[0] in en]


def scraping_func(url: str) -> None:
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if url:
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('table', attrs={'class': 'ember-view'})
            if main_div:
                # обработка полученных данных
                for indx, line in enumerate(main_div):
                    lst = str(line.text).split('\n')
                    if len(lst) > 3:
                        string = ' '.join(lst).replace(' ', '', 1)
                        string = re.sub(r'\[.*?\]', '', string).replace('  ', ' ').replace(' ,', '').replace('; ', ' ')
                        en, ru = [], []
                        for word in string.split():
                            if '(' in word or ')' in word:
                                continue
                            else:
                                lang = check_lang(word)
                                if lang == 'en' and len(en) < 4:
                                    en.append(word)
                                if lang == 'ru':
                                    ru.append(word)
                        print(f'{" ".join(en)} - {" ".join(ru)}')
                else:
                    print('Error with main_div params')
        else:
            print('You have problem with url!')
    else:
        print('Do not have url')


url = 'YOUR URL'
scraping_func(url)
