import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_length(self):
        """Проверка если список пуст"""
        self.assertEqual(arrs.my_slice([], 0), [])

    def test_slice_start_is_none(self):
        "Проверка если старт с None"
        self.assertEqual(arrs.my_slice([1, 2, 3], None), [1, 2, 3])

    def test_slice_end_is_none(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, None), [1, 2, 3])