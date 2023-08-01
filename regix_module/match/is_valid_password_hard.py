import re
from itertools import zip_longest

# Хотя бы одна маленькая буква, одна большая буква, одна цифра
# и один специальный символ, и общая длина не менее 8 символов
pattern = re.compile("""(?x)
    ^                   # Начало строки
    (?=.*[a-z])         # Хотя бы одна маленькая буква (позитивный просмотр вперед)
    (?=.*[A-Z])         # Хотя бы одна большая буква (позитивный просмотр вперед)
    (?=.*\d)            # Хотя бы одна цифра (позитивный просмотр вперед)
    (?=.*[!@#$%^&*()\-_=+{};:,.<>?/|\\~])  # Хотя бы один специальный символ (позитивный просмотр вперед)
    [a-zA-Z\d!@#$%^&*()\-_=+{};:,.<>?/|\\~]{8,}  # Символы из указанных классов и длина не менее 8
    $                   # Конец строки
""")

password_case = ['ojyFKx9W', '4a9kgJ7Z', 'qEcWVYte', 'VpdxP5CK', 'mZVYFcQA', 'aEPl2On2', 'jUq09lAT', 'Q9SAfNvn',
                 'YtBXDxTr', 'ttSjPTZt', '12345', '123456', '1234567', '12345678', '123456789', 'abcdfgtyh', '9wjDXFAB',
                 'Zeiu6b91', 'h7mD4Z98', 'bXpexjno', 'UzWsa58I', 'aV9Rc8pj', 'AvUwZhjS', 'VnmExFqt', 'HFAfln1y',
                 'Cw1pwMgV', 'xk\\U$=[ZN*[@', '-\\nN8A{y6o9X', '`fBLRmI)xI{v', "_+N'<#YafVzA", '{FV9%TwHq%Ta',
                 '%4XL7=B@JE(r', ',0v;4J4RihoB', '%w^lec"d@8C/', "s(pN'7$pnckV", 'Has{?(PPH^aW',
                 'ASDASFASKJF', 'ASdsadAD', 'g=gxcU:-e[RR', 'Zj[%@TYeD<M)', ':*aW$M0,TXgP', 'F.,`j2Dh]}!S',
                 'nOw(}-\-/_a}', '8&}s7X1rq*pw', 'm%;X1cp?<{5m', 'edrL8_~x3|l', '2.S:5bfZi8a', ';ppj{KuyM5Xr'
                 ]

strong_passwords = []
simple_passwords = []
for password in password_case:
    if re.match(pattern, password):
        strong_passwords.append(password)
    else:
        simple_passwords.append(password)

print('Strong password:', ' ' * 25, 'Simple password:')
for g, e in zip_longest(strong_passwords, simple_passwords, fillvalue=" " * 12):
    print(f'{g:<43}{e}')
