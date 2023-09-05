#!/usr/bin/python3
"""Defines divides"""


def matrix_divided(matrix, div):
    """Divides
    Args:
        matrix: list
        div: number

    Raises:
        TypeError: not a list of integers or floats
                    row isn't same size
                    element not an integer or float
                    row is not a list
                    div is not an integer or a float
        ZeroDivisionError: equal 0
    Returns:
        matrix: list
    """
    row_size = None
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(message)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(message)

        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
