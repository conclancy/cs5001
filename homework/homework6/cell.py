''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 6 - Maze
clancy.co@northeastern.edu (002781018)
03 April 2022

The file calculates Cell class used for creating a maze. 
'''


from json.encoder import INFINITY
from multiprocessing.dummy import Value


class Cell:
    '''
    The cell class represents a cell within the maze.
    attributes: row, column, cell_type
    methods: 
    '''

    def __init__(self, row, column, cell_type, distance = INFINITY, 
                 direction = "") -> None:
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

        if isinstance(distance, float):
            self.distance = distance
        else:
            raise TypeError("distance must be of type float")
        
        if isinstance(direction, str):
            directions = ['North', 'South', 'East', 'West', ""]

            if direction in directions:
                self.direction = direction
            else:
                raise ValueError("direction must equal 'North', 'South', \
                                 'East', 'West'")
        else:
            raise TypeError("direction must be of type str")


    def __str__(self) -> str:
        '''Set class default string print behavior'''
        return str(self.row) + ', ' + str(self.column) + ', ' \
               + self.cell_type + ', ' + str(self.distance) + ', ' \
               + self.direction


    def set_distance(self, distance) -> None:
        '''
        set_distance allows the user to change the distance of the cell to 
            to the nearest exit
        params: distnace is an int representing the distance to the exit
        returns: None 
        '''

        if isinstance(distance, float):
            self.distance = distance
        else:
            raise TypeError("distance must be of type float") 


    def set_direction(self, direction) -> None:
        '''
        set_direction allows the user to change the direction of the cell in 
            comparison to the start cell
        params: distnace is an int representing the distance to the exit
        returns: None 
        '''

        if isinstance(direction, str):
            directions = ['North', 'South', 'East', 'West', ""]

            # check to make sure the direction is valid
            if direction in directions:
                self.direction = direction
            else:
                raise ValueError("direction must equal 'North', 'South', \
                                 'East', 'West'")
        else:
            raise TypeError("direction must be of type str")


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
        clear_distance chances all of the space cells back to INFINITY so the
            maze solver can be run again
        params: None 
        Returns:None
        '''

        # only reset the valid space ' ' cells
        if self.cell_type == ' ':
            self.distance = INFINITY


if __name__ == "__main__":
    test_cell = Cell(3, 4, " ") 

    test_cell.set_direction("North")
    test_cell.set_distance(1.0)
    print(test_cell.get_distance())
