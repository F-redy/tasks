# заполнение матрицы
def create_matrix():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]


matrix = [[100, 2, 3, 90, 100],
          [1, 54, 3, 90, 100],
          [1, 2, 5, 90, 100],
          [1, 2, 3, 2, 100],
          [1, 2, 3, 90, 100]]
n = len(matrix)


# по строкам
def row(n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


# по столбцам
def col(n):
    for j in range(n):
        for i in range(n):
            print(matrix[i][j], end=' ')
        print()


# по строкам в обратном порядке, колонки в обычном порядке
def row_reverse_col(n):
    for i in range(n - 1, -1, -1):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


# по строкам и колонкам в обратном порядке
def row_and_col_reverse(n):
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            print(matrix[i][j], end=' ')
        print()


# по строкам в нормальном порядке, по колонкам в обратном порядке
def row_col_reverse(n):
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(matrix[i][j], end=' ')
        print()


# по диагонали, слева на право, сверху вниз
def diagonal_left_right_up_down(n):
    # выше главной диагонали i < j
    # ниже главной диагонали i > j
    for i in range(n):
        for j in range(n):
            if i == j:
                print(matrix[i][j], end=' ')
    print()


# по диагонали, справо на лево, снизу вверх
def diagonal_right_left_down_up(n):
    for j in range(n - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            if i == j:
                print(matrix[i][j], end=' ')
    print()


# по диагонали, слева на право, снизу вверх
def diagonal_left_right_down_up(n):
    for i in range(n - 1, -1, -1):
        print(matrix[i][n - 1 - i], end=' ')


# по диагонали, справа на лево, сверху вниз
def diagonal_right_left_up_down(n):
    for i in range(n - 1, -1, -1):
        print(matrix[n - 1 - i][i], end=' ')
