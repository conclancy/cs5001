''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 3 - Problem 1 (Comparing Floats)
    clancy.co@northeastern.edu (002781018)
    08 FEB 22 
'''
from math import fabs


def float_is_equal(first_float, second_float, threshold):
    '''
    float_is_equal tests if two floats are equal within a threshold
    params: three floating point numbers
    returns: bool
    '''

    if fabs(first_float - second_float) < threshold:
        return True
    else:
        return False


def main():

    # instantiate variables 
    test_passed = 0
    test_failed = 0 

    test_cases = [[1.01, 1.01, True], [3.123456, 3.123456, True], 
                  [2.329, 2.328, False], [2.0, 2.01, False]]

    # test the test cases 
    for t in test_cases:
        if float_is_equal(t[0], t[1], .000001) == t[2]:
            test_passed += 1
        else:
            test_failed += 1

    # return final results
    if test_passed == len(test_cases):
        print("All test passed!")
    else:
        print(test_passed, "tests passed, but", test_failed, "failed :(")


main()
