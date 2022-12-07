#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    adds all unique elements of a list of integers
    """
    num = 0

    for i in set(my_list):
        num += i
    return num
