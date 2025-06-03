#!/usr/bin/python3
'''
This module defines an empty class BaseGeometry
'''


class BaseGeometry:
    '''
    f
    '''
    def area(self):
        '''
        h
        '''
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        f
        """
        if not isinstance(value, int):
           raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
           raise ValueError(f"{name} must be greater than 0")

test = BaseGeometry;

test.area()