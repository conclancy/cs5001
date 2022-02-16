''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 4 - Problem 1 (Chessboard)
    clancy.co@northeastern.edu (002781018)
    15 FEB 22 

    This file generates a chessboard of alternating w and b
    based on a width and height int input from the user
'''


def character_selector(square, row_number): 
    '''
    function to determines which character to return
    params: two int square and row_number
    returns: string ("B" or "W")
    '''

    # Even row logic 
    if row_number % 2 == 0:
        # Even square 
        if square % 2 == 0:
            return("B")
        # Odd square
        else:
            return("W")
    # Odd row logic
    else: 
        # Even square 
        if square % 2 == 0:
            return("W")
        # Odd square
        else:
            return("B")


def row_generator(width, row_number):
    '''
    generates a row for our board
    params: two int square and row_number
    returns: string 
    '''

    # variables
    square = 1
    row = ""

    # Generates row one character at a time
    while square <= width:
        row += character_selector(square, row_number)
        square += 1 

    return(row)


def chessboard(width, height):
    '''
    chessboard function to compare  
    params: two int width and height
    returns: string
    '''

    # Create variables
    height_loop = 1
    board = ""

    # generates all rows except final row
    while height_loop <= height:
        row = row_generator(width, height_loop)
        height_loop += 1
        row += '\n'
        board += row

    return(board)


def main():

    '''
    test cases:
    t[0] = width of board
    t[1] = height of board
    t[2] = extected first character
    t[3] = extected last character
    t[4] = expected number of board squares
    t[5] = expected number of rows
    t[6] = expected test outcome
    '''
    test_cases = [
                  [8, 4, "B", "B", 32, 4, True],      
                  [8, 5, "B", "W", 40, 5, True],
                  [3, 3, "B", "B", 9, 3, True], 
                  [15, 8, "B", "W", 120, 8, True], 
                  [8, 4, "W", "B", 32, 4, False],
                  [8, 4, "B", "W", 32, 4, False],
                  [3, 3, "B", "B", 10, 3, False], 
                  [3, 3, "B", "B", 9, 5, False]]

    # variables
    expected_true = 0 
    expected_false = 0
    results_true = 0
    results_false = 0

    # run tests
    for t in test_cases:

        # increment counts
        if t[6] is True: 
            expected_true += 1
        else: 
            expected_false += 1

        # variables
        board = chessboard(t[0], t[1])
        results = []

        # test first square 
        results.append(board[0] == t[2])

        # test last square 
        results.append(board[-2] == t[3])

        # test square count
        black_squares = board.count('B')
        white_squares = board.count('W')
        total_squares = white_squares + black_squares

        results.append(total_squares == t[4])

        # test row count
        results.append(board.count('\n') == t[5])

        # transform results into a set 
        results = set(results)

        # logic to determine if at least 1 test failed
        if len(results) == 1 and True in results: 
            results_true += 1
        else: 
            results_false += 1

    # final logic deciding what to print
    if expected_true == results_true and expected_false == results_false:
        print("All of your tests passed!")
    else: 
        print("Not all tests passed.", results_true, "passed,", 
              results_false, "failed")


main()
