"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

import turtle

turtle.setup(width=600, height=600)
tina = turtle.Turtle()
tina.shape("turtle")
while True:
    tina.goto(300, 300)
    tina.goto(300, -300)
    tina.goto(-300, -300)
    tina.goto(-300, 300)
    tina.goto(300, 300)
turtle.exitonclick()
