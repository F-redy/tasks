from random import choice


def paint(text: str, color: str) -> str:
    """Colors: green, red, yellow, blue, violet, light_blue"""
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'violet': '\033[35m',
        'light_blue': '\033[36m',
        'drop_color': '\033[0m'
    }
    try:
        return f"{colors[color]}{text}{colors['drop_color']}"
    except KeyError:
        raise ValueError(f'Don\'t have color: {color}')


def italics(text: str) -> str:
    return f"\033[3m{text}\033[0m"


def read_words(words: dict) -> dict:
    print(f'\n{" ":<60} {paint(f"level: {stage}", "violet")}\n')
    for (en, ru), point in words.items():
        question = input(f'{paint("Enter translation for", "light_blue")} "{italics(ru)}": ').strip().lower()

        if question == en.strip().lower():
            words[(en, ru)] += 1
            print(f'{paint("Right!", "green")} "{en}" - "{ru}" {paint(f"has point: {point + 1}", "green")}\n')
        else:
            print(f'{paint("Error!", "red")} "{en}" - "{ru}" {paint(f"has point: {point - 1}", "red")}\n')
            words[(en, ru)] -= 1

    return words


def check_point(words: dict) -> bool:
    return all(point > 4 for point in words.values())


def get_new_pair() -> tuple[str, str]:
    new_word = choice(some_words)
    print(f'{" ":>50}{paint("new pair:", "yellow")} "{italics(" - ".join(new_word))}"')
    return new_word


def delete_pair(pair: tuple) -> None:
    some_words.remove(pair)


def start_game(start: int = 5, start_point: int = 0) -> dict:
    words = dict()
    for _ in range(start):
        p = get_new_pair()
        delete_pair(p)
        words[p] = start_point
    return words


some_words = [
    ('thoughts', 'мысли'), ('abroad', 'за границей'), ('wedding', 'свадьба'), ('sibling', 'родной брат/сестра'),
    ('cousin', 'двоюродный брат/сестра'), ('common', 'общий, распространенный'), ('obvious', 'очевидный, ясный'),
    ('in comparison', 'в сравнении'), ('overpriced', 'завышенная цена'), ('unusual', 'необычный'),
    ('stuff', 'вещи'),
    ('rude', 'грубый, невежливый'), ('behave', 'вести себя, поступать'), ('take part', 'принимать участие'),
    ('exhausted', 'истощенный, изнуренный, измученный, обессиленный'), ('descending', 'убывающий'),
    ('ascending', 'возрастающий'), ('waste', 'напрасно тратить')]

words_to_learn = start_game()
stage = 1

while True:
    words_to_learn = read_words(words_to_learn)
    check = check_point(words_to_learn)
    match check:
        case False:
            words_to_learn = read_words(words_to_learn)
        case True if some_words:
            stage += 1
            words_to_learn.update({get_new_pair(): 0})
        case _:
            break
