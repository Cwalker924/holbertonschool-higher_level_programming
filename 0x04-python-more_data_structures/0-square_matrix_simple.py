#!/usr/bin/python3
import math
def square_matrix_simple(matrix=[]):
    new_matrix = []
    [new_matrix.append(list(map(lambda x: x ** 2, row))) for row in matrix]
    return(new_matrix)
