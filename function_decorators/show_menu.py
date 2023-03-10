# На вход программы поступает строка с названиями пунктов меню,
# записанные в одну строчку через пробел. Необходимо задать функцию с именем get_menu,
# которая преобразует эту строку в список из слов и возвращает этот список.
# Сигнатура функции, следующая:
#
# def get_menu(s): ...
#
# Определите декоратор для этой функции с именем show_menu,
# который отображает список на экран в формате:
# 1. Пункт_1
# 2. Пункт_1
# ...
# N. Пункт_N
#
# Примените декоратор show_menu к функции get_menu, используя оператор @.
# Более ничего в программе делать не нужно.
#
# Sample Input:
# Главная Добавить Удалить Выйти
# Sample Output:
# 1. Главная
# 2. Добавить
# 3. Удалить
# 4. Выйти

def show_menu(func):
    def wrapper(*args, **kwargs):
        list_menu = func(*args, **kwargs)
        [print(f"{n}. {item}") for n, item in enumerate(list_menu, 1)]
        return list_menu

    return wrapper


@show_menu
def get_menu(s: str) -> list:
    return s.split()


if __name__ == '__main__':
    s = input()
    get_menu(s)
