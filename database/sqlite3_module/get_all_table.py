import os
import sqlite3 as sq
from dotenv import load_dotenv

load_dotenv()
DB_ENGLISH_PATH = os.getenv('DB_ENGLISH_PATH')


def get_all_table_db():
    """Вытягивает все названия существующих таблиц в базе данных"""
    with sq.connect(DB_ENGLISH_PATH) as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        return cursor.fetchall()


if __name__ == '__main__':
    print(get_all_table_db())
