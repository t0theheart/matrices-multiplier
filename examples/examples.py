from matrices_multiplier import multiply_matrices

matrix_1 = [
    [5, 8, -4],
    [6, 9, -5],
    [4, 7, -3]
]

matrix_2 = [
    [3, 2, 5],
    [4, -1, 3],
    [9, 6, 5]
]

print(multiply_matrices(matrix_1, matrix_2))
# [
#   [11, -22, 29],
#   [9, -27, 32],
#   [13, -17, 26]
# ]


matrix_3 = [
    [-1, 2, 5],
    [3, 4, 6],
    [-8, 2, 12]
]

matrix_4 = [
    [-2, 2],
    [5, 7],
    [-1, 4]
]

print(multiply_matrices(matrix_3, matrix_4))
# [
#   [7, 32],
#   [8, 58],
#   [14, 46]
# ]
