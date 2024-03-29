# Добавляем протокол к прокси
# Условие:
# Найдите все прокси, и добавьте к ним в начало протокол http://.
#
# Что нужно сделать:
# Нужно найти следующие последовательности:
#
# Адрес состоит из любых числовых последовательностей, разделённых .
# В середине стоит :
# Порт является любой числовой последовательностью
# и в начало к ним добавить протокол http://.
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.
#
# Выходные данные:
# Строка, в которой у всех прокси стоит протокол.

import re

test_case = [
    'Будем 193.193.240.37:45944 считать 221.182.31.54:8080 что 200.199.38.234:8080 все 212.83.166.175:5836 '
    'прокси 74.121.98.90:8080 валидные 82.200.181.54:3128 125.25.82.191:8080 187.108.90.163:44574 202.21.105.115:80'
    '103.89.235.226:83 190.93.176.11:8080 54.189.97.191:3128 85.114.98.246:8080 190.242.98.61:8083 173.82.74.62:5836 '
    '213.27.152.15:3128 154.126.211.169:41014 37.59.115.136:3128 89.191.131.243:8080 66.96.255.46:45619 '
    '190.117.115.150:65103 5.45.64.97:3128 154.66.108.70:53281 185.97.122.226:53281',
    "Сайт 1: 192.168.1.10:8080",
    "Сайт 2: 10.20.30.40:8000",
    "Сайт 3: 123.45.67.89:1234",
    "Сайт 4: 255.255.255.255:9999",
    "Сайт 5: 1.2.3.4:12345",
]

pattern = r"([\d\.]+\:\d+)\b"
for test in test_case:
    print(re.sub(pattern, r'http://\1', test))
