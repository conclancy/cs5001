''' CS5001.38359.202230 - SEC 05 - John Wilder
    Midterm - Question 1
    clancy.co@northeastern.edu (002781018)
    11 MAR 22 

    The file contains a function that orders a list of values from smallest
    to largest.
'''


def order_list(input_list):
    '''
    Takes in a list of numbers and orders them from smallest to largest
    param: single list of numbers
    return: single list with the same elements as the input list but ordered
            from smallest to largest
    '''

    new_list = []
    for item in input_list:
        if len(new_list) == 0:
            new_list.append(item)
        else:
            index = 0
            while index < len(new_list):
                if item <= new_list[index]:
                    break
                index += 1
            new_list.insert(index, item)
    return new_list
