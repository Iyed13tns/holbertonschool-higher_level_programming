#!/usr/bin/python3
"""
This module defines a class Student with methods to retrieve its dictionary
representation for JSON serialization.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves the dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation of the instance.
        """
        return self.__dict__
