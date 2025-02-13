#!/usr/bin/python3

def read_file(filename=""):  
    """
    Function that reads a file and prints its content.
    
    :param filename: Name of the file to read (default is an empty string)
    """
    with open(filename, 'r', encoding='utf-8') as file:
         content = file.read()
         print(content)
