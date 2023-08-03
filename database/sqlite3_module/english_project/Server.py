import os
import re
import sqlite3 as sq
from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, digits

import bcrypt
from FDataBase import FDataBase
from file_utils import FileHandler
from ValidationHelper import ValidationHelper

NAME_DB = 'english_db.db'
ROOT_PATH = os.getcwd()
DATABASE = os.path.join(ROOT_PATH, 'english_db.db')
SQL_SCRIPT = os.path.join(ROOT_PATH, 'english.sql')


def connect_db():
    connect = sq.connect(DATABASE)
    connect.row_factory = sq.Row  # записи из базы данных будут получаться в виде dict(по умолчанию список кортежей)
    return connect


def create_db():
    """Вспомогательная функция для создания базы данных."""
    db = connect_db()
    with open(SQL_SCRIPT, mode='r') as f:
        db.cursor().executescript(f.read())

    db.commit()
    db.close()


class Server:
    DB = connect_db()
    DBASE = FDataBase(DB)
    Helper = ValidationHelper()

    def __init__(self, username: str, entered_password: str, email: str = None, registration: bool = False):
        self.__verified_user = None
        self.data_user = None
        if registration:
            self.add_user(username, entered_password, email)
        else:
            self.login(username, entered_password)

    def __str__(self):
        return f"Вход выполнен пользователем {self.data_user['user']['username'].title()}."

    @classmethod
    def verification_user(cls, username: str):
        username = cls.Helper.clean_string(username)
        user = cls.DBASE.get_user(username)
        return user

    def login(self, username: str, entered_password: str):
        self.__verified_user = self.verification_user(username)
        if self.__verified_user:
            attempts = 5
            password = self.Helper.check_password(entered_password, self.__verified_user['password'])
            while attempts and not password:
                entered_password = input(f'Error password, {attempts} tries left!\nEnter correct password: ')
                attempts -= 1
                password = self.Helper.check_password(entered_password, self.__verified_user['password'])

            if not password:
                self.__verified_user = None
                raise ValueError('The attempts are over!')
            else:
                user_dictionaries = self.get_dictionaries(self.__verified_user['username'])
                self.data_user = dict()
                self.data_user['user'] = self.__verified_user
                self.data_user['dictionaries'] = user_dictionaries
                self.data_user['user']['total dictionaries'] = len(self.data_user['dictionaries'])
                print(f"Авторизация для {username.title()} прошла успешно!")
        else:
            raise TypeError(f'{username.capitalize()} не зарегистрирован!')

    @classmethod
    def add_user(cls, username: str, password: str, email: str):
        username = cls.Helper.clean_string(username)
        hashed_password = cls.Helper.hash_password(password)
        verified_email = cls.Helper.email_verification(email)

        cls.DBASE.add_user(username, hashed_password, verified_email)

    @classmethod
    def get_user(cls, username: str):
        username = cls.Helper.clean_string(username)
        return cls.DBASE.get_user(username)

    @classmethod
    def add_dictionary(cls, dictionary_title: str, user_id: int):
        dictionary_title = cls.Helper.clean_string(dictionary_title)
        slug = cls.Helper.get_slug(dictionary_title)
        date_now = cls.Helper.get_time_now()

        cls.DBASE.add_dictionary(dictionary_title, slug, date_now, user_id)

    @classmethod
    def get_dictionaries(cls, username: str):
        return cls.DBASE.get_dictionaries(username)

    @classmethod
    def get_dictionary(cls, user_id: int, dictionary_title: str):
        dictionary_title = cls.Helper.clean_string(dictionary_title)
        return cls.DBASE.get_dictionary(user_id, dictionary_title)

    @classmethod
    def add_pair(cls, original: str, translate: str, dictionary_title: str, username: str):
        dict_title, username = [cls.Helper.clean_string(word) for word in (dictionary_title, username)]
        date_now = cls.Helper.get_time_now()

        cls.DBASE.add_pair(original, translate, dictionary_title, username, date_now)

    @staticmethod
    def get_words_from_file(path_to_file: str, separator: str = ' - ') -> list[tuple[str, str]]:
        handler = FileHandler(path_to_file)
        words = handler.get_words(separator)

        return words

    @classmethod
    def add_words(cls, words: list[tuple[str, str]], dict_title: str, username: str):
        dict_title, username = [cls.Helper.clean_string(word) for word in (dict_title, username)]
        date_now = cls.Helper.get_time_now()

        cls.DBASE.add_words(words, dict_title, username, date_now)

    @classmethod
    def get_words(cls, username: str, dict_title: str):
        dict_title, username = [cls.Helper.clean_string(word) for word in (dict_title, username)]

        return cls.DBASE.get_words(username, dict_title)


create_db()
