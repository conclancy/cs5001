''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 12 - Sorting
clancy.co@northeastern.edu (002781018)
22 APR 22 

This file tests the sort function
'''

from frequencysort import sort
import unittest


class SortTest(unittest.TestCase):
    '''
    SortTest extends the TestCase class to thest the functionality of the
    sort function from frequencysort. 
    '''

    def test_instruction_example(self):
        '''Test the example from instructions'''

        output = sort([3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8])

        self.assertListEqual(output, [3, 3, 3, 1, 1, 1, 8, 8, 8, 6, 7])

    def test_negatives(self):
        '''Test to ensure negative numbers work correctly '''

        output = sort([-1, -1, -5, -6, -6, -6, 8, -6, 0])

        self.assertListEqual(output, [-6, -6, -6, -6, -1, -1, -5, 8, 0])

    def test_all_same(self): 
        '''Test what happens if all the frequencies are the same'''

        output = sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        self.assertListEqual(output, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_all_same_reverse(self): 
        '''Test what happens if all the frequencies are the same'''

        output = sort([9, 8, 7, 6, 5, 4, 3, 2, 1])

        self.assertListEqual(output, [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_not_equals(self):
        '''Test that a list does not return correctly'''

        output = sort([3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8])

        self.assertNotEqual(output, [3, 3, 3, 1, 1, 1, 8, 8, 8, 6])

    def test_empty(self):
        '''Test the example from instructions'''

        output = sort([])

        self.assertListEqual(output, [])

    def test_letters(self):
        '''Test a list with letters'''

        output = sort(['o', 'C', 'C', 'n'])

        self.assertListEqual(output, ['C', 'C', 'o', 'n'])

    def test_floats(self):
        '''Test a list of floats'''

        output = sort([3, 3, 1, 1, 1, 8.5, 3, 6, 8, 7, 8])

        self.assertListEqual(output, [3, 3, 3, 1, 1, 1, 8, 8, 8.5, 6, 7])


if __name__ == "__main__":
    unittest.main()
