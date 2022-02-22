''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 5 - Problem 1 (Average Grade)
    clancy.co@northeastern.edu (002781018)
    22 FEB 22 

    This file determines if a number less than 10,000 is 
    part of the fibonacci sequence. 
'''


import random


def average_grade(grade_list):
    '''
    calculates the average of a list of numbers
    params: list of floats
    returns: float
    '''

    i = 0
    list_total = 0.0

    while i <= len(grade_list) - 1:
        list_total += grade_list[i]

        i += 1

    return list_total / i


def main():
    '''
    main function for testing average_grade function
    '''

    # create main function variables
    tests_passed = 0
    tests_failed = 0
    grade_lists_tested = 0

    while grade_lists_tested < 5:

        # create loop variables 
        i = 0
        test_grades = []
        number_of_grades = random.randrange(5, 50)

        print("Testing a list of", number_of_grades, "grades")

        # create a list of 5 random integers
        while i < number_of_grades: 

            test_grades.append(random.random() * 100)

            i += 1

        # calulate and generate average
        test_average = sum(test_grades) / len(test_grades) 
        grade_average = average_grade(test_grades)

        # Logic for passing and failing tests
        if test_average == grade_average:
            tests_passed += 1 
            print("List of", number_of_grades, "passed with avg of", 
                  grade_average)
        else:
            tests_failed += 1
            print("Test Average", test_average, "does not equal",
                  grade_average, "calculated grade average")

        # increment test count variable by one
        grade_lists_tested += 1

    # print final test outcomes
    if tests_failed == 0: 
        print("All tests passed")
    else: 
        print(tests_passed, "tests passed but,", tests_failed, "failed")


main()
