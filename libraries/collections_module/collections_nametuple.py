# Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
#
# Your task is to help Dr. Wesley calculate the average marks of the students.
#
# Note:
# 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME.(The spelling and case type of these names won 't change.)
#
# Input Format
# The first line contains an integer N, the total number of students.
# The second line contains the names of the columns in any order.
# The next N lines contains the marks, IDs,name  and class, under their respective column names.
#
# Output Format
# Print the average marks of the list corrected to 2 decimal places.

# Sample Input
#
# TESTCASE 01
#
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6
#
# TESTCASE 02
#
# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5

from collections import namedtuple


def print_average_marks(number_students: int, table_columns: list[str]) -> None:
    Student = namedtuple('Student', table_columns)
    sum_marks = 0

    for n in range(number_students):
        data = input().split()
        student = Student(*data)
        sum_marks += int(student.MARKS)

    print(round(sum_marks / number_students, 2))


def print_average_marks_short_version(number_students: int, table_columns: list[str]) -> None:
    Student = namedtuple('Student', table_columns)
    sum_marks = sum(int(Student(*input().split()).MARKS) for _ in range(number_students))
    print(round(sum_marks / number_students, 2))


n = int(input())  # Number of students
columns = input().split()  # title of columns
print_average_marks(n, columns)
