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
    '''

    def __init__(self, digit):
        '''contructor for the Fibonacci class'''

        if isinstance(digit, int):
            if digit > 0:
                self.digit = digit
            else: 
                raise ValueError("digit must be greater than or equal to 1")
        else:
            raise TypeError("digit must be of type int")

        self.digits = [self.get_fibonacci(d) for d in range(digit)]
    
    def get_fibonacci(self, number):
        '''
        get fibonacci
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
    print(test.digits)
