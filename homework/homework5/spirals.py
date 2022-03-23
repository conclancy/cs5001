''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Homework 5 - Spirals
clancy.co@northeastern.edu (002781018)
19 MAR 22 

The file contains a code to draw a set of shapes using the turtles library
'''


import time
import turtle


def make_angle_list(sides, starting_angle = 0): 
    angle_list = []
    a = 0

    degrees = round(360 / sides, 4)

    while a < 360: 
        starting_angle = round(starting_angle + degrees, 4)
        angle_list.append(starting_angle)
        a = a + degrees

    return  angle_list


def make_polygon(turtle, sides, size, color, angle = 0, x_cor = 0, y_cor = 0):
    
    turtle.width(5)
    turtle.setposition(x_cor, y_cor)

    turtle.down()

    angle_list = make_angle_list(sides) 
    print(angle_list)

    turtle.setheading(angle)
 
    for a in angle_list:
        turtle.color(color)
        turtle.forward(size)
        turtle.setheading(a)
    
    turtle.up()


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

    turtle.width(1)
    turtle.setposition(x_cordinate, y_cordinate)

    turtle.down()

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

    # make sun
    make_sun(t, -300, 300)

    # make rainbow
    colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    t.right(-90)
    t.width(5)

    for c in range(7):
        make_circle(t, 30 * (c + 8), colors[c], -180, -30 * (c + 1))
    
    time.sleep(5)
