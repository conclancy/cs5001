''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 7 - Question 2 (Multiples of 5 Again)
clancy.co@northeastern.edu (002781018)
16 MAR 22 

The file contains a function that filters a list what to only show numbers
above a given threshold.
'''

import random


def filter_list(input_list, threshold):
    '''
    filter_list takes in a list of numbers and a threshold and returns the
    numbers in the list that are less than the threshold.
    :params: a list and an int. 
    :return: a list of numbers less than the threshold
    '''

    # if the input_list variable is null, return a blank list
    if not input_list:
        return []

    # if the first element in the list is above the threshold, send all
    # other elements back into filter_list function and append the value
    # to the returned list. 
    if input_list[0] > threshold:
        value_list = filter_list(input_list[1:], threshold)
        value_list.append(input_list[0])
        return sorted(value_list)

    # else just pass all of the elements back into the function to continue
    else:
        value_list = filter_list(input_list[1:], threshold)
        return sorted(value_list)


if __name__ == "__main__":

    # function vairables
    failed = 0 

    # run 1000 tests
    for i in list(range(10)):

        # create loop variable
        test_list = []

        # create list with 1 to 10 random floats
        for j in list(range(random.randint(1, 10))):
            test_list.append(random.randint(-100, 100))

        print(sorted(test_list))

        # get actual result from find_smallest function
        threshold = random.randint(-100, 100)
        actual = filter_list(test_list, threshold)

        # use build in soreted function to find smallest element
        tmp_list = [i for i in test_list if i > threshold]
        expected = sorted(tmp_list)

        # compare our test results to the build in function and 
        # prints a string for a failed test
        if actual != expected:
            failed = failed + 1
            print("threshold:", threshold)
            print("Failed -", actual, "does not equal", expected)

    # logic for if our tests all pass 
    if failed == 0:
        print("All tests passed")
