''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 7 - Connect Four
clancy.co@northeastern.edu (002781018)
17 APR 22 

The file contains the connect_four class used to create and update
a connect four board.
'''

from queue import Queue
from stack import Stack

class ConnectFour:
    '''This class creates a gameboard for playing connect four'''

    def __init__(self):
        '''constructor for the ConnectFour class'''
        self.rows = 6
        self.columns = 7
        self.player_one = True
        self.board = Stack()
        self.hold_board = Stack()

        # create 6 rows with 7 columns of spaces
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                if c == 0: 
                    # todo
                    row.append(str(r))
                    # row.append(' ')
                else:
                    row.append(' ')

            # enqueue the row to the board
            self.board.push(row)

    def add_piece(self, column) -> None:
        '''
        add_piece allows the user to add their piece to a given column
        params:
            self -- the current object
            column -- int value for the column to drop the piece
        returns:
            void
        '''

        # ensure valid input and set the piece type
        if isinstance(column, int):
            if column > 0 and column <= self.columns:
                if self.player_one:
                    piece = 'X'
                else:
                    piece = 'O'
                
                # decrement the column by one so it can be used to index lists
                column = column - 1 

            else: 
                c = self.columns + 1
                err = "column must be greater than 0 and less than " + str(c)
                raise ValueError(err)
        else: 
            raise TypeError("column must be of type int")

        # logic for placing the piece 
        for r in range(self.rows + 1):
            print(r)

            # logic for first row; you need at least two rows to run process
            if r == 0:
                first_row = self.board.pop()
                print("first row is number:", first_row[0])
                self.hold_board.push(first_row)
                

            # logic for the bottom row of the board

            elif r == self.rows:
                print("trigger 2nd last logic")
                below_row = self.hold_board.pop()
                above_row = self.hold_board.pop() 

                print("above row is:", above_row[0], "below row is:", below_row[0])
                print("above column value:", above_row[column], "below column is:", below_row[column])

                # logic for landing a piece above another piece
                if below_row[column] == ' ':
                    below_row[column] = piece
                else:
                    above_row[column] = piece

                self.hold_board.push(above_row)
                self.hold_board.push(below_row)

            # logic for all rows except the bottom row
            # if the row below is already filled, and the above row is not
            # filled, set the above row to the current piece. 

            #todo: this logic does not appear to be working right now
            # We never get above = 1 and below = 0 
            else:
                above_row = self.hold_board.pop() 
                below_row = self.board.pop()

                print("above row is:", above_row[0], "below row is:", below_row[0])
                print("above column value:", above_row[column], "below column is:", below_row[column])


                # logic for landing a piece above another piece
                if below_row[column] != ' ' and above_row[column] == ' ':
                    print("trigger logic")
                    above_row[column] = piece

                # push both of the rows to the holding board
                self.hold_board.push(above_row)
                self.hold_board.push(below_row)

        # transfer the hold board back to main board stack
        self.transfer_hold_to_board()
    
    def is_game_over(self) -> bool:
        '''
        returns true when a player connects four pieces in any direction
        params:
            self -- the current object
        returns:
            bool -- true when the game is over, otherwise false
        '''
        #todo

    def get_winner(self) -> str:
        '''
        returns the name of the player who wins the game
        params:
            self -- the current object
        returns
            str -- the name of the player who won
        '''
        #todo

    def __str__(self) -> str:
        '''
        returns the game board as a string; each players pieces are shown
        blank cells will not contain marks for either player
        params:
            self -- the current object
        returns
            str -- multiline string showing the board
        '''

        # create a variable to hold the board string
        visual = ''

        # iterate through each row in the board
        for r in range(self.rows):

            # dequeue the row from the board
            row = self.board.pop()

            # instantiate the row string
            row_str = ''

            # for each column in the row, add a pipe character and the 
            # board character (' ', 'X', or 'O')
            for c in row:
                row_str += '|' + c

            # add a new line character to the end of the row
            row_str += '|\n'

            # add the row_string to the board visualization
            visual += row_str

            # add a seperator row of dashes seperating board rows
            visual += (15 * '-') + '\n'

            # requeue the row back to the board object
            self.hold_board.push(row)

        # transfer the temp board back to the main board to maintain order
        self.transfer_hold_to_board()
        
        return visual

    def transfer_hold_to_board(self) -> None:
        '''
        transfers the temporary board back to the main board
        params:
            self -- the current object
        returns:
            void
        '''

        # transfer the rwos from the temproary board back to main board
        for r in range(self.rows):
            row = self.hold_board.pop()
            self.board.push(row)

    def next_player(self) -> None:
        '''
        sets the player variable to alternate turns
        params:
            self -- the current object
            turn -- 1 for player 1 and 0 for player 2
        returns:
            void
        '''

        self.player_one = not self.player_one


if __name__ == "__main__":
    board = ConnectFour()
    print(board)
    board.add_piece(4)
    board.next_player()
    board.add_piece(4)
    board.add_piece(3)
    board.next_player()
    board.add_piece(3)
    print(board)