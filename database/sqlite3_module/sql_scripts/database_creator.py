import sqlite3


def execute_sql_script(sql_file, db_file):
    # Открываем соединение с базой данных
    with sqlite3.connect(db_file) as connect:
        cursor = connect.cursor()

        # Читаем SQL-скрипт из файла
        with open(sql_file, 'r') as file:
            sql_script = file.read()

        # Выполняем SQL-скрипт
        cursor.executescript(sql_script)


# Укажите путь к SQL-скрипту и файлу базы данных
sql_script_file = 'path to sql script'
database_file = r'path to db'

# Вызываем функцию для выполнения скрипта
execute_sql_script(sql_script_file, database_file)
