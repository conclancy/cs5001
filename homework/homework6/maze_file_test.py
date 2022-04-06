''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 6 - Maze
clancy.co@northeastern.edu (002781018)
03 April 2022

The file contains the tests for the Cell class.
The manual keyboard entry methods can be found in maze_keyboard_test.py
'''

from cell import Cell
from maze import Maze
import unittest


class MazeTest(unittest.TestCase):
    '''
    MazeTest extends the TestCase class to test the functionality of
    the Maze class's attributues and functions
    '''

    def test_init(self):
        '''
        Test the initalization of a maze object using the read_maze_file
        function.
        '''

        # test we can import a file and pull dimensions
        maze = Maze("maze-just-walls.txt")
        self.assertEqual(maze.width, 13)

        # test we can import a file and pull dimensions
        maze = Maze("maze-barrier.txt")
        self.assertEqual(maze.height, 7)

        # test that the cells loaded correctly by looking at the length
        # of the cells list
        self.assertEqual(len(maze.cells), 7)
        self.assertEqual(len(maze.cells[0]), 13)

        # test incorrect file path throws a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            maze = Maze("maze.txt")


    def test_get_maze(self):
        '''Test get_maze function is returning the expected strings''' 
        
        # initalize a maze 
        maze = Maze("maze-just-walls.txt")

        # initalize expected string
        expected = 'XXXXXXXXXXXXX\n' + \
                   'X           X\n' + \
                   'X           X\n' + \
                   'X           X\n' + \
                   'X           X\n' + \
                   'X           X\n' + \
                   'XXXXXXEXXXXXX\n'
        
        # test 
        self.assertEqual(maze.get_maze(), expected)

        # initalize a second maze 
        maze = Maze("maze-unreachable.txt")

        # initalize expected string
        expected = 'XXXXXXXXXXXXX\n' + \
                   'X           X\n' + \
                   'XXXXXXXXXXXXX\n' + \
                   'X           X\n' + \
                   'X  XXXXXXX  X\n' + \
                   'X           X\n' + \
                   'XXXXXXEXXXXXX\n'
        
        # test 
        self.assertEqual(maze.get_maze(), expected)


    def test_get_all_cells(self):
        '''get_all_cells should return a flat list of all cell objects'''

        # initalize a maze 
        maze = Maze("maze-just-walls.txt")

        # test to ensure list is the proper length
        self.assertEqual(len(maze.get_all_cells()), maze.width * maze.height)

        # test to ensure the first object is of type `Cell`
        self.assertTrue(isinstance(maze.get_all_cells()[0], Cell))


    def test_set_start(self):
        '''test that set_start declares one of the cells an 'S'''

        # initalize maze and test positions are returning correct values
        maze = Maze("maze-unreachable.txt")
        maze.set_start([4, 7])
        self.assertListEqual(maze.start_cell_xy, [7, 5])
        self.assertListEqual(maze.start_cell_position, [3, 6])

        # test that the visualization is working as expected
        expected = 'XXXXXXXXXXXXX\n' + \
                   'X           X\n' + \
                   'XXXXXXXXXXXXX\n' + \
                   'X     S     X\n' + \
                   'X  XXXXXXX  X\n' + \
                   'X           X\n' + \
                   'XXXXXXEXXXXXX\n'
        
        # visualization using the get_maze function
        self.assertEqual(maze.get_maze(), expected)


    def test_maze_functionality(self): 
        '''
        Test to make sure the test maze is able to have start locations
        selected, paths to an exit identified, and the ability to reset
        the maze and run another test from a different start location
        '''

        # initalize the maze for testing
        maze = Maze("maze-unreachable.txt")
        maze.find_exits([4,7])

        # test that the visualization is working as expected
        expected = 'XXXXXXXXXXXXX\n' + \
                   'X           X\n' + \
                   'XXXXXXXXXXXXX\n' + \
                   'X ****S     X\n' + \
                   'X *XXXXXXX  X\n' + \
                   'X *****     X\n' + \
                   'XXXXXXEXXXXXX\n'
        
        # test that the maze has been filled in with * path
        self.assertEqual(maze.get_maze(), expected)

        # test that the visualization is working as expected
        cleared = 'XXXXXXXXXXXXX\n' + \
                  'X           X\n' + \
                  'XXXXXXXXXXXXX\n' + \
                  'X           X\n' + \
                  'X  XXXXXXX  X\n' + \
                  'X           X\n' + \
                  'XXXXXXEXXXXXX\n'

        maze.reset_maze()

        # test that the * path has been removed
        self.assertEqual(maze.get_maze(), cleared)

        # test that an unsolvable maze just returns a start with no * path
        maze.find_exits([2,7])

        # test that the visualization is working as expected
        expected = 'XXXXXXXXXXXXX\n' + \
                   'X     S     X\n' + \
                   'XXXXXXXXXXXXX\n' + \
                   'X           X\n' + \
                   'X  XXXXXXX  X\n' + \
                   'X           X\n' + \
                   'XXXXXXEXXXXXX\n'
        
        # test that the * path has been removed
        self.assertEqual(maze.get_maze(), expected)


if __name__ == "__main__":
    unittest.main()