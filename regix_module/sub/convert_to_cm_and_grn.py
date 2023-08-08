# Пересчет в документе
# Условие:
# На вход программе подается строка текста.
#
# В тексте могут использоваться дюймы и доллары. Дюймы нужно перевести в сантиметры, а доллары - в грн.
#
# Примечание 1 :
#
# 1 дюйм  = 2,54 см, курс доллара считайте равным 37,4 грн за один доллар
#
# Примечание 2:
#
# Если полученное число целое - округлите его до 0 знаков после запятой, если нет - до двух знаков после запятой.


import re

test_case = [('GROHE Aria 25081000 - Смеситель для ванны (хром) - $558',  # 1
              'GROHE Aria 25081000 - Смеситель для ванны (хром) - 20869,2 грн'),
             ('SCBRHMI Серийный ЖК-дисплей HMI TFT с сенсорной панелью 10,4 дюйма - $95,25',  # 2
              'SCBRHMI Серийный ЖК-дисплей HMI TFT с сенсорной панелью 26,42 см - 3562,35 грн'),
             ('Кран шаровый 1" наружная резьба - нет в продаже',  # 3
              'Кран шаровый 2,54 см наружная резьба - нет в продаже'),
             ('Камера GoPro HERO 11 Black - $399,99',  # 4
              'Камера GoPro HERO 11 Black - 14959,63 грн'),
             ('Dual Battery Charger + Enduro Batteries $59,99',  # 5
              'Dual Battery Charger + Enduro Batteries 2243,63 грн'),
             ('Protective Housing - $49,99',  # 6
              'Protective Housing - 1869,63 грн'),
             ('SanDisk Extreme microSDXC 256GB - $48,1',  # 7
              'SanDisk Extreme microSDXC 256GB - 1798,94 грн'),
             ('GoPro The Handler Floating Hand Grip - $29,99',  # 8
              'GoPro The Handler Floating Hand Grip - 1121,63 грн')
             ]

pattern = re.compile(r"(\$)(\d+,?\d*)|(\d+,?\d*)(?: ?дюйм[а|ов]?|\")")
rate_d = float(input('Enter dollar exchange rate(курс доллара): ').replace(',', '.'))


def convert(match: re.Match) -> str:
    factor, unit = ((2.54, 'см'), (rate_d, 'грн'))['$' == match[1]]
    num = float((match[2] or match[3]).replace(',', '.')) * factor
    x = (round(num, 2), int(num))[int(num) == num]

    return '{} {}'.format(str(x).replace('.', ','), unit)


for i, (test, answer) in enumerate(test_case, 1):
    result = pattern.sub(convert, test)
    assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
    print(f'TEST №{i} - OK\n{result}\n')
