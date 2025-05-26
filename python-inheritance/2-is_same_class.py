#!/usr/bin/python3
def is_same_class(obj, a_class):
    
    class obj(a_class):
        pass
    type(obj) == a_class
    ruturn = True

    
