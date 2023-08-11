import re
from werkzeug.security import generate_password_hash, check_password_hash
from random import choices
from string import digits, ascii_letters, punctuation
from datetime import datetime

symbols = re.escape(punctuation)


class ValidationHelper:

    @staticmethod
    def clean_string(string: str) -> str:
        return string.lower().strip()

    @classmethod
    def generation_password(cls, length_password: int = 12):
        while True:
            password = "".join(choices(ascii_letters + digits + symbols, k=length_password))

            if cls.is_valid_created_password(password):
                return password

    @staticmethod
    def hash_password(password: str) -> str:
        return generate_password_hash(password)

    @staticmethod
    def email_verification(email: str):
        pattern = r"^([\w.\-]{3,})@([\w.\-]{2,})\.([a-z]{2,})$"
        result = re.search(pattern, email)

        if result and len(email) < 321:
            username, domain, extension = result.groups()
            if len(username) < 65 and len(f'{domain}.{extension}') < 256:
                return True

        return False

    @classmethod
    def is_valid_username(cls, entered_username: str) -> bool:
        """Функция проверяет username по следующим критериям:
        - Используются символы a-z, A-Z, 0-9, _, -.
        - Длина от 3 до 32 символов включительно
        - Может начинаться только с:  a-z, A-Z, 0-9.
        - Может заканчиваться только на a-z, A-Z, 0-9
        """
        pattern = re.compile(r"^[\da-zA-Z][_\-]*[\da-zA-Z]{2,31}")
        return bool(pattern.fullmatch(entered_username.strip()))

    @classmethod
    def is_valid_created_password(cls, entered_password: str):
        """
        Хотя бы одна маленькая буква, одна большая буква, одна цифра
        и один специальный символ, и общая длина не менее 8 символов.
        """

        pattern = re.compile(fr"""(?x)
            ^                   # Начало строки
            (?=.*[a-z])         # Хотя бы одна маленькая буква (позитивный просмотр вперед)
            (?=.*[A-Z])         # Хотя бы одна большая буква (позитивный просмотр вперед)
            (?=.*\d)            # Хотя бы одна цифра (позитивный просмотр вперед)
            (?=.*[{symbols}])  # Хотя бы один специальный символ (позитивный просмотр вперед)
            [a-zA-Z\d{symbols}]{8,}  # Символы из указанных классов и длина не менее 8
            $                   # Конец строки
        """)
        return bool(re.match(pattern, entered_password))

    @classmethod
    def is_valid_entered_password(cls, password: str) -> str | bool:
        """
        Проверяет пароль при регистрации пользователя.

        :param password: Строка с паролем. Валидный пароль:
                                                        1 строчная буква, 1 заглавная и 1 цифра. Длинна от 8 символов.
        :return: Если проверка не пройдена сообщение об ошибке. Иначе True.
        """
        # if len(password) < 8:
        #     return 'Short password! Min length 8 symbols.'
        # uppercase, lowercase, digitcase = [any(map(func, password)) for func in [str.isupper, str.islower, str.isdigit]]
        # if not uppercase:
        #     return 'Password must contain at least 1 capital letter!'
        # if not lowercase:
        #     return 'Password must contain at least 1 lowercase letter!'
        # if not digitcase:
        #     return 'Password must contain at least 1 digit!'
        #
        # return True
        return all([any(map(func, password)) for func in [str.isupper, str.islower, str.isdigit]]) and len(password) > 7

    @classmethod
    def check_password(cls, entered_password: str, verified_password: str) -> bool:
        """
        Проверка хеш паролей

        :param entered_password: Пароль без хеша, введенный пользователем.
        :param verified_password: Пароль из базы данных с хешем.
        :return: True если пароли совпадают, иначе False.
        """
        return check_password_hash(verified_password, entered_password)

    @staticmethod
    def get_slug(other_word: str) -> str:
        cyrillic_to_latin = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
            ' ': '_', '_': '_'
        }
        symbols_ = symbols.replace('_', '')

        other_word = other_word.strip().lower()
        clean_punctuation = re.sub(fr'[{symbols_}]+', '', other_word)

        return ''.join([cyrillic_to_latin.get(letter, letter) for letter in clean_punctuation])

    @staticmethod
    def get_time_now():
        return datetime.now().strftime('%d/%m/%Y, %H:%M:%S')


def test_func(func: callable, test_case: list[tuple]) -> None:
    print(f'TEST FOR {func.__name__}')
    for i, (test, answer) in enumerate(test_case, 1):
        result = func(test)
        assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
        print(f'TEST №{i} - OK')
    print()


if __name__ == '__main__':
    h = ValidationHelper()

    test_case_username = [
        ('fredy', True), ('XAM', True), ('1fredy', True), ('_fredy', False), ('!fredy', False), (' !fredy', False),
        ('@!fredy', False), ('fredy1', True), ('fredyA', True), ('FredyA', True), ('Fredy1', True),
        ('Fredy_', False), ('HR', False), ('12345678901234567890123456789012', True),
        ('12345678901234567890123456789012a', False),
    ]

    test_case_password = [('dgah2_dd2g', False), ('JVApa8In', True), ('k7dzbb2d', False), ('pi44', False),
                          ('ddddddd4ddddAs', True), ('iWlGgUnc', False), ('ن', False), ('3123123_123_13131', False),
                          ('____41__', False), ('BOJ8gZai', True), ('sHI4gqR3', True), ('22222', False),
                          ('الأح2Äа5مر', True), ('Wt8bAP5C', True), ('أل42Čö263ف', True), ('dasda_adsadad', False),
                          ('JmL5Lxbw', True), ('_______', False), ('f4aD2g', False), ('بadFa3ав', True),
                          ('qOUO1SRG', True), ('V86kqrWh', True), ('O12CDrxB', True), ('____f______', False),
                          ('dddddddd4ddddas', False), ('الحH3ёدث', True), ('söxöÖ42k', True),
                          ]

    test_func(h.is_valid_username, test_case_username)
    test_func(h.is_valid_entered_password, test_case_password)

    print(h.hash_password('5644977'))
