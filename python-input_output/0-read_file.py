#!/usr/bin/python3

def read_file(filename=""):  
    """
    Fonction qui lit un fichier et affiche son contenu.
    
    :param filename: Nom du fichier à lire (par défaut, chaîne vide)
    """
    with open(filename, 'r', encoding='utf-8') as file:
         content = file.read()
         print(content)
