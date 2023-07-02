import re


def test_regex(test_case: list[tuple[str, str]], regex: str) -> None:
    """
    Tests a regular expression against a list of test cases.

    :param test_case: A list of test cases, where each test case is represented as a tuple containing an example string
     and the expected answer.
    :param regex: The regular expression pattern to be tested.
    :return:This function does not return anything. It raises an AssertionError if any of the test cases fail.
    :raise:If the result of the regular expression does not match the expected answer for any of the test cases.
    """
    for i, (example, answer) in enumerate(test_case, 1):
        result = ' '.join(re.findall(regex, example))
        assert result == answer, f'TEST №{i} - ERROR!\n{result} != {answer}'
        print(f'TEST №{i} - OK!')
