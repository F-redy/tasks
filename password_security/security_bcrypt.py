import bcrypt
from generation_random_password import generation_random_password


def hash_password(password: str) -> bytes:
    # Генерация соли
    salt = bcrypt.gensalt()

    # Хеширование пароля
    password = password.encode('utf-8')  # Пароль в виде байтовой строки

    # Создание хеша с паролем и солью
    hashed_password = bcrypt.hashpw(password, salt)

    return hashed_password


def check_password(entered_password: str, verified_password: bytes) -> bool:
    entered_password: bytes = entered_password.encode('utf-8')  # Введенный пользователем пароль

    return bcrypt.checkpw(entered_password, verified_password)


if __name__ == '__main__':
    length_random_password: int = 16
    random_password: str = generation_random_password(length_random_password)
    result_hashed_password: bytes = hash_password(random_password)
    print(f"""
    PASSWORD: {random_password}
    {('!=', '=')[check_password(random_password, result_hashed_password)]}
    HASH_PASSWORD: {result_hashed_password}""")
