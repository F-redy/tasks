#  Вводится список email-адресов в одну строчку через пробел.
#  Среди них нужно оставить только корректно записанные адреса. Будем полагать, что к таким относятся те,
#  что используют латинские буквы, цифры и символ подчеркивания. А также в адресе должен быть символ "@",
#  а после него символ точки "." (между ними, конечно же, могут быть и другие символы).
#
# Результат отобразить в виде строки email-адресов, записанных через пробел.
#
# Sample Input:
# abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
# Sample Output:
# abc@it.ru biba123@list.ru sc_lib@list.ru

import re


def is_valid_email(email: str):
    # tmp = re.findall(r'[\w_]+@[\w._]+', email)[0]
    # return email == tmp
    return re.fullmatch(r'[\w_]+@[\w._]+', email)


print(*filter(is_valid_email, input().split()))
