import re

from function_generators.phone_number_generator import generator_phones_numbers, codes_operators, codes_county

MIN_PHONE_LENGTH = 7
MAX_PHONE_LENGTH = 13
PERMITTED_OPERATORS = {
    "Киевстар": ("067", "096", "097", "098"),
    "Vodafone (МТС)": ("050", "066", "095", "099"),
    "Lifecell (Лайф)": ("063", "073", "093"),
    "Мошеннические": ("070", "080", "090", "056", "057"),
    "Тримоб, PeopleNet, Интертелеком": ("091", "092", "094")
}


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
    ua_phone_numbers = generator_phones_numbers(codes_operators, codes_county, count_phones=100)

    for n in ua_phone_numbers:
        print(validate_ukrainian_phone_number(n))
