from random import choice

COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'violet': '\033[35m',
    'light_blue': '\033[36m',
    'drop_color': '\033[0m'
}
NEXT_LVL_POINT = 4  # Количество очков для получения новых слов
STARTING_WORD_COUNT = 5  # Количество слов в каждом круге
START_POINT = 0  # Начальное количество очков
STAGE = 1  # Сколько раз уже прошли по словарю
STEP = 1  # Сколько раз повторялись слова на круге
MAX_REPEAT = 4  # Сколько раз повторить весь цикл


def paint(text: str, color: str) -> str:
    """
    The function paints the input text in the specified color.

    Available colors:
    - 'green'     : Green color
    - 'red'       : Red color
    - 'yellow'    : Yellow color
    - 'blue'      : Blue color
    - 'violet'    : Violet color
    - 'light_blue': Light blue color

    :param text: The text to be colored.
    :param color: The desired color for the text.

    :return: The input text wrapped in ANSI color codes for the specified color.

    :raises ValueError: If an unsupported color is provided.
    """
    try:
        return f"{COLORS[color]}{text}{COLORS['drop_color']}"
    except KeyError:
        raise ValueError(f'Don\'t have color: {color}')


def italics(text: str) -> str:
    """
    The function applies italics formatting to the input text.

    :param text: The text to be formatted in italics.
    :return: The input text with italics formatting applied.
    """
    return f"\033[3m{text}\033[0m"


def print_message(result: str, origin: str, translate: str, point: int, color: str) -> None:
    """
    The function prints the text result  with the received data.

    :param result: text: Right or Error
    :param origin: word in original language
    :param translate: word in translate language
    :param point: number of points available
    :param color: color for text
    :return: None
    """
    point = point + 1 if result.lower() == 'right' else point - 1

    print(f'{paint(f"{result.title()}! ", color)}'
          f'{italics(f"<< {origin} | {translate} >>")}'
          f'{paint(f" has point: {point}", "green")}\n')


def read_words(words: dict) -> dict:
    """
    Reads and evaluates user input for word translations, updating the word dictionary.

    :param words: A dictionary containing word pairs and their associated point values.
    :return: The updated word dictionary after user input is processed.
    """

    print(f'\n{" ":<60} {paint(f"level: {STAGE}", "violet")}{paint(f" | step: {STEP}", "violet")}\n')
    for (en, ru), point in words.items():
        question = input(f'{paint("Enter translation for", "light_blue")} "{italics(ru)}": ').strip().lower()

        if question == en.strip().lower():
            words[(en, ru)] += 1
            print_message("Right", en, ru, point, 'green')
        else:
            print_message("Error", en, ru, point, 'red')
            words[(en, ru)] -= 1

    return words


def check_point(words: dict) -> dict:
    """
    Evaluates the points associated with word pairs and organizes them for further action.

    :param words: A dictionary containing word pairs and their associated point values.
    :return: A dictionary containing word pairs and their point values, filtered based on the point threshold.
             Returns None if no word pairs need to be repeated.
    """

    go_repeat = {}
    for pair, point in words.items():
        if point < NEXT_LVL_POINT:
            go_repeat[pair] = point
        else:
            common_words.update({pair: point})
    return go_repeat or None


def get_new_pair() -> tuple[str, str]:
    """
    Retrieves a new word pair randomly selected from the list of available word pairs.

    :return: A tuple containing the new word pair, where the first element is the original word or phrase,
             and the second element is its translation.
    """

    new_word = choice(some_words)
    print(f'{" ":>35}'
          f'{paint("new pair:", "yellow")}'
          f'{paint(" << ", "yellow")}'
          f'{paint(f"{italics(new_word[0]):<30}", "light_blue")}'
          f'{paint("|", "yellow"):<20}'
          f'{paint(f"{italics(new_word[1])}", "light_blue")}'
          f'{paint(" >>", "yellow")}')

    return new_word


def delete_pair(pair: tuple) -> None:
    some_words.remove(pair)


def start_game(start_words: int = STARTING_WORD_COUNT, start_point: int = START_POINT) -> dict:
    words = dict()
    for _ in range(start_words):
        if some_words:
            p = get_new_pair()
            delete_pair(p)
            words[p] = start_point
        else:
            return words
    return words


some_words = [
    ('thoughts', 'мысли'), ('abroad', 'за границей'), ('wedding', 'свадьба'), ('sibling', 'родной брат/сестра'),
    ('cousin', 'двоюродный брат/сестра'), ('common', 'общий, распространенный'), ('obvious', 'очевидный, ясный'),
    ('in comparison', 'в сравнении'), ('overpriced', 'завышенная цена'), ('unusual', 'необычный'),
    ('stuff', 'вещи'),
    ('rude', 'грубый, невежливый'), ('behave', 'вести себя, поступать'), ('take part', 'принимать участие'),
    ('exhausted', 'истощенный, изнуренный, измученный, обессиленный'), ('descending', 'убывающий'),
    ('ascending', 'возрастающий'), ('waste', 'напрасно тратить')]

if __name__ == "__main__":
    words_to_learn = start_game()
    common_words = {}

    while STAGE < MAX_REPEAT:
        words_to_learn = read_words(words_to_learn)
        words_to_learn = check_point(words_to_learn)

        match words_to_learn:
            case dict():
                STEP += 1
                words_to_learn = read_words(words_to_learn)
            case None if some_words:
                STEP = 1
                words_to_learn = start_game()
            case None if not some_words:
                STEP = 1
                STAGE += 1
                some_words = common_words
                words_to_learn = start_game()
                common_words = {}
            case _:
                break
