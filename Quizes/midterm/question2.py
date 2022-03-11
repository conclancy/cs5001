''' CS5001.38359.202230 - SEC 05 - John Wilder
    Midterm - Question 2
    clancy.co@northeastern.edu (002781018)
    11 MAR 22 

    The file contains a function that finds the median in a list of values.
'''


def find_median(input_list):
    '''
    find_median takes a list of numbers as input
    and finds the median value in the list. The median value
    is defined as the value for which half the items are larger
    and half the items are smaller.

    :param input_list: A list of numbers
    :return: The median value of the list
    '''

    # function variables
    size = len(input_list)

    # sorted is a built-in function that will return a sorted list
    sorted_list = sorted(input_list)
    median = 0

    # find the median for even and odd list numbers
    if size % 2 != 0:
        median = sorted_list[int(size / 2)]
    else:
        elements = sorted_list[int((size + 1) / 2)] 
        elements = elements + sorted_list[int((size - 1) / 2)]
        median = 0.5 * (elements)

    return median


def main():

    # Test 1
    my_list = list(range(0, 6))
    expected = 2.5
    actual = find_median(my_list)
    if actual != expected:
        print("FAILED ")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)

    # Test 2
    my_list = list(range(0, 5))
    expected = 2
    actual = find_median(my_list)
    if actual != expected:
        print("FAILED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)


if __name__ == "__main__":
    main()
