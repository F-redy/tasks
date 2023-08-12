import sqlite3 as sq

from DictionaryDataBase import DictionaryDataBase
from UserDataBase import UserDataBase
from WordsDataBase import WordsDabaBase


class BaseDataBase:
    def __init__(self, db: sq.Connection):
        self.__db = db
        self.__cursor = db.cursor()

    def update_dictionary_time(self, time_now: str, dictionary_id: int):
        query = f"""UPDATE dictionaries SET updated_at = ? WHERE id = ?"""

        self.__cursor.execute(query, (time_now, dictionary_id))
        self.__db.commit()


class FDataBase(UserDataBase, DictionaryDataBase, WordsDabaBase): pass
