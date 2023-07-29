import re

text = '''Lorem "ipsum" dolor sit amet, consectetur adipiscing elit, sed do eiusmod "tempor" incididunt ut labore et dolore magna aliqua. Consequat mauris nunc congue nisi. Volutpat blandit aliquam etiam erat velit scelerisque in dictum non. Amet nisl suscipit adipiscing bibendum est ultricies. In ornare quam viverra orci sagittis eu. Gravida in fermentum et sollicitudin ac orci phasellus egestas. Aliquet lectus proin nibh nisl condimentum id venenatis a. Non pulvinar neque laoreet suspendisse interdum consectetur libero. Cursus mattis molestie a iaculis at erat pellentesque adipiscing commodo. Elit ut aliquam purus sit amet. Aliquet bibendum enim facilisis gravida neque convallis a cras. Egestas maecenas pharetra convallis posuere morbi. Tempor orci eu lobortis elementum.

Amet "dictum" sit amet justo donec enim diam vulputate. Viverra justo nec ultrices dui sapien eget mi proin. A arcu cursus vitae congue mauris. In massa tempor nec feugiat nisl pretium fusce. "Curabitur" gravida arcu ac tortor dignissim. Venenatis lectus magna fringilla urna porttitor. Ut porttitor leo a diam sollicitudin. Odio aenean sed adipiscing diam donec adipiscing. Ut sem nulla pharetra diam sit amet. Pharetra massa massa ultricies mi quis hendrerit dolor magna. Elementum sagittis vitae et leo duis ut diam. Faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper. Risus sed vulputate odio ut enim. Justo nec ultrices dui sapien eget. Nec feugiat nisl pretium fusce id velit ut tortor. Ac felis donec et odio pellentesque diam. Suscipit tellus mauris a diam maecenas sed enim ut sem. Vel turpis nunc eget lorem dolor sed viverra. Non consectetur a erat nam at lectus urna.

Tempus "egestas" sed sed risus pretium quam vulputate. Mollis "aliquam" ut porttitor leo a diam sollicitudin. Nec ullamcorper sit amet risus nullam. Vitae congue eu consequat ac. Nisl suscipit adipiscing bibendum est ultricies. Curabitur vitae nunc sed velit dignissim sodales. Enim lobortis scelerisque fermentum dui faucibus in ornare quam. Mauris pharetra et ultrices neque ornare aenean euismod. Netus et malesuada fames ac turpis egestas integer eget. Sit amet risus nullam eget felis. Leo urna molestie at elementum. Velit sed ullamcorper morbi tincidunt ornare.

Sit amet "risus" nullam eget. Sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec "pretium". Egestas dui id ornare arcu odio ut sem nulla. Amet dictum sit amet justo "donec" enim diam. Mauris rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Turpis massa sed elementum tempus. Lacus sed turpis tincidunt id aliquet risus feugiat. Eu lobortis elementum nibh tellus molestie nunc non. Dolor magna eget est lorem ipsum dolor sit. Ut sem viverra aliquet eget. Pulvinar mattis nunc sed blandit libero volutpat sed cras ornare. Massa tincidunt nunc pulvinar sapien et ligula. Sit amet luctus venenatis lectus magna. Tellus cras adipiscing enim eu. Habitasse platea dictumst quisque sagittis. Non arcu risus quis varius quam quisque id diam. Sit amet dictum sit amet justo donec enim diam.
'''

# Задаем регулярное выражение для поиска двойных кавычек
pattern = r'"([^"]*)"'


# # Определяем функцию замены, которая будет вызвана для каждого совпадения
def replace_quotes(match):
    return '«' + match.group(1) + '»'


# Заменяем двойные кавычки на « и » с использованием функции замены
replaced_text = re.sub(pattern, replace_quotes, text)

# version lambda
# replaced_text = re.sub(pattern, lambda match: '«' + match.group(1) + '»', text)

print(replaced_text)


