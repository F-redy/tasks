# A valid email address meets the following criteria:
#
# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
# The username starts with an English alphabetical character, and any subsequent characters consist of one or more
# of the following: alphanumeric characters, -,., and _.
# The domain and extension contain only English alphabetical characters.
# The extension is 1, 2, or 3 characters in length.
# Given  pairs of names and email addresses as input, print each name and email address pair having
# a valid email address on a new line.

# Hint: Try using Email.utils() to complete this challenge. For example, this code:
#
# import email.utils


# print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')

# Функция parseaddr используется для разбора (парсинга) адреса электронной почты, представленного в виде строки.
#
# Она принимает в качестве входных данных строку, представляющую адрес электронной почты (addrstring),
# и возвращает кортеж, содержащий два элемента: имя получателя и адрес электронной почты получателя.
# Например,
#       вызов email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>') вернет ('DOSHI', 'DOSHI@hackerrank.com')


# print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
# Функция formataddr(pair) используется для форматирования имени и адреса электронной почты в одну строку,
# где pair - это кортеж с двумя элементами: имя и адрес электронной почты.
#
# Она принимает в качестве входных данных кортеж pair и возвращает строку,
#в которой имя и адрес электронной почты объединены и отформатированы для представления в форме,
# удовлетворяющей стандартам адресов электронной почты.
#
# Вызов email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')) вернет строку 'DOSHI <DOSHI@hackerrank.com>'.

# produces this output:
#
# ('DOSHI', 'DOSHI@hackerrank.com')
# DOSHI <DOSHI@hackerrank.com>

# Input Format
#
# The first line contains a single integer, n, denoting the number of email address.
# Each line  of the  subsequent lines contains a name and an email address as two space-separated values following
# this format:
# name <user@email.com>

# Output Format
#
# Print the space-separated name and email address pairs containing valid email addresses only.
# Each pair must be printed on a new line in the following format:
#
# name <user@email.com>
# You must print each valid email address in the same order as it was received as input.
#
# Sample Input
# 2
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>

# Sample Output
# DEXTER <dexter@hotmail.com>

import re
import email.utils


def check_email(e_mail) -> bool:
    pattern = re.compile(r"(?i)^[a-z][a-z0-9_\-.]+@[a-z]+\.[a-z]{1,3}$")
    return bool(pattern.match(e_mail))


for _ in range(int(input())):
    string = input()
    name, mail = email.utils.parseaddr(string)

    if check_email(mail):
        print(string)
