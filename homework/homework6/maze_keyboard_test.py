''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 6 - Maze
clancy.co@northeastern.edu (002781018)
03 April 2022

The file contains the tests for the Cell class.
The automatic file read method can be found in maze_keyboard_test.py
    along with the additional tests for the Cell class as all functions are
    shared once the Maze is initiated by either method. 
'''

from maze import Maze
import unittest


class KeyboardTest(unittest.TestCase):
    '''
    KeyboardTest extends the TestCase class to test the functionality of
    the Maze class's attributues and functions
    '''

    def test_keyboard_init(self):
        '''
        This function allows us to test the creation of a maze manually with
        the keyboard. 
        '''

        # test you manually enter the ensure the test passes
        expected = 'XXX\n' + \
                   'X X\n' + \
                   'XEX\n'

        # test we can manually enter a maze using the keyboard
        maze = Maze("", 3, 3)
        self.assertEqual(maze.width, 3)
        self.assertEqual(maze.width, 3)
        self.assertEqual(maze.get_maze(), expected)

        # test you the find exit functionality still works
        '''
        enter extected as followed in order to get the test to pass

        XXXXX
        X   X
        X   X
        XXEXX

        '''

        maze = Maze("", 5, 4)
        expected = 'XXXXX\n' + \
                   'XS* X\n' + \
                   'X * X\n' + \
                   'XXEXX\n'
        
        maze.find_exits([2,2]) 

        self.assertEqual(maze.get_maze(), expected)


if __name__ == "__main__":
    unittest.main()
