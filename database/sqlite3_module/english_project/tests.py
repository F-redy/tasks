from ValidationHelper import ValidationHelper


def test_func(func: callable, test_case: list[tuple]) -> None:
    print(f'TEST FOR {func.__name__}')
    for i, (test, answer) in enumerate(test_case, 1):
        result = func(test)
        assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nERROR in:\n {test}'
        print(f'TEST №{i} - OK')
    print()


test_case_username = [
    ('fredy', True), ('XAM', True), ('1fredy', True), ('_fredy', False), ('!fredy', False), (' !fredy', False),
    ('@!fredy', False), ('fredy1', True), ('fredyA', True), ('FredyA', True), ('Fredy1', True),
    ('Fredy_', False), ('HR', False), ('12345678901234567890123456789012', True),
    ('12345678901234567890123456789012a', False),
]

test_case_password = [('dgah2_dd2g', False), ('JVApa8In', True), ('k7dzbb2d', False), ('pi44', False),
                      ('ddddddd4ddddAs', True), ('iWlGgUnc', False), ('ن', False), ('3123123_123_13131', False),
                      ('____41__', False), ('BOJ8gZai', True), ('sHI4gqR3', True), ('22222', False),
                      ('الأح2Äа5مر', True), ('Wt8bAP5C', True), ('أل42Čö263ف', True), ('dasda_adsadad', False),
                      ('JmL5Lxbw', True), ('_______', False), ('f4aD2g', False), ('بadFa3ав', True),
                      ('qOUO1SRG', True), ('V86kqrWh', True), ('O12CDrxB', True), ('____f______', False),
                      ('dddddddd4ddddas', False), ('الحH3ёدث', True), ('söxöÖ42k', True),
                      ]

if __name__ == '__main__':
    h = ValidationHelper()
    test_func(h.is_valid_username, test_case_username)
    test_func(h.is_valid_entered_password, test_case_password)
