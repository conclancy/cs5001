def value_error_function(data):
    '''
    value_error_function prints all numbers less than 1 or greater than 10. 
    All other values raise a Value Error. 
    param: single integer
    returns: null 
    '''

    # raises error if not <1 or >10, else prints the statement
    if data >= 0 and data <=10:
        raise ValueError("Value must be less than 1 or greater than 10")
    else:
        print(data)

def main():
    t = int(input("Please input a number:"))
    value_error_function(t)

main()