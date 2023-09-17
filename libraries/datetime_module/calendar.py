# Task
#
# You are given a date. Your task is to find what the day is on that date.
#
# Input Format
#
# A single line of input containing the space separated month, day and year, respectively, in MM DD YYY format.

# Constraints
#
# 2000 < year < 3000

# Output Format
#
# Output the correct day in capital letters.

import datetime


def find_day(month: int, day: int, year: int) -> str:
    # Create a datetime object for the given date
    date_object = datetime.date(year, month, day)

    # Get the day of the week in capital letters
    day_of_week = date_object.strftime("%A").upper()
    return day_of_week


# Read the input date in the format (month, day, year)
inp_month, inp_day, inp_year = map(int, input().split())
print(find_day(inp_month, inp_day, inp_year))
