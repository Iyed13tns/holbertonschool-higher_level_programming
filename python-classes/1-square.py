#!/usr/bin/python3

# Définition de la classe Square
class Square:
    # Déclaration de l'attribut privé __size, qui n'est pas encore initialisé
    __size = None

    # Constructeur de la classe Square
    def __init__(self, size):
        # Initialisation de l'attribut __size avec la valeur fournie lors de la création de l'objet
        self.__size = size
