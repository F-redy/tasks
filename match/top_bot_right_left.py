# Пользователь может ввести с клавиатуры следующие команды в виде строки:
#
# top или Top или TOP
# bottom или Bottom или BOTTOM
# right или Right или RIGHT
# left или Left или LEFT
#
# cmd = input()
# С помощью оператора match/case необходимо определить тип команды cmd
# и при совпадении вывести на экран сообщение в формате:
#
# Команда <название команды малыми буквами>
#
# Например, при вводе Top, должны на выходе получить:
#
# Команда top
#
# И так для всех четырех команд. Если тип команды не определен, то вывести строку:
#
# Неверная команда

cmd = input()
text_result = f'Команда {cmd.lower()}'

match cmd:
    case 'top' | 'Top' | 'TOP':
        print(text_result)
    case 'bottom' | 'Bottom' | 'BOTTOM':
        print(text_result)
    case 'right' | 'Right' | 'RIGHT':
        print(text_result)
    case 'left' | 'Left' | 'LEFT':
        print(text_result)
    case _:
        print('Неверная команда')
