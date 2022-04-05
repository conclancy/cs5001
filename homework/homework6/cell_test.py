''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 6 - Maze
clancy.co@northeastern.edu (002781018)
03 April 2022

The file contains the tests for the Cell class.
'''

from cell import Cell
import unittest


class CellTest(unittest.TestCase):

    def test_init(self):
        '''Test the initatilization of a cell'''

        cell = Cell(3, 4, " ")
        
        # test intial attributes
        self.assertEqual(cell.row, 3)
        self.assertEqual(cell.column, 4)
        self.assertEqual(cell.cell_type, " ")
        self.assertAlmostEqual(cell.distance, float('inf'))

        # test does not equals 
        self.assertNotEqual(cell.row, 4)
        self.assertNotEqual(cell.column, 1)
        self.assertNotEqual(cell.cell_type, '*')
        self.assertNotAlmostEqual(cell.distance, 9999999.99)

        # test error messages
        with self.assertRaises(TypeError):
           cell = Cell(3.0, 4, " ")

        with self.assertRaises(TypeError):
           cell = Cell(3, "S", " ")

        with self.assertRaises(ValueError):
           cell = Cell(3, 4, "4")

        with self.assertRaises(TypeError):
           cell = Cell(3, 4, 4)

        with self.assertRaises(ValueError):
           cell = Cell(3, 4, " ", -1.0)
        
        with self.assertRaises(TypeError):
           cell = Cell(3, 4, " ", 1)

    
    def test__str__(self):
        '''Test the __str__ functionality of a cell'''

        cell = Cell(3, 4, " ")

        # test function 
        self.assertEqual(cell.__str__(), '3, 4,  , inf')

        # test cell with a distance
        cell.distance = 1.0
        self.assertEqual(cell.__str__(), '3, 4,  , 1.0')

        # test error 
        

    def test_get_distance(self):
        '''
        Test the get_distance function
        This function returns the character necessary when printing the board
        '''

        cell = Cell(3, 4, " ")

        # test default value
        self.assertEqual(cell.get_distance(), ' ')

        # test another distance value
        cell.distance = 1.0
        self.assertEqual(cell.get_distance(), '1')


    def test_clear_distance(self):
        '''
        Test the clear_distance function to ensure it resets the distance 
        attribute to INFINITY
        '''

        # initialize cell and test successful initalization
        cell = Cell(3, 4, " ", 1.0)
        self.assertEqual(cell.__str__(), '3, 4,  , 1.0')

        # test the clear functionality
        cell.clear_distance()
        self.assertAlmostEqual(cell.distance, float('inf'))


    def test_clear_cell(self):
        '''
        Test the clear_cell function to ensure it resets the cell type
        back to the original value, sets the distance to INFINITY
        '''

        # test that values are cleared 
        cell = Cell(3, 4, "S", 1.0)
        self.assertEqual(cell.__str__(), '3, 4, S, 1.0')
        cell.clear_cell()
        self.assertEqual(cell.__str__(), '3, 4,  , inf')

        # test to ensure an `X` cell is unaffected
        cell = Cell(3, 4, "X", 1.0)
        self.assertEqual(cell.__str__(), '3, 4, X, 1.0')
        cell.clear_cell()
        self.assertEqual(cell.__str__(), '3, 4, X, 1.0')

        # test to ensure an `E` cell is unaffected
        cell = Cell(3, 4, "E", 2.0)
        self.assertEqual(cell.__str__(), '3, 4, E, 2.0')
        cell.clear_cell()
        self.assertEqual(cell.__str__(), '3, 4, E, 2.0')


    def test_coordinate_functions(self):
        '''
        Test to ensure that the get_xy function returns the x and y
        coordinates for the cell.  X is the column, y is the row starting
        from the top left corner of the maze board. 
        '''

        # test initialization 
        cell = Cell(3, 4, " ", 1.0)
        self.assertListEqual(cell.get_xy(), [4, 3])
        self.assertEqual(cell.get_x(), 4)
        self.assertEqual(cell.get_y(), 3)

        # test on row change
        cell.row = 8
        self.assertListEqual(cell.get_xy(), [4, 8])
        self.assertEqual(cell.get_x(), 4)
        self.assertEqual(cell.get_y(), 8)

        # test on column change
        cell.column = 10
        self.assertListEqual(cell.get_xy(), [10, 8])
        self.assertEqual(cell.get_x(), 10)
        self.assertEqual(cell.get_y(), 8)


    def test_make_start(self):
        '''
        Test that the make_start function performs both intended functions:
            1. Change the cell_type attribute to 'S' (for the start cell)
            2. Return the x and y coordinate for use in the calling object
        '''

        # test initialization 
        cell = Cell(3, 4, " ", 1.0)
        self.assertEqual(cell.__str__(), '3, 4,  , 1.0')

        # test list return and cell type change
        self.assertListEqual(cell.make_start(), [4, 3])
        self.assertEqual(cell.cell_type, 'S')

        # test that we can't start on a non-blank cell  
        cell.cell_type = 'X'
        with self.assertRaises(ValueError):
           cell.make_start()


    def test_is_neighbor(self):
        '''
        Test is_neighbor to ensure that it is able to properly identify if the
        given cooridnates are the coordinates of a neighbor cell by returning
        a True, else returning a False
        '''

        # test initialization 
        cell = Cell(3, 4, " ", 1.0)
        self.assertEqual(cell.__str__(), '3, 4,  , 1.0')

        # test north neighbor
        self.assertTrue(cell.is_neighbor(3, 3))

        # test east neighbor
        self.assertTrue(cell.is_neighbor(4, 4))

        # test south neighbor
        self.assertTrue(cell.is_neighbor(5, 3))

        # test west neighbor
        self.assertTrue(cell.is_neighbor(4, 2))

        # test northwest neighbor is not a neighbor
        self.assertFalse(cell.is_neighbor(3, 2))

        # test 1,1 is not a neighbor
        self.assertFalse(cell.is_neighbor(1, 1))




if __name__ == "__main__":
    unittest.main()