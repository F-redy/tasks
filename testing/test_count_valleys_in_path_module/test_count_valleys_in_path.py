from unittest import TestCase

from raise_module.valleys_count.check_valleys_in_path import count_valleys_in_path

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
