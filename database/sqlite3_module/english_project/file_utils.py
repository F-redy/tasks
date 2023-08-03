import os


class FileHandler:
    def __init__(self, path_to_file: str):
        if self.is_file_exists(path_to_file):
            self.path_to_file = path_to_file

    @staticmethod
    def is_file_exists(path_to_file: str) -> bool:
        """
        Check if a file exists at the specified path.

        :param path_to_file: Path to the file.
        :return: bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(path_to_file)

    @staticmethod
    def _check_sep(string: str, separator: str) -> tuple[str, str]:
        """
       Check if a separator exists in the string and split it into two parts.

       :param string: The input string to check and split.
       :param separator: The separator to look for in the string.
       :return: tuple[str, str]: A tuple with two parts of the string (original and translate).

       If the separator is not found in the string, the function prompts the user to enter the correct string
       with the specified separator until a valid input is provided.
       The string is then split into two parts (original and translate) using the separator,
       and the resulting parts are returned as a tuple.
       """
        while separator not in string:
            string = input(f'in string {string}, no {separator}. Enter the correct string with a "{separator}":\n')
        try:
            original, translate = string.lower().strip().split(separator)
            return original, translate
        except ValueError:
            print(string)

    def get_words(self, separator: str) -> list[tuple[str, str]]:
        """
        Read words from a file and return them as a list of tuples.

        :param separator: The separator used to split the words.
        :return: ist of tuples with the words.
        """
        words = []

        with open(self.path_to_file, 'r', encoding='utf-8') as file:
            for pair in file:
                if pair:
                    original, translate = self._check_sep(pair, separator)
                    words.append((original, translate))
        if words:
            return words
        raise ValueError("No words were obtained from the file.")
