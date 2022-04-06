''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 6 - Maze
clancy.co@northeastern.edu (002781018)
03 April 2022

The file contains the Maze class used for running the maze solver. 
'''

import os
import sys
from cell import Cell


class Maze:
    '''
    Maze class for creating your maze object
    attributes: width, height
    methods: #TODO 
    '''

    def __init__(self, file, width = 3, height = 3) -> None:
        '''Constructor for the Maze Class'''

        # set the width attribute
        if isinstance(width, int):
            if width >= 3 and width <= 120:
                self.width = width
            else:
                raise ValueError('Acceptable width values: 3 <= w <= 120')
        else:
            raise TypeError('Width must be of type int.')

        # set the height attribute
        if isinstance(height, int):
            if height >= 3 and height <= 40:
                self.height = height
            else:
                raise ValueError('Acceptable height values: 3 <= h <= 40')
        else:
            raise TypeError('height must be of type int.')

        # hidden initalization of blank cells list attribute
        self.cells = []

        # set the filename attribute
        if isinstance(file, str):
            self.file = file

            if file == "":
                self.read_maze_keyboard()
            else:
                self.read_maze_file()
        else:
            raise TypeError('file must be if type str')

        # hidden initalization of the start cells
        # start position of the cell in the maze list
        self.start_cell_position = [-1, -1]

        # start position of the cell using x, y cordinates
        self.start_cell_xy = [-1, -1]


    def read_maze_file(self) -> None:
        '''
        read_maze_file reads a maze file and sets the cells list attribute
        params self
        returns nothing
        '''

        # read in the requested file
        try:
            file = open(os.path.join(sys.path[0], self.file), 'r')
        except FileNotFoundError:
            e = "Invalid path, please retype and try again"
            raise FileNotFoundError(e)

        # Read all of the contents of the file
        # into a list of strings called filedata.
        filedata = file.readlines()
        file.close()

        # set row count variable
        row_count = 1

        # iterate through each row of the maze 
        for row in filedata:

            # create variables
            column_count = 1
            row_list =[]

            # use the first row to set the dimensions 
            if row_count == 1:
                dimensions = row.split()
                self.width = int(dimensions[0])
                self.height = int(dimensions[1])

            # use the remaining rows to build the maze
            else:

                # for every character except the last \n character
                # create a cell for that object.
                for cell in row[:-1]:
                    row_list.append(Cell(row_count, column_count, cell))
                    column_count += 1 

                self.cells.append(row_list)

            row_count += 1


    def read_maze_keyboard(self) -> None:
        '''
        read_maze_keyboard allows the user to generate a maze manually
        params self
        returns nothing
        '''

        # create variables 
        user_prompt = "Enter " + str(self.width) + " characters:"
        current_row = 1

        # prompt the user to enter 1 row at a time
        while current_row <= self.height:

            # create variables
            iteration = 0
            column_count = 1
            row_list =[]
            characters = ""

            # ensure the user enters the right number of characters
            while len(characters) != self.width:
                characters = ""

                # if this is not the first time in this loop, remind the user
                # of the proper string length before next prompt
                if iteration > 0: 
                    print("Your input length is incorrect!")
                    print("Please enter", self.width, "valid characters")

                # prompt the user for the row 
                user_input = input(user_prompt)

                # check each character to ensure it is a valid input 
                for i in user_input:
                    if i not in ['X', 'E', ' ']:
                        print("You entered an invalid character")
                        print("Please only enter: 'X', 'S', 'E', ' '")
                    else: 
                        characters += i

                # increment the iteration variable in case we need to repeat
                iteration += 1

            # once all row checks pass, create a maze cell for each of the 
            # characters the users input and add them to the row
            for c in characters:
                row_list.append(Cell(current_row, column_count, c))
                column_count += 1 

            self.cells.append(row_list)
            current_row += 1


    def get_maze(self) -> str:
        '''
        get_maze returns the maze set up as a multi-line string.
        param None
        returns a multi-line string representing the board
        '''

        # create a blank string variable to house the board
        maze = ''

        # for each cell in the maze, add its 'type' to the board string
        for row in self.cells:

            # create empty string variable to house row characters
            row_string = ''

            for cell in row:
                row_string += cell.get_distance()

            # add a new line character at the end of the row
            row_string += '\n'

            # add the row to the maze string
            maze += row_string

        return maze


    def get_all_cells(self) -> list:
        '''
        get_all_cells returns a flat list of all the cells in the maze
        params: None
        returns: a single dimension list containing all cells in the maze
        '''

        # variables
        all_cells = []

        # flatten list of cells
        for row in self.cells:
            for cell in row: 
                all_cells.append(cell)

        return all_cells


    def reset_maze(self):
        '''
        reset_maze clears all of the disance and direction from all of the 
            cells in the maze
        params: None
        returns: None
        '''

        # clear the distance and direction from all the cells in the maze
        for cell in self.get_all_cells():
            cell.clear_cell()


    def set_start(self, start) -> None:
        '''
        set_start sets the start attribute for the maze so that we know where
            to begin parsing the maze
        params: None
        returns: None
        '''

        if len(start) != 2:
            raise ValueError("start must be a list with two int elements")

        for i in start:
            if not isinstance(i, int):
                raise TypeError("start must be a list with two int elements")

        # initialize the x value of th start
        # subtract 1 because the first element in a python list is 0
        self.start_cell_position[0] = start[0] - 1

        # initialize the y value of th start
        # subtract 1 because the first element in a python list is 0
        self.start_cell_position[1] = start[1] - 1

        # make the user identified cell the start cell
        start_x = self.start_cell_position[0]
        start_y = self.start_cell_position[1]
        self.start_cell_xy = self.cells[start_x][start_y].make_start()


    def find_exits(self, start):   
        '''
        find_exits identifies all of the exits on cells that are categorized 
            as exits on the board.
        params: start is a list containing two elements with the x and y 
            cordinates of the start location.
        returns:  #TODO -> Type
        '''

        # clear the maze to ensure we are calculating correctly. 
        self.reset_maze()

        # declare placeholder variables for exit coordinates
        exit_x = -1
        exit_y = -1

        # initialization of start cell cordinates
        self.set_start(start)
        start_x = self.start_cell_xy[0]
        start_y = self.start_cell_xy[1]

        # loop through remainin cells and identify distnace until an exit 
        distance = 1
        exit_found = False 

        while not exit_found: 

            if distance == 1: 
                find_neighbors = [[start_x, start_y]]
            else:
                find_neighbors = []
                for cell in self.get_all_cells():
                    cell_distance = cell.get_distance()
                    if cell_distance.isnumeric():
                        if float(cell_distance) == distance - 1:
                            if cell.cell_type in [' ', 'E']:
                                find_neighbors.append(cell.get_xy())

            # prevent infinite loops
            if len(find_neighbors) < 1:
                break

            # find neighbors to the start cell and change to distance 1
            for n in find_neighbors:
                n_x = n[0] 
                n_y = n[1]

                for cell in self.get_all_cells():

                    # change the neighbors distance
                    if cell.is_neighbor(n_x, n_y):
                        cell.set_distance(float(distance))

                        # end the loop if the neighbor is an exit cell
                        if cell.cell_type == 'E':

                            exit_x = cell.get_x()
                            exit_y = cell.get_y()

                            exit_found = True

            distance = distance + 1

        # initiate path variables for proceeding loop
        path_x = exit_x
        path_y = exit_y

        # loop through cells to mark the best path
        while exit_found:

            # prevent infinite loop
            if distance < 0:
                break

            # add the numbered cells to the find_path list
            for cell in self.get_all_cells():
                if cell.is_neighbor(path_x, path_y): 
                    if cell.distance == float(distance):

                        if cell.cell_type == ' ':
                            cell.cell_type = '*'
                            path_x = cell.get_x()
                            path_y = cell.get_y()

                    elif cell.cell_type == 'S':
                        exit_found == False

            distance = distance - 1

        for cell in self.get_all_cells():
            cell.clear_distance()


if __name__ == "__main__":

    # '''
    m = Maze("maze-unreachable.txt", 13, 7)
    m.find_exits([2,7])
    # m.set_start([4, 7])
    print(m.get_maze())
    m.reset_maze()
    print(m.get_maze())
    # '''


    '''
    m = Maze("", 13, 7)
    m.find_exits([6,2])
    print(m.get_maze())
    m.reset_maze()
    print(m.get_maze())
    '''
