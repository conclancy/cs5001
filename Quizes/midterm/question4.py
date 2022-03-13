''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Midterm - Question 4
clancy.co@northeastern.edu (002781018)
11 MAR 22 

The file contains a function that returns all multiples of three that are 
smaller than a given input number.
'''


def multiples_of_three(number):
    '''
    multiples_of_three takes in an int a generates and returns a list of all 
    the multiples of 3 that are less than or equal to the input value 

    :params int: a single integer to generate multiples of three until
    :returns: a list of integers that are multiples of 3 less than or equal
              to the input value. 
    '''

    # function variables
    multiples_list = [0]

    # generates list with multiples of 3 less or equal to input values 
    while multiples_list[-1] + 3 <= number:
        multiples_list.append(multiples_list[-1] + 3)

    return multiples_list


def main():

    # Test 1
    expected = [0, 3, 6, 9, 12]
    actual = multiples_of_three(14)
    if actual != expected:
        print("FAILED ")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)

    # Test 2
    expected = [0, 3, 6, 9, 12, 15]
    actual = multiples_of_three(15)
    if actual != expected:
        print("FAILED ")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)

    # Test 3
    expected = [0, 3, 6]
    actual = multiples_of_three(6)
    if actual != expected:
        print("FAILED ")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)

    # Test 4
    expected = [0, 3, 6]
    actual = multiples_of_three(7)
    if actual != expected:
        print("FAILED ")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)


if __name__ == "__main__":
    main()
