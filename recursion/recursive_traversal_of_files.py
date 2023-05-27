import os

PATH = 'ПОЛНЫЙ АДРЕСС ПАПКИ ДЛЯ СКАНИРОВАНИЯ'


def scan_dir(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print(f'Спускаемся {path}\\{i}')
            scan_dir(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)


scan_dir(PATH)
