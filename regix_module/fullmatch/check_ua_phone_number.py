import re
from random import randint

from typing_extensions import Generator

MIN_PHONE_LENGTH = 7
MAX_PHONE_LENGTH = 13
PERMITTED_OPERATORS = {
    "Киевстар": ("067", "096", "097", "098"),
    "Vodafone (МТС)": ("050", "066", "095", "099"),
    "Lifecell (Лайф)": ("063", "073", "093"),
    "Мошеннические": ("070", "080", "090", "056", "057"),
    "Тримоб, PeopleNet, Интертелеком": ("091", "092", "094")
}

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


def get_name_operator(code_operator: str) -> str:
    for name_operator, codes in PERMITTED_OPERATORS.items():
        if code_operator in codes and name_operator == 'Мошеннические':
            return "\033[31mМошенник\033[0m"

        if code_operator in codes:
            return name_operator

    return '\033[33mНе известный\033[0m'


def cleaning_number(number: str) -> str:
    return re.sub(r"[+ \-]", "", number)


def get_result_text(match: re.Match) -> str | None:
    if match:
        code, code_operator, number = match.groupdict().values()
        number = f"{number[0:3]}-{number[3:5]}-{number[5:]}"

        return f"{get_name_operator(code_operator)} | +38-{code_operator}-{number}"


def validate_ukrainian_phone_number(phone_number: str) -> str:
    pattern = re.compile(r"""(?x)
            ^(?P<code>38|8)
            (?P<operator>
                (?:067|096|097|098)|             # Киевстар
                (?:050|066|095|099)|             # Vodafone (МТС)
                (?:063|073|093)|                 # Lifecell (Лайф)
                (?:070|080|090|056|057)|         # Мошеннические
                (?:091|092|094)                  # Тримоб, PeopleNet, Интертелеком
            )
            (?P<number>[0-9]{7})$
        """)

    if not phone_number:
        return 'Номер отсутствует!'

    if not (MIN_PHONE_LENGTH <= len(phone_number) <= MAX_PHONE_LENGTH):
        return "Не корректная длинна номера"

    phone_number = cleaning_number(phone_number)
    match = pattern.fullmatch(phone_number)

    return get_result_text(match) or "Номер не относиться ни к одному из украинских операторов!"


if __name__ == '__main__':

    random_operators = ["".join(str(randint(0, 9)) for _ in range(3)) for _ in range(25)]
    random_code_country = ["".join(str(randint(0, 9)) for _ in range(randint(1, 2))) for _ in range(5)]

    test_numbers = generation_phones_numbers(codes_operators, codes_county, 100)
    test_random_numbers = generation_phones_numbers(random_operators, random_code_country, 200)

    for n in test_numbers:
        print(validate_ukrainian_phone_number(n))
