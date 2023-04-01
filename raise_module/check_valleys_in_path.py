def check_valid_string_type(string: str) -> None:
    if not isinstance(string, str):
        raise TypeError('string must be only str.')


def check_valid_path(string: str) -> None:
    if any(c not in VALID_CHARS for c in string):
        raise ValueError('path must be only a letters {} or {}.'.format(*VALID_CHARS))


def validate_path_finished(string: str) -> None:
    u, d = VALID_CHARS
    if (string.count(d) - string.count(u)) != 0:
        raise ValueError(f'path {string} - wrong way!')


def check_path(path: str, funcs_tuple: tuple) -> None:
    try:
        for check_func in funcs_tuple:
            check_func(path)
    except (ValueError, TypeError) as e:
        raise type(e)(f'{TEXT_FOR_ERRORS}{e}')


def count_valleys_in_path(path: str) -> int:
    funcs_tuple = (check_valid_string_type, check_valid_path, validate_path_finished)
    check_path(path, funcs_tuple)

    average = result = 0

    for i, p in enumerate(path):
        average = average - 1 if p == 'd' else average + 1
        result += average < 0

    return result


VALID_CHARS = ('u', 'd')
TEXT_FOR_ERRORS = 'Invalid path: '
TEXT_RESULT = 'There were {} valleys on your way.'

if __name__ == '__main__':
    our_path = input('Enter path for count valleys: ').strip().lower()
    res = count_valleys_in_path(our_path)
    print(TEXT_RESULT.format(res))
