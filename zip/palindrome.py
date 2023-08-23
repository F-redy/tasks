def is_palindrome(string: str) -> bool:
    """
    Проверяет, является ли заданная строка палиндромом.

    :param string: Строка, которую необходимо проверить на палиндром.
    :return: Возвращает True, если строка является палиндромом, иначе False.
    """
    for left, right in zip(string, reversed(string)):
        if left != right:
            return False
    return True
