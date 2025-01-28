#!/usr/bin/python3
  """
  Definition of the Square class
  """
class Square:
    """
     Declaration of the private attribute __size, which is not yet initialized
    """   
    __size = None
      """
      Constructor of the Square class
      """   
    def __init__(self, size):
          """
          Initializing the __size attribute with the value provided during object creation
          """
        self.__size = size
