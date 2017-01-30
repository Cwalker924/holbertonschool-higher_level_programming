#!/usr/bin/python3
"""
This module holds only one function:
matrix_divided()
"""


def matrix_divided(matrix, div):
    typeError = ["matrix must be a matrix (list of lists) of integers/floats",
                 "Each row of the matrix must have the same size",
                 "div must be a number", "division by zero", "matrix is empty"]

    if div == 0:
        raise ZeroDivisionError(typeError[3])
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError(typeError[2])

    if matrix == []:
        raise TypeError(typeError[0])
    for row in matrix:
        if row == []:
            raise TypeError(typeError[0])
        if len(row) != len(matrix[0]):
            raise TypeError(typeError[1])
        for n in row:
            if isinstance(n, int) is False and isinstance(n, float) is False:
                raise TypeError(typeError[0])

    new_matrix = []
    for row in matrix:
        form = []
        for n in row:
            form.append(round(n / div, 2))
        new_matrix.append(form)
    return(new_matrix)
