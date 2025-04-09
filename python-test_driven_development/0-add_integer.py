#!/usr/bin/python3
"""
Module 0-add_integer
Ce module fournit une fonction pour ajouter deux entiers.
"""

def add_integer(a, b=98):
    """
    Ajoute deux nombres entiers.
    
    Arguments :
    a : Un entier ou un flottant, obligatoire.
    b : Un entier ou un flottant, optionnel, valeur par défaut 98.
    
    Retourne :
    La somme des deux entiers après conversion en entier.
    
    Exceptions :
    Lève une exception TypeError si les arguments ne sont pas de type valide.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
