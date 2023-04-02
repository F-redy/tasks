import os
import sqlite3 as sq
from pathlib import Path
from typing import Dict, List, Tuple

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH")
FOLDER_PATH = os.getenv("FOLDER_PATH")


def table_exists(table_name: str) -> bool:
    """
    Checks if a table with the given name exists in the database.

    :param table_name: Name of the table to check.
    :return: True if the table exists, False otherwise.
    """

    with sq.connect(DB_PATH) as connect:
        cursor = connect.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))

        if not cursor.fetchone():
            print(f"Table '{table_name}' doesn't exist")
            return False
        return True


def get_file_path(file_name: str) -> str:
    """
    Returns the absolute path to the file with the given name, if such a file exists.

    :param file_name: File name without extension.
    :return: The absolute path to the file, if it exists.
    :raise:
        FileNotFoundError: If the file does not exist.
        Exception: If another error occurred.
    """

    file_path = Path(FOLDER_PATH) / f"{file_name}.txt"
    try:
        file_path.resolve(strict=True)
        return str(file_path)
    except FileNotFoundError:
        raise f"File '{file_name}.txt' does not exist"
    except Exception as e:
        raise f"Error occurred while trying to get file path: {e}"


def get_words_from_table(table_name: str) -> Dict[str, List[str]]:
    """
        Gets all words from a table in the database.

        :param table_name: Name of the table to get words from.
        :return: A dictionary containing all words in the table, where the key is the original word and the value is a
                 list of translations.
        """

    if table_exists(table_name):
        with sq.connect(DB_PATH) as connect:
            cursor = connect.cursor()

            words_bd = cursor.execute(f"SELECT original, translate FROM {table_name}").fetchall()

        return dict(words_bd)


def split_string(string: str) -> Tuple[str, str]:
    """Splits a string into two parts based on the delimiter " - ".

    :param string: The string to split.
    :return: A tuple containing the two parts of the string.
    """

    while True:
        try:
            original_word, translate_word = string.lower().rstrip().split(' - ')
            return original_word, translate_word
        except ValueError:
            string = input(f'Correct the line "{string}": ')
            continue


def create_word_dictionary(path: str) -> Dict[str, List[str]]:
    """
    Reads a file containing words and translations and creates a dictionary.

    :param path: The path to the file containing the words.
    :return: A dictionary containing all the words in the file, where the key is the original word and the value is a
             list of translations
    """

    dictionary = dict()

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.rstrip():
                original_word, translate_word = split_string(line)
                dictionary.setdefault(original_word, []).append(translate_word)

    return dictionary


def create_new_word_dictionary_for_table(path: str, table_name: str) -> Dict[str, List[str]]:
    """Creates a dictionary containing all the new words and their translations that are not already in the table.

    :param path: The path to the file containing the words.
    :param table_name: The name of the table to check for existing words.
    :return: a dictionary containing new words and their translations.
    """

    new_dictionary = dict()

    words_in_file = create_word_dictionary(path)
    words_in_table = get_words_from_table(table_name)

    if words_in_table:
        for word, translate_word in words_in_file.items():
            if words_in_table.get(word) is None:
                new_dictionary.setdefault(word, []).extend(translate_word)

    return new_dictionary if new_dictionary else words_in_file


def insert_words(file_name: str, dict_name: str) -> None:
    """
    Function insert new word to table in db.
    :param file_name: file_name to file with words;
    :param dict_name: table name;
    """
    path = get_file_path(file_name)

    if path and table_exists(dict_name):
        with sq.connect(DB_PATH) as connect:
            cursor = connect.cursor()

            dictionary = create_new_word_dictionary_for_table(path, dict_name)

            for word, translations in dictionary.items():
                translations = "".join(translations) if len(translations) == 1 else f"({', '.join(translations)})"
                cursor.execute(f"INSERT INTO {dict_name} (original, translate) VALUES (?, ?)",
                               (word, translations))

            print('Words added.')


title_file = input('Enter file name: ').lower().strip()
dictionary_name = input('Enter dictionary name: ').lower().strip()
insert_words(title_file, dictionary_name)
