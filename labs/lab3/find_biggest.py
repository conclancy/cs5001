''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 3 - Problem 3 (Functions that call other functions)
    clancy.co@northeastern.edu (002781018)
    10 FEB 22 
'''


def biggest(first, second): 
    '''
    compares two numbers and returns the larger of the two 
    params: two int
    returns: int
    '''

    # Comparison logic
    if first >= second:
        return first
    else:
        return second


def biggest_of_four(first, second, third, fourth):
    '''
    compares four numbers and returns the largest 
    params: four float
    returns: float
    '''

    # intial evaluations
    largest_first_second = biggest(first, second)
    largest_third_fourth = biggest(third, fourth)

    # final evaluation 
    return(biggest(largest_first_second, largest_third_fourth))


def main():

    # Instantiate Variables 
    passed_tests = 0
    failed_tests = 0

    # Test Cases 
    # t[0:3] = test digits 
    # t[4]   = expected value
    # t[5]   = expected evaluation
    test_cases = [
        [1, 2, 3, 4, 4, True],              # Standard
        [-1, 0, 1, 2, 2, True],             # Test negative numbers 
        [4, 3, 8, 0, 8, True],              # Test for order 
        [-1, -2, -3, -4, -1, True],         # Test all negatives
        [1, 2, 3, 4, 1, False],             # Test failure works 
        [-1, -2, -3, -4, -4, False]         # Test failure works
    ]

    # Test functions 
    for t in test_cases: 
        if t[5] is True: 
            if biggest_of_four(t[0], t[1], t[2], t[3]) == t[4]: 
                passed_tests += 1
            else: 
                failed_tests += 1
        elif t[5] is False: 
            if biggest_of_four(t[0], t[1], t[2], t[3]) != t[4]: 
                passed_tests += 1
            else: 
                failed_tests += 1

    if failed_tests == 0: 
        print("All tests pass!")
    else:
        print(passed_tests, "tests passed, but", 
              failed_tests, "failed :(")


main()
