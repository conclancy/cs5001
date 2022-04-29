'''
CS5001.38359.202230 - SEC 05 - John Wilder
Final Examp - Recursion
clancy.co@northeastern.edu (002781018)
29 APR 22 

This file contains a recursive function of the originally provided function.

Instructions:
    1. Write a recursive version of list_of_strings_loop
    2. Write a useful comment for your function
'''


import random


def list_of_strings_loop(number_of_strings) -> list:
    '''
    list_of_strings_loop was provided by the instructor to show desired 
        functioanlity of the recursive function.
    params:
        number_of_strings - int number of strings for the function to return
    returns:
        list of strings
    '''

    # variables
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list_of_strings = []

    # loop logic
    for word in range(number_of_strings):
        string_length = random.randint(1, 5)
        this_word = ""
        for character in range(string_length):
            this_word += random.choice(alphabet)
        list_of_strings.append(this_word)

    # return
    return list_of_strings


def list_of_strings_recursive(number_of_strings) -> list:
    '''
    list_of_strings_recursive generates a list of random strings with a length
        between 1 and 5 characters based on input variables number_of_strings.
    params:
        number_of_strings - int number of strings for the function to return
    returns:
        list of strings
    '''

    # variables
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # check input value is an int
    if not isinstance(number_of_strings, int):
        raise TypeError("number_of_strings must be of type int")

    # recursive logic for list
    if number_of_strings == 1:
        list_of_strings = []
    else:
        number_of_strings -= 1
        list_of_strings = list_of_strings_recursive(number_of_strings)

    # generate the new word
    string_length = random.randint(1, 5)
    this_word = ""
    for character in range(string_length):
        this_word += random.choice(alphabet)
    list_of_strings.append(this_word)

    # return
    return list_of_strings


if __name__ == "__main__":
    print(list_of_strings_recursive(3))
