''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 5 - Spirals
clancy.co@northeastern.edu (002781018)
19 MAR 22 

The file contains a code to draw a set of shapes using the turtles library. 
The main function in this file draws a house, a rainbow, and a sun using the
other declared functions.
'''


import time
import turtle


def make_angle_list(sides, starting_angle=0): 
    '''
    make_angle_list takes in the number of sides we desire for a given shape
    and starting ange and returns a list of angles required for the turtle 
    setheading() function to guide the turtle through shape building.
    params: two ints, the number of sides of the shape, starting angle
    returns: list of angles
    '''

    # declare function variables
    angle_list = []
    a = 0

    # get degrees for a regular version of this shape
    degrees = round(360 / sides, 4)

    # cleate a list of angles until we have complete 360 degrees of angle work
    while a < 360: 
        starting_angle = round(starting_angle + degrees, 4)
        angle_list.append(starting_angle)
        a = a + degrees

    return angle_list


def make_polygon(turtle, sides, size, color, angle=0, x_cor=0, y_cor=0):
    '''
    make_polygon takes in a turtle object and additional parameters describing
    a regular polygon with equal side lengths and angles.
    params: turtle object
        sides int describing how many sides make up the polygon
        size int describes how long the sides will be 
        color string describing the color of the polygon
        angle int describes the starting angle of the turtle
        x_cor int describing the starting x cordinate 
        y_cor in describing the starting y cordinate
    returns: None
    '''

    # set turtle object variables
    turtle.width(5)
    turtle.setposition(x_cor, y_cor)

    # sets the turle's "pen" down for drawing
    turtle.down()

    # calls angle_list function to get a list of angles
    angle_list = make_angle_list(sides) 

    # set the intitial turtle angle
    turtle.setheading(angle)

    # for each angle in list, create a side and set next angle
    for a in angle_list:
        turtle.color(color)
        turtle.forward(size)
        turtle.setheading(a)

    # pick up the tutrle's "pen" so it does not draw on its way to next shape
    turtle.up()


def make_circle(turtle, radius, color, angle=360, x_cor=0, y_cor=0):
    '''
    make_circle takes in a turtle and characteristics describing a circle
    (or a portion there of) and draws the shape on the screen.
    params:
        turtle object
        radius int for the radius of the circle
        color str for the color of the drawn circle
        angle int for the starting angel.  Defaults to 360. 
        x_cor int for the starting x cordinate of the circle
        y_cor int for the starting y cordinate of the circle
    returns: None
    '''

    # set circle color
    turtle.color(color)

    # move turtle, putting down and picking up to prevent unitented drawing
    turtle.up()
    turtle.setpos(x_cor, y_cor)
    turtle.down()

    # draw a circle
    turtle.right(180)
    turtle.circle(radius, angle)


def make_sun(turtle, x_cor, y_cor):
    '''
    make_sun takes in a turtle object and the center cordinates and draws
    a yellow and orange sun object.
    params:
        turtle object
        x_cor int for center of the sun x cordinate 
        y cor int for center of the sun y cordinate
    return: None
    '''

    # set turtle variables
    turtle.width(1)
    turtle.setposition(x_cor, y_cor)

    # sets the turle's "pen" down for drawing
    turtle.down()

    # create 10 rhombuses that will form the sun
    for i in range(10):

        # alternate between yellow and orange 
        if i % 2 == 0:
            color = 'orange'
        else:
            color = "yellow"

        # create the rhombus two shapes at a time
        for i in range(2):
            t.color(color)
            t.forward(50)
            t.right(60)
            t.forward(50)
            t.right(120)

        # turn the turtle right 36 degree (360 /10 rhombuses)
        t.right(36)

    # pick up the tutrle's "pen" so it does not draw on its way to next shape
    turtle.up()


if __name__ == "__main__":

    # instantiate screen and background color
    s = turtle.getscreen()
    s.bgcolor('black')

    # instatiate turtle
    t = turtle.Turtle()
    t.speed(20)
    t.up()

    # make house 
    make_polygon(t, 4, 75, "grey", 0, 150, -50)
    make_polygon(t, 3, 85, "grey", 0, 145, 25)

    # make sun
    make_sun(t, -300, 300)

    # make rainbow
    colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    t.right(-90)
    t.width(5)

    for c in range(7):
        make_circle(t, 30 * (c + 8), colors[c], -180, -30 * (c + 1), -60)

    # pause to admire the picture before it is closed
    time.sleep(5)
