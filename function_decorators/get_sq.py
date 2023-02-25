# Объявите функцию с именем get_sq,
# которая вычисляет площадь прямоугольника по двум параметрам: width и height - ширина и высота прямоугольника.
# И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру:
#
# def get_sq(width, height): ...
#
# Определите декоратор func_show для этой функции,
# который отображает результат на экране в виде строки (без кавычек):
#
# "Площадь прямоугольника: <значение>"
#
# Sample Input:
# 8 11
# Sample Output:
# Площадь прямоугольника: 88

def func_show(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {value}")
        return value

    return wrapper


@func_show
def get_sq(width, height):
    return width * height


get_sq(8, 11)
