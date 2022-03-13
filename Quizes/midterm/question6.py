''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Midterm - Question 6
clancy.co@northeastern.edu (002781018)
11 MAR 22 

The file contains a function that returns the month string and the number of
days in the month according given the month number between 1 and 12
'''


def months_and_days(month):
    '''
    months_and_days takes in a month number and returns the month name and
    the number of days in the month. 
    :params int: month number
    :return: a string with the corresponding month name and number of days 
             in the month
    '''

    MONTHS = [
        "January, 31\n",
        "February, 28\n",
        "March, 31\n",
        "April, 30\n",
        "May, 31\n",
        "June, 30\n", 
        "July, 31\n", 
        "August, 31\n",
        "September, 30\n",
        "October, 31\n", 
        "November, 30\n", 
        "December, 31\n"
    ]

    return MONTHS[month - 1]


def main():

    # function variables
    test_outputs = []

    # test each month 
    for i in list(range(1, 13)):
        if i == 1:
            test_outputs.append(months_and_days(i) == "January, 31\n")
        elif i == 2:
            test_outputs.append(months_and_days(i) == "February, 28\n")
        elif i == 3:
            test_outputs.append(months_and_days(i) == "March, 31\n")
        elif i == 4:
            test_outputs.append(months_and_days(i) == "April, 30\n")
        elif i == 5:
            test_outputs.append(months_and_days(i) == "May, 31\n")
        elif i == 6:
            test_outputs.append(months_and_days(i) == "June, 30\n")
        elif i == 7:
            test_outputs.append(months_and_days(i) == "July, 31\n")
        elif i == 8:
            test_outputs.append(months_and_days(i) == "August, 31\n")
        elif i == 9:
            test_outputs.append(months_and_days(i) == "September, 30\n")
        elif i == 10:
            test_outputs.append(months_and_days(i) == "October, 31\n")
        elif i == 11:
            test_outputs.append(months_and_days(i) == "November, 30\n")
        elif i == 12:
            test_outputs.append(months_and_days(i) == "December, 31\n")

    # make the list of elements unique 
    test_outputs = tuple(set(test_outputs))

    # if the only element in the tuple is `True` then all tests passed
    if len(test_outputs) == 1 and test_outputs[0] is True:
        print("All tests passed")
    else:
        print("One or more tests failed")


main()
