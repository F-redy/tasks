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


def books_scraper() -> list[dict]:
    """
    Function scraper for https://books.toscrape.com/

    :return: list with books
    """

    sections = soup.select('section')
    section = sections[0]
    books_block = section.select_one('ol[class=row]')
    books = books_block.select('li')
    books_data = []

    for book in books:
        image = path + book.find('div', attrs={'class': 'image_container'}).find('img')['src']
        title = book.find('h3').find('a')['title']  # book.h3.a['title']
        price = book.find('p', class_='price_color').text

        books_data.append(
            {
                'title': title,
                'image': image,
                'price': price,
            }
        )

    return books_data


def get_next_page() -> str | None:
    try:
        return f"{path}catalogue/{soup.find('li', attrs={'class': 'next'}).find('a')['href']}"
    except AttributeError:
        return None


def save_to_file(lst_books: list[dict]):
    with open(r'data_books', 'a', encoding='utf-8') as file:
        for page, book in enumerate(lst_books, 1):
            print(f'Book №{counter_books + page}\n'
                  f'title: {book["title"]}\n'
                  f'image: {book["image"]}\n'
                  f'price: {book["price"]}\n',
                  file=file)


path: str = r'https://books.toscrape.com/'
url: str = r"https://books.toscrape.com/catalogue/page-1.html"

site_page: int = 1
counter_books: int = 0

while url:
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == HTTPStatus.OK:
        get_html = resp.content
        soup = BS(get_html, 'html.parser')

        list_books = books_scraper()
        save_to_file(list_books)

        counter = len(list_books)

        print(f'Received {counter} books from page {site_page}.')

        site_page += 1
        counter_books += counter

        url = get_next_page()

print(f'Data was parsed...\ntotal of {site_page} pages were processed;\ntotal of {counter_books} books were received.')
