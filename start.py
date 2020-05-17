from matrices_multiplier.multiplier import multiply_matrices

if __name__ == '__main__':
    result = multiply_matrices(
        matrix_1=[
            [5, 8, -4],
            [6, 9, -5],
            [4, 7, -3]
        ],
        matrix_2=[
            [3, 2, 5],
            [4, -1, 3],
            [9, 6, 5]
        ]

    )

    print(result)
