import turtle

# instantiate screen and background color
s = turtle.getscreen()
s.bgcolor('black')

# instatiate turtle
t = turtle.Turtle()
t.speed(10)

t.setposition(-300, 300)

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