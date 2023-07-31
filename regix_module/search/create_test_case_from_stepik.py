import re
import sys


def create_test_case() -> list[str]:
    """
    Creates a test dataset from text - https://stepik.org/.

    :return: A list of strings representing the test data set.
    """
    length_line = "-" * 158
    print(length_line, '\nEnter the text:')
    # text_stepik: list[str] = list(map(str.strip, sys.stdin.readlines()))
    text_stepik: list[str] = [line.strip() for line in sys.stdin.readlines() if line.strip()]

    test_case = []
    for i, line in enumerate(text_stepik):
        if re.search(r"Sample Input.+", line):
            test = text_stepik[i + 1]
            test_case.append(test)
            print(test)

    print(length_line, '\n', test_case)

    return test_case


if __name__ == '__main__':
    result_test_case = create_test_case()
