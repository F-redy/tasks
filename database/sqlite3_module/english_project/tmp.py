import bcrypt
from Server import Server
from test_bd import get_all_tables


# menu = {
#     'create_db': create_db,
#     'registration': registration,
#     'authorization': authorization,
#     'add_dictionary': add_dictionary, 'get_dictionary': get_dictionary,
#     'add_pair': add_pair, 'add_words': add_words,
#     'get_words_from_file': get_words_from_file,
# }
#


def registration():
    username = input('Enter username: ')
    password = input('Enter password: ')
    email = input('Enter email: ')
    Server(username, password, email, registration=True)


def authorization():
    username = input('Enter username: ')
    password = input('Enter password: ')
    return Server(username, password)


def add_dictionary(user_id: int):
    title_dict: str = input('Enter dictionary title:\n')
    authorized_user.add_dictionary(title_dict, user_id)


def add_words(words: list[tuple[str, str]], title_dict: str, username: str):
    authorized_user.add_words(words, title_dict, username)


# registration()

authorized_user = authorization()
user_id = authorized_user.data_user['user']['id']
username = authorized_user.data_user['user']['username']

words = authorized_user.get_words(username, 'days of week')

for original, translate in words:
    print(f'{original} - {translate}')


def move_words_to_new_db():
    for d in get_all_tables():
        title_dict = ''.join(d.keys())
        words = d[title_dict]
        authorized_user.add_dictionary(title_dict, user_id)
        authorized_user.add_words(words, title_dict, username)
