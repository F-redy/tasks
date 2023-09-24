from random import randint

from typing_extensions import Generator

code_regions = {'Винница': '043', 'Днепр': '056', 'Донецк': '062', 'Житомир': '041', 'Запорожье': '061',
                'Ивано-Франковск': '034', 'Киев': '044 и 045', 'Кропивницкий': '052', 'Луганск': '064', 'Луцк': '033',
                'Львов': '032', 'Николаев': '051', 'Одесса': '048', 'Полтава': '053', 'Ровно': '036', 'Сумы': '054',
                'Тернополь': '035', 'Ужгород': '031', 'Харьков': '057', 'Херсон': '055', 'Хмельницкий': '038',
                'Черкассы': '047', 'Чернигов': '046', 'Черновцы': '037'}

codes_operators = ['067', '096', '097', '098', '050', '066', '095', '099', '063', '073', '093', '070',
                   '080', '090', '056', '057', '091', '092', '094']

codes_county = ["+38", "38", "8"]


def generation_numbers(length_number: int):
    return "".join(str(randint(0, 9)) for _ in range(length_number))


def generation_phones_numbers(operators: list[str], codes: list[str], count_phones: int) -> Generator[str, None, None]:
    for _ in range(count_phones):
        random_code = codes[randint(0, len(codes) - 1)]
        operator = operators[randint(0, len(operators) - 1)]
        number = generation_numbers(length_number=7)

        yield random_code + operator + number


if __name__ == '__main__':
    random_operators = ["".join(str(randint(0, 9)) for _ in range(3)) for _ in range(25)]
    random_code_country = ["".join(str(randint(0, 9)) for _ in range(randint(1, 2))) for _ in range(5)]

    test_numbers = generation_phones_numbers(codes_operators, codes_county, 100)
    test_random_numbers = generation_phones_numbers(random_operators, random_code_country, 200)

    for phone_number in test_numbers:
        print(phone_number)
