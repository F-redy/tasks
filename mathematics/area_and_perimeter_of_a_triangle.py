# Даны длины 3 сторон треугольника (каждая с новой строки).
#
# Найдите:
#
# Периметр треугольника
# Площадь треугольника


def perimeter(a: int, b: int, c: int) -> int:
    return a + b + c


def area(a: int, b: int, c: int) -> float:
    """формула Герона"""
    # полупериметр треугольника
    p = sum([a, b, c]) / 2
    # периметр треугольника
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


a, b, c = (int(input()) for _ in range(3))
print(perimeter(a, b, c))
print(area(a, b, c))
