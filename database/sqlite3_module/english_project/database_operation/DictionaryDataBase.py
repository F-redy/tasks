from FDataBase import BaseDataBase


class DictionaryDataBase(BaseDataBase):

    def add_dictionary(self, dictionary_name: str, dictionary_slug: str, date_now: str, user_id: int):
        query = """INSERT INTO dictionaries values (NULL, ?, ?, ?, ?, ?) """

        self.__cursor.execute(query, (dictionary_name, dictionary_slug, date_now, date_now, user_id))
        self.__db.commit()

        if self.__cursor.rowcount:
            print(f"Словарь {dictionary_name} был создан!")
        else:
            print(f"Словарь {dictionary_name} уже существует!")

    def get_dictionaries(self, user_id: int) -> dict[dict[str: int | str]]:
        query = "SELECT id, title, dictionary_slug, created_at, updated_at, user_id FROM dictionaries WHERE user_id = ?"

        dictionaries = self.__cursor.execute(query, (user_id,)).fetchall()

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
