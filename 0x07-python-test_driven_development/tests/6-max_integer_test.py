import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_duplicate_elements(self):
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)

    def test_string_list(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

    def test_none_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
