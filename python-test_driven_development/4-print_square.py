#!/usr/bin/python3
"""
Module 4-print_square
Ce module contient une fonction pour afficher un carré de taille donnée.
"""

def print_square(size):
    """
    Affiche un carré de taille `size` avec le caractère `#`.

    Arguments :
    - size : un entier représentant la longueur du côté du carré.

    Exceptions :
    - TypeError : si `size` n'est pas un entier.
    - ValueError : si `size` est inférieur à 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)