"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.shape("turtle")
# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here
tina.color("green")
tina.forward(45)
tina.left(72)
tina.color("orange")
tina.forward(45)
tina.left(72)
tina.color("red")
tina.forward(50)
tina.left(72)
tina.color("yellow")
tina.forward(50)
tina.left(72)
tina.color("blue")
tina.forward(55)
turtle.exitonclick()                    # Close the window when we click on it
