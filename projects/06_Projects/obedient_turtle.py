"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, question, error
def huh(t):
    t.color("red")
    t.begin_fill()
    t.circle(90)
    t.circle(-90)
    t.color("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(60)   
        t.left(90)
def drawSquare(t):
    for i in range(4): 
        t.forward(150)
        t.left(90) 
def drawTriangle(t):
    for i in range(3):
        t.forward(150)
        t.left(120)
def drawCircle(t):
    t.circle(90)
def specialMeating(t):
    t.color("red")
    t.begin_fill()
    t.circle(90)
    t.circle(-90)
    t.color("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(60)   
        t.left(90)


# TODO)                        # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)
tina = turtle.Turtle()
shape = question("Shape", "What is your shape(huh? :) )")
if shape == 'square':
    drawSquare(tina)
    print("?","siddy cakes")
if shape == 'triangle':
    drawTriangle(tina)
if shape == 'circle':
    drawCircle(tina)
if shape == 'fish':
    fishy = question("whats da secret password", "NOW")
    if fishy == "dont trust fish":
        for i in range(67):
            huh(tina)
            shape == 'huh?'
        question("U are an idiot lalalalalala", "heheheha")
    specialMeating(tina)
if shape == "huh?":
    huh(tina)
    what = question("WHY DID U DO THIS", "NOW U ARE THIS(HEHEHEHEHEHEHE)huh?")
    if what == 'hahaha':
        question("U are an idiot lalalalalala", "heheheha")

#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.

#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
pass
turtle.exitonclick()     
turtle.done()