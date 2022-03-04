''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 6 - Problem 3 (Add Evens)
    clancy.co@northeastern.edu (002781018)
    3 MAR 22 

    Contains a function that takes in a lists and sums the even elements
'''


def add_evens(number_list):
    '''
    Takes in a list of numbers and sums the even elements 

    params: list of ints
    returns: int
    '''

    # create variable to store even number sum
    even_sum = 0

    # iterate through each number in list and add to sum if even
    for n in number_list:

        if n % 2 == 0:
            even_sum += n 

    return even_sum


def main():
    '''
    Function to test the above number_greater_than function
    '''

    # create variables
    tests_passed = 0
    tests_failed = 0

    test_cases = [[6, [1, 2, 3, 4]],
                  [14, [1, 2, 3, 4, 8]], 
                  [22, [10, 8, 4]], 
                  [0, [1, 3, 5]]]

    for t in test_cases:

        # test each case and increment corresponding pass/fail variables
        if t[0] == add_evens(t[1]):
            tests_passed += 1
        else:
            tests_failed += 1

    # return final results
    if tests_passed != len(test_cases):
        print("Tests failed", tests_failed, "and tests passed", tests_passed)
    else:
        print("All tests passed!")


main()
