"""
Pentagon Crazy

This program already works. Run it, then change it to make it draw a different pattern.
"""

import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600, startx=0, starty=0)

colors = ("red", "blue", "green", "yellow", "orange", "purple", "violet", "white", "black","blue", "magenta", "light blue", "maroon", "light green", "gold")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(100000000)
myTurtle.width(9)

sides = 0.000000002
angle = 5 / sides

for i in range(3600000000000):
    if i == 300:
        myTurtle.width(6)
    if i == 200:
        myTurtle.width(3)
    myTurtle.pencolor(getNextColor(i))
    myTurtle.forward(i)
    myTurtle.right(angle - 1)

myTurtle.hideturtle()

turtle.done()
