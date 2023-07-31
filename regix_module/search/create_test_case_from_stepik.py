import re
import sys


def create_test_case(text: list[str]) -> list[str]:
    """
    Creates a test dataset from text - https://stepik.org/.

    :param text: List of lines of text containing test data.
    :return: A list of strings representing the test data set.
    """
    test_case = []
    for i, line in enumerate(text):
        if re.search(r"Sample Input.+", line):
            test_case.append(text[i + 2])
    return test_case


if __name__ == '__main__':
    print('Enter the text:')
    text_stepik = list(map(str.strip, sys.stdin.readlines()))
    print("-" * 154)
    result_test_case = create_test_case(text_stepik)
    for test in result_test_case:
        print(test)
    print("-" * 154)
    print(result_test_case)
