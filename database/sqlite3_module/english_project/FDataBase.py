import sqlite3 as sq


class FDataBase:
    def __init__(self, db: sq.Connection):
        self.__db = db
        self.__cursor = db.cursor()

    def add_user(self, username: str, hashed_password: str, verified_email: str) -> dict[str: str | int]:
        query = """INSERT OR IGNORE INTO users values (NULL, ?, ?, ?, NULL)"""

        self.__cursor.execute(query, (username, hashed_password, verified_email))
        self.__db.commit()

        if self.__cursor.rowcount:
            print(f"Пользователь {username.capitalize()} был успешно создан!")
        else:
            print(f"Пользователь {username.capitalize()} уже существует!")

    def get_user(self, username: str):
        query = """SELECT id, username, password, email, avatar FROM users WHERE username = ?"""

        user = self.__cursor.execute(query, (username,)).fetchone()

        if user:
            return dict(user)

        raise ValueError(f"User {username} not found!")

    def change_user_password(self, email: str, password: str):
        query = f"""UPDATE users SET password = ? WHERE email = ?"""
        try:
            self.__cursor.execute(query, (password, email))
            self.__db.commit()
            print('Пароль изменён!')
        except sq.Error as e:
            print(f'Ошибка изменения пароля для {email}\n{str(e)}')

    def add_dictionary(self, dictionary_name: str, dictionary_slug: str, date_now: str, user_id: int):
        query = """INSERT OR IGNORE INTO dictionaries values (NULL, ?, ?, ?, ?, ?) """

        self.__cursor.execute(query, (dictionary_name, dictionary_slug, date_now, date_now, user_id))
        self.__db.commit()

        if self.__cursor.rowcount:
            print(f"Словарь {dictionary_name} был создан!")
        else:
            print(f"Словарь {dictionary_name} уже существует!")

    def get_dictionaries(self, username: str) -> dict[dict[str: int | str]]:
        query = """
                    SELECT d.id, d.title, d.dictionary_slug, d.created_at, d.updated_at, d.user_id
                    FROM dictionaries AS d
                    JOIN users AS u ON d.user_id = u.id
                    WHERE u.username = ?
                    """

        dictionaries = self.__cursor.execute(query, (username,)).fetchall()

        if dictionaries:
            return {dictionary['title']: dict(dictionary) for dictionary in dictionaries}
        else:
            return dict()

    def get_dictionary(self, user_id: int, dictionary_title: str) -> dict[str: str | int]:
        query = """SELECT id, title, dictionary_slug, created_at, updated_at, user_id FROM dictionaries 
                                                                                WHERE user_id = ? and title = ?"""
        dictionary = self.__cursor.execute(query, (user_id, dictionary_title)).fetchone()

        if dictionary:
            return dict(dictionary)
        raise ValueError(f"Dictionary: {dictionary_title} not found!")

    def update_dictionary(self, time_now: str, dictionary_id: int):
        query = f"""UPDATE dictionaries SET updated_at = ? WHERE id = ?"""

        self.__cursor.execute(query, (time_now, dictionary_id))
        self.__db.commit()

    def add_pair(self, original: str, translate: str, dict_title: str, username: str, time_now: str):
        query = """INSERT OR IGNORE INTO words values (NULL, ?, ?, ?, ?)"""

        user = self.get_user(username)
        dictionary = self.get_dictionary(user['id'], dict_title)

        self.__cursor.execute(query, (original, translate, dictionary['id'], user['id']))
        self.update_dictionary(time_now, dictionary['id'])

        if self.__cursor.rowcount and self.__cursor.lastrowid:
            print(f"{original} - {translate}: Были добавлены в словарь {dictionary['title']}.")
        else:
            print(f"{original} - {translate}: Уже были добавлены!")

    def add_words(self, words: list[tuple[str, str]], dict_title: str, username: str, time_now: str):
        query = """INSERT OR IGNORE INTO words values (NULL, ?, ?, ?, ?)"""

        user = self.get_user(username)
        dictionary = self.get_dictionary(user['id'], dict_title)
        data = [(original, translate, dictionary['id'], user['id']) for original, translate in words]

        self.__cursor.executemany(query, data)
        self.update_dictionary(time_now, dictionary['id'])

        if self.__cursor.rowcount and self.__cursor.lastrowid:
            print(f"Новые слова добавлены в {dictionary['title']}.")
        else:
            print('Новых слов нет!')

    def get_words(self, username: str, dict_title: str):
        query = """
                    SELECT w.original, w.translate
                    FROM words AS w
                    INNER JOIN dictionaries d ON w.dictionary_id = d.id
                    INNER JOIN users u ON d.user_id = u.id
                    WHERE u.username = ? AND d.title = ?
                """

        self.__cursor.execute(query, (username, dict_title))
        words = self.__cursor.fetchall()

        return words
