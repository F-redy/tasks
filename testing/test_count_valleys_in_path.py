from unittest import TestCase

from raise_module.check_valleys_in_path import count_valleys_in_path


class TestCountValleysInPath(TestCase):
    def test_our_path_success(self):
        data = (('uudddu', 1), ('duuddu', 2), ('dduduu', 5), ('uududd', 0), ('', 0))
        for test, result in data:
            self.assertEqual(count_valleys_in_path(test), result)

    def test_value(self):
        data = ('123', '-1234', '20.1', '.!?')

        for path in data:
            self.assertRaises(ValueError, count_valleys_in_path, path)

    def test_type(self):
        data = (123, 17.3, -21, 0)

        for path in data:
            self.assertRaises(TypeError, count_valleys_in_path, path)
