''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 7 - Connect Four
clancy.co@northeastern.edu (002781018)
17 APR 22 

The file tests the connect_four class
'''


from multiprocessing.sharedctypes import Value
from connect_four import ConnectFour
from stack import Stack
import unittest


class ConnectFourTest(unittest.TestCase):
    '''
    ConnectFourTest extends the TestCase class to test the functionality
    of the ConnectFour board game class
    '''

    def test_init(self):
        '''Test the initalization of the board'''

        board = ConnectFour()

        # test initial attributes
        self.assertEqual(board.rows, 6)
        self.assertEqual(board.columns, 7)
        self.assertTrue(board.player_one)
        self.assertTrue(isinstance(board.board_stack, Stack))

        # test failure of attributes
        self.assertNotEqual(board.rows, 8)
        self.assertNotEqual(board.columns, 4)
        self.assertFalse(isinstance(board.board_stack, list))

    def test_get_row(self):
        '''Test the get row function'''

        board = ConnectFour()

        # test initial row
        self.assertEqual(board.get_row(0), [' '] * 7)
        self.assertEqual(board.get_row(5), [' '] * 7)
        with self.assertRaises(IndexError):
            board.get_row(6)

        # add piece test 
        board.add_piece(0)
        self.assertEqual(board.get_row(0), [' '] * 7)
        self.assertEqual(board.get_row(5), 
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '])

        # add second piece test 
        board.add_piece(0)
        self.assertEqual(board.get_row(0), [' '] * 7)
        self.assertEqual(board.get_row(5), 
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual(board.get_row(4), 
                         ['O', ' ', ' ', ' ', ' ', ' ', ' '])

    def test_get_column(self):
        '''Test the get column function'''

        board = ConnectFour()

        # test initial row
        self.assertEqual(board.get_column(0), [' '] * 6)
        self.assertEqual(board.get_column(5), [' '] * 6)
        with self.assertRaises(IndexError):
            board.get_column(7)

        # add piece test 
        board.add_piece(5)
        self.assertEqual(board.get_column(0), [' '] * 6)
        self.assertEqual(board.get_column(5), 
                         [' ', ' ', ' ', ' ', ' ', 'X'])

        # add second piece test 
        board.add_piece(5)
        self.assertEqual(board.get_column(5), 
                         [' ', ' ', ' ', ' ', 'O', 'X'])

    def test_end_game(self):
        '''Test the is_game_over and get_winner functions'''

        board = ConnectFour()

        # create a winning board for X
        board.add_piece(0)
        board.add_piece(1)
        board.add_piece(0)
        board.add_piece(1)
        board.add_piece(0)
        board.add_piece(1)

        # test not over yet
        self.assertEqual(board.get_winner(), None) 
        self.assertFalse(board.is_game_over())

        # test game now over 
        board.add_piece(0)
        self.assertTrue(board.is_game_over())
        self.assertEqual(board.get_winner(), 'X')

    def test_add_peice(self):
        '''Test add_piece function'''

        board = ConnectFour()

        # test negative numbers
        with self.assertRaises(ValueError): 
            board.add_piece(-1)

        # test float
        with self.assertRaises(ValueError): 
            board.add_piece(-.01)

        # test larger than board size
        with self.assertRaises(ValueError): 
            board.add_piece(8)

        # test larger than board size
        with self.assertRaises(ValueError): 
            board.add_piece("test")

    def test_str(self): 
        '''Tests the __str__ method override'''

        board = ConnectFour()

        # initial setup test
        expected = '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n'

        self.assertEqual(str(board), expected)

        # add piece 
        board.add_piece(0)

        expected = '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '|X| | | | | | |\n' + \
                   '---------------\n'

        self.assertEqual(str(board), expected)

        # add player 2 piece 
        board.add_piece(0)

        expected = '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '| | | | | | | |\n' + \
                   '---------------\n' + \
                   '|O| | | | | | |\n' + \
                   '---------------\n' + \
                   '|X| | | | | | |\n' + \
                   '---------------\n'

        self.assertEqual(str(board), expected)


if __name__ == "__main__":
    unittest.main()
