# Вор ключей
# Условие:
# Вы получили доступ к секретному чату, в котором часто дарят ключи от Windows 7, и решили украсть один из них,
# т.к. у вас не активирован Windows 7. Вы выкачали все сообщения от новых к старым и проходите по ним программой.
#
# Что нужно сделать:
#  Нужно найти первый попавшийся ключ. Нужные ключи в чате всегда отправляют в виде:
#
# Activation key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
# X - любая цифра или латинская буква в верхнем регистре
# Перед нужным ключом должна стоять строка Activation key:
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 5 строк. Гарантируется, что в этих строках есть как минимум 1 ключ.
#
# Выходные данные:
# Выведите в консоль ключ, который был найден. Только ключ. Другие данные не нужны.


import re

test_case = [
    (['Hi', 'Here is my Activation key: PKRHK-6622Q-T49PV-CC3PX-TRX2Y', 'Bye', 'Test', 'Lmao'],
     'PKRHK-6622Q-T49PV-CC3PX-TRX2Y'),
    (['Would you care for1 a cup of tea?', 'Only if you’re having one.', 'CM0T1-6W7ZJ-XY0Z3-ZROM3-BDLZ9',
      'Yeah I have one and I have one Activation key: BR3DD-WJ2D6-RM84G-BHWQK-WFHW3', 'Do you take milk and sugar?'],
     'BR3DD-WJ2D6-RM84G-BHWQK-WFHW3'),
    (['I expect you could do with', 'a cup of tea, couldn’t you?', 'Activation key: A70PM-KQ_BA-HYF2D-16CMK-OM4FP',
      'Guys one Activation key: C7KYW-CBKVC-DPC82-7TPKD-Y8T2C for you', 'TY BRO!'],
     'C7KYW-CBKVC-DPC82-7TPKD-Y8T2C'),
    (['Activation key: A70PM-KQ-BA-HYF2D-16CMK-OM4FP', 'JFP9D-7C4Z9-XHFMD-KH3TX-NTS6Z',
      'Activatin key: ONHVS-A705Q-QIWMB-3TRKD-93JQV', 'gg key: J4DP3-WT02L-VK1DN-36ET7-MEKYI',
      'Activation key: VMXSA-5FPC7-ERNTC-XG3YO-EG9W6'],
     'VMXSA-5FPC7-ERNTC-XG3YO-EG9W6'),
    (['Activation key: ZxHMR-TVFQE-QUEP7-ZRYOV-7SPEX', 'JFP9D-7C4Z9-XHFMD-KH3TX-NTS6Z',
      'Activatin key: ONHVS-A705Q-QIWMB-3TRKD-93JQV', 'gg key: J4DP3-WT02L-VK1DN-36ET7-MEKYI',
      'Activation key: 9KAOG-UTB4I-6JAE3-75BR2-IB27P'],
     '9KAOG-UTB4I-6JAE3-75BR2-IB27P'),
    (['Hi', 'Here is my Activation key: PKRHKF6622QGT49PVVCC3PX3TRX2Y', 'Bye',
      'Activation key: 9KAOG-UTB4I-6JAE3-75BR2-IB27P', 'Lmao'],
     '9KAOG-UTB4I-6JAE3-75BR2-IB27P'),
]

# lst_string = [input() for _ in '12345']
regex = r"(?<=Activation key: )(([A-Z\d]{5}-){4}[A-Z\d]{5})\b"


def find_win_key(lst: list[str], pattern: str) -> str:
    for string in lst:
        key = re.search(pattern, string)
        if key:
            return key[0]


# print(find_win_key(lst_string, regex))
for i, (lst_string, expected_result) in enumerate(test_case, 1):
    result = find_win_key(lst_string, regex)
    assert expected_result == result, f'TEST-{i}: ERROR!\n{result} != {expected_result}'
    print(f'TEST-{i}: OK')
