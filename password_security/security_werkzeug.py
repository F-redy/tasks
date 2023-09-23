from generation_random_password import generation_random_password
from werkzeug.security import check_password_hash, generate_password_hash


def generation_random_hash_password(length_password: int):
    random_password = generation_random_password(length_password=length_password)
    hashed_password = generate_password_hash(random_password)
    return hashed_password


def hash_password(password: str) -> str:
    return generate_password_hash(password)


if __name__ == '__main__':
    n = 33
    random_psw = generation_random_password(length_password=n)
    hashed_psw = generate_password_hash(random_psw)

    print(check_password_hash(hashed_psw, random_psw))
