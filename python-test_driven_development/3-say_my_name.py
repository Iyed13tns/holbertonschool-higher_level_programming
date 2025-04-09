#!/usr/bin/python3
"""
Module 3-say_my_name
Ce module contient une fonction pour afficher un prénom et un nom.
"""

def say_my_name(first_name, last_name=""):
    """
    Affiche 'My name is <first_name> <last_name>'.
    
    Arguments :
    - first_name : chaîne de caractères représentant le prénom (obligatoire).
    - last_name : chaîne de caractères représentant le nom (optionnel, par défaut vide).
    
    Exceptions :
    - TypeError : si `first_name` ou `last_name` n'est pas une chaîne de caractères.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
