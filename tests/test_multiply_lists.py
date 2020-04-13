import unittest
from matrices_multiplier.multiplier import multiply_lists


class TestMultiplyLists(unittest.TestCase):

    def test_multiply_lists_with_positive_integers(self):
        input_data_list_1 = [5, 8, 4]
        input_data_list_2 = [5, 6, 4]
        expected_data = 89
        result = multiply_lists(input_data_list_1, input_data_list_2)
        self.assertEqual(result, expected_data)

    def test_multiply_lists_with_negative_integers(self):
        input_data_list_1 = [-5, -8, 4]
        input_data_list_2 = [-5, 6, -4]
        expected_data = -39
        result = multiply_lists(input_data_list_1, input_data_list_2)
        self.assertEqual(result, expected_data)

    def test_multiply_lists_with_0(self):
        input_data_list_1 = [2, 0, 0]
        input_data_list_2 = [2, 0, 1]
        expected_data = 4
        result = multiply_lists(input_data_list_1, input_data_list_2)
        self.assertEqual(result, expected_data)
