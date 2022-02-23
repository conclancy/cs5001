''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 5 - Problem 3 (Palindrome)
    clancy.co@northeastern.edu (002781018)
    22 FEB 22 

    This file takes checks whether or not an input string is a palindrome 
'''


def is_palindrome(phrase):
    '''
    test if the input string is a palindrome (i.e. same forwards and backwards)
    params: single string
    returns: booleon
    '''

    # ensure the case of the word is consistent
    phrase = phrase.lower()

    # create variables
    start_index = 0
    end_index = len(phrase) - 1
    is_palindrome = True

    # test if the first and last letter are equal.  If not, we can fail 
    # the whole test because the word is not a palindrome. 
    if phrase[start_index] == phrase[end_index]:

        # increment indicies that just passed above test
        start_index += 1
        end_index -= 1

        # iterate over remaining indicies sequentially
        while start_index < end_index:

            # ensure sequential characters match and incement/decrement
            # if any set of characters do not match, set the is_palindrome
            # variable to false and break the while loop.
            if phrase[start_index] == phrase[end_index]:
                start_index += 1
                end_index -= 1
            else:
                is_palindrome = False
                break
    else: 
        is_palindrome = False

    # return true or false depending on the outcomes of above logic
    return is_palindrome


def main():
    '''
    function to test the logic and ensure it is working as expected
    '''

    # variables
    i = 0 
    test_failed = 0 
    expected_failed = 0

    '''
    t[0] = phrase
    t[1] = expected palindrom?
    '''
    test_cases = [['noon', True],
                  ['racecar', True],
                  ['1991', True],
                  ['22022022', True],
                  ['tacocat', True],
                  ['WasitacaroracatIsaw', True],
                  ['^_^', True],
                  ['Connor', False],
                  ['CS5001', False], 
                  ['racecars', False]]

    # iterate over every value in the list
    while i < len(test_cases):

        # run funtion to test palindromeness
        palindrom_test = is_palindrome(test_cases[i][0])

        # increment expected failure variable if we expected a failed result
        if not test_cases[i][1]:
            expected_failed += 1

        # incremented actual failure if the function returned a failure
        if not palindrom_test:
            test_failed += 1

        # increment incidice 
        i += 1

    # print final test results with expected and actual failures 
    if expected_failed == test_failed:
        print("All tests passed with expected values (^_^)")
    else:
        print(test_failed, "tests failed; however, we expected",
              expected_failed, "to fail! (^_-)")


main()
