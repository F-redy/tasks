# Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
# Определите декоратор для этой функции, который имеет один параметр tag,
# определяющий строку с названием тега и начальным значением "h1".
# Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
#
# Пример заключения строки "python" в тег h1: <h1>python</h1>
#
# Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию

# Sample Input:
# Декораторы - это классно!
# Sample Output:
# <div>декораторы - это классно!</div>


from functools import wraps


def tag(tag: str):
    def real_decorators(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return wrapper

    return real_decorators


@tag('div')
def _lower(string: str) -> str:
    return string.lower()


if __name__ == '__main__':
    s = input()
    print(_lower(s))
