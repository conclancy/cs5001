''' 
CS5002 - Prof. Rachlin
Extra Credit Project
clancy.co@northeastern.edu (002781018)
24 APR 22 

# TODO
'''

import turtle

class Fibonacci():
    '''
    The Fibonacci class can be use to create an artistic drawing of the 
    fibonacci spiral
    attributes:
        digit -- the nth digit in the Fibonacci sequence
    methods:
        get_fibonacci -- get the nth Fibonacci number recursively
    '''

    def __init__(self, digit, square_color = 'grey'):
        '''contructor for the Fibonacci class'''

        # digit instantiate if is an int greater than 0.
        if isinstance(digit, int):
            if digit > 0:
                self.digit = digit
            else: 
                raise ValueError("digit must be greater than or equal to 1")
        else:
            raise TypeError("digit must be of type int")

        # fibonacci_sequence instantiate
        self.fibonacci_sequence = [self.get_fibonacci(d) for d in range(digit)]
    
    def get_fibonacci(self, number) -> int:
        '''
        get_fibonacci returns the next number in the fibonacci sequence 
        using recursion.
        params:
            number - the desired digit in the fibonacci sequence
        returns:
            the next value in the fibonacci sequence 
        return type:
            int
        '''

        # base cases
        if number in [0, 1]:
            return number 

        # non-base cases 
        else:
            n = self.get_fibonacci(number - 1) + self.get_fibonacci(number - 2)
            return n


if __name__ == '__main__':
    test = Fibonacci(10)
    print(test.fibonacci_sequence)
