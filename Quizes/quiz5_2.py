'''
This file takes in a list of numbers and returns the largest element
'''


def max_value(integer_list):
    '''
    finds the largest value in a list
    params: list of ints 
    returns: int
    '''

    max_value = integer_list[0]

    for i in integer_list:
        if i > max_value:
            max_value = i

    print(max_value)

def main():
    test = max_value([1,2,3,4,-5])
    print(test)

main()