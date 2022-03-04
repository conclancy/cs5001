''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 6 - Problem 2 (Number Greater Than)
    clancy.co@northeastern.edu (002781018)
    3 MAR 22 

    This file contains a function that takes in two lists and determines which
    of the items in the first list are larger than the corresponding values in
    the second list.
'''


def number_greater_than(list1, list2):
    '''
    Takes in two lists of the same length and determines if the coresponding
    values are larger in the first list than the second list. 

    params: two equal sized lists
    returns: int of how many numbers in the first list are larger than second
    '''

    # create varialbe for storing bigger number count
    bigger = 0

    # iterate through each element of the list
    for i in range(len(list1)):

        # if the element in the first list is larger, increment bigger variable
        if list1[i] > list2[i]: 
            bigger += 1

    return bigger


def main():
    '''
    Function to test the above number_greater_than function
    '''

    # create variables
    tests_passed = 0
    tests_failed = 0

    '''
    t[0] = expected larger than number, 
    t[1] = list 1 
    t[2] = list 2 
    '''
    test_list = [
                 [1, [8.52, 5.04, 0.82, 4, 2.3], [4.1, 5.2, 5.74, 6.42, 2.7]],
                 [1, [2.18, 0.14], [1.23, 3.17]],
                 [2, [2.57, 0.1, 5.72, 8, 9.31], [3.72, 4.9, 9.67, 5.1, 4.93]],
                 [2, [3.14, 4.57, 6.84], [8.6, 0.36, 5.11]],
                 [3, [-1.01, 0, 10], [-2, -1, 0]]]

    # perform each test
    for t in test_list:

        # test each case and increment corresponding pass/fail variables
        if t[0] == number_greater_than(t[1], t[2]):
            tests_passed += 1
        else:
            tests_failed += 1

    # return final results
    if tests_passed != len(test_list):
        print("Tests failed", tests_failed, "and tests passed", tests_passed)
    else:
        print("All tests passed!")


main()
