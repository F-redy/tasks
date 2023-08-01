import re


def test_regex(test_case: list[any], pattern: str, method: str, repl: str = None, flags: int = 0) -> None:
    """
    Tests a regular expression against a list of test cases.

    :param test_case: A list of test cases, where each test case is represented as a tuple containing an example string
     and the expected answer.
    :param pattern: The regular expression pattern to be tested.
    :param method: The name of the regular expression method to be used ('search', 'findall', 'finditer', etc.).
    :param repl: Optional. The name of the capturing group.
    :param flags: Optional. Flags that modify the behavior of the regular expression. Default is 0 (no flags).
    :return:This function does not return anything. It raises an AssertionError if any of the test cases fail.
    :raise:If the result of the regular expression does not match the expected answer for any of the test cases.
    """
    for i, (test, answer) in enumerate(test_case, 1):
        regex_method = getattr(re, method)
        if repl:
            result = regex_method(pattern, repl, test, flags=flags)
        else:
            result = regex_method(pattern, test, flags=flags)
        assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}\nError in {test}'
        print(f'TEST №{i} - OK!\n{result}')
