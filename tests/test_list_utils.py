import unittest
from src.list_utils import unique_items, chunk_list


class TestListUtils(unittest.TestCase):
    def test_unique_items_keeps_order(self):
        self.assertEqual(unique_items([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_unique_items_empty(self):
        self.assertEqual(unique_items([]), [])

    def test_chunk_list_with_remainder(self):
        self.assertEqual(chunk_list([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_chunk_list_empty(self):
        self.assertEqual(chunk_list([], 3), [])

    def test_chunk_list_invalid_size(self):
        for size in (0, -1):
            with self.subTest(size=size), self.assertRaises(ValueError):
                chunk_list([1, 2, 3], size)


if __name__ == "__main__":
    unittest.main()
