#!/usr/bin/python3
"""
Module 2-matrix_divided
Ce module contient une fonction pour diviser tous les éléments d'une matrice.
"""

def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur.

    Arguments :
    - matrix : une liste de listes contenant des entiers ou des flottants.
    - div : un nombre (entier ou flottant).

    Retourne :
    - Une nouvelle matrice où chaque élément est divisé par 'div' et arrondi à 2 décimales.

    Exceptions :
    - TypeError : Si la matrice ou le diviseur ne sont pas valides.
    - ZeroDivisionError : Si 'div' est égal à 0.
    """
    # Vérification de la matrice
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Vérification de la taille des lignes
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Vérification du diviseur
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Division des éléments
    return [[round(x / div, 2) for x in row] for row in matrix]
