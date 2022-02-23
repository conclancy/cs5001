''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 5 - Problem 4 (Day of the Week)
    clancy.co@northeastern.edu (002781018)
    22 FEB 22 

    This file takes in an integer and returns the corresponding day of the week 
    Day 1 is Sunday, Day 2 is Monday, ..., Day 7 is Saturday
'''


def which_day(day_number):
    '''
    Takes the number 1 - 7 and returns the corresponding day of the week.
    Day 1 is Sunday, Day 2 is Monday, ..., Day 7 is Saturday
    params: single int
    returns: string
    '''

    # create variable
    day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday']

    # reutrn the string located at x-1 indice since the first day of the week
    # is "1" but the first indice in the list is "0"
    return day_list[day_number - 1]


def main():
    '''
    This main function tests the above which_day function to ensure
    the function is working as intended. 
    '''

    # create empty list to store test results
    test_results = []

    # run tests and record results.  All should equal True. 
    test_results.append(which_day(1) == "Sunday")
    test_results.append(which_day(2) == "Monday")
    test_results.append(which_day(3) == "Tuesday")
    test_results.append(which_day(4) == "Wednesday")
    test_results.append(which_day(5) == "Thursday")
    test_results.append(which_day(6) == "Friday")
    test_results.append(which_day(7) == "Saturday")
    test_results.append(which_day(7) != "Sunday")

    # create testing variables 
    i = 0 
    failed_tests = 0

    # iterate over test results looking for False (failed) values
    while i < len(test_results):

        # increment the failed test variable for each False in the list
        if not test_results[i]:
            failed_tests += 1

        # increment the iterator
        i += 1

    # alert the user if one or more tests failed; else notify them all passed
    if failed_tests > 0: 
        print(failed_tests, "tests failed :(")
    else:
        print("All tests passed! :)")


main()
