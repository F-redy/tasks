from typing import IO, Generator


def find_word_indexes(file: IO[str], word: str) -> Generator[int, None, None]:
    """
        Возвращает генератор индексов всех вхождений слова `word` в файле `file`.

    :param file: файловый дескриптор, представляющий открытый файл.
    :param word: искомое слово.
    :raises ValueError: если переданный аргумент `word` является пустой строкой.
    :yield: последовательность индексов всех вхождений `word` в файле
    """
    if not word:
        raise ValueError("Word cannot be empty")

    global_index = 0
    for line in file:
        local_index = 0
        while local_index != -1:
            local_index = line.find(word, local_index)
            if local_index > -1:
                yield global_index + local_index
                local_index += 1
        global_index += len(line)


search_word = input()  # искомое слово
path_file = input()  # полный или относительный путь к файлу в котором будем искать
try:
    with open(path_file, encoding="utf-8") as file_txt:
        word_indexes = find_word_indexes(file_txt, search_word)
        print(list(word_indexes))
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print(f"Ошибка обработки файла: {e}")
