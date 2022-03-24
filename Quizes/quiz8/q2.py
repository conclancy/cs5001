def test_integer(number):
    '''
    test_integer prints all integer values and raises a TypeError for inputs
    of all other types.
    param: single integer
    returns: None 
    '''

    if isinstance(number, int):
        print(number)
    else:
        raise TypeError("Number variable must be of type `int`")

test_integer(1.0)