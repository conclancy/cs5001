import turtle

colors = ['pink', 'red', 'purple', 'blue', 'green', 'teal', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(270):
    t.pencolor(colors[x%8])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(46)