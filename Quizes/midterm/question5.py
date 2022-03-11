''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Midterm - Question 5
clancy.co@northeastern.edu (002781018)
11 MAR 22 

The file contains a function that returns all multiples of three that are 
smaller than a given input number.
'''


import random 


def flowchart_function(input_list):
    '''
    flowchart_function takes in a list and returns each element on a row 
    repeated the number of times equivalent to the row number.
    :params list: a list of elements 
    :returns: a multi-line string, one row for each element in input
    '''

    # function variables
    n = 0
    output_string = ""

    # loops for constructing multiline string
    while n < len(input_list):

        # ensure the element is a string
        element = str(input_list[n])

        # increment the counter
        n = n + 1

        # generate the row string
        loop_string = (element * n) + "\n" 

        # append the row to the main return string
        output_string = output_string + loop_string

    return(output_string)


def main():

    # test variables 
    failed = 0

    # test 1
    actual = flowchart_function(["c", "o", "n", "n", "o", "r"])
    expected = "c\noo\nnnn\nnnnn\nooooo\nrrrrrr\n"

    if actual != expected:
        failed = failed + 1
        print("Failed -", actual, "does not equal", expected)

    # run 1000 automated tests
    for i in list(range(1000)):

        # create loop variable
        test_list = []
        auto_exptected = ""
        iteration = 0

        # create list with 1 to 10 random floats
        for j in list(range(random.randint(1, 10))):
            test_list.append(random.randint(0, 9))

        # get actual result from find_smallest function
        actual = flowchart_function(test_list)

        # expected using a for loop
        for element in test_list:
            iteration = iteration + 1
            auto_exptected = auto_exptected + (
                             str(element) * iteration) + "\n"

        # logic for a failed test
        if actual != auto_exptected:
            failed = failed + 1
            print("Failed -", actual, "does not equal", expected)

    # logic for if our tests all pass 
    if failed == 0:
        print("All tests passed")


main()
