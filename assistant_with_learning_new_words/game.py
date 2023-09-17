from random import choice

COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'violet': '\033[35m',
    'light_blue': '\033[36m',
    'drop_color': '\033[0m'
}


class Game:
    """
   Класс для игры с изучением слов.

   Attributes:
       words (list[tuple[str, str]]): Список кортежей с парами слов, где каждый кортеж содержит
           оригинальное слово и его перевод.
       point (int): Начальное количество очков игрока.
       repeat (int): Количество повторений цикла игры.
       count_words (int): Количество слов в каждом круге игры.
       next_lvl_point (int): Количество очков, необходимых для получения новых слов.
       step (int): Количество раз, которое слова повторялись в круге.
       stage (int): Количество раз, которое уже прошли по словарю.

   Methods:
       paint(text: str, color: str) -> str:
           Метод для окрашивания текста в указанный цвет.

       italics(text: str) -> str:
           Метод для форматирования текста курсивом.

       print_message(result: str, origin: str, translate: str, point: int, color: str) -> None:
           Метод для вывода сообщения о результатах игры.

       read_words(words: dict) -> dict:
           Метод для чтения и оценки ввода пользователя для перевода слов,
           обновляет словарь слов после ввода.

       check_point(words: dict) -> dict:
           Метод для оценки очков, связанных с парами слов и их организации для дальнейших действий.

       get_new_pair() -> tuple[str, str]:
           Метод для получения новой пары слов случайным образом из списка доступных пар слов.

       delete_pair(pair: tuple) -> None:
           Метод для удаления пары слов из списка доступных пар слов.

       start_game() -> dict:
           Метод для начала игры и инициализации первоначальных слов.

    """

    def __init__(self, words: list[tuple[str, str]], point: int = 0, repeat: int = 6,
                 count_words: int = 5, next_lvl_point: int = 4, stage: int = 1):
        """
        Инициализирует объект класса Game с заданными параметрами.

        Args:
            words (list[tuple[str, str]]): Список кортежей с парами слов, где каждый кортеж содержит
                оригинальное слово и его перевод.
            point (int, optional): Начальное количество очков игрока. По умолчанию 0.
            repeat (int, optional): Количество повторений цикла игры. По умолчанию 6.
            count_words (int, optional): Количество слов в каждом круге игры. По умолчанию 5.
            next_lvl_point (int, optional): Количество очков, необходимых для получения новых слов.
                По умолчанию 4.
            stage (int, optional): Количество раз, которое уже прошли по словарю. По умолчанию 1.
        """
        self.some_words = words
        self.words_to_learn = dict()
        self.common_words = dict()
        self.point = point  # Начальное количество очков
        self.repeat = repeat  # Сколько раз повторить весь цикл
        self.starting_count_words = count_words  # Количество слов в каждом круге
        self.next_lvl_point = next_lvl_point  # Количество очков для получения новых слов
        self.step = 1  # Сколько раз повторялись слова на круге
        self.stage = stage  # Сколько раз уже прошли по словарю

    def __str__(self):
        return self.some_words

    @staticmethod
    def paint(text: str, color: str) -> str:
        """
        Функция красит входной текст в указанный цвет.

        Available colors:
        - 'green'     : Green color
        - 'red'       : Red color
        - 'yellow'    : Yellow color
        - 'blue'      : Blue color
        - 'violet'    : Violet color
        - 'light_blue': Light blue color

        :param text: Текст, который нужно раскрасить.
        :param color: Желаемый цвет текста.

        :return: Входной текст заключен в цветовые коды ANSI для указанного цвета.

        :raises ValueError: Если указан неподдерживаемый цвет.
        """
        try:
            return f"{COLORS[color]}{text}{COLORS['drop_color']}"
        except KeyError:
            raise ValueError(f'Нет цвета: {color}')

    @staticmethod
    def italics(text: str) -> str:
        """
        Функция применяет к входному тексту форматирование курсивом.

        :param text: Текст, который будет отформатирован курсивом.
        :return: Введенный текст с примененным форматированием курсива.
        """
        return f"\033[3m{text}\033[0m"

    @classmethod
    def print_message(cls, result: str, origin: str, translate: str, point: int, color: str) -> None:
        """
        Функция печатает текстовый результат с полученными данными.

        :param result: text: Right или Error
        :param origin: слово на изучаемом языке
        :param translate: перевод слова на родной язык
        :param point: доступное количество баллов
        :param color: цвет для текста
        :return: None
        """
        point = point + 1 if result.lower() == 'right' else point - 1

        print(f'{cls.paint(f"{result.title()}! ", color)}'
              f'{cls.italics(f"<< {origin} | {translate} >>")}'
              f'{cls.paint(f" has point: {point}", "green")}\n')

    def read_words(self, words: dict) -> dict:
        """
        Считывает и оценивает вводимые пользователем данные о переводе слов, обновляя словарь слов.

        :param words: Словарь, содержащий пары слов и связанные с ними значения баллов.
        :return: Обновленный словарь слов после обработки пользовательского ввода.
        """

        print(f'\n{" ":<60} '
              f'{self.paint(f"level: {self.stage}", "violet")}'
              f'{self.paint(f" | step: {self.step}", "violet")}\n')

        for (original, translation), point in words.items():
            text = self.paint("Enter translation for", "light_blue")
            question = input(f'{text} "{self.italics(translation)}": ').strip().lower()

            if question == original.strip().lower():
                words[(original, translation)] += 1
                self.print_message("Right", original, translation, point, 'green')
            else:
                self.print_message("Error", original, translation, point, 'red')
                words[(original, translation)] -= 1

        return words

    def check_point(self, words: dict) -> dict:
        """
        Оценивает балы, связанные с парами слов, и систематизирует их для дальнейших действий.

        :param words: Словарь, содержащий пары слов и связанные с ними значения баллов.
        :return: Словарь, содержащий пары слов и их значения в баллах, отфильтрованные на основе порогового
                            значения баллов. Возвращает None, если ни одна пара слов не должна повторяться.
        """

        go_repeat = {}

        for pair, point in words.items():
            if point < self.next_lvl_point:
                go_repeat[pair] = point
            else:
                self.common_words.update({pair: point})
        return go_repeat or None

    def get_new_pair(self) -> tuple[str, str]:
        """
        Извлекает новую пару слов, случайно выбранную из списка доступных пар слов.

        :return: Кортеж, содержащий новую пару слов, где первым элементом является исходное слово или фраза.
                    и второй элемент — это его перевод.
        """

        new_word = choice(self.some_words)
        print(f'{" ":>35}'
              f'{self.paint("new pair:", "yellow")}'
              f'{self.paint(" << ", "yellow")}'
              f'{self.paint(f"{self.italics(new_word[0]):<30}", "light_blue")}'
              f'{self.paint("|", "yellow"):<20}'
              f'{self.paint(f"{self.italics(new_word[1])}", "light_blue")}'
              f'{self.paint(" >>", "yellow")}')

        return new_word

    def delete_pair(self, pair: tuple) -> None:
        self.some_words.remove(pair)

    def start_game(self) -> dict:
        words = dict()
        for _ in range(self.starting_count_words):
            if self.some_words:
                p = self.get_new_pair()
                self.delete_pair(p)
                words[p] = self.point
        return words


if __name__ == "__main__":
    second_lesson = [('fault', 'вина'), ('get/receive', 'получать'), ('habit', 'привычка'),
                     ('disappointment', 'разочарование'), ('jar', 'банка'), ('candle', 'свечка'),
                     ('brush/comb', 'расческа'), ('hardly ever', 'почти никогда'), ('solve', 'решать(проблемы)'),
                     ('the same', 'совпадает с'), ('goods', 'продукты'), ('accept', '(принял, подтвердил)')]

    game = Game(second_lesson)
    game.words_to_learn = game.start_game()

    while game.stage < game.repeat:
        game.words_to_learn = game.read_words(game.words_to_learn)
        game.words_to_learn = game.check_point(game.words_to_learn)

        match game.words_to_learn:
            case None if game.some_words:
                game.step = 1
                game.words_to_learn = game.start_game()
            case None if not game.some_words:
                game.step = 1
                game.stage += 1
                game = Game(list(game.common_words), stage=game.stage)
                game.words_to_learn = game.start_game()
                game.common_words = {}
            case dict(d) if len(d) > 0:
                game.step += 1
                game.words_to_learn = game.read_words(game.words_to_learn)
            case _:
                print('Congratulation you are studied all words!')
                break
