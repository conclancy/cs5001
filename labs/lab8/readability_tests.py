''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 8 - Readability (Test File)
clancy.co@northeastern.edu (002781018)
26 MAR 22 

The file tests the functions from readability.py
'''


from readability import *


def test_flesch_grade():
    '''
    Function: test_flesch_grade
        Tests the flesch_grade function
    Parameters:
        None
    Returns nothing, prints results
    '''

    failed_tests = 0

    # test Law School Score
    if flesch_grade(-1) != "Law school graduate":

        # increment failed_tests
        failed_tests = failed_tests + 1

        # print results for users
        print("Failed test - flesch_grade returned", flesch_grade(-1), 
              ", expected 'Law school graduate'")

    # test College graduate
    if flesch_grade(1) != "College graduate":

        # increment failed_tests
        failed_tests = failed_tests + 1

        # print results for users
        print("Failed test - flesch_grade returned", flesch_grade(1), 
              ", expected 'College graduate'")

    # test college
    if flesch_grade(35) != "College":

        # increment failed_tests
        failed_tests = failed_tests + 1

        # print results for users
        print("Failed test - flesch_grade returned", flesch_grade(35), 
              ", expected 'College'")

    # test High Schooler
    if flesch_grade(52) != "High schooler":

        # increment failed_tests
        failed_tests = failed_tests + 1

        # print results for users
        print("Failed test - flesch_grade returned", flesch_grade(52), 
              ", expected 'High Schooler'")

    # test 8th Grader
    if flesch_grade(67) != "8th Grader":

        # increment failed_tests
        failed_tests = failed_tests + 1

        # print results for users
        print("Failed test - flesch_grade returned", flesch_grade(67), 
              ", expected '8th Grader'")

    # test 7th grader
    if flesch_grade(75) != "7th Grader":

        # increment failed_tests
        failed_tests = failed_tests + 1

        # print results for users
        print("Failed test - flesch_grade returned", flesch_grade(75), 
              ", expected 'Law school graduate'")

    # tet 6th grader
    if flesch_grade(83) != "6th Grader":

        # increment failed_tests
        failed_tests = failed_tests + 1

        # print results for users
        print("Failed test - flesch_grade returned", flesch_grade(83), 
              ", expected '6th Grader'")

    # test 5th grader
    if flesch_grade(100) != "5th Grader":

        # increment failed_tests
        failed_tests = failed_tests + 1

        # print results for users
        print("Failed test - flesch_grade returned", flesch_grade(100), 
              ", expected 'Law school graduate'")

    # final print out 
    if failed_tests == 0: 
        print("All Flesch Grade tests passed")


def test_count_syllables():
    '''
    Function: test_count_syllables
        Tests the count_syllables function
    Parameters:
        None
    Returns nothing, prints results
    '''

    # create test cases and variables
    test_cases = [
        ["life", 1],
        ["alumnae", 3],
        ["me", 1], 
        ["Creighton", 2],
        ["University", 5], 
        ["sea", 1], 
        ["Lincoln's", 2], 
        ["18", 1]]

    failed_tests = 0 

    # iterate over test cases 
    for t in test_cases:
        if count_syllables(t[0]) != t[1]:
            failed_tests = failed_tests + 1
            print(t[0], "returned", count_syllables(t[0]), "expected", t[1])

    # final print out 
    if failed_tests == 0: 
        print("All syllable tests passed")


def test_files():
    '''
    Function: test_files
        Tests the functionily of the main function in the readbility module.
    Parameters:
        None
    Returns nothing, prints results
    '''

    # create test file variables
    test_files = [
        ["college.txt", 31, 15, 1, 16.8, "College graduate"],
        ["sixth-grade.txt", 37, 29, 2, 84.2, "6th Grader"], 
        ["gettysburg.txt", 400, 282, 11, 60.8, "High schooler"]]

    # iterate through test cases
    for file in test_files:
        # Open file for reading.
        input_file = open(file[0], 'r')

        # Read all of the contents of the file
        # into a list of strings called filedata.
        filedata = input_file.readlines()

        sentences, words, syllables = analyze_file_data(filedata)
        index = flesch_index(sentences, words, syllables)
        grade = flesch_grade(index)

        # Test syllables functionality
        if syllables != file[1]: 
            print(file[0], "failed syllables test:", syllables, "expected", 
                  file[1])

        # Test word count functionality
        if words != file[2]: 
            print(file[0], "failed words test:", words, "expected", 
                  file[1])

        # Test sentence count functionality
        if sentences != file[3]: 
            print(file[0], "failed sentences test:", sentences, "expected", 
                  file[1])

        # Test flesch index functionality
        if index != file[4]: 
            print(file[0], "failed index test:", index, "expected", 
                  file[4])

        # Test grade index functionality
        if grade != file[5]: 
            print(file[0], "failed grade test:", grade, "expected", 
                  file[4])

        # Close the file.
        input_file.close()


if __name__ == '__main__':
    '''test functions from readability'''

    test_flesch_grade()
    test_count_syllables()
    test_files()
