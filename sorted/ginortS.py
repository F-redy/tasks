# You are given a string S.
# S contains alphanumeric characters only.
#
# Your task is to sort the string  in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
#
# Input Format
#
# A single line of input contains the string S.
#
# Output Format
#
# Output the sorted string S.


def custom_sort(s):
    # Создайте ключ сортировки, который указывает порядок сортировки
    def custom_key(char):
        if char.islower():
            return 0, char
        if char.isupper():
            return 1, char
        if char.isdigit():
            if int(char) % 2 == 1:
                return 2, char
            return 3, char

    sorted_s = sorted(s, key=custom_key)  # Используйте ключ сортировки
    return ''.join(sorted_s)


if __name__ == "__main__":
    s = input('Enter a string: ')
    result = custom_sort(s)
    print(result)
