''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Quiz 10 - Student Class
clancy.co@northeastern.edu (002781018)
06 April 2022

The file contains the student class used for creating student objects with a
name, major, and a list of the classes they have completed.
'''


import re


class Student():
    '''
    Student is a class used to create student objects.
    Attridutes: name, major, class_list
    Methods: add_course
    '''

    def __init__(self, name, primary_major, courses = []):
        '''initalize a Student object'''

        # ensure the name is passed as a string and set name attribute
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("name attribute must be of type str")
        
        # ensure primary_major is a string and set attribute
        if isinstance(primary_major, str):
            self.primary_major = primary_major
        else:
            raise TypeError("primary_major attribute must be of type str")

        # ensure courses is a list and set attribute
        if isinstance(courses, list):
            self.courses = courses
        else:
            raise TypeError("courses attribute must be of type list")


    def add_course(self, course) -> None:
        '''
        Add a class in the form of a string to the Student's course attributes
        params: single str course representing the course the student completed
        returns: void, nothing is returned from this method
        '''

        # ensure the course passed is a string and append it to the courses list
        if isinstance(course, str):
            self.courses.append(course)
        else:
            raise TypeError("course must be of type str")


    def __str__(self) -> str:
        '''
        __str__ method allows the user to print the student object to see the
            student's attributes (name, primary major, course list)
        params: None
        returns: str containing object attributes
        '''

        # concatenate the object's attributes into a single string
        return_string = self.name + ', ' + self.primary_major + ', ' + str(self.courses)

        return return_string



if __name__ == "__main__":
    '''Driver for this program'''

    connor = Student("Connor Clancy", "Computer Science")

    connor.add_course('CS5001')
    connor.add_course('CS5002')

    print(connor)
