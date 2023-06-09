import re
from http import HTTPStatus
from random import randint

import requests
from bs4 import BeautifulSoup as BS

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


def scraping_quizlet(url: str) -> None:
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


def books_scraper(url: str) -> list[dict]:
    """
    Fuction scraper for https://books.toscrape.com/

    :param url: link to site
    :return: list with book
    """

    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])

        if resp.status_code == HTTPStatus.OK:
            html = resp.content
            soup = BS(html, 'html.parser')
            sections = soup.select('section')
            section = sections[0]
            books_block = section.select_one('ol[class=row]')
            books = books_block.select('li')
            books_data = []

            for book in books:
                image = url + book.find('div', attrs={'class': 'image_container'}).find('img')['src']
                title = book.find('h3').find('a')['title']  # book.h3.a['title']
                price = book.find('p', class_='price_color').text

                books_data.append(
                    {
                        'title': title,
                        'image': image,
                        'price': price
                    }
                )

            return books_data


link_books = r'https://books.toscrape.com/'
books_scraper(link_books)

link_quizlet = 'YOUR URL'
scraping_quizlet(link_quizlet)
