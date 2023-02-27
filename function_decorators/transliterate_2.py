# Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
# используя следующий словарь для замены русских букв на соответствующее латинское написание:
#
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку.
# Замены делать без учета регистра (исходную строку перевести в нижний регистр - малые буквы).
#
# Определите декоратор с параметром chars и начальным значением " !?",
# который данные символы преобразует в символ "-" и, кроме того,
# все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису.
# Полученный результат должен возвращаться в виде строки.
#
# Примените декоратор с аргументом chars="?!:;,. " к функции и
# вызовите декорированную функцию для введенной строки s:
#
# s = input()
#
# Результат отобразите на экране.
#
# Sample Input:
# Декораторы - это круто!
# Sample Output:
# dekoratory-eto-kruto-


import re
from functools import wraps

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def transliterate(string: str, cipher: dict[str:str]) -> str:
    """
    Function transliterates a string

    :param string: string to process
    :param cipher: dictionary with key:  replace and with value:  wherewith replace
    :return: converted string with chars replaced
    """
    return string.translate(str.maketrans(cipher))


def punctuator(chars: str = '!?'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return re.sub('-{2,}', '-', transliterate(func(*args, **kwargs), dict.fromkeys(chars, '-')))

        return wrapper

    return decorator


@punctuator(chars='?!:;,. ')
def init_transliterate(string: str) -> str:
    """
    Function converts a string to lowercase and call func transliterate()

    :param string: string to process
    :return: converted string
    """
    return transliterate(string.lower(), t)


s = input()
print(init_transliterate(s))
