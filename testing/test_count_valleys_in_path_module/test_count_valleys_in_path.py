from unittest import TestCase

from raise_module.valleys_count.check_valleys_in_path import count_valleys_in_path, get_valley_count_message

DATA_PATH = r'data_path.txt'


class TestCountValleysInPath(TestCase):

    def test_our_path_success(self):
        with open(DATA_PATH) as test_file:
            for test in test_file:
                length, path, result = test.split()
            self.assertEqual(count_valleys_in_path(int(length), path), int(result))

    def test_value(self):
        data = ((3, '123'), (4, '-1234'), (1, '20.1'), (3, '.!?'))

        for path in data:
            self.assertRaises(ValueError, count_valleys_in_path, *path)

    def test_type(self):
        data = ((3, 123), (1, 17.3), (1, -21), (1, 0))

        for path in data:
            self.assertRaises(TypeError, count_valleys_in_path, *path)


class TestGetValleyCountMessage(TestCase):
    def test_out_text(self):
        data = (
            'On your way there was {} valley.',
            'On your way there were {} valleys.',
            'There were {} valleys on your way.',
        )
        self.assertEqual(get_valley_count_message(0), data[2].format(0))
        self.assertEqual(get_valley_count_message(1), data[0].format(1))
        self.assertEqual(get_valley_count_message(2), data[1].format(2))
        self.assertEqual(get_valley_count_message(3), data[1].format(3))

        for i in range(4, 10000):
            self.assertEqual(get_valley_count_message(i), data[2].format(i))
