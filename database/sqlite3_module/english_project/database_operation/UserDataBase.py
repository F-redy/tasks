import sqlite3 as sq

from FDataBase import BaseDataBase


class UserDataBase(BaseDataBase):

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
