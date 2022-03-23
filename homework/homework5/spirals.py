''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 5 - Spirals
clancy.co@northeastern.edu (002781018)
19 MAR 22 

The file contains a code to draw a set of shapes using the turtles library
'''

import random
import time
import turtle


def make_angle_list(degrees, starting_angle = 0): 
    angle_list = []
    a = 0

    degrees = round(360 / degrees, 4)

    while a < 360: 
        starting_angle = round(starting_angle + degrees, 4)
        angle_list.append(starting_angle)
        a = a + degrees

    return  angle_list

def make_polygon(turtle, sides, size, color, starting_angle = 0):
    # COLOR_LIST = ['red', 'blue', 'purple', 'pink']

    equal_angles = round(360 / sides, 4)

    angle_list = make_angle_list(equal_angles) 

    a = 0

    while a < 360: 
        starting_angle = round(starting_angle + equal_angles, 4)
        angle_list.append(starting_angle)
        a = a + equal_angles

    turtle.setheading(starting_angle)

    for i in angle_list:
        turtle.color(color)
        turtle.forward(size)
        turtle.setheading(i)


def make_circle(turtle, radius, color, angle = 360, position = 0):

    # set circle color
    turtle.color(color)

    # move turtle
    turtle.up()
    turtle.setpos(position, -60)
    turtle.down()

    # draw a circle
    turtle.right(180)
    turtle.circle(radius, angle)


def make_sun(turtle, x_cordinate, y_cordinate):
    turtle.setposition(x_cordinate, y_cordinate)

    for i in range(10):

        if i % 2 == 0:
            color = 'orange'
        else:
            color = "yellow"

        for i in range(2):
            t.color(color)
            t.forward(50)
            t.right(60)
            t.forward(50)
            t.right(120)
        
        t.right(36)


if __name__ == "__main__":
    
    # instantiate screen and background color
    s = turtle.getscreen()
    s.bgcolor('black')

    # instatiate turtle
    t = turtle.Turtle()
    t.speed(999)

    '''
    for i in make_angle_list(10):
        # random.randint(0, 3)
        make_polygon(t, 4, 100, 'red', i)

    for i in make_angle_list(30):
        # random.randint(0, 3)
        make_polygon(t, 3, 150, 'blue', i)
    '''
    # make sun
    make_sun(t, -300, 300)

    colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    t.right(-90)
    t.width(5)

    for c in range(7):
        make_circle(t, 30 * (c + 8), colors[c], -180, -30 * (c + 1))
    
    time.sleep(10)