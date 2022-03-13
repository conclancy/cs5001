''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Midterm - Question 3
clancy.co@northeastern.edu (002781018)
11 MAR 22 

The file contains a function that finds the smallest value in a list
'''

import random


def find_smallest(list_of_numbers):
    '''
    find_smallest takes a list of numbers
    and returns the smallest value in the list
    :param list_of_numbers: A list of any numbers, of any size
    :return: the smallest value in list_of_numbers
    '''

    # function variables
    smallest = None 

    # logic to find the smallest number
    for number in list_of_numbers:
        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number

    return smallest


def test_find_smallest():
    '''
    Tests the find_smallest function to ensure that it is returning
    the smallest value in a list of random numbers. 

    :params None:
    :returns: prints a string of failures or a message that all tests passed
    '''

    # function vairables
    failed = 0 

    # run 1000 tests
    for i in list(range(1000)):

        # create loop variable
        test_list = []

        # create list with 1 to 10 random floats
        for j in list(range(random.randint(1, 10))):
            test_list.append(random.random() * 10)

        # get actual result from find_smallest function
        actual = find_smallest(test_list)

        # use build in soreted function to find smallest element
        test_list = sorted(test_list)
        expected = test_list[0]

        # compare our test results to the build in function and 
        # prints a string for a failed test
        if actual != expected:
            failed = failed + 1
            print("Failed -", actual, "does not equal", expected)

    # logic for if our tests all pass 
    if failed == 0:
        print("All tests passed")


test_find_smallest()
