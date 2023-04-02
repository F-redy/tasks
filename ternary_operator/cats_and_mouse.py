# You are given q queries in the form of three integers a, b, and c. For each query,
# print the appropriate answer on a new line:
#
# If cat A catches the mouse first, print Cat A.
# If cat B catches the mouse first, print Cat B.
# If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

# Function Description
#
# Complete the who_catches_mouse function in the editor below. It should return one of the three strings as described.
#
# who_catches_mouse has the following parameter(s):
#
# int a: Cat A's position
# int b: Cat B's position
# int mouse: Mouse C's position
# Input Format
#
# The first line contains a single integer, q, denoting the number of queries.
# Each of the q subsequent lines contains three space-separated integers describing the respective values of a
# (cat A's location), b (cat B's location), and c (mouse C's location) for that query.

def who_catches_mouse(a: int, b: int, mouse: int) -> str:
    cat_1, cat_2 = (abs(cat - mouse) for cat in [a, b])

    return 'Mouse C' if cat_1 == cat_2 else ('Cat B', 'Cat A')[cat_1 < cat_2]


if __name__ == '__main__':
    request = int(input())
    for _ in range(request):
        cat_a, cat_b, mouse_c = map(int, input().split())
        print(who_catches_mouse(cat_a, cat_b, mouse_c))
