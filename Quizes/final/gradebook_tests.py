'''
CS5001.38359.202230 - SEC 05 - John Wilder
Final - Gradebook Test
clancy.co@northeastern.edu (002781018)
3 MAY 22 

You must implement a testing class that thoroughly tests
the methods described in gradebook.py

You do not need to implement the methods, the description given
in the comments are sufficient for creating tests
'''

from gradebook import Gradebook
import unittest

class GradebookTest(unittest.TestCase):
    '''
    GradebookTest extends the Test the TestCase class to test the 
    functionality of the Gradebook test class. 
    '''

    def test_init(self):
        '''Test the initiation and attributes of the gradebook class'''

        # instantiate an object
        gradebook = Gradebook("cs5001", 2022, "Spring", "Wilder", ['Connor'])

        # test attributes equals
        self.assertEqual(gradebook.course_name, "cs5001")
        self.assertEqual(gradebook.year, 2022)
        self.assertEqual(gradebook.semester, "Spring")
        self.assertEqual(gradebook.instructor, "Wilder")
        self.assertListEqual(gradebook.students, ["Connor"])

        # test not equals
        self.assertNotEqual(gradebook.course_name, "cs5002")
        self.assertNotEqual(gradebook.year, 2021)
        self.assertNotEqual(gradebook.semester, "Summer")
        self.assertNotEqual(gradebook.instructor, "Clancy")
        self.assertNotEqual(gradebook.students, ["Wilder"])

    def test_init_errors(self):
        '''Test to make sure errors are raised when the should be'''

        # test name string error
        with self.assertRaises(ValueError):
            Gradebook(1, 2022, "Summer", "Wilder", ["Connor"])

        # test year not string
        with self.assertRaises(ValueError):
            Gradebook("cs5001", "2022", "Summer", "Wilder", ["Connor"])
        
        # test year not float
        with self.assertRaises(ValueError):
            Gradebook("cs5001", 2022.0, "Summer", "Wilder", ["Connor"])

        # test year year before 2000
        with self.assertRaises(ValueError):
            Gradebook("cs5001", 1999, "Summer", "Wilder", ["Connor"])

        # test that semester error catching works
        with self.assertRaises(ValueError):
            Gradebook("cs5001", 2022, "Winter", "Wilder", ['Connor'])
        
        # test that instructor must be a string
        with self.assertRaises(ValueError):
            Gradebook("cs5001", 2022, "Winter", 1, ['Connor'])

        # test that students must be a list
        with self.assertRaises(ValueError):
            Gradebook("cs5001", 2022, "Winter", "Wilder", 'Connor')

    def test_average_grade(self):
        '''Test to make sure adding and average grade works as expected'''

        # instantiate a gradebook object 
        gradebook = Gradebook("cs5001", 2022, "Spring", "Wilder", ['Connor'])

        # create grades to add
        grades1 = {'Connor': 0}
        grades2 = {'Connor': 100}

        # add grades to the object 
        gradebook.add_grade(grades1)
        gradebook.add_grade(grades2)

        # test to make sure the average is correct
        self.assertEqual(gradebook.average_grade(), {'Connor': 50.0})

        # test grade letter
        self.assertEqual(gradebook.letter_grade(200), {'Connor': 'F'})
        self.assertEqual(gradebook.letter_grade(100), {'Connor': 'A'})

    def test_add_grade_erros(self):
        '''Tests to make sure add_grade only accepts dictionaries'''

        # instantiate a gradebook object 
        gradebook = Gradebook("cs5001", 2022, "Spring", "Wilder", ['Connor'])

        # create grades to add
        grades1 = 100

        # add grades to the object 
        with self.assertRaises(ValueError):
            gradebook.add_grade(grades1)

    def test_str(self):
        '''Test to make sure the string functionality works'''

        # instantiate a gradebook object 
        gradebook = Gradebook("cs5001", 2022, "Spring", "Wilder", ['Connor'])

        # variables
        divider = '-' * 20
        test_string = ''

        # gradebook metadata  
        test_string += 'course name: ' + 'cs5001' + '\n'
        test_string += 'year:        ' + str(2022) + '\n'
        test_string += 'semester:    ' + 'Spring' + '\n'
        test_string += 'instructor:  ' + 'Wilder' + '\n'
        test_string += '\n'
        test_string += 'students'
        test_string += '\n'
        test_string += divider + '\n'
        test_string += '    Connor:[]'+ '\n'

        self.assertEqual(str(gradebook), test_string)

  
if __name__ == "__main__":
    unittest.main()

