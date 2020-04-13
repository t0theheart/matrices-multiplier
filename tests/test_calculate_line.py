import unittest
from matrices_multiplier.multiplier import calculate_line


input_data_matrix_1 = [
    [5, 8, -4],
    [6, 9, -5],
    [4, 7, -3]
]

input_data_verticals_matrix_2 = [
    [3, -6, 1],
    [5, 9, 2],
    [-4, -1, 8]
]


class TestCalculateLine(unittest.TestCase):

    def test_calculate_line_1(self):
        expected_data = [-37, 89, -60]
        result = calculate_line(input_data_matrix_1, input_data_verticals_matrix_2, 0)
        self.assertEqual(result, expected_data)

    def test_calculate_line_2(self):
        expected_data = [-41, 101, -73]
        result = calculate_line(input_data_matrix_1, input_data_verticals_matrix_2, 1)
        self.assertEqual(result, expected_data)

    def test_calculate_line_3(self):
        expected_data = [-33, 77, -47]
        result = calculate_line(input_data_matrix_1, input_data_verticals_matrix_2, 2)
        self.assertEqual(result, expected_data)
