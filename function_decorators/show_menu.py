def show_menu(func):
    def wrapper(*args, **kwargs):
        list_menu = func(*args, **kwargs)
        [print(f"{n}. {item}") for n, item in enumerate(list_menu, 1)]
        return list_menu

    return wrapper


@show_menu
def get_menu(s: str) -> list:
    return s.split()


get_menu('Главная Добавить Удалить Выйти')
