#!/usr/bin/python3
#1-square.py - Daniel Seyi

'''  a class Square that defines a square. It also has a Private instance attribute: size and Instantiation with size (no type/value verification) '''


class Square:
    __size = None

''' Creating an instance with size '''
def __init__(self, size):
    '''Initializing the class Square, with argument of szie'''

    self.__size = size
