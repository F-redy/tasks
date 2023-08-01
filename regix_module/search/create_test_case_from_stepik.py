import re
import sys


def get_input_text_lines() -> list[str]:
    print("-" * 158, '\nEnter the text:')
    # data_list = list(map(str.strip, sys.stdin.readlines()))
    return [line.strip() for line in sys.stdin.readlines() if line.strip()]


def extract_sample_data(data: list[str], marker: str) -> list[str]:
    """
    Extracts sample data from the list of strings based on the marker.

    :param data: A list of strings representing the text data.
    :param marker: A string marker to find the sample data section (e.g., "Input", "Output").
    :return: A list of strings containing the extracted sample data.
    """
    # sample_data = []
    # for i, line in enumerate(data_list):
    #     if re.search(fr"Sample {marker}.+", line):
    #         result = ''.join(data_list[i + 1:i + 2])
    #         sample_data.append(result)

    return [''.join(data[i + 1:i + 2]) for i, line in enumerate(data) if re.search(fr"Sample {marker}.+", line)]


def create_test_case() -> list[tuple[str, str]]:
    """
    Creates a test dataset from text - https://stepik.org/.

    :return: A list of tuples of strings representing the test case.
    """
    data = get_input_text_lines()
    input_data = extract_sample_data(data, "Input")
    output_data = extract_sample_data(data, "Output")

    return list(zip(input_data, output_data))


if __name__ == '__main__':
    result_test_case = create_test_case()
    print(result_test_case)
