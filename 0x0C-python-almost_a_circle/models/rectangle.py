#!/usr/bin/python3
# Rectangle class file written by - Daniel Seyi

'''Importing Base class from base file '''

from models.base import Base


class Rectangle(Base):

    '''
        A class "Rectangle" which inherits Base
        method: __init__()
    '''


def __init__(self, width, height, x=0, y=0, id=None)


'''
    Instance of the class Rectangle is initialized

'''

supper().__init__(id)
self.width = width
self.height = height
self.x = x
self.y = y


@property
def width(self):

    '''
        getter for attribute "width"

        returns: width

    '''
    return self.__width


@width.setter
def width(self, value):

    '''

        setter for attribute "Width"

        returns: int value for width

    '''

    ''' Check if the value type is an integer '''

    if type(value) != int:
        raise TypeError('width must be an integer')

    ''' Check if the value is greater than 0 '''

    if value <= 0:
        raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):

        '''

            getter for attribute "height"

            return: height

        '''
        return self.__height

    @height.setter
    def height(self, value):

        '''

            setter for attribute "height"

            returns: an integer value for height

        '''

        ''' check if the value type is an integer '''

        if type(value) != int:
            raise TypeError("height must be an integer")

        ''' Check if the value is greater than 0 '''

        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):

        '''

            getter for attribute "x"

            returns: x

        '''
        return self.__x

    @x.setter
    def x(self, value):

        '''

            setter for attribute "x"

            returns: an integer value for x

        '''

        ''' Check if the value type of x is an integer '''
        if type(value) != int:
            raise TypeError("x must be an integer")

        ''' check if the value of x is greater than or equal to 0 '''
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):

        '''

            getter for attribute "y"
            return: y

        '''
        return self.__y

    @y.setter
    def y(self, value):

        '''

            setter for attribute "y"

            returns: an integer value for y

        '''

        ''' check if the value of y is an integer '''
        if type(value) != int:
            raise TypeError("y must be an integer")

        ''' check if the value of y is greater than or equal to 0 '''
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):

        '''

            a method that returns the areaof a rectangle

        '''

        return (self.__width * self.width)

    def display(self):

        '''
            Prints the # char Rectangle
        '''

        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):

        '''

            overriding the __str__ method so that it return [Rectangle] (<id>)
            <x>/<y> - <width>/<height>

        '''

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):

        '''

            a method that assigns a key/value pair argument to each attribute:

            args:
                *arg - Non-keyword (positional) arguments
                **kwargs - keyword arguments

        '''

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.weight = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError
        pass
