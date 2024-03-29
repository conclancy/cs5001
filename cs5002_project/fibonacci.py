''' 
CS5002 - Prof. Rachlin
Sprint 2022
Semester Project
clancy.co@northeastern.edu (002781018)

The Fibonacci class can be used to generate a list of 'n' Fibonacci numbers
and display the associated Fibonacci spiral. 
'''

from math import pi
from time import sleep
from turtle import Turtle


class Fibonacci():
    '''
    The Fibonacci class can be use to create an artistic drawing of the 
    fibonacci spiral
    attributes:
        digit -- the nth digit in the Fibonacci sequence
        factor -- how big the desired diagram should be 
        square_color -- the color of the square borders; grey by default
        pen_color -- the color of the spiral; red by default 
    methods:
        get_fibonacci -- get the nth Fibonacci number recursively
        draw_squares -- draw the square borders in square_color
        draw_spiral -- draw the spiral in pen_color
        visual -- draws both the squares and spiral
    '''

    def __init__(self, digit, factor = 1, square_color = 'grey', pen_color = 'red'):
        '''contructor for the Fibonacci class'''

        # digit instantiate if is an int greater than 0.
        if isinstance(digit, int):
            if digit > 0:
                self.digit = digit
            else: 
                raise ValueError("digit must be greater than or equal to 1")
        else:
            raise TypeError("digit must be of type int")

        # digit instantiate if is an int greater than 0.
        if isinstance(factor, int):
            if factor > 0:
                self.factor = factor
            else: 
                raise ValueError("factor must be greater than or equal to 1")
        else:
            raise TypeError("factor must be of type int")

        # colors instantiate
        self.square_color = square_color
        self.pen_color = pen_color

        # fibonacci_sequence instantiate
        self.fibonacci_sequence = [self.get_fibonacci(d) for d in range(digit)]

        # create a turtle object 
        self.turtle = Turtle()
        self.turtle.speed(1000)
    
    def get_fibonacci(self, number) -> int:
        '''
        get_fibonacci returns the next number in the fibonacci sequence 
        using recursion.
        params:
            self - the current object
            number - the desired digit in the fibonacci sequence
        returns:
            the next int value in the fibonacci sequence 
        '''

        # base cases
        if number in [0, 1]:
            return number 

        # non-base cases 
        else:
            n = self.get_fibonacci(number - 1) + self.get_fibonacci(number - 2)
            return n

    def draw_squares(self) -> None:
        '''
        draw_square uses the turtle object to draw the square borders 
        params:
            self - the current object
        returns:
            void
        '''

        # set the boarder color for the drawing
        self.turtle.pencolor(self.square_color)
        self.turtle.setposition(self.factor, 0)

        # draw the first square
        self.turtle.forward(1 * self.factor)
        self.turtle.left(90)
        self.turtle.forward(1 * self.factor)
        self.turtle.left(90)
        self.turtle.forward(1 * self.factor)
        self.turtle.left(90)
        self.turtle.forward(1 * self.factor)

        # draw the remaining squares
        for i in range(1, self.digit):

            # set variables 
            previous = self.fibonacci_sequence[i -1]
            current = self.fibonacci_sequence[i]

            # reset the turtle
            self.turtle.backward(previous * self.factor)
            self.turtle.right(90)

            # draw the next square
            self.turtle.forward(current * self.factor)
            self.turtle.right(90)
            self.turtle.forward(current * self.factor)
            self.turtle.right(90)
            self.turtle.forward(current * self.factor)

        # close the square 
        self.turtle.right(90)
        self.turtle.forward(current * self.factor)
        self.turtle.forward(previous * self.factor)
        self.turtle.right(90)
        self.turtle.forward(previous * self.factor)
        self.turtle.forward(self.fibonacci_sequence[-3] * self.factor)
        self.turtle.right(90)
        self.turtle.forward(self.fibonacci_sequence[-3] * self.factor)

    
    def draw_spiral(self) -> None:
        '''
        draw_spiral uses the turtle object to curve within the circles 
        params:
            self - the current object
        returns:
            void
        '''

        # reset the turtle to the starting position
        self.turtle.penup()
        self.turtle.setposition(self.factor, 0)
        self.turtle.setheading(0)
        self.turtle.pendown()

        self.turtle.pencolor(self.pen_color)

        # draw curve
        self.turtle.left(90)
        for i in range(1, self.digit):

            # set current value for drawing the curve
            current = self.fibonacci_sequence[i]

            # caluate the required forward distance 'unit'
            forward = pi * current * self.factor / 2
            forward /= 90

            # for each degree move one 'unit' forward
            for d in range(90):
                self.turtle.forward(forward)
                self.turtle.left(1)


    def visual(self) -> None:
        '''
        visual calls the draw_squares and draw_spiral functions to create
        the complete Fibonacci sequence spiral drawing. 
        params:
            self - the current object
        returns:
            void
        '''

        # draw objects for the visual
        self.draw_squares()
        self.draw_spiral()

        # pause so the user can admire their art work
        sleep(10)


if __name__ == '__main__':
    '''Driver for the Fibonacci'''

    size = int(input("Enter index of the desired fibonacci number: "))
    color = input("Enter the desired spiral color: ")

    # instantiate a Fibonacci object
    fibonacci = Fibonacci(size, pen_color=color)

    # print the Fibonacci sequence
    print(fibonacci.fibonacci_sequence)

    # draw and display the Fibonacci curve
    fibonacci.visual()
