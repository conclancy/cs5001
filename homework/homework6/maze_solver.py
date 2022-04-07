''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 6 - Maze
clancy.co@northeastern.edu (002781018)
03 April 2022

The file contains the driver program for this module.
This file will promot the user to create or load a maze into the program.
The program will then solve the maze by plotting the optimal route from a 
defined start point to the nearest exit.
'''

from maze import Maze


def main() -> None:
    '''
    This function creaetes a maze and solves it based on given start location
    params: None
    returns: Void
    '''

    # initialize variables
    maze = None
    is_alive = True

    # keep the program alive until the user quits the program
    while is_alive:

        # menu of options for the user to select from 
        menu = 'Select from the following items:\n' + \
           '    [1] - Load a new maze from a file\n' + \
           '    [2] - Enter a new maze manually with your keyboard\n' + \
           '    [3] - Choose a start location for your maze\n' + \
           '    [4] - Print the maze to see current configuration\n' + \
           '    [5] - Reset and clear maze to original configuration\n' + \
           '    [0] - Exit the program '

        print(menu)

        command = input("Please choose an option from the menu above: ")

        # exit loop and program 
        if command == '0':
            is_alive = False

        # allow the user to input a file to generate a new maze 
        elif command == '1':

            # Bring the user back to the main menu if their file is not found
            try:
                file = input("Please enter a file path: ")
                maze = Maze(file)
                print(maze.get_maze())
            except FileNotFoundError:
                print("The file path you entered was not found :(")
                print("Please select another option")

        # allow the user to type in the design for a new maze
        elif command == '2':

            print("Minimum maze size is 3 x 3 characters")

            # variables
            width = 0
            height = 0
            width_prompt = 'Enter maze width between 3 and 120: '
            height_prompt = 'Enter maze height between 3 and 40: '

            # get width input from user
            while width < 3 or width > 120: 
                raw_width = input(width_prompt)
                if raw_width.isnumeric():
                    width = int(raw_width)

            # get height input from user
            while height < 3 or height > 40:
                raw_height = int(input(height_prompt))
                if raw_height.isnumeric():
                    height = int(raw_height)

            maze = Maze("", width, height)
            print(maze.get_maze())

        # solves the maze for the user based on an input start location
        elif command == '3':
            try:
                print("Coordinates start at [0,0] in the top left corner")

                # variables
                start_x = 0
                start_y = 0  
                row = maze.height - 1
                col = maze.width - 1
                x_prompt = f'Enter start x coordinate between 2 - {row}: '
                y_prompt = f'Enter start y cordinate between 2 - {col}: '

                # get x coordinate from the user
                while start_x < 2 or start_x > row:
                    raw_x = input(x_prompt)
                    if raw_x.isnumeric():
                        start_x = int(raw_x)

                # get y coordinate from the user
                while start_y < 2 or start_y > col:
                    raw_y = input(y_prompt)
                    if raw_y.isnumeric():
                        start_y = int(raw_y)

                maze.find_exits([start_x, start_y])
                print(maze.get_maze())

            except AttributeError:
                print("Enter a maze using options [1] or [2] first")
            except ValueError:
                print("Invalid start location.  Please try again.")

        # allows the user to reprint the maze to see the current state
        elif command == '4':
            try:
                print(maze.get_maze())
            except AttributeError:
                print("Enter a maze using options [1] or [2] first")

        # allows the user to clear the maze to original configuration
        elif command == '5':
            try:
                print(maze.reset_maze())
                print('The maze has been reset')
            except AttributeError:
                print("Enter a maze using options [1] or [2] first")


if __name__ == "__main__":
    main()
