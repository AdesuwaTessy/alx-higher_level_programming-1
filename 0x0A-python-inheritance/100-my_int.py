#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 21:03:37 2023
@author: Daniel Seyi
"""


class MyInt(int):
    """
    A class that inherits from int
    """
    def __eq__(self, num):
        """
        equal function for MyInt class
        Attributes:
            num (int): an inputed integer
        Returns:
            The opositive booleanof the input
        """
        return (int(self) != num)

    def __ne__(self, num):
        """
        no equal function for MyInt class
        Attributes:
            num (int): an inputed integer
        Returns:
            The opositive booleanof the input
        """
        return (int(self) == num)
