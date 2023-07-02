from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits


def generation_random_password(length_password: int = 12) -> str:
    punctuation = '!#$%&<=>?@_'
    case = [ascii_lowercase, ascii_uppercase, punctuation, digits]

    password = ''.join(choice(case[randint(0, 3)]) for _ in range(length_password))

    return password


if __name__ == '__main__':
    n = 50
    random_password = generation_random_password(length_password=n)
    print(random_password)
