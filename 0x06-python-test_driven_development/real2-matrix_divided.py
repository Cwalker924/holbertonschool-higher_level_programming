#!/usr/bin/python3
"""
This module holds only one function:
matrix_divided()
"""

def matrix_divided(matrix, div):
    typeError = ["matrix must be a matrix (list of lists) of integers/floats",
                 "Each row of the matrix must have the same size",
                 "div must be a number", "division by zero", "matrix is empty"]

    new_matrix = []
    form = []
    for row in matrix:
        for num in row:
            form.append(round(num / div, 2))
        new_matrix.append(form)
    return(new_matrix)
