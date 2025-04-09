#!/usr/bin/python3
"""
Module 5-text_indentation
Ce module contient une fonction pour afficher du texte avec des sauts de ligne spécifiques.
"""

def text_indentation(text):
    """
    Affiche un texte avec deux nouvelles lignes après chaque caractère `.` `?` ou `:`.

    Arguments :
    - text : Une chaîne de caractères contenant le texte à traiter.

    Exceptions :
    - TypeError : Si `text` n'est pas une chaîne de caractères.
    
    Règles :
    - Aucun espace au début ou à la fin de chaque ligne affichée.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    characters = ['.', '?', ':']
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
        i += 1

    # Nettoyer les espaces inutiles
    lines = [line.strip() for line in result.split("\n")]
    print("\n".join(lines))
