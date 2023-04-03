from datetime import datetime


def time_conversion(string):
    # Преобразуем строку в объект datetime
    # где %I обозначает часы в 12-часовом формате, %M - минуты, %S - секунды, %p - AM/PM.
    dt = datetime.strptime(string, '%I:%M:%S%p')

    # Преобразуем объект datetime в строку в формате 24-часового времени
    # %H обозначает часы в 24-часовом формате.
    return dt.strftime('%H:%M:%S')


s = '07:05:45PM'
result = time_conversion(s)
print(result)  # '19:05:45'
