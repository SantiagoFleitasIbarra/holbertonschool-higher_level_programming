#!/usr/bin/python3
"""
this module returns the division
of a matrix by an integer or a float
"""


def matrix_divided(matrix, div):
    """this defines the new matrix"""

    if not all(isinstance(row, list) and all(isinstance(element, \
            (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
