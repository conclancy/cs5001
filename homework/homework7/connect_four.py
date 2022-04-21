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
        self.victory_conditions = [['O', 'O', 'O', 'O'], ['X', 'X', 'X', 'X']]
        self.board_stack = Stack()
        self.board = []

        # create 6 rows with 7 columns of spaces
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append(' ')

            # enqueue the row to the board
            self.board.append(row)

    def get_row(self, row) -> list:
        '''
        get_row returns a row from the board
        params:
            self -- the current object
            row -- the int index of the row
        returns
            list representing the row
        '''
        return self.board[row]

    def get_column(self, column) -> list:
        '''
        '''
        values = []

        for row in self.board:
            values.append(row[column])

        return values

    def get_diagonals(self) -> list:
        '''
        '''
        diagonals = []

        for d in range(self.rows + self.columns - 1):
            diagonals.append([])
            max_val = max(d - self.rows + 1, 0)
            min_val = min(d + 1, self.rows)
            for diagonal in range(max_val, min_val):
                cell = self.board[self.rows - d + diagonal - 1][diagonal]
                diagonals[d].append(cell)

        for d in range(self.rows + self.columns - 1):
            diagonals.append([])
            max_val = max(d - self.rows + 1, 0)
            min_val = min(d + 1, self.rows)
            for diagonal in range(max_val, min_val):
                cell = self.board[d - diagonal][diagonal]
                diagonals[d].append(cell)

        return diagonals

    def add_piece(self, column) -> None:
        '''
        add_piece allows the user to add their piece to a given column
        params:
            self -- the current object
            column -- int value for the column to drop the piece
        returns:
            void
        '''
        print(column)

        if not self.is_game_over():
            # ensure valid input and set the piece type
            if isinstance(column, int):
                if column >= 0 and column < self.columns:
                    if self.player_one:
                        piece = 'X'
                    else:
                        piece = 'O'

                else: 
                    c = str(self.columns)
                    err = "column must be greater than 0 & less than " + c
                    raise ValueError(err)
            else: 
                err = "column must be of type int"
                raise ValueError(err)

            # column is full; invalid move
            if ' ' not in self.get_column(column):
                err = f"column full {self.get_column(column)}"
                raise ValueError(err)

            # save current board state for undo
            self.board_stack.push(self.board)

            # identify row to play
            row = self.rows - 1
            while self.board[row][column] != ' ':
                row -= 1

            # set the cell to piece
            self.board[row][column] = piece
            self.next_player()

        else:
            raise ValueError("The game is over")

    def is_game_over(self) -> bool:
        '''
        returns true when a player connects four pieces in any direction
        params:
            self -- the current object
        returns:
            bool -- true when the game is over, otherwise false
        '''

        # row victory conditions 
        for row in range(self.rows):
            for x in range(self.columns - 3):
                if self.get_row(row)[x:x + 4] in self.victory_conditions:
                    return True

        # column victory conditions
        for col in range(self.columns):
            for x in range(self.rows - 3):
                if self.get_column(col)[x:x + 4] in self.victory_conditions:
                    return True

        # diagonal visctory conditions
        for d in self.get_diagonals():
            for x in range(len(d)):
                if d[x:x + 4] in self.victory_conditions:
                    return True

        return False

    def get_winner(self) -> object:
        '''
        returns the name of the player who wins the game
        params:
            self -- the current object
        returns
            str -- the name of the player who won
        '''

        # logic for if the game is over
        if self.is_game_over():

            if self.player_one:
                peice = 'O'
            else:
                peice = 'X'

            return peice

        # play continues
        else:
            return None

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
        for row in self.board:

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

        return visual

    def next_player(self) -> None:
        '''
        sets the player variable to alternate turns
        params:
            self -- the current object
        returns:
            void
        '''

        self.player_one = not self.player_one

    def undo(self) -> None:
        '''
        undos the previous move
        params: 
            self -- the current object
        returns:
            void
        '''

        print("undo")
        print(self.board)
        self.board = self.board_stack.pop()
        print(self.board)


if __name__ == "__main__":
    board = ConnectFour()
    print(board.is_game_over())
    print(board)
    board.add_piece(1)
    board.next_player()
    board.add_piece(2)
    board.next_player()
    board.add_piece(2)
    board.add_piece(3)
    board.add_piece(3)
    board.add_piece(3)
    board.next_player()
    board.add_piece(4)
    board.next_player()
    board.add_piece(4)
    board.add_piece(4)
    board.undo()
    board.add_piece(4)
    print(board.is_game_over())
    print(board)
    print(board.get_winner())
