from FDataBase import BaseDataBase


class WordsDabaBase(BaseDataBase):
    def add_pair(self, original: str, translate: str, dict_title: str, dict_id: int, user_id: int, time_now: str):
        query = """INSERT INTO words values (NULL, ?, ?, ?, ?)"""

        self.__cursor.execute(query, (original, translate, dict_id, user_id))
        self.update_dictionary_time(time_now, dict_id)

        if self.__cursor.rowcount and self.__cursor.lastrowid:
            print(f"{original} - {translate}: Были добавлены в словарь {dict_title}.")
        else:
            print(f"{original} - {translate}: Уже были добавлены!")

    def add_words(self, words: list[tuple[str, str]], dict_title: str, dict_id: int, user_id: int, time_now: str):
        query = """INSERT INTO words values (NULL, ?, ?, ?, ?)"""

        data = [(original, translate, dict_id, user_id) for original, translate in words]

        self.__cursor.executemany(query, data)
        self.update_dictionary_time(time_now, dict_id)

        if self.__cursor.rowcount and self.__cursor.lastrowid:
            print(f"Новые слова добавлены в {dict_title}.")
        else:
            print('Новых слов нет!')

    def get_words(self, user_id: int, dictionary_id: int) -> list:
        query = "SELECT w.original, w.translate FROM words WHERE user_id = ? and dictionary_id = ?"

        self.__cursor.execute(query, (user_id, dictionary_id))
        words = self.__cursor.fetchall()

        return words
