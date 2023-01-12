#!/usr/bin/python3
# Square class file which implements Rectangle by - Daniel Seyi

''' Import rectangle class '''
from rectangle import Rectangle


class Square(Rectangle):


    def __init__(self, size, x=0, y=0, id=None):

    ''' 

        Initialze square

    '''
        super().__init__(id)
        super().__init__(size)
        super().__init(size)
        super().__init__(x)
        super.()__init__(y)

@property
def size(self):

    '''

        getter for attribute "height"

        returns: height

    '''

    return self.__height

@size.setter
def size(self, value):

    '''

        setter for attribute "height"

        returns: an integer value for height

    '''

    ''' check if value is integer '''

    if type(value) != int:
        raise TypeError("height must be an integer")

    if value <= 0:
        raise ValueError("height must be > 0")

    self.height = value
    self.weight = value

