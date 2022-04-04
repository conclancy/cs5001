''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 6 - Maze
clancy.co@northeastern.edu (002781018)
03 April 2022

The file calculates Cell class used for creating a maze. 
'''


class Cell:
    '''
    The cell class represents a cell within the maze.
    attributes: row, column, cell_type
    methods: 
    '''

    def __init__(self, row, column, cell_type) -> None:
        '''Constructor for the Cell Class'''

        # sets the row attribute if it is an int
        if isinstance(row, int):
            self.row = row
        else:
            raise TypeError("row must be of type int")

        # set the column attribute if it is an int
        if isinstance(column, int):
            self.column = column
        else:
            raise TypeError("column must be of type int")

        # set the cell_type if it is an X, S, or ' ' str
        if isinstance(cell_type, str):
            if cell_type == "X":
                self.cell_type = cell_type
            elif cell_type == "E":
                self.cell_type = cell_type
            elif cell_type == " ":
                self.cell_type = cell_type
            elif cell_type == "S":
                self.cell_type = cell_type
            else:
                raise ValueError("cell_type must be 'X', 'E', 'S', ' '")
        else:
            raise TypeError("column must be of type str")


    def __str__(self) -> str:
        '''Set class default string print behavior'''
        return str(self.row) + ', ' + str(self.column) + ', ' + self.cell_type


if __name__ == "__main__":
    test_cell = Cell(3, 4, "X")
    print(test_cell)
