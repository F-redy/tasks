from random import choice


def read_words(words: dict) -> dict:
    print(f'{" ":<60} level: {stage}')
    for (en, ru), point in words.items():
        question = input(f'Enter translation for "{ru}": ').strip().lower()
        if question == en.strip().lower():
            words[(en, ru)] += 1
            print(f'Right! "{en}" - "{ru}" has point: {point + 1}\n')
        else:
            print(f'Error! Point -1. "{en}" - "{ru}" has point: {point -1}\n')
            words[(en, ru)] -= 1
    return words


def check_point(words: dict) -> bool:
    return all(point > 4 for point in words.values())


def get_new_pair() -> tuple[str, str]:
    new_word = choice(some_words)
    print(f'{" ":>55}new pair: "{" - ".join(new_word)}"')
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
    if not check_point(read_words(words_to_learn)):
        words_to_learn = read_words(words_to_learn)
    if some_words:
        stage += 1
        words_to_learn.update({get_new_pair(): 0})