import unittest
import types
from generator_2 import flat_generator

class TestFlatGenerator(unittest.TestCase):
    """Тесты для flat_generator."""

    def test_flat_generator_with_simple_list(self):
        """Тест с простым списком списков."""
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual_result = list(flat_generator(list_of_lists))
        self.assertEqual(actual_result, expected_result)

    def test_flat_generator_with_nested_lists(self):
        """Тест с вложенными списками."""
        list_of_lists = [[1, 2, [3, 4]], [5, [6, [7, 8]]], 9]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual_result = list(flat_generator(list_of_lists))
        self.assertEqual(actual_result, expected_result)

    def test_flat_generator_with_empty_lists(self):
        """Тест с пустыми списками."""
        list_of_lists = [[], [], []]
        expected_result = []
        actual_result = list(flat_generator(list_of_lists))
        self.assertEqual(actual_result, expected_result)


if __name__ == 'main':
    unittest.main()