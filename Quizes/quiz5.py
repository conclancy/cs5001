'''
This file takes in 5 numbers as inputs, sums them up, and prints 
the total to the screen. 
'''


def sum_list(number_list):
    '''
    sums a list of integers 
    params: list of ints
    returns: int
    '''
    
    list_sum = sum(number_list)
    return list_sum


def main():

    # receive inputs 
    element1 = int(input("Input first integer: "))
    element2 = int(input("Input first integer: "))
    element3 = int(input("Input first integer: "))
    element4 = int(input("Input first integer: "))
    element5 = int(input("Input first integer: "))

    # create list and sum
    number_list = [element1, element2, element3, element4, element5]
    list_sum = sum_list(number_list)
    
    print(list_sum)


main()
