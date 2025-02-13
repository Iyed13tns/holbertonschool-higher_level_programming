#!/usr/bin/python3  # Spécifie l'interpréteur Python à utiliser

def read_file(filename=""):  
    """
    Fonction qui lit un fichier et affiche son contenu.
    
    :param filename: Nom du fichier à lire (par défaut, chaîne vide)
    """
    with open(filename, 'r', encoding = 'utf-8') as file:
         file.read()
         print(filename)
