import re

test_case = ["Как же я люблю **Markdown**!", "А тут и **Bold text**, и *Italic*!", "*Курсив* и **Жирный текст**",
             "Просто обычный текст без форматирования", "**Жирный текст*",  # не решен
             "***Текст с разными*** *форматами*",
             "*Курсив с **жирным** текстом*",  # не решен
             "Просто обычный текст без форматирования",
             "Текст с одиночным * символом",
             "Текст с несколькими *** символами",
             "**Текст с **неправильным форматом",
             "*Текст с пропущенными * тегами",
             "Текст с несколькими ** разделителями"
             ]

# pattern = r"(\*{1,2})(.+?)\1"
pattern = r"(?<![\*|\*\*])(\*{1,2})([^\*|\*\*]+?)(\*{1,2})(?![\*|\*\*])"


# v1
def convert(match_obj):
    key, text, _ = match_obj.groups()
    return {"**": r"<strong>{}</strong>", "*": r"<em>{}</em>"}.get(key).format(text)


# v2
def convert_to_html(match):
    stars, string, _ = match.groups()
    return fr"<strong>{string}</strong>" if stars == "**" else fr"<em>{string}</em>"


# v3
def convert_to_html_format(match: re.Match) -> str:
    return (r"<em>{}</em>", r"<strong>{}</strong>")[match[1] == "**"].format(match[2])


func_list = [convert_to_html_format, convert, convert_to_html]


for test in test_case:
    print(f'{" ":<3}<--function-->{" ":<32}<--result-->{" ":<50}<--test-string-->')
    for func in func_list:
        res = re.sub(pattern, func, test)
        f = " " * (37 - len(func.__name__))
        print(f'{func.__name__}{f}{res}{" " * (106 - len(res) - len(f) - len(func.__name__))}{test}')
    print()

