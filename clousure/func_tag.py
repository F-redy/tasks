# Используя замыкания функций, объявите внутреннюю функцию,
# которая заключает строку s (s - строка, параметр внутренней функции) в произвольный тег,
# содержащийся в переменной tag - параметре внешней функции.
#
# Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым.
# Вторую строку нужно поместить в тег из первой строки с помощью реализованного замыкания.
# Результат выведите на экран.
#
# P.S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
#
# Sample Input:
# div
# Сергей Балакирев
# Sample Output:
# <div>Сергей Балакирев</div>


def func_tag(tag: str):
    def func_string(string: str) -> str:
        return f"<{tag}>{string}</{tag}>"

    return func_string


t, s = input(), input()
func = func_tag(t)
print(func(s))
