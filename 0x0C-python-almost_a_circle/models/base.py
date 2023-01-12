#!/usr/bin/python3
# Base class - Created by Daniel Seyi

''' Create a Base class '''

class Base:
    '''
        Represents the Base for all other classes in the project

        Attribute: __nb_objects = 0 # A private class attribute
    '''
    __nb_objects = 0


    ''' Initializing the class constructor '''

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

