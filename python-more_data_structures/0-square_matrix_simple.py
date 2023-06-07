#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0] * len(row) for row in matrix]

    # Iterate over each element in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute the square of the value and store it in the corresponding position in the new matrix
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
