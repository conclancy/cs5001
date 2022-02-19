''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 4 - Problem 3 (diagonal numbers)
    clancy.co@northeastern.edu (002781018)
    17 FEB 22 

    This file takes in an integer and returns the number of lines 
    equal to that integer and iterates through to nothing
'''


def diagonal_number(lines):
    '''
    prints the number of lines input into the function and decrements by 1.
    params: one int number
    returns: str
    '''

    # variables
    line_string = "" 
    final_string = ""

    i = 1

    # first line generation
    while i <= lines:
        # print(len(line_string.replace(" ","")))
        line_string = line_string + str(i) + ' '
        i += 1

    # iterates over string reduce by one until final string created
    while len(line_string.replace(" ", "")) > 0:

        # Logic to ensure there is a space before the next line char
        if line_string[-1] == ' ':
            final_string = final_string + line_string + '\n'
        else: 
            final_string = final_string + line_string + ' \n'

        # removes empty spaces at the end of the line
        line_string = line_string.rstrip()

        # removes the last space and number from the string
        right_iterator = -1

        if len(line_string) > 1:

            # finds the next space starting from the end 
            while line_string[right_iterator] != ' ':
                right_iterator += -1

            # removes frinal number and string
            line_string = line_string[:right_iterator]
        else: 
            line_string = line_string[:-1]

    # return final string to caller
    return(final_string)


def main():

    # variables
    test_cases = [[3, '1 2 3 \n1 2 \n1 \n', True],
                  [2, '1 2 \n1 \n', True], 
                  [-1, '', True], 
                  [-1, ' \n', False], 
                  [3, '1 2 \n 1 \n', False]]

    passed_count = 0 
    failed_count = 0

    # test the test-cases     
    for t in test_cases:

        # print(diagonal_number(t[0]))

        if (diagonal_number(t[0]) == t[1]) is t[2]: 
            passed_count += 1
        else:
            print(diagonal_number(t[0]))
            failed_count += 1

    # return final resutls
    if failed_count == 0:
        print("All tests passed")
    else: 
        print(passed_count, 'tests passed, but', failed_count, 'failed')


main()
