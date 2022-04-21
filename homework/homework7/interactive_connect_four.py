''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 7 - Connect Four
clancy.co@northeastern.edu (002781018)
17 APR 22 

The file contains the a class used to interact with a connect four
gameboard object and drives the user interface for playing the game.
'''

from connect_four import ConnectFour

if __name__ == '__main__':
    '''driver function'''

    board = ConnectFour()

    while True:
        print('\n')
        print(board)

        if board.player_one:
            print("Player X's turn")
        else:
            print("Player O's turn")

        move = input("Which column would you like to play? ")

        if move == 'Q':
            break
        else:
            board.add_piece(int(move))

        if board.get_winner() is not None:
            print(board)
            print(board.get_winner())
            break

        board.next_player()
