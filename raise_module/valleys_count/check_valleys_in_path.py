def check_length_path(all_steps: int, path: str) -> None:
    if all_steps != len(path):
        raise ValueError('The number of steps is not equal to the path')


def check_valid_string_type(path: str) -> None:
    if not isinstance(path, str):
        raise TypeError('string must be only str.')


def check_valid_path(path: str) -> None:
    if any(c not in VALID_CHARS for c in path):
        raise ValueError('path must be only a letters {} or {}.'.format(*VALID_CHARS))


def check_path(all_steps: int, path: str, funcs_tuple: tuple) -> None:
    try:
        for check_func in funcs_tuple:
            if check_func.__name__ == 'check_length_path':
                check_func(all_steps, path)
            else:
                check_func(path)
    except (ValueError, TypeError) as e:
        raise type(e)(f'{TEXT_FOR_ERRORS}{e}')


def print_valley_count_text(valley: int) -> None:
    match valley:
        case 1:
            print(TEXT_RESULT[0].format(valley))
        case 2 | 3:
            print(TEXT_RESULT[1].format(valley))
        case _:
            print(TEXT_RESULT[2].format(valley))


def count_valleys_in_path(all_steps: int, path: str) -> int:
    funcs_tuple = (check_valid_string_type, check_valid_path, check_length_path)
    check_path(all_steps, path, funcs_tuple)

    altitude = valley_count = 0

    for step in path:
        u, d = VALID_CHARS
        valley_count += altitude == 0 and step == d
        altitude += 1 if step == u else -1

    return valley_count


VALID_CHARS = ('U', 'D')
TEXT_FOR_ERRORS = 'Invalid path: '
TEXT_RESULT = (
    'On your way there was {} valley.',
    'On your way there were {} valleys.',
    'There were {} valleys on your way.',
)

if __name__ == '__main__':
    steps = int(input('How many steps on the way? '))
    our_path = input('Enter path for count valleys: ').strip().upper()
    valleys_count = count_valleys_in_path(steps, our_path)
    print_valley_count_text(valleys_count)
