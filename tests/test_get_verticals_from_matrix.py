import unittest
from matrices_multiplier.multiplier import get_verticals_from_matrix


class TestGetVerticalsFromMatrix(unittest.TestCase):

    def test_get_verticals_from_matrix_3_x_3(self):
        input_data = [
            [5, 8, -4],
            [6, 9, -5],
            [4, 7, -3]
        ]
        expected_data = [
            [5, 6, 4],
            [8, 9, 7],
            [-4, -5, -3]
        ]
        result = get_verticals_from_matrix(input_data)
        self.assertEqual(result, expected_data)

    def test_get_verticals_from_matrix_3_x_2(self):
        input_data = [
            [5, 8],
            [6, 9],
            [4, 7]
        ]
        expected_data = [
            [5, 6, 4],
            [8, 9, 7]
        ]
        result = get_verticals_from_matrix(input_data)
        self.assertEqual(result, expected_data)

    def test_get_verticals_from_matrix_2_x_3(self):
        input_data = [
            [5, 8, -4],
            [6, 9, -5],
        ]
        expected_data = [
            [5, 6],
            [8, 9],
            [-4, -5]
        ]
        result = get_verticals_from_matrix(input_data)
        self.assertEqual(result, expected_data)
