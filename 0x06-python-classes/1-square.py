#!/usr/bin/python3
# 1-square.py - Daniel Seyi

'''  a class Square that defines a square. It also has a Private instance
attribute: size and Instantiation with size (no type/value verification) '''


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initializing this square class
        Args: size - represnets the size of the square defined
        """

        self.__size = size
