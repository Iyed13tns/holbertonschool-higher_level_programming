#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
ssss
The function ensures that the matrix is a list of lists of integers or floats,
and that all rows are of the same size.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    s
    Returns a new matrix with elements rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
