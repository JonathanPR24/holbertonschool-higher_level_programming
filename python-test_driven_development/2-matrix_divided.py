#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a list of lists of integers
                       or floats.
        div (int or float): The divisor to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by the divisor, rounded to
              2 decimal places.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats
                   or if each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
