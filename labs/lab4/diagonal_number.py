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

    # first line generation
    while len(line_string) < lines:
        line_string = line_string + str(len(line_string)+1)

    # iterates over string reduce by one until final string created
    while len(line_string) > 0:
        final_string = final_string + line_string + '\n'
        # print(line_string)
        line_string = line_string[:-1]

    # ensure the string always ends with a \n 
    final_string = final_string + '\n'

    # printing; this will need to be moved main()
    print(final_string)


diagonal_number(-1)