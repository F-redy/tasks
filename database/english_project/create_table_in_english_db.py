import os
import sqlite3 as sq

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH")


def check_table_in_db(title: str):
    with sq.connect(DB_PATH) as connect:
        cursor = connect.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (title,))

    return cursor.fetchone()


def create_new_table(title: str):
    with sq.connect(DB_PATH) as connect:
        cursor = connect.cursor()

    if check_table_in_db(title) is None:

        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {title}(
                        id             INTEGER         NOT NULL     PRIMARY KEY AUTOINCREMENT,
                        original       VARCHAR (70)    NOT NULL     UNIQUE,
                        translate      VARCHAR (70)    NOT NULL)"""
        )
        print(f'Table "{title}" created.')
    else:
        print(f'Table "{title}" already exists.')


table_name = input('Enter the name of the table you want to create: ').lower().strip()
create_new_table(table_name)
