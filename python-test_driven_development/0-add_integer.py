#!/usr/bin/python3
"""
Module 0-add_integer
Ce module fournit une fonction pour additionner deux entiers.
"""

def add_integer(a, b=98):
    """
    Ajoute deux nombres entiers ou flottants.
    Arguments :
    - a : Un entier ou flottant (obligatoire)
    - b : Un entier ou flottant (par défaut 98)
    
    Retourne :
    - La somme de `a` et `b` en tant qu'entiers.
    
    Exceptions :
    - Lève une exception TypeError si `a` ou `b` ne sont pas valides.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)