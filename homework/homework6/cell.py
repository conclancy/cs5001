''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 6 - Maze
clancy.co@northeastern.edu (002781018)
03 April 2022

The file contains the Cell class used for creating a maze. 
'''


from json.encoder import INFINITY


class Cell:
    '''
    The cell class represents a cell within the maze.
    attributes: row, column, cell_type
    methods: 
    '''

    def __init__(self, row, column, cell_type, distance = INFINITY) -> None:
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
            elif cell_type == "*":
                self.cell_type = cell_type
            else:
                raise ValueError("cell_type must be 'X', 'E', 'S', '*', ' '")
        else:
            raise TypeError("column must be of type str")

        if isinstance(distance, float):
            if distance < 0:
                raise ValueError("distance must be a float > 0")
            else:
                self.distance = distance
        else:
            raise TypeError("distance must be of type float")


    def __str__(self) -> str:
        '''Set class default string print behavior'''
        return str(self.row) + ', ' + str(self.column) + ', ' \
               + self.cell_type + ', ' + str(self.distance)


    def set_distance(self, distance) -> None:
        '''
        set_distance allows the user to change the distance of the cell to 
            to the nearest exit
        params: distnace is an int representing the distance to the exit
        returns: None 
        '''

        if isinstance(distance, float):

            # only set the distance for valid cells 
            if self.cell_type == ' ' and self.distance == INFINITY:
                self.distance = distance

        else:
            raise TypeError("distance must be of type float") 


    def get_distance(self) -> str:
        '''
        get_direction current distance from the start for valid space cells
            all other cells return their character representation.
        params: None
        returns: a string representing the distance or character of the cell
        '''

        # returns the cell type or the distane of the cell

        if self.cell_type != ' ':
            return self.cell_type
        elif self.distance != INFINITY:
            return str(int(self.distance))
        else:
            return self.cell_type

    def clear_distance(self) -> None:
        '''
        clear_distance sets the cells distance back to infinity
        params: None
        Returns: void
        '''
        self.distance = INFINITY


    def clear_cell(self) -> None:
        '''
        clear_distance chances all of the space cells back to INFINITY so the
            maze solver can be run again
        params: None 
        Returns:void
        '''

        # only reset the valid space ' ' or start 'S' cells
        if self.cell_type in [' ', 'S', '*']:
            self.cell_type = ' '
            self.distance = INFINITY
            self.direction = ""


    def get_xy(self) -> list:
        '''
        get_xy returns the x and y coordinates for the cell
        params: None
        returns: a list with the x and y coordinats
        '''

        return [self.column, self.row]


    def get_x(self) -> int:
        '''
        get_x returns the x coorindate for the cell
        params: None
        return: the x coordinate as a integer 
        '''
        return self.column

    def get_y(self) -> int:
        '''
        get_y returns the y coorindate for the cell
        params: None
        return: the y coordinate as a integer 
        '''
        return self.row


    def make_start(self) -> list:
        '''
        make_start changes a valid space cell into an 'S' start square
        params: None
        returns: None
        '''

        if self.cell_type == ' ':
            self.cell_type = 'S'

        return self.get_xy()


    def is_neighbor(self, x, y) -> bool:
        '''
        is_neighbor allow the cell to tell you if it is a neightbor to the 
            cell with input cordinates x and y.  A neighbor is defined as a
            cell that shares an edge with the current cell. 
        params: two ints, x and y
        returns: bool for whether or not the cell is a neighbor
        '''

        # North cell
        if self.row == y - 1 and self.column == x:
            return True

        # East cell
        elif self.row == y and self.column == x + 1:
            return True

        # South cell
        elif self.row == y + 1 and self.column == x:
            return True

        # West cell
        elif self.row == y and self.column == x - 1:
            return True

        # all other cells return False, not a neighbor
        else:
            return False


if __name__ == "__main__":
    test_cell = Cell(3, 4, " ") 

    test_cell.set_distance(1.0)
    print(test_cell.get_distance())
    print(test_cell)
