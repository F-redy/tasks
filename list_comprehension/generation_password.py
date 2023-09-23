import random
import secrets
import string


# Генерация простого пароля
def generate_simple_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# Генерация сложного пароля
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# Генерация 10 простых паролей
simple_passwords = [generate_simple_password() for _ in range(10)]

# Генерация 10 сложных паролей
strong_passwords = [generate_strong_password() for _ in range(10)]


def print_password():
    # Вывод результатов
    print("Простые пароли:")
    for password in simple_passwords:
        print(password)

    print("\nСложные пароли:")
    for password in strong_passwords:
        print(password)


if __name__ == '__main__':
    print_password()
