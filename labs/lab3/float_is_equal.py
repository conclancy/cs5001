''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 3 - Problem 1 (Comparing Floats)
    clancy.co@northeastern.edu (002781018)
    08 FEB 22 
'''
from math import fabs
from random import random

def float_is_equal(first_float, second_float, threshold):
    '''
    float_is_equal tests if two floats are equal within a threshold
    params: three floating point numbers
    returns: bool
    '''

    if fabs(first_float, second_float) < threshold:
        return True
    else:
        return False

def main():
    

main()