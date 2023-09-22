# handle_comment(data): Этот метод вызывается при обнаружении комментария в HTML-коде.
# Ему передается строка data, содержащая текст комментария.
# В методе происходит определение типа комментария (однострочного или многострочного)
# на основе наличия символов новой строки (\n) в тексте комментария.
# Затем метод выводит информацию о типе комментария и тексте комментария (если текст не равен символу новой строки).
#
# handle_data(data): Этот метод вызывается при обнаружении текстовых данных внутри элементов HTML-кода.
# Ему также передается строка data, содержащая текстовые данные.
# В методе происходит вывод информации о типе данных ("Data") и сам текст данных
# (если текст не равен символу новой строки).


# Task
#
# You are given an HTML code snippet of N lines.
# Your task is to print the single-line comments, multi-line comments and the data.
#
# Print the result in the following format:
#
# >>> Single-line Comment
# Comment
# >>> Data
# My Data
# >>> Multi-line Comment
# Comment_multiline[0]
# Comment_multiline[1]
# >>> Data
# My Data
# >>> Single-line Comment:
# Note: Do not print data if data == '\n'.
#
# Input Format
#
# The first line contains integer N, the number of lines in the HTML code snippet.
# The next N lines contains HTML code.
#
#
# Output Format
#
# Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom
# in the snippet.
#
# Format the answers as explained in the problem statement.
#
# Sample Input
# 4
# <!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->

# Sample Output
# >>> Multi-line Comment
# [if IE 9]>IE9-specific content
# <![endif]
# >>> Data
#  Welcome to HackerRank
# >>> Single-line Comment
# [if IE 9]>IE9-specific content<![endif]


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print("{}\n{}".format(">>> Multi-line Comment", data))
        else:
            print("{}\n{}".format(">>> Single-line Comment", data))

    def handle_data(self, data):
        print("{}\n{}".format(">>> Data", data)) if data != '\n' else None


parser = MyHTMLParser()
html = '\n'.join(input() for _ in range(int(input())))
parser.feed(html)
