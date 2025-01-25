"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(100)                           # Make the turtle move as fast, but not too fast. 


forwards = [96]
lefts = [99]
colors = ['green, red, orange, yellow, blue, brown' ]

sides = 3
angle = 360 / sides

for i in range(1010):
    if i ==700:
        tina.width(1.5)
        tina.color('orange')
    if i == 600:
        tina.width(1)
        tina.color("brown")
    if i == 500:
        tina.width(0.5)
        tina.color('green')
    if i == 300:
        tina.width(3)
        tina.color("blue")
    if i == 200:
        tina.color("gold")
    tina.forward(i)
    tina.right(angle - 1)

turtle.exitonclick()  

