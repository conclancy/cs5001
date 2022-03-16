''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 7 - Question 2 (Multiples of 5 Again)
clancy.co@northeastern.edu (002781018)
16 MAR 22 

The file contains a function that takes in a single number and returns a list
with all of the multples of 5 less than or equal to that value
'''


import random


def test_count_by_fives_recursive(ending_value):
    '''
    test_count_by_fives_recursive is willtest the count_by_fives_recursive
    the expected outcome from the two functions should be the same.
    :params int: single int that will be the largest value in the list
    :return: a list of multiples of 5 between 0 than the input value
    '''

    # local vairables 
    result = []
    count = 0

    # generate list in increments of 5
    while count <= ending_value:
        result.append(count)
        count += 5

    # return results
    return result


def count_by_fives_recursive_two(input_value, ending_value):
    '''
    count_by_fives_recursive_two returns alls values between 0 and the input
    number in the form of a list.
    :params int: two inputs are both ints
    :return: a list of multiples of 5 between 0 than the input value
    '''

    # if the initial input value is negative, return an empty list
    if ending_value < 0:
        return []

    # if the input value is less than or equal to the ending value, add 5
    # to the input value and call the function again.  Then append the input
    # value to the returned list.
    if input_value <= ending_value:
        values_list = count_by_fives_recursive_two(input_value + 5, 
                                                   ending_value)
        values_list.append(input_value)
    else:
        values_list = []

    # return a list with multiples of 5 sorted
    return sorted(values_list)


if __name__ == "__main__":
    # test to ensure the function is working as expected
    for i in list(range(100)):

        # local variable in loop
        testing_value = random.randint(-100, 100)

        # test the generated value in expected and actual functions
        expected = test_count_by_fives_recursive(testing_value)
        actual = count_by_fives_recursive_two(0, testing_value)

        # print failed results
        if expected != actual:
            print(testing_value, "caused test to fail!")
            print(expected)
            print("\nDoes not equal\n")
            print(actual)
