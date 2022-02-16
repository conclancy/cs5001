''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 4 - Problem 2 (fibonacci)
    clancy.co@northeastern.edu (002781018)
    15 FEB 22 

    This file determines if a number less than 10,000 is 
    part of the fibonacci sequence. 
'''


def is_fibonacci(number):
    '''
    determines if a number is in the fibonacci sequence
    params: one int number
    returns: bool
    '''

    # variables
    is_fibonacci = False
    current_number = 0
    previous_number = 0

    while current_number < 10000:

        # determine if current number is a fibonacci
        if number == current_number:
            is_fibonacci = True
            break

        # increment numbers 
        if current_number < 1:
            current_number +=1 
        else:
            next_number = current_number + previous_number
            previous_number = current_number
            current_number = next_number

    return(is_fibonacci)


def main():

    # test cases
    fibonacci = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                 233, 377, 610, 987, 1597, 2584, 4181, 6765]

    not_fibonacci = [-1, 6, 12, 22, 6000, 10946]

    # variables 
    failed_tests = 0

    # test fibonacci numbers
    for n in fibonacci:

        if not is_fibonacci(n):
            failed_tests += 1

    # test non-binonacci numbers 
    for n in not_fibonacci:

        if is_fibonacci(n):
            failed_tests += 1

    # prints test resutls
    if failed_tests == 0:
        print("All tests passed")
    else:
        print(failed_tests, "tests failed")


main()
