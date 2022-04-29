'''
CS5001.38359.202230 - SEC 05 - John Wilder
Final Examp - Gradebook
clancy.co@northeastern.edu (002781018)
29 APR 22 

# todo
'''


from multiprocessing.sharedctypes import Value


class Gradebook:
    '''
    A Gradebook is an object that contains all the information for a
    single course. It knows the name of the course, the year, the semester,
    and all of the students in the class along with their grades.

    The Gradebook needs to store each of those pieces of information in their
    attribute. The name of the course is a string, the year is an int, the semester
    is a String containing one of three possible values "Fall", "Spring", "Summer",
    the instructor's name is a string, and the students and their grades
    are stored in a dictionary where the key is the student's name (str) and
    the value is the current number of points they have received on each
    assignment (list of int).
    '''
    def __init__(self, course_name, year, semester, instructor, students):
        '''
        Initialize a new Gradebook object.

        A ValueError is raised if the input has the wrong type of input.
        A ValueError is raised if the input year is less than 2000.
        :param course_name: a string of the course name
        :param year: the year of the course, must be an int
        :param semester: one of the following values Fall, Spring, Summer
        :param instructor: the name of the instructor, as a string
        :param students: a list of student names (strings)
        '''

        # course_name 
        if isinstance(course_name, str):
            self.course_name = course_name
        else:
            raise ValueError("course_name must be of type string")
        
        # year
        if isinstance(year, int):
            if year >= 2000:
                self.year = year
            else:
                raise ValueError("year cannot be less than 2000")
        else:
            raise ValueError("year must be of type int")

        # semester
        if isinstance(semester, str):
            if semester in ['Fall', 'Spring', 'Summer']:
                self.semester = semester
            else:
                raise ValueError("semester must be Fall, Spring, Summer")
        else:
            raise ValueError("semester must be of type string")
        
        # instructor 
        if isinstance(instructor, str):
            self.instructor = instructor
        else:
            raise ValueError("instructor must be of type string")
        
        # create students dictionary from a list of students 
        if isinstance(students, list):
            self.students = students
            self.initialize_grade_dictionary()
        else:
            raise ValueError("students must be of type list")

    def average_grade(self):
        '''
        Returns the average (arithmetic mean) number of points
        received py the students in the class.
        :return: average number of point earned
        '''

    def letter_grade(self, total_points):
        '''
        Given the total points available returns a dictionary
        that has the student name along with their corresponding
        letter grade.
        The following is the grade scale
        93.00–100.00   A
        90.00–92.99    A-
        86.00–89.99    B+
        82.00–85.99   B
        77.00–81.99    B-
        73.00–76.99    C+
        69.00–72.99   C
        65.00–68.99   C-
        0.00–64.99    F

        If a grade would be out of this range a ValueError should be raised.
        If the total number of points available is less than 1 a ValueError should be raised.

        :param total_points: the total number of points (int) available in the class so far
        :return:a dictionary with a key of a student's name and a value of the letter grade (str)
        '''

    # the following methods are assumed to exist, but do not need to be tested
    # you can rely on them in your tests
    def add_grade(self, assignment_grades) -> None:
        '''
        This takes a dictionary as input. The dictionary has student names as
        a key and the points for an assignment as the value. This methods will
        add the grade for each student to the dictionary in the class that has
        student as key and the value is the list of all the grades so far.So
        if this class attribute that contains the grades has 2 grades for each
        student, after running this method there would be 3 grades for each 
        student.
        :param assignment_grades: a dictionary that has student names as keys,
            and their grade on a single assignment as the values
        '''

        # check to ensure assignment_grades is a dict
        if not isinstance(assignment_grades, dict):
            raise ValueError("assignment_grades must be of type dict")

        # for each students name in the assigned_grades dict 
        for name in assignment_grades.keys():

            # test to make sure the value is numeric.  We will use floats for
            # the points values because they will eventually be averaged 
            # resulting in a float and it allows us to input ints or floats.
            try:
                grade = float(assignment_grades[name])
                self.student_dict[name].append(grade)
            except TypeError:
                raise TypeError("grades should be numeric")
            


    def get_grades(self) -> dict:
        '''
        This method returns the dictionary of student grades for this course.
        The dictionary has the student names as keys, and a list of all of 
        their grades as values
        :return: The dictionary of student grades
        '''
        return self.student_dict


    def initialize_grade_dictionary(self) -> None:
        '''
        This is a helper function for the constructor. It takes a list of 
        students that is passed into __init__ and creates a dictionary where 
        each student name is a key, and an empty list is the value.
        :return: A new dictionary with student names as keys, and an empty
            list as values
        '''

        # function variables
        students_dict = {}

        # for each student, create a key value pair with the student's name
        # and an empty dictionary.
        for s in self.students:
            if isinstance(s, str):
                students_dict[s] = []
            else: 
                raise ValueError("student's names must be of type str")

        # set object variable to the generated student dictionary

        self.student_dict = students_dict

    def __str__(self):
        '''
        print the gradebook option in a human readable form. 
        params:
            self - the current object
        returns:
            void; it prints a string
        '''

        # variables
        divider = '-' * 20
        gradebook = ''

        # gradebook metadata  
        gradebook += 'course name: ' + self.course_name + '\n'
        gradebook += 'year:        ' + str(self.year) + '\n'
        gradebook += 'semester:    ' + self.semester + '\n'
        gradebook += 'instructor:  ' + self.instructor + '\n'
        gradebook += '\n'
        gradebook += 'students'
        gradebook += '\n'
        gradebook += divider + '\n'

        # students 
        for s in self.student_dict.keys():
            ''''''
            info = (' ' * 4 ) + s + ':' + str(self.student_dict[s]) + '\n'
            gradebook += info


        return gradebook

if __name__ == "__main__":

    # initialize
    students = ['Connor', 'John', 'Bob', 'Sue']
    gradebook = Gradebook('cs5001', 2022, 'Fall', 'Wilder', students)

    # add grades for assignment 1
    grade_1 = {
        'Connor': 95,
        'John': 100,
        'Bob': 80,
        'Sue': 0
    }

    gradebook.add_grade(grade_1)

    # add grades for assignment 2
    grade_2 = {
        'Connor': 95,
        'John': 80,
        'Bob': 79,
        'Sue': 100,
    }

    gradebook.add_grade(grade_2)

    print(gradebook)