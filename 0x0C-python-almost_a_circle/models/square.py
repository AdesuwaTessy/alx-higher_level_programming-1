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

    return self.__width

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

def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            Overloading str function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
